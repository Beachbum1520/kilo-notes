# Keep SpO2 in the Oura pipeline rather than dropping it

**Decided:** Fix the SpO2 authorization issue and keep SpO2 in the Oura data pull. This overrode Claude's call to drop SpO2.

**Why:** "We may not need it now, but we may in the future."

**Rejected alternatives:** Dropping SpO2 to avoid the re-authorization work. Claude proposed it because SpO2 was not a tracking priority.

**Would revisit if:** unknown

**Approx date:** June 2026

**Source:** Getting an Oura API key, 2026-06-08
