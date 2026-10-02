# Use one continuous five-category harvest prompt that writes to a -all.md file

**Decided:** Scott wrote a combined harvest prompt. It covers all five categories in one continuous pass, writes straight into a downloadable `<project>-all.md` file (first used as `manila-sales-all.md`), and appends as it goes instead of printing in chat.

**Why:** He wanted no stopping between categories and no asking permission to continue. When the output limit is hit, Claude resumes exactly where it stopped on "continue".

**Rejected alternatives:** The earlier approach of one pass per category, in batches of 10 with a stop after each batch.

**Would revisit if:** Not stated.

**Approx date:** August 2026

**Source:** Extract project history into five categories, 2026-08-05
