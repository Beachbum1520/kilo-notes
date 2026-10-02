---
name: learnings
description: Hard-won technical gotchas in the WattsWay data pipeline (TCX, FitnessSyncer, Supabase) and API application strategy
sources: [backfill]
aliases: []
---

- [stated] FitnessSyncer modifiedTime trap: FitnessSyncer sets Drive `modifiedTime` to the original activity date on historic backfills, not the upload date — always use `createdTime` to find newly exported files; never rely on `modifiedTime` for recency
- [stated] TCX XML timestamp rule: never use filename timestamps (they're offset by hours) — always use the `<Id>` element timestamp
- [stated] TCX dump-skip pattern must be generalized (e.g. match any `-HH-00-00.000-.tcx`) to handle timezone offset variance across users
- [stated] Walk-before-run classifier ordering: walk classification must precede run rules to avoid partial matches
- [stated] This Supabase project has `auto-expose` OFF — all new tables require explicit GRANTs or 403 errors will result
- [stated] Treadmill distance caveat: treadmill distances are watch stride estimates (~8% high); post-run calibration edits Garmin Connect's summary but not the exported TCX — accepted known limitation
- [stated] API applications: position WattsWay as a platform in development (not a personal project) for commercial API applications; use "Watts Way Fitness" as the company name to match the prior Garmin registration; live domain, privacy/terms pages, and three integrations support the application
- [stated] TrainingPeaks fat mass note: fat mass and lean mass are mathematically derived from the same body fat % reading, so the fat mass line will largely mirror lean mass inverted — useful for trends, noisy on individual days