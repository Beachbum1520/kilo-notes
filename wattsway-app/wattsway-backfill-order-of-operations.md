# Order of operations for the scheduler deploy and history backfill

**Decided:** Scott laid out the order: run the scheduler agent prompt, then Danielle upgrades FitnessSyncer, then run the null (reset last_synced_at) command on both their accounts, then resync. Claude confirmed the order and added deploy steps between merge and resets.

**Why:** To get full history into both Scott's and Danielle's accounts.

**Rejected alternatives:** none stated.

**Would revisit if:** unknown.

**Approx date:** July 2026

**Source:** Creating a logo for wattsway fitness app, 2026-07-11
