# WattsWay `activities` table

Unified per-activity schema: id, user_id, source (default garmin), source_format (default tcx), drive_file_id (unique — guarantees no duplicates on re-sync), file_name, activity_type, start_time, duration_seconds, distance_meters, avg_hr, max_hr, calories, created_at.
Owner-only RLS; index on (user_id, start_time desc). Manual entry and a future Garmin API lane are expected to write to the same table.

**Approx date:** July 2026

**Source:** Garmin activities migration SQL (unnamed attachment) — Importing Garmin data with FitnessSyncer, 2026-07-10
