# Coach tool v1: read existing data, build no new storage

**Decided:** v1 reads from what already exists (Oura and Withings already land in Google Drive/Sheets via his Apps Script pipelines) and builds no new storage. Manual pasting is fine where automation is hard (RP sessions, Garmin runs). No database, no deploy, no token-refresh service in v1 — local script + simple UI.

**Why:** The coaching engine is the point; automate later only if the tool earns it.

**Rejected alternatives:** Building a database, cloud deploy, or automated ingestion up front.

**Would revisit if:** The tool proves itself and manual steps become worth automating.

**Approx date:** June 2026

**Source:** personal-coach-tool-spec.md — Watts Way Fitness App, 2026-06-12
