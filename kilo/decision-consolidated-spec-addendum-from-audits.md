# Write one consolidated spec addendum from the three audits

**Decided:** Scott said "Yes" to writing one consolidated addendum to the spec, built from the three audits, before touching Stage 0. It covers:
1. Forced session-start retrieval for cross-cutting tags (physical-status, deal-criteria, dispute-status).
2. A staleness field (`checked_at` / `stale_after`) on status-bearing notes.
3. A `criteria` note kind.
4. A structured plan/position state table.
5. Reconciliation at write time.

**Why:** All three audits showed the same failures: retrieval judged by relevance rather than forced, no persistent state objects, stale status with no flag, and reconciliation left entirely to manual checks.

**Rejected alternatives:** Patching the fitness mode on its own.

**Would revisit if:** Not stated.

**Approx date:** September 2026

**Source:** Backend-first development approach, 2026-09-13
