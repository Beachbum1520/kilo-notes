# WattsWay `daily_metrics` and `user_integrations` tables

`daily_metrics`: one row per athlete per day — hrv_ms, resting_hr, sleep_hours, deep_sleep_hours, rem_hours, sleep_score, readiness, weight_lbs, body_fat_pct, lean_mass_lbs; unique on (user_id, date) so syncs upsert.
`user_integrations`: one row per athlete per provider — access_token, refresh_token, expires_at, status, last_synced_at; unique on (user_id, provider).
Both tables use row-level security so users see only their own rows. Migration file: 20260709120000_daily_metrics_and_integrations.sql.

**Approx date:** July 2026

**Source:** WattsWay PWA README (unnamed attachment) — Watts Way Fitness App, 2026-06-12
