# Garmin ingestion uses TCX files, not FIT

**Decided:** The WattsWay Garmin ingestion lane parses the TCX files FitnessSyncer drops in the "Workout Files TCX" Drive folder. The parallel FIT folder ("Workout Files") stays in Drive as an untouched archive.

**Why:** Scott does not use the Garmin watch strength profile (rep counting), so the set/rep data only FIT carries doesn't matter to him. He said he's not sure anyone uses it: "It's not that great." Claude had recommended TCX for v1 unless that strength data mattered.

**Rejected alternatives:** FIT parsing. It is lossless (strength sets, running dynamics) but needs a binary parser library and is harder to debug. Not needed, since Scott doesn't use the strength profile.

**Would revisit if:** set-level strength data or running dynamics become needed for the plan builder, or daily step counts are wanted (the monitoring dumps are much smaller in FIT).

**Approx date:** July 2026

**Source:** Importing Garmin data with FitnessSyncer, 2026-07-10
