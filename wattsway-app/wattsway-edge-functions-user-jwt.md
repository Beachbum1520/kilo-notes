# WattsWay edge functions use the caller's JWT, never the service-role key

**Decided:** Edge functions (sync-oura, sync-withings, withings-callback, later sync-garmin) build a Supabase client scoped to the caller's JWT with verify_jwt = true, so RLS guarantees each function only touches the caller's rows; provider tokens never reach client code.

**Why:** Isolation between athletes enforced by Postgres RLS.

**Rejected alternatives:** Using the service-role key.

**Would revisit if:** unknown.

**Approx date:** July 2026

**Source:** WattsWay PWA README (unnamed attachment) — Watts Way Fitness App, 2026-06-12
