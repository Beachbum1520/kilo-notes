# Protecting employee emails from web scrapers
Date: 2026-05-05
Conversation: b0b5f7ac-038b-42a0-841a-4418807b2b61
Domain: business-ops

## Summary
**Conversation Overview**

The person, who appears to be in a leadership or management role at Blueprint RF (a Cox Communications company), was responding to an internal email thread about a Marriott client request. Marriott had asked Blueprint RF to update their public-facing website to include an escalation contact path, referencing a competitor (Allbridge) as an example. The person had security and privacy concerns about posting individual names, phone numbers, and email addresses on a public webpage and asked Claude to help rewrite their internal reply email, expand on their bot-harvesting concern with supporting statistics, and advise on whether Cox Security needed to be looped in.

Claude rewrote the reply email in a professional tone that acknowledged Marriott's intent while presenting a data-backed case against public posting, citing Imperva's 2025 Bad Bot Report (37% of global internet traffic from malicious bots, rising for six consecutive years). The email proposed routing the escalation path content behind the existing authenticated Customer Portal as an alternative, and included a directed ask to Par Bayat (the email's original author, identified as Hospitality Support Manager at Blueprint RF) to verify whether the Marriott LSP agreement explicitly requires public-facing posting. Other colleagues mentioned in the thread include Carigan Bennett, Steve Clark, Scott Watts, and Kyle Davis, with Julian Cayetano on CC.

On the question of looping in Cox Security, Claude advised that this decision — moving content off a public page and behind an existing login — likely does not require Security involvement since it reduces rather than expands exposure. However, Claude flagged that a courtesy notification may be appropriate if the Customer Portal is hosted on Cox infrastructure, and that the more pressing escalation is a Legal/Contracts review to determine what the Marriott agreement actually requires before any action is taken.

### SCOTT (2026-05-05T13:11)
Help me re-word and re-write this email.  if my laim about the robo-callers and spam collectors is rigth, lets expand on it a bit.  any stats to this wouyld be helpful. The attache screen shot from Allbridge is one of our competitiprs.  the other two screen shots are from our website

Looks pretty specific to me.  I do not like the idea of having individual names and emails on a forward-facing web server.  Web crawlers and other bots scour the internet for just this sort of thing, to then sell to the robo-callers, and the spam vendors.  We have a link to the customer portal on our website, I would be fine with posting behind that login.  Is there anything in our agreements that says we have to do this? 
   
From: Bayat, Par (CCI-Bluprint RF) <par.bayat@blueprintrf.com> 
Sent: Tuesday, May 5, 2026 8:33 AM
To: Bennett, Carigan (CCI-Atlanta) <carigan.bennett@cox.com>; Clark, Steve (CCI-Southeast) <Steve.Clark@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>
Cc: Cayetano, Julian (CCI-Bluprint RF) <Julian.Cayetano@blueprintrf.com>
Subject: Blueprint RF Marriott Site
Good afternoon, everyone
Marriott has requested that we update our website to include the BPRF escalation path.
 
As a reference, they provided an example from another LSP page to ensure we are aligned with their request.
 
@Watts, Scott (CCI-Blueprint RF) @Davis, Kyle (Blueprint RF), do you approve us pasting the escalation path details directly onto the site as requested by Marriott?
Regards,
 	 	Par Bayat
Hospitality Support Manager
Blueprint RF
CCI - Blueprint RF
Cell: (470) 374-3860
Leave Us a Google Review
 
Follow Us on LinkedIn
PTO Notice:   5/22/2026
Travel Notice: 5/26/2026 -> 5/29/2026 (Marriott Connect Conference)
[File uploaded: 1777986586729_image.png]
[File uploaded: 1777986616129_image.png]
[File uploaded: 1777986621709_image.png]

### CLAUDE (2026-05-05T13:11)

Your instinct is well-founded and the data backs it up strongly. Here's the rewritten reply:

---

Your instinct is 100% correct. A few supporting data points I wove into the email:

- According to Imperva's 2025 Bad Bot Report, bots accounted for 51% of all global web traffic in 2024 — the first time automated activity has outnumbered humans in a decade. Bad bots specifically made up 37% of all traffic.
- Email harvesting bots scan webpages looking for text that follows the email address format and copy it directly into spammer databases. This is not theoretical — it happens constantly and automatically.
- Bad bot traffic has risen for six consecutive years, up from 32% in 2023 to 37% in 2024.

The email takes a firm but constructive position: you're not blocking Marriott's request, you're redirecting it to a smarter solution you already own (the Customer Portal). The ask to Par to verify whether the agreement actually *requires* public posting is the right move — Marriott may have just pointed to Allbridge as a reference without mandating that exact approach.

### SCOTT (2026-05-05T13:13)
and would we need to loop in cox secirty before making this change?

### CLAUDE (2026-05-05T13:13)
 Good instinct to ask. Short answer: **probably not for this specific decision**, but here's the honest breakdown.

**Why Cox Security likely doesn't need to be looped in:**
- You're not changing any system architecture, firewall rules, or network configuration
- You're moving content *off* a public page and *behind* an existing authenticated portal — that's a reduction in exposure, not an expansion
- This is a content/editorial decision, not an IT security change

**Why you might want to give them a heads-up anyway:**
- If the Customer Portal is hosted on Cox infrastructure or subject to Cox's data governance policies, they may have an interest in what PII is stored behind it
- If Marriott pushes back and escalates to a formal contractual dispute, having Cox Security aware of your reasoning (and the bot harvesting rationale) could be useful CYA
- Cox may already have policies about what contact information can and cannot be publicly posted on vendor/partner sites — worth a quick check

**The more important loop-in is probably Legal/Contracts**, not Security. The real question is what your LSP agreement with Marriott actually says. If there's language requiring "publicly accessible" escalation information, that's a contract issue before it's a security issue. Par needs to pull that thread first.

**Bottom line:** Notify Cox Security as a courtesy if the portal sits on their infrastructure, but don't let it slow the decision down. The contract review is the actual gating item here.
