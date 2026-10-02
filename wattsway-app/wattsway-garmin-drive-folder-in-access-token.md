# Garmin provider stores Drive folder ID in access_token column

**Decided:** Add 'garmin' to the user_integrations provider check; Google auth is a single shared service account (drive.readonly, JWT-bearer), each athlete shares their own Drive folder with it, and the per-user folder ID is stored in the existing generic access_token column.

**Why:** The per-user value isn't a secret, and reusing "the one per-user value this provider needs" column avoids a Garmin-only column; athletes stay isolated even though Google credentials are shared.

**Rejected alternatives:** Adding a Garmin-only column; per-user Google OAuth.

**Would revisit if:** unknown.

**Approx date:** July 2026

**Source:** Garmin activities migration SQL (unnamed attachment) — Importing Garmin data with FitnessSyncer, 2026-07-10
