# Declining calls but rising forecast
Date: 2026-06-18
Conversation: d65cc611-5d83-494d-8c27-6bf7dad5ffd4
Domain: business-ops

## Summary
**Conversation Overview**

The person, Scott, is working in a hospitality or facilities operations context and is reviewing a workforce management forecast submitted by an external vendor, CallTek. The specific file under review is `BPRF_Erlang_AUG_2026_EST__with_Intown_.xlsm`, an Erlang-based staffing forecast for August 2026 that includes an "Intown" queue adjustment. Scott's core concern was that the forecast projected a rebound in call volume despite a clear downward trend in recent actuals, and he asked Claude to review the workbook and explain the discrepancy.

Claude analyzed the workbook in depth, identifying that the forecast uses a linear trend plus multiplicative seasonal model. The key finding was that August carries the highest seasonal factor of the year (+9.6%), which mathematically lifts a depressed deseasonalized baseline back above 10,000 calls. Claude further identified that the model's embedded documentation was stale — showing a positive trend slope of +111.34 calls/month anchored to September 2025, predating the sharp decline observed from October 2025 onward. Claude also flagged data reconciliation issues in the `SupportingView` tab, where early-2026 "overall" actuals show conflicting figures for January, February, and April. The analysis concluded that Joan's August forecast of 10,125 sits at the high end of a credible range (~8,600–10,700) and is roughly 3–8% optimistic, with a more defensible central estimate of ~9,400–9,800. Key named parties include Joan Paca (CallTek Operations Manager, forecast author), Phoebe Bayno, Robertson Delima, Louwell Sabellano, Darline Nailon, Lizzie Bernabe, Shelley Tabernero (all CallTek cc recipients), and Kyle Davis (Blueprint RF).

When asked to draft a response, Scott clarified that this forecast involves CallTek only, not Cloudstaff, indicating these are two distinct vendor relationships Scott manages separately. Claude produced two email draft variants using a message compose tool: a collaborative/diagnostic version framing the pushback as clarifying questions before committing to a staffing plan, and a direct/hold-for-revision version that explicitly withholds sign-off and proposes a conservative planning baseline of ~9,400–9,800. Both variants contain identical substantive asks covering trend re-fit confirmation, seasonal factor recalibration, explanation of the May 2026 anomaly, actuals reconciliation, and a request for a prediction interval. Claude offered additional framing guidance on which variant to use depending on whether this is a recurring pattern with the vendor, and flagged a decision point about whether Kyle Davis should see the technical challenge on a reply-all or whether some items should be raised with Joan directly.

### SCOTT (2026-06-18T19:37)
this doesnt make sense to me.  the calls have been trending down, yet they are forecating more?  Please review and advise
[File uploaded: [EXTERNAL] BPRF Forecast_ Aug 2026.pdf]
[File uploaded: BPRF Erlang AUG 2026 EST (with Intown).xlsm]

### CLAUDE (2026-06-18T19:41)
I'll dig into the actual workbook to see how Joan built this forecast, because the email screenshot alone won't show me the formulas driving those numbers.

I'll use Python with openpyxl to read through the spreadsheet and understand how the forecast calculations work.Let me open the workbook and look at the structure and formulas.

The "Forecast" sheet is probably where the important data is, so I should take a closer look at it.The "Forecast" sheet is where the action is. Let me dump it with formulas.

The forecast model uses linear trend with seasonal adjustment across 21 months of data, showing a positive trend slope of 111.34 calls per month—meaning call volume is expected to increase. The baseline is calculated by dividing the last month's call count (12,113) by its seasonal factor (1.020), yielding 11,876.

Looking at the actual historical data from January 2024 through September 2025, I can see the 21-month period the model is based on. But here's a critical discrepancy: the forecast sheet ends at September 2025, yet the email is dated June 2026 and references August 2026 forecasts. The chart in the PDF appears to show historical data extending through May 2026, which creates a timeline mismatch I need to reconcile. There's a fundamental mismatch here: the PDF chart shows actual call volume declining sharply (from ~14,000 down to 8,583), but the forecast model is predicting an uptick above that last actual value. The model itself has a positive trend slope of +111.34 calls per month based on data through September 2025, which explains why it's forecasting higher numbers despite the recent downward pattern visible in the chart.

The real issue is that the model was trained on data from January 2024 through September 2025, when call volumes were actually rising or holding steady. It learned an upward trend from that period, but it hasn't been retrained on the recent sharp decline that's visible in the October 2025 through May 2026 data shown in the chart. So the forecast is anchored to an outdated trend that no longer reflects what's actually happening.

Wait, let me reconsider this more carefully. The PDF forecast shows different numbers than what's in the Forecast tab of the workbook—the PDF has 10,564, 10,304, 10,125 while the sheet shows 12,492 for October 2025, 11,011 for November, and so on. That suggests the PDF was generated from a more recent model run, but the workbook's Forecast tab is still showing results from an older run through September 2025. The workbook itself is labeled "AUG 2026 EST (with Intown)", so I need to figure out where the PDF's forecast numbers are actually coming from. So these daily breakdowns (Mon 475, Tue 443, etc.) are weekly call volumes that sum to the monthly totals like 2635 for June. When I multiply by roughly 4.33 weeks, I get around 11,400 calls per month, but the chart shows June at 10,564—close but not exact. I'm wondering if these daily numbers actually represent daily averages instead.

Actually, looking at the percentages at the top (18% Mon, 17% Tue), those seem to be day-of-week distributions. If 2635 is the weekly total and I multiply by 4 weeks, I get 10,540, which matches the June forecast of 10,564 pretty closely. That reconciles. July follows the same pattern: 2550 × 4 = 10,200 versus the chart's 10,304. But August breaks the pattern—2196 × 4 = 8,784, yet the chart shows 10,125. There's a discrepancy there, so maybe August has a different adjustment or the daily tables are using a different week count.

Let me refocus on what the user actually asked: calls are trending down, yet the forecast is going up. The key is understanding the trend slope and the seasonal factors. I need to dig into the chart's source data and trace how the forecast was generated. Looking at the model structure, it's a linear trend plus multiplicative seasonality. The trend slope is +111.34 per month—that's positive, learned from the Jan 2024 to Sep 2025 period. August has the highest seasonal factor at 1.096, meaning August is seasonally +9.6% above baseline. The baseline itself is 11,876.96. So even with a simple model, the positive trend and strong August seasonality could explain why the forecast is higher despite recent weakness.This is illuminating. The "Forecast" tab is auto-generated model documentation, and it reveals exactly what's going on. Let me confirm the chart's source data and the recent actuals before I write this up.

I'm looking at the SupportingView sheet data that feeds the chart, extracting the monthly "Calls Offered" figures from the BPRF Call Center Overall column to see the trend across early 2025, with March hitting the peak at 14,247 calls.

The data shows a sustained decline from that March peak down to 8,583 by May 2026, but then the forecast jumps back up to 10,564 for June 2026—a 23% increase above the last actual value. This validates the user's concern about the forecast being unrealistic. The root cause appears to be the forecasting model using a linear trend with seasonal adjustment based on 21 months of data, which is picking up a positive slope that doesn't reflect the recent downtrend. More recent data from October 2025 through May 2026 shows a sharp decline—dropping from 11,873 down to 8,583—which the forecast model hasn't properly accounted for. The model appears to still be relying on that earlier upward trend and high baseline rather than recognizing this recent downtrend, so its projections are likely overestimated. I'm checking whether the forecast formula is correctly applying the seasonal factors to see where the disconnect is. That calculation doesn't match either, so the model must have been re-run with fresh data for the PDF. The forecast values are actually declining month-to-month (June through August), which suggests the updated model either has a negative trend or a seasonal effect that's pulling the numbers down.

Let me work backwards from the forecasts using the seasonal factors to find the underlying deseasonalized trend. Dividing each forecast by its seasonal multiplier shows the base level dropping from around 9,700 in June down to 9,238 by August, which means the trend is falling sharply enough to overcome August's high seasonal factor.

The real puzzle is why the updated model still forecasts June through August 2026 in the 10,100–10,600 range when the most recent actual (May at 8,583) and the three-month trailing average (~9,807) are both lower. The answer lies in August's seasonal factor being the year's highest at 1.096, so the model is applying that strong seasonal boost to a deseasonalized baseline.

The question then becomes whether that August seasonal factor—computed from 2024–2025 data where August consistently ran high (13,022 and 13,330)—still holds true going forward. The seasonality is definitely real in the historical record, so the forecast logic of "deseasonalized ~9,200 plus ~10% seasonal lift = ~10,100" isn't unreasonable on the surface, but I need to think through whether that historical pattern is still valid.

The real issue Scott should push back on is whether the baseline assumption is sound. The most recent actual in May 2026 is 8,583, and the trend has been sharply declining. An August forecast of 10,125 would require an 18% rebound from that May number, which implicitly assumes the recent drop is temporary noise rather than a structural shift. If the decline is actually secular—fewer rooms, self-service deflection, a lost property—then the model is fundamentally wrong about what the baseline should be.

But I'm noticing a data quality problem that complicates this. Looking at the columns for early 2026, the overall figures in column B don't consistently match the detail column F, except in March and May. January through April show discrepancies of 400–300 calls, which raises questions about how the overall is being calculated across different columns. The chart is pulling from one of these columns, so I need to figure out which one is actually reliable before I can trust the trend.

There's also a seasonality issue baked into the forecast. The seasonal factors were estimated during 2024–2025 when the call center was running at a much higher volume, around 12,000–14,000 calls. Now that the baseline has dropped to roughly 9,000, applying that same +9.6% August adjustment might overstate the actual seasonal swing in absolute terms. If the business has structurally downshifted, the seasonal pattern's shape might hold, but the model's assumption about mean reversion is where it's likely going wrong.

And here's the real problem: the model's own documentation shows a positive trend of +111 calls per month, which directly contradicts what I'm seeing in the actual last twelve months of data.

The forecast tab in the workbook still lists a rising trend of +111.34/month with a baseline anchored to September 2025 at 12,113 calls—but that's completely at odds with a forecast that's supposed to reflect declining volume. The documentation is stale and internally inconsistent with what the numbers are actually showing. Scott has every right to push back and ask whether the documented model (rising +111/month, baseline 11,877) is what actually generated these forecasts, or if it was re-run without updating the documentation. The two don't align.

Now I'm checking the forecast against some basic benchmarks to see if the numbers pass a sanity test. If I apply a −25% YoY decline to August 2025's 13,330, I get roughly 10,000, which is remarkably close to the forecast of 10,125. That means the forecast is actually consistent with the recent YoY decline pattern of −20% to −34%, so it's not unreasonable from that angle. The real issue is the month-over-month perspective—the forecast sits 18% above the last actual reading and well above the trailing average, which creates the tension I'm seeing.

The honest answer is that the forecast isn't obviously wrong; it's a seasonal model capturing that August is typically strong, and even with the YoY decline, a seasonally strong August lands around 10,000. Scott's skepticism comes from comparing it to the most recent months, which are seasonally weak and possibly anomalously low. But the forecast depends entirely on two critical assumptions that need scrutiny: whether May's 8,583 is truly representative, and whether the seasonal pattern itself still holds. The weekly breakdown for August checks out—multiplying the weekly total by the number of weeks in the month gives roughly 9,728, which aligns with the forecast of around 10,125 when accounting for the Intown overlay. The daily percentages also track consistently, with weekdays ranging from 15–17% and weekends dropping to 10–11%, which sums to 100%.

Now looking at the SLA and staffing side—August shows about 89% SLA with scheduled agents ranging from 27 down to 20 across the week, and these numbers are derived from Erlang calculations based on the volume forecast. This is where it gets critical for Scott: if the forecast is inflated, the agent requirements balloon too, which directly inflates the CallTek and Cloudstaff headcount costs he's responsible for managing.

The risk cuts both ways though—if he under-staffs based on recent lower volumes and August actually does spike seasonally, SLA tanks. So there's real budget and operational tension here.

I should also flag the data inconsistencies between columns B and F for Jan/Feb/Apr 2026, plus the Forecast tab documentation is outdated (only built through September 2025 with a positive trend noted). Those are legitimate cleanup items. Let me think through whether the model is actually pulling from that stale baseline by checking if the forecast values align with an updated regression, though I can't fully reverse-engineer the exact calculation without more detail. The year-over-year comparison actually makes the forecast defensible—it's down 24% versus August 2025, which aligns with the observed decline pattern—so the real disagreement hinges on whether May's trough represents a structural shift or just seasonal noise. This forecast bias has real operational teeth: it'll over-staff agents and inflate offshore costs, so I need to give Scott specific questions to push back on with Joan and CallTek, and concrete next steps to validate which story is true.

Now I'm calculating benchmark comparisons for August 2026—the naive last-actual baseline, the trailing 3-month and 6-month averages—so he has clean ammunition to test the forecast's assumptions against simpler alternatives.

I'm also working through year-over-year methods: applying the May decline rate, the April rate, the March rate, and averaging the last three months' YoY trends to see where they land. Joan's forecast of 10,125 sits at the high end of that plausible range, which is worth flagging.

My recommendation is to push back on the forecast as roughly 3–8% optimistic. The key uncertainties are whether August's historical seasonal spike of +9.6% still holds and whether May's dip represents a genuine trough or a shift to a new baseline. I'd ask Joan to validate her seasonal factors were recalibrated for the current volume regime, explain the May drop, and reconcile some data discrepancies before signing off. the analysis itself — keeping prose for the mechanism and tradeoffs, then a focused list of questions for Joan. A chart showing the call volume trend with the forecast overlaid against a benchmark band would make the rebound concern immediate and visual, which fits the data-driven context here. I'll include a chart to strengthen the analysis—it'll show the historical actuals from January 2025 through May 2026, the three forecast points in red for June through August, and reference lines marking the last actual value and the trailing six-month average so the gap becomes visually clear. Now I'm structuring the response: I'll open with the verdict that the forecast is above recent run-rate but not unreasonable once seasonality is factored in, then dig into the real issue driving the concern. The stale forecast tab with its outdated trend assumption and the mismatch between the benchmark and forecast columns are the real weak points undermining confidence. I'll pull together a comparison table showing August 2026 estimates across different methods—Joan's 10,125 sits at the high end—and then lay out concrete questions to ask her, since this forecast drives staffing and offshore costs downstream, and overestimating creates unnecessary overhead.I dug into the workbook itself — the `SupportingView` tab is the chart's source data, and the `Forecast` tab contains the auto-generated model documentation. Here's what I found.

## Your instinct is half right — but for a more interesting reason than "they got the direction wrong"

The actuals are unambiguously down. Calls Offered peaked at **14,247 in Mar 2025** and have eroded to **8,583 in May 2026** (the last actual). The trailing 6-month average (Dec'25–May'26) is **~9,867**. So when Joan forecasts **10,564 / 10,304 / 10,125** for Jun/Jul/Aug, she's projecting volume **~18% above the most recent actual and ~3% above the 6-month average**. On a pure level basis, yes — that looks like it's fighting the trend.

## Why the model rebounds: August is the seasonal high point

The model (documented on the `Forecast` tab) is a **linear trend + multiplicative seasonal** method. The mechanism that produces the "up" forecast is seasonality, not trend. The deseasonalized level baked into those forecasts is roughly **9,200–9,700**. The model then multiplies by each month's seasonal factor — and August carries **the highest factor of the entire year, +9.6%** (June +8.9%, July +6.7%). That +9.6% bump is what lifts a depressed ~9,200 baseline back up to ~10,100. The forecast isn't ignoring the decline; it's saying *"August is historically a peak month, so even off a lower base it springs back."*

## The honest counterpoint (where your hunch may be wrong)

Look at it year-over-year instead of month-over-month and the picture flips:

- Aug 2025 actual: **13,330**. Joan's Aug 2026: **10,125** → that's a **−24% YoY decline**.
- Recent observed YoY declines: Mar **−27%**, Apr **−20%**, May **−34%**.

So on a YoY basis, **10,125 is squarely inside the decline you're already seeing.** The forecast is not blind to the downtrend — it's encoding "August, but ~25% lighter than last August." That's defensible. The entire disagreement reduces to one question: **is May's 8,583 a seasonal/anomalous trough, or is it the new run-rate?** If it's a trough, Joan is roughly right. If 8,583 is the true level, she's biased high.

Here's where the August forecast sits against every reasonable benchmark:

| Method | Aug 2026 estimate |
|---|---|
| Last actual carried flat (May) | 8,583 |
| Trailing 3-mo avg (Mar–May) | 9,807 |
| Trailing 6-mo avg | 9,867 |
| Aug'25 × avg recent YoY (−27%) | 9,716 |
| Aug'25 × mildest YoY (Apr, −20%) | 10,690 |
| **Joan's forecast** | **10,125** |

Joan lands at the **high end** of the credible band (8,600–10,700). A more balanced central estimate is **~9,400–9,800**. She's optimistic by roughly 3–8%, not wildly wrong.

Let me load the visualizer so I can show you the trend against the forecast and benchmarks.

I'm setting up a Chart.js visualization that spans from January 2025 through August 2026, with the historical actuals displayed as a solid line and the forecast period shown as a dashed segment. I'll add reference lines for the last actual value and the six-month average to highlight the gap between current performance and projections. The data starts with calls offered from the supporting view, beginning at 12,827 in January and moving through the spring months.

Building the chart now...

Now I'm tying together the core issue around stale documentation and data quality, then laying out what Joan specifically needs to do and what happens operationally if we don't address this.## Where the forecast is genuinely weak — and your real ammunition

Two things in the file undercut confidence and are fair to challenge:

**The embedded model documentation is stale.** The `Forecast` tab documents the model as having a **trend slope of +111.34 calls/month (positive — i.e., growing)** and a **baseline of 11,877 anchored to September 2025** (12,113 ÷ 1.020). That documentation was built on a 21-month window ending Sep 2025, during the high-volume regime. It is internally inconsistent with a book that's fallen ~30% since. Either the shipped numbers came from that stale model (in which case they're too high) or it was re-fit but the documentation wasn't refreshed. Ask Joan which.

**There's a data-reconciliation problem in the chart source.** In `SupportingView`, the "overall" series disagrees with itself for early 2026: Jan shows both 9,931 and 9,523; Feb 9,777 vs 9,292; Apr 10,499 vs 10,188. Mar and May reconcile, the rest don't. Before debating the forecast, the historical actuals it's built on need to tie out.

## The second-order effect that matters for you

This forecast isn't academic — it drives the Erlang agent requirements and therefore CallTek/Cloudstaff staffing and cost. At 10,125 the Aug schedule lands at ~27 agents weekday peak. If true volume is ~9,400–9,800, you're being asked to staff and pay for capacity ~3–8% above need. Get it wrong the other way — staff to May's 8,583 and August seasonally spikes — and SLA craters. Given you own that cost line, a 10% forecast error in either direction is a real budget and service-level event, which is exactly why the load-bearing assumptions deserve an answer.

## What to put back to Joan

- What's the **re-fit trend slope on the trailing 12 months**? Confirm the +111/month in the model doc is not what generated these numbers.
- Were the **seasonal factors re-estimated**, or carried over from the 2024–25 high-volume regime? August's +9.6% is doing all the lifting.
- **What happened in May (8,583)?** Partial month, holiday, queue/Intown change, or the new run-rate? The whole forecast hinges on treating it as a trough.
- **Reconcile the Jan/Feb/Apr 2026 actuals** (the 9,931-vs-9,523 type splits) and refresh the stale `Forecast`-tab documentation.
- Ask for a **prediction interval**, not just a point estimate — with this much recent volatility, ±1,000+ is honest.

Net: I'd treat 10,125 as the top of the range, push for a re-fit on the recent decline, and plan around a central case nearer **9,400–9,800** until Joan can defend the August seasonal rebound and explain the May number.

### SCOTT (2026-06-18T19:46)
this is just calltek and not cloudstaff. draft the response for me

### CLAUDE (2026-06-18T19:47)
Scott needs a reply to Joan Paca at CallTek about the August 2026 forecast, and he's clarified this is CallTek-specific, so I should remove any Cloudstaff references. Joan's the Operations Manager there, and the email is cc'd to Phoebe Bayno, Robertson Delima, Louwell Sabellano, Darline Nailon, Lizzie Bernabe, Shelley Tabernero, and Kyle Davis from Blueprint RF.

I'll use the message compose tool to draft this as an email reply. Scott's tone is analytical and direct, but since CallTek is an external vendor partner, I need to keep it professional and collegial while still being pointed about the forecast concerns. He wants to push back on what looks like an inflated forecast without being adversarial. Given his preference for directness and concrete next steps, I'll offer two variants — one more collaborative and diagnostic, one more direct and firm — so he can choose based on how he wants to calibrate the relationship temperature.

For the technical content, I'm focusing on the key diagnostic questions: why the forecast sits above recent actuals, whether the positive trend slope of +111/month is justified, if seasonal factors were re-estimated or just carried over from a higher-volume period, what the May trough signals about the actual run-rate, and reconciling the discrepancies in the early 2026 actuals. I'll also ask for a prediction interval rather than just a point estimate. I want to keep it focused and not overload the message.

Now I'm thinking through the email structure. Joan is the Ops Manager and Scott can reference reviewing the workbook. The subject line is a reply to their forecast submission. The tone needs to be warm and direct—acknowledge their work, then move into the substantive questions without being condescending since these are partners. Scott prefers minimal formatting, but a vendor email with several distinct questions actually benefits from a short numbered list. I'm planning two variants: one collaborative and diagnostic that frames this as a request for clarification before finalizing staffing, and a firmer version that states he can't sign off on the staffing plan yet and lists what needs to be resolved first.

For credibility, I need to reference the actual data: the peak of 14,247 in March 2025 dropping to 8,583 in May 2026, the August forecast of 10,125 which is about 18% above the last actual number and 3% above the trailing six-month average, the model showing a positive trend of 111 per month anchored to September 2025, the seasonal factor for August at 9.6%, and some column discrepancies in January, February, and April plus a May anomaly. I should also request the prediction interval to understand the confidence range around the forecast.

I'll focus on the highest-impact questions to keep the email tight and actionable: refit the trend and baseline, clarify whether seasonal factors need re-estimation, explain the May anomaly, reconcile the early 2026 actuals, and ask for the prediction interval. That's five asks, but I'll keep each one crisp so it doesn't overwhelm.This is going to CallTek (Joan and her team), so here's a reply you can send. I've dropped the Cloudstaff angle and kept it focused on the forecast methodology and the actuals reconciliation. Two versions depending on how hard you want to lean.

Two versions above, both as a reply-all to the existing thread.

The split is about how much rope you give CallTek. The **collaborative** version frames it as "help me understand before we commit" — it preserves Joan's standing in front of her cc'd team (Phoebe, Robertson, et al.) and Kyle, and gets you the same answers without drawing a line. The **direct** version explicitly withholds sign-off and puts a conservative planning number (~9,400–9,800) on the table now, which is the right move if you suspect this forecast would otherwise get quietly operationalized into the August schedule before anyone reconciles it.

My read: go collaborative unless this is a recurring pattern. The five questions are identical in both — if the trend wasn't re-fit and the seasonal factors are stale, the methodology answer alone will force the revision, and you won't have spent relationship capital to get there. Save the firmer version for the follow-up if the reply comes back hand-wavy.

One thing to decide before sending: whether you want Kyle seeing you challenge the vendor's model in this much technical detail on a reply-all, or whether you'd rather raise items 1–2 (the trend/seasonality questions) with Joan directly and keep the reconciliation ask (item 4) on the thread. If you'd prefer that split, I can rework it into a thread reply plus a separate direct note to Joan.
