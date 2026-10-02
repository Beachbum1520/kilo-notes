# Project feedback on slide presentation
Date: 2026-07-17
Conversation: 1040e961-57b6-4c3f-bd99-f637697ec811
Domain: business-ops

## Summary
**Conversation overview**

Scott works at Blueprint RF (BPRF), a hospitality network services company, and was engaged in a detailed review of marketing slide content related to their DG2 gateway product. The conversation centered on reviewing three DG2-specific slides and then expanding to the full 82-slide repository deck, with the goal of preparing feedback for the broader team (sales, marketing) and then distilling that into a slide-by-slide change list ahead of a one-on-one review call with the company's marketing person.

Key decisions and facts established during the session: the product line is formally called "Dominion Gateway" with DG2 as the current generation shorthand (prior generations: DG1, DG1.5; DG3 in development but kept out of all external material). The marketing person had flagged a legal requirement that "Dominion" cannot appear in external materials — only "DG2" — so Scott did not want that rule re-explained back to the marketing person, only the slides that still violated it. LSP stands for LAN Service Provider (not "Licensed"), and the correct credential framing is "certified and approved LAN Service Provider." Internal platforms (including monitoring and back-office systems) are never to be named externally; Dan's team is building a replacement platform. DG3 is never to be mentioned in external or forwardable material.

Scott's working style preferences were clearly demonstrated throughout: he wants feedback trimmed to only what needs to change, not what's already correct; he escalates precision quickly when Claude over-explains or recaps information the recipient already knows; he communicates differently for internal teams vs. forwardable external material and is sensitive to tone (authoritative vs. collaborative). Key colleagues mentioned include Dan (software/engineering team lead, building the platform replacement), Kathy (leads a team that includes the sales/marketing distribution list), and an unnamed marketing person who is Scott's direct call partner for the deck review. The email signatory throughout is Scott. Scott corrected Claude on the LSP expansion, the product naming convention, and the appropriate audience awareness when drafting forwardable content.

**Tool knowledge**

Claude used `bash_tool` with `markitdown` to extract full slide text from uploaded PPTX files into markdown, then used `grep` with case-insensitive flags (`-in`) and pipe to `head` for targeted searches across the extracted text. Diffing between two deck versions was done via `diff deck.md deck2.md` with line-range pagination using `sed -n`. The most reliable search pattern for finding naming violations across a large deck was a single grep with pipe-separated terms: `grep -in "dominion\|preferred gateway\|Meets Brand\|BPRF Gateway\|NMS\b\|Data Mining\|As Built\|40 Gbps\|10 Gb\|DGs\b" deck2.md`. Important limitation to note: `markitdown` extracts slide text, titles, body copy, and diagram labels but does not capture text embedded inside images or screenshots — visual passes are required for image-heavy slides to catch naming violations in mockups or portal screenshots.

### SCOTT (2026-07-17T13:05)
Scan all convos, doc and anything else in this project,  then use that to provide feedback on this slide, and more to follow
[File uploaded: 1784293477540_image.png]

### CLAUDE (2026-07-17T13:06)

Got the context — including yesterday's thread on the Cox Integration training where we landed on the "DG2 where the brand allows it" framing. That matters for this slide, so I'll flag it below. Here's the critique, grouped by weight:

**Structural problems**

1. **The center circle is the weakest text on the slide.** "Fully-formed server integration for deeper analytics and a more robust guest experience" — nobody outside BPRF knows what "fully-formed server integration" means, and "deeper analytics" is promised in the hub but no spoke on the slide delivers it. The center of a hub-and-spoke should be the one-sentence answer to "what is DG2." Right now the slide never says it plainly: DG2 is a gateway. Suggested center: *"DG2: Blueprint RF's purpose-built hospitality gateway — brand-compliant, centrally managed, no licensing fees."* Or add an analytics spoke if analytics is a real claim.

2. **Your strongest competitive claim isn't on the slide.** In the Charter deck we leaned on the Dominion gateway being one of only two Marriott-approved gateways. "Meets Brand-Standards" as written sells the *GUI* ("robust GUI allows quick set-up") — that's the least persuasive version of your best point. Lead with the approval/certification fact; the GUI is a footnote.

3. **Brand-standard claim needs the Hyatt caveat — depending on audience.** Per yesterday's training thread: sellers can't walk into Hyatt pitching DG2. If this slide is going into the Cox/Spectrum training package or any generic seller-facing collateral, "Meets Brand-Standards" unqualified will create exactly the accuracy problem we just fixed in Lesson 2. If it's Marriott-specific (GRE&T proposal), it's fine as-is. Which deck is this for? That answer changes the fix.

4. **"Enhanced Security" and the Cisco ISE bullets overlap.** ISE *is* the security story. Merge them into one spoke ("Security & Access Control: Cisco ISE integration for dynamic network access control, plus centralized monitoring and threat response by Blueprint RF") and free a slot for the missing analytics point or Cosmos monitoring integration. Also verify the ISE claim — "across all network devices" is a strong absolute; is that true on every deployment or only where ISE is licensed at the property?

**Content sharpening**

5. **"No Licensing Fees" is underweighted.** Against competitor stacks carrying 3-year prepaid Aruba Central subscriptions or Nomadix license models, this is a real TCO argument. Sharpen: "No per-room, per-AP, or recurring software license fees — all software developed and maintained by Blueprint RF." That's a differentiator, not a feature.

6. **"Increased Throughput"** — "10 Gb per interface" should be **10 Gbps**, and "bonded" should be "link aggregation (LACP)" if a technical audience will see this. Minor, but a Charter or brand engineering reader will notice.

7. **"Single Source Conferencing"** — "flexible GUI that enables site access to all major conferencing features" is muddy. What's the actual claim — that conference/event bandwidth provisioning is managed natively in DG2 instead of a separate platform (11OS)? Say that. Given the open conference-platform decision, be careful this bullet doesn't promise capability that's still in the 110S replacement discovery.

8. **Header style is inconsistent.** Seven benefit headers and one product name ("Cisco Identity Services Engine (ISE)"). Make them all benefit-first.

**Mechanical**

9. Hyphen: "Brand-Standards" → "Brand Standards." Double space in "with  brand standards." "gateway/ firewall" has a stray space. "DGs" vs "DG2" — pick one naming convention (if failover is between DG2 units, say "two or more DG2s").
10. Left column runs GUI → ISE → Security → Licensing with no priority logic. Reorder both columns so the top-left and top-right positions carry the two strongest claims (brand approval, high availability or no-license TCO) — eyes hit those first.

Net read: the bones are fine, but the slide currently sells eight co-equal features and buries the two things that actually win deals — brand certification and zero licensing cost. Tell me the audience (Cox training, Marriott GRE&T, general collateral?) and send the next slides; I'll keep the feedback consistent across the set.

### SCOTT (2026-07-17T13:06)
put all that in an email i can send to the larger team to include sales and marketing

### CLAUDE (2026-07-17T13:07)

Draft's ready above. A few deliberate choices worth noting:

- **Grouped by priority** (Must Fix / Should Fix / Mechanical) same as your Cosmos deck feedback format, so the team knows what blocks external use vs. polish.
- **Kept it forwardable** — no references to specific RFPs, the Charter work, or competitor pricing comparisons. The Hyatt/Nomadix point is stated as factual platform reality, not as a training miss.
- **Item 3 asks the team to confirm audience** rather than assuming — that also puts the accuracy burden on whoever built the slide, and gates the "brand standards" claim before it ships anywhere.
- **Verification asks (ISE claim, conferencing capability)** are framed as confirm-before-external-use, consistent with not putting unvalidated claims in writing to brands or Spectrum.

If this is going to Kathy's org as part of the distribution, the tone is informing-not-asking as-is — you're setting the review gate ("I'd like to review the full deck before anything is finalized") without requiring anyone's sign-off. Send the next slides when ready.

### SCOTT (2026-07-17T13:08)
lets go ahead and incorpaote a review of the other two dg slode.s  lets hit all three in one email reply
[File uploaded: 1784293639300_image.png]
[File uploaded: 1784293661135_image.png]

### CLAUDE (2026-07-17T13:09)
Quick read before the draft: slides 1 and 2 are content-identical — the only difference is the blue vs. gray center circle. So the real review is two slides plus a duplicate to resolve. Also worth noting: the analytics slide partially answers my earlier critique — the "deeper analytics" claim from the hub slide does get supported later in the deck, so I've adjusted that feedback to a cross-reference fix rather than a cut. Here's the consolidated email:

Consolidated draft is ready above — 15 items across the set, same Must Fix / Should Fix structure so the team can triage.

Two judgment calls I made that you should sanity-check before sending:

1. **Item 12 (data-flow directionality)** — I flagged the CRM arrow for verification rather than asserting it's wrong, since I'd want Dan's team to confirm the actual sync behavior before you correct it in writing. If you already know it's bidirectional with Salesforce, tell me and I'll state it as a correction instead of a question.

2. **Item 10** — I called out the DG2/BPRF Gateway/Dominion Gateway naming inconsistency but left the "pick one" decision to the team. If you have a preference (DG2 for this deck seems right given the titles), I can make it a directive rather than an open item.

One thing I deliberately did *not* put in the email: the diagram's "Monitor Database" and "NOC Dashboard" are clearly Cosmos under the hood. Whether to name Cosmos externally is a positioning decision — naming it strengthens the proprietary-platform story (which worked in the Charter material) but also commits you to demoing it if asked. Worth deciding before the deck goes anywhere external, but verbally, not in this thread.

### SCOTT (2026-07-17T13:10)
do not want to name cosmos or CAS.  Dan and team are actively working on a replacment

### CLAUDE (2026-07-17T13:11)
Good call — and that's exactly the right reason to keep it generic. If the deck names Cosmos and Dan's replacement ships mid-lifecycle, every piece of collateral goes stale, and you've committed to demoing a platform you're actively sunsetting. I've added a platform-naming rule to the email as its own item — stated as a standing rule, without the replacement rationale, since "we're rebuilding our monitoring platform" isn't something to put in a thread going to sales and marketing.

Updated draft is ready. The platform-naming rule is now item 2, positioned as a standing rule for all external material rather than a slide-specific fix — it states the *what* (generic functional labels only) without the *why* (Dan's replacement work), so nothing in the thread signals a platform transition to sales and marketing. Item 12's diagram-label guidance now points back to that rule so the two stay consistent.

I've also noted the no-Cosmos/no-CAS rule going forward, so it'll carry into future RFP responses, decks, and collateral reviews automatically — including the Marriott GRE&T proposal, where it's worth double-checking any inherited boilerplate for platform names before submission.

### SCOTT (2026-07-17T13:13)
Do we spell out anyway that DG2  means BPRF's Dominion Gateway V2?  If not should we?

### CLAUDE (2026-07-17T13:13)
No — neither slide spells it out. The overview slide uses "DG2" cold from the title down, and the analytics slide gets closest with "DG2, our proprietary gateway," but "Dominion Gateway" never appears anywhere in the set.

And yes, it should, for a reason beyond style: your brand-approval claim depends on it. If Marriott's GPNS approved-gateway list says "Dominion Gateway" and the slide says "DG2," a brand or Charter reader can't connect the product on the slide to the name on the approval list — which weakens the single strongest claim we're telling the team to add. Standard fix: spell it out once at first use — "DG2 (Dominion Gateway 2)" or "the Dominion Gateway 2 (DG2)" — then use DG2 for the rest of the deck.

One thing to confirm before it goes in writing: is the official product name "Dominion Gateway 2," or is DG2 shorthand for the second-generation Dominion Gateway? Whatever the formal name is on datasheets and the Marriott approval documentation is what should appear in the parenthetical — those need to match exactly.

I've folded it into the email as part of item 3 (the first-introduction fix) with the verification note:

Updated — the first-use definition is now item 3 at the top of Must Fix, tied directly to the brand-approval argument so the team understands it's a claims-integrity issue, not a style nit. The suggested center-circle text in item 4 and the diagram standardization in item 12 both now flow from it, so the naming fix is consistent end-to-end.

The one open dependency in the email is the verification ask: whoever revises the slides needs to pull the exact product name from the datasheet and the Marriott approval records so the parenthetical matches verbatim. If you already know the formal name off-hand ("Dominion Gateway 2" vs. "Dominion Gateway, Gen 2" or similar), tell me and I'll hard-code it and drop the verification language — otherwise it's safer to leave the check with the team.

### SCOTT (2026-07-17T13:14)
the product name is Dominion Gateways.  We call it DG2.  there was a DG1 and a DG 1.5, and we are workign on DG3 now.  Its like our org is Blueprint RF, but wqe call in BPRF

### CLAUDE (2026-07-17T13:15)
That maps cleanly — product line is **Dominion Gateway**, and DG2 is the generation designator, same pattern as Blueprint RF/BPRF. So the parenthetical should be "the Dominion Gateway (DG2)," not "Dominion Gateway 2" — the "2" is inside the shorthand, not part of the formal name.

One deliberate omission: I'm keeping DG3 out of the email. A forwardable thread to sales and marketing that mentions a next-gen gateway in development invites sellers to hint at roadmap with customers and gives brands a reason to ask "should we wait for DG3?" Same logic as the platform-naming rule — roadmap stays out of external-adjacent writing.

Final version is ready. Item 3 now states the naming as fact — "the Dominion Gateway (DG2)," with the BPRF analogy so the convention clicks instantly for the team — and the verification ask is gone since you've confirmed it. The center-circle suggestion in item 4 uses the correct form. No mention of DG1, DG1.5, or DG3 anywhere; the generational history isn't needed to enforce the rule, and DG3 stays out of forwardable material entirely.

I've also noted the naming convention (Dominion Gateway product line, DG2 as current-gen shorthand, DG3 kept out of external material), so it carries forward into the Marriott GRE&T proposal and anything else DG-related.

That's the full set covered — two open items sit with the team after this sends: audience confirmation (which gates the brand-standards language) and the duplicate resolution. If more slides come in from this deck, send them over and I'll keep the numbering and structure consistent.

### SCOTT (2026-07-17T13:19)
I think we need to lean in to the fact that our DG is certifed and we need to call it out.  but we need to also clearly call out that BPRF is the approved providers for these major brands.  that is whaty gets us tot the table to sell, our DG and service and support is what wins the deals

### CLAUDE (2026-07-17T13:20)
That's the right hierarchy, and it's worth being explicit about it because the current slide inverts it — it sells features (what wins deals) without ever establishing credentials (what gets us in the room). The two claims do different jobs:

- **BPRF as approved provider** is a *company* credential — it answers "why are you even allowed to bid?" That arguably shouldn't live on a product slide at all; it should hit the reader before DG2 is ever introduced.
- **DG2 certification** is a *product* credential — it answers "why this gateway?" That belongs on the DG2 slide as the lead spoke.

So my recommendation to the team is two changes: restructure the "Meets Brand Standards" bullet into a certification-led claim, and add a company-credentials element ahead of it — either a dedicated "Why Blueprint RF" slide or a persistent proof line. One accuracy guardrail I'm building in: approved-provider status is brand-by-brand, so the slide should name the brands where we hold it rather than claim "all major brands" — same discipline as the Hyatt/Nomadix caveat. Updated email:

Restructured version is ready. Key changes:

- **Item 1 is now the positioning directive**, top of the email, with your exact selling logic stated as the organizing principle: approved provider gets us in the room; certified gateway plus service and support wins the deal. Every other fix now ladders under that frame, and the subject line changed to reflect that this is direction, not just cleanup.
- **The two-level split is explicit** — (a) company credential (BPRF approved-provider status, positioned before DG2 is introduced) and (b) product credential (DG2 certification as the lead bullet, with a suggested rewrite the team can lift verbatim).
- **New item 8** — since you said service and support is half of what wins, I flagged that it barely exists on the slide. The team either adds a support bullet (24/7 NOC, single point of accountability as the LSP) or confirms a dedicated support slide lives elsewhere in the deck.
- **I gave the team a decision to bring back** — credentials slide vs. proof line — rather than dictating the mechanism. Keeps them owning the design work while you own the positioning.

Two accuracy guardrails baked in that protect the claims: brands are to be named specifically where we hold approved status (no "all major brands" generalization), and the certification language stays subject to the audience confirmation in item 6 — because "brand-certified" said unqualified in Hyatt-facing material creates the same problem the training thread just fixed.

### SCOTT (2026-07-17T13:26)
here's the entire slide deck. take a look at it before i hit send.  my task is not toe review the entire thing, but lets make sure my claims about needing a why brof sliode is not already here.  i scanned and did niot see it
[File uploaded: BPRF_Slide_Repository__Last_Update_-_07_16_2026_.pptx]

### CLAUDE (2026-07-17T13:28)

Good instinct to check — here's what's actually in there. The deck is 82 slides; short answer: **your claim holds, but needs one precision fix before you send, and I found something bigger while I was in there.**

**On the "Why BPRF" question:** The deck *does* have company-intro slides — 9 ("Our Customers" logo wall, 2,700+ hotels / 367,000+ rooms), 10–11 ("Blueprint RF"), 12 ("Who We Serve"), 13 ("Who We Are"), plus a literal "Why Blueprint RF" bullet buried in the footer of slide 63. So if the email says "our credentials story is missing," someone will reply "slides 9–13." But here's what validates your point: **the approved-provider credential appears nowhere in all 82 slides.** The strongest language slide 13 musters is "trusted by major hotel brands." The only "approved partner" claim in the entire deck is on slide 77 — and it credits *Phonesuite* as the "trusted and approved Marriott partner," not BPRF. GPNS appears exactly once, in a Marriott future-state appendix slide. So the intro slides establish scale and footprint but never the qualifying credential. I've reworded item 1(a) to say exactly that — sharpens the ask and preempts the pushback.

**The bigger find — there's a third DG2 slide, and it contradicts the ones you reviewed.** Slide 34, "DG2: Our Upgraded WiFi Network Server," claims **40 Gbps per interface**; slides 35/36 say **10 Gb per interface**. That's a 4x discrepancy inside the same section, and slide 34 also calls DG2 a "WiFi Network Server" while 37 calls it a "proprietary gateway" — a third product descriptor. Slide 33 adds a fourth: "DG2 – preferred gateway" (soft language that undercuts the certification story). Any technical reviewer who reads the section in sequence catches the throughput conflict immediately.

**Two more worth a line each since you'll be in the thread anyway:**
- **Slide 9 vs. 12 conflict:** 2,700+ hotels / 367,000+ rooms vs. 2,300 hotels / 315,400 rooms. Same repository, contradictory footprint stats — one is stale.
- **Slide 62 (Vendor Differentiation) contains Omni-specific text** — "single-source service provider for *Omni's* network needs" — sitting in the general repository, plus references to SolutionInc and the ElevenOS partnership. If someone reuses that slide for Marriott or Hilton without catching it, Omni's name ships in a competitor brand's deck.

Updated email:

Updated email is ready — now grounded in the actual repository with slide numbers throughout. Key changes from the version you were about to send:

1. **Item 1(a) is now bulletproof.** Instead of "our credentials story is missing" (refutable by pointing at slides 9–13), it acknowledges those slides exist, quotes the strongest language the deck actually has ("trusted by major hotel brands"), and lands the Phonesuite finding — the only "approved partner" claim in 82 slides credits Phonesuite, not BPRF. Nobody can push back on that.

2. **The slide 34 contradictions are now a blocking section** — the 40 Gbps vs. 10 Gb conflict and the four different product descriptors (WiFi Network Server / gateway / preferred gateway / undefined). I dropped the earlier "should read 10 Gbps" fix since we don't actually know which number is right — that's now an engineering confirmation, not a copyedit.

3. **Repository-wide finds added:** the 2,700/367K vs. 2,300/315K stat conflict, and the Omni-specific text sitting in the general-use Vendor Differentiation slide.

4. **Audience question resolved** — since this is the repository, item 9 now directs the caveated version as the master, with brand-specific decks free to simplify. The "confirm the audience" ask is gone.

5. **Item 11 got better** — the deck actually has strong support content (slides 57–63, including real SLA numbers: 92% service level, <30s answer). The fix is now bridging the DG2 slides to it rather than creating support content from scratch.

One judgment call to flag: the closer names items 2, 5, and 6 as blocking for external use. That's a defensible position for a repository last updated yesterday, but it does put a hold on slides sales may already be pulling. If that's heavier than you want on a first send to Kathy's org, I can soften "blocking" to "prioritize first."

### SCOTT (2026-07-17T13:41)
thsi is good.  but lets soften this last sentence a bit to lees athorative

### SCOTT (2026-07-17T13:41)
thsi is good. but lets soften this last sentence a bit to lees athorative

For item 1(a), bring me a recommendation on where the approved-provider credential lands (existing intro slides vs. dedicated credentials slide) before the next draft. Items 2, 5, and 6 are blocking — the throughput conflict, stat conflict, and customer-specific content need resolution before any of these slides go external. I'd like to review the updated set before anything is finalized.

### CLAUDE (2026-07-17T13:42)

Done — the closer now reads:

*"On item 1(a), I'd welcome the team's thoughts on where the approved-provider credential fits best — the existing intro slides or a dedicated credentials slide. I'd also suggest we prioritize items 2, 5, and 6 (the throughput conflict, footprint stats, and customer-specific content) since those are the ones most likely to cause issues if the slides get pulled for external use in the meantime. Happy to take a look at the updated set whenever it's ready."*

Three shifts: "bring me a recommendation" → "I'd welcome the team's thoughts," "blocking" → "prioritize... most likely to cause issues," and "I'd like to review before anything is finalized" → "happy to take a look whenever it's ready." Same substance and same review touchpoint, but it reads as collaborative guidance rather than a gate — better fit for a thread that includes Kathy's org. Everything else is untouched. Ready to send.

### SCOTT (2026-07-17T15:36)
marketing guy wants to do a call to reivew with me.  give me the slide by slide changes, so I can sned ot him in advance of this call

### CLAUDE (2026-07-17T15:36)

Ready above — the 21 items reorganized into a walk-the-deck format: four deck-wide rules up top (naming convention, certified-over-preferred, internal-platform rule, and your selling logic), then 22 numbered changes in slide order from 9 through 62. Everything with suggested language is lift-ready, so the call can be decisions rather than wordsmithing.

Two things structured deliberately for the call itself:

- **Item 1 is framed as the discussion item** — credential placement (intro slides vs. dedicated slide) is the one genuinely open design question, so it's flagged as the thing to decide together rather than a directive. That gives the marketing guy something to own on the call.
- **The closer suggests a call agenda** — credential placement, throughput conflict, and the Omni text first — so the 30 minutes goes to the three items that need decisions or engineering input, not the mechanical fixes he can just execute.

One prep note for you, not the email: before the call, it's worth knowing the answer to item 4 yourself. If you can get the DG2 interface spec confirmed (40 vs. 10 Gbps) from Dan's team or engineering beforehand, you resolve the biggest factual conflict live on the call instead of leaving it as homework.

### SCOTT (2026-07-17T15:44)
search all chats in this project, and then try again.  the feedack you will see from leagl about DG2 came form marketing,

### CLAUDE (2026-07-17T15:45)

Corrected version is ready. What changed:

1. **Rule A is now the legal mandate** — DG2 only, no "Dominion" anywhere, with the practical fix for first use: define it functionally ("DG2, Blueprint RF's proprietary hospitality gateway") instead of expanding a name we can't print. All the suggested slide language in items 7 and 8 is rewritten to comply.

2. **New item 22 — slides 40–41 contain "Dominion Dashboard,"** an active trademark violation in the current repository. It's flagged as legal, positioned first in the call priority, with drop-in replacement text ("Our legacy dashboard laid the groundwork…") so it can be fixed same-day. Since marketing is the one who relayed the legal ruling, handing them a live violation they missed in their own repository also lands well going into this call.

3. **Dropped the old rationale** that tied naming to approval documentation ("brand approval docs reference the Dominion Gateway by name") — that argument is dead under the ruling. The certification claim in item 8 now stands on GPNS approval directly. One thing to verify before or on the call: how Marriott's GPNS documentation actually lists the product now — if their paperwork says "Dominion Gateway," someone should confirm with Legal how we reference our own product's certification without using the prohibited name. That's a real edge case worth two minutes with the marketing guy.

The trademark rule was already in my notes from your earlier conversation and I failed to apply it to the last two drafts — that one's on me, and it's corrected throughout now.

### SCOTT (2026-07-17T15:47)
again,  he is the one that told me about the legal requriemt for DG2.  so not sure why we need to speel it out to him again

### CLAUDE (2026-07-17T15:48)
Fair — spelling out his own rule back to him reads like I'm briefing him on something he taught us. The useful part isn't the rule, it's that his repository still has two slides violating it. Reframed: Rule A now just references the guidance as his ("per the Legal guidance you flagged") and moves straight to application, and item 22 simply points at slides 40–41 as instances that still need the scrub.

Done. Rule A now opens with "consistent with the Legal guidance you flagged" — crediting him as the source and moving straight to the application question (how to define DG2 at first use, descriptor standardization). Item 22 is a "heads up" that slides 40–41 still carry "Dominion Dashboard" — flagging the miss without any weight on it, replacement text included so it's a two-minute fix. And it's dropped out of the priority framing at the bottom since it doesn't need call time, just a text swap.

Reads as a peer helping him enforce his own rule now. Ready to send.

### SCOTT (2026-07-17T15:49)
for ruke a.  why dont you tell me everywehere itneh deck this needs to be changed.  you have seen the entire deck.  your attention to detiual here is better than mine

### CLAUDE (2026-07-17T15:50)

Done. Rule A is now the complete inventory from all 82 slides, split into "already compliant" and "needs change" with exact slide numbers and the exact strings to swap — so the marketing guy can execute the naming pass without opening the email a second time.

The scan also produced two things worth having:

1. **Slide 19 is the model.** It already says "DG2 — Proprietary gateway, completely customizable" — the exact right language, and it's the *first* substantive DG2 mention in the deck. So the fix isn't inventing new phrasing; it's propagating slide 19's language through the product section. That's an easier sell on the call ("your slide 19 already has it right") than "rewrite everything."

2. **Verified the negative space.** The generic "gateway" uses (slides 39, 42, 62, 63 — "gateway performance," "gateway-agnostic model") are explicitly cleared as no-change, so nobody over-corrects and starts mangling category language that's fine as-is.

One caveat for the call, not the email: my scan covers slide *text* — titles, body, diagram labels, speaker notes. If any "Dominion" or old naming lives inside embedded images or screenshots (the portal screenshots on slide 42 would be the likely spot), text extraction won't catch it. Worth the marketing guy doing a visual pass on image-heavy slides as part of the scrub.

### SCOTT (2026-07-17T15:54)
for rule a, why are you giving all the shot that is right.  just give me what he needs to change.  that's all he wants me to tell him is what slides need to be changed, and what changes to make.  for all the rukles, steps, feedback, etc.

### CLAUDE (2026-07-17T15:55)

Stripped to a pure change list — every item is now "current text → new text" or a single-sentence instruction. Cut: the compliant inventory, the sequencing note, the selling-logic rule (that's call conversation, not an edit), and all the why-this-matters rationale. Rules are down to three one-liners. The only remaining explanation anywhere is the one-line closer separating decision items (1, 4, 23) from direct edits, so he knows what to prep for versus what to just execute.

Roughly half the length of the previous version. Ready to send.

### SCOTT (2026-07-17T17:30)
looks like we may not be workign off the latest version of the deck.  see attched and gice it another go
[File uploaded: BPRF_Slide_Repository__Last_Update_-_07_17_2026_.pptx]

### CLAUDE (2026-07-17T17:31)

New email is ready — down from 23 items to 10, all verified against the 7/17 file with updated slide numbers. Structure: opens by crediting the fast turnaround (he clearly worked from your email, so acknowledging it costs nothing and buys goodwill for the punch list), then splits cleanly into quick edits vs. the three items needing decisions (brand designations beyond Marriott, the 40 Gbps engineering confirm, CRM arrow directionality).

The three things worth knowing going into the call:

1. **Item 6 is the one to make sure lands** — "the support model that wins the deal" on slide 32 is your internal framing language sitting in customer-facing copy. It's a ten-second fix, but if it ships, a brand reader sees the sales scaffolding.
2. **Item 2 reframes the credential discussion.** He already added the Marriott LSP line, so the call question shifts from "add it" to "can we name more brands, and does it deserve better placement than a trailing sentence." If Hilton, Choice, or Wyndham have formal designations we can cite, that's the strongest version of the intro slides.
3. **The throughput conflict likely resolved itself** — 40 Gbps bonded vs. 10 Gbps per interface is internally consistent math (4×10G LACP). One confirm from engineering closes it, so it's no longer a blocker, just a checkbox.

Same caveat as before: text extraction doesn't see inside images, so the new captive-portal mockups (slide 38) and icon-heavy installation slides are worth a visual pass for stray old naming.

### SCOTT (2026-07-17T17:39)
LSP is lan service proivider.  not licened.  and i thin we shouls conside saying certifed and approved

### CLAUDE (2026-07-17T17:39)

Updated. The LSP correction is now item 1, elevated to a deck-wide priority fix with all three instances located (slides 10, 12, and 32) — and the "certified and approved" upgrade is folded into the same fix so it's one edit, not two passes. Item 7's replacement text now shows the bullet with both fixes applied, so he can copy the final sentence directly.

One note on the "certified and approved" phrasing for the call: it's the right construction for Marriott, where both are true. If item 3's discussion opens the door to naming other brands, hold each one to the same test — only pair "certified and" with brands where a formal certification actually exists, otherwise "approved" alone. That keeps the whole credential line audit-proof if a brand ever asks us to substantiate it.
