# Preparing content for Manus AI slideware output
Date: 2026-08-13
Conversation: ffc56618-cc8f-4927-a3b4-0dab967aa7b4
Domain: business-ops

## Summary
**Conversation overview**

Scott Watts, Senior Director of Hospitality Operations at Blueprint RF (BPRF), worked with Claude to build a complete content and prompt package for a Spectrum Business sales training session. BPRF is a hospitality-focused managed Wi-Fi and LAN Service Provider serving 2,600+ hotels, recently being launched as a solution through Spectrum Business following a merger. Scott is coordinating a 120-minute virtual Session 1 training for 64 Spectrum attendees across Sales Engineering and Technical Sales Consultant (TSC) organizations. Key colleagues mentioned include Brian Napier, Marie Henson, Par Bayat, Dan Apa, Cedric, and Bayron (BPRF presenters); Bob Schroeder (Spectrum GVP, Business Technical Sales); James An (program architect); Jady, Kathy Hatala (Sr Director of Sales, Cox Hospitality Group), Cassell, Markos, and Aaron (Spectrum stakeholders). Scott Watts reports into a Sr Director level and interacts with Bob Schroeder as a GVP, which affects how communications should be framed.

Claude analyzed an uploaded working draft deck (Charter_Training_v2.pptx), searched prior conversation context, and produced two key deliverables: a detailed content pack (BPRF_Spectrum_Session1_CONTENT_PACK.md) consolidating all confirmed facts, gap analysis, mandatory corrections, and "do not include" guardrails; and a Manus AI prompt (BPRF_Spectrum_Session1_MANUS_PROMPT.md) structured for slideware generation. Critical naming rules were flagged throughout: the gateway product must be called "DG2" only (never "Dominion"), DG3 must not appear anywhere, and internal system names "Cosmos" and "CAS" must be replaced with functional labels in all external-facing material. The content pack also flagged three slides with no usable content (owned by Brian Napier, Marie Henson, and Par Bayat) and one open OEM naming question requiring SME confirmation before the deck ships.

The conversation also involved drafting three email replies to Bob Schroeder regarding session scheduling and format. Scott had not received a calendar invite and needed to nudge Bob while noting presenter availability favored Wednesday afternoon, with flexibility to push a week. When Bob's reply signaled a preference for a shorter "introductory" format, Claude drafted a reply reframing the session as 60 minutes recorded for reuse, with written cohort scoping replacing the live 30-minute block. Scott then corrected Claude's tone — the draft read as too directive for a Sr Director writing to a GVP — and requested softer, more suggestive language that preserved Bob's decision-making authority on format, timing, and logistics. The revised draft converted all recommendations into questions and kept the two-hour option explicitly available. Scott's consistent communication pattern is concise, professional, and audience-calibrated; he types informally when working with Claude but expects polished, contextually appropriate output for external audiences.

### SCOTT (2026-08-13T15:58)
see atrached email, and search everythign you have available for addtioanl context  i need you to give me any addtioanl material, content etc., and the prompt so that I cam load this into manus ai for slidware output
[File uploaded: charter se training.pdf]
[File uploaded: Charter Training v2.pptx]

### CLAUDE (2026-08-13T16:03)

I have the thread, the roster, and the v2 deck. Let me pull it together.

Two files: the prompt to paste into Manus, and the content pack to attach alongside `Charter_Training_v2.pptx` and the email PDF.

Six things worth your attention before you run it:

**The roster changes the design.** Bob's file says 64, and the split is 44 Sales Engineering (24 SEs + 9 Solutions Architects + 11 leaders) against 19 TSC. That's a 70/30 skew toward the technical bench, plus 14 people-leaders and the GVP. I built the deck spec around dual-track "what this means for you" closers on each topic block, because a TSC and a Solutions Architect need different takeaways from the same GPNS slide. Nine Solutions Architects also tells you where the depth appetite will land in the closing 30 — probably BOM/design mechanics, not brand standards.

**The v2 deck has three legal/naming violations.** Slide 11 says "Dominion" twice — once in the gateway list, once in the footnote about being one of two Marriott-approved proprietary gateways. Slide 6's architecture diagram names Cosmos and CAS outright, and this deck goes to a Spectrum audience on a thread marked [EXTERNAL]. All four are called out as mandatory corrections in §7 and as hard rules in the prompt.

**Three slides have no content at all** — approved HW by brand (Brian's), the FSR flow (Marie's), and "What does this mean for a customer?" I drafted the customer-impact slide from the EOL logic already in the deck and built the brand-HW matrix as far as confirmed fact goes (Marriott complete, Hyatt/Nomadix confirmed, four brands blank). Marie's FSR slide I left as a structural skeleton — there's nothing to build from and inventing process steps would be worse than a visible placeholder.

**One open OEM question.** The deck says Marriott-approved switches and APs are "Cisco." The course feedback you submitted to Rize specified "Cisco Meraki." Those aren't the same claim, and given the Hilton Meraki Dashboard warnings this year, it's worth Brian or Julian closing it before this ships to 64 Spectrum people.

**Two additions that don't exist in v2 and probably should.** A "where BPRF fits in your motion" swimlane — 64 people whose first question is what they own versus what you own — and the Marriott Managed routing rule as its own slide. Kathy raised that guardrail on the thread and it's the kind of thing that's cheaper to state once in a deck you authored than to correct 24 SEs on later.

**Timing.** Bob still hasn't confirmed the 18th or 19th. If it's the 18th, that's five days out. The prompt asks Manus to return the outline for your approval before building, which costs you an hour and saves a rebuild.

### SCOTT (2026-08-13T17:35)
i have not gottne and invite or anythign else from bob and james on this.  can you help with a fendly reply?  if dates are still not loched down, we would prefer wed afternoon due to presenter pto.  if they need t pus a week, we can accondoate that too

### CLAUDE (2026-08-13T17:35)

**Reply-all** on Bob's August 6 message — To: Bob, James, Jady, Kathy, Cassell; Cc: Markos, Aaron unchanged. Bob sent the roster to the group, so a group reply keeps the record showing BPRF ready and waiting rather than silent.

A few notes on the choices:

**Opening with thanks for the roster, not with the chase.** The first line is gratitude and evidence of work done, which makes the nudge read as a status update rather than a prod at a GVP. "We've built the session around it" does the quiet work of telling Bob his delay is costing your team prep time, without saying so.

**Volunteering the week push before they ask.** You're seven days from the 19th and Bob has been quiet for a week — there's a real chance the date slipped on his side and he's sitting on it. Offering the following week first removes any awkwardness in him taking it, and it costs you nothing since your team gets an extra week of build time either way. It also keeps you as the accommodating party in a thread Jady and Kathy are reading.

**"A couple of our presenters are out earlier that week"** rather than naming PTO explicitly — same information, and it doesn't invite a "can they move it" reply.

**No re-ask on anything else.** You already have headcount and role mix. Adding a second ask to a scheduling nudge dilutes it and gives Bob two things to not answer instead of one.

One timing thought: if nothing lands by end of day Friday the 14th, the 19th stops being realistic for a five-presenter session with material still in build. At that point I'd stop waiting on the thread and go direct to James — he's the program architect and the one who actually wants this launched, and a one-line "should we just target the following week?" from you to him will move faster than another group email.

### SCOTT (2026-08-13T17:48)
no.  i do not have all of these folks contacts onfo.  Bob needs to to create and sen to me to forared to the prestners on my team

### CLAUDE (2026-08-13T17:49)
Right — that changes the last line. Bob owns the distribution list; you own the outline.

Same reply-all. The change is the third paragraph.

The framing is deliberate: the reason given is that Bob's team holds the list, not that you're handing off the session. You keep the outline — which is the piece that actually sets format, sequence, and time allocation — and you're offering it *for* his invite, so it travels to all 64 attendees with your structure intact. Bob does the mechanical work of sending; you still define what the session is.

The "send it my way as well" is doing real work too. Without it you're relying on Bob remembering to include you on an invite you're presenting at, and you have no artifact to forward to Brian, Marie, Par, Dan, and Cedric.

### SCOTT (2026-08-13T20:29)
here is bob's reply.  based on the agenda james provided, we were thinking could easily use 2 hurs (as i think was already discssedu in the thread)  but if ia reaidn his tone correclty, he wants shorter?
[File uploaded: 1786651187072_image.png]

### CLAUDE (2026-08-13T20:30)
Your read is right, but the more consequential signal isn't the length — it's two other things in that message.

**"Introductory call."** James wrote "in-depth training session or workshop." Bob has quietly renamed it. That's a scope reframe, and the question about time is him asking you to justify against the smaller frame, not the bigger one.

**He's delegating his own attendance.** "I can nominate someone to facilitate and record" plus leadership out Wednesday means the GVP and much of the leadership layer may not be in the room. That matters more than the clock. Your closing 30-minute block only works if the people who can authorize cohort time are present — and if the session is being recorded for field playback, a meaningful share of the 64 are watching asynchronously anyway. You cannot run live scoping to a recording.

So fighting for two hours wins you a longer session with fewer decision-makers in it. I'd take the reframe and convert it.

**Give him the 60-minute version — and make it an asset rather than an event.** A tight, recorded, evergreen introduction across all five topics is something Spectrum can hand to every new seller for the next two years. That's more durable than a one-time two-hour workshop, and it's genuinely what "roll with it" is asking for.

**Then move the scoping from live to written.** Send the cohort menu (§6.5 in the content pack) as a short list and ask his directors and managers to mark what their teams need. You still author the series, it still comes back to you, and it now reaches the leaders who were out Wednesday. Written responses from named managers are a better record than hands raised on a call.

One caution: a recorded session is forwardable permanently. The DG2 naming rules and the Cosmos/CAS removals move from important to non-negotiable, and I'd cut the competitor certification-status line from the Marriott provider slide before anything gets captured on video.

On timing — Wednesday is now bad on their side and early that week is bad on yours. Thursday the 20th, 2:00pm ET / 11:00am PT clears both and covers the west coast.

Bob's message came to you directly, so this can go back to him alone — though I'd reply-all if you want Jady and Kathy to see that the two-hour session compressed on Spectrum's side rather than yours.

Two notes on the draft. The second paragraph names two hours before proposing sixty minutes, so the record shows you scoped the full agenda and made a deliberate call — not that you never had two hours of material. And the third paragraph asks his managers to respond in writing, which converts the scoping block you're losing into a document you control and gets it in front of the leadership layer that missed the call.

If he takes this, the deck spec changes materially: 60 minutes is roughly 18–20 slides, not 32–36. Say the word and I'll rework the Manus prompt and content pack to the shorter cut — the trims are mostly in Topic 4, which was carrying seven slides on Marriott.

### SCOTT (2026-08-13T20:33)
he's a gvp and i am a sr dir.  maybe soften it a bit amke it sound more suggesttive thatn directive

### CLAUDE (2026-08-13T20:33)

Same substance, different register. The changes:

Every recommendation is now a question he answers rather than a plan he's told about — "would a shorter format serve you better," "would Thursday the 20th work," "would it be easiest for you to send the invite." He keeps the decision on all three.

The two-hour option stays explicitly on the table ("happy either way"). That's the key softener: you're not talking a GVP out of something, you're offering him a choice and telling him which way you'd lean. If he wants the full two hours, he takes it without having to override you.

"Only if that's useful to you" on the cohort-scoping paragraph gives him a graceful decline. He almost certainly won't decline — it saves his managers time — but the exit makes the offer read as helpful rather than as you installing a process on his org.
