# Statement of work coverage review
Date: 2026-08-28
Conversation: d3b1e769-c5ef-442a-9ee4-297043b6f956
Domain: business-ops

## Summary
**Conversation Overview**

The person works in a technical project management or operations role at Blueprint RF (BPRF) and was reviewing a subcontractor-facing Technical Statement of Work (TSOW) for a network cabling cleanup job at MSYDE TPS Slidell property. The scope involves remediation of MDF/IDF cabling across 5 switches, with associated patch cable replacement, labeling, testing, and photo documentation. Key colleagues mentioned include Bret (direct report responsible for drafting the TSOW), Stephen Walker (customer-side contact with a prior billing dispute history), Kathy and Jady (customer leadership involved in escalation), and Scott (the person, based on email signature). The SubK being used is ACE Comm, though the person clarified that vendor assignment is handled outside the TSOW document.

Claude reviewed the TSOW and design tool (MSYDE_Design_Tool_v4_3 MACD), identified several gaps, and drafted a revision-request email to Bret. Key issues flagged included: switch count showing "0" despite a 5-switch labor basis, missing explicit photo verification workflow (before-photo verified before work starts, after-photo verified before SubK release, both saved to OAB), patch cable length concern (3ft previously flagged as insufficient, resolved by Bret switching to bulk CAT6 cut-to-length), boilerplate full-install scope language irrelevant to a cleanup job, and a new guestroom testing line not reflected in the labor estimate. The person confirmed their boss approved absorbing costs, clarifying payment terms are irrelevant to the SubK-facing document. The person also noted that onsite contact information would need to be chased down separately, not through Bret.

The person's communication style with direct reports is direct and list-based, focused on actionable numbered items without preamble. They made several corrections to Claude's approach: payment terms don't belong in a SubK SOW, vendor confirmation is outside TSOW scope, and Bret wouldn't have onsite contact details. On the guestroom testing scope creep identified in the revised TSOW, the person chose to leave it and see how the SubK responds rather than pre-emptively addressing it.

### SCOTT (2026-08-28T18:33)
review and give feedback. does this sow cover everythign we need? are we covered?
[File uploaded: Re_ [EXTERNAL] RE_ [Blueprint RF] Re_ MSYDE TPS Slidell, we are onsite.pdf]
[File uploaded: MSYDE Design Tool v4.3 (MACD) - 8.28.2026.xlsx]
[File uploaded: MSYDE - TSOW - 8.28.2026.pdf]

### CLAUDE (2026-08-28T18:35)

Reviewed the TSOW, the design tool, and the email thread. Short answer: **not fully covered** — the SOW handles the physical/technical scope reasonably well, but it's silent on the two things most likely to bite you given this account's history: money and vendor assignment. Here's the breakdown.

**1. Payment isn't addressed anywhere — this is the real exposure.**
Stephen Walker already told you in writing "we aren't paying" on the prior cabling issue, and Kathy told the customer "Scott will coordinate and dispatch the techs" without resolving who's footing this bill. The TSOW has zero pricing/payment terms — it's pure scope. If this goes out and gets executed before the payment question is settled at the CIO Summit, you're repeating the exact pattern that already burned you once (tech dispatched, customer refuses to sign/pay, everyone scrambles). Recommend: don't release this for execution until you have it in writing who's paying, even if that's a one-line confirmation from Jady/Kathy's side.

**2. Vendor isn't named in the document.**
You were explicit: ACE Comm or a "better subK," not TechNet, not Work Market/Field Nation. The TSOW has no field identifying who's actually doing the work. Worth confirming ACE Comm accepted before this goes final — otherwise the SOW is scope without an executor.

**3. Switch count is inconsistent between the SOW and the actual labor plan.**
The TSOW lists "Number of Switches: 0," but Bret's email basis for the 3-day estimate is 5 switches at ~2/day. That's an internal contradiction on a document that could get scrutinized by a customer who's already disputing billing. Fix the field before this leaves the building — "0 switches" on a switch-remediation job looks bad if anyone reads it literally.

**4. Zero schedule buffer.**
3 days × 2 switches/day = 6 switch-capacity against 5 actual switches — a 1-switch margin, not a 1-day margin. Given this property's specific history (guest-room delay disputes, "additional charges may apply" language that's already hedged/soft), any slip costs you either an uncomfortable change-order conversation or an unpaid overrun. If you want the downtime clause to actually hold up, I'd tighten "may apply" to something more definitive, matching what you told the team verbally.

**5. Your new photo-verification workflow isn't fully written into the SOW.**
The document states before/after photos are required — good, that's covered. But your directive was more specific: TDE verifies the before-photo before work starts, subK isn't released until the after-photo is verified, everything lands in OAB. None of that verification/release gate is written down here. Since you said "no exceptions, all installs," it's worth having it in writing rather than relying on it being remembered.

**6. Patch cable quantities look oversized for the stated scope.**
BOM shows 235 units each of 1ft and 3ft blue patch cables. The SOW language says blue cables are only being ordered "as required to correct length" for a 5-switch cleanup — 470 total patch cables is a lot for that framing. Worth a sanity check that this wasn't carried over from a different template/property before it goes out as a cost commitment.

**7. Onsite contact fields are blank.**
Given the prior no-show complaint from the GM, I'd get a real name/phone in there before scheduling — that's the exact gap that caused the last miscommunication.

**8. Scope language is templated for a full install, not a cleanup.**
Sections like PMS check-in testing, captive portal testing across iOS/Android/Microsoft, and the full Conference Tool configuration block don't apply to an MDF/IDF cable cleanup MACD. Leaving them in either confuses the subK about actual deliverables or gives the customer room to argue those items are in scope. I'd trim the Installation Key Items section down to what's actually being done: cable cleanup, labeling, testing, photo documentation — not the full network-standup checklist.

Bottom line: the technical/cabling scope is solid and matches what was discussed. The gaps are commercial and procedural — payment terms, vendor confirmation, and making your new photo-verification rule explicit — and those are exactly the categories that turned the last MSYDE issue into a multi-week email chain with Kathy and Jady in the loop.

### SCOTT (2026-08-28T18:37)
my boss has said we are eatign the costs.  and we need the beofre and after pics for sure

### CLAUDE (2026-08-28T18:37)
Good — that closes the biggest gap. Two things follow from that:

**Payment now needs to appear on the SOW, not just be known verbally.** If BPRF is eating the cost, that should be stated explicitly somewhere in the document (e.g., "No charge to customer" or similar), especially given Stephen Walker already has this in writing as an open question on his end. Silence on cost in a document you're sending externally can get read as "still TBD" by a customer who's actively watching for exactly that ambiguity. One line closes it.

**On the photos — the requirement text is already in the SOW, but the workflow you actually want isn't.** Right now it just says photos must be taken before/after. Your standing instruction was more specific:

- TDE verifies the before-photo before the subK is allowed to start work
- SubK isn't released until the after-photo is verified
- Both get saved to OAB

None of that gate/verification sequence is written into this document — it's just "must take photos," which a subK could satisfy by snapping pics with no checkpoint tied to them. Since you said no exceptions on this going forward, I'd write it as an explicit step rather than leave it to memory. Want me to draft the added language for both of these (the no-charge line and the photo verification workflow) so you can drop it into the TSOW before it goes out?

### SCOTT (2026-08-28T18:38)
no.  this sow goes to the subcontractor (SubK) not the cusotmer.  and its none of their busienss who is paying for twhat

### CLAUDE (2026-08-28T18:38)
Fair — that's my error, I was treating it like a customer-facing document. You're right that the subK doesn't need to see payment terms; that's between BPRF and the customer, not something that belongs in a subcontractor scope of work. Drop that point entirely.

The photo verification workflow still stands though, since it applies to whoever's doing the physical work — the SubK is exactly who needs to know the before-picture has to be verified before they start and the after-picture verified before they're released. Since you've confirmed pics are a hard requirement, want me to draft that as an explicit step for the SOW (something like a "PIC Pass Process" addition, similar to how the conference tool section already has one), or are you handling that separately?

### SCOTT (2026-08-28T18:38)
help me with a a reply to bret on htis.  he works for me.  need to get these changes made

### CLAUDE (2026-08-28T18:39)

Draft's above — six concrete change items, no payment language since that's not the subK's business. Item 2 (photo verification workflow) is the one you flagged as non-negotiable, so it's spelled out with the same structure as the Conference Tool's existing PIC Pass Process for consistency. Let me know if you want any of these cut or reworded before it goes to Bret.

### SCOTT (2026-08-28T18:40)
3.  dont need to confirm acecom.  tsow doest have anyut to do with that.  and are we sure the 3ft is long enough.  pretty sure previsoly were tld that weasnt long enough.

5. he is not goign toknow #5.  we will ahve to chase this down.

### CLAUDE (2026-08-28T18:40)

Updated — dropped item 3 (ACE Comm confirmation, not the TSOW's concern) and item 5 (onsite contact, since Bret won't have that and it's on your team to chase separately). Down to 4 items now: switch count, photo verification workflow, the patch cable length question, and the scope trim.

### SCOTT (2026-08-28T19:37)

[File uploaded: MSYDE - TSOW - 8.28.2026.pdf]
[File uploaded: MSYDE Design Tool v4.3 (MACD) - 8.28.2026.xlsx]
[File uploaded: 1787945823317_image.png]

### CLAUDE (2026-08-28T19:37)
Went through the revised TSOW against your four items — all four are addressed:

1. **Switch count** — now shows 5, matches the labor basis. ✓
2. **Photo verification workflow** — now explicit in both the Design Notes and the Installation Key Items section (before-photos taken and verified before SubK starts, after-photos taken and verified before SubK is released, both saved to OAB). Matches the PIC Pass Process structure. ✓
3. **Patch cable length** — Bret didn't just swap to a longer fixed length, he changed the approach entirely: one box of bulk CAT6 to be cut, crimped, and terminated by the SubK to whatever length is actually needed. That sidesteps the length problem altogether rather than guessing at 3ft vs. something longer. ✓
4. **Scope trim** — Installation Key Items is now cabling, labeling, testing, and photo documentation only, plus an explicit "Scope Clarification" line excluding VLANs, firewall/gateway config, AP config, PMS, and SSID/splash from SubK scope. ✓

One thing worth a second look before you sign off: the revision adds a new line — cable testing now explicitly covers **all 92 guestrooms**, not just the MDF/IDF cleanup. That wasn't in the original ask (MDF/IDF cleanup, cable management, labeling) and it's not reflected anywhere in the labor estimate, which is still 3 days based on 5 switches. If testing 92 room drops is genuinely in scope now, that's added time the current schedule doesn't account for — worth confirming with Bret whether that's intentional scope or something that crept in, before this goes to the SubK.

### SCOTT (2026-08-28T19:39)
na. lets leave it and see what the subk come back with

### CLAUDE (2026-08-28T19:39)
Works — no need to force it now. If the SubK comes back with a longer timeline or a change order tied to the guestroom testing, you'll have a clean read on whether that line was the driver. Let me know if you want anything else on this before it goes out.
