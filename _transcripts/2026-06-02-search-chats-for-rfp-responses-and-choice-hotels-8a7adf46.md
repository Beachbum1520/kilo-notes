# Search chats for RFP responses and Choice Hotels
Date: 2026-06-02
Conversation: 8a7adf46-6f4b-45e4-9c25-298c957f3ac0
Domain: business-ops

## Summary
**Conversation Overview**

Scott works in a sales/business development role at BPRF (a managed Wi-Fi and hospitality technology company backed by Cox) and is engaged in multiple concurrent RFP and sales efforts in the hospitality vertical. This conversation began with Scott requesting two things: the current date and time (confirmed as Tuesday, June 2, 2026, 6:50 AM PDT, Portland time), and a search of prior conversations covering RFP responses and Choice Hotels activity. Claude retrieved both threads and summarized them in detail before new work began.

The Marriott GRE&T RFP thread involved a completed clarification-question phase (17 questions organized by RFP section, submitted via Par to Jason Orsin ahead of a May 8 deadline). Strategic calls included sharpening a question about legacy GRE access, dropping a question to preserve a competitive strength for the proposal itself, and flagging Sonifi listed as the VOD provider when BPRF has its own licensed solution. On Schedule 7 SLA negotiation, Scott directed Par to hold the 10% credit cap position with Jady as the approval gate before any movement. The actual proposal response remains the open work item. The Choice Hotels inside sales thread involved a Manila-based team, an ETF/cancel-for-convenience challenge with Cox incumbent contracts, and a pivot to execution and training — with Lloyd (Cloudstaff CEO) committing two weeks of free training from a sales consultant named Wayne, flying to Cebu to work with the team on call recordings and QA reviews. Whether Jady provided a clean directional answer on the ETF question remained unresolved.

Scott then introduced a new workstream: a Choice Hotels HSIA RFP (file: HSIA_RFP_Vendors_2026_FINAL.xlsx). Claude fully ingested the workbook and surfaced that this is a structured capabilities questionnaire across 12 scored categories with a tight timeline — clarifications due Friday June 5, Choice's response June 9, full vendor responses due June 22. Claude noted the strategic connection between this corporate-level RFP and the inside-sales effort: a brand-standard designation here would resolve the property-by-property ETF problem from the top down. Scott directed Claude to start with clarification questions. Claude produced a set of 10 questions grouped by theme: Program Scope and Award Structure (including the question about whether the award becomes a mandated brand standard, which Scott flagged as the most strategically important), Commercial and Owner Economics, Choice Systems Integration (Safety NetAccess/ILP, choiceADVANTAGE PMS, Select Networx), Pricing and Response Format, and Pilot structure. Claude flagged that the RFP was sent to Mark Ludlow and Kathy Hatala (cc Jady), with Scott not on the distribution, and that submission routing is a decision Scott needs to make before Friday. The conversation ended with Claude asking whether Scott wanted to cut, add, or sharpen questions before finalizing.

Key people across both threads: Par (aggregation/relationship contact on Marriott), Jason Orsin (Marriott contact), Jady (approval gate, senior stakeholder), Kathy Hatala (Choice contact, political dynamics noted), Mark Ludlow (Choice brand contact, reports to Kathy), Marie (conducted outreach to Mark), Lloyd (Cloudstaff CEO), Wayne (Cloudstaff sales training consultant). Scott's working pattern is to prioritize the clarification-question phase of RFPs as a strategic lever before drafting full responses, and to ground questions explicitly in RFP section references.

**Tool Knowledge**

Claude used the `conversation_search` tool to retrieve prior context on two topics. Searches worked effectively using specific terminology tied to the actual subject matter — "RFP response Marriott GRE&T proposal" and "Choice Hotels inside sales ETF cancel for convenience" — rather than generic terms. For the Excel workbook, Claude used `extract-text` on the uploaded file with a two-pass approach: the first call retrieved the first 300 lines, and a second call using `tail -n +90` captured the remainder, which was necessary to get full workbook coverage. Excel serial date values in the RFP timeline required manual conversion via a Python datetime calculation using the 1899-12-30 base date offset (accounting for Excel's 1900 leap year bug); this produced accurate readable dates for all four timeline milestones.

### SCOTT (2026-06-02T13:50)
get current day and time, and search all chats for convos about RFP repsonses, and choice hotels

### CLAUDE (2026-06-02T13:50)
 I need to handle two tasks here: first, get the current date and time, then search through past conversations for discussions about RFP responses and Choice Hotels. Since the user is working within a Project, the search will be scoped to that project's conversations. Let me start by fetching the precise time, then move on to searching the chat history.

 I need to convert that UTC time to Scott's local timezone in Portland—that's PDT in June, which is seven hours behind UTC. So 1:50 PM UTC becomes 6:50 AM PDT. Now let me search through the chats to find what I'm looking for.

 Looking for Choice Hotels conversations now.Now let me search for the Choice Hotels conversations.

 I'm pulling together information from both threads to give Scott a clear picture. Since he's in Portland, I need to convert the current time from UTC to his local timezone—1:50 PM UTC translates to 6:50 AM PDT. I'll organize this with some light structure to make it easy to scan across the two topic areas he asked about.It's **Tuesday, June 2, 2026, 6:50 AM PDT** (Portland time).

Here's where both threads stand based on our past conversations:

**Marriott GRE&T RFP**

You worked the clarification-question phase hard and landed the list at 17 questions, reorganized by RFP section reference, working from the RFP docx, the requirements xlsx, and the xlsb clarification template. Those went to Par for aggregation and relationship-filtering before submission to Jason Orsin ahead of the May 8 deadline — sent via email for Par's review, not entered directly into the form. A few strategic calls baked in: you sharpened Q6 (legacy GRE 1.0/2.0 access) to crack the door open without exposing competitive weakness, dropped the Cox Media advertising question to save that one-stop-shop angle as a *strength for the proposal itself*, and added the competitive flag on Sonifi being listed as the VOD provider in Appendix 2 when BPRF has its own licensed VOD solution.

Separately, on the related SLA negotiation (Schedule 7), you directed Par to hold Option 1 (the 10% credit cap) as the protective position, with Jady as the explicit approval gate before any movement toward the 50% escalating cap.

The proposal itself — the actual GRE&T response following the clarification round — is the open piece still ahead of you.

**Choice Hotels inside sales**

This evolved a lot. The core issue you raised: your savings-led pitch ("if I can save you money on managed Wi-Fi, can I send a proposal?") only works if Choice properties can actually leave their provider. Marie's attempt to get clarity from Mark surfaced two data points — Choice corporate sets *no* termination standard (it's contract-by-contract), and the Cox incumbent contract carries a 100% ETF for the full remaining term, the opposite of cancel-for-convenience — with the one counterweight that those ETFs are reportedly hard to collect. You sent Jady and Kathy the "force a decision" version, closing with "Give me a direction and I'll realign the team."

Kathy's reply was the turn: you read it as her not wanting to continue the Philippines inside sales effort (no corporate political capital in it for her), and you suspect she's quietly hoping it fails so she can pivot toward the CB sales team. Meanwhile, digging in with the team on-site, you confirmed the real problem isn't the ETF question at all — it's execution. The reps had received little to no sales training; they understood the job as getting through the call list. "Telling ain't selling" — they weren't asking for the proposal, they were letting the gatekeeper become a roadblock, not even understanding that at Choice the GK is often part of the owner/operator family and should be sold to directly.

Your move: you got Lloyd (Cloudstaff CEO) to agree to two weeks of free training from their expert sales consultant, Wayne, who's flying to Cebu to meet you and help stand up call recordings and QA sales-call reviews for the team. You remained confident the Manila team can succeed.

The open item there is whether the ETF/cancel-for-convenience question ever got a clean directional answer from Jady — that was still unresolved as the focus shifted to the training fix.

Want me to pull up the actual emails or question lists from either thread, or pick up drafting on the GRE&T proposal?

### SCOTT (2026-06-02T13:52)
nope.  we are also now goign to work on a choice rfp.  see attached
[File uploaded: [EXTERNAL] HSIA _ Choice Hotels RFP _ Cox Hospitality Network.pdf]
[File uploaded: HSIA_RFP_Vendors_2026_FINAL.xlsx]

### CLAUDE (2026-06-02T13:53)
 I need to check the xlsx skill documentation first to understand how to read the workbook, then load the Excel file Scott uploaded so I can analyze the Choice Hotels RFP data.On it. Let me read the workbook fully before we plan an approach — I've got the cover email already.

Now let me read the actual RFP workbook.

 I need to check if there are additional sheets in the workbook beyond Future Readiness to get the complete picture.

 I'm noticing the RFP Timeline dates are stored as Excel serial numbers, so I need to convert them using the Excel date system — accounting for the 1900 leap year bug where Excel incorrectly treats 1900 as a leap year.

 I'm ready to synthesize this for Scott—he wants the full picture distilled into a tight summary with the key strategic angle, the tight timeline (clarification due Friday, just three days out), and what needs tackling first, without unnecessary elaboration. abilities/information-gathering RFP* — not the same beast as Marriott GRE&T. It's a structured Excel questionnaire: Company Info, Program Requirements (scored 1-5 Yes/No/Partial across 12 categories). Choice is doing "moderate modernization."
2. This connects directly to the inside-sales / cancel-for-convenience thread — this is the corporate-level Choice relationship. Winning or placing well here changes the whole dynamic of the Manila inside sales effort (instead of cold-calling individual price-driven properties fighting ETFs, a brand-standard program win would be top-down). Worth flagging.
3. The clarification window is essentially now — clarifications due Fri Jun 5 (3 days out), Choice responds Jun 9, full responses due Jun 22. So if there are clarification questions to ask, that's the urgent near-term action, exactly like the Marriott GRE&T process. That's the most time-sensitive thing.
4. Recipients: Mark Ludlow and Kathy Hatala, cc Jady. So Kathy is on this directly — same political dynamic. Mark reports to Kathy. Scott isn't even on the original email — that's worth noting given his pattern of navigating involvement.
5. BPRF's strengths align well with what Choice is asking for: SOC2 Type II and ISO 27001 cover the security questions, managed Wi-Fi across 2,656 hotels and 200K+ endpoints hits the infrastructure requirements, PNOC proactive monitoring addresses their monitoring categories, and Cox backing handles the financial and carrier sourcing pieces. The gap is Choice-specific integrations — ILP, Safety NetAccess, choiceADVANTAGE PMS — which may or may not already be in BPRF's stack.

So the RFP is a structured questionnaire with 12 scored categories, and the timeline is tight: clarifications due Friday, Choice's response Monday, full answers due June 22. BPRF's core strengths — security certifications, managed Wi-Fi at scale, proactive monitoring, and Cox backing — map directly to what Choice needs, but I need to verify whether the Choice-specific integrations are already supported or if that's a gap to address.Got it — fully ingested both. This is a different animal from the Marriott GRE&T RFP, and the timeline is tight, so here's the read.

**What it is.** Choice is running a structured capabilities/info-gathering RFP for a "moderate modernization" of their HSIA program — not a guest-entertainment play like Marriott. It's an Excel questionnaire across three response sheets: Company Information (firmographics, financials), and Program Requirements, which is the meat — 50-some questions in 12 categories, each scored by the vendor 1–5 (Best-in-class) with Yes/No/Partial plus comments.

**Timeline — this is the urgent part:**
- Requests for clarifications due **Fri, Jun 5** (three days out)
- Choice responds to clarifications **Tue, Jun 9**
- Full vendor responses due **Mon, Jun 22**

So the same move you ran on Marriott applies here: if we want clarifications in, that window closes Friday. That's the near-term decision.

**The 12 scored categories:** Vendor Solution & Service Model, Network Architecture & Managed Services, Performance & Bandwidth Optimization, Connectivity & Carrier Strategy, Guest Experience & Access, Security & Network Protection, Monitoring/Reporting & Compliance, Support Model & SLAs, Hardware Strategy & Lifecycle, Financial Model & Owner Impact, Brand Compliance & Revenue Capabilities (the biggest block — 18 questions, all the Choice-specific stuff), and Future Readiness & Scalability.

**Where this sits strategically — worth naming up front:**

This is the corporate-level Choice relationship, and it reframes the inside-sales fight entirely. Right now the Manila team is grinding individual price-driven properties against full-value ETFs. A strong placement here is the top-down version of the same goal — brand-standard program adoption instead of property-by-property cold calls. The two efforts should inform each other.

Most of the questionnaire plays to BPRF's strengths: managed Wi-Fi at scale (2,656 hotels, 200K+ endpoints), PNOC proactive monitoring, SOC2 Type II / ISO 27001 for the security block, and the Cox parent for financials, carrier sourcing, and the financing/owner-funding questions Choice keeps hammering. The exposure areas are the Choice-specific integrations in section 11 — ILP authentication / Safety NetAccess, choiceADVANTAGE PMS, dynamic passcodes, tiered paid bandwidth. Those need a real capability check before we commit Yes/Partial scores in writing.

**One thing to flag:** the cover email went to Mark and Kathy, cc Jady — you're not on the To line. Same political terrain as the inside-sales thread, and Mark (who gave Marie the thin answer) is the named brand contact here. Worth a thought on how you want to be positioned on this before we get deep into drafting.

Where do you want to start — the clarification questions while that window's open, a capability gap-check on section 11, or the response structure overall?

### SCOTT (2026-06-02T13:54)
clairification questiosn first

### CLAUDE (2026-06-02T13:56)
 Scott needs clarification questions submitted by Friday (3 days away), so I'm drawing on the Marriott GRE&T RFP process where I developed 17 strategically-organized questions to identify genuine ambiguities and competitive openings. I need to assess what specific gaps and strategic angles exist in this RFP that warrant clarification.

The key distinction here is that this is a standard capabilities questionnaire with fewer inherent gaps than a full RFP, but there are still real ambiguities worth surfacing — and some that could strategically position BPRF favorably. I should stay disciplined and only ask what's genuinely unclear or strategically valuable, avoiding the padding Scott flagged in the Marriott round.

Looking at the actual RFP content, the scope isn't clearly defined — it doesn't specify how many properties are in scope, which Choice brands or segments are included, or whether this is a portfolio-wide mandate or owner-optional. The language around "different hotel segments" and "upscale versus midscale" suggests multiple brands are involved, but that needs clarification to scope the response properly.

The most critical question is whether the awarded vendor becomes a mandated brand standard, an approved option among several, or just a recommended choice owners can select — that distinction fundamentally determines adoption leverage and directly impacts the cancellation and ETF implications. I also need to understand the incumbent situation with Cox and whether Choice is consolidating providers or expanding the approved list.

On the financial side, the RFP mentions "owner investment considerations" and "moderate investment model" but doesn't clarify who's actually contracting and paying — whether it's Choice corporate, individual franchisees, or if the vendor funds implementation. That shapes the entire financial model and how to position financing options. I should also ask whether there's any brand-funded component or if owners bear the full cost.

Finally, the enforcement mechanism around non-compliant properties in sections 7.4 and 11.14 is vague — I need to understand what teeth Choice actually wants here and what role the vendor plays in compliance.

On integrations, I'm trying to pin down whether Safety NetAccess is the mandated ILP authentication platform and if Choice will provide API specs, whether the choiceADVANTAGE PMS integration requires API documentation from Choice, and critically, whether Choice takes a revenue share on paid-tier offerings. I also need to understand what Select Networx is and how the awarded vendor fits into that sourcing program.

For the revenue model, I'm checking if Choice's brand standards actually allow charging guests for premium Wi-Fi since many brands require free Wi-Fi for members — this directly impacts whether paid tiers are even viable. On the evaluation side, I'm noting that vendors self-score themselves 1-5, so I should understand if there's category weighting to know where to focus effort. The pricing question is tricky because the RFP asks for TCO in monthly and one-time costs, but without knowing the reference property profile — room count, number of APs — I can't calculate a meaningful unit cost.

I need to clarify whether they want actual pricing now or just capabilities with pricing deferred, and if pricing is expected, against what property model. For the pilot details, I should ask how many properties, who selects them, and who funds it. On future tech like streaming, mobile keys, and IoT, I'm wondering if these are roadmap items with timelines or just aspirational — probably worth a general answer but maybe not a formal clarification. I'm being disciplined about which questions actually matter strategically rather than asking everything.

The real priority is nailing down the award structure — whether this is a mandated brand standard going forward, an approved vendor among many, or owner-optional. That directly solves Scott's cancel-for-convenience problem and makes the inside-sales ETF issue much less relevant for new properties. I need to be selective about which questions might signal weakness, especially after seeing how Scott handled the Marriott round.

I should avoid anything implying BPRF can't already support Choice integrations, but straightforward questions about specs or access are fair game. The routing question matters too — Mark is the Choice contact with Kathy cc'd, so I'll present the questions and let Scott decide how to submit them.

I'm organizing these by the RFP's own structure since Scott prefers that approach. The ambiguities cluster around program scope, commercial terms, systems integration, pricing format, and the pilot structure, so I'll group the questions there. Each one will ground the ambiguity in actual RFP language, state the question clearly, and note why it matters for scoping the response.

I'll draft ten questions, keeping them tight and using that format that worked well on Marriott — stating the material impact at the end.

For the second question, I need to clarify whether Choice is mandating a single HSIA provider as a brand standard, creating an approved vendor list that owners choose from, or simply recommending optional solutions. This distinction fundamentally shapes how we'd structure deployment, support, and pricing.

The third question zeros in on Cox's current position in the portfolio and whether Choice wants to consolidate providers, expand the roster, or maintain the status quo with upgraded standards — this ties directly to cancellation risk.

Now I'm moving into the commercial section, looking at who bears the investment burden and how financing works across the owner base. paying party for the modernized service — Choice corporate, the individual franchise owner, or a blended model? This determines how we structure pricing, financing, and the owner-adoption approach.

Q5 — Section 11 references "tiered bandwidth services, including free and paid options" and "billing and revenue capture." Under current Choice brand standards, are properties permitted to charge guests (including loyalty members) for premium/tiered bandwidth? And does Choice intend to participate in paid-tier revenue (e.g., revenue share), or does that economic flow to the owner and/or provider?

[Real ambiguity — free-for-members policies are common, and the revenue questions can't be answered without knowing the model]

**Choice Systems Integration**

Q6 — Question 11.1 mentions Safety NetAccess for ILP authentication. I need to know if that's the mandatory platform across all in-scope brands, whether Choice will provide integration specs and support, and if providers must integrate with Safety NetAccess specifically or can deliver equivalent authentication that meets the ILP requirement.

Q7 — Question 11.8 calls out choiceADVANTAGE PMS and Select Networx in the cover email. I'm asking Choice for API documentation and a technical contact for both systems, plus clarification on what role Select Networx plays in the provider's sourcing and delivery model.

**Pricing & Response Format**

Q8 — The RFP asks for total cost of ownership with monthly and one-time costs in Question 10.1, but without a reference property profile or representative mix from Choice, I can't normalize TCO across segments. I need to know if Choice will provide that baseline.

Q9 — I'm also clarifying whether fully developed pricing is expected by June 22, or if this phase is capabilities-focused with detailed pricing deferred to shortlist/presentation. That changes how much pricing detail I commit to in writing now.

**Pilot**

Q10 — Questions 11.17–11.18 reference a pilot at "representative properties," but I need specifics on property count, brand mix, timeline, and whether Choice or the provider bears pilot costs and operational risk.

Now I'm reviewing which questions are essential to keep. Q1 on scope is genuinely unclear, so that stays. Q2 on award structure is the headline strategic question. Q3 on incumbent positioning and consolidation is also critical, though it overlaps somewhat with Q2 — but it's worth keeping since it directly addresses Cox's existing footprint as a strength rather than a weakness.

Q4 through Q9 are all material: funding source, revenue models, Safety NetAccess details, the Choice programs, TCO reference properties, and pricing timing. Q8 and Q9 could potentially merge since they're both pricing-related, but I'll keep them as a pair for now to maintain clarity, though Scott's preference for tightness might push me toward combining them later.

Q10 on pilots is genuine and worth keeping. Ten questions feels disciplined and complete—I'm deliberately not padding with things that are either answerable from the RFP itself or would come across as gaming the process, like category weightings.

I've grounded each question in actual RFP language and verified the references (Safety NetAccess at 11.1, choiceADVANTAGE PMS at 11.8, TCO at 10.1, pilot language at 11.17/11.18, and Select Networx in the cover email). Now I need to decide whether to put this in an artifact for Scott to review or keep it inline in the chat where we can iterate on it together—inline worked well on the Marriott deal, and that's how he prefers to refine. I should flag the timing and routing considerations upfront since he'll want to manage those himself. I'll open with a brief note on my approach—disciplined and grounded—then move straight into the questions using bold headers and Q labels like he responded well to before, keeping the preamble minimal.Here's a disciplined first cut — grounded in the actual RFP language and question numbers, only the genuine ambiguities and the strategic openings worth using the window on. Ten questions, grouped the way the gaps cluster.

**Program Scope & Award Structure**

**Q1** — The RFP describes "a moderate modernization approach… across our portfolio" and references variation "across different hotel segments" and "upscale versus midscale." Which Choice brands and segments are in scope, and approximately how many properties? Is the scope portfolio-wide or limited to specific brands/segments?

**Q2** — The RFP states Choice will "determine next steps" after review. Is Choice seeking to designate a mandated brand-standard HSIA provider, establish a roster of approved/preferred providers that owners select among, or recommend optional solutions owners may adopt? Whether selection results in a brand standard versus an approved-vendor designation is material to how we scope deployment, support, and commercials.

*(This is the one that matters most — it's the corporate-level answer to the cancel-for-convenience question the inside-sales team has been stuck on.)*

**Q3** — Cox is an incumbent HSIA provider at a portion of the portfolio today. Is the objective to consolidate onto fewer providers, expand an approved-provider roster, or maintain the current multi-provider environment under modernized standards?

**Commercial & Owner Economics**

**Q4** — The RFP emphasizes "owner investment considerations," "financing and phased implementation options," and a "moderate investment model." Who is the contracting and paying party — Choice corporate, the individual franchise owner, or a blended model? This determines how we structure pricing, financing, and owner adoption.

**Q5** — Section 11 references "tiered bandwidth services, including free and paid options" and "billing and revenue capture." Under current Choice brand standards, are properties permitted to charge guests (including loyalty members) for premium tiers? And does Choice intend to participate in paid-tier revenue (e.g., revenue share), or does that economic flow to the owner and/or provider?

**Choice Systems Integration**

**Q6** — Question 11.1 references integration with Safety NetAccess for ILP authentication. Is Safety NetAccess the required authentication platform across all in-scope brands, and will Choice provide integration specifications to support our response? Are providers expected to integrate with Safety NetAccess specifically, or to deliver an equivalent capability that satisfies the ILP requirement?

**Q7** — Question 11.8 references integration with choiceADVANTAGE PMS, and the cover email references Select Networx. Will Choice provide API documentation and a technical contact for these systems, and what role is Select Networx expected to play in the awarded provider's sourcing and delivery model?

**Pricing & Response Format**

**Q8** — Question 10.1 requests total cost of ownership including monthly recurring and one-time costs. Will Choice provide a reference property profile (room count, current infrastructure, connectivity, brand) or a representative property mix? Without a reference model, TCO can't be normalized across segments.

**Q9** — Is fully developed pricing expected with the June 22 response, or is this phase focused on capabilities with detailed pricing requested at shortlist/presentation? This affects how much pricing detail we commit to in writing now.

**Pilot**

**Q10** — Questions 11.17–11.18 reference a pilot at "representative properties." Approximately how many properties, who selects them, and is the pilot owner-, brand-, or provider-funded? This shapes the pilot structure and success metrics we propose.

Two things to weigh: clarifications are due **this Friday (Jun 5)**, so there's not much runway. And the RFP came to Mark and Kathy cc Jady — you're not on it, so how these get submitted is a routing call you'll want to make before we finalize.

Want to cut, add, or sharpen any before we lock the set?
