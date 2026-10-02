---
name: overview
description: WattsWay family fitness PWA — purpose, architecture, integrations, current state, and what's next
sources: [backfill]
aliases: [WattsWay, Watts Way Fitness, wattsway]
---

## Purpose & scope

- [stated] Scott is building WattsWay (Watts Way Fitness), a private, invite-only family fitness PWA
- [stated] Goal: a unified family fitness platform aggregating health and activity data from Oura, Withings, and Garmin, with dashboards, activity tracking, body composition monitoring, and eventually automated training plan features
- [stated] Scott is the primary builder and user; family members are being progressively onboarded
- [stated] Scott's son Joshua is an experienced developer with GitHub Write access and collaborator status on the repo
- [stated] Scott is tracking a "recomp" goal (Armor Build program) — losing fat while maintaining/gaining lean mass

## Stack & infrastructure

- [stated] Frontend: React/Vite PWA, deployed on Vercel
- [stated] Backend: Supabase (project ref `hzwotatjfltswmiundky`), pg_cron, edge functions in TypeScript
- [stated] Data sources: Oura, Withings, Garmin (Garmin via FitnessSyncer → Google Drive TCX pipeline)
- [stated] GCP project `wattsway-drive` (scott.watts1117@gmail.com), Drive API enabled, service account `wattsway-sync@wattsway-drive.iam.gserviceaccount.com` (Viewer-only on TCX folders)
- [stated] Secrets `GOOGLE_SERVICE_ACCOUNT_EMAIL` and `GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY` stored in Supabase; private key retains literal `\n` escapes and the function un-escapes at runtime
- [stated] Version control: GitHub, private repo, Pro plan for branch protection enforcement
- [stated] IDE/agents: Cursor (local on Windows desktop) plus Cursor cloud agents
- [stated] Branding: Manus.ai used for logo generation
- [stated] Scott's user ID: `a5e2d08f-7e41-4e4f-9d69-08c45620391c`
- [stated] Drive folder IDs — Joshua TCX: `1mfG_OUkmrux7GbMsUyisT8p0VjAyWykg`; onboarded family member TCX: `1ECoMD1179iFpKgUn4CEqwVoheXpsrfmq`

## Current state (as of import — re-verify)

- [stated] Garmin data pipeline fully operational: FitnessSyncer → Google Drive (TCX files) → Supabase edge function `sync-garmin` → `activities` table
- [stated] Six-type activity taxonomy: run, treadmill, strength, walk, breathing (cold plunges, excluded from training load views), generic
- [stated] Oura and Withings integrations are live alongside Garmin
- [stated] Hourly auto-sync scheduler deployed: pg_cron job firing at :15 calls the `sync-all` Supabase edge function, sweeps all users/providers with service-role auth, logs to `sync_runs` table (self-pruning after 30 days); shared sync modules live in `_shared/`
- [stated] Brand assets deployed: Variant 2 red colorway W-mark logo (#FF2D2D→#CC1133 gradient), PWA icon set, `BrandHeader` React component across dashboard and Settings pages
- [stated] Scott's color preference is red
- [stated] Bug fixes shipped: stale-chunk auto-reload; two-row activity card layout; TCX dump-skip regex generalized for timezone offset variance (a family member's files used `-12-00-00` vs. `-08-00-00`); HR regex updated for `xsi:type` attribute tolerance
- [stated] Known issue: Withings OAuth on iOS — the Health Mate app hijacks the OAuth URL inside the PWA; proper fix is queued
- [stated] A family member (user ID `9f2d1573-772e-4d51-babe-6a474164b609`, Drive folder ID `1ECoMD1179iFpKgUn4CEqwVoheXpsrfmq`) is onboarded on Oura and Garmin via FitnessSyncer/Drive; historic run files are missing because FitnessSyncer only fetched run summaries without trackpoint detail

## On the horizon

- [stated] Withings iOS OAuth fix is queued
- [stated] Historic run file recovery for the onboarded family member: Garmin bulk GDPR export → FIT-to-TCX conversion (Claude to handle in-chat) → manual upload to the Drive folder
- [stated] FitnessSyncer backfill edge case: after any historic backfill, `last_synced_at` must be nulled, because FitnessSyncer backdates Drive `modifiedTime` to the activity date, making files invisible to incremental sync windows
- [stated] Shoe/gear tracker (Roadmap #6): native WattsWay feature using activity distance data already in the `activities` table; business rule is that all distance-generating activity types count toward shoe mileage with no exclusions; planned tables `shoes` plus per-activity assignment logic
- [stated] TrainingPeaks API access: application submitted, program currently paused (similar to Garmin's); if granted, slots into the plan builder phase for pushing structured workouts to athlete calendars and reading completed workouts back
- [stated] Garmin official API: access request filed July 10, currently paused with no timeline; architecture is ready to slot it in alongside the Drive lane if/when it reopens
- [stated] Fat mass chart line: dual Y-axis approach recommended for the body composition chart (fat mass on the right axis); agent prompt targeting branch `fat-mass-chart-line` with PR workflow is ready