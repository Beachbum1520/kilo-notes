# Systems Audit Findings — full record

**What this is:** the complete responses to the three self-audits run on 13 September 2026 against live Claude.ai Projects. `spec-addendum-v1.md` is the consolidated design conclusion drawn from these; this file is the underlying evidence, preserved so the addendum's claims can be checked without going back to the conversations.

**Method.** Each audit was run inside the project being audited, asking that instance to describe its own mechanics — data inputs and what persists, decision logic on new input, pushback behavior, cross-session memory, gaps, and goal alignment. The instruction each time: *"Be exact and mechanistic. I'm not looking for reassurance that the system works — I'm looking for the actual logic so I can decide what to keep, what to fix, and what a new system needs to replicate."*

**Source conversations:** "Personal AI coaching system audit" (Fitness & Training) · "Personal AI system architecture audit" (Business Ops) · "Personal AI system design audit" (Job Opportunities).

---

## 1. Fitness & Training audit

### Data inputs — carried vs. fresh

| Category | Carried or fresh |
|---|---|
| Goals (longevity, NYC 2027 guide-run, sub-4:00, Armor Build recomp) | Carried — project memory files |
| HR zones, run caps, strength split, thermal protocol | Carried |
| Physiology baselines (DEXA, HRV/Hct link, RHR, labs) | Carried, but stamped "re-verify" — point-in-time snapshots, not live feeds |
| Supplement/med stack | Carried; updated only when told it changed |
| Schedule constraints (office Tue/Wed, gym locations) | Carried |
| Race history | Carried |
| Symptom/pain reports, missed sessions, today's numbers | **Fresh only** — no log; if not said this session, it does not exist |
| Oura/Withings/Garmin daily data | **Not carried.** Baselines in memory, not a live feed. Today's number requires actively fetching the Drive sheet that turn |
| Lab values | Carried as of last-stated date, never auto-rechecked |

The stated mechanism: *"at the start of a reply I see a listing of memory file titles/descriptions, not their contents. I choose which files to open based on relevance to your message. If your question doesn't obviously touch a file, I may not read it."* Named failure mode: a symptom report that doesn't sound like a training question gets answered without pulling HR-cap or med-stack context.

### Decision logic

No coded threshold table. A number arrives → compared against carried baseline *if that file was opened* → read and recommendation in the same turn. "This week's plan" is never rewritten as a stored object, because no such object persists — the plan exists only as text generated that turn. Mild-vs-significant is a judgment call each time, not a rule: *"There's no documented severity ladder — this is a gap, not a feature."* No confirmation is required before adjusting a recommendation.

### Pushback behavior

Hold the position, state reasoning once, don't cave without a real reason, don't re-argue. Enforced by instruction text only — *"there's no audit trail confirming I didn't quietly fold three turns later. It's consistent because the instruction is clear, not because there's a system forcing it."*

### Cross-session memory

Persists: only what is written into memory files, either on explicit instruction or by a background pass that applies its own bar for durability.

Does not persist: anything the background pass doesn't judge durable (*"a one-off 'knee's a little sore today' likely doesn't get filed unless it recurs"*); the session's plan as a plan object; the reasoning chain behind stored conclusions; anything from Drive, which is fetched live per session and never cached.

### Gaps

- No live data pull by default — must be triggered, not passively watching.
- No time-series storage — single "latest known" values, not a queryable trend.
- **No enforced pre-read step.** Project instructions say review the memory card before every response; mechanically it's a relevance judgment, not a hard gate. *"That's the actual failure mode behind past wrong facts (stale DEXA, stale RHR, 'iron untested') — nothing forced a check against source files; it took you catching it."*
- FIT binary parsing needs a code-execution session; TCX over 1MB can't be pulled whole.
- No severity/threshold schema for symptom reports.
- No proactive or scheduled check-ins — everything is reactive.
- No automatic reconciliation of a new claim against the memory file before stating it as fact.

### Goal alignment

Concrete derived rules (strength before run, two spaced lower days, HR cap overrides pace, cold plunge AM only) fire mechanically. The north-star goals function as narrative tiebreakers: *"If you removed the north-star language from memory tomorrow, the day-to-day plans wouldn't change much, because the operative constraints are the concrete derived rules, not the abstract goals themselves."*

### Its own bottom line

> a static fact-store curated turn-by-turn, read selectively rather than exhaustively; zero live-data awareness unless triggered; zero automated verification against source-of-truth files; zero persistent "current plan state" object — only regenerated text.

---

## 2. Business Ops audit

### Data inputs

**Persisted** (but not live): org structure and reporting lines, peer map, BPO contacts; vendor/contract terms as stated facts rather than contract text (MSA sections, exclusivity clauses); active disputes (CallTek/Josh, MBM billing) as narrative status at last write, not ticket state; naming/redaction constraints; Charter merger context, brand/RFP status, staffing targets; drafting style rules.

**Fresh each time:** any number, date or event since the last memory write; anything not told and not in an opened file; real-time status of anything at all.

The distinction stated precisely: *"The split isn't 'what's important vs. unimportant' — it's 'what got written to a file after a past turn' vs. everything else. Importance doesn't get you into memory; a past conversation touching the topic does."*

### Decision logic

No rules engine. Each turn: scan one-line file descriptions, judge by relevance heuristic which to open. Explicitly non-deterministic — *"'What do I do about Josh's non-compete threat' and 'should I worry about the CTC contract angle' could pull different files depending on which keywords land, even though they're the same underlying question."* Contradictions get flagged by pattern-matching in the moment, not by a validation pass. **Consistent in shape, not in coverage; framing changes what gets retrieved.**

### Pushback behavior

State reasoning once, directly, then defer. No re-litigating. But: *"I will not remember to re-raise a concern later unless the topic comes back up. There's no persistent 'flagged risk' object tracking open pushback across sessions."*

### Cross-session memory

*"Nothing is a tracked state machine. There is no ticket object, no dispute object with a status field, no event loop checking 'has this changed.'"* An automated pass after each turn writes what it judges durable to a flat prose file. No polling, no expiry logic. Concrete consequence: if the Sept 15 meeting with Josh and Jady has already happened, the file still shows it as scheduled. Files are size-capped (~48KB), which pushes toward pruning rather than a growing structured history.

The line worth keeping: *"It reads like continuity; mechanically it's a periodically-refreshed cache of prose, not a database with state transitions."*

### Gaps

- No live access, ever, to Salesforce, Zendesk, CAS, Cosmos, Field Nation, Workday. Any status given on those is a last report, not a query.
- No structured org chart — a name list with reporting sentences, not traversable authority/approval fields.
- No contract/MSA database — specific clauses as stated, not the documents.
- No timestamped dispute log; nothing surfaces *"this was last updated 11 days ago, confirm still accurate"* unprompted.
- No cross-file conflict detection unless two conflicting files happen to be read in the same turn.

Standing caveat it issued about itself: *"Anywhere I sound confident about current status, treat it as last-known-state, not verified-current-state, unless you just told me otherwise this session."*

### Goal alignment

Understood priorities: protect written-record deniability on political/strategic matters; move dispute leverage through Jady rather than direct confrontation; keep BPRF/Cox structure and platform names out of external material; hit PNOC/staffing targets; position for VP in the January reorg; evaluate exit from CallTek toward Cloudstaff.

Applied **reactively only** — rules fire when a draft touches them, but nothing scans for opportunities to advance those priorities. *"It sits inert until a specific draft or decision touches it."*

---

## 3. Job Opportunities audit

### Data inputs

Persisted in four flat files: Charter comp/retention terms (LTIP split, RSU cliff, IC bonus discrepancy, 401k mechanics) in `career-inflection.md`; the Cloudstaff thesis, the people map, and CallTek market context in `cloudstaff-thesis.md`; negotiating posture and principles in `principles-and-working-style.md`. Anything said this session lives only in that conversation until a background pass files it.

*"Nothing here is inferred from a general 'understanding of you' — it's four flat files. If a fact isn't in one of them, I don't have it."*

### Decision logic

**Not automatic.** A new comp detail or timeline shift is not diffed against stored terms unless asked, or unless writing the response requires it. *"If Lloyd's ballpark number lands and you paste it in without asking me to evaluate it, I'll acknowledge it and it may get filed as a new fact — the comparison against your comp floor or the Charter numbers only happens if the response calls for it or you request it."* Stored files are not updated mid-conversation; a background pass does that after the turn.

### Pushback behavior

State once, directly. *"There's no persistent 'disagreement flag' carried into future turns — if you make a call I think is off, that's logged as your call, not as an open dispute I revisit later."* Adds: agreeing more than the evidence supports is a failure mode it cannot self-detect mid-conversation.

### Cross-session memory

A current state exists — the four files — *"and it's exactly as current as the last write."* Example given: `cloudstaff-thesis.md` last updated Sept 11 with Lloyd's reply. Nothing resets at a session boundary. What does not persist: reasoning chains, unadopted draft language, and anything the background pass judged non-durable.

### Gaps

- **No timeline artifact.** Dated facts exist (Sept 2 dinner, Sept 11 Lloyd reply) but no structured chronology across both tracks. *"If you asked 'what's the full sequence of what's been said since June,' I'd be reconstructing narrative order from prose files."*
- **No deal-terms ledger.** No structured comparison of Cloudstaff (undefined — no role, comp or equity terms yet) vs. Charter (base + bonus + RSU schedule + vesting dates). Rebuilt live every time.
- **No explicit decision-criteria object.** No stored comp floor, risk tolerance, or flip threshold.
- **No auto-reconciliation between the two files.** If a Cloudstaff development changes the Charter forfeiture math, that connection is made in the moment, never stored.

The sharpest single admission across all three audits: *"if you asked me right now 'what dollar number would make Cloudstaff clearly better than staying,' I don't have a stored answer; I'd have to ask you or infer from proxies."*

### Goal alignment

Stored and explicit: Cloudstaff > Charter internal > secondary externals, as a stack rank. Everything below that rank is inferred from behavior rather than stated — withdrawal from Allbridge over comp, holding out on Cloudstaff comp anchoring until role scope is clear, forfeiture math (Aug 2029 cliff, Jan 2027 IC tranche) as a live timing input.

---

## 4. What converged

Three unrelated domains, three independent instances, the same three structural findings:

1. **Retrieval is relevance-judged, not forced.** File descriptions are seen; contents are opened on a heuristic. Confirmed in all three, and named by the fitness instance as the cause of past factual errors.
2. **State is a periodically-refreshed prose snapshot, not a queryable object.** No plan object, no ticket object, no comparison table. Status reads as current but is last-known. Nothing flags staleness.
3. **Reconciliation is entirely manual.** New information is never automatically checked against stored facts. Fitness: no auto-check against baselines. Ops: no cross-file conflict detection. Job-search: *"nothing cross-checks new inputs against stored terms unless a human triggers it via a question."*

The convergence is the argument. These are not speculative improvements to design against — they are failures already observed in production use, in three domains that share nothing but the mechanism underneath them.

**Why this is not fixable with better instructions:** every gap is downstream of two product decisions — relevance-judged retrieval instead of forced/tagged retrieval, and a flat prose cache instead of structured state. Those are the product working as designed for a different use case (a helpful assistant per conversation) than the one being asked for (a persistent operational co-pilot with state). Three separate instances independently reported that the instruction-following is honest but the underlying mechanism doesn't guarantee it. That is the argument for owning the retrieval layer.

→ Design response: `spec-addendum-v1.md`.
