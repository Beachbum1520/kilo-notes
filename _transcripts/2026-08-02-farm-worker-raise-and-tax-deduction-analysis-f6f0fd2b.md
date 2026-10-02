# Farm worker raise and tax deduction analysis
Date: 2026-08-02
Conversation: f6f0fd2b-8ea1-4fa9-8f44-31036afab546
Domain: watts-way-farms

## Summary
**Conversation Overview**

The person operates Watts Way Farms, LLC, a cattle and hog operation in Georgia (Franklin, GA area) run full-time by his wife Angie, who is the LLC owner. He has substantial W-2 income from outside employment. The conversation centered on formalizing payroll for a part-time farm hand named Josh, who had been paid cash with no deductions, and who requested a raise. The person worked through the tax implications of different pay rates and classification structures, ultimately focused on the W-2 route as the legally correct and financially optimal approach.

The discussion covered a wide range of interconnected topics: the contractor vs. employee classification question (concluded W-2 is correct given equipment provision and ongoing relationship), federal and Georgia FICA obligations, federal and Georgia income tax withholding mechanics, UI/SUTA agricultural exemptions (confirmed exempt given Josh's single-worker status), I-9 requirements, Georgia new hire reporting, Form 943 vs. 941 distinctions for agricultural wages, workers' comp exemptions for farm labor, and the hobby loss rules under §183. Regarding the hobby loss analysis, the person confirmed Angie's full-time daily participation and the farm's ability to satisfy the nine profit-motive factors under Treas. Reg. §1.183-2(b), with the farm's losses currently offsetting W-2 income due to material participation. The person also correctly noted that Form 5213 timing works differently than initially described—the conversation clarified that the horse-breeding 2-of-7 safe harbor doesn't apply to cattle operations, and that the standard 3-of-5 test applies. The excess business loss limitation under §461(l) was discussed, with a web search confirming the 2026 threshold reset to lower levels under the OBBBA, though well above any realistic farm loss scenario here.

The person's accountant, described as honest and competent but new to U.S. payroll mechanics, will be handling ongoing compliance. The person decided against upgrading QuickBooks Online for payroll at this time, instead requesting a standalone Excel workbook to help the accountant learn and execute payroll calculations. Claude built a fully functional five-tab workbook (Watts_Way_Farms_Payroll_Calculator_2026.xlsx) implementing the IRS Annual Percentage Method from Publication 15-T and Georgia's 2026 withholding formula, pre-filled with Josh's details, verified against multiple test cases including wage base caps, bracket lookups, exempt toggles, and the Step 2 checkbox schedules. The person consistently preferred precise, mobile-friendly responses with concrete numbers and clear bottom-line summaries, and corrected Claude on the §183 safe harbor details and Form 5213 timing, indicating comfort challenging technical claims.

### SCOTT (2026-08-02T19:19)
My farm help makes $10 an hour cash money under the table. He works only around 10 to 11 hours per week. He wants a raise to $13.50 an hour. I told him if I do that he’s getting a 1099 at the end of the year so I get a tax write off. Estimate the benefit to me from a farm expense. And what will it cost him. He won’t make enough to have to pay income tax

### CLAUDE (2026-08-02T19:20)
I'm working through the tax implications for Scott. He's looking at roughly 546 hours of farm labor annually, which translates to either $5,460 or $7,371 depending on the wage rate. The key benefit is that deducting this expense on Schedule F reduces his taxable income—with his substantial W-2 earnings, he'd see a marginal tax savings at the federal level (22-24%) plus Georgia's state rate of 5.39%.

But here's the critical issue: if he's been paying cash under the table, he likely hasn't been deducting those wages at all, so the full $7,371 becomes the incremental deduction. However, there's a bigger problem lurking—classifying a farm worker as a 1099 contractor when they're working regularly under his direction is probably misclassified. Agricultural labor has specific rules under Form 943 and FUTA, with thresholds at $150 or $2,500 in annual payroll that trigger withholding and employer payroll tax obligations.

If he issues a 1099 for someone who's really an employee, he'd owe employer FICA of about 7.65% (~$564), though FUTA might be exempt depending on the farm's size. For the worker, the self-employment tax hit is substantial—about $1,041 on $7,371 in net earnings, even though there'd be no income tax owed since the standard deduction covers it. I should flag the misclassification issue directly given his focus on epistemic precision, and note that I'm not a tax advisor.

The worker could partially offset this through EITC—at $7,371 single with no dependents, he'd qualify for roughly $630, which helps. He'd also earn 4 quarters of Social Security coverage, which is a meaningful long-term benefit. So while the raise adds $1,911 gross, the self-employment tax reduces the net gain to around $870.

Looking at the effective hourly rate: the $3.50 bump (35% raise) shrinks to about $1.59/hr after SE tax, bringing his take-home to roughly $11.59/hr. But here's the key insight—Scott's actual out-of-pocket cost for the raise is only about $5,270 after accounting for tax savings, which is actually cheaper than what he's currently paying in cash. The raise essentially pays for itself.

Now I need to lay out the tax implications clearly for mobile viewing. I'm uncertain about Scott's federal bracket, so I'll model both 22% and 24% scenarios, plus Georgia's state rate around 5% (with a note to verify the 2026 rate after recent legislation). This gives me marginal rates of 27% and 29% to work with for the calculation.

I should also flag the farm loss issue since it's never been profitable — there's a real hobby loss risk under the IRS tests, and whether those losses can offset his W-2 income depends on material participation and for-profit intent. That's worth a brief mention given the pattern of losses.**Hours baseline:** 10.5 hrs/wk × 52 = ~546 hrs/yr → $5,460 at $10, **$7,371 at $13.50** (+$1,911 gross).

**Your side — the write-off**

Right now the cash is presumably not deducted, so you're paying $5,460 with post-tax dollars. Deducting $7,371 on Schedule F saves you your marginal federal rate plus GA (~5%, flat rate stepping down — verify the 2026 number):

- At 22% fed + 5% GA → ~$1,990 saved
- At 24% fed + 5% GA → ~$2,138 saved

Net cost of the raise: roughly **$5,235–$5,380** — slightly *less* than the $5,460 you're spending now. The raise pays for itself.

Two caveats. First, no SE-tax savings, since the farm runs at a loss — it's income-tax only. Second, a farm that's never shown a profit and keeps taking losses against W-2 income is where the hobby-loss test (profit in 3 of 5 years) bites. More documented deductions help the paper trail but deepen the loss.

**His side — the 1099**

You're right that he owes no income tax (standard deduction ~$16,100 single). But self-employment tax starts at $400 of net earnings:

- Net earnings: $7,371 × 92.35% = $6,807
- SE tax at 15.3% = **~$1,041**

So his take-home is $6,330, or **$11.59/hr effective** — not $13.50. Against $10 tax-free now, his real raise is $1.59/hr, not $3.50. He should know that before he agrees, and he'll need to file and probably make quarterly estimates.

Two things that soften it for him: at that income he likely qualifies for EITC (~$600 range if single, no kids), and $7,371 earns him all 4 Social Security credits for the year.

**The classification flag**

If he works your hours, with your equipment, under your direction, he's an employee, not a contractor — and a 1099 is a misclassification. Ag labor triggers withholding at $150 paid to one worker, and you'd file Form 943 and owe the employer half of FICA (~$564 on $7,371). Done correctly, his cost drops to ~$564 and yours rises by about the same. Worth running past your accountant before you commit to the 1099 — I'm not a tax pro, and this is the part with real exposure.

### SCOTT (2026-08-02T19:22)
He works the hours he wants to work. He picks schedule. But does use my equipment

### CLAUDE (2026-08-02T19:22)
The user's pushing back on how I classified this, so I need to be fair about the gray areas—schedule control and equipment provision lean toward employer status, while contractor arrangements and equipment ownership point the other way. Agriculture has its own wrinkles worth acknowledging. I should lay out the actual factors that matter: behavioral control, financial control, and the nature of the relationship itself. Setting your own hours helps the independent contractor argument, but it's not the deciding factor. When an employer provides equipment and tools, that's a strong signal they're the employer. The absence of profit or loss opportunity, no investment on the worker's side, no other clients, an indefinite ongoing relationship, and work that's core to the business—these all stack toward employment status. I'll keep this concise and grounded, not preachy.

There's also the federal versus Georgia angle to consider, and the FLSA has its own economic realities test that differs from the IRS approach. The small-farm exemption under FLSA—the 500 man-day rule—handles minimum wage and overtime separately from tax classification. The real enforcement risk isn't high for small cash farm labor, but it surfaces when someone files a Schedule C and then faces an audit, or files an SS-8, or claims unemployment or workers' comp after an injury. An injury on the farm is where the actual exposure lives. Georgia exempts farm laborers from workers' comp requirements, which is worth flagging as a separate protection.Schedule control is a real point in your favor — it's one of the behavioral-control factors, and it's the one people most often fail. But it's one factor among several, and the others lean the other way:

- **Equipment** — contractors typically bring their own tools. Yours is his.
- **No profit/loss opportunity** — he can't make more by working efficiently or lose money on a job. He's paid by the hour, which is the single most employee-like payment structure.
- **No other clients, no business** — no LLC, no insurance, no advertising, not holding himself out to other farms.
- **Integral to the business** — he's doing farm work on a farm. Courts weight this heavily. A contractor is more like the guy who comes to fix your well.
- **Indefinite, ongoing** — not project-scoped with an end date.

Setting hours plus using your equipment is a common pattern for casual employees, not a contractor signature.

That said, here's the practical read: enforcement on small cash ag labor is rare, and nobody's auditing your Schedule F over $7,371. The realistic trigger isn't the IRS — it's **an injury**. If he gets hurt working your hogs or cattle and files for workers' comp or unemployment, the classification gets decided by someone else, retroactively, with penalties. Georgia exempts farm laborers from mandatory workers' comp coverage, which cuts your exposure some, but you'd want to confirm that with your carrier rather than take it from me.

Second trigger: he files a Schedule C, sees the $1,041 SE bill, and files Form SS-8 asking the IRS to rule. That determination is binding and lands on you.

Worth ten minutes with your accountant. Form 943 with $564 of employer FICA is cheap insurance compared to a retroactive determination, and it's a cleaner deduction than a 1099 that could be challenged.

### SCOTT (2026-08-02T19:25)
Right now I pay him out of my personal account with post tax dollars. If I give him a raise, then he would at a minimum get a 1099 from me. Give me the cost summary to me and him for both the 1099 and the w2 route

### CLAUDE (2026-08-02T19:25)
Now I'm working through the financial comparison between the two compensation structures. With the raise to $13.50/hour, that comes to $7,371 gross. For the 1099 route, Scott would deduct those wages on Schedule F, which gives him a tax savings of roughly $1,990 to $2,138 depending on whether we use a 27% or 29% combined federal and state tax rate.

For the W-2 route, Scott's total outlay is higher because he'd owe employer FICA of about $564 on top of the $7,371 in wages, bringing his total cost to $7,935. That deduction yields $2,142 to $2,301 in tax savings, so his net cost lands between $5,634 and $5,793. I'm also factoring in potential payroll processing costs of $400–600 annually, though he could handle it himself with Form 943. FUTA and Georgia SUTA don't apply here since he doesn't meet the agricultural worker thresholds.

The key difference for the worker: under 1099 he nets $6,330 (about $11.59/hr after self-employment tax), while under W-2 he nets $6,807 (about $12.47/hr) since he'd only owe employee FICA with no income tax withholding required. So the W-2 route puts roughly $477 more in his pocket.

For Scott, the 1099 route costs $5,233–$5,381 net, while W-2 costs $5,634–$5,793 before admin fees—roughly $400 more expensive. I need to build out a clean comparison table showing both tax brackets to make this concrete.

Since he's paying from personal post-tax dollars with no deduction currently, the baseline is $5,460 real cost. For the W-2 route, the FICA threshold is straightforward: he's over both the $150 per-employee and $2,500 aggregate tests, so wages are subject to FICA. Income tax withholding would normally apply but he can likely claim exempt on the W-4 if he has no tax liability, so expect zero withheld. I should note the payroll admin cost and calculate his effective hourly rate to round out the picture.**Assumptions:** 546 hrs/yr, $7,371 gross at $13.50. Combined marginal rate shown at 27% (22% fed + 5% GA) and 29% (24% + 5%). Baseline today: you spend **$5,460 post-tax, zero deduction**; he nets $5,460 clean.

**Your cost**

| | 1099 | W-2 |
|---|---|---|
| Gross paid | $7,371 | $7,371 |
| Employer FICA (7.65%) | $0 | $564 |
| **Total outlay** | **$7,371** | **$7,935** |
| Deduction value @27% | −$1,990 | −$2,142 |
| **Net cost @27%** | **$5,381** | **$5,793** |
| **Net cost @29%** | **$5,233** | **$5,634** |
| Admin | none | Form 943 annually; payroll service $400–600/yr if you don't DIY |

**His cost**

| | 1099 | W-2 |
|---|---|---|
| Gross | $7,371 | $7,371 |
| SE tax (15.3% on 92.35%) | $1,041 | — |
| Employee FICA (7.65%) | — | $564 |
| Income tax | $0 | $0 (files W-4 exempt) |
| **Net to him** | **$6,330** | **$6,807** |
| **Effective hourly** | **$11.59** | **$12.47** |
| Filing burden | Schedule C + SE, quarterly estimates | none — he may not even need to file |

**The bottom line**

The W-2 route costs you about **$400 more** net and gives him about **$477 more**. That's the whole spread. You're buying correct classification, no SS-8 risk, no retroactive exposure if he gets hurt, and a deduction nobody can challenge — for roughly $400 a year.

Two things worth confirming with your accountant: you're almost certainly under the FUTA ag thresholds ($20,000 in a quarter, or 10+ workers for 20 weeks), and Georgia SUTA has similar ag exemptions — so those are likely $0, but don't assume it.

And either way, both routes beat what you're doing now. Even the W-2 at $13.50 costs you about $175–330 *more* than the $5,460 you currently spend with no deduction at all. Standard caveat — I'm not a tax professional, and the classification piece in particular is worth the ten minutes.

### SCOTT (2026-08-02T19:27)
Give me the scenarios at $12 per hours.

### CLAUDE (2026-08-02T19:27)
Now I'm comparing the tax implications between a 1099 contractor arrangement and a W-2 employee setup for this hourly rate. With the 1099, after self-employment taxes he'd net about $10.30 per hour, while as a W-2 employee with employer FICA contributions he'd take home roughly $11.08 per hour, though the total cost to the employer would be higher. I'm starting to look at what deduction values might apply to each scenario.**Assumptions:** 546 hrs/yr → $6,552 gross at $12.00. Baseline today: you spend **$5,460 post-tax, no deduction**; he nets $5,460 clean.

**Your cost**

| | 1099 | W-2 |
|---|---|---|
| Gross paid | $6,552 | $6,552 |
| Employer FICA | $0 | $501 |
| **Total outlay** | **$6,552** | **$7,053** |
| **Net cost @27%** | **$4,783** | **$5,149** |
| **Net cost @29%** | **$4,652** | **$5,008** |

**His cost**

| | 1099 | W-2 |
|---|---|---|
| Gross | $6,552 | $6,552 |
| SE tax | $926 | — |
| Employee FICA | — | $501 |
| Income tax | $0 | $0 |
| **Net to him** | **$5,626** | **$6,051** |
| **Effective hourly** | **$10.30** | **$11.08** |

**Why $12 is the interesting number**

At $12, *both* sides beat the status quo — which wasn't true at $13.50.

- You spend **$311–$808 less** than the $5,460 you're paying now, depending on route and rate.
- He nets **$166 more** on the 1099, **$591 more** on the W-2.

The deduction is doing the work. You're converting post-tax dollars into pre-tax ones, and that gap funds most of the raise.

The catch on the 1099 column: his effective rate is $10.30/hr against $10.00 cash today. That's a 3% raise in his pocket, not a 20% one, and he now has to file a Schedule C. He may not see that as a raise at all. On the W-2 he gets $11.08 effective with no filing burden — a real, visible bump.

If the goal is for him to *feel* the raise while you spend less than you do today, **W-2 at $12** is the cleanest cell in these tables. And it's the correctly classified one.

### SCOTT (2026-08-02T19:29)
What is his effective pay rate going the W-2 route. And what is my effective cost per hour with that rate

### CLAUDE (2026-08-02T19:29)
**W-2 at $12.00/hr, 546 hrs**

**His effective rate:** $6,051 ÷ 546 = **$11.08/hr** take-home (after his $501 FICA, no income tax).

**Your effective cost:** total outlay $7,053 ÷ 546 = $12.92/hr before the deduction. After the write-off:

- @27% → $5,149 ÷ 546 = **$9.43/hr**
- @29% → $5,008 ÷ 546 = **$9.17/hr**

**The spread that matters**

You're at roughly **$9.20–$9.43/hr net** — *below* the $10.00/hr you're paying now — while he goes from $10.00 to $11.08. Both sides come out ahead because the deduction absorbs the difference.

One thing that doesn't show in the hourly math: his FICA buys him Social Security and Medicare credits. $6,552 earns all four quarterly credits for the year, which the cash arrangement gives him nothing toward.

### SCOTT (2026-08-02T19:29)
Run it at $13.50

### CLAUDE (2026-08-02T19:30)
**W-2 at $13.50/hr, 546 hrs**

**His effective rate:** $6,807 ÷ 546 = **$12.47/hr** take-home.

**Your effective cost:** total outlay $7,935 ÷ 546 = $14.53/hr before the deduction. After:

- @27% → $5,793 ÷ 546 = **$10.61/hr**
- @29% → $5,634 ÷ 546 = **$10.32/hr**

**Side by side, W-2 route**

| | $12.00 | $13.50 |
|---|---|---|
| His effective | $11.08 | $12.47 |
| Your effective @27% | $9.43 | $10.61 |
| Your effective @29% | $9.17 | $10.32 |

**The read**

At $13.50 you cross back over $10/hr — you're paying $0.32–$0.61/hr more than the cash arrangement costs you today. That's **$175–$330 over the year**. He gains $1.39/hr over the $12 scenario, or about $756.

So the question is whether $175–$330 of your money is worth $756 of his. That's a retention call, not a tax one.

### SCOTT (2026-08-02T19:31)
Summarize the for a text message to Angie. Both at $12 and $13.50 per hour. The w-2 route only.

### CLAUDE (2026-08-02T19:31)
Ran the numbers on giving [name] a raise. Best route is putting him on a W-2 instead of paying cash — it's the correct classification anyway since he uses our equipment, and it protects us if he ever gets hurt out here.

At $12/hr: he takes home $11.08/hr after his FICA. Costs us about $9.20–$9.40/hr after the tax write-off. That's LESS than the $10/hr we're paying him now, because right now we get no deduction at all.

At $13.50/hr: he takes home $12.47/hr. Costs us about $10.30–$10.60/hr after the write-off. So roughly $175–$330 more per year than what we're spending today.

Either way he gets a real raise and we spend about the same or less. The $13.50 version costs us ~$300 more a year but puts ~$750 more in his pocket. Both also get him Social Security credits he's earning nothing toward right now.

Only extra work on us is a Form 943 once a year. Want me to talk to the accountant before I tell him anything?

### SCOTT (2026-08-02T19:34)
I keep him to fill out W4. Do I need him to do an i9 as well or just get a copy of his dl?

### CLAUDE (2026-08-02T19:34)
Yes — Form I-9 is required for every employee, no exceptions for farm labor or part-time. A copy of the driver's license alone doesn't satisfy it.

The catch is that a driver's license is only a **List B** document (identity). You need either one List A document, or one List B *plus* one List C (work authorization). So DL + Social Security card, or DL + birth certificate, or just a U.S. passport by itself.

A few mechanics worth knowing:

- Section 1 (his part) on or before his first day; Section 2 (your part) within 3 business days.
- You must physically examine the original documents. He picks which ones to present — you can't demand a specific one.
- Don't file it with anyone. Keep it separate from his personnel file, 3 years from hire or 1 year after termination, whichever is later.
- Copying documents is optional, but if you copy for one employee you should copy for all. Consistency is what keeps you out of discrimination trouble.

Also worth getting at the same time: **Form G-4** (Georgia's state withholding certificate — the W-4 only covers federal), and his SSN for the W-2 itself.

One flag since he's been paid cash: the I-9 is dated from hire. If you're formalizing an existing arrangement, ask your accountant how to handle the start date — treating it as a new hire on the date payroll begins is usually the cleanest, but that's their call, not mine.

### SCOTT (2026-08-02T19:36)
What the cutoff for 0%

### CLAUDE (2026-08-02T19:37)
I'm figuring out the income tax cutoff point—the standard deduction threshold where no federal income tax is owed. For 2026, I'm using $16,100 as the projected standard deduction for a single filer, though there's some uncertainty around that figure. At 546 hours of work, that would bring gross wages right to that $16,100 mark.

I also need to account for Georgia's own state income tax, which has a $12,000 standard deduction for single filers and a flat rate around 5.19% (stepping down to about 5.09% in 2026). And I should note that FICA taxes apply from the first dollar earned—the 0% cutoff only applies to income tax. There's also the EITC phase-in to consider. I want to present both the federal and Georgia cutoffs with the hourly equivalent, keeping it concise for mobile viewing.**Federal:** he owes $0 income tax up to the standard deduction — **$16,100** for a single filer in 2026 (worth a quick verify with your accountant; that's the inflation-adjusted figure). At 546 hrs/yr, that's **$29.49/hr** before he'd owe a dime of federal income tax.

**Georgia:** lower bar. GA's standard deduction is $12,000 single, so he'd start owing state tax above that — **$21.98/hr** at his hours. GA's flat rate is around 5.1% and scheduled to keep stepping down, so even at $25/hr he'd owe roughly $60–70 in state tax.

**What doesn't have a cutoff:** FICA. The 7.65% comes out of dollar one regardless — no threshold, no exemption. So "0%" only ever means income tax.

Practical upshot: at $12 or $13.50 he's nowhere near either line. You'd have to nearly double his rate before federal kicks in, and he'd have to clear about $22/hr before Georgia does. If he ever picks up a second job, though, the two incomes stack — that's when he'd need to stop claiming exempt on the W-4.

### SCOTT (2026-08-02T19:59)
My personal W-2 income that this schedule F gets netted against is almost 400,000 per year gross I may be in a higher bracket than the 29%

### CLAUDE (2026-08-02T19:59)
Looking at the 2026 tax brackets for married filing jointly, with a gross income around $400K, I'm calculating where that falls in the bracket structure—the 24% bracket tops out around $410K and the 32% bracket starts shortly after, so I need to figure out the taxable income after the standard deduction to see which bracket applies.

Filing status is crucial here since single filers hit the 32% bracket much earlier (around $205K taxable), which would push him into the 35% bracket at $400K gross. But married filing jointly keeps him in the 24% bracket, plus Georgia's ~5.1% state rate. The farm loss is the key variable—it reduces ordinary income at whatever his marginal rate is, and if it's large enough, it could shift him between brackets entirely.

The hobby loss rules are the real concern at this income level, not the tax rate mechanics themselves. Filing status is the key variable I'm missing — most likely he's filing married filing jointly given he's married to Angie and using Schedule F, but I should present both scenarios and keep the format mobile-friendly.Filing status swings this a lot, so both:

**Married filing jointly** (likely, given Angie): $400K gross − ~$32K standard deduction ≈ $368K taxable. The 32% bracket for MFJ doesn't start until roughly $410K taxable in 2026. So you're probably still **topped out at 24%** — meaning 29% combined is right after all.

**Single/separate:** $400K gross lands you in the **35%** bracket, and combined runs ~40%.

**W-2 route, effective cost per hour to you:**

| Combined rate | $12.00 | $13.50 |
|---|---|---|
| 29% (24% fed) | $9.17 | $10.32 |
| 37% (32% fed) | $8.12 | $9.14 |
| 40% (35% fed) | $7.74 | $8.71 |

At 40%, even $13.50/hr costs you less than $9 — well under the $10 you're paying in cash today.

Two things that matter more than the bracket question:

**The Additional Medicare tax doesn't help you.** The 0.9% surtax over $250K MFJ is on wages, and a Schedule F loss doesn't reduce W-2 wages. Same for NIIT — wages aren't subject to it. So the farm deduction only works against ordinary income tax.

**The bigger flag:** at $400K of W-2 income with a farm that's never been profitable, you're the exact profile the hobby-loss rules target. Three profitable years out of five is the safe harbor, and you don't have them. That doesn't make the deduction wrong — it makes documentation of profit motive (business plan, separate books, the beef segment's actual margins) the thing that protects it. Worth a real conversation with your accountant, not just on this $7K but on the whole Schedule F posture.

Verify the 2026 bracket thresholds and GA's current flat rate with them — those numbers move.

### SCOTT (2026-08-02T20:01)
I’m pretty sure the eight or nine rules or whatever it is that the government mandates for a business I can check every single box there is. We just don’t make a profit. And many many many big corporations never make a profit and it’s OK.

### CLAUDE (2026-08-02T20:01)
You're right about the nine factors — Treas. Reg. §1.183-2(b), and if you genuinely check them all, that's the ballgame. Profit motive is the test, not profit. Separate books, business plan, expertise, time invested, changing methods when something isn't working, expectation of asset appreciation. You've got a real one: the Dexter beef whole/half segment is documented as profitable at the segment level, and your strategic shift toward boxes and retail cuts is exactly the "changed operating methods in response to losses" factor. Land appreciation on 90 acres counts too.

Where I'd push back a little is the corporate comparison. Amazon and Uber were losing money on their own returns — nobody was netting those losses against a separate salary. What draws attention isn't losing money; it's the *combination* of sustained losses, high outside wage income, and an activity that has recreational appeal to a lot of people. Farming, horses, and aircraft are the classic three. That's a scrutiny profile, not a verdict.

Two practical notes:

The 3-of-5 safe harbor is just a presumption shift. Without it, you carry the burden of proving motive rather than the IRS carrying the burden of disproving it. Very winnable if your file is what you say it is — but it means the file has to be assembled, not just true.

And **Form 5213** lets you elect to defer the determination until the fifth year, which stops the clock on assessment. Some accountants like it, others say it's a flag that invites the look. Worth asking yours which camp they're in.

None of that changes the answer on your farm hand. Put him on a W-2, take the deduction, it's a legitimate labor expense either way.

### SCOTT (2026-08-02T20:02)
I believe for the 5213 you wait until they question your profitability on the three out of five year and then you file it. And it’s worth no team that Angie is the full-time farmer. The LLC is in her name. She works at every single day. We just happen to be filing jointly since we’re married.

### CLAUDE (2026-08-02T20:03)
I need to clarify two key points here. On the 5213 timing issue, Scott's partially correct — there is a provision to file after being questioned, but it's specifically a 60-day window following a notice of deficiency, not an indefinite window waiting for them to ask. And I need to address the Angie-as-owner question as well.

The statute lays this out as: the election must be filed within 3 years of the first year's return due date, OR within 60 days of receiving written notice from the IRS proposing to disallow deductions — whichever comes first. So the notice route doesn't extend the deadline beyond 3 years; it actually accelerates it if the IRS acts before that window closes. If the farm's been operating for many years, that initial 3-year window is likely already gone, leaving only the notice-triggered 60-day path as a viable option.

For Scott's situation, this is probably worth flagging directly — his farm likely started too long ago for the standard 3-year election, so I should suggest he verify the timeline with his accountant rather than assume the longer window applies.

On Angie's side, her full-time involvement is genuinely strong evidence of profit motive under the hobby loss factors. The LLC structure itself is fine — as a disregarded single-member entity, it flows to their joint return either way, and losses offset his W-2 income legally. What's particularly valuable here is that her material participation also shields the losses from passive activity loss limitations under a separate statute, which is distinct from the hobby loss analysis but reinforces the overall picture. Her daily work effort is one of the strongest factors the IRS looks at, and it's clearly not recreational.

The excess business loss cap probably isn't worth mentioning — their farm losses are well below the $626K threshold for married filing jointly, so there's no constraint there.On the 5213 timing, I think it's narrower than that. The election has to be made within **3 years after the due date of the return for the first year of the activity**. The notice route — 60 days after the IRS sends written notice proposing to disallow — isn't an extension past that window; it's a shortened deadline if the notice arrives early. So if the farm has been running more than three years, the 3-year window is likely closed and 5213 may not be available at all. Worth having your accountant confirm the read rather than counting on it being there later.

Angie's role is the stronger card anyway, and it does two separate jobs:

**Hobby loss (§183)** — full-time daily labor is one of the heaviest factors in the nine. Someone working a farm every day, year-round, in Georgia summers is not doing it recreationally. That's the factor that's hardest for the IRS to argue with.

**Passive activity loss (§469)** — this is a *different* rule and a real trap you're already clear of. Losses from an activity you don't materially participate in get suspended, not deducted against wages. Angie's daily participation blows past the material-participation tests, and on a joint return her participation counts for both of you. So the losses are active and properly offset your W-2.

The LLC being in her name doesn't change much mechanically — single-member LLC is a disregarded entity, flows to Schedule F on the joint 1040 either way. But it's consistent with the story, and consistency is what the file is made of.

The one thing I'd actually do: make sure the documentation matches the reality. Contemporaneous log of her hours, the business plan, segment-level P&L showing the beef enterprise works. You have the facts. The question is whether they're written down anywhere.

### SCOTT (2026-08-02T20:05)
Maybe it’s not the 5213 form I’m thinking about but for Farms there’s a form specifically for the hobby law and I think it extends it to seven out of 10

### CLAUDE (2026-08-02T20:05)
The horse-breeding exception under §183(d) uses a 2-of-7-year test rather than the standard 3-of-5, but it's still filed on Form 5213—there's no separate form for it. So while the extended window does exist, it's specifically for activities that are predominantly horse-related, not farms generally.There is an extended window, but it's horses, not farms generally — and it's **2 profitable years out of 7**, not 7 of 10. §183(d) carves out activities consisting in major part of breeding, training, showing, or racing horses. Cattle and hogs don't qualify; you're on the standard 3-of-5.

And there's no separate farm hobby-loss form. Form 5213 is the only election form, and it covers both versions — same form, different window depending on whether it's a horse activity (7 years) or everything else (5 years).

So the two things you may be blending: the 2-of-7 horse presumption, and the 5213 election timing. Neither gets you a longer runway on a cattle and hog operation.

What farms *do* get that's real and worth more to you than either:

- **Schedule F income averaging (Form 1040 Schedule J)** — spread a high-income farm year back across the prior three. Only useful in a profitable year, but worth knowing exists.
- **NOL carryforward** — farm losses that exceed current-year offset capacity carry forward indefinitely at 80% of taxable income.
- **Excess business loss limit (§461(l))** — the one that could actually bite you. Around $640K MFJ for 2026, so a $7K farm hand expense is nowhere near it, but if you ever have a big equipment or infrastructure year against $400K of wages, that's the cap to watch. Disallowed amounts convert to NOL carryforward rather than disappearing.

Your accountant can confirm the current-year thresholds — those all index annually.

### SCOTT (2026-08-02T20:07)
Look up and see if you can find what the excess business loss limit is for 2020

### CLAUDE (2026-08-02T20:07)
The CARES Act suspended the excess business loss limitation under Section 461(l) retroactively for 2018, 2019, and 2020, so there was no limit that year. The threshold that would have applied was $259,000 for single filers and $518,000 for married filing jointly, adjusted for inflation in 2020. I should verify these specific figures to be certain.

For 2020, the CARES Act eliminated the contribution limit entirely, though the standard threshold would've been $259,000/$518,000 if it applied. Form 461 also didn't exist that year. Scott might be asking about an amended return or a carryover loss, though the three-year amendment window has already closed by now.**There was no limit for 2020.** The CARES Act retroactively suspended the rule, so noncorporate taxpayers could deduct excess business losses arising in 2018, 2019, and 2020 without limitation. Form 461 didn't even exist for the 2020 tax year — it came back starting in 2021.

The number that *would* have applied absent the suspension: $259,000 single, $518,000 for joint filers in 2020 — the inflation-adjusted version of the original $250K/$500K.

The limitation resumed for tax years beginning after Dec. 31, 2020. It's since been extended past the original 2025 sunset, which is why there's still a threshold to watch in 2026.

One practical note if you're looking backward: the amended-return window for 2020 closed in 2024, so if there's a 2020 loss question in play it's likely too late to do anything about it directly. Any unused loss would have carried forward as an NOL rather than disappeared, though — worth asking your accountant whether there's a carryforward balance sitting on your returns that you're not tracking.

### SCOTT (2026-08-02T20:08)
Look up and see if you can find what the business loss limit is for 2026

### CLAUDE (2026-08-02T20:08)
I need to find the 2026 excess business loss limit, which should be inflation-adjusted from the 2025 amount of $313,000 for single filers and $626,000 for married filing jointly—my estimate is around $320,000 and $640,000 respectively, especially since the One Big Beautiful Bill Act made this provision permanent in July 2025.

I need to correct my earlier calculation—the 2026 threshold is actually $512,000 for MFJ and $256,000 for single filers, which is down from 2025's $626,000. The key distinction I was missing is that the excess business loss limitation restricts how much business losses can offset nonbusiness income once you exceed that threshold, not how much total loss you can claim. In Scott's case, his farm loss is nowhere near that $512,000 ceiling, so this limitation wouldn't apply to him anyway. I should also remember that W-2 wages paid by the business factor into these calculations.**$512,000 married filing jointly, $256,000 single** for 2026.

I owe you a correction — I said "around $640K MFJ" earlier. That was wrong, and wrong in the direction that matters. The OBBBA made the limitation permanent and reverted the thresholds to the original TCJA amounts, so they *decreased* in 2026 from 2025's $313,000/$626,000. I was extrapolating the old inflation trend forward instead of accounting for the reset.

That's roughly $114,000 less deductible loss for a joint filer than in 2025 — the indexing methodology was rolled back, erasing several years of inflation creep.

**What it means for you:** still nowhere close. Your farm loss would need to exceed $512K in a single year to hit it. Even a big EQIP-year equipment purchase with Section 179 wouldn't get you there.

One detail worth knowing given your setup: the calculation runs on Form 461, pulling in Schedule F farm income among other business lines. But W-2 wages from employment are *excluded* from the business-income side of that calculation — a CARES Act technical correction settled that. So your $400K salary doesn't offset the farm loss inside the Form 461 math; it's purely the nonbusiness income the loss is being applied against.

The relevant number for you stays the same: nine profit-motive factors and Angie's material participation, not the EBL ceiling.

### SCOTT (2026-08-02T21:42)
What about Georgia state taxes.

### CLAUDE (2026-08-02T21:42)
I need to look up Georgia's 2026 tax conformity details—specifically the flat rate, standard deduction, and whether the state conforms to the §461(l) limitation. My notes indicate Georgia conforms to Section 179 but not bonus depreciation, so I'll need to find the current 2026 rate.

For Georgia's 2026 tax rate, I'm seeing conflicting information on the standard deduction — the state Department of Revenue lists it as $15,000 for single filers and $30,000 for married filing jointly, but another source suggests those amounts don't take effect until 2027, with $12,000/$24,000applying in 2026 instead. I need to flag this discrepancy since the official DOR page should be authoritative but the timing doesn't align with what the other source claims.

For Scott's situation specifically, the standard deduction is less critical since he's likely itemizing at his income level, and even with the SALT cap changes, it won't significantly impact his calculation. What matters more is confirming Georgia's conformity to federal Section 461(l) rules on farm losses, verifying how the state treats hobby losses, and understanding the payroll tax obligations — I don't have complete information on the 461(l) conformity piece yet. Now I'm organizing the response: I'll walk through the combined rate to confirm the 29% figure, explain how the farm loss gets treated under Georgia rules, cover the employer-side withholding and SUTA obligations, and flag the standard deduction issue — keeping it tight for readability.**Rate:** Flat 4.99% for 2026, cut from 5.19% under HB 463 — three years ahead of the original glide path. It steps down 0.125 points annually toward 3.99%.

So my 5% assumption held up. Your combined marginal rate of **29% (24% federal + 4.99% GA)** is right, and all the effective-cost-per-hour numbers I gave you stand.

**The farm loss at the state level**

Georgia starts from federal AGI, so the Schedule F loss flows through automatically — no separate state election or form. The nine-factor hobby test and material participation are federal determinations Georgia follows. What Georgia *doesn't* follow is bonus depreciation (it conforms to §179 instead), which matters when you start buying EQIP-related equipment but not for a labor expense.

One thing I can't confirm from these results: whether Georgia conforms to the §461(l) excess business loss limitation. Some states decouple. Academic for you at $7K of wages, but worth asking your accountant if you ever have a large infrastructure year.

**Employer side, if you go W-2**

- **Form G-4** — Georgia's withholding certificate, separate from the federal W-4. He can claim exempt on both at his income.
- **Georgia SUTA** — agricultural labor is generally exempt below the same thresholds as FUTA ($20,000 in a quarter or 10+ workers). You're almost certainly $0, but confirm with the Georgia DOL.
- **Form G-7** — quarterly withholding return if any GA tax is withheld. If he's exempt, likely nothing to remit, but registration may still be required.

**One flag:** sources conflict on Georgia's 2026 standard deduction. The DOR page says $15,000 single / $30,000 joint, while other sources put 2026 at $12,000/$24,000 with the increase arriving in 2027. That shifts the exact point where your farm hand would start owing Georgia tax — somewhere between $22 and $27/hr at his hours. Either way he's clear.

### SCOTT (2026-08-02T21:43)
No for Josh, my farm hand

### CLAUDE (2026-08-02T21:43)
Josh earns between $6,552 and $7,371 annually as a farm hand, which falls below Georgia's standard deduction of $12,000–$15,000, so he has no state income tax liability. The key cutoff points are $21.98/hr for the $12,000 deduction and $27.47/hr for the $15,000 deduction. He may also qualify for a G-4 exemption, and Georgia doesn't have a state-level FICA equivalent to consider.

Even though he owes no tax, filing a return could be worthwhile—he might recover any withholdings and could claim the Georgia surplus rebate (up to $250 for single filers), though that requires having filed returns in prior years.**Josh owes $0 Georgia income tax at either rate.**

His gross is $6,552 at $12 or $7,371 at $13.50. Georgia's standard deduction is at minimum $12,000 for a single filer — he's not close.

**Where the Georgia line falls** (546 hrs/yr): if the deduction is $12,000, he'd start owing at **$21.98/hr**; if it's $15,000, **$27.47/hr**. That's the conflict I flagged, and it doesn't touch him either way.

**What this means practically:**

- He can claim exempt on **Form G-4** (Georgia) same as the federal W-4, so nothing gets withheld.
- Georgia has no state disability or payroll tax on the employee side, and no local income tax anywhere in Georgia. So state costs him literally nothing.
- His only real tax bite stays the 7.65% FICA — $501 at $12/hr, $564 at $13.50. That's federal and unavoidable.

So the effective hourly numbers I gave you hold exactly: **$11.08 at $12/hr, $12.47 at $13.50.**

One small upside worth mentioning to him — Georgia is issuing a one-time surplus rebate of up to $500 for married couples (single filers get a smaller amount), but you generally have to file a return to receive it. Even owing nothing, filing might put a couple hundred dollars in his pocket.

### SCOTT (2026-08-02T21:45)
Was about unemployment insurance. Do I have to pay into that?

### CLAUDE (2026-08-02T21:45)
Looking at the SUTA agricultural labor exemption rules, both federal FUTA and Georgia SUTA use the same thresholds: either $20,000 in cash wages during a calendar quarter or 10 or more agricultural workers employed on 20 different days across 20 different weeks. I should verify Georgia's specific requirements to make sure they align with this framework.

Looking at Georgia's agricultural employer liability rules, Josh's situation is straightforward — with just one worker earning around $1,840 per quarter, he falls well below the threshold of either 10+ workers across 20 different weeks or $20,000+ in quarterly payroll. The same applies to FUTA requirements. What's key here is that agricultural labor operates under its own separate test rather than the general employer standard that applies to other businesses.

One important distinction: if Angie is an owner rather than an employee, she wouldn't count toward coverage anyway. And on the flip side, if Josh were to lose his job, he wouldn't be eligible for unemployment benefits since there's no coverage in place — that's the practical consequence of falling below the threshold.**No — you're exempt on both federal and state.**

Georgia's agricultural test is 10 or more workers on any day during 20 different weeks in a calendar year, or $20,000 or more in gross payroll for any calendar quarter. Josh is one worker at roughly $1,840/quarter. Federal FUTA uses the identical thresholds for ag labor, so no liability there either.

**The important detail:** Georgia's *general* employer test is $1,500 quarterly payroll or at least one worker in 20 different calendar weeks — and Josh working year-round would blow through that second one easily. But agricultural labor is carved out and tested only under the ag-specific rule. That carve-out is what saves you. Make sure whoever sets up your payroll codes him as agricultural labor, not general.

So your W-2 cost stays at just the 7.65% employer FICA — $501 at $12/hr, $564 at $13.50. The numbers I gave you hold.

**Two flip sides worth knowing:**

Since you're not paying in, Josh earns no UI coverage. If you ever let him go, he can't draw benefits on those wages. That's not your problem legally, but it's honest to mention if he asks.

Georgia requires Form DOL-800, a Separation Notice, for each worker separated regardless of reason. Whether that applies to an exempt ag employer is worth a question to the GDOL — it's a five-minute call and cheaper than finding out later.

You could also elect voluntary coverage, but at your scale there's no reason to.

### SCOTT (2026-08-02T21:47)
So do I need to set up anything g special with fed or state to start doing all of this?  I already ein

### CLAUDE (2026-08-02T21:47)
Looking at the setup checklist for his agricultural operation. He's got the EIN sorted, and with annual payroll taxes around $1,128, he can skip EFTPS deposits and just pay with Form 943 when he files. Still need to handle W-4, G-4, and I-9 paperwork, plus get a Georgia withholding number for state compliance.

For Georgia specifically, he should register with the Department of Revenue even if the employee claims exempt status — safer to have it on file. He'll need to file W-2s with SSA by January 31st and submit Georgia's G-1003 reconciliation form. Workers comp isn't an issue since farm labor is exempt in Georgia, but new hire reporting is mandatory within 10 days — that's something people often overlook. I'm confident about the $2,500 threshold for 943 and Georgia's new hire reporting requirements, though I should probably verify a couple of these details with an accountant to be thorough.

One thing to flag: the EIN needs to be in the LLC's name (Angie's entity), not a personal name, since that's what will be paying the wages. I'll keep this as a tight checklist format that works on mobile.Not much. Here's the full list:

**Federal**
- **EIN** — done. One check: it needs to be the EIN for the entity actually paying him. If your existing EIN is tied to the LLC in Angie's name and that's who's paying, you're fine.
- **Form 943** — the agricultural employer's annual federal return. No registration needed, you just start filing it. Due January 31.
- **Deposits** — here's the nice part: if your total annual 943 tax is under $2,500, you can pay it with the return instead of making periodic deposits. At ~$1,128 total (his FICA + yours), you're well under. No EFTPS schedule, no monthly deposits.
- **W-2 + W-3 to SSA** by January 31.

**Georgia**
- **Withholding account** with the DOR (Georgia Tax Center) — likely needed even if Josh claims exempt and nothing is withheld, since you'd still file the annual G-1003 reconciliation with his W-2. Worth confirming with your accountant whether registration is required with zero withholding.
- **GDOL** — nothing. You're not liable, so no account.
- **New hire reporting** — this one gets missed. Georgia requires reporting new hires within 10 days, and it applies regardless of your UI exemption status. Free, online.

**On file, not filed anywhere**
- W-4, G-4, I-9. Keep the I-9 separate from his other paperwork.

**Workers' comp** — Georgia exempts farm labor, so not required. But "not required" isn't "not a good idea" when he's working hogs and cattle. Worth a quote from your carrier; a voluntary policy on one part-time hand is usually cheap, and it's the exposure that actually worries me here.

Honestly, the whole setup is a couple hours. The annual filing burden is one federal form and one state reconciliation.

### SCOTT (2026-08-11T16:54)
my accountant is filipino.  good guy.  hard worker.  and very honest.  wants to handle my payroll, but admitted he has never done us payroll.  based on that, I am not going to upgradew my QBO for payroll yet.  i'd like for you to make me a workbook that will help help calaulte and see how payroll caclautes here in the us.  i am thinkg a tab whewre he woudl enter the pya rate, withholdesing etc. and it will calcualte fica, (soc sec and meidcare) fed tax, state tax,  etc.  and then produces a paycheck stub i can oprint and give to the employee

### CLAUDE (2026-08-11T17:02)
Scott needs an Excel workbook for payroll processing with separate tabs for setup (employer and employee info, W-4 and G-4 data), a payroll calculator where he inputs hours and rate to generate calculations, and a printable pay stub. I should check the xlsx skill documentation first, then design the workbook to handle FICA taxes, federal and Georgia state withholdings, with potential tabs for YTD tracking and a reference section.…

I need…

I'm reviewing the 2026 federal tax withholding tables with Social Security and Medicare rates, along with the W-4 adjustments for different filing statuses, and now moving into Georgia's state withholding requirements which uses a flat 4.99% rate.…

I've confirmed Georgia's 2026 tax structure: a flat 4.99% rate with a $15,000 standard deduction for single/HOH/MFS filers and $30,000 for married filing jointly, plus $5,000 per dependent. This resolves the earlier discrepancy I was tracking.

For federal withholding, I'm working through the 2026 percentages: Social Security at 6.2% on wages up to $184,500, Medicare at 1.45% plus an additional 0.9% for employees earning over $200,000. For federal income tax, I'm using the Worksheet 1A method from Publication 15-T, which involves calculating annual gross wages, adding other income, applying standard deductions ($8,600 for single/HOH, $12,900 for MFJ), then applying the tax tables to determine tentative withholding before adjusting for credits and extra withholding amounts.

Now I'm building out the workbook structure with a START HERE tab for instructions, a Setup tab for employer and employee information including W-4 and G-4 details, a Payroll Calculator that shows each calculation step-by-step, a Pay Stub for printing, a Pay Register to track year-to-date entries, and tax tables.

I'm refining the approach so the Payroll Calculator handles one pay period at a time with a manual input field for prior year-to-date amounts, while the Pay Register becomes the source of truth with formulas that automatically compute all 26 pay periods. The Pay Stub will then pull data from a selected row in the register, creating a cleaner workflow.

Building the Pay Register with columns for period number, pay date, period start and end dates, regular hours, overtime hours, and regular pay... For FIT, I need to annualize the current period's gross wage using the pay frequency from setup, then add any other income and subtract deductions and the standard deduction amount to get the adjusted annual wage. Then I'll look up the appropriate tax bracket based on that amount.

For Georgia, I'm following a similar annualization approach but using their state-specific standard deduction amounts that vary by filing status. I'll create a lookup table for the GA withholding letters to handle the ambiguity, then build out the formula: subtract dependent and adjustment allowances (each worth $5,000), apply the 4.99% rate, divide by pay periods, and add any additional withholding from line 6. For exemptions, I'll check the W-4 exempt flag for federal and the G-4 exempt flag for Georgia to zero out the respective withholding amounts.

Now I'm setting up the visual design with Arial font, using blue for input cells, yellow highlighting for cells that need to be filled in, black for formulas, and green for cross-sheet references. I'm structuring the workbook with six sheets: a "Start Here" landing page, a "Setup" tab for employer and employee info, a "How It Calculates" walkthrough showing the math for one pay period, a "Payroll Register" for all employees, a "Pay Stub" template, and a "2026 Tax Tables" reference sheet. I'm defining named ranges in Setup for the employer details like name, address, EIN, and phone, plus employee fields like name and address.

I'm continuing with the pay setup section—hourly rate, overtime multiplier, pay frequency, and periods per year—then the Federal W-4 fields covering filing status, Step 2 checkbox, Step 3 credits, and the various Step 4 deduction and withholding amounts.

Now I'm adding the Georgia state tax form with marital status letter, dependent and additional allowances, and extra withholding per period. Then I'm pulling in the tax rates from the rates table—Social Security employee rate and wage base, Medicare rates including the additional Medicare threshold, Georgia's flat tax rate, and the standard deduction amounts derived from federal filing status and Georgia's marital letter, plus the dependent allowance value.

I'm thinking through how to structure the tax tables for lookups. The challenge is handling six different federal tax schedules—three for standard deduction and three for Step 2 checked—plus Georgia's standard deduction by letter. Rather than building separate blocks for each schedule, I'm considering consolidating everything into one lookup table with columns for the key, income thresholds, base tax, and rates, then using a single INDEX/MATCH approach to pull the right values.

The tricky part is avoiding array formulas since they're unreliable in LibreOffice via openpyxl. Instead of using MATCH with multiple criteria, I can use SUMPRODUCT to directly extract the base tax and rate values by matching on the key, income floor, and ceiling all at once—that way it's a normal formula that works reliably across platforms.

I'll set the top bracket's upper limit to a very large number so the comparison logic holds for all income levels. Then I'll do the same for the rate and excess-over calculations.

For the standard deduction, I'll use a simple SUMIFS lookup based on filing status.

The key format will combine filing status and step 2 flag, like "SINGLE-N" or "MFJ-Y". In the setup sheet, the filing status dropdown will have the standard options, and I'll build the key formula by converting the status to uppercase and appending the yes/no answer.

For the standard deduction amount itself, if step 2 is checked it's zero, otherwise it's 12,900 for married filing jointly or 8,600 for single and head of household. But I need to double-check the actual worksheet structure — it looks like the standard deduction might be added to step 4(b) deductions rather than subtracted directly.

Looking at Worksheet 1A for 2026, I'm working through the steps: I take the employee's taxable wages for the period, divide the annual other income by pay periods, add those together, then handle the deductions. If it's a 2020+ W-4 and step 2 isn't checked, I add the standard deduction amount to the step 4(b) deductions before dividing by pay periods. This gives me the adjusted wage amount per period, floored at zero.

The system then uses either annualized or per-period tax tables depending on whether it's automated or manual withholding.

I'm going to implement the annualized version since it's mathematically equivalent and clearer: I'll annualize the gross wages, add any other income, subtract deductions and the standard deduction amount (unless step 2 is checked), then look up the tentative annual tax from the table. After subtracting annual credits and flooring at zero, I divide by the number of pay periods and add any extra withholding from step 4(c).

One thing to keep in mind is that with variable hours—like if someone chooses their own schedule—each paycheck's annualized amount will fluctuate, which affects the calculation.

Now I'm setting up the payroll register with 52 rows to cover a full year of weekly pay periods. I'll include columns for the period number, pay dates, period start and end dates, regular and overtime hours, regular pay calculated from the hourly rate, overtime pay at the appropriate multiplier, and any other income like bonuses.

Then I'm adding columns to calculate gross pay, track year-to-date gross, determine Social Security wages subject to the wage base cap, compute Social Security and Medicare employee withholdings including the additional Medicare tax, calculate federal income tax using the annualized method with the adjusted annual wage amount, handle Georgia state income tax similarly, and capture employer-side payroll taxes. I'll also include a column for other deductions and calculate net pay and total employer cost. It's a comprehensive setup with many helper columns, but I'm keeping them all visible since this is meant to be a teaching and working tool.

Scott wants to see the calculation logic, which makes sense. For the pay stub itself, I'll compute year-to-date figures using SUMIFS to sum values from the register where the period number is less than or equal to the selected period. I need to handle blank rows carefully—if earnings, hours, and overtime are all blank, the gross should be zero and cascade that through all calculations. The pay stub will let you enter a period number, then use INDEX/MATCH to pull that row from the register, displaying the employer info, employee details, pay period dates, a breakdown of earnings with both current and year-to-date columns, gross pay, all deductions, and net pay.

Writing the spreadsheet formulas... Writing setup schema... Continuing with the Georgia state withholding section and then moving into the derived calculations that pull from federal and state standard deduction formulas. I'm also setting up the tax tables for 2026, which includes the federal payroll tax rates like Social Security and Medicare employee/employer rates and wage bases.

Generating tax table data... Filling in the tax bracket data for single filers, married filing jointly, and head of household statuses with their corresponding income thresholds, base taxes, and marginal rates. Generating tax bracket tables... Setting up the register structure with row 1 as the title, row 2 for notes, row 4 as headers, and rows 5-56 containing the 52 periods of data. The columns will track period number, pay date, period dates, hours worked (regular and overtime), other pay, and then calculated regular pay.

Now I'm building the formulas for the pay calculations—regular pay multiplies hours by the hourly rate from the setup sheet, overtime pay applies the overtime multiplier, and gross pay sums those with any other pay. For the year-to-date gross accumulation, I need to handle the first period specially (starting at zero) and then add each period's gross to the prior running total. Social Security wages are capped at the annual limit, and I'm calculating both the employee and employer portions based on the tax tables. I'm breaking this into separate helper columns to make the formulas more readable and easier to debug — each one handles a specific part of the tax calculation like the bracket base, rate, and threshold, then combines them to get the final FIT per paycheck. Writing tax bracket lookup formula... Adding more tax calculations...

Now I'm setting up the Pay Stub tab with a period selector that uses MATCH to find the corresponding row in the Payroll Register, then INDEX to pull data from that row. I'm also creating a YTD formula that sums values up to the selected period using SUMIFS with a conditional criteria.

The stub itself displays employer and employee information at the top, followed by an earnings section with rows for regular pay, overtime, and other income, then a deductions section below that.

Now I'm thinking about the layout and controls—I need to add a period selector somewhere that won't clutter the printable stub. I'm considering placing it in the G1 area with a label, then setting the print area to exclude that column so it stays hidden when printing.

For the "How It Calculates" tab, I'm planning to create a walkthrough that shows how federal income tax gets computed using the IRS Annual Percentage Method, starting with a single gross pay input and then stepping through the annualization and calculation process. Continuing with the Georgia tax calculation using the taxable annual amount, then moving into FICA withholding for Social Security and Medicare with their respective rates and caps. I'm also planning a summary section that shows gross pay, total deductions, net pay, and employer costs with explanations. I'll need to set up a "Start Here" tab with instructions and legend, then write the spreadsheet code with proper formatting for currency, percentages, hours, and dates, using blue font for emphasis.

For the implementation, I'm applying blue font color to input cells and yellow fill for cells that need to be completed. I'm prefilling the Setup tab with a realistic example—Watts Way Farms with an employee named Josh earning $12/hour on a weekly schedule, 52 pay periods, filing status Single, and both federal and Georgia exemptions set to "No" so the tax calculations are visible and demonstrate how the tool works. I'll note in the Start Here section that Josh would likely claim exempt status on both, and explain how to toggle that setting.

With Josh's numbers ($12/hr × 10.5 hours/week = $126/week, annualized to $6,552), both FIT and GA withholding naturally calculate to $0 through the actual math, which perfectly demonstrates that the machinery is working correctly while also showing a realistic scenario where no tax is owed. I'll add a few additional example rows with higher earnings so the accountant can see nonzero withholding amounts in action. nonzero withholding, try entering $480 (a 40-hour week)." That way the default matches Josh's actual situation while still demonstrating the calculation machinery.…

Let me verify the calculations are actually correct by loading the data and spot-checking against the expected values. For period 1, I'm checking that 10.5 hours at $12/hour gives $126 gross, then validating the Social Security and Medicare withholdings, the annualized income calculation, and the federal income tax before moving on to state taxes.…

I'm verifying the OT calculation for the 570 hours row—the taxable income of 21,040 falls in the 19,900–57,900 bracket, so I'm applying the base tax of 1,240 plus 12% on the excess amount, which gives 1,376.80 weekly or 26.48 per pay period. For Georgia, I'm calculating the state tax on the remaining 14,640 at the 4.99% rate, which comes to about 14 per pay period.…

I'm verifying the Social Security wage base cap calculation—row 6 correctly caps at $84,500 after subtracting the $100,000 threshold, and row 7 shows zero as expected. For Additional Medicare tax, the YTD amount of $300,000 exceeds the $200,000 threshold by $100,000, which when multiplied by the 0.9% rate gives $900 in tax, while row 6 properly calculates to zero since the excess hasn't been reached yet.…

Five tabs:

**Setup** — employer, employee, pay rate, and every field off the W-4 and G-4. Pre-filled with Josh at $12/hr weekly, single. Only tab with settings.

**How It Calculates** — the teaching tab, and the one your accountant should read first. Walks one paycheck through all 36 steps of the IRS Annual Percentage Method and the Georgia formula, each line with a plain-English explanation of what it's doing and why.

**Payroll Register** — 52 rows. Enter date and hours; everything calculates. The intermediate steps (adjusted annual wage, bracket base, rate, threshold) are shown rather than hidden so any paycheck can be checked by hand.

**Pay Stub** — type a period number, print. Current and YTD columns, and a section showing the employer-paid FICA so Josh can see it isn't coming out of his check.

**2026 Tax Tables** — all six federal bracket schedules, FICA rates, Georgia's 4.99% and deductions. Update this each January and the whole workbook rolls forward.

**Verified against known cases.** At Josh's 10.5 hours: $126 gross, $7.81 Social Security, $1.83 Medicare, $0 federal, $0 Georgia, **$116.36 net**, $135.64 farm cost. At 40 hours it correctly produces $17.04 federal and $9.56 Georgia. I also tested the Social Security wage base cutoff, the additional Medicare surtax, the Step 2 checkbox schedules, and both exempt toggles.

**Two things to flag for your accountant:**

The federal method annualizes each paycheck, so an unusually big week withholds proportionally more. That's correct behavior, not a bug — but it's the thing that confuses people new to US payroll.

Georgia's 2026 standard deduction is $30,000 joint and $15,000 single. How that splits across the four G-4 marital status letters is my interpretation, flagged in the workbook. Only letter A matters for Josh, but confirm the others before running anyone else through it.

No pre-tax deductions modeled, and the OBBBA overtime and tips exclusions aren't in there. Neither applies to your situation now.
