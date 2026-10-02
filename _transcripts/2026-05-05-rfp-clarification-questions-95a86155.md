# RFP clarification questions
Date: 2026-05-05
Conversation: 95a86155-06a2-4f07-9a40-7aebaf581e1b
Domain: business-ops

## Summary
**Conversation Overview**

The person is a senior executive (Scott) at BPRF, a managed WiFi provider owned by Cox (which also owns Cox Media), working on a competitive RFP response to Marriott's GRE&T (Guest Room Entertainment & Technology) platform initiative. BPRF has an existing footprint of 1,000+ Marriott properties as a managed WiFi provider but is not one of the four currently approved GRE system integrators, despite attempting to enter the GRE program for nearly a decade. Scott is working with a direct report named Par, who serves as the Marriott brand manager and has a long-standing personal and professional relationship with Scott. Par reports to Scott and will serve as the internal aggregator and relationship filter before clarification questions are submitted to Marriott's contact (Jason Orsin) by the May 8, 2026 deadline.

The primary task throughout this conversation was developing, refining, and finalizing a set of clarification questions for the Marriott GRE&T RFP, working from three uploaded documents: the RFP itself (DOCX), a requirements questionnaire (XLSX), and a clarification form template (XLSB). Claude extracted and analyzed all three documents, generated an initial 21-question set, then reorganized them by RFP section reference at Scott's request. The list was iteratively refined through a series of corrections and strategic discussions: fixing an inaccurate characterization of STB/smart TV compatibility (Q4), sharpening the SI transition access question (Q6) to strategically open the door to legacy hotel access without revealing competitive weakness, dropping questions that were answered clearly in the RFP (channel lineup enforcement, advertising economics framing), dropping questions irrelevant given BPRF's existing SOC2 Type 2 and ISO 27001 certifications (security review timing), and adding a critical competitive question about Sonifi being listed as the VOD provider in Appendix 2 when BPRF has its own fully licensed VOD solution with hospitality release windows. A key strategic insight was also captured: Cox Media's advertising capabilities under the same parent company as BPRF make the Riott Media advertising partnership question a strength to save for the proposal rather than a clarification question. The final list landed at 17 questions.

Scott explicitly prefers direct, efficient communication and corrected Claude when questions misattributed RFP language, contained contradictions with the overall strategy, or asked about things BPRF already knew or had covered. For the email to Par, Scott rejected an overly formal first draft and requested a tone that reflects a decade-long working friendship while maintaining appropriate professional hierarchy — shorter, more direct, and trusting of Par's judgment. Scott confirmed the questions will be sent via email to Par for review and consolidation, not submitted directly into the clarification form. Key domain terminology used throughout: GRE 1.0/2.0/GRE&T, PRPM (Per Room Per Month), FTG (Free to Guest), SI (System Integrator), Riott Media, Bonvoy, D2C apps, VOD, hospitality release windows, SOC2 Type 2, ISO 27001.

### SCOTT (2026-05-05T14:33)
Review this rfp and other docs in great detail.  I am about to start reading it too.  First task is to come up with the clarification questions
[File uploaded: GRET Marriott RFP_final.docx]
[File uploaded: GRE_T RFP requirement questionnaire.xlsx]
[File uploaded: Request for Clarification form.xlsb]

### CLAUDE (2026-05-05T14:34)

Good — I've fully ingested all three documents. Here's what I'm working with:

- **GRET_Marriott_RFP_final.docx** — The full RFP, covering the GRE&T platform transition, content distribution objectives, advertising/monetization (Riott Media), and requirements across hardware/tech, commercials, advertising partnerships, and security
- **GRE_T_RFP_requirement_questionnaire.xlsx** — The formal response questionnaire across five sheets: Hardware & Tech Mgmt, Commercials & Pricing, Advertising/Partnerships, Security, and a Price Sheet template
- **Request_for_Clarification_form.xlsb** — The vendor clarification template with numbered rows (1.0–34.0) for Category, Question, and Marriott Answer — this is what we fill out

The clarification deadline is **May 8, 2026** — tight. Let me dig into the gaps, ambiguities, and strategic pressure points across all sections.

---

Here are the clarification questions I'd recommend submitting, organized by category:

---

## 🏗️ Hardware & Technology Management

**Q1.0 — GRE&T API/Integration Specs**
The RFP references integration with Marriott's "cloud-based architecture" and cloud browser-rendered UX, but no technical specifications or API documentation have been provided. Will Marriott share GRE&T integration specs, SDK documentation, or a technical reference architecture prior to proposal submission? Without this, respondents cannot accurately scope integration effort or cost.

**Q2.0 — Smart TV Compatibility Requirements**
GRE&T is described as compatible with smart TVs "without requiring set top boxes." What smart TV OS platforms and minimum firmware/model years are in Marriott's approved fleet? Are respondents expected to support all TVs currently deployed across GRE 1.0 and GRE 2.0 hotels, or only a forward-looking approved list?

**Q3.0 — GRE 1.0 / GRE 2.0 Transition Timeline**
Approximately 5,700 hotels are on legacy GRE platforms (~2,900 on 1.0, ~2,800 on 2.0). What is the expected migration rate and timeline? Are respondents expected to support all three environments simultaneously, and for how long?

**Q4.0 — On-Property Network Conditions**
The RFP notes fleet variation in "network quality." Will Marriott provide minimum network SLA requirements or baseline specifications that respondents can design to? Are there minimum bandwidth or latency thresholds properties must meet to qualify for the solution?

**Q5.0 — System Integrator (SI) Role**
GRE 1.0 and 2.0 both relied on system integrators for hardware deployment. What is Marriott's expected SI involvement in GRE&T deployments? Will respondents be expected to work with Marriott-approved SIs, and will a list be provided?

---

## 💰 Commercials & Pricing

**Q6.0 — Pricing Model: Hotel vs. Marriott vs. Brand**
The RFP states that final adoption decisions remain with individual hotels. Is pricing negotiated and contracted at the Marriott corporate level (enterprise agreement) or hotel-by-hotel? Are respondents expected to propose pricing that Marriott then commercializes to hotels, or is there a direct hotel contract model contemplated?

**Q7.0 — Volume / Rebate Basis**
The price sheet references volume-based rebates. Is the volume threshold calculated on total enrolled rooms across the portfolio, or per hotel? At what point (contract execution vs. deployment) does room count get locked for rebate tier purposes?

**Q8.0 — FTG Cost Responsibility**
Does Marriott expect the respondent to absorb all content licensing costs for the Free-to-Guest (FTG) baseline lineup within the PRPM pricing, or are there content costs passed through to the hotel/owner separately? Please clarify the commercial boundary between respondent pricing and hotel-direct content licensing.

**Q9.0 — GRE 1.0 Pricing**
The questionnaire asks respondents to describe pricing reductions as hotels transition from GRE 1.0/2.0 to GRE&T. Are respondents expected to propose pricing for GRE 1.0 properties as well, or only GRE 2.0 and GRE&T?

---

## 📺 Content & Channel Lineup

**Q10.0 — Appendix 2 & 3 Not Populated**
The RFP references Appendix 2 (US channel lineup) and Appendix 3 (Canada channel lineup) but neither appears to contain channel-level detail in the document provided. Can Marriott provide the full channel lists for both? These are necessary to assess content licensing scope and cost.

**Q11.0 — Brand Standard Enforcement**
The RFP states brand-standard channel lineups must be offered while also allowing "hotel-level customization." What is the enforcement mechanism? Can a hotel owner override the brand standard lineup, and if so, what is the respondent's obligation — to offer it or to enforce it?

**Q12.0 — D2C App Integration**
The RFP references OTT app content consumption (130M+ hours annually). Which specific apps are currently approved or required for the GRE&T platform? Are respondents expected to negotiate D2C app agreements directly, or does Marriott hold those relationships?

---

## 📊 Advertising & Riott Media

**Q13.0 — Riott Media Exclusivity**
The RFP mentions "preferred/exclusive commercial business" in the context of the reseller opportunity. Is Marriott seeking an exclusive advertising monetization partner, or will multiple vendors be awarded advertising rights? If exclusive, does that exclusivity apply per inventory type (e.g., live TV vs. in-app vs. Wi-Fi portal)?

**Q14.0 — Data Ownership & Audience Segments**
Marriott references making audience segments available for advertising targeting. What Bonvoy/first-party data will Marriott make available to the advertising partner, and under what conditions? Will a data processing agreement framework be shared prior to proposal submission?

**Q15.0 — CAPEX Investment Threshold**
The RFP references potential upfront investment by the partner in exchange for 1M+ new entertainment customers. Is there a minimum financial commitment Marriott is seeking from partners? What defines "net new entertainment customer" in this context — a Bonvoy member, a new subscriber, or a unique viewer?

**Q16.0 — Advertising Revenue Baseline**
Are there any existing advertising revenue contracts or commitments in place on the current GRE 1.0/2.0 platforms that the selected partner would need to honor or transition? What is the current state of ad monetization, if any?

---

## 🔒 Security & Data Privacy

**Q17.0 — Architecture Review Timing**
The RFP states all vendors must complete an "Architecture and Security Policy review" as well as executing an MSA and DPA. Will Marriott initiate this review process for finalist respondents prior to final award, or only post-award? Clarifying this is important for respondents to plan integration and legal resources.

**Q18.0 — Greater China Scope**
The security questionnaire specifically asks about Greater China compliance. Is Marriott seeking a solution that covers Chinese mainland properties under this RFP, or is the North American scope primary with China as a future phase? This materially affects architectural and licensing requirements.

**Q19.0 — PII Data Elements**
The security questionnaire references Personal Data extensively. Can Marriott clarify what specific data elements the GRE&T platform is expected to collect from guests — e.g., viewing behavior, room number, Bonvoy loyalty ID, device identifiers? This is needed to accurately scope privacy compliance obligations.

---

## 📋 Process & Scope

**Q20.0 — Single vs. Multi-Vendor Award**
The RFP states Marriott may select "one or multiple respondents." Will Marriott clarify if there are distinct award categories (e.g., one winner for content distribution, one for advertising monetization), or could a single respondent win across all categories? Understanding this helps respondents determine whether to submit a full-scope or partial proposal.

**Q21.0 — Proposal Format**
Beyond the Excel questionnaire, are there specific page limits, section requirements, or formatting standards for the narrative proposal? The RFP references "Proposals and any representative artifacts" but does not define what constitutes a complete submission.

---

That's 21 questions across all material categories — more than enough to fill the 34 clarification slots in the template. Once you've read through the RFP yourself, you may want to trim, reprioritize, or add based on where you see the biggest gaps or strategic leverage points. Happy to help sharpen any of these or draft the actual form entries once you're ready.

### SCOTT (2026-05-06T14:57)
for each f the questions, give me the RFP refernece page

### CLAUDE (2026-05-06T14:58)
 The RFP came in as a Word doc without page numbers in the extracted text, so let me go back to the source and map sections properly.

Good news and bad news. The page break detection confirms this document is formatted in a way where the vast majority of the narrative body (all the sections from Terms & Conditions through RFP Request for Clarification) falls on what renders as **page 2** — which tells me Marriott's document relies heavily on continuous flow with very few hard page breaks. The appendices start at pages 3–5. The document doesn't use numbered pages the way a traditional multi-page RFP would.

So rather than mislead you with phantom page numbers, here's the honest mapping — using **section references** which are the only reliable anchors in this document:

---

## Clarification Questions — RFP Section References

| # | Question | RFP Section Reference | Questionnaire Tab |
|---|---|---|---|
| Q1.0 | GRE&T API/Integration Specs | **Background: GRE&T Environment** — GRE&T bullet list (Cloud Rendered UX, Unified Experience Framework) | Hardware & Tech Mgmt |
| Q2.0 | Smart TV Compatibility Requirements | **Background: GRE&T Environment** — "Minimal On-property Hardware" bullet | Hardware & Tech Mgmt |
| Q3.0 | GRE 1.0 / 2.0 Transition Timeline | **Background: GRE&T Environment** — GRE 1.0 (~2,900 hotels) and GRE 2.0 (~2,800 hotels) descriptions; "GRE&T expected to ramp in Q4 2026" | Hardware & Tech Mgmt |
| Q4.0 | On-Property Network Conditions | **RFP Overview** — "Scale reliably across a varied hotel fleet, including variations in network quality" bullet | Hardware & Tech Mgmt |
| Q5.0 | System Integrator Role in GRE&T | **Background: GRE&T Environment** — GRE 1.0 and GRE 2.0 both describe SI-managed hardware; GRE&T silent on SI role | Hardware & Tech Mgmt |
| Q6.0 | Pricing Model: Hotel vs. Corporate | **Contract Terms, Pricing & Conditions** — "commercialize their offer to hotels"; **RFP Overview** — "final adoption decisions will remain at the discretion of individual hotels" | Commercials & Pricing |
| Q7.0 | Volume / Rebate Basis | **Questionnaire — Price Sheet tab** — Volume Rebate table (no methodology defined) | Commercials & Pricing / Price Sheet |
| Q8.0 | FTG Cost Responsibility | **RFP Overview** — "Lowering costs for hotels / hotel owners"; **Questionnaire — Commercials tab** — "Confirm that any third-party costs required to deliver the solution will be absorbed by the respondent" | Commercials & Pricing |
| Q9.0 | GRE 1.0 Pricing Scope | **Questionnaire — Commercials tab** — "Describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T" | Commercials & Pricing |
| Q10.0 | Appendix 2 & 3 Not Populated | **Appendix 2** (US Channel Lineup) and **Appendix 3** (Canada Channel Lineup) — both are empty/header-only in the provided document | Content / Hardware & Tech Mgmt |
| Q11.0 | Brand Standard Enforcement | **RFP Overview** — "Offer Marriott sponsored Brand Standard channel line-ups while enabling channel line-up flexibility (Appendix 4)"; **RFP Requirements** — "Proposals must explain...protects brand integrity" | Hardware & Tech Mgmt / Commercials |
| Q12.0 | D2C App Integration Scope | **RFP Overview** — "Reduce content costs for hotels for live TV and D2C app content"; **Advertising section** — "130M+ hours of app content annually" | Hardware & Tech Mgmt |
| Q13.0 | Riott Media Exclusivity | **Monetize Advertising** section — "preferred/exclusive commercial business of 1M+ new entertainment customers"; reseller opportunity language | Advertising & Partnerships |
| Q14.0 | Data Ownership & Audience Segments | **Monetize Advertising** section — "data-enablement opportunities"; **Questionnaire — Advertising tab** — "What unique data inputs are required from Marriott?" | Advertising & Partnerships / Security |
| Q15.0 | CAPEX Investment Threshold | **Monetize Advertising** section — "contemplation of upfront investment for GRE&T CAPEX (e.g., hardware purchase and fulfillment)" | Advertising & Partnerships |
| Q16.0 | Advertising Revenue Baseline | **Monetize Advertising** section — "450M+ hours of live TV" and "130M+ hours of app content" cited; no baseline revenue or current monetization state disclosed | Advertising & Partnerships |
| Q17.0 | Architecture Review Timing | **MSA, DPA and Security Review** section — "Any chosen vendor will be required to complete an Architecture and Security Policy review" | Security |
| Q18.0 | Greater China Scope | **Questionnaire — Security tab** — "Does your solution work in the Greater China region...?" vs. RFP body's North American scope focus | Security |
| Q19.0 | PII Data Elements | **Questionnaire — Security tab** — extensive Personal Data questions; **Monetize Advertising** section — data-enablement references | Security |
| Q20.0 | Single vs. Multi-Vendor Award Structure | **RFP Requirements** — "Marriott may select one or multiple respondents"; **RFP Overview** — "primary objective is to identify one or multiple content distributors" | Process / All tabs |
| Q21.0 | Proposal Format & Submission Requirements | **RFP Requirements** — "An Excel Requirement Questionnaire has been provided"; **RFP Process and Timeline** — "Proposals and any representative artifacts must be received via email" — no page/format specs given | Process |

---

Since the document doesn't have traditional page numbering, when you fill out the clarification form, I'd recommend referencing by **section heading name** (e.g., "Background: GRE&T Environment" or "Appendix 2") rather than a page number — that'll hold up regardless of how Marriott printed it. Want me to draft the actual form entries now for the .xlsb clarification template?

### SCOTT (2026-05-06T15:00)
redo the questions grouped by RFP Section Reference.

### CLAUDE (2026-05-06T15:00)
 Here are the clarification questions regrouped and renumbered by RFP section order:

---

## RFP Overview

**Q1.0** — The RFP states Marriott may select "one or multiple respondents" and separately identifies objectives spanning content distribution, advertising monetization, and subscription acquisition. Are these treated as distinct award categories (e.g., a content partner award vs. an advertising partner award), or is Marriott seeking integrated respondents who address all objectives? This materially affects whether a partial-scope proposal is competitive.

**Q2.0** — The RFP lists "Scale reliably across a varied hotel fleet, including variations in network quality" as a core objective but provides no minimum network specifications. Will Marriott publish minimum bandwidth, latency, or infrastructure prerequisites that properties must meet? Without this, respondents cannot accurately scope fallback or degraded-mode requirements.

**Q3.0** — The RFP states "Reduce content costs for hotels for live TV and D2C app content" as an objective and references 130M+ hours of annual app consumption. Which specific D2C apps are currently approved or required within GRE&T? Are respondents expected to negotiate D2C licensing directly, or does Marriott hold those relationships?

---

## Background: GRE&T Environment

**Q4.0** — GRE&T is described as compatible with smart TVs without set top boxes, but no approved TV fleet specifications are provided. What smart TV OS platforms and minimum firmware/model years are in Marriott's current deployed fleet? Are respondents expected to support all TVs currently in GRE 1.0 and GRE 2.0 properties, or only a forward-looking approved list?

**Q5.0** — Approximately 5,700 hotels remain on GRE 1.0 (~2,900) and GRE 2.0 (~2,800), with GRE&T ramping in Q4 2026. What is the expected migration pace — hotels per quarter or per year? Are respondents expected to simultaneously support all three environments, and for how long is dual/triple-stack support anticipated?

**Q6.0** — GRE 1.0 and GRE 2.0 both relied on system integrators for hardware deployment and on-property infrastructure. What is Marriott's expected SI role in GRE&T? Will respondents be required to work through Marriott-approved SIs, and will an approved SI list be provided?

**Q7.0** — The RFP references integration with Marriott's "cloud-based architecture" and cloud browser-rendered UX but provides no technical specifications. Will Marriott share GRE&T API documentation, SDK specs, or a technical reference architecture prior to proposal submission? Without this, respondents cannot accurately scope integration effort or cost.

---

## Monetize Advertising & Data-Enablement

**Q8.0** — The RFP references "preferred/exclusive commercial business" and "net new" entertainment customers in the context of the advertising/reseller opportunity. Is Marriott seeking an exclusive advertising monetization partner, or will multiple vendors be awarded rights? If exclusive, does exclusivity apply per inventory type (e.g., live TV vs. in-app vs. Wi-Fi portal display)?

**Q9.0** — The RFP references making "data-enablement opportunities" available to the advertising partner but does not specify what Bonvoy or first-party data Marriott will provide. What audience segments or data types will be made available, under what conditions, and will a data processing agreement framework be shared before proposals are due?

**Q10.0** — The RFP references upfront CAPEX investment "in exchange for net new and preferred/exclusive commercial business of 1M+ new entertainment customers." Is there a minimum financial commitment Marriott is seeking from partners for this consideration? And how is "net new entertainment customer" defined — Bonvoy member, new subscriber, or unique viewer?

**Q11.0** — The RFP cites 450M+ hours of live TV and 130M+ hours of app content consumed annually as the basis for advertising revenue share. What is the current state of advertising monetization on GRE 1.0/2.0 platforms? Are there existing ad contracts or commitments the selected partner would need to honor or transition?

---

## RFP Requirements / Contract Terms

**Q12.0** — The RFP states brand-standard channel lineups must be offered while also allowing "hotel-level customization." What is the enforcement mechanism when a hotel owner wishes to deviate from the brand standard lineup? Is the respondent's obligation to offer the compliant lineup, to enforce it, or both?

**Q13.0** — The RFP asks respondents to confirm all pricing is net to hotel and excludes third-party markups, but the contract commercialization model is described as "needing to be refined." Is pricing contracted at the Marriott corporate level and then passed to hotels, or are respondents expected to contract hotel-by-hotel? Clarifying this is essential to structuring the pricing model.

**Q14.0** — The Commercials questionnaire asks respondents to describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T. Does Marriott expect respondents to propose pricing for active GRE 1.0 properties as well, or only GRE 2.0 and GRE&T?

---

## MSA, DPA & Security Review

**Q15.0** — The RFP states all chosen vendors must complete an "Architecture and Security Policy review" and execute an MSA and DPA. Will Marriott initiate this process for finalists prior to final award, or only post-award? This affects how respondents plan legal and integration resources against the proposal timeline.

**Q16.0** — The Security questionnaire specifically asks whether the solution works in the Greater China region given compliance and government restrictions. Is Greater China within the scope of this RFP, or is it a future phase following North American deployment? This materially affects architectural requirements and licensing obligations.

**Q17.0** — The Security questionnaire contains extensive Personal Data obligations but does not identify what data elements the GRE&T platform will collect from guests. Can Marriott specify which data types are in scope — e.g., viewing behavior, room number, Bonvoy loyalty ID, device identifiers — so respondents can accurately assess their compliance posture?

---

## Appendix 2 & 3 — Channel Lineups

**Q18.0** — Appendix 2 (US Approved Channel Lineup) and Appendix 3 (Canada Approved Channel Lineup) appear as headers only in the provided RFP document with no channel-level detail included. Can Marriott provide the full channel lists for both? These are necessary for respondents to assess content licensing scope, cost, and lineup compliance.

---

## Price Sheet (Questionnaire)

**Q19.0** — The Price Sheet includes a volume rebate table with suggested tiers and discount percentages but provides no methodology. Is volume calculated on total enrolled rooms across the Marriott portfolio, or per individual hotel? At what point — contract execution or live deployment — is room count locked for rebate tier qualification?

---

## Process

**Q20.0** — Beyond the Excel questionnaire, are there specific page limits, required sections, or formatting standards for the narrative proposal? The RFP references "Proposals and any representative artifacts" but does not define what constitutes a complete or compliant submission.

---

That's 20 questions across 8 sections in document order. Ready to drop these directly into the clarification form whenever you are.

### SCOTT (2026-05-06T18:44)
Q4.0 the bullet above says, " ·       Cloud Rendered UX: The TV interface is delivered via a cloud browser. It is compatible with either a set top box connected to a standard television or a smart TV."

### CLAUDE (2026-05-06T18:44)
 You're right — the RFP explicitly states compatibility with **either** a set top box **or** a smart TV. Q4.0 as written mischaracterizes it as smart TV only. Let me fix that:

---

**Q4.0 (revised)** — GRE&T is described as compatible with either a set top box connected to a standard television or a smart TV. However, no approved device specifications are provided for either path. What are the approved set top box models and smart TV OS platforms/minimum firmware versions within Marriott's current deployed fleet? Are respondents expected to support all devices currently in GRE 1.0 and GRE 2.0 properties, or only a forward-looking approved hardware list?

---

That's a stronger question too — it covers both hardware paths and still surfaces the missing spec gap. Want to keep going through the rest or move to filling out the form?

### SCOTT (2026-05-06T18:51)
Q6. needs a bit of clarification.  We know who the current approved GRE SI's are.  BPRF isn't one of them.  The question needs to be around the takover of the legacy platforms,  is that going to be something that happens, then if so, will we support the legacy versions  via the SI (GRE 1.0 & 2.0), or will we recieve the requitese approval access  to the Mariot managed UX (vendirs, etc.) for gre 2.0.  My guess is that their intent is that the exisiting providers will be the ones to support the gre 1.0 and 2.0 until they upgrade to GRE&T.  But since we are not a current provider, need to try and shae this so that w will somehow get access to the 5,700 hotels

### CLAUDE (2026-05-06T18:51)
 Exactly right — the strategic play here is making sure Blueprint RF doesn't get locked out of the 5,700 legacy hotels just because you're not a current approved SI. The question needs to open the door without tipping your hand that you're not already in the SI program. Here's the revised version:

---

**Q6.0 (revised)** — The RFP indicates GRE&T will ramp in Q4 2026, while approximately 5,700 hotels remain on GRE 1.0 and GRE 2.0 during the transition period. For newly selected content distribution vendors who are not current GRE 1.0/2.0 system integrators, what is the intended path to serve those legacy properties during the transition? Specifically: (a) will newly selected vendors be expected to support GRE 1.0/2.0 properties through the existing approved SI ecosystem, (b) will Marriott provide newly selected vendors with the necessary access credentials and platform permissions to support GRE 2.0's Marriott-managed UX directly, or (c) is the expectation that legacy properties will only be served by current approved providers until they migrate to GRE&T? Understanding this is critical to accurately scoping the addressable opportunity and transition support model in our proposal.

---

That question does a few things for you: it signals you understand the platform landscape, doesn't expose that BPRF isn't currently approved, and forces Marriott to define on record whether new entrants get access to the legacy base or get effectively frozen out until GRE&T migration. Ready to keep refining or move to the form?

### SCOTT (2026-05-06T18:57)
not sure I undrstand #9.  it is part of the rfp overview. and it says:

A.    Monetizing advertising and data-enablement opportunities for both Marriott and the Partner across video, display and unique opportunities brought forth in partnership
·       Propose shared economics across advertising revenue including but not limited to advertising sales, reseller agreements, data enablement, and other unique collaborative opportunities e.g., UX units
·       Proposed shared economics across Partner subscription acquisition including live TV and apps

### CLAUDE (2026-05-06T18:57)
 You're right — re-reading that section, Marriott is telling respondents what **they** need to propose (shared economics, revenue share structures, etc.). It's not a gap or ambiguity in the RFP — it's an instruction. There's nothing to clarify because Marriott is explicitly asking vendors to come with their own creative commercial structures.

Q9.0 as written doesn't hold up. It's not a legitimate clarification question — it's us asking Marriott to define something they've intentionally left open for vendors to propose.

Two options:

1. **Drop it entirely** — the section is clear enough, and asking about it could signal we don't fully understand the RFP
2. **Replace it with a sharper question** from the Advertising & Partnerships questionnaire tab that actually has a gap — for example, the questionnaire asks about Riott Media inventory types but never defines which inventory Marriott controls vs. what the SI/vendor controls, which is a real ambiguity worth surfacing

Which direction do you want to go?

### SCOTT (2026-05-06T18:57)
let me see your suggestion here

### CLAUDE (2026-05-06T18:57)
 Here's the replacement:

---

**Q9.0 (revised)** — The Advertising & Partnerships questionnaire asks respondents to identify which Riott Media inventory types they can sell (guest-room entertainment TV, Wi-Fi portal display, owned digital, offsite digital, etc.). However, it is unclear which of these inventory types Marriott directly controls versus what is controlled or influenced by the content distribution vendor or the property's existing technology infrastructure. Can Marriott clarify the ownership and control structure of each inventory type listed, and identify any inventory categories where access or activation is dependent on the selected content vendor's platform or the existing SI infrastructure?

---

This one is strategically useful for BPRF too — because the answer will reveal whether Wi-Fi portal display inventory (which is squarely in your wheelhouse) is something you could potentially bring to the table as part of a broader partnership play. Want to keep it or adjust the angle?

### SCOTT (2026-05-06T18:59)
we BPRF are owned by Cpx.  Cox also owns Cox Media.  I think we have this covered.

### CLAUDE (2026-05-06T18:59)
 That changes the calculus completely — if Cox Media is already in the advertising sales business and BPRF sits under the same parent, you potentially have a built-in answer to the Riott Media partnership question that most pure content vendors won't have. That's a competitive differentiator worth positioning carefully in the proposal itself.

For the clarification question though, same conclusion as Q9.0 original — if Cox Media already knows this space, BPRF likely already understands the inventory control structure well enough that asking about it signals weakness rather than diligence.

**Recommendation: drop Q9.0 entirely** and save the Cox/Cox Media angle for the proposal where it can be framed as a strength — essentially positioning BPRF/Cox as a one-stop shop covering both the managed Wi-Fi infrastructure and the advertising demand side through Cox Media.

Want me to flag that as a key narrative thread to develop when we get to the proposal stage? And should we move on to tightening the remaining questions?

### SCOTT (2026-05-06T18:59)
drop the question.  give me the entire list again so I don;t have to keep scrolling.

### CLAUDE (2026-05-06T19:00)
 Here's the full current list:

---

## RFP Overview

**Q1.0** — The RFP states Marriott may select "one or multiple respondents" and separately identifies objectives spanning content distribution, advertising monetization, and subscription acquisition. Are these treated as distinct award categories (e.g., a content partner award vs. an advertising partner award), or is Marriott seeking integrated respondents who address all objectives? This materially affects whether a partial-scope proposal is competitive.

**Q2.0** — The RFP lists "Scale reliably across a varied hotel fleet, including variations in network quality" as a core objective but provides no minimum network specifications. Will Marriott publish minimum bandwidth, latency, or infrastructure prerequisites that properties must meet? Without this, respondents cannot accurately scope fallback or degraded-mode requirements.

**Q3.0** — The RFP states "Reduce content costs for hotels for live TV and D2C app content" as an objective and references 130M+ hours of annual app consumption. Which specific D2C apps are currently approved or required within GRE&T? Are respondents expected to negotiate D2C licensing directly, or does Marriott hold those relationships?

---

## Background: GRE&T Environment

**Q4.0** — GRE&T is described as compatible with either a set top box connected to a standard television or a smart TV. However, no approved device specifications are provided for either path. What are the approved set top box models and smart TV OS platforms/minimum firmware versions within Marriott's current deployed fleet? Are respondents expected to support all devices currently in GRE 1.0 and GRE 2.0 properties, or only a forward-looking approved hardware list?

**Q5.0** — Approximately 5,700 hotels remain on GRE 1.0 (~2,900) and GRE 2.0 (~2,800), with GRE&T ramping in Q4 2026. What is the expected migration pace — hotels per quarter or per year? Are respondents expected to simultaneously support all three environments, and for how long is dual/triple-stack support anticipated?

**Q6.0** — The RFP indicates GRE&T will ramp in Q4 2026, while approximately 5,700 hotels remain on GRE 1.0 and GRE 2.0 during the transition period. For newly selected content distribution vendors who are not current GRE 1.0/2.0 system integrators, what is the intended path to serve those legacy properties during the transition? Specifically: (a) will newly selected vendors be expected to support GRE 1.0/2.0 properties through the existing approved SI ecosystem, (b) will Marriott provide newly selected vendors with the necessary access credentials and platform permissions to support GRE 2.0's Marriott-managed UX directly, or (c) is the expectation that legacy properties will only be served by current approved providers until they migrate to GRE&T? Understanding this is critical to accurately scoping the addressable opportunity and transition support model in our proposal.

**Q7.0** — The RFP references integration with Marriott's "cloud-based architecture" and cloud browser-rendered UX but provides no technical specifications. Will Marriott share GRE&T API documentation, SDK specs, or a technical reference architecture prior to proposal submission? Without this, respondents cannot accurately scope integration effort or cost.

---

## Monetize Advertising & Data-Enablement

**Q8.0** — The RFP references "preferred/exclusive commercial business" and "net new" entertainment customers in the context of the advertising/reseller opportunity. Is Marriott seeking an exclusive advertising monetization partner, or will multiple vendors be awarded rights? If exclusive, does exclusivity apply per inventory type (e.g., live TV vs. in-app vs. Wi-Fi portal display)?

**Q9.0** — The RFP references upfront CAPEX investment "in exchange for net new and preferred/exclusive commercial business of 1M+ new entertainment customers." Is there a minimum financial commitment Marriott is seeking from partners for this consideration? And how is "net new entertainment customer" defined — Bonvoy member, new subscriber, or unique viewer?

**Q10.0** — The RFP cites 450M+ hours of live TV and 130M+ hours of app content consumed annually as the basis for advertising revenue share. What is the current state of advertising monetization on GRE 1.0/2.0 platforms? Are there existing ad contracts or commitments the selected partner would need to honor or transition?

---

## RFP Requirements / Contract Terms

**Q11.0** — The RFP states brand-standard channel lineups must be offered while also allowing "hotel-level customization." What is the enforcement mechanism when a hotel owner wishes to deviate from the brand standard lineup? Is the respondent's obligation to offer the compliant lineup, to enforce it, or both?

**Q12.0** — The RFP asks respondents to confirm all pricing is net to hotel and excludes third-party markups, but the contract commercialization model is described as "needing to be refined." Is pricing contracted at the Marriott corporate level and then passed to hotels, or are respondents expected to contract hotel-by-hotel? Clarifying this is essential to structuring the pricing model.

**Q13.0** — The Commercials questionnaire asks respondents to describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T. Does Marriott expect respondents to propose pricing for active GRE 1.0 properties as well, or only GRE 2.0 and GRE&T?

---

## MSA, DPA & Security Review

**Q14.0** — The RFP states all chosen vendors must complete an "Architecture and Security Policy review" and execute an MSA and DPA. Will Marriott initiate this process for finalists prior to final award, or only post-award? This affects how respondents plan legal and integration resources against the proposal timeline.

**Q15.0** — The Security questionnaire specifically asks whether the solution works in the Greater China region given compliance and government restrictions. Is Greater China within the scope of this RFP, or is it a future phase following North American deployment? This materially affects architectural requirements and licensing obligations.

**Q16.0** — The Security questionnaire contains extensive Personal Data obligations but does not identify what data elements the GRE&T platform will collect from guests. Can Marriott specify which data types are in scope — e.g., viewing behavior, room number, Bonvoy loyalty ID, device identifiers — so respondents can accurately assess their compliance posture?

---

## Appendix 2 & 3 — Channel Lineups

**Q17.0** — Appendix 2 (US Approved Channel Lineup) and Appendix 3 (Canada Approved Channel Lineup) appear as headers only in the provided RFP document with no channel-level detail included. Can Marriott provide the full channel lists for both? These are necessary for respondents to assess content licensing scope, cost, and lineup compliance.

---

## Price Sheet

**Q18.0** — The Price Sheet includes a volume rebate table with suggested tiers and discount percentages but provides no methodology. Is volume calculated on total enrolled rooms across the Marriott portfolio, or per individual hotel? At what point — contract execution or live deployment — is room count locked for rebate tier qualification?

---

## Process

**Q19.0** — Beyond the Excel questionnaire, are there specific page limits, required sections, or formatting standards for the narrative proposal? The RFP references "Proposals and any representative artifacts" but does not define what constitutes a complete or compliant submission.

---

19 questions total. Ready to start populating the clarification form, or do you want to keep refining first?

### SCOTT (2026-05-06T19:51)
on # 11, right now the channel line up is the minimum,  the indiviusals are allowe3d to go aboe at their ow expense.  don;t eed this quesito.

### CLAUDE (2026-05-06T19:51)
 Agreed — if the brand standard is already established as a floor and hotels can add above it at their own cost, there's no ambiguity to clarify. Drop Q11.0 and renumber. Here's the updated full list:

---

## RFP Overview

**Q1.0** — The RFP states Marriott may select "one or multiple respondents" and separately identifies objectives spanning content distribution, advertising monetization, and subscription acquisition. Are these treated as distinct award categories (e.g., a content partner award vs. an advertising partner award), or is Marriott seeking integrated respondents who address all objectives? This materially affects whether a partial-scope proposal is competitive.

**Q2.0** — The RFP lists "Scale reliably across a varied hotel fleet, including variations in network quality" as a core objective but provides no minimum network specifications. Will Marriott publish minimum bandwidth, latency, or infrastructure prerequisites that properties must meet? Without this, respondents cannot accurately scope fallback or degraded-mode requirements.

**Q3.0** — The RFP states "Reduce content costs for hotels for live TV and D2C app content" as an objective and references 130M+ hours of annual app consumption. Which specific D2C apps are currently approved or required within GRE&T? Are respondents expected to negotiate D2C licensing directly, or does Marriott hold those relationships?

---

## Background: GRE&T Environment

**Q4.0** — GRE&T is described as compatible with either a set top box connected to a standard television or a smart TV. However, no approved device specifications are provided for either path. What are the approved set top box models and smart TV OS platforms/minimum firmware versions within Marriott's current deployed fleet? Are respondents expected to support all devices currently in GRE 1.0 and GRE 2.0 properties, or only a forward-looking approved hardware list?

**Q5.0** — Approximately 5,700 hotels remain on GRE 1.0 (~2,900) and GRE 2.0 (~2,800), with GRE&T ramping in Q4 2026. What is the expected migration pace — hotels per quarter or per year? Are respondents expected to simultaneously support all three environments, and for how long is dual/triple-stack support anticipated?

**Q6.0** — The RFP indicates GRE&T will ramp in Q4 2026, while approximately 5,700 hotels remain on GRE 1.0 and GRE 2.0 during the transition period. For newly selected content distribution vendors who are not current GRE 1.0/2.0 system integrators, what is the intended path to serve those legacy properties during the transition? Specifically: (a) will newly selected vendors be expected to support GRE 1.0/2.0 properties through the existing approved SI ecosystem, (b) will Marriott provide newly selected vendors with the necessary access credentials and platform permissions to support GRE 2.0's Marriott-managed UX directly, or (c) is the expectation that legacy properties will only be served by current approved providers until they migrate to GRE&T? Understanding this is critical to accurately scoping the addressable opportunity and transition support model in our proposal.

**Q7.0** — The RFP references integration with Marriott's "cloud-based architecture" and cloud browser-rendered UX but provides no technical specifications. Will Marriott share GRE&T API documentation, SDK specs, or a technical reference architecture prior to proposal submission? Without this, respondents cannot accurately scope integration effort or cost.

---

## Monetize Advertising & Data-Enablement

**Q8.0** — The RFP references "preferred/exclusive commercial business" and "net new" entertainment customers in the context of the advertising/reseller opportunity. Is Marriott seeking an exclusive advertising monetization partner, or will multiple vendors be awarded rights? If exclusive, does exclusivity apply per inventory type (e.g., live TV vs. in-app vs. Wi-Fi portal display)?

**Q9.0** — The RFP references upfront CAPEX investment "in exchange for net new and preferred/exclusive commercial business of 1M+ new entertainment customers." Is there a minimum financial commitment Marriott is seeking from partners for this consideration? And how is "net new entertainment customer" defined — Bonvoy member, new subscriber, or unique viewer?

**Q10.0** — The RFP cites 450M+ hours of live TV and 130M+ hours of app content consumed annually as the basis for advertising revenue share. What is the current state of advertising monetization on GRE 1.0/2.0 platforms? Are there existing ad contracts or commitments the selected partner would need to honor or transition?

---

## RFP Requirements / Contract Terms

**Q11.0** — The RFP asks respondents to confirm all pricing is net to hotel and excludes third-party markups, but the contract commercialization model is described as "needing to be refined." Is pricing contracted at the Marriott corporate level and then passed to hotels, or are respondents expected to contract hotel-by-hotel? Clarifying this is essential to structuring the pricing model.

**Q12.0** — The Commercials questionnaire asks respondents to describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T. Does Marriott expect respondents to propose pricing for active GRE 1.0 properties as well, or only GRE 2.0 and GRE&T?

---

## MSA, DPA & Security Review

**Q13.0** — The RFP states all chosen vendors must complete an "Architecture and Security Policy review" and execute an MSA and DPA. Will Marriott initiate this process for finalists prior to final award, or only post-award? This affects how respondents plan legal and integration resources against the proposal timeline.

**Q14.0** — The Security questionnaire specifically asks whether the solution works in the Greater China region given compliance and government restrictions. Is Greater China within the scope of this RFP, or is it a future phase following North American deployment? This materially affects architectural requirements and licensing obligations.

**Q15.0** — The Security questionnaire contains extensive Personal Data obligations but does not identify what data elements the GRE&T platform will collect from guests. Can Marriott specify which data types are in scope — e.g., viewing behavior, room number, Bonvoy loyalty ID, device identifiers — so respondents can accurately assess their compliance posture?

---

## Appendix 2 & 3 — Channel Lineups

**Q16.0** — Appendix 2 (US Approved Channel Lineup) and Appendix 3 (Canada Approved Channel Lineup) appear as headers only in the provided RFP document with no channel-level detail included. Can Marriott provide the full channel lists for both? These are necessary for respondents to assess content licensing scope, cost, and lineup compliance.

---

## Price Sheet

**Q17.0** — The Price Sheet includes a volume rebate table with suggested tiers and discount percentages but provides no methodology. Is volume calculated on total enrolled rooms across the Marriott portfolio, or per individual hotel? At what point — contract execution or live deployment — is room count locked for rebate tier qualification?

---

## Process

**Q18.0** — Beyond the Excel questionnaire, are there specific page limits, required sections, or formatting standards for the narrative proposal? The RFP references "Proposals and any representative artifacts" but does not define what constitutes a complete or compliant submission.

---

18 questions. Want to keep refining or move to populating the clarification form?

### SCOTT (2026-05-06T19:57)
where does it say, "RFP asks respondents to confirm all pricing is net to hotel and excludes third-party markups'

### CLAUDE (2026-05-06T19:58)
 Good catch — let me verify that.

That language is in the **Commercials & Pricing tab of the questionnaire**, not the RFP body itself. So Q11.0 is sourced correctly, but the attribution in the question is wrong — it should reference the questionnaire, not the RFP. Here's the corrected version:

---

**Q11.0 (revised)** — The Commercials & Pricing questionnaire instructs respondents to confirm all pricing is net to hotel, PRPM, and exclusive of all third-party markups. However, the RFP body describes the contract commercialization model as "needing to be refined." Is pricing expected to be contracted at the Marriott corporate level and then commercialized to hotels, or are respondents expected to contract directly with individual hotels? Clarifying the contracting structure is essential to accurately modeling net pricing.

---

That's tighter and more accurately sourced. Want to keep going or is the list ready to go into the form?

### SCOTT (2026-05-06T20:02)
Q12 is kind of tied to my framing for Q6.  why are you only asking abut gre 1.0 and not 2.0 hotels?

### CLAUDE (2026-05-06T20:02)
 You're right — if the whole point of Q6 is to get access to all 5,700 legacy hotels, then Q12 should be asking about both GRE 1.0 and GRE 2.0 pricing, not just 1.0. The way it's written now it actually contradicts the strategic intent of Q6. Here's the fix:

---

**Q12.0 (revised)** — The Commercials questionnaire asks respondents to describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T. Does Marriott expect respondents to propose pricing for active GRE 1.0 and GRE 2.0 properties during the transition period, or only for GRE&T? If transition-period pricing is expected, should it be structured as a separate tier or incorporated within the PRPM model?

---

That keeps it consistent with Q6's framing that BPRF intends to be in play across all 5,700 legacy hotels, not just waiting for GRE&T migration. Want the full list again with both Q11 and Q12 updated?

### SCOTT (2026-05-06T20:03)
shoudl we just call it out as a takeover opportuniy from the incumbent providers

### CLAUDE (2026-05-06T20:03)
 No — I wouldn't. A few reasons:

1. **It signals you're not a current approved provider** — which Marriott may not have fully registered yet. No need to draw attention to it.

2. **It could come across as adversarial** — framing it as a "takeover" of incumbents in a clarification question to Marriott could raise flags about whether you're a collaborative partner or a disruptor looking to poach existing relationships.

3. **The clarification process is public** — the RFP explicitly states Marriott will distribute all clarification responses to all respondents with no indication of who asked. Your competitors will read every question you submit. You don't want to tip your hand or your strategy.

The better play is to keep Q6 and Q12 professionally neutral — framed around "newly selected vendors" and "transition period pricing" — which asks Marriott to define the access path without revealing that BPRF specifically needs it. Then in the **proposal itself**, where only Marriott sees it, you can make the affirmative case for why BPRF/Cox is positioned to serve both the legacy base and GRE&T. That's where the takeover narrative belongs. Want the full updated list now?

### SCOTT (2026-05-06T20:04)
they know full well we are not a current provider. there are only 4 approvd GRE providers.  we have over 1,000 marripess where are the managed wifi privder.  we have been trying to get into gre for close to a decade

### CLAUDE (2026-05-06T20:04)
 That's a completely different context — and honestly it changes the tone of how aggressive you can be in the clarification questions. Marriott knows exactly who you are, knows you're not a current GRE provider, and presumably issued this RFP in part to open the door to new entrants. The 1,000+ Marriott properties where BPRF is already the managed WiFi provider is a significant existing footprint that Marriott is well aware of.

So the real question is — does being more direct in Q6 and Q12 actually help you, or does the neutral framing still serve you better even in this context?

My honest take: **the neutral framing still wins**, but for a different reason. It's not about hiding who you are — Marriott knows. It's about **making Marriott answer on the record** in a way that benefits all new entrants, including BPRF. If you frame it as "we want access to legacy hotels," Marriott can dodge it. If you frame it as "what is the intended path for newly selected vendors," Marriott has to define a policy — and that policy applies to everyone, including you.

The proposal is where you make the BPRF-specific case. The clarification questions are where you get Marriott to open doors on the record.

Want to keep Q6 and Q12 as they are with that framing in mind, and get the final list together?

### SCOTT (2026-05-06T20:06)
13 seems like a nothing sandwhich.  not sure i care when.  we have soc2 type 2 and iso 27001, not sure i am concerneced abiut their review

### CLAUDE (2026-05-06T20:06)
 Agreed — if BPRF already has SOC2 Type 2 and ISO 27001, you'll sail through their architecture and security review whenever it happens. The timing question is a non-issue for you. Drop Q13 and renumber. Want the full clean list?

### SCOTT (2026-05-06T20:06)
yes

### CLAUDE (2026-05-06T20:07)
 ## RFP Overview

**Q1.0** — The RFP states Marriott may select "one or multiple respondents" and separately identifies objectives spanning content distribution, advertising monetization, and subscription acquisition. Are these treated as distinct award categories (e.g., a content partner award vs. an advertising partner award), or is Marriott seeking integrated respondents who address all objectives? This materially affects whether a partial-scope proposal is competitive.

**Q2.0** — The RFP lists "Scale reliably across a varied hotel fleet, including variations in network quality" as a core objective but provides no minimum network specifications. Will Marriott publish minimum bandwidth, latency, or infrastructure prerequisites that properties must meet? Without this, respondents cannot accurately scope fallback or degraded-mode requirements.

**Q3.0** — The RFP states "Reduce content costs for hotels for live TV and D2C app content" as an objective and references 130M+ hours of annual app consumption. Which specific D2C apps are currently approved or required within GRE&T? Are respondents expected to negotiate D2C licensing directly, or does Marriott hold those relationships?

---

## Background: GRE&T Environment

**Q4.0** — GRE&T is described as compatible with either a set top box connected to a standard television or a smart TV. However, no approved device specifications are provided for either path. What are the approved set top box models and smart TV OS platforms/minimum firmware versions within Marriott's current deployed fleet? Are respondents expected to support all devices currently in GRE 1.0 and GRE 2.0 properties, or only a forward-looking approved hardware list?

**Q5.0** — Approximately 5,700 hotels remain on GRE 1.0 (~2,900) and GRE 2.0 (~2,800), with GRE&T ramping in Q4 2026. What is the expected migration pace — hotels per quarter or per year? Are respondents expected to simultaneously support all three environments, and for how long is dual/triple-stack support anticipated?

**Q6.0** — The RFP indicates GRE&T will ramp in Q4 2026, while approximately 5,700 hotels remain on GRE 1.0 and GRE 2.0 during the transition period. For newly selected content distribution vendors who are not current GRE 1.0/2.0 system integrators, what is the intended path to serve those legacy properties during the transition? Specifically: (a) will newly selected vendors be expected to support GRE 1.0/2.0 properties through the existing approved SI ecosystem, (b) will Marriott provide newly selected vendors with the necessary access credentials and platform permissions to support GRE 2.0's Marriott-managed UX directly, or (c) is the expectation that legacy properties will only be served by current approved providers until they migrate to GRE&T? Understanding this is critical to accurately scoping the addressable opportunity and transition support model in our proposal.

**Q7.0** — The RFP references integration with Marriott's "cloud-based architecture" and cloud browser-rendered UX but provides no technical specifications. Will Marriott share GRE&T API documentation, SDK specs, or a technical reference architecture prior to proposal submission? Without this, respondents cannot accurately scope integration effort or cost.

---

## Monetize Advertising & Data-Enablement

**Q8.0** — The RFP references "preferred/exclusive commercial business" and "net new" entertainment customers in the context of the advertising/reseller opportunity. Is Marriott seeking an exclusive advertising monetization partner, or will multiple vendors be awarded rights? If exclusive, does exclusivity apply per inventory type (e.g., live TV vs. in-app vs. Wi-Fi portal display)?

**Q9.0** — The RFP references upfront CAPEX investment "in exchange for net new and preferred/exclusive commercial business of 1M+ new entertainment customers." Is there a minimum financial commitment Marriott is seeking from partners for this consideration? And how is "net new entertainment customer" defined — Bonvoy member, new subscriber, or unique viewer?

**Q10.0** — The RFP cites 450M+ hours of live TV and 130M+ hours of app content consumed annually as the basis for advertising revenue share. What is the current state of advertising monetization on GRE 1.0/2.0 platforms? Are there existing ad contracts or commitments the selected partner would need to honor or transition?

---

## RFP Requirements / Contract Terms

**Q11.0** — The Commercials & Pricing questionnaire instructs respondents to confirm all pricing is net to hotel, PRPM, and exclusive of all third-party markups. However, the RFP body describes the contract commercialization model as "needing to be refined." Is pricing expected to be contracted at the Marriott corporate level and then commercialized to hotels, or are respondents expected to contract directly with individual hotels? Clarifying the contracting structure is essential to accurately modeling net pricing.

**Q12.0** — The Commercials questionnaire asks respondents to describe how pricing will decrease as hotels transition from GRE 1.0/2.0 to GRE&T. Does Marriott expect respondents to propose pricing for active GRE 1.0 and GRE 2.0 properties during the transition period, or only for GRE&T? If transition-period pricing is expected, should it be structured as a separate tier or incorporated within the PRPM model?

---

## Security

**Q13.0** — The Security questionnaire specifically asks whether the solution works in the Greater China region given compliance and government restrictions. Is Greater China within the scope of this RFP, or is it a future phase following North American deployment? This materially affects architectural requirements and licensing obligations.

**Q14.0** — The Security questionnaire contains extensive Personal Data obligations but does not identify what data elements the GRE&T platform will collect from guests. Can Marriott specify which data types are in scope — e.g., viewing behavior, room number, Bonvoy loyalty ID, device identifiers — so respondents can accurately assess their compliance posture?

---

## Appendix 2 & 3 — Channel Lineups

**Q15.0** — Appendix 2 (US Approved Channel Lineup) and Appendix 3 (Canada Approved Channel Lineup) appear as headers only in the provided RFP document with no channel-level detail included. Can Marriott provide the full channel lists for both? These are necessary for respondents to assess content licensing scope, cost, and lineup compliance.

---

## Price Sheet

**Q16.0** — The Price Sheet includes a volume rebate table with suggested tiers and discount percentages but provides no methodology. Is volume calculated on total enrolled rooms across the Marriott portfolio, or per individual hotel? At what point — contract execution or live deployment — is room count locked for rebate tier qualification?

---

## Process

**Q17.0** — Beyond the Excel questionnaire, are there specific page limits, required sections, or formatting standards for the narrative proposal? The RFP references "Proposals and any representative artifacts" but does not define what constitutes a complete or compliant submission.

---

17 questions. Ready to populate the form?

### SCOTT (2026-05-06T20:13)
appendix 2 and 3 is visibale.  the qestuo here is on appendix 2.  it calls outr Sonfi as the optional VOD App.  sonfifi is a current GRE provider and a cp,petior.  need to ask if they are the brand standardard or if we can use our own VOD app. which we have with fiull licensing, hospitality relase window, etc.
[File uploaded: 1778098290329_image.png]
[File uploaded: 1778098305134_image.png]

### CLAUDE (2026-05-06T20:13)
 Great catch — and this is actually one of the most strategically important questions in the entire clarification set. BPRF has a fully licensed VOD app with hospitality release windows, and Sonifi (a current GRE competitor) is listed as the optional VOD provider. You need Marriott to clarify whether that's a brand standard lock-in or an open field. Here's the revised Q15.0:

---

**Q15.0 (revised)** — Appendix 2 identifies Sonifi as the optional VOD application for the US channel lineup. Is Sonifi designated as the approved brand standard VOD provider, or are newly selected content distribution vendors permitted to propose an alternative VOD solution — provided it meets Marriott's technical requirements, content licensing standards, and hospitality release window obligations? Clarifying this is critical to understanding whether the VOD layer is an open competitive element of this RFP or a pre-determined component.

---

That question is clean, doesn't overplay your hand, signals you have a qualified alternative without naming it, and forces Marriott to answer on the record in a response that goes to every respondent — including Sonifi. Want the full updated list?

### SCOTT (2026-05-06T20:18)
on 17, may need to expand on it.  doesn;t the rfp say in one section that must repsond to entire rfp, and in antoehr talk aboiut parts of the rfp respondants may not be able to repsond to?

### CLAUDE (2026-05-06T20:18)
 Yes — exactly right. The RFP has a direct contradiction. In one place it says "All respondents must respond to the entire RFP" as a bold heading, but in the RFP Overview it says "We are open to varying proposals that help us in meeting one or more of the objectives below" and "Whether you provide a partnership, content, services or other, we welcome hearing how your company can help." Those two positions are in direct conflict. Here's the expanded question:

---

**Q17.0 (revised)** — The RFP contains what appears to be conflicting guidance regarding scope of response. The "RFP Requirements" section states in bold that "All respondents must respond to the entire RFP," yet the "RFP Overview" states that Marriott is "open to varying proposals that help us in meeting one or more of the objectives" and welcomes respondents who provide "a partnership, content, services or other." Can Marriott clarify whether a respondent who cannot address all sections of the questionnaire — for example, a respondent with strong capabilities in content distribution but limited advertising monetization infrastructure, or vice versa — will be disqualified, or whether partial-scope proposals will be evaluated on the merits of the areas addressed? If full response is required, should respondents who cannot address a specific section indicate that explicitly rather than omitting it?

---

That question does double duty — it protects respondents who can't cover every section, and it signals to Marriott that the contradiction needs to be resolved on the record. Want the full final list now?

### SCOTT (2026-05-06T20:22)
good job.  noe listr of questrions.  I am not fillign out the form.  I am putting it in an email to Par our Marriott brand amager to review, decide and aggregate with eveyone elses quetions.  for clairy Par reports up through me. Help me draft teh email subject and intro.  I have the questiosn ready to go now.

### CLAUDE (2026-05-06T20:22)

Short, clean, and positions this correctly — you're the one driving it, Par is the filter before it goes to Marriott. Want me to adjust the tone or add anything, like a specific ask on when you need Par's feedback given the May 8 deadline?

### SCOTT (2026-05-06T20:23)
a litle too formal. par and have worked together for more than a decade and are fre3inds outside of work.  i am the boss and eed to keep professional, but that is a litle over the top coming from em

### CLAUDE (2026-05-06T20:24)

That feel more like you? Short, gives Par the context and the ask, acknowledges their relationship with Marriott without being over the top about it. Want any tweaks before you attach the questions and send?
