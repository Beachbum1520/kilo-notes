# Move provider tokens to Supabase Vault

**Status:** access_token/refresh_token stored as plaintext text columns (RLS owner-only, server-side only). Intended hardening: move them into Supabase Vault so they're encrypted at rest. Left as a follow-up.

**Open questions:** When to change the edge functions' read/write path.

**Blocked on:** Prioritization.

**Last activity:** July 2026

**Source:** WattsWay PWA README (unnamed attachment) — Watts Way Fitness App, 2026-06-12
