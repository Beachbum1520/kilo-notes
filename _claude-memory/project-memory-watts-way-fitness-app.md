# Claude project memory: Watts Way Fitness App

**Purpose & context**

Scott is building **WattsWay** (Watts Way Fitness), a private, invite-only family fitness PWA (React/Vite, Supabase backend, deployed on Vercel) that aggregates health and activity data from Oura, Withings, and Garmin. The goal is a unified family fitness platform with dashboards, activity tracking, body composition monitoring, and eventually automated training plan features. Scott is the primary builder and user; family members are being progressively onboarded. Scott's son Joshua is an experienced developer with GitHub Write access and collaborator status on the repo.

Scott works iteratively with Claude and Cursor agents, prefers **direct, terse communication with exact paths and values, one step at a time, no hedging**. He gets frustrated when Claude guesses rather than diagnoses systematically, and has explicitly asked to slow down and work one step at a time. He holds positions when pushed back without factual correction and expects the same in return.

**Current state**

Active infrastructure and recent completions:
- **Garmin data pipeline** fully operational: FitnessSyncer → Google Drive (TCX files) → Supabase edge function (`sync-garmin`) → `activities` table. Six-type activity taxonomy: run, treadmill, strength, walk, breathing (cold plunges, excluded from training load views), generic.
- **Oura and Withings** integrations are live alongside Garmin.
- **Hourly auto-sync scheduler** deployed: pg_cron job (firing at :15) calls `sync-all` Supabase edge function, sweeps all users/providers with service-role auth, logs to `sync_runs` table (self-pruning after 30 days). Shared sync modules in `_shared/`.
- **Brand assets** deployed: Variant 2 red colorway W-mark logo (#FF2D2D→#CC1133 gradient), PWA icon set, `BrandHeader` React component across dashboard and Settings pages. Scott's color preference is red.
- **Bug fixes shipped**: stale-chunk auto-reload, two-row activity card layout, TCX dump-skip regex generalized to handle timezone offset variance (family member's files used `-12-00-00` vs. `-08-00-00`), HR regex updated for `xsi:type` attribute tolerance.
- **Known issue — Withings OAuth on iOS**: Health Mate app hijacks the OAuth URL inside the PWA; proper fix is queued.
- A family member (user ID `9f2d1573-772e-4d51-babe-6a474164b609`, Drive folder ID `1ECoMD1179iFpKgUn4CEqwVoheXpsrfmq`) is onboarded on Oura and Garmin (via FitnessSyncer/Drive); historic run files missing because FitnessSyncer only fetched run summaries without trackpoint detail — resolution path is Garmin bulk GDPR export → FIT-to-TCX conversion → manual Drive upload.

**On the horizon**

- **Withings iOS OAuth fix** (queued).
- **Historic run file recovery** for onboarded family member: GDPR export → FIT-to-TCX (Claude to handle in-chat) → upload to Drive folder.
- **FitnessSyncer backfill edge case**: After any historic backfill, `last_synced_at` must be nulled because FitnessSyncer backdates Drive `modifiedTime` to activity date, making files invisible to incremental sync windows.
- **Shoe/gear tracker** (Roadmap #6): Native WattsWay feature using activity distance data already in the `activities` table. Business rule: all distance-generating activity types count toward shoe mileage with no exclusions. Planned tables: `shoes`, per-activity assignment logic.
- **TrainingPeaks API access**: Application submitted (program currently paused, similar to Garmin's). If granted, slot into plan builder phase for pushing structured workouts to athlete calendars and reading completed workouts back.
- **Garmin official API**: Access request filed July 10, currently paused with no timeline. Architecturally ready to slot in alongside the Drive lane if/when it reopens.
- **Fat mass chart line**: Dual Y-axis approach recommended for the body composition chart (fat mass on right axis); agent prompt targeting branch `fat-mass-chart-line` with PR workflow ready.
- **Body composition goal context**: Scott is tracking a "recomp" goal (Armor Build program) — losing fat while maintaining/gaining lean mass.

**Key learnings & principles**

- **FitnessSyncer modifiedTime trap**: FitnessSyncer sets Drive `modifiedTime` to the original activity date on historic backfills, not the upload date. Always use `createdTime` to find newly exported files; never rely on `modifiedTime` for recency.
- **TCX XML timestamp rule**: Never use filename timestamps — they're offset by hours. Always use the `<Id>` element timestamp.
- **TCX dump-skip pattern**: Must be generalized (e.g., match any `-HH-00-00.000-.tcx`) to handle timezone offset variance across users.
- **Walk-before-run classifier ordering**: Walk classification must precede run rules to avoid partial matches.
- **Auto-expose OFF in Supabase**: This project has `auto-expose` OFF; all new tables require explicit GRANTs or 403 errors will result.
- **Treadmill distance caveat**: Treadmill distances are watch stride estimates (~8% high); post-run calibration edits Garmin Connect's summary but not the exported TCX — accepted known limitation.
- **API applications**: Position WattsWay as a platform in development (not a personal project) for commercial API applications. Use "Watts Way Fitness" as company name to match prior Garmin registration. Live domain, privacy/terms pages, and three integrations support the application.
- **TrainingPeaks fat mass note**: Fat mass and lean mass are mathematically derived from the same body fat % reading, so the fat mass line will largely mirror lean mass inverted — useful for trends, noisy on individual days.

**Approach & patterns**

- **Two-lane development**: Claude handles architecture, diagnosis, and code generation; Cursor cloud agents (cursor.com/agents) execute implementation tasks (Scott's work laptop is browser-only). Agent prompts are written by Claude as copy-paste ready.
- **PR workflow enforced**: Branch protection on `main` (`protect-main` ruleset) — PRs required, force pushes blocked, deletions restricted. No direct pushes to main.
- **Handoff doc maintained in two places**: Claude project instructions and `wattsway-dev-handoff.md` at repo root so agents can read it. Updated same-day.
- **Systematic diagnosis over guessing**: Scott explicitly prefers root-cause diagnosis before solutions.
- **Incremental onboarding**: Family members create FitnessSyncer accounts and connect Garmin independently; Scott completes the Google Drive destination step using his Google account.

**Tools & resources**

- **Frontend**: React/Vite PWA, deployed on Vercel
- **Backend**: Supabase (project ref: `hzwotatjfltswmiundky`), pg_cron, edge functions (TypeScript)
- **Data sources**: Oura, Withings, Garmin (via FitnessSyncer → Google Drive TCX pipeline)
- **GCP**: Project `wattsway-drive` (scott.watts1117@gmail.com), Drive API enabled, service account `wattsway-sync@wattsway-drive.iam.gserviceaccount.com` (Viewer-only on TCX folders)
- **Secrets**: `GOOGLE_SERVICE_ACCOUNT_EMAIL`, `GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY` stored in Supabase (private key retains literal `\n` escapes; function un-escapes at runtime)
- **Branding**: Manus.ai for logo generation
- **IDE/agents**: Cursor (local on Windows desktop) + Cursor cloud agents
- **Version control**: GitHub (private repo, Pro plan for branch protection enforcement)
- **Drive folder IDs**: Joshua TCX: `1mfG_OUkmrux7GbMsUyisT8p0VjAyWykg`; family member TCX: `1ECoMD1179iFpKgUn4CEqwVoheXpsrfmq`
- **Scott's user ID**: `a5e2d08f-7e41-4e4f-9d69-08c45620391c`