# Crafting team note into email
Date: 2026-09-08
Conversation: 50bdcdfd-3cbe-4243-9ab8-8611b26f415d
Domain: business-ops

## Summary
**Conversation Overview**

The person is working on a Marriott account retention initiative and managing a Philippines-based team. They are preparing communications for two colleagues named Jady and Kathy, where Jady appears to be an approval authority and Kathy has a cross-functional role likely in Sales. The conversation began with a request to turn a team member's note into a professional email, and Claude drafted that email while flagging three strategic considerations: data reliability, functional ownership, and the absence of a cost ask.

In the second exchange, the person uploaded a lost-customer spreadsheet (Marriott_NLC_YTD_2026.xls) and shared their plan to have team members Par, Elma, and Mary Rose lead a proactive retention effort. The proposed approach included conducting exit interviews with lost customers and identifying at-risk accounts on month-to-month contracts or those expiring within 12 months. Claude analyzed the file, confirmed 53 lost Marriott properties across 2026 YTD, identified a management company concentration pattern (Naples Hotel Group, ROHM Hotels, Plamondon Hospitality Partners, and Marriott International Inc. accounting for roughly 25% of churn), and recommended sequencing outreach by management company before individual properties.

Claude also flagged organizational considerations: Elma's reporting line to Julian in Cebu CS warranted a heads-up, and Mary Rose's proposed role represented a scope expansion worth noting for future comp discussions. Additional strategic recommendations included using support ticket history as a leading indicator rather than relying solely on contract expiration dates, segmenting the at-risk list by risk type rather than just timing, and defining measurable success criteria before presenting to Jady. The person uses informal, fast-typed messages and prefers Claude to synthesize data, surface strategic risks, and propose structured next steps.

**Tool Knowledge**

Claude used a bash tool to process the uploaded .xls file. The file required installing the `xlrd` library (`pip install xlrd --break-system-packages`) before pandas could read it, as the default openpyxl engine does not support legacy `.xls` format. The working approach was `pd.read_excel('filename.xls')` after xlrd installation, not the default engine. The `markitdown` utility was attempted first but the xlrd/pandas approach proved more reliable for structured data extraction and aggregation from this file type.

### SCOTT (2026-09-08T16:09)
a note from one of my team memebrs int he philippines.  help me craft this ito an email i can sedn to jady and kathy
[File uploaded: 1788883739654_image.png]

### CLAUDE (2026-09-08T16:09)

Here's a draft, framed as a proactive initiative (not a reaction to pressure) with Jady as the approval point and Kathy informed rather than asked to weigh in:

---

**Subject: Proactive retention outreach — Marriott portfolio**

Jady, Kathy —

Flagging a trend and a proposed response.

Over the past 8 months we've seen churn of roughly 50–60 Marriott properties, including several that have been with BPRF since inception. I'd like to get ahead of it rather than keep reacting property by property.

Proposal: stand up a small dedicated outreach function (1–2 people) whose job is proactive account check-ins — service feedback, open concerns, reinforcing our value prop — before issues turn into cancellations. This came from the Philippines team, who see the early signals firsthand.

I'll pull together the churn detail (property list, tenure, stated reasons where we have them) so we're working from hard numbers rather than a general impression. Jady, let me know if you want to align on scope/cost before I build this out further.

---

A few things worth pressure-testing before you send:

1. **You don't have the underlying data yet.** "50 to 60" is your team member's estimate, not a pulled report. If Jady asks "which 50-60 and why," you want the list in hand — worth pulling from Salesforce before this goes out, or the email invites a question you can't answer.
2. **Kathy's function, not yours.** Retention outreach on accounts sits closer to Sales than Ops — Kathy may read this as you proposing to encroach on her territory, given she's credit-protective. I kept it framed as "flagging + proposing," not "here's my team taking this on," but you may want a decision on who owns the function before it's in writing.
3. **No cost/headcount ask stated yet** — I left that as a follow-up to Jady rather than baking a number into the first email, since you haven't approved economics with him yet.

Want me to pull the churn numbers into a quick table first, so the email carries data instead of an estimate?

### SCOTT (2026-09-08T16:34)
here's the exact list.  I was thinkign we have Par lead the effort along with Elma and Mary Roe from our philip0ujnes based team.  I want to lay out a few detuals of what we will do.  i was thinking we would start by reahig out to these lsot cusotmers and see if we can get some detiuals on why they left and then also start looking at the hotels on month-to-momth contracts or those that expire in next 12 months or so and get a feel for if tey are goignt o stay or leave.  thoguts?  what else can we do to be a bit more proactive here
[File uploaded: Marriott NLC YTD 2026.xls]

### CLAUDE (2026-09-08T16:35)

Data confirms the estimate: **53 lost Marriott properties**, Jan 1–Sep 8, 2026 (9 months, not 8, but close enough).

**Distribution:**
- By month: Jan 6, Feb 8, **Mar 13** (spike), Apr 3, May 10, Jun 5, Jul 1, Aug 5, Sep 2 (partial)
- No single-month acceleration trend — March and May are outliers, not a steady climb
- Geographically scattered — FL (7) and GA/TX/MN/MD (4 each) lead, but nothing concentrated enough to be a regional issue

**The sharper signal — management company concentration:**
- Naples Hotel Group: 4 lost properties
- ROHM Hotels, Plamondon Hospitality Partners: 3 each
- Marriott International Inc (corporate-managed, not franchise): 3
- Those 4 management companies alone account for **13 of 53 (~25%)** of the churn

That's worth checking before you launch a blanket "call every lost property" motion — if Naples Hotel Group or ROHM pulled 3-4 properties for one shared reason (a corporate decision, a competing vendor relationship, a billing dispute), that's a management-company-level conversation, not 13 separate exit interviews. Worth having Par pull those four accounts first and see if there's a common thread before the wider outreach starts.

**On the team — one flag:** Elma reports to Julian (Cebu CS), not into TDE/Philippines ops directly. Fine if Julian's aware and it's a light lift, but worth a quick heads-up to him so it's not news that his report is doing outreach work for you. Mary Rose leading an analysis/outreach function is a step up from Office Administrator scope — not a problem given the dotted line you already run, but if this becomes a recurring function rather than a one-time push, that's a comp/title conversation at some point, not just a task assignment.

**On the plan itself:**
1. Exit interviews on the lost 53 — good, but sequence it: management-company accounts first (the 25% concentration), then the long tail.
2. M2M / expiring-in-12-months — right instinct, but that data isn't in this file. You'll need a contract-status pull from Salesforce (expiration date + current contract type) before Par can build the "at-risk" list. Worth confirming that field is populated reliably before promising Jady a forward-looking view.

**Other proactive levers worth adding:**
- **Leading indicators, not just exit interviews** — pull support ticket volume/SLA performance in the 90 days *before* cancellation for the 53 lost properties. If there's a common pattern (open ticket backlog, missed SLA, no account touch in X months), that becomes your early-warning trigger for the at-risk list, not just contract expiration date.
- **Segment the at-risk list by why they'd leave, not just when the contract ends** — a M2M property with zero tickets and 4 years tenure isn't the same risk as one expiring in 90 days with open complaints. Contract date alone will overweight your list toward false positives.
- **Define what "success" looks like before you start** — a save rate target or a check-in cadence (e.g., quarterly touch on every M2M account) gives Jady something measurable when you report back, rather than "we called some hotels."

Want me to build the outreach/at-risk framework into something concrete (checklist, tracking sheet, or the email to Jady/Kathy) once you've confirmed the contract-status data is available?
