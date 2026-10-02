# charter ramp up for new sellers
Date: 2026-07-30
Conversation: 0ab136e0-3ce7-422f-8cbe-e50448765705
Domain: business-ops

## Summary
**Conversation overview**

Scott is a Senior Director at Blueprint RF (BPRF), now operating post-merger with Charter/Spectrum as one company. He manages TDE (Technical Design Engineer) teams, Care/NOC teams, and Philippines-based support operations. His key direct reports and collaborators include Marie Henson (TDE supervision), Kyle Davis (Care/NOC), Brian (Senior Sales Engineer), and Julian Cayetano (SE). His manager is Jady, who holds the same Senior Director title but sits above Scott in the current structure; Scott is aware they are likely competing for VP roles in a January reorg. Other key figures include Kathy (Spectrum sales leadership), Steve Collet (Spectrum field operations), Brian Miller (SVP, Jady's boss's boss), and Chris Fulton (SVP, Spectrum business org). The broader context involves integrating BPRF's hospitality Wi-Fi design, install, and support operations with Spectrum's seller force across Marriott, Choice, and Hyatt brands.

The conversation covered four major workstreams. First, Scott and Claude collaborated extensively on a TDE capacity and throughput workbook, starting with a framework Claude built from scratch, then incorporating data the team populated, then adding a calculator front-end tab (Tab 0) that takes opportunity counts by type as inputs and returns TDE headcount required, gap against current bench, and a date when new capacity lands. The calculator was rebuilt twice to incorporate confirmed rates from Marie: 7.5 hours per day (not 8), one TDE out on PTO as a headcount deduction (not an hours haircut), EOL at 1.5 hours (not 2.0), and new build at 3.0 hours (lighter than upgrade because the LV vendor handles cabling and racks, and no network discovery is required). The install constraint — Monday-only starts forcing a 1:1 TDE-to-install ratio — is modeled separately from hours-based capacity, with a section showing what the schedule costs versus staggered starts. The current bench is 14 active TDEs, with a 15th returning from leave at the start of October.

Second, Scott drafted a TDE headcount request to Jady asking for 5 additional TDEs, with the ask structured as a capacity position rather than a decision request, given Scott's read that Jady is unlikely to decide independently and that they are now peers competing for the same upward opportunities. The email was refined across many iterations: removing register references from the pre-close governance period, correcting attribution of the 5 upgrade opportunities to the Spectrum seller team broadly rather than one seller, removing any mention of the capacity calculator to avoid Jady requesting access to a tool Scott wants to control, and framing the consequence of inaction (design and FSR slip behind installs) without CYA language. The final version also incorporated Marie's confirmation that 12 starts per week is current and accurate as of that day. Third, Scott drafted a factual readout to Jady of two conversations with Brian Miller (Thursday 8/20) and Chris Fulton (Friday 8/21) about the future of the Philippines-based teams, at Jady's request. Scott assessed this as a politically motivated ask — Jady filing Scott's direct SVP access in writing before a trip to meet his new boss. The readout was written narrowly, attributed as recollection not verbatim, with qualifiers preserved ("current plans" not "plans"), and the detail about financial metrics Scott provided to Fulton was removed to avoid establishing Scott's cost expertise in a document Jady controls and will summarize upward.

Fourth, Scott responded to Jady's email attaching a Spectrum pipeline file and asking for a team split, SLA, and capacity clarity. The reply proposes capping install starts at 7 per week rather than splitting teams (preserving cross-utilization), explicitly asks for offer approval on 3-4 of the 5 candidates, defends TDE-led installs against third-party alternatives using the historical zero first-time PIC pass rate (the team's own name was "the PIC fail report"), commits to delivering a volume-driven SLA with three stated conditions (volume, start cap, request completeness), and challenges the "taking too long" feedback by distinguishing BPRF's clock (starts at complete request) from the Age column clock (starts at case creation). The Marriott forecast was not mentioned in the final send because Jady's email was itself about the missing forecast.

Scott's voice preferences are well-established: plain language over jargon ("

### SCOTT (2026-07-30T16:31)
help me with a reply here
[File uploaded: BPRF-SF-QP_MeetingMinutes_2026-07-29.pdf]
[File uploaded: 1785429048477_image.png]

### CLAUDE (2026-07-30T16:31)
Here's a single draft — reply-all (Jady, Kathy, Aaron). It answers on substance, adds the BPRF-side data that Kathy's cut doesn't cover, flags the Legal dependency, and leaves the "how do you want this to flow" question to Jady rather than answering it for him.

Two notes on the reasoning behind it:

**Sequencing #6 into #7.** You own the capacity assessment jointly with JD, due at the next governance session. That deliverable is unsourceable until someone defines the account universe. Tying them explicitly puts the dependency on record and makes the priority list the gating item rather than your capacity read.

**The Legal caveat is doing real work.** If the deliverable gets scoped to include Spectrum noncustomer data, it stalls behind Decision #2 and the Pre-Day 1 date slips — with your name on the downstream item. Scoping BPRF's contribution to BPRF's own installed base keeps you deliverable regardless of how Legal rules.

If you'd rather stay narrower and not raise #7 in this thread, say the word and I'll cut that paragraph.

### SCOTT (2026-07-30T16:35)
i only want to speak to my swim lanes.  on the capacity growth, my ask is the same as was when it came up on a call with the Charter team a few weeks ago.  i need to know the projected demand in order to spesak to wheter y team can absorb it or not. same with scale  up.  it taks a minute to staff and train etc.  need to match that ramp with the forecasted demad

### CLAUDE (2026-07-30T16:36)
Trimmed to your lanes — Action #7 and Decision #7 only, no comment on how Kathy builds #6.

One placeholder to fill: `[X weeks]` for recruit-to-productive lead time. That number is the whole argument for why the forecast has to come first, so it's worth being specific — if the ramp is 10–12 weeks and Day 1 is inside that window, the answer to Decision #7 is already determined.

### SCOTT (2026-07-30T16:36)
I don't need to say, "speaking only to the two items with my name on them, Action #7 and Decision #7."  jsut only speak to my items

### CLAUDE (2026-07-30T16:36)

Still need `[X weeks]` filled in.

### SCOTT (2026-07-30T16:39)
Would this help you with my emails drafts if I added this to project instructions?
[File uploaded: IMG_8253.png]

### CLAUDE (2026-07-30T16:39)
Mostly no — and a couple of them would work against you.

These are written for blog and social content, where the goal is passing as casually human. Your emails go to a VP, a peer director, and Charter-side leadership, and they need to survive being forwarded. "Natural imperfections," "conversational," "less scripted," "personality and opinions coming through" is the opposite of what that correspondence should be. Prompt 5 in particular would push toward the exact thing your written-record discipline says to avoid.

The one with real value is #3 — stripping AI tells. But generic phrasing gets you generic results. A specific list works better: no "delve," no "it's worth noting," no "I hope this finds you well," no three-item parallel constructions, no closing paragraph that restates the ask.

What would move the needle much more:

- **Paste 3–5 of your own sent emails** into project instructions as voice reference. Cadence, sentence length, how you open and close, where you get blunt. That does more than any abstract instruction.
- **Name your tells.** Every time you edit one of my drafts, the edit is data. The last three rounds told me you cut meta-framing, cut anything outside your lane, and want the item numbers referenced naturally rather than announced.
- **Register per audience.** Jady, Kathy, CTC, and hotel brands are four different voices. One "sound human" rule flattens all four.

If you want, add a short line to project instructions instead: strip AI-tell phrasing and hedging, but keep the register formal and forwardable. That captures the useful 20% without importing the parts that fight your actual use case.

### SCOTT (2026-07-30T16:40)
Ok. But I would never say “per cohort”. I do t even know what a cohort is.

### CLAUDE (2026-07-30T16:40)
Fair — swapped it for plain language. "Hiring and training a new group" says the same thing without the jargon.

Anything else in there that isn't your voice, flag it and I'll swap it. `[X weeks]` is still the one number only you can fill.

### SCOTT (2026-07-30T18:34)
this is current ratio.  "With seller count I can run it against the current model (2.5 TDEs per seller, 1 SE per 3 sellers) and give you headcount by period rather than a general answer."

I don't think it's linear.  They have said 100 sellers.  Need to nail the load daily.

### CLAUDE (2026-07-30T18:34)
That's the right correction — and it's worth putting in the email, because the ratio is what someone will otherwise multiply by 100 to get an answer you'd have to walk back. Rewrote it as daily load per role, with the non-linear pieces named.

Two things worth knowing before you send:

**The support tail is the real risk.** Pre-sale load ends when the deal closes. Post-sale load starts there and compounds — every property sold in month one is still generating tickets in month twenty-four. If the 100 sellers hit their number, the NOC and TDE load in year two is larger than anything in the forecast, and that's the headcount nobody budgets for. The line is in the draft, but it may be worth its own slide at the governance session.

**You'll likely get a bad forecast.** "100 sellers" as a starting input suggests nobody has modeled per-seller productivity yet. If what comes back is thin, your fallback is to model it yourself in bands — low, expected, high per-seller output — show the headcount and the ramp date for each, and let leadership pick the band. That converts your open question into their decision, which is where it belongs anyway.

### SCOTT (2026-07-30T18:35)
leave out the 100 sellers.  they have said thats what it is, but have not said all 100 will be engaged day 1.  or maybe move it to a differnt paragrasph and say this is what I heard.  what is it really.

### CLAUDE (2026-07-30T18:35)

Framing it as "what I heard" also does something useful on the record: if the number turns out to be wrong or the phasing was never decided, that surfaces now rather than at the governance session when you're the one expected to have an answer.

`[X weeks]` is the last open item.

### SCOTT (2026-07-30T18:39)
and o this, "where they're actually productive takes [X weeks], - its not a clean as that either.  we have an establiusehd multi-,ojth trainign progress where TDE's go through all aspespect. form CO's to EOL to take overve to full upgrades to full desgins lie a with a new build, and they also step into the isntalls based on same levels of compleitiy. same with the FSR process (Final sales review, fo your refernce, everyon knows what FSRE is).  its not they go through all this training and are ready to execute.  it depends on skill they cone in with (NOC agent with alot of experience vs starting with soe with the techical chops but not th eiundustry experience) and as they advance they are are able to tok tae or more and more of the complex works

### CLAUDE (2026-07-30T18:40)
That changes the argument in a useful way — it's not "weeks to productive," it's that a new head adds capacity at the bottom of the complexity ladder and only reaches the top months later. Which means the complexity of the demand matters as much as the volume. Rewrote it that way, and the placeholder is gone.

It's running longer than your usual — seven paragraphs. Two candidates to cut if you want it tighter:

- The ratios sentence. Now that complexity and daily load are both spelled out, "2.5 TDEs per seller" mostly gives someone a number to multiply. Cutting it removes that temptation entirely.
- The pre-sale/post-sale tracking lines. Real, but they're the case for the governance deck more than for this reply.

Cutting both gets you to five paragraphs and keeps the two arguments that matter: confirm the seller number and phasing, and complexity drives ramp. Say the word and I'll trim it.

### SCOTT (2026-07-31T14:05)
jady's rpely.
[File uploaded: 1785506697576_image.png]

### CLAUDE (2026-07-31T14:05)
Jady's ask is the better version of the question, and it's answerable without Charter. A throughput model is portable — build it once and it converts any demand number into headcount whenever the forecast shows up.

Two things to get right before you build it:

**The 250 / 50 ambiguity is a 12x swing.** Annual reads as ~21 proposals and ~4 closes a month, which your current team likely absorbs without a req. Monthly reads as 250 proposals and 50 installs a month, roughly 600 new properties a year against a 2,600-property base. Don't chase Charter for the answer — build the table with both columns. Then the missing variable is visibly theirs, and the model already covers whichever way it lands.

**"50 deals closed" needs the same treatment.** A deal that is one property and a deal that is a 40-property management company portfolio produce completely different install and support load. Given the meeting was about property-management company coverage, portfolio deals are the likelier intent — which would make the install and Care numbers much larger than the deal count suggests.

On the model itself: a flat "one TDE produces 10 BOMs per month" invites someone to multiply it, and you just spent an email explaining why that breaks. Express throughput by complexity tier — CO, EOL, takeover, upgrade, new build design — with units per month for each, then a blended rate against an assumed mix. State the mix assumption explicitly so it's visible when it turns out wrong.

Jady asked for Care positions too, which his TDE example doesn't cover. The conversion there is tickets per property per month against tickets per agent per day. That coefficient is the one that turns deals closed into NOC headcount, and it's the number you already have real data for.

Want me to build the throughput table as a spreadsheet — tiers down the side, both period readings across — or draft the reply to Jady first?

### SCOTT (2026-07-31T14:06)
yes.  give me the framwork of what the table and repsonse looks liek and I will send it to my managers to valudiate, correct, populate, etc.

### CLAUDE (2026-07-31T14:10)

Built the framework. Reply to Jady first, then the workbook.

The workbook is six tabs, structure only — every yellow cell is an input for your managers to fill:

**2. Throughput** — the core ask. Rows by role, lane and complexity tier: CO, EOL, takeover, upgrade, new-build design; installs at three complexity levels; FSR standard and complex; Care, dispatch, PNOC. Units per FTE per month, converted to per day, with owner, confidence and source columns so a measured rate is visibly distinct from a guess.

**3. Ramp** — months to competency at each tier by entry profile, plus productive-capacity percentage while ramping. This is where the internal-NOC-agent-versus-external-technical-hire difference lives.

**4. Care Load** — tickets per property per month split Year 1 versus steady state, tickets per agent per day, shrinkage and 24/7 coverage factor.

**5. Demand Model** — pulls the rates through and outputs FTE by role. Reading A (annual) and Reading B (monthly) run as parallel columns, so the basis ambiguity is visible rather than buried in a single assumption. Care is shown at end of Year 1 and Year 2 — the Year 2 number is the one that shows the support tail.

**6. Open Questions** — the six items that have to come back from Charter, with why each one moves the answer.

One thing to watch when it comes back: complexity mix is the single largest driver of the TDE number, and nobody has that data. If your managers can't ground it, model it in bands rather than letting one guessed percentage carry the output.

### SCOTT (2026-07-31T14:12)
for this, "I'm sending the framework to Marie, Kyle and Julian this week to populate and validate against actual output rather than estimate."  jsut sya i iwll work wit my teams.

### CLAUDE (2026-07-31T14:12)

Week of August 10 is the only thing left to sanity-check against your calendar — that's a week and a half out, and it depends on how fast the rate data comes back.

### SCOTT (2026-07-31T16:07)
now i am goign to send your spreadsheet workbopj to my team.  specifically marie, kyle and brian. help me with that email that will include the workbook as an attachment

### CLAUDE (2026-07-31T16:07)

Two things to check before sending:

**Brian's assignment is generic** — I don't know his lane, so I left it as "take the rows that fall in your lane." Tell me his function and I'll assign him specific tabs and rows the way Marie and Kyle are.

**Aug 6 is tight for real data.** If Marie has to pull actual BOM and install output out of Salesforce rather than estimate it, that's a query someone has to run. If you'd rather protect the quality, push to Monday Aug 10 and tell Jady the week of the 10th means later in the week.

### SCOTT (2026-07-31T16:09)
change last snetence to lets get first draft done by augu 6th, and set up a call to review before frisdya of that week.  also include some veribage that if they disagree with any of the framework or think there is a better way to prsent to devlep that feedback too

### CLAUDE (2026-07-31T16:09)

Per your OOO convention, direct reports book time on your calendar rather than the reverse — so "set up a call" reads as their action to schedule. If you'd rather own the invite yourself given the deadline, say so and I'll flip it.

Brian's tab assignment is still generic. Give me his function and I'll make it specific.

### SCOTT (2026-07-31T16:15)
we shoudl include that jady directed we leaves se's out of this due to chartehr alrready haveing a bunch that he is assuming will be leveraged for this ramp

### CLAUDE (2026-07-31T16:15)

That paragraph is forwardable, which is worth noting since it attributes a scope decision to Jady in writing. It's stated as direction rather than assessment, so it holds up fine if it travels — but if you'd rather keep the attribution off the record, "SE headcount is out of scope for this exercise" carries the same instruction to your team without naming who decided it.

### SCOTT (2026-07-31T18:53)
from brian (my sr sales engineer):

Scott,
 
For clarity, you don’t want me to fill in the SE rows on Tab 2?
 
Or fill it in, but it won’t affect head count ultimately.

I htink i want to reply to yes fill it out based on our current capaicty, metircs, run time, etc.  but we wont be uisng it to for consider head coutns adds until the agenda changes

### CLAUDE (2026-07-31T18:53)

Brian's question is a good signal — if he read the scope note as "skip it," the wording in the original tasking email was ambiguous enough that Marie or Kyle may have read it the same way. Might be worth sending this to all three rather than just replying to Brian.

### SCOTT (2026-08-27T18:56)
ok.  a few things here.  

1. lets review the completed workbook from my team.  I had planned on coming back to you to build the calculator, but Marie from my team built the attached.  My thought was that you could add a tab to the front of the workbook that pulled data from all the tabs my team populates, and then I could enter the number of deals, types of deal, etc., and you would spit out the headcount, the ramp, etc.  
2.  I need to send an email to Jady for an ask of more TDEs; I need you to help me craft that.  Read the attached email about the capacity of the TDE team. One thing that has changed the resource allocation that we  had to adjust for was the request for the install team to have all installs start on Mondays.  We will previously staff the team to provide 7-day-a-week coverage with multiple install starts per week.  Now, with all starts on Monday, the TDE-to-install ratio is 1 to 1. A TDE can't support more than one install at a time anymore. 
3. Today Jady told me to put in writing the conversations I had last week with Brian Miller and Chris Fulton about the future of my Filipino teams.  Typical cya political move here.  Jady can say Scott said versus being accountable himself. brian miller is Jady's new boss's boss. and Chris is another SVP in the specturm buinsess org.  short verison is they both told me there are not current plans to on-shore my off shore teams. Jady indicated that this is for a report that get filetered up to his leaders and ends up a part of larger weekly rpeort that lands on chris winfress desk.  i guess i am fine wiht this becuase it is truew what both of these dvps said, jsu tnot sure they wanteded in memorilzed in writing.  And in the new org, Jady and I have the same Senior Director title, though I still report to him.  I think he may be a little threatned that his empire is being dismatneld around him.  he is travelign to stamford next week to mee with his new boss, mark kornegay.
4. 
5. lets start wotrkog ot he above.  due to the optics and polictacl nature of eveything right now. do not make any assumtipjn,s ask me to clairfy if needed.  and you might do bet to take a few minutes to read all the chats in this project to help get othe relevant detials
[File uploaded: RE_ Revisit TDE capacity and headcount for the additional spectrum sellers.pdf]
[File uploaded: FTE Calculator.xlsx]
[File uploaded: BPRF_Capacity_Throughput_Model_FRAMEWORK v.1.xlsx]
[File uploaded: 1787856572508_image.png]
[File uploaded: 1787856629308_image.png]
[File uploaded: 1787856853018_image.png]
[File uploaded: 1787856930890_image.png]

### CLAUDE (2026-08-27T18:59)
Starting with the files. Let me read what your team populated and Marie's calculator before anything else.

Files reviewed. Let me pull the relevant history from this project before I ask anything.

Read everything — Marie's email, her FTE Calculator, and the populated workbook. Before I build or draft anything, here's what I found and what I need from you.

## Workbook QA — problems that will break the model

**Three conflicting rate sets for the same work.** Tab 2 says one thing, Marie's new "Output per OLA" tab says another, and her FTE Calculator says a third:

| Tier | Tab 2 (units/mo) | OLA tab (hrs/unit) | FTE Calc (hrs/unit) |
|---|---|---|---|
| CO | 2 | 2.0 | not included |
| EOL | 50 | 1.5 | 2.0 |
| Takeover | 2 | 3.0 | 3.0 |
| Upgrade | 8 | 4.0 | 4.0 |
| New Build | 1 | 3.0 | 3.0 |

At 4 hrs per upgrade and ~160 hrs a month, pure-tier throughput is 40 upgrades. Tab 2 says 8. Those aren't the same measurement — 8 looks like a share of a blended month, not single-tier capacity. Tab 5 divides demand by the Tab 2 number, so as it sits the model would overstate headcount by roughly 5x on upgrades.

**Hours per Unit on Tab 2 is 7.5 on every TDE row.** That's the workday, not per-unit time. The real per-unit hours only exist on the OLA tab.

**Blockers on other tabs:** Care Load B8 is text ("20-25") not a number, and the coverage factor is blank — every Care formula on Tab 5 returns nothing. Tab 3 productive-capacity row is empty. Tab 5 mix, properties per deal, designs per proposal, FSRs per deal and current headcount are all blank. The example row on Tab 2 was never deleted.

**My recommendation:** rebuild the calculator on hours, not units. Marie's FTE Calculator already works that way and it's the only construct that survives a mix change. Tab 2 becomes a reference sheet; the OLA hours become the engine.

## What I need before building

1. Which hours set is authoritative — the OLA tab or the FTE Calculator? They disagree on EOL (1.5 vs 2.0), and the FTE Calculator has no CO at all.
2. New Build full design at 3.0 hrs is *less* than an Upgrade at 4.0. Real, or a transposition?
3. Available productive hours per FTE per month — 160 (Marie's 8×20), 157.5 (7.5×21), or the 165 sitting on her OLA tab? And do you want shrinkage applied on top, or is it already baked in?
4. **The install constraint.** This is the one I most need right. With Monday starts and 1:1, is the TDE tied to that install for its full duration (22.5–37.5 hrs across the week), or only through the start? That determines whether install capacity is "12 TDEs consumed Monday, freed progressively" or "12 TDEs consumed all week" — and it's the difference between a 2-head ask and a much larger one.

## On the Jady email

Marie's math lands at minimum 4 FTEs. Before I draft:

- Is 4 your number, or are you asking for something different?
- Anchoring to Sept 7?
- Do you want the Monday-start change named as the cause, and attributed to the project team's request — or stated as a constraint without pointing at who set it?
- Attaching the calculator, or keeping the numbers in the body?

## On the Brian Miller / Chris Fulton memo

I won't draft this without your words rather than my reconstruction. Send me:

- Dates and setting of each conversation (call, in person, group or 1:1)
- What each of them actually said, as close to verbatim as you can get
- Who the memo is addressed to — Jady only?
- Whether you want a pure factual readout, or your read included

One thing worth saying now: a dated, attributed record that two SVPs said there are no current plans to onshore is more protective of your team than not having it. The exposure is the word "current" — if that reaches Winfrey's desk as a flat "no onshoring planned," it can later read as you having overstated what you were told. So I'd want to preserve their qualifiers precisely and date-stamp it.

Which of the three do you want first?

### SCOTT (2026-08-27T19:10)
for your #1 - writne me an email back to the team expalin the discrepancy and ask them which prevails. 
same for #2
same for #3

4. yes. a tde can only support a single install at a time with the current scheudle molde given to us byu the install team 

on the Jady email.  I was thinking we shoudl ask for 5?  what do you think? look at thsi email that Kathy just sent.  58 new sellers.  even if only a fraction of them are prodiuctiove, this could be a large new influx of work for my teams. 

on atacheing hte calauotart, tell him it is comelted and we can use it to model variosu ramp sche3yudled.  i still want you to build a pretty front end for it

On the brian miller chirs fulton.  these convos both happen last week, thursday 8/20 with brian miller, and friday 8/21 with chris fulton to be exact. i cant rememebr thre verbatim, basically i asked them both aboyt the future lans around my philppiens trams and how it reconciles to Chirs winfress stamtents about a us based sales and service org.  brian went to a little bit of detual baout charter spectrm cusotmsr callign in verus a bprf cusotmer calling in, and that they dont think they are calling into spetrcum support,  chris had asked me for some financial metrics on the call center costs, which you know abut if you searched tohe other chats.  he said based on those numebrs, it doesnt make sense to bring them on-shore.

### CLAUDE (2026-08-27T19:12)

Kathy's email didn't come through — nothing new in the uploads. Send it and I'll factor the 58-seller number in properly.

**On 5 vs 4:** ask for 5, but only because there's a documented fifth driver — not as padding. Marie's 4 covers Spectrum design volume (2), FSR (1), and leave coverage (1). The fifth is the install concurrency constraint itself, which is now confirmed: 12 Monday starts × 1 TDE each = 12 of your 14 consumed, leaving 2 for design and FSR combined. That's a structural gap that exists today, before a single Spectrum deal lands. It's the strongest number in the whole ask because it isn't a forecast — it's the current schedule.

The thing to be honest about in the email: 5 heads do not solve September 7. Recruiting is 6 weeks internal, 9 external, and competency on upgrades is another 2–4 months. Approving today puts productive capacity in Q4 at the earliest. Framing it as "this is the Q4 fix, and the September gap gets managed by triage" is more credible than implying the ask closes the gap.

Here's the first email.

Now the Jady ask. I've held it to what's documented — Marie's four plus the install concurrency constraint as the fifth — and been explicit that this doesn't fix September.

I left the 58 sellers out — send me Kathy's email and I'll add it, since "58 sellers even at partial productivity" is a stronger forward-looking argument than the single-seller extrapolation currently carrying that paragraph.

Now the memo. Written as a dated readout with hedged attribution, since you don't have verbatim.

Three things to weigh on that last one:

**"These are my recollection of the substance rather than verbatim."** Keep it. It's the sentence that protects you if either of them later characterizes the conversation differently. Without it, a paraphrase presented as fact is yours to defend.

**The closing line about characterizations, not commitments.** Also protective, for the reason I flagged — this lands on Winfrey's desk through two layers of summarization, and "no current plans" compresses easily into "no plans." That line is what stops the compression from being attributed to you.

**I left the cost figures out.** You told Chris the numbers; restating them here puts your BPO run rate into a document that travels upward through a chain you don't control. Say the word if you want them in.

Last item: the calculator front end. I can't build the engine until the team answers questions 1–3 — the rates drive everything. Two options: I build it now on the OLA hours as provisional and swap when they confirm, or I wait for Tuesday. Which do you want?

### SCOTT (2026-08-27T19:12)
you have have full stipped when kathys email didnt come in.  here it is
[File uploaded: [EXTERNAL] Marriott - Management Company conversations and rules of engagement with Spectrum field reps.pdf]

### CLAUDE (2026-08-27T19:12)
That changes the argument materially. Three things in Kathy's email that belong in the ask:

**The 58 sellers are hunting net new — new builds and takeovers.** That's the top of the complexity ladder, and it's where your bench is thinnest. Marie's own six-month data shows the current mix is 520 EOL against 23 new builds — roughly 4 new builds a month. A seller force pointed at net new inverts that mix toward the tiers that take 3–4 months of competency ramp after a 6–9 week recruit.

**There are two demand waves, not one.** Kathy is simultaneously directing the BPRF sales team to work the top 150 management companies on full upgrades, EOLs and new builds. Both waves land on the same 14 TDEs in September.

**Kathy just told you where the forecast is.** They're pulling everything at 75%+ probability from Salesforce as they launch into September to build a roadmap. That is the demand input you've been asking for since July. Asking for it is much stronger than asking for a forecast in the abstract.

Revised:

Two judgment calls in there worth a look:

**I named Kathy as the source.** It's attribution to a distributed email, not a read on her — but the paragraph does connect her campaign to your capacity problem, and Jady may forward it. If you'd rather not have it read that way, "58 Spectrum sellers are working Marriott deals" without the attribution carries the same weight.

**I said the calculator is complete.** It isn't quite — the rate discrepancies are still open with your team. It'll be true by the time Jady asks to see it, but if he asks tomorrow, that's a gap. Softening to "the calculator is built and I'm finalizing rates with the team this week" costs you nothing.

One thing I didn't put in: the 75%+ pull is going to Kathy and Jady's Rules of Engagement session next week, not to you. If you want that data, it's worth asking for it directly rather than waiting to be included.

### SCOTT (2026-08-27T19:15)
wheres the output per OLA tab?

### CLAUDE (2026-08-27T19:15)
It's the third tab in the workbook your team returned — sitting between "2. Throughput" and "3. Ramp" in `BPRF_Capacity_Throughput_Model_FRAMEWORK_v_1.xlsx`. Marie added it; it wasn't in the framework I sent.

What's on it:

**Left block (A–F)** — OLA hours per unit by tier, times units per FTE, giving manhours: CO 2.0, EOL 1.5, Takeover 3.0, Upgrade 4.0, New Build 3.0, Install low 22.5, Install medium/high 37.5, FSR standard 1.5, FSR complex 3.0.

**Right block (H–L)** — a column headed "Harold (Apr)" with one TDE's actual April output: 16 EOL, 1 upgrade, 1 low-complexity install, 39 standard FSRs, 18 complex FSRs. Multiplied by the OLA hours, that totals 163 manhours against the 165 sitting in E17.

**Bottom (A19:B23)** — six months of volume: CO 43, EOL 520, MACD 45, Upgrade 215, NB 23.

That Harold column is the most useful thing in the file and I underweighted it in my last message. Marie back-tested her OLA hours against a real TDE's real month and landed at 163 of 165 available hours. That's validation, not estimate — it says the hours-per-unit set is sound and that 165 is the available-hours figure.

Which means question 3 in the team email is close to answered, and question 1 mostly resolves in favor of the OLA hours. Worth trimming that email down to the two things still genuinely open: the EOL discrepancy (1.5 vs 2.0), and whether New Build at 3.0 hours is real. Want me to cut it back?

### SCOTT (2026-08-27T19:21)
for the email to Jady witht he tde ask, i wanted include the summary of me convo with brian and chris.  put it all ina  single email

### CLAUDE (2026-08-27T19:21)

One thing to decide knowingly before you send it as one email.

The readout is going to be filtered up into a weekly report that lands on Winfrey's desk. The headcount ask is a decision Jady owns and may forward or push back on. Combining them means each travels wherever the other goes — and it puts "two SVPs said no plans to onshore" in the same document where you're asking for five more offshore heads.

That linkage can read two ways. Either as a clean business case, or as using the SVP comments as leverage for the ask. Given Jady is heading to Stamford next week to meet Kornegay, and given he pushed the memo to you rather than writing it himself, I'd guess he wants the readout clean enough to lift straight into his report. A five-head offshore request sitting above it complicates that.

Separate emails cost you nothing and let each stand on its own. But it's your read of Jady, not mine — say the word and this version is ready to go.

### SCOTT (2026-08-27T19:23)
i dont think decsion is up to jady, or stated differntly i dont think he will make the decsion,  he is so scread of his job and future right now, he wount be makign any meanignful decisons.

### CLAUDE (2026-08-27T19:23)
That changes what the email is for. If he won't decide, then this isn't a decision request — it's a dated record and a positioning document, and it should be built differently.

Three adjustments worth making:

**Split them.** More important now, not less. If Jady is avoiding the headcount item, a combined email means the readout he actually asked for — and probably needs for Stamford — gets stuck behind the thing he's avoiding. Send the readout clean and fast. It's the one that helps him.

**Lower the decision burden on the ask.** A frightened manager won't approve five heads, but he might carry a prepared case into a meeting with his new boss. Reframing it as material he can use — here's the constraint, here's the math, here's what I need to size it — asks him to transmit rather than to stick his neck out. Same content, different job for him.

**Give silence a cost, on the record.** If nothing is approved, state plainly what happens and when: design and FSR turnaround slips behind installs starting the week of September 7. That's not a threat, it's the operational consequence, and it means an unanswered email still does accountability work. This one already has the timing paragraph — it just needs a date attached to the outcome.

The item is also already on the governance register as Decision #7, JD / Scott / Leadership. That's a legitimate second path that doesn't route around Jady.

Want me to rework the headcount email along those lines and keep the readout as its own send?

### SCOTT (2026-08-27T19:24)
yes.  let me see it

### CLAUDE (2026-08-27T19:24)

What changed and why:

**No "I need to request."** It opens as a position on the record. Nothing in it requires Jady to say yes, which means he can forward it without having committed to anything — and a manager protecting his position is far more likely to move something he doesn't have to own.

**"What the numbers support"** instead of "The request." Same five heads, but attributed to the math rather than to you wanting them. Harder to decline, easier to carry.

**A dated consequence.** Week of September 7, design and FSR slip behind installs. Silence now produces a documented outcome rather than nothing.

**The register reference in the subject line.** It puts the item in a governance venue with other names on it, which doesn't route around Jady but does mean it isn't solely his to sit on.

**The offer at the end.** He's meeting Kornegay next week. A one-pager he can walk in with is the version of this that serves him — and it's the likeliest path to the heads actually getting approved.

The readout stands as its own send, unchanged from what I drafted earlier.

### SCOTT (2026-08-27T19:26)
where are you getting this from "This is Action #7 and Decision #7 on the governance register."

### CLAUDE (2026-08-27T19:26)
From the meeting minutes PDF you uploaded at the start of this conversation — the HG SB Lead Sharing/GTM Pod meeting, dated Wednesday, July 29, 2026, the one attached to Kathy's email.

Action register item 7: assess project-management and support capacity and prepare a resource-scaling update so leadership can determine whether the current team can absorb the projected opportunity volume. Owner listed as JD / Scott Watts, due next governance session.

Decision register item 7: confirm whether the existing BPRF team can absorb the projected demand or whether additional staffing is required. Owner JD / Scott Watts / Leadership, due next governance session.

Two caveats before you rely on it. That register is a month old, and I don't know whether a governance session has happened since or whether the numbering still holds — if it's been reissued, the reference will look sloppy. And I assumed "JD" is Jady, which is why the email reads as though he's already a named owner. I never confirmed that with you.

If either is off, drop the register reference from the subject and the opening line. The email works without it.

### SCOTT (2026-08-27T19:27)
july 29th is ancient history.  that was pre-close.  we are post close now. one comapy

### CLAUDE (2026-08-27T19:27)
Cutting it. Post-close, citing a pre-close register makes you look like you're working off stale paper — and if the governance structure was replaced at close, it invites a correction you don't need.

That call flags something else worth checking. The 12 install starts per week figure comes from Marie's note describing the last agreement with the project team — I don't know whether that predates close too. If the install team has reset its targets post-close, the "12 of 14 TDEs consumed" math moves, and that number is carrying the entire argument.

Worth confirming with Marie before this goes to Jady.

### SCOTT (2026-08-27T19:27)
marie confirmed that today

### CLAUDE (2026-08-27T19:28)
Good — then the load-bearing number is current and the email stands as drafted.

Where that leaves the four items:

**Jady capacity email** — ready to send.

**Philippines readout** — ready, separate send.

**Team email on rate discrepancies** — still sitting in the earlier version. Given the Harold column validates the OLA hours against a real month at 163 of 165 available hours, questions 1 and 3 are mostly answered. Worth trimming to what's actually open: EOL at 1.5 versus 2.0, whether New Build at 3.0 hours is real, and the blank cells on the Care Load and Ramp tabs.

**Calculator front end** — I can build it now on the OLA hours, since Harold's month backs them up, and swap the EOL figure if Marie comes back with 2.0. That gets you a working model before Jady asks to see it, rather than after.

Which do you want next?

### SCOTT (2026-08-27T19:28)
give me the jady email again with out all the register shot in it

### CLAUDE (2026-08-27T19:28)
That last version already had it stripped — but the tool output came back malformed, so it may not have rendered for you. Here it is again.

One line still worth a decision before you send: "The calculator is complete." The rate questions with Marie are still open, so if Jady asks to see it tomorrow it isn't quite true. "The calculator is built and I'm finalizing rates with the team this week" costs nothing and stays accurate.

### SCOTT (2026-08-27T19:32)
wtf is all of this, "What I need.
I understand everything at 75 percent probability and higher is being pulled out of Salesforce to build a September roadmap. Get me that pull with deal type on it and I will run it through our capacity calculator and come back with required headcount by lane rather than a judgment call. The calculator is complete — enter deal counts and types and it returns headcount and the ramp behind it."

and add that with te activation of choice in early sept and hyat not longer after for thes new specturm sellers, i think time is of the essecne espaiclly consider the ramp to a fully productive tde can be 6 months or more.  we hire with the requsite tech skil set but expeinece in hospitality and a tde model greslty influences ramp time

### CLAUDE (2026-08-27T19:32)
Cut it. You're right that it undercuts the ask — you state a number, then say you can't size it without data you don't control. And "get me that pull" is directive at your boss over something Kathy owns.

Replaced it with the timing argument, and reconciled the ramp figures to yours.

Two things I changed that you should look at:

**"Anything approved today is a Q1 resource, not a September one."** Your 6-month figure pushes it past Q4 — 9 weeks recruiting plus 6 months lands in March. That's a harder message than the earlier draft, and it's the strongest argument for approving now, but check that you want it stated that bluntly.

**Choice and Hyatt.** I wrote it as "activates for these new Spectrum sellers in early September, with Hyatt not long after." If those dates are firmer than that, name them — a specific date does more work than "not long after."

### SCOTT (2026-08-27T19:34)
there are firm activation dates, i just dont knwo what they ae.  but jady was onteg same call i was abut this, so he knows. 

I think the 12 installs beignngin week of sept 7 shoudl be next to the part aboutg teh 1:1 tde to install ratio

### CLAUDE (2026-08-27T19:34)
Fixed both. On Choice and Hyatt I pointed at the shared call rather than guessing dates — that way it reads as a reminder rather than a claim you'd have to defend.

I also tightened the "gap exists today" line, since the 12-of-14 math only bites once you're actually at 12 starts a week.

The Choice/Hyatt line is slightly awkward as written — "on the dates covered on the call we were both on" is doing an odd job of gesturing at something without naming it. If you can pull the dates off your calendar or the call notes before you send, drop them in and the sentence gets much stronger. Otherwise "Choice activates in early September with Hyatt following" reads more naturally and Jady will fill in the specifics himself.

### SCOTT (2026-08-27T19:36)
ofc thats akward.  put it back the way it wad.  it was fine beofre

### CLAUDE (2026-08-27T19:36)

Good to go. Next up whenever you want it: the trimmed team email on the two open rate questions, and the calculator front end.

### SCOTT (2026-08-27T19:37)
does that fisrt sentiec, "Putting the TDE capacity position in writing so you have it ahead of next week, and so it is on the record before September volume lands." sound a bit liek i am cya;ing and sayaing jady doesnt ahave approval authority any more>

### CLAUDE (2026-08-27T19:38)
Yes. "On the record" is audit language, and "ahead of next week" hints that he's carrying it somewhere rather than deciding it. Both signal exactly what you don't want to signal.

Swapped for a plain statement of purpose.

I also dropped "next week" from the closing line for the same reason — it was pointing at his trip.

One line left that reads slightly defensive: "I would rather that be a known and accepted tradeoff than a surprise." It's true and it's the sentence that makes silence cost something, but it is the most CYA-flavored thing in the email. Cutting it leaves the consequence stated plainly without the framing. Your call.

### SCOTT (2026-08-27T19:41)
not sure this sentece is accurae, "We already have 5 upgrade opportunities in the pipeline from a single Spectrum seller"  i would say fromt eh specturm sellers team since the merge close and trainign last week

### CLAUDE (2026-08-27T19:41)

Worth knowing what that trade buys you: attributing to the team rather than one seller gives up the per-seller extrapolation, but it's the version that survives Jady asking which seller. Marie's original framing would have invited that question, and "just one" is hard to hold if the five actually came from several people over two weeks.

Two small numbers in there I'd still verify against Marie's note before it goes: 14 active TDEs, and whether the five are all upgrades.

### SCOTT (2026-08-27T19:42)
it may be one, it may be rwo.  i ont know.

### CLAUDE (2026-08-27T19:42)
The current wording already handles that. "5 upgrade opportunities have come in from the Spectrum seller team since close and last week's training" is true whether it was one seller or three — it makes no claim about how many produced them.

That's the version to send. No change needed.

### SCOTT (2026-08-27T19:45)
i agree now on not saying, "The capacity calculator is complete. We can use it to model different ramp schedules — enter deal counts and types and it returns required headcount by lane and the ramp behind it. Happy to walk you through it or put this on a single page if that is more useful."  i think what you said earlier soudns better, and I do not want to create a scneario whwere he says, send it to me,  i want to own and amintain this to conroal the narrative for as long as pososble.  baiscly Jady and I are now peers and will be compeitng for the same vp roles when th reorg comes in jan.  he is obvisouly going to presnet himself as the giy that know both the sles and ops and support side of the house.

### CLAUDE (2026-08-27T19:45)

That close does the work you want. It signals the capability exists, sets your own delivery date, and offers nothing to hand over.

One tradeoff to keep in view: the model is only a differentiator while you're the one running it. If Jady eventually needs numbers for a reorg conversation and you've been holding the tool, the safer play is to give him output — a scenario run, a one-pager with your name on it — rather than the file. Output travels with attribution attached. A spreadsheet doesn't.

Also worth removing from the earlier readout draft, given what you've just told me: the line about Chris Fulton asking you for call center financials. That establishes you as the person SVPs go to for the cost picture on the support side, which is exactly the ground Jady would want to claim. It reads as neutral fact in a memo he's filtering upward — but he's the one summarizing it.

### SCOTT (2026-08-27T19:47)
and int he ground jady wants to cliam is exaclty why he is wnating me to put my convos in writing to him.  I bekvie it wasnt an accident that his bosses bos (brian) flew to atanta last week and didnt give us advnace notice until the day beofre and then sceudle a bunch of meetings with jady;s teams.

### CLAUDE (2026-08-27T19:47)
That read is plausible, and the day-before notice with meetings scheduled across Jady's teams is the part that supports it. Skip-levels with short notice are how a new leader gets an unfiltered picture before the incumbent can shape it. Whether it's assessment of the org or assessment of Jady, you can't tell from the outside — but Jady evidently thinks he knows, and asking you to memorialize a conversation you had directly with Miller is consistent with wanting to know what Miller heard from you.

Which means the readout has a second reader in practice, even if it's addressed to Jady.

Two adjustments worth considering:

**Drop the Fulton financials line.** You already agreed the ground matters. In a document Jady is summarizing upward, that sentence is the one most likely to get compressed or dropped — and it's the one establishing you as the person SVPs come to.

**Consider what you're not obligated to relay.** You were asked to write up two conversations. A factual readout of what Miller and Fulton said about onshoring satisfies that. It doesn't require characterizing your own positioning in those conversations, what else was discussed, or what you concluded. Narrow is fine here.

The counterweight: if Jady's summary reaches Miller and it's thinner or differently shaped than what Miller remembers saying, that's a small risk to you. Sending the readout directly to Jady with no one copied keeps it clean, but it also means you have no independent record of what you actually reported. Keeping your sent copy matters more than usual here.

Want me to redo the readout with the financials line out?

### SCOTT (2026-08-27T20:00)
yes.  let me see it.  sent the tde email  time to work on thsi one

### CLAUDE (2026-08-27T20:00)

I replaced the financials sentence with "based on the economics" — it keeps Fulton's actual reasoning intact, which matters for the memo to be truthful, without recording that you were the source of the numbers.

Three things to decide before sending:

**"Per your request."** It's accurate and it puts the origin of the document on the record, which protects you if the readout is later characterized as something you volunteered. It's also mildly pointed. Cut it if you'd rather not flag that.

**The closing line about characterizations, not commitments.** Keep it. That's the sentence that stops "no current plans" from compressing into "no plans" as this gets summarized upward — and the compression would be attributed to you.

**Copy no one.** Adding anyone turns a requested readout into a move. Send it to Jady alone and keep your sent copy.

### SCOTT (2026-08-27T20:05)
sent. back to the ramp tool.  here is brian's response
[File uploaded: 1787861133489_image.png]

### CLAUDE (2026-08-27T20:08)
Brian's answer closes question #2 — new build design is genuinely lighter because the LV vendor handles cabling and rack work. Marie's ramp tab agrees, incidentally: new build is the *fastest* of the Level 2 competencies to train into, not the slowest.

Which means one sentence in the email you just sent is wrong: "new build and takeover work, which is the top of our complexity ladder and the longest to train into." Takeover holds up. New build doesn't. If Jady forwards it to Brian or Marie for validation, that's the line they'd catch.

The underlying argument survives — EOL at 1.5 design hours shifting to upgrade at 4.0 and installs from 22.5 to 37.5 hours is still a large load increase. It's the "hardest work" framing that's off, not the conclusion. My call would be to fold the correction into the sizing when you bring the model back rather than send a standalone retraction, but if you think Jady moves on it this week, better to correct now. Your read.

Building the calculator now.

Built and tested. Running it against your current monthly run rate (7 CO, 87 EOL, 8 takeover, 36 upgrade, 4 new build at a 30% close rate):

- Design 2.0 FTE, FSR 1.7 FTE, install 12 FTE under Monday starts
- Total required 15.6 against 14 active — gap of 1.6

**The number worth your attention is in section 5.** Install work at that volume needs 7.1 FTE if capacity could be shared. Under Monday starts with 1 TDE per install, it consumes 12. The schedule change is tying up **4.9 TDEs beyond what the work itself requires** — almost exactly the five heads you asked for.

That reframes your ask in a way that's stronger than what you sent. The five aren't really about Spectrum volume; they're recovering capacity a scheduling decision took away. That argument doesn't depend on a forecast anybody has to agree with, and it points at a policy that could also just be changed.

The flip side, which you should know before Jady runs the model himself: at today's volume the gap is 1.6, not 5. The ask only reaches five once you either add Spectrum volume or count the concurrency loss explicitly. Right now the email leans on the former, and the model supports the latter much better.

Section 6 converts the gap to a date. Approving September 1 puts a fully productive external hire at early May 2027.

Rates are seeded from the OLA tab and every one is editable, so when Marie confirms EOL at 1.5 or 2.0 you change one cell.

Your team's tabs are untouched — the calculator is a new first tab.

### SCOTT (2026-09-16T17:56)
maries resposnes on blue
[File uploaded: RE_ Action needed by Aug 6 — capacity and throughput rates - Charter Ramp model.pdf]

### CLAUDE (2026-09-16T17:58)
All three closed. Rates I seeded were right — EOL confirmed at 1.5, CO stays 2.0, new build lighter because there's no network discovery, which matches Brian's answer from the other direction.

The material change is item 3. Marie says 7.5 hours a day, not 8, and **one TDE on PTO per day**. That's a headcount deduction, not an hours haircut, and it moves your numbers. Rebuilding with it.

Rebuilt and tested at your current run rate. What Marie's answers changed:

**The "2 left for design and FSR" figure in the email you sent is actually 1.** Roster of 14 less one TDE on PTO is 13 effective. Twelve consumed by Monday-start installs leaves one. You understated it — no correction needed, but it's a stronger number if it comes up in conversation.

**Gap moves from 1.6 to 2.8** at today's volume, driven by 157.5 available hours instead of 165 plus the PTO deduction.

**The Monday-start cost holds at 4.5 TDEs** — install work needs 7.5 FTE if capacity could be shared, consumes 12 under 1:1. That's still the single best-evidenced number you have, and it doesn't require anyone to believe a demand forecast.

Two of Marie's notes worth keeping in view. Her 6-month ramp includes install training, so if you hired design-only the ramp shortens — she offered to strip it. And her new-build hours hold only when site info arrives complete, which for 58 Spectrum sellers selling net new into unfamiliar properties is not a safe assumption.

Kyle also corrected Tab 4 D5: all tickets, excluding monitoring.

The calculator is the first tab; your team's tabs are unchanged behind it.

### SCOTT (2026-09-17T17:29)
see attached.  my boss jsut sent this.  I need arpely that says I jsut got the choce forecast and am still waiitng on the marriott forecast, and with the limits to the exclusive monday start dates formt he install team, etc. etc. we are currently keeping up but no idea how long we will be able to sustain it.  we jsut stated the recruiting for 5 additoanl tde's as he directed, bit no offers have been made yet.
[File uploaded: [EXTERNAL] Fw_ BPRF Update 9-17-2026.pdf]
[File uploaded: Spectrum BPRF 9-17-2026.xlsx]

### CLAUDE (2026-09-17T17:30)

Read the pipeline file. 32 opportunities created since 8/19 — 18 sitting in the design queue now, 11 at proposal. Mix is roughly half new build, half upgrade.

One thing in the attachment you should look at before sending.

The three Marriott Village opportunities — SpringHill, Fairfield, Courtyard — are 23 days old and still sitting in Design. Rochester Airport is 9 days, Marriott Dallas Allen and Four Points are 7. Steve Collet is now sending this file daily to seven Spectrum directors, and the Age column is right there.

"We are keeping up" is defensible if those ages reflect missing floorplans or site assessment forms rather than your queue — Collet's own housekeeping note says cases keep arriving without the required documents, which would put the delay on their side. But if anyone reads the Age column as BPRF turnaround, your claim gets challenged with your boss cc'd.

Worth checking with Marie what's actually holding those three. If it's missing documents, saying so converts your biggest exposure in that file into evidence for your case — and it lines up with the SLA question Collet says is still unanswered.

### SCOTT (2026-09-17T17:36)
and put int here that the isntall team has only comnited to the two week advance notice of installs and they get prioirty of tde time

### CLAUDE (2026-09-17T17:37)

That addition also gives you a cleaner explanation for anything aging in the design queue than "we're behind" — design waits because installs took the people, on two weeks' notice, under a schedule someone else set. It's the same fact pattern Collet is describing from his side when he asks about an SLA.

Which is worth thinking about. Spectrum is actively seeking an SLA from BPRF and hasn't gotten one. If an SLA gets set without these two constraints on the record, you'd be committing to turnaround times you can't control the inputs to. This email puts them in writing with Jady before that conversation happens.

### SCOTT (2026-09-25T01:14)
atathced email i got from jady.  I want to send the below along with the workbook we have developed.  thoughts?  and need help wiuth the rpely.  and note the part about us needing to add the install piece.  that is the ext part we will be working n.  these sames tdes that are doign to deisn bom and fsr are the ones that will also lead the isntalls for those we win.

my draft reply below:

Though I am having a hard time understanding why a forecast that I have been told has been created and shared with others can’t be shared with me after multiple requests and after I have been told it can be shared with me, I am already working with my teams on a way to begin to forecast capacity against anticipated demand.
 
Please see attached. Cells C5 to C9 are the only ones required for input.  This is where the opportunities forecast by type is entered, and the TDE headcount is eeded based upon the entered number of install starts per week.
 
All installs are now TDE-led, and I don't want to go back to using SubKs for that.  My teams will hit the 80% first-time pass rate by Q4, as always planned, because of the TDE install process.  If we go back to letting SubK lead installs, I am confident we will see the near-0% pass rate from them that we saw for so many years before TDEs.
 
Marie, Brian, Kyle, and I have spent many hours analyzing the level of effort for every facet of TDEs job requirements.  We have taken the last 6 months of design work by type from the BPRF sellers prior to the merge, and layered in the Mariott activity since the merge, and the Choice forecast which I was given.
 
Now, what I would like to do is basically what you are stating below, with a slight tweak.  Instead of dividing the team in half and creating opportunities for idle time, I would rather limit the install teams to 7 install starts per week for now.  This is with the understanding that the 5 TDE’s we discussed hiring will be approved once offers are ready.  We are very close to be ready to make 3 and possibly 4 offers. As this new batch of TDE’s is onboarded, we can allow the install teams to begin to flex more, and the timing on this should align with some percentage of the opportunities converting to projects to then be installed.
 
What our capacity model is missing and I will get added in the next few days is the install forecast.  Since my TDE teams lead all installs, I have to also forecast install starts. Since I don’t control the install team, and historically have been unable to get them to give me more than a 2-week forecast of installs, I am going to take the current backlog and then add an PWIN input variable that calculates the resulting number of install starts and then assume an even spread per month based on a 90-day install timeline.
 
I would also like some more details pleas eon the comment below, “The leaders are getting “feedback” from the field that it’s taking too long”.  I have dug into this, and have been told that the current Spetrum standard is 14 days.  The majority of the correct and complete design requess we get we are turnig around in hours not days, but nothing is going over 7 days.  So wel ahead of the Spectrum norm.
[File uploaded: Re_ EXTERNAL Fw_ Choice Forecast.pdf]

### CLAUDE (2026-09-25T01:16)
Read Jady's email and your draft. Five things before the redraft, in order of risk.

**1. Verify "nothing is going over 7 days" before you write it.** The 9/17 pipeline file he sent you last week shows three Marriott Village opportunities at 23 days in Design stage, plus Rochester at 9 and two more at 7. That file goes to seven Spectrum directors daily. If Age reads as days since creation and those sat in your queue, that sentence gets contradicted with the evidence already in circulation. If they were waiting on floorplans or site assessments, you're fine — but say so explicitly rather than leaving the flat claim exposed.

**2. Bank the SLA concession.** Jady wrote that he's fine with a specific SLA tied to a specific volume. That's precisely the argument you made on 9/23, and he conceded it. Your draft doesn't acknowledge it. Lock it in writing now, before the Choice launch conversation happens without it.

**3. Answer the question he actually asked.** He asked for a clear number of TDEs per side. Your counter proposes a different lever — capping starts — which is the better mechanism, but it reads as dodging unless you also state the resulting number. Cap at 7 starts and you're telling him 7 on install, 6 on design/BOM/FSR against an effective bench of 13. Give him that, then explain why the cap is the better control.

**4. Cut the SubK paragraph, or reframe it.** Jady said nothing about subcontractors. Writing "I don't want to go back to using SubKs" puts an option on the table that nobody proposed — and once someone sees installs consuming 12 of 14 TDEs, "why do installs need TDEs?" becomes an obvious cost question. Frame it as the value the model delivers, not as a preference you're defending.

**5. Move the forecast complaint and strip the editorializing.** "Having a hard time understanding why" leading the email makes it about grievance. The request is legitimate — put it last, factually, and it still lands.

Redraft:

Two notes on what I changed:

I dropped your flat "nothing is going over 7 days" and replaced it with the conditional framing — correct and complete requests turn in hours, anything longer is waiting on documents. If you confirm with Marie that nothing in the queue actually exceeds 7 days including the Marriott Village items, put the harder number back. It's a stronger sentence; I just don't want it written until it's checked.

I also removed the contingency language around the 5 hires. "With the understanding they will be approved" invites Jady to revisit approval he's already given. The redraft treats the hires as in motion and makes the cap the thing that's temporary.

On the install forecast module — your methodology is sound. One design question before I build it: PWIN applied to the backlog gives expected wins, but installs don't start when the deal closes. If there's a lag between close and install start, the 90-day spread should begin at close plus that lag, otherwise the model front-loads install load by however long that gap runs. What's the typical close-to-first-install-start interval?

### SCOTT (2026-09-25T01:20)
1.  the 7 days is specifc to once my teams get shte complete and accutrate deign requets, that menas th site assemssmenr, floor plans, etc.  eveythign we need to do the desig and bom, etc.
2.  goo call out,  that is a part of our plan, we are goign to make sla based on these caveats.  we need to call it out>
3. becuase splitting the teams is a dumb idea and causes opporutniy for idele time.  cappy install start is baiscall ythe same things but still laowows my to corss utilize my tde's as business demads dictate
4. yes he did, "feel free to look at the current demand along with the amount of 3rd party installers that you are using to gage what the numbers should be"  i think this is what he meant with thsi stamters.  subK's and 3rd party isntallers are the same thing.
5. agrred.  i need to state it somehow.  that's what you are good at

### CLAUDE (2026-09-25T01:20)
All five noted — and you're right on #4, I missed his third-party installer line. That changes the answer: he's asking whether more installers reduces your TDE requirement, which deserves a direct answer rather than a defense.

The completeness point also fixes your exposure on the aging opportunities. Your clock starts at a complete request; Collet's Age column starts at case creation. Stating that distinction explicitly makes the 7-day number safe to assert hard.

The three SLA caveats are the most valuable paragraph in the email. Once those are agreed in writing, the "taking too long" complaint becomes a question about request completeness and install scheduling — neither of which you control — rather than a question about your team's throughput.

Two things still open before I can build the install forecast module:

Close-to-install-start lag. PWIN against the backlog gives you expected wins, but if installs start 30 or 60 days after close, the 90-day spread has to begin at close plus that lag or the model front-loads install demand.

Whether the cap should be a constraint or an output. Right now install starts per week is an input you set. If you want the model to tell you what cap the bench can sustain given a design forecast, that's a different calculation — solve for starts rather than set them. That version would answer Jady's question directly at any volume.

### SCOTT (2026-09-25T01:22)
and on the "e are close to making 3 and possibly 4 offers. "  his direction was to beign interviewing, but no offer yet.  that is why i needed worked that we need approval to hire.  and when we used subk lead isntalls the first tine pass rate wasnt ear zero, it was zero for years beofre i started.  when i started, the teams literally called the report, the "PIC fail report"

### CLAUDE (2026-09-25T01:22)
Both are material — the offer-approval point especially, since it puts the decision back on him in writing.

"I need approval to make those offers" is now the only direct ask in the email, sitting next to a proposal that's explicitly contingent on it. If he doesn't answer, the 7-cap stays permanent and that's documented as the reason.

The PIC detail is stronger than the softened version — a report the team named for its failure mode is the kind of specific that doesn't get argued with.

### SCOTT (2026-09-25T01:24)
"It is built on the last six months of design work by type from the BPRF sellers pre-merge, layered with Marriott activity since the merge and the Choice forecast."  it not built on that.  and you know it.  you helped build it.  its buolt on the very very detalied anaylsiu we did of al of the work the tdes do and the level of effort for eeach.  we ae buiding the forecast model based on what we do have, which is the lt on the last six months of design work by type from the BPRF sellers pre-merge, layered with Marriott activity since the merge and the Choice forecast.  that is why we need approval on the new tde hires.

### CLAUDE (2026-09-25T01:24)
Fair correction. The level-of-effort analysis is the engine; the six months plus Marriott plus Choice is the demand being run through it. Those are different things and conflating them undersells the work.

One line to check before you send: "Even before the Marriott forecast is layered in, it shows us short against what we are already seeing." I based that on the model showing a 2.8 FTE gap at your current run rate. I haven't run the Choice forecast through it — that's next week's work with the install module. If you want a number in that sentence rather than "short," tell me and I'll run Choice through and give you the figure.

### SCOTT (2026-09-25T01:28)
you are going rogue on me.  take a minute to review everythig and regroup.  we have 14 tde's current;y.  the 15th one that was a tde that left to take care of a sick and dieing moreht retuns at the beignning of the moth.  and that last parargraph.  he knows I dont have the marritt forecast  that is his whole posint of his email.  go back to the fost verison of this email you drafted and make these corrdections.  you are too far from point on this latest draft

### CLAUDE (2026-09-25T01:28)
Regrouped. The arithmetic problem was mine: your 9/23 email already put 7 installs = 7 TDEs available and 12 starts = 3 left, roster-based. Introducing an "effective bench of 13" contradicted your own written record. Back to your numbers, with the 15th returning in October.

Changes from the last version: the Marriott forecast paragraph is gone entirely — the demand-side sentence in the opener notes what you're working from without restating what he already knows. Headcount is on your own 9/23 arithmetic. The 15th is in without the personal detail, which doesn't belong in a forwardable email.

### SCOTT (2026-09-25T01:42)
I still dont like.  you seem to have forgetten the dynamic between me and Jady.

dont say, "the engine"  sunds too AI,.  its a work book.  call it wat it is.

"The demand side is built from" this doenst make any snese either.  not sure whay you ar enot understnaidng. I am buodig a forecast aed on what I have  we are using 6 moths of actual bprf seller activy prior to the merge.  we are usign the spectum sellers marriott activt sicne the close, and the choice forecast i did revie.  its because of this and with the instlals set to 7 starts per week that we need to to approve the 5 ew hores.  but also why i think that with the 15th tde coming back and the 3 possibly 4 we are ready to make an offer on, we "should" be ok.  of course all this goes to shit if we get a tidal wave of desing work fort eh spetrcum sellers. 

"For reference, the week the install team ran 12 starts, I had 3 TDEs for everything else." no value to this sentecnec i think

" Going back to installer-led installs would change the ratio, but that process is why we are on track for the 80 percent first-time PIC pass rate in Q4" this sounds exaclty backeards.  we are on track for 80% first time pic thanks to tde led installs.  not subk led installs.

"On splitting the teams. I can give you a clear number, and I would rather set it by capping install starts than by fixing a split. " the reads ackweard too.  why niot just simply sate, verus splitting the teams. i want to limit the starts to 7 per week, and then give a brief explaintion why.  i dont need a buch of fancy ai sounding verbaige here. 

"On the SLA. Tying it to a specific volume is exactly right and I will commit to it. Three things have to be named or the commitment is not meaningful:" dont make it read like he suddenly gave me the idea i was lookign for.  i was already goign doe this path before he gave me the captain obviosu answer.

on the 3 things you are saying i need him to give me.  no.  i am not lookign him to give me anythign.  even with the limited data posit i have (ie no forecat) I am going to come up with a volume dirive sla and give it back to them.

### CLAUDE (2026-09-25T01:43)
Understood on all six. Rewritten plainer, and the SLA is now something you're delivering rather than something you're asking him for.

One thing worth weighing, since it cuts against the tone you want.

"We should be in reasonable shape" is a more confident position than the earlier drafts, and it fits the dynamic — you're not pleading. But it also gives Jady an easy exit on the offer approval. If you're fine, the urgency drops, and he's already disposed toward not deciding.

The tidal-wave sentence is doing the work of keeping pressure on, but it's soft. If you want that paragraph to still force a decision, tying the confidence explicitly to the offers going out does it without changing your posture: we're in reasonable shape *with* those hires, not in spite of them.

Your call — it's a real tradeoff between projecting control and keeping the ask alive.

### SCOTT (2026-09-25T01:46)
the reaosnable shape is if he approves the 5 new hores.  do you think that is not being communcated clearyl here?

### CLAUDE (2026-09-25T01:46)
It's clear on a careful read, not on a skim — and Jady's the reader who skims to the part that lets him not decide.

Two specific weaknesses:

**The condition trails the conclusion.** "Between the 15th coming back and those hires, we should be in reasonable shape" puts the good news in the emphasis position. Lead with the dependency instead and it can't be read the other way.

**3 or 4 versus 5.** The paragraph says offers are ready on 3, possibly 4. Then "those hires" carries the reasonable-shape claim. So the email never actually says the number is 5 — a reader could conclude 3 or 4 gets you there and the other two aren't needed.

Tightened:

> Per your direction we have been interviewing, and we are ready to extend offers on 3, possibly 4 of the 5 candidates now. I need approval to make those offers. With all 5 in and the 15th back, we are in reasonable shape against what we are seeing today and can start raising the start cap as opportunities convert to installs. Without them, I am holding at 7 starts a week and design turnaround stretches as volume grows. Either way, a tidal wave of design work from the Spectrum sellers changes the math.

That keeps your posture — you're stating the operating consequence, not asking for help — while making approval the thing the paragraph turns on. Want me to drop it into the full email?

### SCOTT (2026-09-25T01:47)
give me the whole email with that change.  dont go changing anythign else

### CLAUDE (2026-09-25T01:47)

Only the hiring paragraph changed.
