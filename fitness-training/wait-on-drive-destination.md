# Build the FitnessSyncer Drive destination only after backfill completes

**Decided:** Wait to build the Drive destination side until all the historic data has synced ("we probably need to wait until have all the data before doing the drive destination side").

**Why:** Avoids writing a partial file mid-backfill.

**Rejected alternatives:** Wiring the Drive destination immediately.

**Would revisit if:** the historic sync completes.

**Approx date:** July 2026

**Source:** Wc 6/30 - Weekly coaching, 2026-06-29
