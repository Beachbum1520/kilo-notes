# [UNCERTAIN] Withings loader/dedupe parsing spec

**Decided:** Scott said "yes" to Claude writing the parsing spec (withings_loader.py): drop zero-weight setup rows, treat zero body-comp as not measured, collapse a weight-only read followed by a complete read within ~10 minutes into the complete one, keep standalone weight-only reads, one row per day. The rules were Claude's, built on Scott's dry-feet correction; explicit adoption beyond "yes, write it" is unconfirmed.

**Why:** To give the Cursor reader clean daily data.

**Rejected alternatives:** Claude's earlier "drop all zero rows" rule (corrected by Scott).

**Would revisit if:** unknown

**Approx date:** June 2026

**Source:** Weighing scale integration rebuild strategy, 2026-06-20
