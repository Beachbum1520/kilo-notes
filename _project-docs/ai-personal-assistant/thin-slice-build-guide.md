# Thin Slice — Build Guide

**Goal:** a working personal AI assistant over your own notes, reachable from your phone, built by you.

**Secondary goal, and the more important one:** understand retrieval systems well enough to judge them, specify them, and eventually deploy them in an operating business.

**Time:** roughly 20–25 hours. No deadline. Stage boundaries are natural stopping points.

---

## Tooling

**Use Claude Code for this build.** It's included in your Max plan, it's repo-native, and it operates at the architecture level rather than line-completion level — which is what you want when the point is understanding what you built. Cursor stays where it is for the WattsWay app; these are different tools for different jobs, not a replacement.

**Use Python.** Better libraries for text processing and embeddings, and the skills transfer directly to data work you might do on the business side later. Node would also work; this guide assumes Python.

**One rule that matters more than any other:** let Claude Code write the plumbing, but *you* write and understand the retrieval query. That query is the transferable skill. Everything else is boilerplate you'll never think about again.

---

## Stage 0 — Groundwork

**~2 hours**

Accounts and tools:

- Supabase account, new project (free tier). Note the connection string and the `service_role` key.
- Voyage AI account. Free tier covers everything here.
- Anthropic API key (separate from your Claude subscription — this is API billing).
- Python 3.11+, a virtualenv, and Claude Code installed.
- A new **private** GitHub repo for the assistant code.
- A second **private** GitHub repo for your notes. Empty for now.

**Homework before Stage 2 — do this in the background:**

Write 25–40 markdown notes into the notes repo. Pull them from your existing Claude projects: decisions you've made, constraints, conclusions from long threads, things you ruled out and why. One topic per file. Put them in folders by domain.

This is not busywork. It's the corpus, and writing it will teach you more about what's worth retaining than any amount of architecture. It's also independently valuable — those decisions currently exist only inside chat threads you can't search.

**Done when:** you can connect to Supabase from a Python script and print the Postgres version.

---

## Stage 1 — One vector, end to end

**~2 hours**

The smallest thing that demonstrates the whole idea.

**What you're learning:** what an embedding actually is, and what "similar" means mathematically.

Enable the extension and make a toy table:

```sql
create extension if not exists vector;

create table toy (
  id      bigserial primary key,
  content text,
  embedding vector(1024)
);
```

Then, by hand — don't delegate this one:

1. Send three sentences to Voyage's embed endpoint. Print the raw response. Look at it. It's a list of 1024 floating point numbers.
2. Insert all three with their vectors.
3. Embed a fourth sentence that means something similar to one of them but shares no words with it.
4. Query: `select content, embedding <=> :query_vec as distance from toy order by distance limit 3;`

**The moment worth pausing on:** your query matched a sentence with no words in common. That is the entire premise of the system, and seeing it work once makes every later decision make sense.

**Then break it deliberately.** Embed a fabricated brand name — something like "Marquette Ridge Holdings" — put it in one of the sentences, and search for it. Watch semantic search do a mediocre job on an exact string. That failure is why Stage 3 exists.

**Done when:** you've seen both the success and the failure with your own eyes.

---

## Stage 2 — Ingest the notes repo

**~4 hours**

**What you're learning:** chunking is where retrieval quality is won or lost. Most people skip this and never understand why their system feels stupid.

Schema (Claude Code can generate the rest of the migration):

```sql
create table sources (
  id           uuid primary key default gen_random_uuid(),
  path         text not null unique,
  title        text not null,
  project      text not null,
  content_hash text not null,
  indexed_at   timestamptz
);

create table chunks (
  id        bigserial primary key,
  source_id uuid references sources(id) on delete cascade,
  ordinal   int,
  content   text not null,
  embedding vector(1024) not null,
  fts       tsvector generated always as (to_tsvector('english', content)) stored
);

create index on chunks using hnsw (embedding vector_cosine_ops);
create index on chunks using gin (fts);
```

Write an ingest script that walks the notes repo, and get these three things right:

1. **Split on markdown headings first**, then paragraphs. Never mid-sentence.
2. **Prepend the file title and folder path to each chunk before embedding.** A chunk reading "we decided against it because of latency" is meaningless alone; with "Business Ops / Vendor Selection" prepended it's retrievable.
3. **Hash the file content.** Unchanged files skip re-embedding. This is what makes re-runs cheap.

**Experiment worth running:** ingest once at 400-token chunks, once at 1200. Query both. The difference in answer quality is the lesson.

**Done when:** the whole repo is indexed, and re-running the script performs zero embedding calls.

---

## Stage 3 — Hybrid search

**~3 hours**

**What you're learning:** why production retrieval systems combine two search methods, and how to fuse ranked lists. This is the most commercially transferable thing in the guide.

Write this one yourself. Type it out, don't paste it.

```sql
create or replace function search_chunks(
  q_text text,
  q_vec  vector(1024),
  n      int default 10
) returns table (content text, score float)
language sql stable as $$
with vec as (
  select id, content,
         row_number() over (order by embedding <=> q_vec) as rank
  from chunks
  order by embedding <=> q_vec
  limit n * 2
),
kw as (
  select id, content,
         row_number() over (
           order by ts_rank_cd(fts, websearch_to_tsquery('english', q_text)) desc
         ) as rank
  from chunks
  where fts @@ websearch_to_tsquery('english', q_text)
  limit n * 2
)
select coalesce(vec.content, kw.content),
       coalesce(1.0/(60 + vec.rank), 0.0) + coalesce(1.0/(60 + kw.rank), 0.0)
from vec full outer join kw on vec.id = kw.id
order by 2 desc
limit n;
$$;
```

**Understand these three things before moving on:**

- `<=>` is cosine distance. Smaller is closer.
- The two branches produce independent *rankings*, not comparable scores. Fusing raw scores from different systems is meaningless — this is why the formula uses rank position.
- `1.0/(60 + rank)` is Reciprocal Rank Fusion. The 60 is a damping constant that keeps any single first-place result from dominating. Change it to 5 and re-run to see what it does.

**Done when:** the fabricated brand name from Stage 1 comes back in the top 3, and a purely conceptual query still works.

---

## Stage 4 — Answers, not results

**~3 hours**

**What you're learning:** prompt assembly and context budgeting — the difference between a search box and an assistant.

The loop:

1. Take the question. Embed it.
2. Retrieve top 10 chunks.
3. Assemble a prompt: system instructions, then retrieved chunks with their source paths, then the question.
4. Call the Claude API. Return the answer with sources listed.

**What to try, because it teaches the most:**

- Ask a question with **no** retrieval. Then with retrieval. Same model, same question. The delta is the entire value of the system.
- Feed it 3 chunks, then 20. More is not better — irrelevant context actively degrades answers. Finding where that turns is a real skill.
- Add "if the provided context doesn't answer the question, say so" to the system prompt. Watch the failure mode change from confident invention to honest gaps.

**Done when:** you ask something spanning two domains and get an answer that draws on both.

---

## Stage 5 — Telegram

**~3 hours**

**What you're learning:** long-polling, and why an allowlist is the first thing you build rather than the last.

- Register a bot with BotFather. You get a token.
- Use `python-telegram-bot`. Long-polling, not webhooks — no public URL required, no timeout ceiling.
- **First code you write in this stage:** reject any message whose `from_user.id` isn't yours. Hard-coded. Before anything else works.
- Split outbound messages over 4096 characters on paragraph boundaries.
- Show a typing indicator while processing.

**Done when:** you ask a question from your phone, on the couch, and get an answer from your own notes.

That moment is the payoff for Stages 0–4. Enjoy it before continuing.

---

## Stage 6 — Deploy

**~2 hours**

**What you're learning:** environment separation and secret handling. Boring, and the boring parts are where systems leak.

- New Railway project, connected to the repo.
- Every secret as an environment variable. Nothing in the repo, ever. Add `.env` to `.gitignore` before your first commit, not after.
- Confirm the process restarts cleanly.
- Set the spend cap on your Anthropic key now — $300 hard, $150 alert. Do it before you forget.

**Done when:** your laptop is closed and the bot still answers.

---

## Stage 7 — Evaluation

**~3 hours**

**Do not skip this stage.** It is the most valuable one in the guide and the one everybody skips.

**What you're learning:** how to know whether a retrieval system actually works. This is the skill that lets you evaluate a vendor, a contractor, or an internal build — and the reason most enterprise RAG projects disappoint is that nobody did it.

1. Write 20 questions you'd genuinely ask your notes.
2. For each, note by hand which file *should* be the top result.
3. Write a script that runs all 20 and reports how often the correct file appears in the top 3. That number is **recall@3**.
4. Record the baseline.
5. Change one thing — chunk size, the RRF constant, whether titles are prepended, top-k. Re-run. Compare.

**The lesson:** you now have a number instead of an opinion. Every retrieval improvement from here is measurable. When someone tells you their AI search is good, you know exactly what question to ask them.

**Done when:** you have a baseline recall@3 and have moved it with at least one deliberate change.

---

## What you'll have

- Cross-domain retrieval over your own notes, from your phone, with no caps
- A working system you understand line by line
- Roughly 60% of the full specification's value
- The knowledge to judge whether a contractor's work on the remaining 40% is any good

## What's deliberately left out

Google Drive sync, Workspace format export, OCR, image handling, the extraction pipeline, the isolated job-search store, write-back.

These are the slog. They're also the parts where you learn the least per hour. Hire them out, or take them on later — but only after the thin slice has been running long enough to prove you use it.

---

## A note on why this is worth the hours

You run an operation with a hundred-plus people supporting hotel brands, where the recurring problem is that knowledge lives in people's heads and long threads nobody can search. That is precisely the problem this architecture solves.

Building it once at personal scale — where the stakes are low, the corpus is yours, and a bad answer costs nothing — is a cheap way to develop judgment about a class of system your industry is going to spend a great deal of money on over the next few years. Most executives evaluating these systems have never built one. After Stage 7, you'll be able to ask a vendor what their recall is and know what to do with the answer.

---

*Companion documents: `personal-ai-assistant-spec.md` (full build spec) and `hiring-kit.md` (sourcing the remaining 40%).*
