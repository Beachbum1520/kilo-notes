# Personal AI Assistant — Build Specification

**Version:** 1.0
**Owner:** Scott Watts
**Status:** Ready for contractor scoping

---

## 1. Purpose

Build a private, single-user AI assistant that maintains one unified memory across all of the owner's domains, accessible from a phone, with no artificial caps on document count or context retention.

The problem being solved: existing consumer AI products isolate context into containers. Navigating those containers requires narrow scoping, but useful reasoning requires cross-cutting visibility. This system separates the two by making hierarchy **metadata**, not walls.

### Success criteria

The build is successful when the owner can:

1. Ask a question from a phone messaging app and get an answer informed by any prior conversation, document, or decision, regardless of which domain it came from.
2. Scope a query to one domain when desired (`"in fitness only, …"`).
3. Have a decision made in one domain surface automatically when relevant to another.
4. Add, update, and remove source documents through normal file tools, with the index following automatically.
5. Run a long working session without a context ceiling forcing a lossy restart.
6. Trust that a decision recorded last month is reported back accurately, including decisions to *reject* an approach.

---

## 2. Architecture

```
Telegram  ──►  Railway (persistent Node/Python process)
                    │
                    ├──►  Claude API          (reasoning)
                    ├──►  Embedding API       (vectors)
                    └──►  Supabase Postgres   (pgvector + full-text index)
                              ▲
                              │  sync
                    ┌─────────┴─────────┐
              Google Drive          GitHub repo
              (files, PDFs,         (markdown notes,
               sheets, images)       decisions, logs)
```

**Systems of record:** Google Drive and GitHub. These hold canonical content. They are human-navigable, editable without the assistant, and survive the assistant being decommissioned.

**Index:** Supabase. Derived, disposable, rebuildable from source at any time. Never the only copy of anything.

This separation is non-negotiable. If the index becomes the only home for content, the system becomes a lock-in trap.

---

## 3. Components and accounts

| Component | Choice | Notes |
|---|---|---|
| Messaging interface | Telegram Bot API | Free, official, no business verification. Long-polling, not webhooks. |
| Runtime | Railway | Persistent process. Render or Fly.io acceptable substitutes. |
| Database + vector index | Supabase (Postgres + pgvector) | **New project, separate from the WattsWay app project.** Prod on Pro tier — free tier has no point-in-time recovery and pauses after 7 days idle. Contractor dev environment runs on free tier. |
| Reasoning model | Anthropic Claude API | Opus / Sonnet / Haiku, routed by task — see §9. |
| Embeddings | Voyage AI `voyage-4` (1024 dim) | Resolved — see §15. Matryoshka dimensions available (256/512/1024/2048). |
| File store | Google Drive | Single root folder, service-account access. |
| Notes store | GitHub | **Private repo, separate from the WattsWay app repo.** |

---

## 4. Data model

### 4.1 Core tables

```sql
create extension if not exists vector;
create extension if not exists pg_trgm;

-- Canonical source objects (1 row per Drive file or repo file)
create table sources (
  id            uuid primary key default gen_random_uuid(),
  backend       text not null check (backend in ('drive','github','upload')),
  external_id   text not null,              -- Drive fileId or repo path
  title         text not null,
  path          text not null,              -- folder path / repo path
  project       text not null,              -- top-level tag
  subproject    text,                       -- optional second level
  mime_type     text,
  content_hash  text not null,              -- skip re-embed when unchanged
  last_modified timestamptz not null,
  indexed_at    timestamptz,
  deleted_at    timestamptz,                -- soft delete / tombstone
  unique (backend, external_id)
);

-- Embedded chunks (many per source)
create table chunks (
  id          bigserial primary key,
  source_id   uuid not null references sources(id) on delete cascade,
  ordinal     int  not null,
  content     text not null,
  embedding   vector(1024) not null,
  fts         tsvector generated always as (to_tsvector('english', content)) stored,
  token_count int,
  created_at  timestamptz not null default now()
);

-- Extracted durable facts (the curated layer — see §7)
create table notes (
  id          uuid primary key default gen_random_uuid(),
  kind        text not null check (kind in
                ('decision','constraint','preference','number','correction','rejected')),
  content     text not null,
  rationale   text,
  project     text not null,
  subproject  text,
  confidence  text not null default 'stated'
                check (confidence in ('stated','implied')),
  source_ref  text,                          -- conversation id or file
  superseded_by uuid references notes(id),
  embedding   vector(1024) not null,
  fts         tsvector generated always as (to_tsvector('english', content)) stored,
  created_at  timestamptz not null default now()
);

-- Raw conversation archive
create table messages (
  id           bigserial primary key,
  thread_id    text not null,
  role         text not null check (role in ('user','assistant')),
  content      text not null,
  project      text,
  has_media    boolean not null default false,
  embedding    vector(1024),
  fts          tsvector generated always as (to_tsvector('english', content)) stored,
  created_at   timestamptz not null default now()
);
```

### 4.2 Indexes

```sql
create index on chunks   using hnsw (embedding vector_cosine_ops);
create index on notes    using hnsw (embedding vector_cosine_ops);
create index on messages using hnsw (embedding vector_cosine_ops);

create index on chunks   using gin (fts);
create index on notes    using gin (fts);
create index on messages using gin (fts);

create index on sources (project, subproject) where deleted_at is null;
create index on notes   (project, kind) where superseded_by is null;
```

### 4.3 Tag taxonomy

Tags derive automatically from folder path (Drive) or directory path (GitHub). Initial taxonomy:

| project | subproject values |
|---|---|
| `business-ops` | `manila-sales`, `call-center`, `hotel-brands`, `vendors` |
| `job-search` | — |
| `cloudstaff-venture` | — |
| `farms` | `livestock`, `sales`, `equipment` |
| `wattsway-app` | `features`, `infrastructure` |
| `fitness` | `training`, `labs`, `nutrition` |
| `home` | `pool`, `concrete`, `office`, `network` |

Adding a folder adds a tag. No schema change required. Depth beyond two levels is stored in `path` and searchable, but not used for filtering.

### 4.4 Isolation of `job-search`

`job-search` content must not share a database with `business-ops`. A `WHERE` clause is a policy, not a boundary — one bug, one missing filter, one contractor query and the separation is gone.

**Implementation: a second Supabase project.**

| | Primary store | Isolated store |
|---|---|---|
| Contains | `business-ops`, `farms`, `wattsway-app`, `fitness`, `home`, `cloudstaff-venture` | `job-search` only |
| Tier | Pro | Free (low volume) |
| Schema | As specified above | Identical |
| Credentials | Prod key set A | Prod key set B |

The runtime holds both connections. Query routing:

- Default queries hit the **primary store only**.
- `job-search` is reachable only when explicitly scoped: `/scope job-search`.
- **No query ever spans both stores.** Cross-store retrieval is not a feature to be disabled later; it must not be implemented.
- The extraction pipeline writes to whichever store the active scope points at.

This is a physical boundary. It survives bad code, and it means a full dump of the primary store contains nothing about the job search.

Corresponding Drive and GitHub separation: `job-search` gets its own root folder (separate service account) and its own private repo.

---

## 5. Ingest and sync

### 5.1 Google Drive

- Access via **service account**, granted to **one root folder only**. The assistant must not be able to enumerate the rest of the owner's Drive.
- Poll the Drive `changes` feed on an interval (default: 5 minutes) using a stored `startPageToken`.
- For each changed file: compare `content_hash`; skip if unchanged.
- **Google Workspace formats require export before processing:**
  - Google Docs → `text/markdown`
  - Google Sheets → `text/csv` per tab
  - Google Slides → `text/plain`
- PDFs → text extraction; fall back to OCR when the text layer is empty.
- Images → vision pass via Claude to produce a text description, which is what gets embedded.
- Deletion in Drive sets `sources.deleted_at` and removes chunk rows. Chunks are never orphaned.

### 5.2 GitHub

- Private repo, markdown only.
- Webhook on push, or poll if webhook setup is deferred.
- Directory path maps to `project` / `subproject`.
- Commit SHA stored in `sources.content_hash`.

### 5.3 Ad-hoc uploads

Files sent directly to the Telegram bot are written to a Drive `_inbox` folder under the root, then picked up by the normal Drive sync. **No content enters the index without a home in a system of record.**

### 5.4 Chunking

- Target 800 tokens, 100-token overlap.
- Split on markdown headings first, then paragraphs, then sentences. Never mid-sentence.
- Prepend each chunk with `title` and `path` before embedding — materially improves retrieval on short chunks.

---

## 6. Retrieval

Hybrid search using Reciprocal Rank Fusion. **Vector-only retrieval is not acceptable** — it fails on exact strings such as brand names, SKUs, lab markers, and proper nouns.

```sql
create or replace function search_memory(
  query_text   text,
  query_vec    vector(1024),
  filter_project text default null,
  match_count  int default 20
) returns table (
  id bigint, content text, source_kind text, score float
) language sql stable as $$
with vec as (
  select c.id, c.content, 'chunk'::text as source_kind,
         row_number() over (order by c.embedding <=> query_vec) as rank
  from chunks c
  join sources s on s.id = c.source_id
  where s.deleted_at is null
    and (filter_project is null or s.project = filter_project)
  order by c.embedding <=> query_vec
  limit match_count * 2
),
kw as (
  select c.id, c.content, 'chunk'::text as source_kind,
         row_number() over (
           order by ts_rank_cd(c.fts, websearch_to_tsquery('english', query_text)) desc
         ) as rank
  from chunks c
  join sources s on s.id = c.source_id
  where c.fts @@ websearch_to_tsquery('english', query_text)
    and s.deleted_at is null
    and (filter_project is null or s.project = filter_project)
  limit match_count * 2
)
select coalesce(vec.id, kw.id),
       coalesce(vec.content, kw.content),
       coalesce(vec.source_kind, kw.source_kind),
       coalesce(1.0 / (60 + vec.rank), 0.0)
     + coalesce(1.0 / (60 + kw.rank), 0.0) as score
from vec full outer join kw on vec.id = kw.id
order by score desc
limit match_count;
$$;
```

An equivalent function runs against `notes` and `messages`.

### 6.1 Retrieval tiering

Results are assembled in this priority order:

1. **`notes`** — curated durable facts. Always searched. Highest weight.
2. **`chunks`** — document content. Always searched.
3. **`messages`** — raw transcript archive. Searched only when tiers 1 and 2 return fewer than 5 results above threshold.

Rationale: raw transcript is mostly conversational scaffolding. Ranking it equally with curated notes drowns the signal the extraction pipeline exists to produce.

### 6.2 Scoping

Natural-language scope hints (`"in fitness only"`, `"just business ops"`) resolve to a `filter_project` value. Default is unfiltered — cross-domain search is the point of the system.

---

## 7. Extraction pipeline

**This is the component that determines whether the system feels intelligent. It is not optional and must not be descoped.**

After each exchange, a second model call (Haiku — cost is negligible) evaluates the turn and writes zero or more rows to `notes`.

### 7.1 Capture rules

**Capture:**
- Decisions made, with rationale
- Constraints stated
- Specific numbers, figures, and targets the owner supplied
- Corrections to previously recorded facts
- Stated preferences about tools, process, or output
- **Approaches evaluated and rejected, with the reason** — `kind = 'rejected'`

**Do not capture:**
- Open questions, transient state, or scheduling detail
- The assistant's own suggestions, recommendations, or drafts
- Anything the owner did not explicitly adopt

### 7.2 The critical rule

> An option the assistant proposed is **not** a decision the owner made, even if the owner engaged with it positively. Only an explicit adoption ("yes, do that", "we're going with X") produces a `decision` note.

Violating this rule causes the assistant to later assert the owner's position incorrectly. This has already occurred in practice and is the single most damaging failure mode of the system.

### 7.3 Rejected decisions

`kind = 'rejected'` is the highest-value record type and the one most likely to be lost by naive summarization. It is what prevents re-litigating settled questions. Retrieval must surface a matching `rejected` note whenever the assistant is about to recommend that same approach.

### 7.4 Supersession

When a new note contradicts an existing one, set `superseded_by` on the old row rather than deleting it. History is retained; only current notes are retrieved by default.

### 7.5 External capture

Conversations that occur outside this system need a path in:

- **Claude Code / Cursor:** a session-end script runs extraction over the git diff plus session notes and commits results to the notes repo. Automatic.
- **Other chat products:** the owner forwards the thread to the bot; extraction runs on paste. One action.
- **Bulk backfill:** periodic Claude.ai data export, processed through the same pipeline.

### 7.6 Weekly review

Every Sunday the bot posts everything written to `notes` in the past week. The owner confirms or corrects inline. Corrections write a `correction` note and set `superseded_by`.

Without this loop, extraction errors compound silently.

---

## 8. Telegram interface

- **Long-polling**, not webhooks. No public endpoint, no signature verification, no timeout envelope.
- **Access control: allowlist by Telegram user ID.** Any message from an unlisted ID is discarded silently. Without this, anyone who finds the bot has full read access to the memory store. This is a hard requirement.
- Inbound images accepted and routed through the vision pass (§5.1).
- Inbound voice notes transcribed before processing.
- Outbound messages exceeding Telegram's 4096-character limit split on paragraph boundaries, or delivered as a `.md` file attachment when longer than ~3 messages.
- Typing indicator during processing. Multi-minute operations post a progress line.
- Commands: `/scope <project>`, `/unscope`, `/note <text>` (manual note capture), `/forget <note-id>`, `/review`.

---

## 9. Model routing and prompts

| Task | Model | Rationale |
|---|---|---|
| Primary reasoning | Claude Opus | Quality where it matters |
| Routine queries, summarization | Claude Sonnet | Cost/latency balance |
| Extraction, classification, scope detection | Claude Haiku | High volume, low complexity |
| Image description | Claude Sonnet (vision) | — |

### 9.1 System prompt requirements

The system prompt is owner-authored and version-controlled in the notes repo. It must establish:

- Direct, analytical register. No hedging, no restating the question, no unsolicited caveats.
- Explicit statement that the owner retains professional advisors for medical, legal, and financial decisions, and is not seeking advice in those capacities — educational and mechanistic explanation is the expected mode.
- Instruction to check `notes` for `kind = 'rejected'` before recommending an approach.
- Instruction to distinguish, when reporting prior context, between what the owner decided and what the assistant previously suggested.

---

## 10. Security and access control

| Control | Requirement |
|---|---|
| Telegram access | User-ID allowlist. Non-negotiable. |
| Drive scope | Service account, single root folder. No broad Drive scope. |
| Drive deletes | Assistant moves to `_archive`. Hard delete is a human action only. |
| Secrets | Railway environment variables. Never committed. |
| Logging | **No prompt or response bodies in application logs.** Log request IDs, latency, token counts, and errors only. |
| Database | Supabase Pro tier for point-in-time recovery. Daily backup verified restorable at least once. |
| Transport | TLS everywhere. No plaintext egress. |
| Spend controls | Hard monthly ceiling on the Anthropic API key. Per-turn tool-call cap to prevent runaway agent loops. |
| Purge | `/forget` and a tag-level purge path must exist and be tested before real data is loaded. |

---

## 11. Contractor engagement

The memory store will contain career, financial, health, family, and employer-adjacent material. The following controls are requirements of the engagement, not preferences.

### 11.1 Synthetic data

The contractor builds and tests exclusively against a **synthetic corpus** supplied by the owner: same schema, same tag taxonomy, same document shapes, fabricated content. The contractor never has access to real content at any point.

### 11.2 Environment separation

| | Contractor | Owner |
|---|---|---|
| Supabase project | Dev (synthetic) | Prod |
| Anthropic API key | Dev key, low spend cap | Prod key |
| Telegram bot | Dev bot | Prod bot |
| Drive access | Test folder | Real root folder |
| Deployment | Dev Railway project | Prod Railway project |

### 11.3 Ingest

The contractor delivers the ingest pipeline. **The owner runs it against real data**, after handoff, on prod infrastructure.

### 11.4 Handoff checklist

- [ ] All source code transferred to owner-controlled repo
- [ ] Every dev credential revoked (Anthropic, Supabase, Telegram, Voyage, Google service account)
- [ ] Every prod credential generated fresh by the owner, never seen by the contractor
- [ ] Contractor removed from Supabase, Railway, GitHub, and Google Cloud
- [ ] Codebase audited for logging of prompt/response bodies
- [ ] Dev Supabase project deleted
- [ ] Runbook delivered: restart, reindex, restore from backup, rotate keys

### 11.5 Contract terms

NDA, IP assignment, and a no-retention clause covering code and any data encountered. Treat these as deterrents; §11.1–11.4 are the actual controls.

---

## 12. Cost model

**One-time:** 60–90 contractor hours.

**Recurring:**

| Item | Monthly |
|---|---|
| Railway | $10–20 |
| Supabase Pro (primary store) | $25 |
| Supabase Free (isolated store) | $0 |
| GitHub | already paid |
| Embeddings | $3–10 |
| Claude API (estimated usage) | $50–150 |
| **Estimated total** | **$90–205** |

Replaces roughly $100/month of current subscription spend. Approximately cost-neutral at the low end.

### 12.1 Spend ceiling vs. estimate

The `$50–150` Claude API line is a **forecast of normal use**. The spend ceiling is a separate control: a hard cap configured on the API key that stops billing if something misbehaves. It is not additional budget — it is the point at which the system shuts itself off.

| Control | Value |
|---|---|
| Hard monthly cap on Anthropic key | $300 |
| Alert threshold | $150 |
| Per-turn tool-call cap | 10 |
| Per-turn token cap | 200k |

Rationale for $300: double the high end of normal use. Enough headroom that a genuinely heavy month doesn't lock the assistant out; low enough that a runaway loop is stopped within a day rather than producing a four-figure invoice. Revisit after three months of actual usage data.

---

## 13. Milestones and acceptance criteria

**M0 — Environments.** Both environments provisioned, synthetic corpus generated, secrets management in place.
*Accept:* contractor can deploy to dev; no real credentials exist in the contractor's environment.

**M1 — Ingest and index.** Drive and GitHub sync operational, chunking and embedding working, Workspace export and OCR paths handled.
*Accept:* a file added, edited, and deleted in the test Drive folder is reflected in the index within one poll interval, including a Google Doc and a scanned PDF.

**M2 — Retrieval.** Hybrid search live, tiering implemented, scope filtering working.
*Accept:* against the synthetic corpus, an exact-string query (a fabricated brand name) and a purely conceptual query both return correct results in the top 5.

**M3 — Telegram.** Bot live with allowlist, images, voice, message splitting, commands.
*Accept:* a non-allowlisted account receives no response; a 6,000-character answer arrives intact.

**M4 — Extraction.** Post-turn pipeline writing to `notes`, supersession logic, weekly review digest.
*Accept:* in a scripted 20-turn dialogue containing 4 owner decisions, 2 rejections, and 6 assistant suggestions, the pipeline records exactly the 4 decisions and 2 rejections, and **zero** assistant suggestions. This test must pass before handoff.

**M5 — Write-back and hardening.** Drive and repo writes, `_archive` behavior, purge path, spend caps, backup restore test, runbook.
*Accept:* full handoff checklist (§11.4) signed off.

---

## 14. Out of scope

- **Code authoring.** The WattsWay build stays in Cursor and Claude Code. Vector retrieval over a codebase is worse than a dedicated coding tool. This system holds *decisions about* the app, not the app.
- **Multi-user access.** Single user, v1.
- **Autonomous action.** The assistant retrieves, reasons, and writes to its own stores. It does not send email, book, purchase, or act on external systems in v1.
- **Real-time collaboration or a web UI.** Telegram is the interface.

---

## 15. Open decisions

### Resolved

| Decision | Resolution |
|---|---|
| Separation of `business-ops` and `job-search` | Two Supabase projects, physical isolation. See §4.4. |
| Raw transcript retention | 24 months, then purged. Config value `MESSAGE_RETENTION_MONTHS`. Extracted `notes` are retained indefinitely and carry the durable content. |
| Voice notes | Deferred past v1. Telegram voice messages receive a "not yet supported" reply rather than being silently dropped. |
| Additional users | None. Single Telegram ID on the allowlist. No spouse account, no shared access, no second seat in any future version without a deliberate revision to this spec. |
| Monthly API spend ceiling | $300 hard cap, $150 alert. See §12.1. |
| Embedding provider | Voyage AI `voyage-4`, 1024 dimensions. Schema is already written for `vector(1024)`. Free allocation of 200M tokens on the voyage-4 generation is expected to cover the full initial ingest at no cost. |

### Still open

None. Specification is complete and ready for contractor scoping.

### Note on reversibility

Switching embedding providers later requires a schema migration (`vector(1024)` → new dimension), a full re-embed, and an index rebuild. At this corpus size that is approximately one day of work and a negligible API bill — not the multi-week migration it would be at enterprise scale. Treat the choice as considered, not irreversible.
| GitHub plan | Existing paid plan is sufficient. No change required. |
| Supabase plan | Primary store upgrades to Pro at go-live. Free tier is acceptable for the contractor's dev environment and for the isolated `job-search` store. |

---

*End of specification.*
