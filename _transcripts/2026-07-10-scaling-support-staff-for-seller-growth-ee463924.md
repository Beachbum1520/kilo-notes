# Scaling support staff for seller growth
Date: 2026-07-10
Conversation: ee463924-4855-4ee8-89ea-bcfde6e26705
Domain: business-ops

## Summary
**Conversation Overview**

The person asked Claude to calculate staffing ratios for TDEs (Technical Design Engineers or similar role) and SEs (Solutions Engineers or similar role) based on a baseline of 15 TDEs and 2 SEs supporting 6 sellers, then project those ratios for 25, 50, and 100 sellers. Claude computed the ratios (2.5 TDEs per seller and 1 SE per 3 sellers) and presented the scaled projections in a table format, rounding up to whole numbers since fractional headcount isn't actionable.

Claude also proactively flagged that pure linear scaling typically overstates staffing needs at higher volumes, noting that efficiency gains from standardization, tooling, tiered workflows, and a "three-lane TDE model" (referenced as something already in development) would likely bend the curve downward. Claude suggested presenting the linear ratio as a ceiling alongside a modeled efficiency scenario (10–20% reduction at 50+ sellers) to strengthen the credibility of any staffing proposal. A colleague named Jady was mentioned in connection with the staffing model, suggesting this work is being prepared for a specific stakeholder. Claude offered to build out a more sophisticated model incorporating efficiency assumptions if needed.

### SCOTT (2026-07-10T20:00)
if it takes 15 tdes and 2 se's to support 6 sellers. how may tde's and se's to support, 25 sellers, 50 sellers, 100 sellers

### CLAUDE (2026-07-10T20:00)
I'm calculating the staffing ratios by dividing the current headcount by seller count, then scaling those ratios up for different team sizes—so 2.5 TDEs and roughly 0.33 SEs per seller, which gives me projections of 63 TDEs and 9 SEs for 25 sellers, 125 TDEs and 17 SEs for 50 sellers, and 250 TDEs and 33 SEs for 100 sellers.Using your current ratios — 2.5 TDEs per seller and 1 SE per 3 sellers — here's the linear scale-up (rounding up since you can't staff fractional people):

| Sellers | TDEs (2.5:1) | SEs (1:3) |
|---------|-------------|-----------|
| 6 (today) | 15 | 2 |
| 25 | 62.5 → **63** | 8.33 → **9** |
| 50 | **125** | 16.67 → **17** |
| 100 | **250** | 33.33 → **34** |

One caveat worth raising if this is going into a staffing model for Jady: pure linear scaling almost always overstates need at higher volumes. Support functions typically gain efficiency with scale — standardized designs, better tooling, tiered workflows, and the three-lane TDE model you're building would all bend that curve down. If you want the numbers to survive scrutiny, it may be worth presenting the linear ratio as the ceiling and a modeled efficiency gain (say 10–20% at 50+ sellers) as the realistic ask. Happy to build that version out if useful.
