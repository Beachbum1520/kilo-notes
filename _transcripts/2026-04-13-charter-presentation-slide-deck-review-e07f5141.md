# Charter presentation slide deck review
Date: 2026-04-13
Conversation: e07f5141-9b44-42b3-9722-2319954325d1
Domain: business-ops

## Summary
**Conversation Overview**

Scott Watts (Senior Director, Hospitality Operations at Blueprint RF) worked with Claude on two interconnected work streams: reviewing and improving an existing Cosmos platform presentation for Charter, and building a brand-new executive-level presentation responding to a specific Charter due diligence question (SB-1119, Item 2360): "Please provide national brand trouble call monitoring certification requirements used by CB Customer Ops." Scott noted his boss directed him not to wait for clarification on this question but to answer it proactively, and framed the entire effort as high-stakes, describing it as effectively a job interview situation with Charter senior leadership.

The Cosmos deck review (Cosmos_BPRF_4_2026.pptx) resulted in detailed feedback organized by priority (critical/must fix, should fix, nice to have), covering typos ("Salesfore," "Monitioring"), a duplicate slide 9, missing slide context and descriptions, cut-off text, and structural gaps like missing agenda and closing slides. Scott requested this feedback formatted as a copy-paste-ready team email, signed from him. For the Charter response, Scott uploaded extensive supporting materials including three brand overview decks (Marriott, Hilton, Hyatt), a zip archive of national brand standards documentation across all major brands Blueprint RF serves (Marriott, Hilton, Hyatt, Choice, Wyndham, Omni), and internal team email threads. Claude ingested all materials and built a polished 8-slide PowerPoint presentation (ManagedWiFi_Charter_Overview.pptx) using PptxGenJS, designed to serve as the standalone formal response to Charter. The deck's narrative arc was carefully calibrated to Scott's explicit strategic goal: make managed Wi-Fi seem valuable and complex enough to warrant partnership and investment, but not so overwhelming that Charter would walk away, and not so simple that they'd think they could absorb it without Blueprint RF.

Key colleagues mentioned: Jady (Scott's boss, who engaged others when Scott was unexpectedly out for a personal matter), Kyle, Marie, and Julian Cayetano (Manager, Technical Customer Care — three of Scott's direct reports), Megan (interpreted the Charter question in the email thread), and Dan (provided technical architecture detail on Cosmos). The final deliverable included Scott and Julian as named points of contact on the closing slide. Scott also requested a team email to Jady (To:) with Kyle, Marie, and Julian (CC:) attaching the draft deck, explicitly asking the team to prioritize review the same day the email would send (12:30am ET on the 14th) given Jady's April 15th deadline. Scott's communication style is informal and fast-moving in his own messages but expects professional, structured output in deliverables and emails drafted on his behalf. He prefers Claude to ingest materials fully before producing output, and explicitly said so multiple times during the session.

**Tool Knowledge**

For PPTX creation, PptxGenJS was used via Node.js (`node build_deck.js`) and does not support loading or modifying existing `.pptx` files — when edits were needed to an already-generated deck, the full build script had to be re-run with modifications. The reliable pipeline for visual QA was: PptxGenJS generates `.pptx` → `soffice.py --headless --convert-to pdf` converts to PDF → `pdftoppm -jpeg -r 130` converts PDF pages to per-slide JPEGs for review. Text extraction from uploaded `.pptx` files used `python -m markitdown [file]`. The skills file at `/mnt/skills/public/pptx/SKILL.md` and `/mnt/skills/public/pptx/pptxgenjs.md` provided creation guidance. When inserting new slides into an existing build script, Python string replacement (`str.replace`) on the raw `.js` file was used to inject slide code blocks before the `pres.writeFile()` call, which proved more reliable than attempting in-place edits with the `str_replace` tool when the target string contained special characters.

### SCOTT (2026-04-13T23:10)
attached is a ppt i have to give to charter.  also attached is the thread to my team on it.  i am way behind.  review and givre me other feedback pn the slide deck

[Attachment: ]
Slide 2 – I thought the asset database was Salesforce, and we pushed/pulled into Cosmos to reconcile?  i.e., Salesforce is our source of truth, not Cosmos.

Some rando details I picked up from covo’s with Dan that I think we should include in this slide about what Cosmos is:: 
•	dg agent is a collection of Python/bash
•	the GUI is JavaScript using React framework(i believe), sitting on an nginx webserver, serving up information stored in a PostgreSQL DB

Slide 3 and 4 – I think we need the title to better reflect what these screenshots are of.  I assume this is the NOC agent Montori dashboard?

Slide 5 – need a title and or description.  I.e., is this daily availability report for a specific property?  Can it be run for an entire brand, an entire management company, a range of dates, etc., etc.? 

•	it looks like their code is php, JavaScript, jquery, etc .

•	Where do pollers run?  The agents run on each of the DGs (and NUC devices of non-DG GW sites). It does the SNMP walks and pings. It then sends the results back to the DB via API to the Postgres DB running on our server in QTS.  The DGs do nothing more than that function.  No alerting, etc is done here.  It's strictly gather data and pass it back to the central server.  
•	Where does alert logic execute?  The alert logic would run on the central server in QTS.
•	Do we have DB backups and restore-tested copies? Yes, this is in place.
•	Is business logic (thresholds, suppression rules) stored in DB tables or hard-coded?  I haven't seen their code but i'm sure it's in both places.  The DB would hold the setting while the server code took those thresholds and did the checks

From: Cayetano, Julian (CCI-Bluprint RF) <Julian.Cayetano@blueprintrf.com> 
Sent: Tuesday, April 7, 2026 6:17 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Apa, Dan (CCI-Bluprint RF) <dan.apa@blueprintrf.com>
Subject: RE: IRL | 2361, 2363

Hope this works for you.

Regards,
Julian C
Blueprint RF
404-269-1525
jcayetano@blueprintrf.com

From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Tuesday, April 7, 2026 12:13 PM
To: Apa, Dan (CCI-Bluprint RF) <dan.apa@blueprintrf.com>; Cayetano, Julian (CCI-Bluprint RF) <Julian.Cayetano@blueprintrf.com>
Subject: RE: IRL | 2361, 2363

Do you two have this task?  Can I get an ETA?

From: Watts, Scott (CCI-Blueprint RF) 
Sent: Friday, April 3, 2026 10:07 AM
To: Apa, Dan (CCI-Bluprint RF) <dan.apa@blueprintrf.com>; Cayetano, Julian (CCI-Bluprint RF) <Julian.Cayetano@blueprintrf.com>
Subject: FW: IRL | 2361, 2363

See below.  Can you two take this on?  I’d like to review before it is submitted to the Charter folks.

Thanks,
scott

From: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com> 
Sent: Thursday, April 2, 2026 4:17 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Riley, Jordan (CCI-Atlanta) <Jordan.Riley@cox.com>
Cc: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Subject: RE: IRL | 2361, 2363

Scott, would it be possible for someone to record a demo/overview of Cosmos?  I suspect that might come closer to what they are looking for and could avoid you having to do a demo on a call with them.  We’re trying to same people time on our side by starting to record demos and that also allows us to create a resource that we can point others to in the future if needed.  

I’m going to roll 2360 into this thread also – To your clarification questions “Are you asking about the contracted requirements from the national brands we serve regarding our proactive monitoring of all IP endpoints? Or the actual call-monitoring requirements for my call center agents (call recording, ticketing, etc.)? Or something else completely?”

Charter asked the question and we can certainly clarify with them.  However, my guess is that with 2360 they are looking for the national brand requirements they have of us and how we perform against those.  Our performance may be covered in the document you sent to respond to Question #2363.  If you can share what the brands require of us, we can submit and let them tell us if they need someone different or more.   

2360 (Commercial Business)
Question:
Cox Business – Follow up to 3/3 meeting SB 1119: Please provide national brand trouble call monitoring certification requirements used by CB Customer Ops.

From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Thursday, April 2, 2026 3:16 PM
To: Riley, Jordan (CCI-Atlanta) <Jordan.Riley@cox.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>
Subject: RE: IRL | 2361, 2363

Hi Jordan,

Here is a screen grab of the COMOS overview. Let me know if this is enough for you.
 

Also attached is our latest scorecard for the call center.  Let me know if you have any questions.

Thanks,

Scott Watts
Senior Director, Hospitality Operations
Email: scott.watts@blueprintrf.com
 
          
 
Book time with Watts, Scott (CCI-Blueprint RF) 
 
 

From: Riley, Jordan (CCI-Atlanta) <Jordan.Riley@cox.com> 
Sent: Thursday, April 2, 2026 2:20 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Subject: IRL | 2361, 2363

Hi Scott,

We have identified you as the owner of the questions below. Can you please confirm you are the owner and confirm if you can complete by the expected SLA date of 4/20?

Thanks,
Jordan

________________________________________
2361 (Commercial Business)
Question:
Cox Business – Follow up to 3/3 meeting SB 1119: Please provide an overview of the Cosmos monitoring platform used by Customer Ops.
Please upload answers to folder 7.4, “Cox Business and Hospitality Network.”
Update / Notes:

________________________________________
2363 (Commercial Business)
Question:
Blueprint RF – Follow up to 3/3 meeting SB 1119: Please provide the monthly SLA scorecard for the Blueprint RF call center.
Please upload answers to folder 7.4, “Cox Business and Hospitality Network.”
Update / Notes:

[File uploaded: Cosmos BPRF 4.2026.pptx]
[File uploaded: ]

### CLAUDE (2026-04-13T23:12)

Good — I've now reviewed all 9 slides alongside the email thread. Here's a thorough breakdown of every issue I see:

---

## Overall Feedback

The deck is a solid start — the content is genuinely strong and the visuals are good. But there are several issues that need to be fixed before sending to Charter, ranging from factual errors to structural problems.

---

### 🔴 Critical / Must Fix

**Slide 2 — "Salesfore" typo + wrong framing of the database**
The slide says "a central database like Salesforce" — two problems. First, "Salesforce" is misspelled as "Salesfore" (visible in the slide text). Second, your team's note is clear: Salesforce IS the source of truth, not a generic example. The wording should reflect that Cosmos syncs to/from Salesforce (or pulls from it), not that it uses "a database like Salesforce." This is a factual accuracy issue that could raise eyebrows with Charter.

**Slide 9 — Appears to be a duplicate of Slide 2**
Slide 9 has the exact same diagram and text as Slide 2, titled "continued." This looks like an accident. Either it was meant to be something else or it shouldn't be there. Remove or replace it.

**Slides 3 & 4 — Generic title "Device Monitoring" on both; no context**
As your team flagged, these screenshots need more descriptive titles. Based on what I can see: Slide 3 appears to be the **NOC Agent/Montori dashboard for a specific property** (Courtyard Atlanta Buckhead). Slide 4 shows the **device inventory list view in Cosmos**. Retitle them accordingly, e.g., *"Cosmos NOC Dashboard – Property View"* and *"Cosmos Device Inventory View."*

**Slide 5 — No context or description**
The title just says "Reporting" but the report shown is clearly a **site-level availability report for Courtyard Atlanta Buckhead** for a specific date range. Add a description explaining: what the report shows, whether it can be run by brand/management company/date range, and what audience it's designed for. This is a key question Charter will have.

**Slide 3 — "Monitioring" typo in the title**
The slide title reads "Device **Monitioring**" — fix the spelling.

---

### 🟡 Should Fix

**Slide 8 — "continued" is not a title**
The slide title just says "continued." It should reflect the actual content: something like *"NOC Triage & Escalation Workflow."* Same issue on Slide 9.

**Slide 8 — Text gets cut off at the bottom**
The last line of text on Slide 8 ("Resolution or Replacement: Final closure of the...") is cut off by the blueprintrf.com footer. The text box runs into the footer. Fix the text box height or reduce font size.

**Slide 6 — Stray asterisk in body text**
The "Hierarchical Suppression" bullet reads: "* System recognizes network topology." The asterisk at the start is a formatting artifact — remove it.

**Slide 2/9 — Technical architecture details missing**
Per Dan's input in the email thread, you have real detail you could add to enrich Slide 2: the DG agent is Python/bash, the GUI is React/JavaScript on nginx, and the data is stored in PostgreSQL. The polling agents run on the DGs (and NUC devices for non-DG sites), send results via API to PostgreSQL at QTS, and all alerting logic runs centrally at QTS. This kind of architectural detail would strengthen the deck significantly for a technical audience like Charter.

---

### 🟢 Minor / Polish

**Slide 7 — Title wraps over the diagram**
The title "Cosmos Generated Ticket - Percent Down Criteria" is two lines and overlaps slightly with the diagram below. Consider abbreviating or resizing.

**Slide 1 — "BPRF COSMOS" is not a great title for an external audience**
Charter may not know what "BPRF" means. Consider spelling it out: "Blueprint RF Cosmos" or simply "Cosmos – Device Monitoring, Alerting & Escalation Workflow."

**General — No agenda or table of contents**
This is going to Charter as a formal deliverable (IRL question 2361). A brief agenda slide after the title showing the 4-5 topics covered would make it more professional.

**General — No closing slide**
There's no summary or "thank you / questions" slide. For a Charter submission, at minimum add a closing slide with contact info.

---

### Summary of Actions Needed

| Priority | Slide | Fix |
|---|---|---|
| 🔴 | 2 | Fix "Salesfore" typo; clarify Salesforce is the source of truth |
| 🔴 | 9 | Remove or replace duplicate slide |
| 🔴 | 3 & 4 | Add descriptive titles |
| 🔴 | 3 | Fix "Monitioring" typo |
| 🔴 | 5 | Add description of report scope/capabilities |
| 🟡 | 8 | Fix title; fix text cutoff |
| 🟡 | 6 | Remove stray asterisk |
| 🟡 | 2 | Add technical architecture details from Dan |
| 🟢 | 1 | Spell out "BPRF" |
| 🟢 | All | Add agenda slide + closing slide |

Want me to go ahead and make these edits directly to the PowerPoint file?
[File uploaded: slide-1.jpg]
[File uploaded: slide-2.jpg]
[File uploaded: slide-3.jpg]
[File uploaded: slide-4.jpg]
[File uploaded: slide-5.jpg]
[File uploaded: slide-6.jpg]
[File uploaded: slide-7.jpg]
[File uploaded: slide-8.jpg]
[File uploaded: slide-9.jpg]

### SCOTT (2026-04-13T23:14)
give me the feedback in a copy and paste format that I can put into the email

### CLAUDE (2026-04-13T23:14)

There you go — ready to copy and paste. I signed it "Scott" based on the thread, but adjust as needed. Everything is grouped by priority so your team knows what's blocking submission vs. what's just polish.

### SCOTT (2026-04-13T23:28)
here is a spin off thread on thios. re: sb-1119 that is alos refernced int he other thread.  read this and the other thread abut my clariifcation requests.  I hav ea bunch more to upload here for you to helo me with my rpely, so don;t wat time formatting reply yert.  just ingest the docs.  My leader told me to not wait on the clarificatiob, but instaed tell them what I think they eed to know here.
[File uploaded: 1776122845590_image.png]

### CLAUDE (2026-04-13T23:28)
 Got it. I've ingested question 2360 — Charter is asking for the national brand trouble call monitoring certification requirements used by CB Customer Ops.

I also have the full context from the earlier thread, including Megan's interpretation that Charter likely wants to know what the national brands require of you and how you perform against those requirements.

Go ahead and upload the rest of the docs and I'll hold off on drafting anything until you're ready.

### SCOTT (2026-04-13T23:31)
here are 3 slide decks my team came up with for a priort meetign trying to summarize the three major brands we serve and the uniquiness created by their stnadards we have to adhere to.  ingest this.  still no feedback yet.  more to come
[File uploaded: HILTON Overview.pptx]
[File uploaded: HYATT Overview.pdf]
[File uploaded: Marriott Overview & 5 Management Companies.pptx]

### CLAUDE (2026-04-13T23:31)
 Ingested all three. Here's what I've captured:

**Hyatt** — Standards & Implementation Guide (March 2026). Key requirements: Approved Product List (Ruckus, Cisco, Aruba), Wi-Fi 6E/7 + Cat6A, symmetrical fiber (20–50Mbps+ depending on brand tier), Hyatt-approved NMS reporting to corporate dashboards, Brand Excellence Audits, 24/7/365 monitoring with 4-hour onsite response for critical failures, 99.9% uptime on high-impact properties, WPA3 + VLAN separation, hardware refresh every 5–7 years.

**Hilton and Marriott** — text extraction needed since those are .pptx files I can't see inline. Let me grab those now.

All three fully ingested. Here's my summary of what I now have across all docs:

**Hilton** — Blueprint RF is a "Support Only" integrator (not a full approved integrator — important distinction). Cisco Meraki is the primary approved manufacturer for guest networks. Hilton uses ServiceNow for all sales/install process. Monthly SLA reports due by the 10th business day, reviewed on monthly calls. Weekly directives sent every Friday that BPRF must respond to. Brand Standard Audits at install and during network lifetime. Firewall rules and network config dictated by Hilton. BPRF supports 1,059 hotels / 141,319 guest rooms across 1,052 franchised + 7 managed sites.

**Marriott** — BPRF is one of only two vendors with a Marriott-approved proprietary gateway (the Dominion), deployed in 1,060+ properties. Reports due 5th of each month (contracted hotels, pending installs, gateways, helpdesk, incident, SLA, pricing, asset inventory). 90-day window from signature to install completion, Schedule 6/UAT due within 10 days of completion. Governed by GPNS firewall, switch, and wireless specs (IT-GPNS-006/007/008). BPRF supports 1,062 hotels / 135,235 guest rooms. Top 5 management companies breakdown also included (Aimbridge, Atrium, Tharaldson, MCR, and one more — 322 total properties, Marriott-dominant).

**Hyatt** — Approved Product List (Ruckus, Cisco, Aruba), Wi-Fi 6E/7 + Cat6A, 20–50Mbps+ symmetrical fiber, 24/7/365 monitoring, 4-hour onsite response, 99.9% uptime on high-impact sites, hardware refresh every 5–7 years, quarterly standards updates.

Ready for more uploads whenever you are.

### SCOTT (2026-04-13T23:37)
this is the big one.  these are the the majority if not all of the docs that define the brands standards for the various hotel brands we serve.  ingest all of this too.  take you time.  alot her to digest.  then I need either a word doc or power point that summarizes the natire of the managed wifi business serving the major hotel brands on a national scale.  these are senior level folks at Charter.  And my goal is to keep my job (my boss said treat all this as a job interview).  This manged wifi space is new territory to Charter, but is a space they are very interested in.  I want to cmmuncatie that is when properly funded and supporte,d this can a very profiutable space.  but that it does carry with it some unique requkrmets that charter proably hasnt seen before. i want them to be interested, but do not want what we do to seem so easy that they can easily absorb it into theoir large machoine.  or so complex that that juice aint worth the squezze.
[File uploaded: BPRF - National Brand Standards.zip]

### CLAUDE (2026-04-13T23:43)
 

Excellent — fully ingested. I now have a comprehensive picture across all brands. Let me build this deck.

All 7 slides look sharp. Copying to output now.

Here's your 7-slide deck. Here's the narrative arc, since you'll want to walk Charter through it:

**Slide 1 – Title.** Sets the tone: serious, polished, not a product brochure.

**Slide 2 – The Opportunity.** Opens with scale (3,000+ properties, 5 brands, 99.9% uptime required) and frames the key message upfront: this is not a commodity ISP play.

**Slide 3 – The Brand Ecosystem.** Marriott / Hilton / Hyatt side by side, with the specific compliance requirements each demands. Makes it immediately clear that each brand is its own universe.

**Slide 4 – What Compliance Actually Requires.** Six pillars (hardware, specs, security, monitoring, reporting, certification) with real specifics pulled from your brand docs. This is the "complexity is real but manageable" slide.

**Slide 5 – The Certified Integrator Advantage.** Left column: what it takes to operate. Right column: why that creates durable competitive moat. The Dominion gateway point (1 of only 2 Marriott-approved) lands well here.

**Slide 6 – What Proper Investment Unlocks.** The "fund us" slide — framed around operational infra, proprietary assets, and growth levers. Not a budget ask, just the strategic logic.

**Slide 7 – The Bottom Line.** Four numbered takeaways that close the loop cleanly.

One thing to fill in before you use it: **Slide 2 has "$XXM" for Annual Recurring Revenue** — you'll want to drop in the real number when you're ready.
[File uploaded: charter_slide-1.jpg]
[File uploaded: charter_slide-2.jpg]
[File uploaded: charter_slide-3.jpg]
[File uploaded: charter_slide-4.jpg]
[File uploaded: charter_slide-5.jpg]
[File uploaded: charter_slide-6.jpg]
[File uploaded: charter_slide-7.jpg]

### SCOTT (2026-04-13T23:53)
need to put this on the title slide.  And what about a POC slide at the end?  Me and Julain?

### CLAUDE (2026-04-13T23:53)
 Two quick questions before I build:

Also — what did you want to put on the title slide exactly? You said "need to put this on the title slide" but I don't see what "this" is referring to — did something not come through? And what are your and Julian's titles for the POC slide?

### SCOTT (2026-04-13T23:53)
[User dismissed — do not proceed, wait for next instruction]

### CLAUDE (2026-04-13T23:53)
 Got it, standing by!

### SCOTT (2026-04-13T23:53)
this was the quetion as per the tracker
[File uploaded: 1776124415715_image.png]

### CLAUDE (2026-04-13T23:54)
 Got it — so the full question is:

**"Please provide national brand trouble call monitoring certification requirements used by CB Customer Ops."**

And Megan's read (which your boss agrees with — don't wait for clarification, just answer it) is that Charter wants to know **what the national brands require of BPRF** in terms of monitoring/SLA/trouble call standards, and how BPRF performs against those.

Based on everything you've uploaded, you actually have a very strong answer to this sitting in your docs already. The deck I built covers a lot of it visually, but for the formal IRL response you'll need a written reply to drop into the tracker.

Want me to draft that written response for question 2360 now? I can pull the specific monitoring/SLA/reporting requirements from each brand's docs (Marriott's GPNS reporting specs, Hilton's SLA report requirements, Hyatt's 24/7 monitoring and 4-hour response mandates, etc.) and frame it as a direct answer to what Charter is asking — referencing the deck as a supporting attachment.

### SCOTT (2026-04-13T23:54)
i want the presentation to be the repsonse

### CLAUDE (2026-04-13T23:54)
 Perfect — clean and simple. So the play is:

1. The deck *is* the answer to 2360
2. You upload it to folder 7.4 in the Charter tracker
3. Your written response in the tracker is just a one-liner pointing to it

Want me to draft that one-liner tracker response for you? Something like: *"Please see the attached overview of national brand monitoring certification requirements and BPRF's compliance framework across Marriott, Hilton, Hyatt, Choice, Wyndham, and Omni."*

And separately — still need to know what you wanted to add to the title slide (your image came through but I couldn't see what "this" was referring to), and the POC slide details for you and Julian. What are your titles and contact info?

### SCOTT (2026-04-13T23:55)
i want the title slide to include the exact question we are answering

### CLAUDE (2026-04-13T23:55)
 Got it. So the title slide subtitle/descriptor becomes:

**"Cox Business – Follow up to 3/3 meeting SB-1119: Please provide national brand trouble call monitoring certification requirements used by CB Customer Ops."**

Want me to work that in cleanly — probably as a smaller line below the current subtitle, maybe in that muted blue color — and then also add the POC slide? Still need your and Julian's details (titles, email, phone) for that last slide.

### SCOTT (2026-04-13T23:57)
yes. to the title slide.  Here are mine and Julian's details for the contact slide at the ned:

Scott Watts
Senior Director, Hospitality Operations
Email: scott.watts@blueprintrf.com

Julian Cayetano
Manager, Technical Customer Care
julian.cayetano@blueprintrf.com

### CLAUDE (2026-04-13T23:59)

PptxGenJS can't load existing files, so I'll rebuild the full deck with the two changes baked in — title slide update and new POC slide at the end.

Now add the POC slide before writeFile:

Both look great. Copying the final file.

Done — 8 slides total. Title slide now clearly calls out SB-1119 Item 2360 and the exact Charter question, and the POC slide closes it out cleanly with you and Julian. This is ready to upload to folder 7.4.
[File uploaded: charter_slide-1.jpg]
[File uploaded: charter_slide-8.jpg]

### SCOTT (2026-04-14T00:28)
My boss wrapped others into this when he thought I was out for a family emergency today.  Help with an email to the team with my draft, soliciting feedback,  ia m goign to attached the presso we did as a draft
[File uploaded: 1776126464311_image.png]

### CLAUDE (2026-04-14T00:28)

There you go. I kept it professional but matter-of-fact — no over-explaining about the family emergency, just focused on the work. Jady and the others are cc'd on the original thread so they'll have context.

One thing to note: the deadline is **April 15th — that's Tuesday, two days away**, so you're in good shape to get feedback tomorrow and still submit on time.

### SCOTT (2026-04-14T00:29)
the email is the Jayd, with Kyle, Julain and Marie (3 of my direct rpeorts) on cc

### CLAUDE (2026-04-14T00:29)
 Got it — Jady is the "To" and your three directs are on CC.

There you go — Jady is addressed directly, your three directs are implied as CC recipients. It defers to Jady for alignment first (since she's your boss's contact) and then routes the detailed feedback through your team. Clean chain of command.

### SCOTT (2026-04-14T00:30)
this email will go out at 12:30am ET on the 14th.  tell Kyle, Marie and Julain to priotize reviwewing and feedback today to in ordere to meet Jafdy deadline of the 15th

### CLAUDE (2026-04-14T00:30)
 

Done. The urgency is clear to your team without being alarmist — and it's framed around Jady's deadline rather than sounding like you're panicking. Good luck, Scott — you've put together a strong package tonight.
