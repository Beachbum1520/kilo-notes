everything hinges on what triggers the discount period.

The key variables are whether the clock starts from invoice date, receipt, or period end (which would make 7/16 the cutoff if net 15 from 7/1), and whether the discount requires actual payment or just Scott's approval. If BPRF's AP department had the invoice on 7/7 and didn't pay by the deadline, that's a different story than if the terms were ambiguous about when the clock started.

I should also verify whether CallTek met their own SLA obligations — specifically if they delivered the required reports by the 5th business day of July for June's data, since that's a condition precedent to BPRF's payment obligations. I need to be careful here — I've already made two contract interpretation mistakes this session, so I should stick to what I can actually verify rather than making unsupported claims. The real leverage point isn't this month's discount; it's that a 2% prompt-pay discount on $1.4M annual spend works out to roughly $28K yearly, which is substantial enough that BPRF should be systematically capturing it if they're not already losing money on missed deadlines.

The underlying issue is structural: invoices arrive on the 7th, the discount window closes around the 22nd, and the approval process requires wading through a massive workbook. That's a workflow problem worth fixing regardless of how this particular dispute resolves. I'll lay out the numbers cleanly, flag what needs verification in the contract, and focus on the process gap.The 2/15 term isn't in SOW No. 2 — Section 3.0 covers rates, retroactive billing, no-other-costs, and CPI, but sets no payment terms, no due date, and no discount mechanic. It's MSA, and I haven't seen it. Given I've now been wrong twice this session by reading before verifying, I'm not going to tell you what it says.

What to check, in order of what actually decides this:

**What starts the clock.** Invoice date, receipt, or receipt of a *correct and undisputed* invoice? That last formulation is common and it's the only version that gives you anything. The invoices are dated 7/7 with a 7/31 due date — 24 days, not net 30 from invoice date, which suggests the terms may run from period end (7/1 → 7/31). If so, the 15-day window closed around 7/16, not 7/22.

**What satisfies it — approval or payment.** These are different events and it matters a lot. If the term requires *payment* within 15 days, your approval timing is beside the point; AP had the invoice on 7/7 either way. CallTek framing this as "you took too long to approve" may be them assigning you a cause that isn't actually the operative one.

**Whether the discount is taken or offered.** If BPRF deducts it unilaterally on qualifying payment, CallTek doesn't get to adjudicate it.

## The honest read

If it's a clean 2/15 from invoice date, you probably don't win this. It's 8/4 — 28 days out. Even immediate approval on 7/7 would have needed payment by 7/22, and that's an AP cycle question, not a Scott question.

The argument that could work is that the clock runs on a complete and correct invoice package, and June's wasn't: the Hotel Staff Calls SLA supporting data required by Attachment B is still outstanding, and Invoice 2 included 4.47 hours of TL/AM time contrary to Pricing Table 3.1A. **Only make that argument if the MSA language actually supports it.** Asserting it and getting corrected would be the third time in this cycle, and after two dead claims you can't afford a fourth exchange where they're right and you're not.

## The number that matters isn't this month's

2% of $116,896.86 is **$2,337.94**. At roughly $1.4M annual spend, systematic capture is **~$28,000/year** — and a 2/15 term annualizes to about 49%, so it's real money you should be getting every month.

The structural problem: invoices arrive on the 7th, the window closes around the 16th–22nd, and approving requires reconciling a 10,000-row workbook. That cycle doesn't work, and it will keep not working. Fix it by having CallTek deliver the reporting package with the invoice by the 5th business day as Attachment B already requires, and by pre-agreeing what a complete package contains — which is the same code-mapping request already in your draft email. That request now does double duty.

I'd handle this month's $2,338 as a one-time ask on relationship grounds rather than a contractual claim, and spend the actual effort on the standing process. Worth noting the posture shift, though: they're now initiating the fee dispute, which is a different CallTek than the one you've been describing.

Send me the MSA payment terms clause and I'll tell you whether you have a claim or a process problem.

### SCOTT (2026-08-04T13:01)
here's the msa
[File uploaded: BPRF_CallTek Supplier Agt for Outsourcing Contact Center Support_MSA_executed_11 13 2020.pdf]

### CLAUDE (2026-08-04T13:02)
I'm noticing a critical distinction in the invoice payment terms—the discount applies if paid within fifteen business days from when Blueprint RF actually receives the invoice, not from the invoice date itself. CallTek appears to be miscalculating by using calendar days instead of business days, which would throw off the deadline significantly.

Working through the calendar, if the invoices were sent July 7, 2026 (a Tuesday), the fifteen business day window extends through July 28, 2026—that's the actual deadline for payment to qualify for the discount.

Since today is August 4, that window closed about a week ago, and full payment never arrived by the deadline. The discount is technically lost. But here's the key distinction: the condition requires Blueprint RF to pay in full within fifteen business days of receipt, regardless of when Scott approved it. Whether approval came on July 8 or August 3 doesn't change the payment deadline—it was always July 28. The real question is whether the delay in approval caused the payment delay, or if AP simply didn't process it in time.

There's also a discrepancy I'm noticing: CallTek's invoice shows a due date of July 31, but the MSA specifies net 45 days from invoice receipt, which would be August 21. That's a significant gap—their invoice due date is only 24 days out, which contradicts the MSA terms. And looking at the monthly invoice deadline in section 8.2, the third business day of July would fall on either July 3 (if that's the observed holiday) or July 6, depending on how the holiday is counted.

CallTek submitted the invoices on 7/7, which means they were late by a day or two. That compressed BPRF's discount window, which is a fair point to raise in negotiations.

More importantly, the invoices don't appear to meet Exhibit H's requirements. They're missing the PO number, the actual location where services were performed (they show BPRF's Norcross address instead of Cebu), the BPRF contact name with routing ID, and proper supplier contact details beyond just the AR email. So there's a compliance issue here.

Section 8.3.3 gives BPRF the right to reject non-compliant invoices and withhold payment until they're corrected — which means BPRF arguably had no obligation to pay in the first place, and the discount clock shouldn't have been running. It's not an express tolling clause, so it's more of an inference than a slam dunk, but it's a solid argument.

Looking at the other provisions: Section 12.2 requires CallTek to provide supporting documentation for disputed amounts within 30 days, and Section 8.3.2 gives CallTek only 90 calendar days from payment to object to discrepancies or lose the right. But here's the key issue — BPRF hasn't actually paid yet. Scott hasn't approved the payment as of today (8/4), and the 15-business-day discount window closed on 7/28, so the 2% discount is already gone unless CallTek explicitly agrees to reinstate it.

The real problem with CallTek's response is their reasoning. They're blaming Scott's approval delay, but the discount window is actually tied to payment timing, not approval timing — that's an AP operations issue, not a management decision. The structural challenge is that CallTek invoiced late (7th business day instead of the required 3rd), and even with a well-functioning AP process, reconciling the reporting package before the 15-business-day window closes is tight. This month's 2% discount amounts to $2,337.94, which annualizes to roughly $28,000 per year — a meaningful amount if this pattern continues.

I should also note that Article 12.1 actually gives BPRF audit rights with a three-year lookback, requiring CallTek to repay any overcharges plus 5% interest, with CallTek covering audit costs if the overcharge exceeds 5%. That's the recovery mechanism I flagged as missing from the SOW, so it's good to have it on record now that both billing theories are resolved.

The audit clause itself states that if an inspection reveals CallTek overcharged, they'll promptly repay the overcharge plus 5% interest. And Article 3.16 covers the right to audit with 30 days' notice, limited to once per 12 months, with a security focus.

I found something critical in Article 3 Definitions: "Productive Hour" is defined as "the total number of time Supplier Agents provide Blueprint RF services including talk time, hold time, available time and Wrap Time." The MSA Article 4.1 also clarifies that if there's any conflict between the MSA and a Statement of Work, the MSA terms prevail — which SOW No. 2's preamble confirms. So the MSA definition controls here, and it uses the same functional standard of "total time Agents provide Blueprint RF services," which validates my correction that make-busy time shouldn't count.

Now I'm noticing the distinction between two different billing constructs. The MSA's "Billable Minutes" definition excludes available, unavailable, break, and lunch time — but that's for per-minute pricing models, not CPPH. Productive Hour explicitly includes available time while Billable Minutes excludes it, so they're separate concepts. The Outbound Teleco line might fall under "Billable Minutes" since it's billed per minute, though Scott isn't contesting it anyway. I'm also starting to look at Article 7.2 on Telecommunications to understand how those costs are allocated.

Looking at the contract language, Article 7.2 is pretty clear — all outbound transport costs are CallTek's responsibility. Combined with Article 4.1 stating the MSA prevails over the SOW, and the fact that there's no teleco line in the SOW pricing table, that $1,657.04/month charge seems to conflict with what the MSA says. Scott's reasoning is that this per-minute billing has been running for years without challenge, which could constitute a course of dealing, but I should flag that MSA 7.2 appears to contradict the current arrangement.

Scott's already made his decision not to push back on it, and I respect that call. But since the MSA language is new information he didn't have when he decided, I'll mention it once — just one sentence for the file, framed as a factual note rather than a recommendation to reopen the issue. The non-waiver clause in 13.5 means that years of payment alone don't necessarily override what the contract actually says.

Now let me verify the deadline itself: if CallTek computed 15 calendar days from the invoice date of 7/7, that lands on 7/22, which they've already passed. Checking for US holidays in that window — Independence Day 2026 falls on Saturday July 4th with Friday July 3rd as the observed date, so nothing in the relevant timeframe. The deadline is either 7/28 or 7/27 depending on whether we count the receipt date itself, but either way they're past it.

Let me structure the answer now: first, what the clause actually says, then why their reasoning is flawed but their conclusion happens to be correct, then the date calculation, and finally what options exist. then it's two business days late. I'll frame it as one to two days depending on whether July 3rd counts as a holiday. But here's the stronger point: the invoice's due date of 7/31 versus the MSA's net 45 from receipt means payment isn't actually due until 8/21. CallTek is demanding payment three weeks early, and since today is 8/4, BPRF isn't even late on payment yet—CallTek has no legitimate complaint about payment timing at all.Found it. **Article 8.3.1**, last sentence:

> All invoices shall be subject to a two (2) percent (2%) discount if paid in full by Blueprint RF within fifteen (15) business days after the date of Blueprint RF's receipt of the applicable invoice.

Four things matter in that sentence, and CallTek has at least one of them wrong.

## Their reason is wrong. Their conclusion is right.

**The trigger is payment, not approval.** The clause conditions the discount on being *paid in full* within the window. Your approval timing is not the operative event — whether you approved on July 8 or August 3, the discount required cash out the door by the deadline. "You took so long to approve" is not a defense the clause contemplates, and you should not accept that framing.

**It's fifteen business days, from receipt — not calendar days from invoice date.** Invoices sent Tuesday, July 7. Counting business days from July 8, the window closed **Tuesday, July 28**. (July 4 fell on a Saturday, observed Friday July 3 — before the window opened, so no holiday adjustment.) If CallTek calculated 15 calendar days they'd have landed on July 22, which is wrong in their favor by four business days.

**"Shall be subject to" is mandatory, not discretionary.** This is not a courtesy CallTek extends. It's a term of the agreement.

But the window closed a week ago and no payment went out. **On the merits, they're right that June doesn't qualify.**

## What you can push back on

**They invoiced late.** Article 8.2 requires invoices by close of business on the **third business day** of each month. The third business day of July 2026 was Monday July 6 (or Friday July 3, depending on how Cox treats the observed holiday). They sent on July 7 — one to two business days late. Their own delay compressed your window. Not a knockout, but it's a fair point in a goodwill conversation and it's factual.

**Their invoice due date is wrong.** The invoices state 7/31. Article 8.2 and 8.3.1 both provide **net 45 days from receipt** — that's **August 21**. Today is August 4. Under the MSA, this invoice isn't even due for another seventeen days. They have no standing to characterize you as slow.

**The Exhibit H argument — real, but not a slam dunk.** Article 8.3.3 provides that BPRF may return non-compliant invoices and *"shall have no obligation to pay such invoices until such invoices are corrected."* Exhibit H requires, among other things, a PO number or project/GL account, the address where services were performed, and a BPRF contact name in firstname.lastname routing format. Neither invoice carries those. So arguably the payment obligation never properly attached, and a discount conditioned on payment shouldn't run against you.

Be clear-eyed: 8.3.3 addresses the *obligation to pay*, not the discount clock, and there's no express tolling provision. It's a genuine argument, not a certainty. Given I've been wrong twice reading these documents this week, I'd raise it as a question rather than an assertion — *"can you confirm how the 15-business-day window is calculated where the invoice doesn't meet Exhibit H?"* — and let them answer.

## The number that actually matters

$2,337.94 on June. At roughly $1.4M annual spend, **~$28,000/year** — and a 2% discount for paying about 30 days early annualizes near 49%. This is the most valuable thing in the MSA that you aren't currently capturing.

The cycle as it runs today can't capture it: invoices arrive on the 7th, the window closes on the 28th, and approving requires reconciling a 10,000-row workbook against a headcount screenshot. That's workable — three weeks is enough — but only if the reporting package arrives *with* the invoice and AP knows the target date. Attachment B already requires the SLA, inbound call, and QA reports by the 5th business day. Tie invoice submission and the reporting package together, define what a complete package is, and give AP a standing 15-business-day flag.

The code-mapping request already in your draft email does double duty here — it's part of defining a complete package.

## Three other things in the MSA worth knowing

**Audit rights exist after all.** Article 12.1 — three-year record retention, inspection on reasonable request, and if an inspection reveals an overcharge, CallTek repays it **plus 5% interest**, and bears the audit cost if the overcharge exceeds 5%. This is what I told you the SOW was silent on. Not needed for June, but it's there.

**The Productive Hour definition confirms the correction.** Article 3 defines it as *"the total number of time Supplier Agents provide Blueprint RF services including talk time, hold time, available time and Wrap Time"* — and Article 4.1 provides the MSA prevails over the SOW. Same functional standard, and it closes that question definitively. CallTek's treatment was right.

**On the teleco line — your call stands, but the MSA is squarely against it.** Article 7.2 assigns the cost of *"transporting outbound Contacts"* to Supplier, and Article 4.3.1 puts all facility and telecom expense on them. Article 13.5 also provides that failure to enforce isn't waiver, so years of payment haven't extinguished it. You've decided not to challenge it and I'm not reopening that — but you now have a materially stronger position on ~$20K/year than you did when you made the call, and it's worth knowing that if the relationship goes where you think it's going.

### SCOTT (2026-08-04T13:07)
Here's exactly what they said
[File uploaded: 1785848846954_image.png]

### CLAUDE (2026-08-04T13:08)
The critical distinction here is that the discount starts from the invoice receipt date of July 7, 2026, not when they're uploaded to the COX system. This matters because the invoices were just uploaded to the portal, which could be interpreted as the receipt date—but that's different from when the invoices were originally sent. Article 8.3.1 appears to define the timeline for Blueprint RF's receipt of the application, which would set the clock for the fifteen business day window.

CallTek's argument hinges on whether receipt means when the invoices hit the COX portal or when they were initially sent. They're essentially conceding that the portal upload happened separately from the email, which suggests if the upload was late, then receipt was late. I'm working through the business day count from July 7 to verify the deadline—counting July 7 as day one, the fifteenth business day would fall around July 27 or 28 depending on whether we include the start date.

The real pivot though is that CallTek explicitly distinguished between "invoice receipt date of July 7" and "the date the invoices are uploaded to the COX system," implying those are two different dates. If the portal upload happened later than July 7, then under section 8.3.4, receipt would be the later date, which could push past the deadline entirely.

Scott needs to find out: (1) whether Cox actually operates an Electronic Invoicing System that CallTek is contractually required to use, and (2) when those specific invoices were actually uploaded to it. If they went up on July 20, the discount window extends to around August 10 and is still active. Also, emailing a PDF to Scott doesn't count as proper submission if the portal is the required channel—Scott isn't the AP department.

On the make-busy codes, they've now confirmed in writing which ones they're using: Reviewing Tickets, Long Case Notes, and Special Tasks.  The phrase "currently treated as billable" is revealing—that word "currently" suggests this is CallTek's own practice rather than something agreed upon, which gives Scott leverage to push for a formal standard going forward.

Joan Paca is involved as the account manager, which is a concern. The email came from someone else at CallTek, not Joan. The code confirmation is also useful for cross-checking the ARR numbers.

For next steps: Scott should nail down the portal upload date—that single fact determines whether the ~$2,338 discount applies. He needs to confirm whether Cox operates an Electronic Invoicing System per the contract. And he shouldn't concede the point, but he also shouldn't overreach.

Their argument is a bare assertion with no contractual citation—they didn't reference 8.3.1. What's interesting is the framing shifted from Scott's account of "you took too long to approve" to this receipt-date argument. They did cite "15 business days" correctly, so they clearly know the clause. I should offer a brief reply for Scott to consider.Two things happened in that email. One is what you asked for. The other is CallTek pre-empting an argument they know is available to you.

## They just told you where the weakness is

Read the discount sentence again: the window runs from receipt on July 7, *"and not from the date the invoices are uploaded to the COX system."*

Nobody volunteers a distinction that doesn't cut against them. That sentence concedes the invoices go into a Cox system on a **different, later date**, and argues the earlier one governs. They wouldn't raise it unless the later date helped you.

**MSA Article 8.3.4** is the provision they're steering around: if BPRF transitions to an Electronic Invoicing System, *"Supplier shall submit all invoices to Blueprint RF through such Electronic Invoicing System."* If Cox operates that system and it's the required channel, then submission happens at upload — and Article 8.3.1's clock runs from **BPRF's receipt**, which is plausibly the portal date, not the date Joan emailed you a PDF. You aren't AP. An email to you isn't submission through the contractual channel.

Two facts decide roughly $2,338:

1. Does Cox operate an Electronic Invoicing System that CallTek is required to submit through?
2. What date were BPR-2026-07-01 and -02 actually uploaded to it?

If the upload was July 20, the window runs to about August 10 and the discount is **still live today.** Ask for the upload confirmation and timestamp before you concede anything.

Also worth noting quietly: their reason changed. It was "you took too long to approve." Now it's a receipt-date calculation. The clause conditions the discount on payment, not approval — so the first version was never right, and they've moved off it without saying so.

On the arithmetic itself they're correct: 15 business days from July 7 lands on July 28. No holiday adjustment (July 4 fell Saturday, observed Friday July 3, before the window opened). If the July 7 date governs, the discount is gone.

## What you actually got

The code mapping, in writing: **Reviewing Tickets, Long Case Notes, Special Tasks.** That's the record, and it's exactly the three buckets — 623.86 hours, $6,058 in June — I incorrectly tried to disallow.

Note the phrasing: *"currently treated as billable."* That's CallTek describing its own practice, not citing an agreed standard, because none exists. The MSA and SOW define a Productive Hour functionally and leave the code mapping entirely to them. "Currently" is your opening to convert this into an agreed standard — through Section 14 change control or the monthly staffing meeting — rather than something they set unilaterally and can expand.

The Agent Resolve Rate cross-check under SOW Section 4.2 is now straightforward: tickets written per calls handled, tested against Reviewing Tickets hours. Ridge at 94.64 of 179.01 billed hours is the case to start with.

## Two smaller notes

The reporting files landing "in the portal" isn't the split you asked for under Section 4.3 — that's total agent sign-in time detailing billable *and* non-billable time. Confirm you got that specific report and not just a re-send of the monthly workbook.

Joan being looped in on the remaining items is worth watching given the history, but nothing to act on yet.

Want a short reply that asks for the portal upload confirmation without conceding the July 7 date? Two or three sentences is the right length — a question, not an argument, so their answer goes on the record before they know why you're asking.

### SCOTT (2026-08-04T13:18)
yes.  the process is they send me the invlices for approval via email.  then, once approved, i give them the ok to upload into the cox oracle payment portal

### CLAUDE (2026-08-04T13:19)
Scott walked me through how this works: CallTek sends him invoices via email for approval, he approves them, then they get uploaded to the Cox Oracle payment portal. This is the crucial detail—the invoices don't actually reach BPRF until that Oracle upload happens, so the email approval is just a preliminary step. That means "BPRF's receipt of the applicable invoice" in section 8.3.1 could reasonably point to the Oracle upload date rather than the initial email. But there's a complication: Scott personally received those invoices on July 7, and he IS Blueprint RF, so you could argue "Blueprint RF's receipt" means when Scott got the email. That's the real weakness in the argument.

Section 8.3.4 does help though—it says if BPRF switches to an Electronic Invoicing System, the supplier has to use it, and Cox Oracle looks like that system. So submission through Oracle should count as proper submission. Exhibit H also requires the PO number and other details, so the invoice has to meet those standards.

But the deeper issue is that Scott's own process creates the problem. He's the gatekeeper on the upload, which means he controls when the clock starts running. If it starts from the Oracle upload, that's good for capturing the discount because he controls the timing. If it starts from the email, the clock begins before AP even sees it, and his approval step eats into the window. Either way, the process is fundamentally broken—the discount becomes nearly impossible to capture because the clock starts ticking on email receipt, but AP can't actually pay until the invoice is in Oracle, which doesn't happen until Scott approves it. So the review time gets subtracted from the discount window.

That's the real argument: under their reading, the discount is structurally impossible to claim. Contract interpretation disfavors readings that make a provision illusory or impossible to perform.

Their own email actually helps here—they said "the date the invoices are uploaded to the COX system," which confirms they know the upload date is different from the email date.

For the reply, I should keep it short and in question form, not concede the July 7 date, and get the upload date on the record. I'll draft something that asks for confirmation of when those two invoices were uploaded to the Oracle portal and requests the submission confirmations, without arguing yet.

I need to be careful about the recipient—the email came from CallTek Inc. generically with Joan Paca looped in, so I shouldn't guess at names. I'll address it generically or use a bracket.

The key move: get the upload date documented first, then save the structural argument for later. Once I make that argument, they'll prepare their response. Better to lock down the facts while they're still being casual about it.That process detail changes the analysis, and it's the strongest thing you've said all week.

## Their reading makes the discount unobtainable

If the clock starts when they email you the invoice, but AP can't pay until the invoice is in Oracle, and it doesn't reach Oracle until you approve — then your entire review window is subtracted from the payment window. Under CallTek's interpretation, the 2% is capturable only if you approve a 10,000-row reconciliation instantly and AP cuts a check with days to spare.

A reading that renders a bargained-for term effectively impossible to satisfy is a weak reading. The natural one is that "Blueprint RF's receipt of the applicable invoice" means receipt through the channel invoices are actually submitted through — the Oracle portal, which Article 8.3.4 contemplates as the required channel once BPRF transitions to an Electronic Invoicing System. Your email inbox is an approval checkpoint, not AP intake.

The honest weakness: you are Blueprint RF, and you received them July 7. CallTek will say receipt is receipt. That's why you don't lead with the argument — you get the upload date on the record first, before they understand why you're asking.

**Don't put the reasoning in this reply.** Just the question.

"Since invoices are submitted to Blueprint RF through the portal" is doing the work — it states the mechanic as fact, which it is, without arguing that it controls. Their answer will either give you a live window or close the question. "Before we close this out" keeps it open without committing you either way.

Two things to line up while you wait:

**Confirm the Oracle portal is the required channel.** Article 8.3.4 conditions this on BPRF having transitioned to an Electronic Invoicing System. If Cox AP treats Oracle submission as the intake event — which the process you described implies — that's the fact that makes the argument work. Worth a quick check with AP or Sourcing on how they date invoice receipt for payment-terms purposes. If Oracle's own record shows a receipt date, that's better evidence than anything either of you argues.

**The process needs fixing regardless of how June lands.** Right now the discount is structurally uncapturable if their reading holds, and marginal even if yours does. Two changes fix it: CallTek delivers the invoice *and* the complete reporting package together by the third business day per Article 8.2, and AP gets a standing flag on the 15-business-day date. That's ~$28K/year, which dwarfs the $2,338 you're arguing about.

If they come back with a July upload date that's still inside the window, ask for the credit on the next invoice rather than a reissue — cleaner, and it's how the SOW already handles SLA credits.

If they hold the July 7 line, I'd let June go and put the process fix in place for July's invoices. Winning a $2,338 argument isn't worth spending goodwill you'll want for the make-busy standard, which is the larger number and the one still genuinely open.

### SCOTT (2026-08-04T13:21)
that message does nothing.  they know they upload to the portal after i approve.  i actually have nothgb to do with the discoutns.  I am sure the ap folks have it built intot he system, and will take it.

### CLAUDE (2026-08-04T13:22)
CallTek's message to Scott isn't actually informing him of a policy—it's a preemptive move. They're anticipating that Oracle's AP system will automatically deduct the 2% discount when processing the invoice, so they're documenting their position now to dispute the short payment when it arrives.

The right move for Scott is silence on the discount entirely. If he acknowledges or replies "noted," he's creating an admission that BPRF agreed the discount doesn't apply, which CallTek could use against Cox's AP department later. The contract also gives CallTek 90 days from payment receipt to formally dispute any discrepancy in writing—if they don't, the dispute rights waive. So Scott should drop this from his reply, avoid explaining the Oracle date logic to CallTek, and not proactively loop in AP. If CallTek escalates, that becomes AP and Sourcing's problem to handle.You're right, and my draft was worse than useless — it would have signaled that you think there's something to argue about.

Reframe what that email actually is. CallTek isn't informing you of a fact. They're **getting ahead of a short payment they expect.** They know Oracle will take the 2% automatically when AP pays inside the window from the portal receipt date. So they're planting a sentence in your inbox now, so that when the deduction lands they can point to it: *"we notified Blueprint RF the discount didn't apply."*

That makes your reply the only thing at risk here. If you acknowledge that sentence — even "noted" — you've handed them a BPRF representation that the discount didn't apply, and they'll wave it at AP when the deduction hits. Right now they have an assertion nobody agreed with. Keep it that way.

**Say nothing about the discount.** Not agreement, not pushback, not a question. The item isn't yours, the system will resolve it, and any response you give can only be used against Cox.

Two things that make silence the strong play rather than the passive one:

**MSA 8.3.2** gives CallTek 90 calendar days from receipt of payment to notify BPRF in writing of a payment discrepancy — and they waive the right to dispute if they don't. An email to you before payment isn't notice of a discrepancy; there's no payment yet. If AP deducts the 2% and CallTek doesn't file a proper written dispute inside 90 days, it's closed permanently.

**Your lane.** Payment terms sit with AP and Sourcing. If CallTek wants to contest a deduction, that's the channel, and pushing them there costs you nothing. You don't need to tell them that either — just don't take the bait.

If they raise it again directly, one line: *"Payment terms and discount application are handled by Cox AP — I'd direct that to them."* Factual, correct, no position taken.

The reply worth sending is the one you already have — approving the invoices, requesting the Section 4.3 billable/non-billable split, flagging the TL treatment and the missing SLA data. Just leave the discount paragraph out entirely.

Worth noticing for the file: their stated reason changed between messages, from "you took too long to approve" to a receipt-date calculation. Neither is a position you agreed with, and you shouldn't create a record that you did.
