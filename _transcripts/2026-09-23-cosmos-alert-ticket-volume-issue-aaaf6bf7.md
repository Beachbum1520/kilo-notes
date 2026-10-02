# COSMOS alert ticket volume issue
Date: 2026-09-23
Conversation: aaaf6bf7-5d85-4177-a7b6-6906452f242b
Domain: business-ops

## Summary
**Conversation Overview**

Scott, who joined his current company in September 2022, worked with Claude to draft and refine a series of escalating communications about COSMOS, a proactive network monitoring system provided by CTC (also referred to as CallTek). COSMOS integrates with CAS (their current ticketing platform) to auto-generate tickets, and the core problem is that this integration has produced catastrophically excessive ticket volume. Key terminology throughout: COSMOS (CTC's monitoring platform), CAS (current ticketing system), PNOC (Proactive Network Operations Center), NOC (Network Operations Center), and Zendesk (the replacement ticketing platform in development).

The conversation progressed through several drafts. The email began as a threat to disable the integration if CTC didn't provide a remediation plan, then evolved into a directive ordering CTC to disable it immediately after Scott confirmed his team was already building a replacement. Two customer escalations were incorporated: Renodis (TownePlace Suites Fayetteville), who reported approximately 20,000 alert emails in a month and twice threatened to file an abuse complaint against Scott's domain, and Atrium (Embassy Suites Omaha), whose Outlook locked up from alert volume. CTC's position that the email frequency is "by design" is central to Scott's argument. Key data anchoring the email: 2024 as the pre-integration baseline (75,246 tickets, ~206/day) versus August 2026 (710,568 tickets, 113x the monthly baseline), with August 31 alone producing 45,642 tickets of which only 104 were email-originated. The COSMOS SOW was signed June 2, 2021 with a 45-day estimated completion; it did not deploy until late 2025, making it over five years late.

Claude also drafted a separate forward to Jady, Scott's leader, which Scott wanted to include his personal reflection that loyalty to his CTC team had delayed an exit decision he now believes is correct. Claude recommended splitting that note: send the factual timeline in writing and deliver the exit call and personal reflection verbally to avoid contradicting the CTC-facing email and to protect against the note being forwarded. Scott disagreed and wanted the full note sent to Jady as written, so Claude produced the complete version incorporating the SOW signing date, the Q1 exit intent, the late November/early December telephony cutover from CTC's Mitel system to a hosted voice system Scott's company controls (timed to Scott being on-site in the Philippines), and Scott's personal acknowledgment that Jady had been right about CTC. Claude recommended attaching the SOW because it establishes that CAS alarm management and 100K-device scanning in 15 minutes were already contracted deliverables, making the current failures a breach rather than a feature gap. Key colleagues mentioned: Jady (Scott's leader, long-advocating a CTC exit), Helen (planned PNOC-to-NOC integration lead), Dan (building replacement monitoring platform), Alison (CTC contact who gave the "by design" response), Josh and Mio (CTC leadership recipients of the directive email), Zachary (Renodis contact who demanded executive escalation), Aaron and Jeanene (involved in the Renodis thread), Andras (raised rwc600 hardware upgrade), Cedrich (has open action items on the Renodis Salesforce data issue).

### SCOTT (2026-09-23T14:35)
Review the notes below and the attached screenshots.  My proactive monitoring system (COSMOS) that CTC provides jsut aint cutting it.  my team is reccommending that we turn off the integratin from cosmos to cas and go back to the PNOC manaully creatign tickets for legit alerts.  which then disrupts helens plan to intergrate th pnco into the noc. soethign that has been planned for years but was waiting on cosmos to be fully funtional. based on these tickets numbers, cosmos is creatig a buch of tickets that it shouldnt be,  help with with an email to the ctc leadership to adress this

Last month (August) produced about 1/3 of all the tickets we have ever created since 2014 
 

Here is 45,642 ticket created only on August 31 2026.

 
If I only include email tickets on August 31 2026 we have about 104 tickets
[File uploaded: 1790171927409_image.png]
[File uploaded: 1790171931956_image.png]
[File uploaded: 1790171937957_image.png]
[File uploaded: 1790171945134_image.png]
[File uploaded: 1790171955073_image.png]

### CLAUDE (2026-09-23T14:36)

A few things to check before it goes out:

- **Your "1/3" figure is off.** August's 710,568 is 23% of the all-time total (3,065,619), not a third. I used the stronger comparison instead: August alone is 92% of everything from 2014 through 2025 combined (770,046).
- **The 99.8% line needs one more check.** The 45,538 non-email tickets include phone, web, and API tickets too, not just the integration. Re-run Aug 31 with Requester = CAS Integration (or Group = Proactive Monitoring) and put the exact number in. That lets you drop "predominantly," so CTC can't pick at the figure.
- **Aug 31 was about 2x the August daily average** (45,642 vs. ~22,900). If CTC tries to call that day an outlier, the monthly and yearly numbers still make the case.
- **Loop in Jady before sending.** The October 9 disable threat is a lever against a vendor you're already in dispute with, and it builds the record he'll want for the exit plan.
- **I left Grand Hyatt Vail out on purpose.** That 68-day suppression is the opposite failure (too few alerts instead of too many), and together they show a pattern. But it belongs in the compliance track you're holding for Jady, not in an operational ask.

On your team's recommendation: fully reverting to manual is a blunt fix. It drops the legitimate auto-tickets along with the noise, and item 2 (containment to critical alert classes) gets you most of the relief without that loss. On the other hand, the cost to Helen's plan is smaller than it looks. You're targeting a CTC exit in Q1 and Dan's team is building a replacement platform, so the NOC/PNOC integration probably gets rebuilt on the new platform anyway. The real decision is what PNOC runs on between now and Dan's platform, not whether to save Cosmos. Keep that reasoning verbal; the draft doesn't touch it.

### SCOTT (2026-09-23T14:39)
it was towards the end of 2025 that we fired off the ticket generation for cosmos.  i think was around july august but we ahd a few misstarts whre we had to turn it off due to identifed issues with the cosmos system.

### CLAUDE (2026-09-23T14:39)
That makes 2024 your clean pre-Cosmos baseline. It's a much stronger comparison than stacking years together, and it changes how the data section should read. Replace the "Ticket creation by period" block and the "Portfolio growth" line with:

> For context, 2024 was the last full year before auto-ticketing went live. It serves as our pre-integration baseline.
>
> - 2024 (pre-integration): 75,246 tickets, about 6,270 per month and 206 per day
> - 2026 YTD: 2,295,573, which is 30x all of 2024
> - August 2026: 710,568, which is 113x the 2024 monthly average
> - August 31 alone: 45,642, which is 222x the 2024 daily average. Only 104 of those came in by email; the other 45,538 (99.8%) were system-generated, predominantly through the integration.
>
> Portfolio growth does not come close to explaining a two-order-of-magnitude increase. This is also not the first time the integration has created problems. It was turned off more than once during the 2025 rollout because of issues identified in Cosmos, which is why the curve starts in 2025.

Before you send, pin down three things:

- **Dates for the 2025 misstarts.** If Kyle or Helen can give you the on/off dates, name them in the email. "More than once" is defensible, but specific dates put the pattern on the record and also set a precedent that turning the integration off is a normal remedy, not an escalation.
- **Whether the integration was on in January 2026.** January was 29,493 and August was 710,568, a 24x swing within the same year. If the integration was on the whole time, the problem is getting worse, not holding steady, and that supports the October 9 deadline. If it was off in January, that month gives you a second clean baseline.
- **Why 2024 doubled from 2023** (36,182 to 75,246) before Cosmos existed. CTC may point to that as organic growth. If it came from the ticketing platform change or new brand volume, have that explanation ready. It doesn't weaken the 113x figure, but you don't want to be caught without an answer.

### SCOTT (2026-09-23T14:42)
again when we first fired it off, there were alot of turn it on and then turn it back off instances.  not worht digign in to the specifics  the story is there and is obviosu, cosmos is blowing up our tickets making it hard to know what to work and when and how to propeorly servie our customers

### CLAUDE (2026-09-23T14:42)

The email now opens on the customer-service problem. The numbers are down to one baseline comparison, and the 2025 on/off history is a single line with no specifics. The asks and the October 9 deadline haven't changed.

### SCOTT (2026-09-23T14:46)
one slight change, we are turning off the integration now.  ctc doesnt know but my team is working on a replacment now and these mass tickets effects our inttgrateon to our new ticketing system.  it takes abiut 3 hours to ingest 10K tickets into our new system.  at the current ticket generation rate, we will never get them all in.

### CLAUDE (2026-09-23T14:46)

The email is now a notice that the integration is off, not a threat to turn it off. The replacement system and the ingestion problem stay out of it. It gives the operational reason, which is true and defensible on its own. I dropped the remediation-plan and volume-target asks, since you don't want CTC scoping work on a platform you're leaving. The root-cause ask stays because it puts the failure on the record.

Your ingestion math doesn't support "never," though:

- **Capacity at 10K per 3 hours:** about 80K/day if it runs around the clock.
- **Current generation rate:** September is running about 14.9K/day (341,649 over 23 days), and August averaged about 22.9K/day. Either way you're well under capacity, and with the integration off the rate drops to near baseline.
- **The real problem is the backlog.** 2026 YTD alone (2.3M) is about 690 hours, or roughly 29 days of nonstop ingestion. All-time (3.07M) is about 38 days.

The better move is to not migrate the Cosmos junk at all. Filter out tickets where Requester = CAS Integration and the ticket was closed with no agent action, and ingest only human and actionable history. That likely cuts the backlog by 90%+. It also keeps your new system's reporting from starting out as polluted as the current one. Settle this with Dan before the migration plan hardens.

Two more things before you send:

- **PNOC coverage.** Make sure manual coverage is actually staffed before the switch goes off, not after. The first missed outage after you disable the integration becomes CTC's story, not yours. That's why I added the September 25 coverage confirmation.
- **Tell Jady first.** This is a unilateral change to a CTC-provided service in the middle of a dispute. He'll want to hear it from you before Josh calls him.

### SCOTT (2026-09-23T14:50)
the cosmos to cas is both system they control.  that forst sentence needs to me directing them to turn it off

### CLAUDE (2026-09-23T14:50)
Replace the opening paragraph with:

> Please disable the Cosmos-to-CAS auto-ticketing integration effective immediately, and confirm in writing once it is complete. PNOC will return to manual ticket creation for validated alerts.

Everything else stands. Also add this as item 1 in the list and renumber the other two, so the confirmation has a deadline and a clear owner:

> 1. Today: written confirmation that the integration has been disabled, with the time it was turned off.

That timestamp also gives you a clean cutoff date for the migration filter.

### SCOTT (2026-09-23T14:56)
and maybe mention that we have had multipl critical cusotmers compalin that we are literraly shitting down their email serviers with the number of emails alertr they are getting, and one even threatened to file complaints against our domain.  if you search the other chats in this projhect, i think you will chats related to it. and that alsions assertion is that this is by design just isnt acceptable.  any system desinged to blow up my cusotmers email servers is not good design
[File uploaded: Re_ [EXTERNAL] RE_ Monitoring - Network Degradation - 47% Down - Embassy Suites Omaha Downtown Old Market - OMADT _ sev_2_high _ Open [2ZV777-VZY7R].pdf]

### CLAUDE (2026-09-23T14:57)

I couldn't find the domain-complaint thread in this project's chats, so that customer is unnamed in the draft. If you want it named, tell me who. Naming them makes it harder for CTC to dismiss, but only name them if they'd be comfortable showing up in CTC correspondence.

What the Omaha thread adds:

- **The email that set off Atrium's complaint was about an AP that came back up.** The Status field reads "Up." Every recovery event is generating a customer email, not just outages. That's why the draft calls out "including devices coming back up": it's the clearest evidence that the design is broken.
- **Alison's deflection doesn't hold.** She said Atrium also gets alerts directly from Meraki. Maybe so, but the email Jeanene forwarded came from BPRF Helpdesk on a CAS ticket. The draft points out that these emails come from our domain, without arguing with her directly.
- **I didn't name Alison.** "The response to Atrium" puts her position on the record without a personal callout to her leadership. Name her if you want the accountability to stick to her specifically.

One point for your file, not this email: "by design" is the same framing CTC used on Grand Hyatt Vail ("performed as designed"). In that RCA they also committed to a delivery date for flapping-ticket automation. If that date has passed, it's a strong line to add, because this Omaha ticket is exactly the flapping behavior they committed to fix. It's also a direct tie to the Vail compliance record, so check with Jady before connecting the two in writing.

### SCOTT (2026-09-23T15:02)
heres the compaint email.  and the atrium is the other one
[File uploaded: RE_ [EXTERNAL] RE_ Monitoring - AP Down - TownePlace_Suites_Fayetteville - FAYTS _ Open [PXY5W9-G727N].pdf]

### CLAUDE (2026-09-23T15:03)

Both threads are in the draft. Renodis is the lead example because it has the full record: six weeks of escalations, specific volumes, and two written threats to file a domain complaint. Your September 9 question to Alison is now on the record next to the "by design" response.

Before you send:

- **The Renodis root cause cuts both ways.** Alison's September 8 analysis found two problems on our side: APs in Salesforce weren't marked Production, and it's unclear whether Dan's Salesforce-to-Cosmos sync script is still running. If this goes to Josh, he'll point there. That's why the draft doesn't call the Renodis alerts false or blame Cosmos for the bad data. The argument rests on design: no monitoring system should send 5,000 emails in 24 hours for one property, whatever data it's fed. Close out Dan's and Cedrich's action items before you send, so a CTC reply can't turn this into a Salesforce hygiene argument.
- **Has anyone called Zachary?** He asked for an executive contact on September 8. The last response on that thread is Aaron's holding note from July 29, and Zachary's complaint that no one had replied is in writing. If no executive has called him, that call matters more than this email, and it should happen today. The draft says he "demanded executive contact," so CTC could ask whether you delivered it.
- **I left out Andras's rwc600 hardware upgrade.** Putting it in this email would invite a funding conversation on a platform you're replacing. If CTC raises it as the fix, decline it on a separate thread.

### SCOTT (2026-09-23T15:13)
sent.  now i need to forward it to jady with a note.  i was thinking something like:

Below as an fyi.  The COSMOS replacement and the CAS/Zendesk replacement are slated to be ready for our review by the end of October. 
 
I do not intend to allow CallTek to reenable the auto-ticketing. Its been over 5 years. COSOMS is never going to be a production-ready system.
 
As we discussed, we are targeting a late November/early December cutover away from the CTC mitel phone to the Hosted Vice syste that we contro, hopefully while I am on-site in the Philippiens to ensure that it goes smoothly.
 
This sets us up to plan for a Q1 migration away from CallTek.  I think you have been saying it for a while, but probably due to my affection for my CTC team and their years of loyalty and dedication to our account, I have been holding out hope that CTC leadership would come to their senses and turn that ship around.  Sadily, I think it is time to call it, and move toward a q1 exit.

### CLAUDE (2026-09-23T15:13)
I'd split this note. Send the facts and timeline in writing, and make the exit call and "never re-enable" position in person. Three reasons:

- **It contradicts the email you just sent.** You told CTC that re-enabling depends on reviewing their root-cause analysis. A note on the same thread saying you'll never allow it makes that ask look like a pretext. If Josh's dispute ends up with lawyers involved (and the non-compete fight already has counsel on it), this is exactly the thread that gets pulled.
- **Exit intent and your read on CTC leadership are what your own rules keep verbal.** A forward can get forwarded again, and this one is attached to a CTC-facing email.
- **The personal part will land better said out loud.** Telling Jady he was right, and that loyalty to your team kept you holding out, is a good relationship moment. It doesn't need to sit in email.

Also check the "over 5 years" figure. Auto-ticketing went live in mid/late 2025, so if Josh ever sees that number, he'll dispute it. If you mean Cosmos's total development time, say that verbally.

Here's the written version:

> Jady,
>
> FYI below. I've directed CTC to disable Cosmos auto-ticketing effective today, following repeated customer escalations, including a threatened abuse complaint against our domain from Renodis.
>
> Timeline on our side:
> - Monitoring and ticketing replacements: ready for our review by end of October
> - Telephony cutover from the CTC Mitel platform to our hosted voice system: targeting late November/early December, ideally while I'm on-site in the Philippines
>
> I'd like 30 minutes this week to walk through next steps.
>
> Scott

In the 30 minutes, cover the rest verbally: no re-enable, the Q1 exit decision, and that he was right. The dates in the note already make the case for Q1 without saying it.

### SCOTT (2026-09-23T15:18)
the agreement with ctc to devleop cosmos was signed the summer before i started with the company.  i started in sept of 2022. see attached. it took them until end of 2025 to get it finsished ad deployed.  this email is to jady my leadrer only.
[File uploaded: SOW - COSMOS NMS_BPRF_signed060221.pdf]

### CLAUDE (2026-09-23T15:18)
Your "over 5 years" is right. The SOW was signed June 2, 2021, with a 45-day estimated completion (mid-July 2021). It went live at the end of 2025, about 4.5 years late, and September 2026 is 5+ years from signing. Here's the note:

> Jady,
>
> Below as an FYI. I've directed CTC to disable Cosmos auto-ticketing effective immediately.
>
> Our replacements for Cosmos and for CAS/Zendesk are slated to be ready for our review by the end of October. I do not intend to let CallTek re-enable auto-ticketing. The Cosmos SOW was signed in June 2021 with a 45-day estimated completion. It didn't reach deployment until late 2025, and more than five years after signing it still isn't production-ready. I don't believe it ever will be.
>
> As we discussed, we're targeting a late November/early December cutover from the CTC Mitel phone system to the hosted voice system we control, ideally while I'm on-site in the Philippines to make sure it goes smoothly.
>
> That sets us up for a Q1 migration away from CallTek. You've been saying it for a while. My affection for my CTC team and their years of loyalty to our account kept me hoping CTC leadership would turn the ship around. Sadly, I think it's time to call it and move toward a Q1 exit.
>
> Scott

Attach the SOW. It adds two things the note doesn't spell out:

- **The SOW commits CTC to scanning 100K devices in 15 minutes.** Andras's rwc600 server is timing out at 26K. So the hardware upgrade Alison raised should be CTC's cost to meet a commitment they already made, not a new BPRF spend.
- **CAS alarm management is in the contracted scope.** The ticket-flooding behavior is a defect in something CTC was already paid to build, not a feature request.
