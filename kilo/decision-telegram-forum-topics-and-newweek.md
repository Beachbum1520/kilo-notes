# Add Telegram forum topics and a /newweek command to the spec

**Decided:** [UNCERTAIN] Scott said "Yes. Let's do that." to Claude's proposal for a spec addendum with three parts:
- Run Kilo in a private Telegram supergroup with forum topics, mapping `message_thread_id` to the existing `thread_id` column, to separate conversations for human navigation.
- Keep project tagging for cross-domain retrieval.
- Add a `/newweek` command that marks a weekly boundary and triggers a close-out extraction on the outgoing thread.

**Why:** It gives conversation separation like Claude.ai Projects (for example a new fitness topic each week) while retrieval still crosses domains.

**Rejected alternatives:** A bare private 1:1 bot chat, which is what Stage 5 assumed as written.

**Would revisit if:** Not stated.

**Approx date:** September 2026

**Source:** Backend-first development approach, 2026-09-13
