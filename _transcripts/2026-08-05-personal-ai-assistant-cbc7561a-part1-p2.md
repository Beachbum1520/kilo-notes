I'm leaning toward recommending a second Supabase project for job-search since it's low-volume and can stay on the free tier, giving him a physical boundary rather than relying on WHERE clauses and policies. For raw message retention, I'm thinking 24 months before rolloff after extraction completes, since the notes capture the durable content and older transcripts have minimal retrieval value while being the most sensitive data to store long-term.

Now I need to update the spec file to reflect these decisions and close out the open items — updating the Supabase section to note free tier for dev and Pro for production, revising the cost model, documenting the job-search separation architecture, and resolving decisions 2 through 6 while leaving embedding open. I'll make targeted edits to the affected sections rather than rewriting the whole document. I should create a new area file for this personal AI build project since it's becoming an ongoing area with durable decisions and constraints. I'll handle the file edits first, then set up the memory file, then respond.

## On the ceiling — two different things

The `$50–150` in that table is a **forecast** of what you'd normally spend. The ceiling is a **circuit breaker** — a hard cap on the API key that stops billing when something goes wrong. Not additional budget. It's the number at which the system shuts itself off.

You need it because an agent loop that misbehaves — bad retrieval feeding a retry loop, a sync job re-embedding the same corpus overnight — can burn far past normal use before you notice. Without a cap, you find out from the invoice.

I set it at **$300 hard, $150 alert**, plus a 10-tool-call and 200k-token cap per turn. Double your high estimate: enough headroom that a genuinely heavy month doesn't lock you out, tight enough that a runaway is stopped inside a day. Revisit after three months of real data.

## Separation — I made it physical, not policy

You said keep business-ops and job-search separate. A `WHERE` clause isn't separation — one missing filter and it's gone. So: **two Supabase projects.**

Primary store holds everything except job-search. A second project holds job-search alone, free tier, low volume. Runtime holds both connections. Default queries hit primary only; job-search is reachable only under explicit `/scope job-search`. **No query spans both** — that's specified as something the contractor must not implement, not a feature to disable later.

Separate Drive root folder and separate service account too, and its own private repo. A full dump of the primary store contains nothing about your job search.

## Supabase free tier is a problem for prod

No point-in-time recovery, and projects **pause after 7 days idle**. Fine for the contractor's dev environment and fine for the low-traffic job-search store. Primary store needs Pro at go-live — $25, already in the cost table.

GitHub at $48/yr is fine as-is. No change.

## Retention

Set at 24 months, then purge, as a config value you can change. Extracted notes are kept indefinitely — they carry the durable content, and they're a fraction of the volume. Raw transcripts past two years have low retrieval value and are the most sensitive blob in the system.

---

**One open decision left: embedding provider.** Voyage `voyage-3` at 1024 dimensions, or OpenAI `text-embedding-3-small` at 1536. It sets the vector dimension across every table and is genuinely painful to change after ingest — you'd re-embed the entire corpus.

Voyage is the Anthropic-aligned choice and performs well on retrieval benchmarks. OpenAI has broader tooling and more people who've worked with it, which matters slightly for hiring. Either is defensible; I'd take Voyage.

Say the word and it goes in the spec as resolved, and you're ready to post the job.

### SCOTT (2026-08-05T17:21)
"I set it at $300 hard, $150 alert" - agreed!.

not sure the ramifivatiosn of this decison on voyage verussu open ai
[File uploaded: 1785950501723_image.png]

### CLAUDE (2026-08-05T17:22)
The user is asking about the differences between Voyage and OpenAI embeddings, so I need to understand what's changed with Voyage since it was acquired by MongoDB in February 2025 — that's a significant shift for anyone considering it as a vendor. I should search to verify the current state and check what OpenAI's text-embedding-3-small offers, since these details matter for making an informed decision.

Looking at the key trade-offs: Voyage generally performs better on benchmarks and costs less per token, but there's now vendor risk with MongoDB ownership. The dimension difference (1024 vs 1536) gives Voyage a storage advantage of about 33%, which could matter on Supabase's limited free tier. OpenAI is more familiar to most developers, but the switching cost isn't as high as it might seem — re-embedding his corpus would only run $5-20, so this decision is more reversible than I initially suggested. He's already paying for ChatGPT, but that's separate from API billing anyway.

Let me check the current pricing and status for both services to give him accurate numbers.

Voyage just released their 4th generation models in January 2026 with 1024 default dimensions and Matryoshka scaling options, plus 200M free tokens to start. They're now part of MongoDB, and all voyage-4 variants share the same vector space so I can index with the large model and query with lite without reindexing. Pricing-wise, lite is $0.02/M and large is $0.12/M, though OpenAI's text-embedding-3-small matches the lite price point.

At his scale — likely 10-100MB of text across nine projects — the 200M free tokens probably covers his entire corpus forever, making embedding cost completely negligible. Switching models isn't painful either; re-embedding would be free or a few dollars, with the real effort being a schema migration and reindex, maybe a day of work rather than weeks. I should update the spec to voyage-4 and mark this resolved since the vector dimension stays at 1024 anyway.

The key tradeoff is quality versus cost: voyage-4 approaches the previous flagship quality and is what serious RAG teams use, while OpenAI 3-small ranks a tier below on retrieval benchmarks. But since cost is a non-factor here, voyage-4 is the clear choice.

Storage-wise, 1024 dimensions means 33% less storage and faster HNSW indexing compared to 1536, which matters on Supabase Pro's disk allocation. The real vendor risk worth flagging honestly is that Voyage is now owned by MongoDB — the standalone API still exists, but there's some chance it gets deprecated in favor of Atlas integration, whereas OpenAI's embedding API isn't going anywhere. Both support matryoshka embeddings now, so he can truncate dimensions later without re-embedding if needed. OpenAI is more familiar to contractors, but the API call is trivial either way. Since switching is genuinely cheap at his scale, this decision is low-stakes and worth framing that way.

Now I need to update the spec file — change voyage-3 to voyage-4 in the table, mark section 15 as resolved, and verify the schema already uses vector(1024) which aligns with voyage-4's default. Then I'll update the memory file with the resolved decisions and spending ceiling.

I need to correct my earlier overstatement and present the file again, keeping it concise.First, correct something I said last turn: I called it "genuinely painful to change." **That was overstated at your scale.** Switching later means a schema migration, a re-embed, and an index rebuild — about a day of work and a trivial API bill. It's a considered choice, not a one-way door. Don't agonize.

Also, my model reference was stale. The current generation is voyage-4, launched January 2026, at $0.06 per million tokens, defaulting to 1024 dimensions with Matryoshka options at 256, 512, 1024, and 2048.

## The actual ramifications

**Cost — a non-factor.** Every account gets 200 million free tokens on the voyage-4 generation, roughly 400,000 documents. Your entire corpus almost certainly fits inside that. OpenAI's `text-embedding-3-small` is cheaper per token, but at these volumes embedding costs are negligible next to vector storage and generative model calls. You'd be optimizing a rounding error.

**Quality — Voyage wins.** Voyage is the model most serious RAG teams end up switching to. This is the axis that actually matters, because your retrieval quality determines whether the thing feels smart or feels broken. It's the one place I'd pay for the better option — and here you're not even paying more.

**Storage — Voyage wins.** 1024 dimensions vs 1536 is a third less vector storage and a faster HNSW index. Relevant on Supabase Pro's disk allocation, and it compounds as the corpus grows.

**Vendor risk — OpenAI wins, mildly.** Voyage is now part of MongoDB. The standalone API still operates, but MongoDB is clearly steering toward Atlas-integrated access, so there's a nonzero chance the standalone path gets deprecated in favor of their platform. That's the one real argument against. OpenAI's embedding endpoint isn't going anywhere.

Given that switching costs you a day, that risk is manageable rather than disqualifying.

**Hiring — OpenAI wins, marginally.** More contractors have used it. But it's a five-line API call either way; anyone who can't adapt shouldn't get the job.

**One thing Voyage has that's genuinely useful:** all voyage-4 models share a single vector space, so you can index with voyage-4-large and query with voyage-4-lite without re-indexing. That gives you a quality/cost dial you can turn later without touching the corpus.

## Called it

Voyage `voyage-4` at 1024 dimensions. Better retrieval, smaller index, free at your volume, and the schema was already written for it. Spec upda