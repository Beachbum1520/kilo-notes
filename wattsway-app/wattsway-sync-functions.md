# WattsWay provider sync functions

sync-oura: calls Oura API v2 (daily_sleep, daily_readiness, sleep) for the last 90 days on first sync, 7 days after; upserts into daily_metrics.
sync-withings: refreshes the Withings access token, fetches body measurements, converts kg → lbs, derives lean mass, upserts into daily_metrics.
withings-callback: exchanges the Withings OAuth2 code for tokens.
Withings app uses scope user.metrics; callback URL https://wattsway.com/settings.

**Approx date:** July 2026

**Source:** WattsWay PWA README (unnamed attachment) — Watts Way Fitness App, 2026-06-12
