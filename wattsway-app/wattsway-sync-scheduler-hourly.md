# Auto-sync scheduler runs hourly, not once a day

**Decided:** The WattsWay auto-sync scheduler (sync-all via pg_cron) runs hourly at minute 15, not once a day at 5 AM ET.

**Why:** Scott raised the concern. FitnessSyncer free accounts sync only once a day at times the user can't choose. A daily run that happens before FitnessSyncer's drop would miss an entire day. Scott suggested running hourly instead.

**Rejected alternatives:** A single daily run at 09:00 UTC (5 AM ET), timed after Scott's own FitnessSyncer drop.

**Would revisit if:** unknown.

**Approx date:** July 2026

**Source:** Creating a logo for wattsway fitness app, 2026-07-11
