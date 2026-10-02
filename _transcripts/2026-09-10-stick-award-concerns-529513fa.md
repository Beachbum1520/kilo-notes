# Stick award concerns
Date: 2026-09-10
Conversation: 529513fa-f1ed-4cad-9b81-e1c463e2efe4
Domain: business-ops

## Summary
**Conversation Overview**

The person shared a Restricted Stock Unit (RSU) award agreement and asked Claude to review it for concerns. Claude read from two memory files (`career-inflection.md` and `charter-cox-merger.md`) to contextualize the review against the person's broader career situation, specifically a potential move to a company called Cloudstaff.

Claude's analysis identified five key findings. First, the 669 RSUs vest on a full cliff schedule on August 20, 2029 — no graded vesting. Second, voluntary resignation without qualifying "Good Reason" forfeits all units, and the Agreement's narrow Good Reason definition (base salary cut, non-payment, or relocation over 50 miles) does not cover the person's current "accountability without authority" situation or an unfulfilled verbal promotion. Third, the non-compete clause is operationally broader than its named-competitor schedule implies, and the person's intended Cloudstaff role in a hospitality-WiFi vertical may fall within Charter's covered business scope — flagged as requiring legal counsel before resignation. Fourth, a data discrepancy between the 669-share count in this agreement and a 1,004-share figure in prior notes needs resolution via an equity account statement. Fifth, the Change in Control acceleration provision applies only to future events, not the already-completed Cox/Charter transaction.

The conversation reflects that the person is navigating a significant career decision and evaluating the financial and legal consequences of departing their current employer. Key entities mentioned include Charter (current employer), Cloudstaff (prospective employer), and a prior colleague named Joe whose former organizational responsibilities had apparently been transferred to the person.

**Tool Knowledge**

Claude used `memory_read` to simultaneously retrieve two project files — `/projects/019e0d60-c136-766c-b5d1-9dacf8581440/career-inflection.md` and `/areas/charter-cox-merger.md` — in a single call using an array parameter, which successfully provided the contextual background needed to interpret the RSU agreement in light of the person's career situation.

### SCOTT (2026-09-10T16:49)
for my stick award.  aythign of concern here?
[File uploaded: grantAgreement.pdf]
[File uploaded: planDocument (1).pdf]

### CLAUDE (2026-09-10T16:50)

Bottom line: yes — two things matter for your Cloudstaff decision, and one data discrepancy needs resolving.

**1. Full cliff, no graded vesting.** 100% of the 669 RSUs vest in one shot on the third anniversary of the grant — Aug 20, 2029 (§3.1). Nothing vests before then. This isn't like a typical 25/25/25/25 schedule; it's all-or-nothing.

**2. Voluntary resignation without "Good Reason" = zero.** If you leave for Cloudstaff before Aug 2029 and it doesn't fit one of the carve-outs, all 669 units are cancelled (§3.2(i)) — no pro-rata, nothing. The carve-outs that would save you something:
- **Retirement** (§3.2(ii)): needs age 55+ *and* 5+ years of service *and* age+YOS ≥ 70 *and* the RSUs outstanding ≥1 year. You're 55, but age+YOS≥70 requires 15+ years of service — check your actual BPRF/Cox service date, because if you're short of that, Retirement doesn't apply and you get nothing on voluntary exit.
- **Good Reason**: the Agreement's own definition (§1(b)) controls over the Plan's broader one, and it's narrow — a base salary cut, non-payment of comp, or relocation >50 miles. It does **not** cover scope creep, an unfulfilled verbal VP promotion, or being handed Joe's former org without the title. So the "accountability without authority" situation you're in right now does not, on its face, give you Good Reason under this document.

Net: as this Agreement reads, walking to Cloudstaff before the 2029 cliff forfeits the full 669 units unless you can independently establish Retirement eligibility.

**3. Non-compete is broader than Schedule 1 suggests.** Schedule 1's named-competitor list is telecom/video/ISP-focused and doesn't name hospitality-WiFi players (CallTek, Allbridge, etc.). But the operative definition in §6.3.2(i) is generic — "any business... that offers, provides, markets or sells any service or product of a type offered by... the Company" anywhere Charter does business. Charter's Spectrum Business unit does serve hospitality/commercial broadband, so a hospitality-vertical build at Cloudstaff is arguably inside that definition even though it's not on the named list. Restricted period is 6 months post-termination for non-compete, 1 year for customer/employee non-solicit (§6.3.2). This is a real exposure for the Cloudstaff plan, not a technicality — worth flagging to counsel before you resign, not after.

**4. Data discrepancy to resolve.** Your career-inflection notes have a "recently granted RSU award — 1,004 shares, cliff August 2029." This document is 669 shares, granted Aug 20, 2026, cliff Aug 20, 2029. Same cliff year, different count. Either these are two separate grants (annual + some other award) or one of the two numbers is stale/wrong. Worth pulling your Fidelity/Charter equity statement to confirm which.

**5. No CIC protection here for a repeat event.** §3.3 accelerates vesting on a Change in Control — but this grant post-dates the Cox/Charter close, so it's protecting you against a *future* CIC of Charter, not the one that already happened. Doesn't help or hurt you now, just don't assume it covers what already occurred.

Everything else (arbitration in Stamford under AAA rules, standard confidentiality/IP assignment, recoupment clause) is boilerplate consistent with the Plan and not unusual for a Delaware public company.
