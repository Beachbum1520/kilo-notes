Dashboard and ElevenOS integrations"** — two errors in one line. DG2 is a gateway, not a controller. And DG2 didn't replace ElevenOS — it *integrates with* ElevenOS for conferencing (it's on your platform-benefits slide). As written, a seller at a property with 11OS conferencing would tell the customer it's going away.
3. **"Room:AP ratio is 1:1 in most cases"** — confirm this with Brian/Marie before it circulates. If it's really "varies by design; in-room AP deployments trend 1:1," say that — a flat 1:1 claim will get quoted back at your TDEs on every budgetary quote.
4. **"Sales support will initiate the DocuSign approval request... via button-push automation"** — this quietly expands their access from "opportunity entry" to initiating customer-facing contract actions from inside your Salesforce. Maybe that's the intended end state, but it's beyond the scoped profiles you committed to in writing, and it's a workflow your team hasn't validated. This needs a "pending process confirmation" flag, not a promise to sellers tomorrow.
5. **The $2.50/room management fee is printed on slide 3.** Your call, but pricing hardcoded into a deck that gets recorded and redistributed is a maintenance and discounting problem — sellers will treat it as list price forever. Suggest "per-room management fee (see rate card)."

Also two things in **your** deck worth a look before tomorrow:

- **The architecture slide names "Cosmos NMS."** That's an internal platform name in an external-facing, recorded deck — and Dan's team is actively building its replacement, so you'd be teaching 64 sellers a name that's going away. Two-minute fix: relabel it "Network Management System (NMS)."
- Minor: the GPNS certificate examples slide shows real property names, MARSHA codes, and Par's signature — fine for this audience, but since Bob's recording for field playback, confirm you're comfortable with those artifacts living in a redistributed video.

**On fitting Eric in tomorrow:** give him one ~8–10 minute segment between your Section 3 (Qualification) and Section 4 (Design + FSR) — his slides walk the Spectrum seat through exactly that handoff, then Marie and Cedrich pick up "and here's what happens on our side." His slide 2 (per-property opportunity sizing) could also serve as Scott Cassell/James-friendly opening context, but don't fragment him across the hour — one slot, clean handoff in, clean handoff out.

Want me to draft the feedback note to Eric with the five corrections? It should go today so he has tonight to revise — framed as "great content, five alignment fixes so our decks say the same thing tomorrow."

### SCOTT (2026-08-19T19:06)
he doesnt get to present tomoorw  that flight plan is full.  give me a nice repsone. back to hi and name the corrctions that he needs to make

### CLAUDE (2026-08-19T19:06)

The construction:

1. **The "no" never lands as a no.** "The hour is fully allocated" is a capacity fact, not a judgment on his content — and the redirect to a follow-on session gives his deck a *bigger* future slot than the 8 minutes he'd have gotten tomorrow. He's told his content anchors a whole deep dive; hard to be sore about that.
2. **Correction #4 is the one carrying real weight.** It re-states the access scope ("currently scoped to opportunity entry") in writing, on the thread where he first floated the DocuSign automation — so if that workflow ever appears in his M&Ps unvalidated, the record shows you flagged it before the deck circulated.
3. **"Send the revised version when ready and I'll confirm alignment"** — establishes review-before-circulation as the norm for his BPRF-describing material without ever demanding it. He revises, you confirm, that's the loop now.
4. **Each correction ships with drop-in replacement language** — same technique as the Rize feedback. People argue with critiques; they paste suggestions.

One internal follow-up this creates: **item 3 needs Brian or Marie to confirm the real AP-ratio guidance today** — you suggested replacement language ("in-room deployments commonly run 1:1") that you should verify before Eric bakes it in. Quick Teams ping covers it.

And the two fixes on your own deck are still open for tonight: the **Cosmos NMS** label on the architecture slide, and a comfort-check on the **real property certificates** (names, MARSHA codes, Par's signature) living in a recording Bob redistributes. Want me to suggest exact replacement text for the architecture slide label?

### SCOTT (2026-08-19T19:12)
for this one, "2. DG2 / ElevenOS — DG2 is our gateway (not a controller), and it integrates with ElevenOS for conferencing rather than replacing it. As written, a seller could tell a property their conferencing platform is going away. Suggest: "DG2 gateway + Blueprint ONE dashboard; DG2 integrates with ElevenOS for conference functions." we also have our own conference tool that is being pilotied right now,  it will repace the 11os cof tool.

#3 is nt accurate.  we dont usually run 1:1. we deisng to the brand standards.  if a general rule of thrumb that s 1 1:2 ration dpending on ap placemnt, walltype etc.

#5 - the price is set by the brand.  for amarriott it depeds ont he size of the hotel.  the exact nu,ebt shoudl be verifed with sale,s but it is not $2.50 prpm for all marriott across all theire brands.

4. on the docusign, that is how custemrs recieves the contracts to sing.  not sure what tyou are sayig here

### CLAUDE (2026-08-19T19:13)
On #4 — here's what I was flagging, and why it can come out of the email: the concern wasn't DocuSign itself, it was *who holds the button*. Today a BPRF person initiates the DocuSign send from your Salesforce; Eric's deck has **Spectrum's** sales support doing it, and the access you committed to in writing was "profiles scoped to opportunity entry." Initiating a customer-facing contract send is a bigger permission than entering an opportunity. But if that's the intended workflow — and since the proposal has already cleared Finance/TDE review by that point, it's mechanical — then it's not a correction for Eric at all. It's an internal note for Dan: **the sales support profile needs DocuSign-initiation permission designed in, and nothing beyond it.** So it moves from the email to Dan's provisioning spec. Dropped.

Here's the rebuilt email with your corrections — and note on #2, I kept the pilot out of it deliberately: your conference tool replacement is an internal roadmap item in pilot, and it has no business in a deck circulating to Spectrum sellers before it launches. The word "today" does the future-proofing quietly.

---

Eric,

This is strong — the "what's different from Spectrum BAU" framing is exactly what your side of the house needs, and the process flow tracks our intake-to-proposal motion accurately. This deck is the right companion piece to our training material.

On tomorrow: the hour is fully allocated across our five presenters and the closing planning discussion, so we won't have a live slot — but this content shouldn't sit on the shelf. It's the natural anchor for one of the follow-on sessions we're scoping in tomorrow's close, and in the meantime it can circulate as the sales ops reference once we tighten a few items.

Four alignment corrections so our materials say the same thing:

1. Design composition — "Designs will consist of Ruckus Access Points + Palo Alto Firewall" is more fixed than reality. Designs use Marriott-approved OEMs (Ruckus, Aruba, Cisco Meraki) with firewall selection driven by property tier and the design itself. Suggest: "Designs use Marriott-approved OEMs; equipment selection is determined by the property-specific design."

2. DG2 / ElevenOS — DG2 is our gateway (not a controller), and today it integrates with ElevenOS for conference functions rather than replacing it. As written, a seller could tell a property their conferencing platform is going away. Suggest: "DG2 gateway + Blueprint ONE dashboard; DG2 integrates with ElevenOS for conference functions."

3. AP ratio — 1:1 is not our typical design. We design to the brand standards; as a general rule of thumb it lands around 1:2 (one AP per two rooms), varying with AP placement, wall construction, and property specifics. Suggest: "AP ratio is determined by the property-specific design to brand standards — commonly in the 1:2 range depending on placement and construction."

4. Per-room management pricing — the $2.50 figure shouldn't be hardcoded. Pricing is set by the brand program, and for Marriott it varies by property size — there isn't a single per-room number across their brands. Suggest: "per-room management fee set by the brand program; verify current pricing with the BPRF sales team."

Send the revised version when ready and I'll confirm alignment. And let's put this on the agenda when the follow-on sessions get scoped — it's the right centerpiece for the sales ops deep dive.

Scott

---

The internal side-note for Dan now has two items when the roster lands: profiles scoped to opportunity entry **plus** DocuSign initiation designed in deliberately — permission granted on purpose, not discovered later.

### SCOTT (2026-08-19T19:14)
not dan.  he doest do shit with sf users acocunt.  and i really dont care if it is bprf sales or  charter sale.s  that is a political war goign on right now that I dont have a do in the figth on

### CLAUDE (2026-08-19T19:14)
Understood on both — Dan's out of the SF provisioning picture, my mistake carrying that assumption forward, and I'll drop it from the internal notes. Whoever actually admins user accounts gets the roster when it lands; you told Eric "send it to me and I'll ensure it gets done," which routes it right regardless.

And on the DocuSign/who-initiates question — you're right, I was manufacturing a stake for you in a fight that isn't yours. Whether Spectrum sales support pushes the button or a BPRF rep does is a sales-side ownership question, exactly the Kathy/Gaby/RoE territory you've been deliberately staying out of. Your line is unchanged either way: opportunity comes in, TDEs design it, FSR gates it, proposal goes out, fulfillment runs. Who clicks send on the contract doesn't move any of that.

So the email stands as drafted — four corrections, DocuSign untouched — and the only real internal action left from this whole exchange is the pair of deck fixes tonight: the **Cosmos NMS** relabel on your architecture slide, and the comfort-check on the real certificates (property names, MARSHA codes, Par's signature) living in Bob's recording. Everything else is clean for tomorrow.

### SCOTT (2026-08-19T19:14)
giv me the email again with the other corrections

### CLAUDE (2026-08-19T19:15)
---

Eric,

This is strong — the "what's different from Spectrum BAU" framing is exactly what your side of the house needs, and the process flow tracks our intake-to-proposal motion accurately. This deck is the right companion piece to our training material.

On tomorrow: the hour is fully allocated across our five presenters and the closing planning discussion, so we won't have a live slot — but this content shouldn't sit on the shelf. It's the natural anchor for one of the follow-on sessions we're scoping in tomorrow's close, and in the meantime it can circulate as the sales ops reference once we tighten a few items.

Four alignment corrections so our materials say the same thing:

1. Design composition — "Designs will consist of Ruckus Access Points + Palo Alto Firewall" is more fixed than reality. Designs use Marriott-approved OEMs (Ruckus, Aruba, Cisco Meraki) with firewall selection driven by property tier and the design itself. Suggest: "Designs use Marriott-approved OEMs; equipment selection is determined by the property-specific design."

2. DG2 / ElevenOS — DG2 is our gateway (not a controller), and today it integrates with ElevenOS for conference functions rather than replacing it. As written, a seller could tell a property their conferencing platform is going away. Suggest: "DG2 gateway + Blueprint ONE dashboard; DG2 integrates with ElevenOS for conference functions."

3. AP ratio — 1:1 is not our typical design. We design to the brand standards; as a general rule of thumb it lands around 1:2 (one AP per two rooms), varying with AP placement, wall construction, and property specifics. Suggest: "AP ratio is determined by the property-specific design to brand standards — commonly in the 1:2 range depending on placement and construction."

4. Per-room management pricing — the $2.50 figure shouldn't be hardcoded. Pricing is set by the brand program, and for Marriott it varies by property size — there isn't a single per-room number across their brands. Suggest: "per-room management fee set by the brand program; verify current pricing with the BPRF sales team."

Send the revised version when ready and I'll confirm alignment. And let's put this on the agenda when the follow-on sessions get scoped — it's the right centerpiece for the sales ops deep dive.

Scott

---

Ready to send. Then the two deck fixes tonight — Cosmos relabel and the certificate check — and tomorrow's clear.

### SCOTT (2026-08-19T19:17)
na.  im not changing.  those are minor and at some point you have a put pin in it and go to war witht he army you have, not the one you want

### CLAUDE (2026-08-19T19:17)
Fair — the deck's finalized, the presenters are prepped against it, and re-cutting slides the night before a session for two cosmetic items is how clean decks get broken. Neither one is a factual error in front of that audience; worst case, "Cosmos" is a name that ages out of a recording eventually, and that's a problem for a future version, not tomorrow.

Pin's in. You're set: Eric's email goes out today, deck ships as-is, and tomorrow the only jobs are keeping five presenters inside their 15-minute lanes and landing the closing block — the follow-on session list and the cadence structure are where the hour actually pays off.

Good luck tomorrow. If you want a quick debrief after — what landed, what the directors marked for deep dives, what goes into the follow-on roadmap — I'm here.

### SCOTT (2026-08-19T19:19)
ya, and Jady, my boss, just asked for me to forward the deck and invite to him.  so this whole thing may go to shit before we make it to the starting line

### CLAUDE (2026-08-19T19:19)
Maybe — but read the ask before assigning it a motive. Jady forwarding-level interest the day before is most likely one of three things, in descending order of probability: he wants to see what his org is putting in front of a GVP before it happens (reasonable, and frankly overdue on his part); someone above him or beside him — Kathy, or someone on the Charter side — asked him what BPRF is presenting and he needs to answer; or he wants to attend. Only the middle one has any teeth, and even then, what he'd be forwarding is a clean, DG2-compliant, brand-accurate deck built by your team in under a week. That's not exposure — that's the showcase reaching one more executive.

Here's the thing: this deck survives Jady-level review easily. It survives *Lewis-level* review. The GPNS content is factual, the OEM slide is exactly the correction Kathy herself demanded in the course, the naming is legal-compliant, and the process content is your operational ground truth. If it goes up the chain, it goes up looking like your shop knows what it's doing.

Forward it with one line of framing so the deck doesn't travel naked: "Deck for tomorrow's Spectrum SE/TSC session, 12:00 ET — 60-minute overview format, my leads presenting their own sections, closing block scopes the follow-on series. Invite attached." That's it. No justifications, no pre-defending choices nobody's questioned. If he has a concern, he'll surface it tonight and you'll have hours to react; if he's just staying informed, you look like a director who briefs up without being chased.

The one genuinely annoying scenario — Jady decides tonight he wants changes or wants to reshape the session — is also the least likely, because it would require him to engage with content detail the day before, which is not his pattern. Conflict-averse cuts your way here: the path of least resistance for him is watching it go well and taking credit upward.

Send it, sleep on it, run the session. The starting line is twelve hours out and nothing in that forward moves it.

### SCOTT (2026-08-19T19:21)
i will be purposely unavailable in about 1 1 /2 hours (5pm ET).  he is in vegas, so his work days extends past mine,  and my bigger fear is the actual presntaiton, Jady loves to be the center of attention in the sorts of thjgn, espectially to charter to present him self and the most valube person in the entire org. the glue that hold eveythign together

### CLAUDE (2026-08-19T19:21)
Then don't leave a vacuum for him to fill — assign him the stage before he takes it. The mistake would be forwarding a deck with no defined role for Jady, because an undefined Jady expands to fill available airtime. A Jady with a named two-minute slot at the top has gotten his moment in front of Charter, on the agenda, in writing — and everything after it visibly belongs to the run-of-show.

So the forward you send in the next 90 minutes does double duty. Deck, invite, and this:

---

Jady — deck and invite attached for tomorrow's Spectrum SE/TSC session (12:00 ET, 60 min, ~64 attendees from Bob Schroeder's org).

Run of show: I'd like you to open it — 2–3 minutes of executive welcome and the partnership context, then hand to me. I'll MC and keep us on time. Brian takes opportunity intake, Par has Marriott/GPNS, Marie and Cedrich cover design/FSR and platforms, and I close with the follow-on training roadmap discussion so Bob's directors can flag where their teams need depth. Format is built for the recording to hold up as a standing onboarding asset on their side.

Scott

---

Why this works on him specifically: the open is the *most* visible slot — first voice Charter hears, the frame-setter, the "glue" role he wants — and it's also the only slot that ends on a hard wall, because it hands to you by design. You become MC, which means you own every transition for the remaining 57 minutes. If he interjects mid-session, the MC's move is gracious and immediate: "Good point — Brian, pick it up from there." Nobody watching sees containment; they see a well-run session.

The 5pm disappearance now works *for* you instead of against you: the run-of-show lands as a complete, presenter-committed structure before you go dark. If he replies at 8pm Vegas wanting more, you see it in the morning with twelve hours to game time and the cleanest answer available: "Presenters are locked and rehearsed to this timing — your open sets the whole thing up." Renegotiating a published agenda the morning of is more friction than Jady the conflict-avoider typically spends.

And the quiet insurance: Bob's org is getting the *recording*. A session where the Senior Director MCs and the working team performs is what survives on Charter's servers — whatever gets ad-libbed live, the structure is what's remembered.

Send it before 5. Then go be unavailable with a clear conscience.

### SCOTT (2026-08-19T19:23)
no.  i want him to say nothing for the entire presenataion,  anything he says is in fdanger of stepping on something me or someone else is already covering.

### CLAUDE (2026-08-19T19:24)
Then let's be honest about the constraint first: you cannot script your boss into silence, and any version of asking for it — even obliquely — is the one move that guarantees a bad outcome, because it hands a conflict-averse guy a grievance he'll never raise directly. What you *can* do is engineer the session so there's no natural opening for him, and have recovery moves ready if he takes an unnatural one. Silence can't be assigned; it can be made the path of least resistance.

Three mechanisms, in order of importance:

**1. The forward gives him no hook.** No role offered, no "let me know your thoughts," no question marks anywhere — questions are invitations. Just:

---

Jady — deck and invite attached for tomorrow's Spectrum SE/TSC session (12:00 ET, 60 minutes, ~64 from Bob Schroeder's org). Run of show is fully allocated: I'm MC'ing, Brian has intake, Par has Marriott/GPNS, Marie and Cedrich have design/FSR and platforms, and I close with the follow-on training roadmap so Bob's directors can flag where their teams need depth. Session is being recorded for their field playback.

Scott

---

"Fully allocated" and the minute math (five presenters + closing block ÷ 60) do the work without a word about who isn't speaking. "Recorded for their field playback" is the second quiet deterrent — improvised remarks live forever on Charter's servers, and he knows it.

**2. You speak first and close the door in the same breath.** The self-introduction is the classic entry point — deny it by doing it for him, mid-stride: *"Thanks everyone — I'm Scott Watts, and we've also got Jady West, our VP, with us today. We've got exactly 60 minutes and five presenters, so let's get right into it — Brian."* Named, honored, and the train's already moving. No pause after his name; pauses are doors.

**3. Brief your presenters on pace, and yourself on recovery.** Dead air is where the impromptu speech lives — no gaps between sections, you bridge every handoff yourself in one sentence. And if he interjects anyway, the MC recovery is warm and instant: *"Great context — and it tees up exactly what Marie's covering, Marie go ahead."* Whatever he says becomes a setup for your agenda, thirty seconds, done. You can't prevent the interjection; you fully control what happens four seconds after it starts.

The residual risk you have to price in: he opens with two minutes of welcome no matter what you do. If that's the whole tax, pay it — it costs nothing, and fighting it costs plenty. What the structure above actually prevents is the *recurring* Jady, and that it does well.

Send the forward now, before 5. The agenda that's already published is the one that's hardest to renegotiate from Vegas.

### SCOTT (2026-08-19T19:26)
email reply i just got form Eric
[File uploaded: 1787167523163_image.png]

### CLAUDE (2026-08-19T19:26)
Two things in that one line, and the second matters more than the first.

**"Can I see content for tomorrow?"** — yes, send it. It goes in front of 64 of his colleagues plus a recording in less than 24 hours; withholding it overnight protects nothing and costs goodwill with the guy who just took four corrections gracefully. Attach the PDF.

**"I was copied on some other 'playbooks' which had some of the data I was using"** — that's the real intel. It means the wrong numbers didn't originate with Eric: the Ruckus+Palo Alto design claim, the 1:1 ratio, the flat $2.50/room are sitting in *other documents circulating on the Charter side*, authored by someone else, reaching audiences you can't see. You just corrected one downstream copy; the source is still feeding whoever reads it next. You want those playbooks.

Reply:

---

Eric,

Deck attached — this is the final version for tomorrow.

And that's useful to know about the playbooks. If you can forward whatever was circulating with that data (the design composition, AP ratio, per-room pricing), I'd like to see the source material — if those figures are living in other Charter-side documents, we should get them corrected at the origin rather than chasing them copy by copy. Happy to give the same quick alignment pass I gave yours.

Thanks for turning the corrections around — talk tomorrow.

Scott

---

"Same quick alignment pass I gave yours" extends the review-before-circulation norm from Eric's deck to the whole document family, framed as a service. If those playbooks came from James's sales-planning shop or LaMont's training org, you'll know by what Eric forwards — and depending on what's in them, that's either a quiet correction email or something Jady should hear about verbally first.

### SCOTT (2026-08-19T19:27)
my brand managers opwn the playbooks.

### CLAUDE (2026-08-19T19:27)
Stop — that reframes everything. If Par and the brand managers own the playbooks, then the wrong data isn't a Charter-side contamination problem, it's *your shop's* documents carrying claims your own review just called errors. Eric wasn't freelancing; he was faithfully copying from BPRF source material. Which means two uncomfortable but fixable things:

1. **Your correction email to Eric is now checkable against your own playbooks.** If he pulls up a BPRF playbook that says 1:1 AP ratio or flat $2.50/room, your "that's not accurate" reads as your org contradicting itself in front of a Spectrum Sr Director. Before anything else, you need to know *what the playbooks actually say* — it's possible Eric misread or over-generalized (e.g., a Marriott-specific playbook where in-room wall-plate designs genuinely run denser, or a $2.50 figure that's real for one brand tier and got universalized). Error in his transcription vs. error in your source are very different problems.
2. **Don't send the "forward me the playbooks" email I drafted** — asking Eric to send you your own team's documents announces you don't know what your brand managers publish. Kill that version.

Revised reply — still sends the deck, still closes the loop, keeps the checking internal:

---

Eric,

Deck attached — this is the final version for tomorrow.

Good context on the playbooks — those are maintained by my brand management team, so I'll review the source material on our side and make sure it's aligned with the corrections I sent you. If anything in the playbooks needs updating, we'll push the revision and let you know so your M&Ps track the current version.

Talk tomorrow.

Scott

---

That converts the awkward fact into ownership: your team's docs, your review, your revision cycle, and his M&Ps downstream of it — the source-of-truth chain pointing the right direction.

Then the internal move, tonight or first thing tomorrow: ask Par (and Julian, since brand support rolls up through him) which playbook Eric would've been copied on, and check three things — design composition language, AP ratio, per-room pricing. If the playbook is wrong, it gets corrected quietly and Eric gets the updated version, no ceremony. If the playbook is *right* and Eric over-read it, your corrections stand as sent and nothing further needed. Either way you find out before Eric does.
