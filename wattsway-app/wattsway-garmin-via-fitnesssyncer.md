# Garmin activities ingested via FitnessSyncer → Google Drive

**Decided:** Garmin runs land as TCX files in a Google Drive folder via FitnessSyncer; a `sync-garmin` edge function reads the folder and upserts parsed activities into `public.activities`.

**Why:** Garmin's official developer API application is still pending.

**Rejected alternatives:** Garmin official API (not yet approved).

**Would revisit if:** Garmin API application is approved (a future Garmin API lane is expected to write to the same table).

**Approx date:** July 2026

**Source:** sync-garmin edge function (unnamed attachment) — Importing Garmin data with FitnessSyncer, 2026-07-10
