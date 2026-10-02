# Withings FitnessSyncer export uses 7 columns

**Decided:** The FitnessSyncer Withings destination exports seven columns: Date (US), Weight in LB, Fat Ratio, Fat Free Mass in LB, Fat Mass Weight in LB, Body Muscle Mass in LB, Bone Mass in LB (Scott configured it; the resulting CSV has exactly these).

**Why:** Matches the archive schema (Claude's proposal, implemented by Scott).

**Rejected alternatives:** Scott asked about adding fat mass %, muscle mass %, and water %; Claude recommended skipping them as redundant/noisy and Scott did not add them. [UNCERTAIN whether Scott explicitly agreed]

**Would revisit if:** unknown

**Approx date:** June 2026

**Source:** Weighing scale integration rebuild strategy, 2026-06-20
