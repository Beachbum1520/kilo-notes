# Oura → Google Sheet Apps Script

Scott uses a Google Apps Script that pulls Oura data into a Google Sheet tab named "Oura" via OAuth2 (replacing Oura Personal Access Tokens, retired Dec 2025), with self-renewing tokens and merge-by-date writes.
History backfilled from 2024-01-01; daily trigger refreshes the last 14 days; historical sync in 120-day chunks.
Columns: Date, Sleep Score, Total Sleep, REM, Deep, Avg HRV, Lowest RHR, Readiness, Temp Dev, Activity, Steps, Stress High, SpO2.

**Approx date:** June 2026

**Source:** Oura to Google Sheet Apps Script (unnamed attachment) — Wc 6/30 - Weekly coaching, 2026-06-29
