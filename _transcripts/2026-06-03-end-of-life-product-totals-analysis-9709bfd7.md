# End of life product totals analysis
Date: 2026-06-03
Conversation: 9709bfd7-42be-4580-b3ef-6029360bad5a
Domain: business-ops

## Summary
**Conversation Overview**

The person works in a sales or business development context and asked Claude to analyze an attached pivot table showing revenue data across a team. The core task was calculating how much of the total revenue figures represented EOL (end-of-life) deals, in both dollars and percentage terms, across three metrics: NRC (non-recurring charges), MRC (monthly recurring charges), and deal count.

Claude initially separated two EOL label types ("EOL" and "Marriott EOL") in the analysis, but the person quickly corrected this approach, stating simply "eol is eol" — indicating a preference for direct, consolidated answers without over-segmentation or unnecessary caveats. The combined EOL figures show EOL represents approximately 24.3% of NRC, 49.9% of MRC, and 60% of deal count. Key colleagues referenced in the data include Amy Keefe, Dave Ruggieri, Lily, and Scott Mora.

The person then reframed the analysis by clarifying that their team handles all EOL deals, and asked Claude to fold Dave Ruggieri's full production into their team's numbers to show a consolidated view of their team's contribution to the overall book. After accounting for overlap (Dave's EOL already included in the EOL bucket), the combined figures show the person's team accounts for approximately 85.8% of NRC, 94.4% of MRC, and 82.2% of total deal count. Claude flagged that the NRC figure is heavily weighted by a single large Marriott Upgrade deal from Dave, and suggested MRC is the more defensible metric if the person is building a case for team value. The person did not respond to this framing.

### SCOTT (2026-06-03T17:31)
review the attached.  how much of the totals are EOL.  in dollars and percent
[File uploaded: 1780507845472_image.png]

### CLAUDE (2026-06-03T17:31)
 I'm looking at a pivot table to calculate what portion of the totals are EOL-related. I need to identify which categories count as EOL—there's a straightforward "EOL" category and also "Marriott EOL" entries, so I'll need to sum both to get the complete picture in dollars and percentages. Now I'm completing Scott Mora's totals and calculating the grand sum across all four team members, then breaking down the EOL items specifically to sum up their NRC values. That gives me 24.31% for the NRC EOL portion. Now I'm moving on to the MRC EOL calculations, adding up the individual amounts across Amy, Amy Marriott, Dave Marriott, Lily Marriott, and Scott Marriott to get a total of $7,833.50, then I'll need to find what percentage that represents of the grand total MRC.

The MRC EOL comes to about 49.86% of the total. For the count-based breakdown, the EOL entries total 27 out of 45 overall, which is 60%. I should probably show both the pure Marriott EOL numbers and the combined EOL figures since the user might be asking about either one.

Looking at just the Marriott EOL lines without Amy's generic EOL entry, the NRC adds up to about 241,319.25, which represents roughly 22% of the total NRC.

For MRC, those same Marriott EOL entries total 7,096.00 (about 45% of MRC), and the count is 24 items out of 45 total (53%). I think the clearest approach is to present all EOL items together as one figure since they're all end-of-life, but I'll call out that there's a standalone generic "EOL" line from Amy that's separate from the Marriott-specific ones.

Scott's an accountant who wants precision and direct analysis with clear tradeoffs, so I should flag this ambiguity explicitly rather than glossing over it. I'll keep the response tight and structured—a small table makes sense here since he's asking for dollars and percentages across different metrics, and that's exactly what tabular data is for.Combining both EOL line types ("EOL" + "Marriott EOL"), here's the breakdown against the grand totals:

| Metric | EOL total | Grand total | EOL % |
|---|---|---|---|
| NRC | $266,252.93 | $1,095,168.77 | 24.3% |
| MRC | $7,833.50 | $15,709.50 | 49.9% |
| Count | 27 | 45 | 60.0% |

One classification flag worth noting: there are two distinct labels in the pivot — a generic **"EOL"** (only Amy Keefe, $24,933.68 NRC / $737.50 MRC / 3 deals) and **"Marriott EOL"** (all four reps). I folded both into the EOL bucket above since both are end-of-life by definition. If your intent is *Marriott EOL only*, the figures drop to:

- NRC: $241,319.25 → **22.0%**
- MRC: $7,096.00 → **45.2%**
- Count: 24 → **53.3%**

The takeaway either way: EOL is a modest quarter of NRC revenue but roughly half of recurring (MRC) and the clear majority of deal *volume* — i.e., lots of small, low-dollar EOL transactions diluting the average deal size, with the big NRC dollars concentrated in Marriott Upgrade work (Dave Ruggieri's $666K alone is 61% of total NRC). Worth deciding whether the generic "EOL" label on Amy's deals is a data-entry inconsistency that should be normalized to "Marriott EOL."

### SCOTT (2026-06-03T17:32)
eol is eol.

### CLAUDE (2026-06-03T17:32)
 Scott's being clear—end of life is end of life, no need to overthink it. I should combine both labels and present the straightforward numbers without second-guessing whether to separate out Marriott's EOL status.Agreed — combined view it is.

| Metric | EOL | Grand Total | % |
|---|---|---|---|
| NRC | $266,252.93 | $1,095,168.77 | 24.3% |
| MRC | $7,833.50 | $15,709.50 | 49.9% |
| Count | 27 | 45 | 60.0% |

EOL is a quarter of NRC dollars but half of recurring revenue and 60% of deal count — small-ticket, high-volume work. The NRC weight sits elsewhere: Marriott Upgrade carries the quarter, with Dave's $666K alone at 61% of total NRC.

### SCOTT (2026-06-03T18:09)
my team does the eol's.  factor in dave's numbers into my team as weel and how does it look

### CLAUDE (2026-06-03T18:10)
 I'm parsing what Scott is asking for—he wants me to combine his team's EOL work with Dave Ruggieri's entire book of business and see what the combined numbers look like. Let me calculate the totals for that scenario. So I need to subtract Dave's EOL portion from his total to avoid double-counting, then add his remaining deals to the EOL bucket to get my team's complete numbers: $939,695.48 NRC, $14,834.00 MRC, and 37 total deals.

Now I'm verifying these calculations against the grand totals—my team represents 85.8% of NRC, 94.4% of MRC, and 82.2% of the deal count—and spot-checking the individual EOL line items to make sure the sums are correct. Now I'm calculating the percentages for my team's allocation: 85.8% of NRC revenue, 94.4% of MRC revenue, and 82.2% of the total count. That leaves the remaining work split between Amy and Lily on non-EOL, non-Dave projects like the Hilton and Marriott change orders and upgrades.

I'm realizing there might be some confusion about who Scott is — there's a Scott Mora in the data who handles a lot of Marriott EOLs, but the user is Scott from Blueprint RF. Since the user mentioned "my team does the EOLs" as a plural, it sounds like the EOL work is handled by a team effort rather than just one person.

Let me double-check my math by verifying the non-team portion adds up correctly to the grand total across NRC, MRC, and count — and it does, so my breakdown is solid.

Now I need to clarify something important: when the user says "factor in Dave's numbers," I interpreted that as attributing all of Dave's production to the team, with deduplication to avoid counting his EOL twice since it's already in the EOL bucket. This gives us the $939,695.48 total, and the math works out the same way regardless of whether we're adding his full book or just his non-EOL portion, since the EOL is already accounted for separately.

I'll present this as "my team" (EOL plus Dave's full production) versus the rest, but I need to flag the deduplication assumption upfront since it directly impacts the final number. Given the user's background in accounting and preference for structured, analytical reasoning with explicit tradeoffs, I'll keep the presentation tight and use a simple table for the financial breakdown—clean formatting without excess.Here's the consolidation. Key mechanic first: Dave's Marriott EOL ($54,621.33 / $677.50 / 3) is *already* in the EOL bucket, so I'm not double-counting it — "your team" = all EOL deals (every rep) **plus** Dave's non-EOL book on top.

| Bucket | NRC | MRC | Count |
|---|---|---|---|
| All EOL (every rep) | $266,252.93 | $7,833.50 | 27 |
| Dave – non-EOL | $673,442.55 | $7,000.50 | 10 |
| **Your team total** | **$939,695.48** | **$14,834.00** | **37** |
| Everyone else | $155,473.29 | $875.50 | 8 |
| Grand Total | $1,095,168.77 | $15,709.50 | 45 |

Your team as a share of the book:

| Metric | Your team | % of total |
|---|---|---|
| NRC | $939,695.48 | **85.8%** |
| MRC | $14,834.00 | **94.4%** |
| Count | 37 | **82.2%** |

What's left to "everyone else" is thin: Amy's Hilton/Marriott change orders + one Marriott New Build ($113K — the only sizable one), Lily's single Marriott Upgrade, and Scott Mora's three change orders. Strip out that one New Build and the residual is ~$42K of NRC across 7 deals.

Two things worth pressure-testing before you take this number anywhere:

The 85.8% is doing a lot of work because Dave's $666K Marriott Upgrade is in it. Your *EOL-native* contribution is 24.3% of NRC — the jump to 85.8% is almost entirely Dave's upgrade book, not EOL volume. If the argument you're building is "my team drives the revenue," fine; if it's "EOL drives the revenue," the data doesn't support that and someone will call it.

Second, MRC at 94.4% is the more durable story than NRC. Recurring revenue is stickier and harder to dismiss as one-off project lumpiness. If you're positioning the team's value, lead with the recurring number, not the one inflated by a single large upgrade.
