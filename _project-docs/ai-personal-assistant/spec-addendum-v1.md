# Personal AI Assistant — Addendum v1

**Companion to:** `personal-ai-assistant-spec.md` (v1.0)
**Basis:** Systems audits run against three live Claude.ai Projects (Fitness/Training, Business Ops, Job Opportunities/Cloudstaff), September 2026. Full audit responses on file.
**Status:** Ready to fold into spec v1.1 before Stage 0.

---

## A. Why this addendum exists

The audits were run to answer one question: what is Claude.ai's Projects feature actually doing, mechanically, when it acts as a persistent assistant across sessions? All three came back with the same structural gaps, independently, despite covering unrelated domains (training, hotel-brand operations, career negotiation). That convergence is the justification for the additions below — these aren't speculative improvements, they're fixes for failures already observed in production use.

**The three confirmed failure modes:**

1. **Retrieval is relevance-judged, not forced.** Each turn, only a listing of file descriptions is seen; which files actually get opened depends on a heuristic read of the current message. A symptom report that doesn't sound like a training question, or a dispute update that doesn't sound like the file it lives in, can be missed. Confirmed independently in all three domains, and named by the audited instance itself as the cause of past factual errors ("stale DEXA, stale RHR, iron untested — caught by you, not the system").

2. **State is a periodically-refreshed prose snapshot, not a queryable object.** There is no ticket object, no plan object, no comparison table — only "the last time this was written down." Status reads as current but is really last-known. No mechanism flags staleness.

3. **Reconciliation is entirely manual.** New information is never automatically checked against stored facts for contradiction or relevance. It happens only if a question happens to trigger it.

Kilo's design already avoids some of this by construction (hybrid search always runs against chunks, §6.1). The additions below extend that same discipline to the curated notes layer, and to the state that discipline doesn't currently cover at all.

---

## B. Schema additions to §4.1

### B.1 `tags text[]` on notes

Independent of project/subproject. Lets a fact surface across domain boundaries without loosening the job-search isolation (§4.4) — tags are an orthogonal dimension, not a bypass of the store split.

Initial cross-cutting tags:

- `physical-status` — symptom, injury, or health-relevant mention, regardless of which project it was said in
- `dispute-status` — an open conflict, escalation, or negotiation with a live state
- `criterion` — see B.3

### B.2 `checked_at` / `stale_after` on status-bearing notes

Every audit surfaced the same gap under different names: fitness had no time-series or freshness check, ops had a dispute file silently days out of date, job-search had "exactly as current as the last write" with no flag. A note tagged `dispute-status` or otherwise representing a living situation (not a one-time decision) gets a `checked_at` timestamp, and Kilo surfaces it unprompted when stale — "CallTek dispute last confirmed 11 days ago, still accurate?" — rather than waiting to be asked.

### B.3 New note kind: `criterion`

Added to the `kind` check constraint in §4.1 (alongside `decision`, `constraint`, `preference`, `number`, `correction`, `rejected`).

This is the sharpest gap the job-search audit surfaced: "if you asked me right now what dollar number would make Cloudstaff clearly better than staying, I don't have a stored answer — I'd infer from behavior." A threshold, floor, or trigger condition you state ("if X happens, that changes the calculus") must be captured as its own discrete fact at the moment you state it, not left to be reconstructed from past behavior under pressure later, when it matters most.

### B.4 New table: `positions` (or `plans`, domain-dependent naming)

The single biggest structural gap across all three audits: no persistent, mutable, queryable "current state" object. Fitness: no object for "this week's plan," only regenerated text. Job-search: no side-by-side comparison of Charter vs. Cloudstaff terms, rebuilt from prose every time. Ops: no ticket/dispute object with a status field.

```sql
create table state_objects (
  id            uuid primary key default gen_random_uuid(),
  project       text not null,
  subproject    text,
  label         text not null,          -- "week-of-2026-09-14 plan", "charter-track", "cloudstaff-track"
  fields        jsonb not null,         -- structured key/value state, shape varies by label
  updated_at    timestamptz not null default now(),
  superseded_by uuid references state_objects(id)
);
```

Kept deliberately loose (`jsonb`) rather than one rigid schema per domain — a training plan's fields and a negotiation-track's fields don't share a shape, and forcing one invites exactly the kind of premature schema rigidity the spec elsewhere avoids (§4.3's tag taxonomy is intentionally extensible for the same reason).

---

## C. Retrieval changes to §6 / §6.1

### C.1 Forced session-start injection

New retrieval path, distinct from query-time hybrid search: at the start of a session (new Telegram topic, or `/newweek`), Kilo runs a fixed lookup for unresolved `physical-status`, `dispute-status`, and `criterion`-tagged notes relevant to the active project scope — independent of what the opening message says. This is the direct fix for failure mode #1. It does not depend on the user's phrasing landing on the right keywords.

This is additive to, not a replacement for, §6's hybrid search. Query-time retrieval still runs normally within the session.

---

## D. Extraction pipeline changes to §7

### D.1 Reconciliation at write time

New instruction for the extraction pass: when a new fact is written, check it against existing unresolved notes in the same project/tag for contradiction or direct relevance, and set `superseded_by` (§7.4) or append a cross-reference immediately — not left for a future retrieval to notice by accident. This is the fix for failure mode #3, confirmed independently in all three audits.

### D.2 Capture `criterion` facts explicitly

Extraction must recognize threshold/trigger language ("if X, then Y matters," "the floor is," "what would change my mind is") and write it as a `criterion` note (B.3), not fold it into a `decision` or lose it in narrative.

---

## E. Interface changes to §8 (Telegram)

### E.1 Forum topics, not a flat private chat

Run the bot in a private supergroup with topics enabled. Each recurring context (a training week, a farm season, an ops thread) gets its own topic — separate scrollback, mapped to the existing `thread_id` column in `messages` (§4.1), which is already present and currently unused for this purpose.

### E.2 `/newweek` command

Stamps a boundary on the current thread, triggers a close-out extraction pass on the outgoing week's messages, and opens the injection described in C.1 for the new one.

---

## F. Role-specific behavior — addendum to §9.1

Fitness-coach mode (and analogous "advisor" modes for other domains) requires behavior beyond the generic "direct, analytical register" currently specified:

- When a `physical-status` (or equivalent) tagged note surfaces via C.1, Kilo proposes a concrete adjustment in the same turn — not just a mention of the fact. "Knee pain Tuesday → box squats this week" not "knee pain was mentioned Tuesday."
- On pushback: state the reasoning plainly, once, without hedging. If the user acknowledges and proceeds anyway, respect the decision and do not re-raise it unprompted in that session. Log the override as a `decision` note with the advice given in the rationale field (§7), so it's available if the pattern recurs — this is what lets a future session say "this is the third time," rather than starting over each time.
- This is a firm, stated-once-then-respected shape — distinct from re-litigating and distinct from silent compliance. All three audits confirmed the current Claude.ai instances already do the "state once, defer" half correctly; what's missing is the follow-through logging (D.1) that would let a future session recognize a pattern instead of relitigating from zero.

---

## G. Explicitly deferred, not overlooked

The ops audit surfaced a category worth naming so it doesn't look like an oversight later: **no live read access to external systems** (Salesforce, Zendesk, CAS, Workday, etc.). This stays out of scope per §14 (no autonomous action, v1). Kilo improves on *retrieval over what you've told it or written down* — it does not become an integration platform. That's a substantially larger engineering effort than this build, and conflating the two would undo the scope discipline that made the thin-slice approach (`thin-slice-build-guide.md`) viable in the first place.

Similarly: live device data (Oura/Withings/Garmin) is a real gap the fitness audit surfaced, but the fix is narrower than "integrate everything" — WattsWay's Supabase project already aggregates this data (see `/projects/.../wattsway-app`). The addition here is Kilo querying that existing store as a new ingest source, not building a new device-data pipeline from scratch.

---

*End of addendum. Fold into `personal-ai-assistant-spec.md` as v1.1 before resuming Stage 0.*
