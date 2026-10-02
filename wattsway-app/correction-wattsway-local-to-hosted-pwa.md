# WattsWay moved from local Streamlit script to hosted PWA

**What was wrong:** The June 2026 coach-tool spec called for a local Python + Streamlit tool with no database, no auth, no deploy, and reading Google Sheets directly.

**Correct version:** The build became WattsWay: a React + Vite PWA with Supabase (database, invite-only auth, edge functions syncing Oura + Withings into a `daily_metrics` table), deployed on Vercel at wattsway.com, with multiple family users.

**Approx date:** June–July 2026

**Source:** WattsWay PWA README (unnamed attachment) — Watts Way Fitness App, 2026-06-12
