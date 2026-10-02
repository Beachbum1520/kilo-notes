# REJECTED.md

Approaches evaluated and ruled out, with reasons. The point of this file is to prevent re-litigating settled questions.

**Format:** what was considered, why it was rejected, and what would change the answer. That last field matters — a rejection isn't permanent, it's conditional on the reasoning that produced it.

---

## Hardware

### AI wearable pendants (Bee, Omi, Limitless/Meta, Plaud)

**Rejected.** These are capture devices — microphone, transcription, a vendor cloud. They address none of the actual problem, which is fragmented context and retrieval. Adds a second vendor with its own caps and terms. Limitless being absorbed into Meta is a live example of the platform risk being avoided.

*Would change if:* the goal shifted from retrieval to passive capture. It hasn't.

**Separately:** recording consent law differs sharply by jurisdiction — Georgia is one-party, the Philippines is all-party and criminal. An always-on recorder on a Manila trip is not a gray area.

---

## Interface

### WhatsApp

**Rejected in favor of Telegram.** The official Business API requires Meta business verification and bills per conversation window. Unofficial bridges work until the number gets banned. Telegram's bot API is free, official, and takes minutes to set up. Same phone-based UX.

*Would change if:* Telegram became unavailable, or a hard requirement emerged to reach people who only use WhatsApp. Neither applies to a single-user system.

---

## Orchestration and hosting

### n8n / OpenClaw as an orchestration layer

**Rejected.** Both assume you need a framework to wire the pieces together. With Supabase and a persistent process already in the stack, a thin custom implementation is smaller, more comprehensible, and has no framework upgrade treadmill. Also incompatible with the learning goal — a visual workflow builder hides exactly the mechanics worth understanding.

*Would change if:* the system grew many integrations and connector maintenance became the dominant cost.

### VPS with Docker, reverse proxy, TLS management

**Rejected.** Most of the maintenance burden of self-hosting lives here, and none of it is necessary. Railway runs a persistent process from a GitHub repo with no server to patch.

*Would change if:* costs at scale ever justified running raw infrastructure. Not at single-user volume.

### Vercel for the assistant backend

**Rejected.** Serverless is built for short request/response cycles. An agent loop that retrieves, calls a model, tool-calls, and calls again wants minutes. Would require a queue and an async ack-then-push pattern to work around timeouts.

**Vercel remains correct for the WattsWay PWA frontend.** Different workload, different answer.

*Would change if:* the assistant became a simple stateless query/response with no agent loop.

### Supabase Edge Functions

**Rejected, narrowly.** Genuine upside: runs adjacent to the database, so vector queries skip a network hop, and no new vendor. But it reintroduces the timeout envelope and forces webhooks instead of long-polling.

*Would change if:* adding Railway as a vendor became a problem, or if latency on vector queries turned out to matter more than expected.

---

## Storage

### Notion as the document store

**Rejected.** Stores blocks rather than documents, so chunking fights the data model. API rate limits make full re-indexing painful. Export is lossy. Trades Google lock-in for worse lock-in.

*Would change if:* Notion shipped a document-level export and materially better API throughput.

### S3 / R2 / Supabase Storage as the document store

**Rejected.** Cheap and durable, but there's no way to browse or edit content without custom tooling. A system of record you can't open by hand isn't one.

*Would change if:* the corpus became machine-generated and never needed human editing.

### Migrating off Google Drive entirely

**Rejected.** Weeks of migration for near-zero gain. Dropbox and OneDrive are the same shape with none of the existing footprint. Drive stays for files; a GitHub markdown repo was *added* for notes rather than replacing anything.

---

## Retrieval

### Pure vector search

**Rejected.** Fails on exact strings — proper nouns, brand names, SKUs, lab markers, part numbers. Semantic similarity does not reliably retrieve a literal token. Hybrid search combining pgvector with Postgres full-text, fused by reciprocal rank, is the design.

*Would change if:* nothing. This is settled and is the discriminator in contractor screening.

### OpenAI `text-embedding-3-small`

**Rejected in favor of Voyage `voyage-4`.** Voyage benchmarks better on retrieval, uses 1024 dimensions against OpenAI's 1536 (a third less vector storage and a faster index), and its free allocation covers the full initial ingest.

**Acknowledged downside:** Voyage is now part of MongoDB, which creates some risk that standalone API access gets folded into their platform.

*Would change if:* Voyage deprecated standalone access. Switching costs roughly one day — schema migration, re-embed, index rebuild — so this is reversible, not load-bearing.

---

## Data separation

### A `WHERE` clause separating business-ops from job-search

**Rejected.** A filter is a policy, not a boundary. One missing predicate, one bug, one ad-hoc query and the separation is gone. Implemented instead as two physically separate Supabase projects with separate credentials, where cross-store queries are specified as something that must never be built.

*Would change if:* nothing. The cost of the extra project is zero on the free tier.

---

## Organization

### Merging Claude projects into fewer, broader ones

**Rejected.** Projects serve two conflicting jobs — context container (wants breadth) and conversation folder (wants narrowness). Merging fixes context at the cost of navigability, and conversation lists become unsearchable. Narrow projects are the correct call; the context problem gets solved by the assistant being built here, not by reorganizing.

**Exception accepted:** Business Ops and Manila Inside Sales are parent/child and can merge.

---

## Tooling

### Replacing Cursor with Claude Code

**Rejected.** Previously evaluated and settled: Cursor stays for the WattsWay app.

Claude Code is used for the *assistant* build — a different codebase with different needs. These coexist; this is not a reversal.

*Would change if:* nothing. Do not raise again.

---

## Build approach

### Outsourcing the entire build

**Rejected in favor of a thin slice built personally, then contracting the remainder.**

Reasons:
- A large share of the specification's complexity — synthetic corpus, redacted spec, dev/prod separation, access matrix, break-glass procedure, offboarding — exists solely because a stranger is involved. Building personally eliminates it.
- The primary goal is learning, not delivery. Outsourcing the whole thing forfeits the point.
- No deadline pressure.

**What is still intended for contract:** Google Drive sync, Workspace format export, OCR, image handling, the extraction pipeline. High slog, low learning per hour.

*Would change if:* the thin slice stalls, or the remaining scope proves larger than expected.

### Full-time offshore hire for the build

**Deferred, not rejected.** Better value than a one-off contractor if maintenance and other personal technical projects are factored in. Revisit after the thin slice is running.

---

## Scope

### Coding assistance inside the retrieval system

**Rejected — permanently out of scope.** Vector retrieval over a codebase is worse than a dedicated coding tool. The assistant holds *decisions about* projects, not the projects themselves.

### Autonomous action (email, booking, purchasing)

**Out of scope for v1.** The assistant retrieves, reasons, and writes to its own stores. It does not act on external systems.

### Additional users

**Rejected.** Single user. No shared access, no second seat, no exceptions without a deliberate revision to the specification.
