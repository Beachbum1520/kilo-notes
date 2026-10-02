# Hourly sync-all cron instead of a single morning run

**Decided:** Schedule a `sync-all` edge function hourly at minute 15 via pg_cron + pg_net ('sync-all-hourly', '15 * * * *'), authenticated with an x-cron-secret header matching the CRON_SECRET function secret.

**Why:** FitnessSyncer's free tier drops Garmin TCX files into Drive overnight at a non-configurable time that varies per user (Scott's from ~2:30 AM to past 4 AM ET); all syncs are idempotent, so hourly is as safe as a fixed time without guessing, and new family connections start syncing within the hour.

**Rejected alternatives:** A single fixed "morning" sync time.

**Would revisit if:** unknown.

**Approx date:** July 2026

**Source:** sync-all hourly cron SQL (unnamed attachment) — Creating a logo for wattsway fitness app, 2026-07-11
