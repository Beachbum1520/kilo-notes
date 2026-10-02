# Interview preparation for software dev hire
Date: 2026-06-29
Conversation: 38121caf-f033-461b-bedc-a8e9d0d6d9b4
Domain: business-ops

## Summary
**Conversation Overview**

The person is a senior leader (likely Senior Director or VP level) at a hospitality technology company supporting a large hotel network, overseeing a software development department among other functions. They were preparing for a 30-minute screening call with Terry Parrish, a candidate their direct report Dan (software dev department manager) wants to hire for an open position. Key colleagues mentioned include Dan (direct report, hiring manager for this role), Jady (the person's manager, who owns P&L decisions including compensation band approvals), and Leo Hagan (referenced as a prior situation where comp expectations needed to route to Jady). The team operates across US and Philippines locations with distributed, async work patterns. The role supports internal operational systems for a large hotel network.

Claude helped the person prep for the call with structured questions and talking points, flagging resume items worth probing (AWS certifications depth vs. breadth, a short tenure at a prior employer, an unusual career pivot, and a significant incident-reduction claim needing specifics). During and after the call, the person relayed key information: the candidate's prior role ended due to a site closure with a declined relocation offer (clean reason to be on the market), the role is currently two days in-office per week but expected to move to five, the candidate's home location involves a substantial commute, and the candidate confirmed comfort with the full in-office trajectory. The person flagged that they did not want to undermine Dan's ownership of this hire.

After the call, the person confirmed the candidate passed on technical merit and made a strong impression for discipline and initiative, attributed to a military background. Claude drafted a hiring recommendation email to Jady summarizing the screen, recommending to proceed, offering Jady the option to interview the candidate first, and routing the compensation decision to Jady as P&L owner — consistent with how prior comp situations have been handled. The person requested one line edit: removing a specific reference to the Philippines office from the candidate summary line, replaced with "working across time zones." The email was composed using a structured tool and finalized in that form. The person's communication pattern for upward messages to Jady is concise, direct, and routes decisions cleanly without over-explaining. Protected information about the candidate's personal circumstances was deliberately excluded from the written record at the person's implicit direction and Claude's recommendation.

### SCOTT (2026-06-29T17:37)
this is the guy dan, the mgr of my software dev dept wants to hire for the open postion we have.  i have 30 mins on the calendar with him in abut 30 mins.  give me some qurstions and talkign points fo this call
[File uploaded: resumeterryparrish.pdf]

### CLAUDE (2026-06-29T17:38)
Scott's preparing for a final-round conversation with Terry, a candidate Dan wants to bring on. Since Scott's a Senior Director rather than the hiring manager, this is more of a skip-level assessment—he's probably looking to gauge Terry's overall fit, decision-making ability, communication style, and genuine motivation for the role rather than diving into technical depth.

Looking at Terry's resume, there are some interesting threads worth exploring. The 20+ year career arc is solid, but a few things stand out: the respiratory therapy degree seems like an outlier alongside the CS and computer engineering credentials—worth a curious, light touch question about that pivot. The work history itself is actually continuous when you parse it out, though the "Early roles" section lumps five companies across 15 years in California together, which is worth understanding better—whether that was rapid movement, growth within roles, or something else entirely.

The seven AWS certifications, including Solutions Architect and DevOps Engineer Professional, are impressive but raise a question about depth versus credential collection—I'd want to know if the real-world work backs up the breadth. The claim about reducing incident rates by over 90% is substantial and worth probing on how that was measured. There's also a minor attention-to-detail flag: a duplicate bullet point under Emory suggests the resume got some AI assistance and wasn't carefully reviewed.

Given Scott's org—supporting BPRF's internal systems like Salesforce, Cosmos, and OAB for a BPO-heavy hospitality tech operation—this role is probably full-stack cloud development supporting network ops platforms. That context matters for how to evaluate whether Terry's background actually maps to what the team needs.

Scott would likely focus on understanding why Terry's leaving GM and what draws them to BPRF, whether the certs translate to real production chops, how they handle incidents and ambiguity, and how they'd collaborate across the distributed team including the Philippines operations. Compensation expectations and any flight risk signals—those recent short stints at Cognizant and GM—would also be on his mind, especially given his P&L responsibility and past comp band issues.

The Cognizant role as a Senior Android Engineer is a bit of a pivot from the cloud/full-stack positioning, and that seven-month tenure warrants a gentle probe. I should frame any concerns as questions to explore rather than character judgments based on a resume alone.

For this 30-minute call, I don't need to create a document — he wants talking points he can reference live, so I'll keep it scannable with light structure and grouped questions for clarity without over-formatting.

The real value here is focusing on what Dan's technical screen won't cover: I'll lead with a quick resume read (what to probe, what stands out), then frame the conversation around motivation and fit, ownership and judgment, collaboration across distributed teams, a couple technical sanity checks, and compensation logistics. I'll also flag potential red or yellow flags worth clarifying.

For the resume specifics, those seven AWS certs show breadth but I should verify depth through experience-backed questions. The seven-month Cognizant stint and Android pivot need clarification, and those early roles lumped together from 2001–2016 across five big companies are vague enough to warrant one probing question. The respiratory therapy background is unusual but more curious than critical. I noticed a duplicate bullet at Emory—minor attention-to-detail thing I'll just be aware of rather than raise directly. That 90% incident reduction claim needs specifics on how it was measured.

Now thinking about Scott's actual environment: distributed team across US and Philippines, working with Salesforce, Cosmos, and OAB systems. I should ask about offshore collaboration and async work patterns, plus how he handles picking up existing or legacy codebases. The real angle here is that their software isn't greenfield—it powers operational systems for 2,600+ hotels with 200K endpoints, so uptime is critical. That's worth framing directly: "Our software isn't a typical SaaS product; it's operational infrastructure hotels depend on 24/7. How do you approach being on the hook for that kind of responsibility?"

On compensation, the Leo Hagan precedent suggests if Scott's near the band ceiling, he might get routed to Jady, so surfacing expectations early could prevent surprises down the line.

I'll structure this to be scannable—he needs to glance at it during the call itself. Short, direct questions organized into clear sections.Here's a tight prep sheet you can glance at on the call. Since Dan owns the technical screen, your 30 minutes are best spent where his screen won't reach: motivation, judgment, ownership, how he works with a distributed team, and a couple of sanity-checks on whether the resume holds up.

## Quick read on the resume (where to probe)

A few things stand out that are worth clarifying rather than taking at face value:

- **Seven AWS certs, including two Professional-level.** Strong on paper, but cert breadth can outrun hands-on depth. Don't quiz the certs — instead ask experience questions and see if the war stories match the credentials.
- **Cognizant was only ~7 months (Jan–Aug 2021), as a "Senior Android Engineer."** That's a short stint and an odd pivot from his cloud/full-stack narrative. Worth understanding why he left and how it fits.
- **"Early roles" lumps 5 companies (Raytheon, General Dynamics, DreamWorks, DirecTV, Guard Time) into one 2001–2016 block in California.** 15 years compressed into vague bullets — get him to talk specifics on at least one.
- **"Reduced incident rates by over 90%" at GM** — big number, no baseline. Ask how it was measured and what he actually changed.
- The Respiratory Therapy associate's is an unusual thread but more curiosity than concern.

## Opening / framing (first 3–4 min)

- Set context: you're not re-running Dan's technical eval; you want to understand how he thinks, what he's looking for, and whether the team's a fit both directions.
- Quick frame on the role: this isn't greenfield SaaS — the software supports live network operations across 2,600+ hotels and 200K+ endpoints. Uptime is the product. The team is US and Philippines-based.

## Questions by bucket

**Motivation & fit**
- He's at GM and "Current" — what's pulling him to look, and what's he hoping the next role gives him that this one doesn't?
- What does he know about what we do, and what made this interesting enough to take the call?

**Ownership & judgment**
- Walk me through a production incident you owned end to end — what broke, what you did, what you changed so it didn't recur. (This is your check on the 90% claim.)
- Tell me about a time you inherited someone else's messy codebase or system. How'd you get your footing?

**Working in our environment**
- Most of our dev work isn't building from scratch — it's supporting operational systems people depend on 24/7. How do you stay sharp on work that's more "keep it running and improve it" than "ship something shiny"?
- You'd be collaborating daily with engineers in the Philippines across time zones. What's your experience working with distributed or offshore teams, and how do you keep things moving async?

**The pivots / timeline**
- The Cognizant stretch was brief — what happened there?
- Of all those early-career companies, which one shaped you most, and what did you actually build?

**Logistics (close it out)**
- Get his comp expectations on the table early — better to surface a mismatch now than after Dan's invested. (Worth flagging to Jady before anything firms up, same as the Leo situation.)
- Timeline / other processes he's in.

## What to listen for
- Specificity. Does he tell concrete stories or stay at buzzword altitude? The resume leans generic, so push for detail and see if he can deliver it.
- Whether he asks *you* good questions — strong senior people interview you back.
- Coachability and humility vs. seven-certs swagger.

Want me to turn the comp-expectation read into a quick note for Jady afterward, or draft your feedback-to-Dan template so you can fire it off right after the call?

### SCOTT (2026-06-29T18:07)
gm closed june 1st.  he said was given option to move to austin, tx, and declined

### CLAUDE (2026-06-29T18:07)
So Terry's situation makes sense now — GM closed the Roswell site on June 1st and he turned down the Austin relocation offer, which is why he's actively job hunting. This context clarifies what prompted the search in the first place.

A few things to keep in mind for the call: his resume still lists GM as "Current," so it's been about four weeks since the closure. I should gently verify whether this was a true relocation offer he declined or if it was framed as part of a severance package — either way it's fine, but it tells me about his actual availability and how he's positioning the transition. Also worth a light touch on whether he's committed to staying in Atlanta long-term, since our team spans US and Philippines and I want to make sure he's stable on location before we go too deep into comp conversations. The upside is he's likely more motivated and flexible right now, which could work in our favor on timeline and terms.Good — that actually de-risks the biggest question on the page. The short Cognizant stint plus the "why are you leaving a job you're currently in" question were the two things that looked a little off, and a site closure with a declined relocation is a clean, credible reason to be on the market. Not a flag.

A few things it changes for the call:

**It resolves the motivation question** — you don't need to dig on "why leave GM." Instead, pivot that energy to: *"You declined Austin — what's keeping you in Atlanta?"* You want to confirm he's rooted here and not just job-hopping until the next relo-required offer comes along. If he's anchored in Atlanta for real reasons (family, house, roots), that's a stability signal in your favor.

**His resume is now slightly stale** — it still says GM "Current." Minor, but if he doesn't mention he's actually been out since June 1, that tells you something small about attention to detail. If he's upfront about it, good.

**It shifts the comp/timeline dynamic toward you.** He's between roles, ~4 weeks out, likely talking to others but also more motivated and possibly more flexible on start date and number. Don't lowball, but you have a little more room than if you were prying him out of a stable seat. Still get the number on the table early.

**One light thing to listen for:** "given the option to move and declined" and "laid off in a site closure" can be the same event told two ways. Not worth challenging — but how cleanly and honestly he frames it tells you how he'll frame things when something goes sideways on your team. You want someone who owns the plain version, not someone who spins.

You've got the technical depth covered by Dan, so spend your 30 on rootedness in Atlanta, how he works async with the Philippines team, and one real ownership story. Want me to drop the comp note to Jady once you've got his number?

### SCOTT (2026-06-29T18:09)
a bit far from of office..
[File uploaded: 1782756544188_image.png]

### CLAUDE (2026-06-29T18:09)
Looking at this map showing the commute from Loganville to the Perimeter area near 285/400 in Dunwoody — that's roughly 50 minutes and 34 miles. Given that Terry's resume lists Atlanta and we were discussing hiring them, this is probably showing their home location relative to where the office is situated.

The real question is what the in-office expectations are for this role. If it's hybrid or remote-focused, especially for a software developer supporting a distributed team across the US and Philippines, then a 50-minute commute becomes much less of a concern. And ultimately, this is Terry's decision to make — they can weigh whether the commute works for them. I should be careful not to treat distance as a disqualifier, though it's fair to clarify what the actual office attendance requirements are.Yeah — that's a real Atlanta commute. Loganville to the Perimeter is ~35 miles and the map's optimistic 50–57 min is *off-peak*. With actual rush hour on 78/285 you're realistically looking at 75–90 min each way, easily 3 hours round trip on a bad day.

A few thoughts before you let it weigh too heavily:

**It's his call to make, not really yours to screen on.** The cleanest move is to be transparent about the in-office expectation and let him decide if it works. Plenty of people knowingly take a long commute. What you don't want is to quietly down-rank him over it — that's both legally cleaner to avoid and just better practice.

**The real question is the in-office expectation for this role.** Your dev team is already split US/Philippines and works async by necessity. If this seat can run hybrid or mostly-remote, the commute is close to a non-issue and you shouldn't sweat it. If Dan needs him in a chair five days a week, then it's worth surfacing directly.

**Where it *does* legitimately matter is retention.** Long commutes are one of the more common quiet reasons people bail at 9–12 months. So it's fair to factor in as a stability question — not "should we hire him" but "will this stick." That ties back to the rootedness read from before: he's anchored east-side, declined a relo, so he's not going anywhere geographically — but a brutal daily drive is its own flight risk.

So the move on the call is one honest question: lay out what in-office actually looks like for this role, and ask him plainly whether the drive is something he's good with long-term. His answer tells you more than the mileage does.

Want me to phrase that question so it lands as logistics-checking rather than "we're worried about your commute"?

### SCOTT (2026-06-29T18:11)
this psotion is in the ofifce two days a week now.  soon most liekly will be moving to 5

### CLAUDE (2026-06-29T18:11)
Scott's facing a real decision point here—two days a week is manageable, but the trajectory toward five days changes everything. A three-hour daily commute becomes a serious quality-of-life issue and a genuine flight risk, especially if he doesn't know that escalation is coming. I need to give him a straight assessment of what he's actually signing up for.

The right move is to be upfront about the likely shift to five days. Hiring someone under the premise of two days when he knows it's heading to five is setting both the candidate and the team up for failure. That's not how you treat someone fairly, and it'll cost him more in the long run when they leave. Keep it direct and practical—no need to overthink this.That changes the math in an important way, and it's worth being clear-eyed about it.

At two days a week, a Loganville commute is annoying but very livable — most people absorb that fine. At five days, ~3 hours round trip daily is exactly the kind of thing that quietly burns people out and has them back on the market in under a year. So the trajectory matters more than the current state.

The thing I'd flag: **you know it's likely going to five days. He probably doesn't.** If you hire him on the two-day premise and the in-office expectation triples six months in, you've got a strong chance of losing him right after he's ramped — which is the most expensive time to lose anyone. That's not a reason to pass on him, but it is a reason not to let the two-day number do the talking on the call.

The straight move is to tell him where it's heading. Something like: *"Right now this is two days in-office, but I want to be upfront — we expect that to move toward full-time in-office before too long. I'd rather you weigh that now than be surprised later."* Then watch how he reacts. If he's genuinely fine with a daily Loganville-to-Perimeter drive, great, you've de-risked it honestly. If he hesitates, better to know today.

Three reasons that's the right call beyond just being fair:

- It protects the hire. A candidate who opts in with full information sticks; one who feels bait-and-switched leaves.
- It's a values check on him too — how he responds to an inconvenient truth told plainly tells you how he'll handle them on your team.
- It keeps *you* clean. If this ever gets revisited, you disclosed the real expectation rather than soft-pedaling it to land the candidate.

One more angle worth a beat: is there any world where this specific seat stays hybrid even as the broader team goes to five? If Dan would flex on that for the right person, the whole concern evaporates and you've got a strong candidate with a now-manageable commute. Worth knowing your own room before the call so you don't over- or under-promise.

Want me to tighten that disclosure line into something you can say verbatim?

### SCOTT (2026-06-29T18:12)
i asked him abotu 5 days,  and he said is fine..  but he is alos iunemplyed and already shared has small children, (twins) to suppor.t  but this is dan's guy.  I do not want ot urserp him

### CLAUDE (2026-06-29T18:13)
I'm noticing some tension in Scott's position here—Terry seems like a reasonable candidate on paper (willing to work in-office, though unemployed and supporting twins), but Scott's hesitant to override Dan's judgment since this is Dan's hire to make. There's something unresolved in Scott's thinking about how to handle this situation. The key is to affirm Scott's instinct to respect Dan's ownership while reframing the real concern — that financial desperation might produce a fragile yes rather than genuine commitment — as a legitimate retention signal worth flagging. But I need to be clear that the unemployment and kids can't factor into the hiring decision itself; that's legally and ethically risky territory. The move is for Scott to pass his observations to Dan as clean, job-relevant input about retention risk, then let Dan own the call. lean into that framing — keep the concern verbal and translate it into job-relevant criteria. The real question isn't about his kids or unemployment, but whether he'll stay given the commute and role trajectory, which he's already confirmed. Scott should give Dan an honest, job-focused assessment and let Dan make the call, rather than vetoing based on personal circumstances. I need to keep this tight and direct since he's heading into a call soon. The core move is to validate his instinct to defer to Dan while adding the legal guardrail about protected status — framed as protecting him, not lecturing. I'll skip the psychoanalysis and assume good faith on the retention concern, just give him the clean way to flag legitimate worries without using family circumstances as a decision factor. Being unemployed actually cuts both ways — it makes him motivated and available, but that's exactly why I need to think about retention. The real protection isn't screening him out; it's the honest conversation I already had with him. I could offer to help him frame the handoff to Dan, which feels useful and keeps things straightforward.Your instinct to defer to Dan is the right one — this is his hire to own, and stepping on that would cost you more with Dan than any single candidate is worth. So hold that line.

But let me separate the two things you're feeling, because one is fair and one is a trap.

The fair part: you're picking up that "5 days is fine" from an unemployed guy who needs the paycheck might be a *need-this* yes rather than a *want-this-long-term* yes. That's a legitimate retention question — is this durable once the commute reality and the five-day grind set in. Reasonable thing to wonder about.

The trap: letting "unemployed with twins to support" become a reason to hesitate on him. That can't be what tips the call, and you don't want it anywhere near the written rationale. Decisions that read as "we passed because of his family situation" are exactly the kind of thing that creates exposure, and it's not job-relevant anyway. You already did the correct thing — you asked him the hard question directly and he said yes. Take the yes at face value. The honest disclosure you made *is* your protection against a desperation-yes; you didn't soft-pedal it, so if he stays, he stays with eyes open.

Honestly, the unemployment cuts both ways in his favor as much as against — motivated, available now, fast start. The kids are irrelevant to whether he can do the job.

So here's the clean move: if you walk out of this call with a genuine gut read on fit or staying-power, hand it to Dan as *job-relevant* input — "here's my read on durability given the commute trajectory" — and let him weigh it. Keep it verbal, keep it about the role, and let Dan own the decision. That keeps you out of his lane and keeps you clean on the record.

You're about to walk in — want me to give you the one or two questions that get at "will he stay" without going anywhere near his personal situation?

### SCOTT (2026-06-29T19:03)
he passed, other thatn the distance, which isnt fair to judge him badly on.  he said its fine, and its fine.  he definteily has the tehncial choips to do the job, and maube its his military background but he cam across as very disciplined, initiative taking kind of team memebr.  write me a summary for jaDY, OFFER TO KET HIM INTERVIEW OR ask if we are good to proceed to the offer

### CLAUDE (2026-06-29T19:04)
I'm drafting a summary for Jady, Scott's manager, keeping it focused on job performance and relevant facts. Scott was clear that distance and personal circumstances shouldn't factor into the evaluation, so I'll stick to what matters professionally and leave the family situation out of the record.

The email should confirm the candidate passed screening, highlight the technical fit and initiative demonstrated, address the commute as a disclosed factor that's been accepted, and give Jady a clear choice on next steps. I'll also flag compensation as an open item that needs to route to Jady since Scott didn't provide a specific number, rather than guessing at one. Dan's eval is solid on the technical side—AWS, cloud infrastructure, full-stack work, containers. Terry came across as disciplined and self-directed, which matters for a distributed setup. His previous role ended cleanly in June due to a site closure, and I walked him through the commute reality—two days now, likely five eventually—and he's comfortable with it. I'm ready to move forward, so I'm asking Jady if he wants to interview Terry or if we should proceed straight to an offer.

I'll route the compensation discussion through Jady as the P&L owner and get Terry's expectations locked in before we finalize anything.

Drafting an email to confirm next steps.He passed your screen, Dan owns the technical call and is sold, and you've handled the one real question — the commute — the right way by disclosing it and taking his yes. Here's a tight note for Jady that keeps it job-relevant, routes the comp decision to her as P&L owner, and asks the proceed question cleanly.

That's ready to send. A couple of notes:

I kept his family situation out entirely — it's not job-relevant and doesn't belong in the written record. If Jady asks about staying-power given the commute, that's a verbal conversation, not an email line.

I left the comp routing in because it mirrors how you handled Leo — surfacing the P&L decision to Jady before anything firms up rather than carrying it yourself. If you've already got his number or want to leave comp out until you do, easy to cut that paragraph.

Want me to draft the quick feedback-to-Dan note too, so he's looped that you cleared the screen and it's now in Jady's hands?

### SCOTT (2026-06-29T19:06)
rework this line, "The kind of self-starter who holds up on a distributed team working async with the Philippines" take out philippines

### CLAUDE (2026-06-29T19:06)

Done — now reads "working across time zones." Everything else is unchanged and it's ready to send.
