# Centralizing sales reporting from our Salesforce
Date: 2026-09-09
Conversation: 4e1d9b77-00ad-4cd7-9d6d-c9ca2ce59231
Domain: business-ops

## Summary
**Conversation Overview**

Scott (at Blueprint RF, working with a partner organization called Spectrum) needed help drafting two pieces of professional communication related to a Salesforce reporting dispute. The core issue: Erik Nowak (a Spectrum-side contact) was building an automated report for Mark Kornegay (Jady West's new boss) that pulls opportunity and pipeline data from Spectrum's Salesforce instance rather than BPRF's, which Scott considers the authoritative source for opportunity counts and current sales stage. Scott's goal was to redirect the reporting source to BPRF Salesforce before the automation was finalized, and to position Par as the person who would own running the report going forward.

The first draft Claude produced was for a thread involving Jady West and Kathy Hatala — Scott clarified that was a separate communication and not what he needed. The actual ask was a direct, one-on-one reply to Erik's email with no CC recipients. Scott also corrected a factual error in Claude's draft: Claude had assumed Erik's report was pulling from BPRF's Salesforce, but Scott confirmed it was pulling from Spectrum's. Claude also included an unnecessary opening line ("Saw your note to Mark — nice work getting that moving") that Scott flagged as redundant given it's an in-thread reply; the final version drops the recap entirely and opens directly with the data-source flag.

Scott's consistent preference throughout was framing the ask around data integrity (single source of truth, avoiding drift) rather than ownership or control language, specifically to avoid appearing territorial if the message were forwarded. He also types quickly with significant typos and expects Claude to interpret and clean up without flagging each error.

### SCOTT (2026-09-09T15:37)
seebwlo thread.  i need to clesn up my reply.  i want to sae that we need to control the rpeorting, but dont want to say anythign that makes me appear territoiral if it gets forwarded.

I saw what Eric was sending.  It comes from their SF, not ours.  I am going to try and connect with him and convince him to let Par send the weekly report from our SF, not theirs.  Our SF is the soure of truth, especially when it comes to the number of opps and the current sales stage.
 
[@jady.west](mailto:jady.west@spectrum.com) – anything you can do to help effect this change will help us here.  I think it is important that we control the reporting up on this to the extent we can.
 
 
From: Hatala, Kathy <Kathy.Hatala@spectrum.com> 
Sent: Tuesday, September 8, 2026 3:50 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Cc: jady.west <jady.west@spectrum.com>
Subject: [EXTERNAL] Re: Dashboard or report
 
Per your email if you can take it from here Scott that would be great. Let me know how I can help as needed. 
 
Brian had an SE report of what has been logged to date by Spectrum reps - maybe useful until a dashboard can be created. Only issue was it could not be exported to excel was my understanding. 
 
Kathy 
 
From: Hatala, Kathy <[Kathy.Hatala@spectrum.com](mailto:Kathy.Hatala@spectrum.com)>
Sent: Tuesday, September 8, 2026 2:34 PM
To: McIntosh, Rachael <[Rachael.McIntosh@spectrum.com](mailto:Rachael.McIntosh@spectrum.com)>; Napier, Brian (CCI-Bluprint RF) <[brian.napier2@blueprintrf.com](mailto:brian.napier2@blueprintrf.com)>
Cc: Brissett, Lisa (CCI-Bluprint RF) <[lbrissett@blueprintrf.com](mailto:lbrissett@blueprintrf.com)>; amoore <[amoore@blueprintrf.com](mailto:amoore@blueprintrf.com)>; Watts, Scott (CCI-Blueprint RF) <[scott.watts@blueprintrf.com](mailto:scott.watts@blueprintrf.com)>
Subject: Re: Dashboard or report
 
Adding Scott Watts who was also on the Mark Kornegay email request. 
 
Scott - we met recently with Rachael and Brian to add a field for Spectrum sellers. 
 
This is still in development. 
 
I know Erik Nowak mentioned a dashboard he wanted to create. Can you ping him on this and let us know what needs to happen from our side? 
 
Kathy 
 
From: McIntosh, Rachael <[Rachael.McIntosh@spectrum.com](mailto:Rachael.McIntosh@spectrum.com)>
Sent: Tuesday, September 8, 2026 2:20 PM
To: Hatala, Kathy <[Kathy.Hatala@spectrum.com](mailto:Kathy.Hatala@spectrum.com)>; Napier, Brian (CCI-Bluprint RF) <[brian.napier2@blueprintrf.com](mailto:brian.napier2@blueprintrf.com)>
Cc: Brissett, Lisa (CCI-Bluprint RF) <[lbrissett@blueprintrf.com](mailto:lbrissett@blueprintrf.com)>; amoore <[amoore@blueprintrf.com](mailto:amoore@blueprintrf.com)>
Subject: Re: Dashboard or report
 
Once deployed your team will see these fields on Leads, Accounts, and Opportunities. Then they just select the right Spectrum folks from the list of contacts and we will be able to report against it.
 

 

Rachael McIntosh | Senior Manager, Operations | 
M: 404-316-4643 | O: 404-269-7170
6205 B Peachtree Dunwoody Rd | Atlanta, GA 30328
Book Time With Me: http://spectrumpn.info/callRachael
 
 
 
From: Hatala, Kathy <[Kathy.Hatala@spectrum.com](mailto:Kathy.Hatala@spectrum.com)>
Date: Tuesday, September 8, 2026 at 3:14 PM
To: McIntosh, Rachael <[Rachael.McIntosh@spectrum.com](mailto:Rachael.McIntosh@spectrum.com)>; Napier, Brian (CCI-Bluprint RF) <[brian.napier2@blueprintrf.com](mailto:brian.napier2@blueprintrf.com)>
Cc: Brissett, Lisa (CCI-Bluprint RF) <[lbrissett@blueprintrf.com](mailto:lbrissett@blueprintrf.com)>; amoore <[amoore@blueprintrf.com](mailto:amoore@blueprintrf.com)>
Subject: Dashboard or report
Mark Kornegay, Jady's new boss, asking for a dashboard or report from BPRF Salesforce we can get to show the opportunities created by L-Spectrum team. 
 
Thoughts? 
 
Kathy 
 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.

### CLAUDE (2026-09-09T15:37)
Here's a cleaned-up version that keeps your point but reframes it around data integrity rather than control — that's the version that survives a forward without reading as territorial:

---

Kathy – happy to take this from here.

I saw Erik's note on the dashboard. The report he's proposing would pull from Spectrum's Salesforce instance rather than ours. I'd like to get Par pulling the weekly report from the BPRF Salesforce instead, since that's where opportunity counts and sales stage are actually maintained and kept current — using a secondary source risks the numbers drifting out of sync with what's real. I'll reach out to Erik directly to work that out.

Jady – if you're able to help reinforce that BPRF Salesforce should be the source for this reporting, it'll help keep the numbers clean and consistent as this gets built out.

---

Why this version doesn't read as territorial: it never says "our system" vs. "their system" as a possession claim — it grounds the ask entirely in data accuracy (single source of truth, avoiding drift/duplication). That's a claim almost impossible to push back on and gives Jady something concrete and defensible to back you up on if forwarded up to Mark Kornegay. The original draft's "we need to control the reporting up on this" is the one line that reads as turf — I cut it entirely rather than soften it, since any version of "control" retains that flavor.

One thing worth deciding before you send: do you want to loop in Erik directly on this thread, or handle that as a separate 1:1 conversation first? Looping him in here puts it in writing in front of Jady and Kathy right away; a side conversation first gives him a chance to agree before it's visible to his chain.

### SCOTT (2026-09-09T15:38)
nope. that message is between jady, kathy and e.  now help ,e with a seaprte note to etric summarizing this.

### CLAUDE (2026-09-09T15:39)

Same logic as the internal note — data integrity framing, not a control claim — but adapted for a direct, collegial ask since Erik's the one who'd actually build the dashboard. It gives him an easy out to align before doing the work rather than after, which is the version he's more likely to say yes to.

### SCOTT (2026-09-09T15:40)
eric already knows all of this, see attached. 
Wanted to loop you in directly on something that came up on a thread with Kathy Hatala and Jady. Mark Kornegay (Jady's new boss) asked for a dashboard or report showing opportunities created by the Spectrum team, and I saw you'd mentioned building a dashboard for this."
[File uploaded: RE_ Cox CRM for Blueprint.pdf]

### CLAUDE (2026-09-09T15:41)
Good catch — that changes things. Erik's report is already pulling from "our" (BPRF) Salesforce, not Spectrum's. So the premise of the last draft — that you needed to convince him to switch sources — doesn't hold. He's already doing what you wanted; the open items now are just: get visibility/ownership into the automation he's building, and make sure Par is positioned as the one running it once it's live.

Here's a shorter note that drops the redundant summary and gets to that:

This keeps the same underlying goal — Par owning the reporting cadence — but reframes it as picking up the baton on something Erik already built correctly, rather than redirecting him. Cleaner, and it doesn't risk implying you missed that he was already on the right instance.

### SCOTT (2026-09-09T15:42)
no.  erics is not pulling from bprf's sf.  its pulling from spectrum.

### CLAUDE (2026-09-09T15:42)
Got it — thanks for the correction. That flips it back to the original concern: Erik's report is built on Spectrum's instance, not BPRF's, even though it says "our salesforce" (he's writing from Spectrum's seat). So the ask stands — you want this sourced from BPRF SF instead. Since he's already fully looped in on the thread, the note can be short and skip the recap:

Timing matters here too — he said he's automating a link in the next couple of days, so this lands before it's locked in rather than after.

### SCOTT (2026-09-09T15:43)
"Saw your note to Mark on the daily report — nice work getting that moving."

i am going to reply to his rmial.  nto cc anyone.  just him.  so dont really need this sentecne. nned a better intor

### CLAUDE (2026-09-09T15:43)

Goes straight to the flag since it's already in-thread with him — no context-setting needed.
