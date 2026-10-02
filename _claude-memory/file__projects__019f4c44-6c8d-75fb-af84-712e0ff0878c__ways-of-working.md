---
name: ways-of-working
description: How WattsWay development is run — two-lane Claude/Cursor split, PR workflow, handoff docs, onboarding, and Scott's collaboration preferences
sources: [backfill]
aliases: []
---

- [stated] Two-lane development: Claude handles architecture, diagnosis, and code generation; Cursor cloud agents (cursor.com/agents) execute implementation tasks because Scott's work laptop is browser-only
- [stated] Agent prompts are written by Claude as copy-paste ready
- [stated] PR workflow enforced: branch protection on `main` (`protect-main` ruleset) — PRs required, force pushes blocked, deletions restricted; no direct pushes to main
- [stated] Handoff doc maintained in two places — Claude project instructions and `wattsway-dev-handoff.md` at repo root so agents can read it; updated same-day
- [stated] Scott prefers systematic root-cause diagnosis before solutions, rather than guessing
- [stated] Scott prefers direct, terse communication with exact paths and values, one step at a time, no hedging
- [stated] Scott has explicitly asked to slow down and work one step at a time
- [stated] Incremental family onboarding: family members create FitnessSyncer accounts and connect Garmin independently; Scott completes the Google Drive destination step using his Google account