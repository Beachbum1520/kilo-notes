# Hyatt Grand Vail conversation
Date: 2026-07-22
Conversation: c54637d9-e2ce-4475-a32a-caa65c6f3291
Domain: business-ops

## Summary
**Conversation Overview**

Scott is working across multiple active vendor and operational threads, and this conversation focused on two interconnected issues at Grand Hyatt Vail involving their managed network services vendor, CallTek (operating through a platform called Cosmos), and a contact named Alison who serves as CallTek's point of contact for escalations. Scott's role appears to be on the operator/service delivery side of a company called BPRF, with Jady being a senior internal stakeholder he reports escalation strategy to, and Cedrich being a field technician (TDE side) who had previously done work at the property. Briggs Barggren is the IT Manager at Grand Hyatt Vail.

The core issue is a 68-day monitoring suppression failure at Grand Hyatt Vail (May 14–July 21), discovered through a conference group Wi-Fi incident. CallTek's own RCA confirmed that a misconfigured collectd agent caused a false core-down state on the Nomadix gateway, which triggered Cosmos's hierarchy suppression and killed automated ticketing for the entire property. During the outage window, two APs logged down events across seven dates with no tickets, and 649 WARNING-level packet loss events plus five FAILURE events generated no response until hotel staff called in on July 14. The PNOC had noted the core-down alert on May 14 and disregarded it, violating their own protocols. Scott asked Claude to draft and iteratively refine email replies to Alison, building a documented record that holds CallTek accountable using their own RCA language. The final reply rebutted Alison's "performed as designed" framing, quantified the suppression window and event log data, and formally demanded three written commitments: a fleet-wide Nomadix site audit with results, a committed delivery date for flapping ticket automation, and a defined detection standard for sustained WARNING-level degradation below the 15-minute offline threshold.

Scott explicitly stated that this documentation is being built for a post-merger lobby to exit CallTek, with Jady as the internal audience. Claude flagged that the exit intent must stay verbal and out of written records to avoid bad-faith exposure in any dispute or diligence process, and recommended the Jady briefing be moved up before CTC leadership shapes their own version of events with Hyatt Corporate. Claude also identified that the fleet audit commitment in CallTek's own RCA Section 5 is a significant leverage point, as other Hyatt properties may currently be in a suppressed state, which would convert Vail from an isolated incident into a systemic pattern.

**Tool Knowledge**

Claude used `conversation_search` with the query "Hyatt Grand Vail" to locate the April thread, and separately with "Vail Briggs wireless" when searching for a more recent thread. Neither located the current week's conversation, which Scott confirmed existed — indicating that recency-based search may not surface very recent threads reliably, and that `recent_chats` with a date-bounded parameter (e.g., `after: 2026-07-19`) is a better primary approach for finding current-week conversations. For file reading, `extract-text` worked on both the `.docx` RCA document and the `.xlsx` event log; piping the spreadsheet output through `head -60` was sufficient to capture the event distribution data needed for the reply without processing the full 649-row log.

### SCOTT (2026-07-22T23:05)
did we have a chat ont he hyatt grand vail recently

### CLAUDE (2026-07-22T23:05)

Yes — end of April. It was the Grand Hyatt Vail network assessment thread. Briggs Barggren (IT Manager at the property) had flagged wireless issues, and Cedrich had completed a review that found the Santana SSID was restored property-wide plus several RF problems: heavy 2.4 GHz client load, 5 GHz channel width and DFS exposure, and significant co-channel interference on the Conference and Guest groups.

We drafted two emails: one to Cedrich approving the remediation work (prioritizing the CCI on Conference and Guest, band steering off 2.4 GHz, moving 5 GHz to 80 MHz and off DFS channels, with a request for a change summary afterward), and then a customer-facing update to Briggs confirming Santana was restored on all APs and covering the network adjustments.

Want me to pull up the full thread, or are you working on a follow-up to Briggs or Cedrich?

### SCOTT (2026-07-22T23:05)
na. there was a more recnt thread, this week. not sure if you were invlcoed or not

### CLAUDE (2026-07-22T23:05)

I checked — nothing on Grand Hyatt Vail this week. Your chats from July 19–22 in my searchable scope are: the Spectrum/Cox course feedback work, the CallTek invoice/net-45 review, the ATLBH closure reply, the CTC AI recording issue, the Poppy Lou announcement, and a quick chat-finder session. The most recent Vail thread I can find is still the April 30 one with Cedrich and Briggs.

One caveat: since we're in a project, I can only search conversations within this project. If the Vail chat happened outside the project or in a different one, it wouldn't show up for me here. Could also be it was an email thread you handled without me. Anything you want to pick up on Vail now?

### SCOTT (2026-07-22T23:06)
here it is.  help me clean up my reply please

[Attachment: ]
Thanks, Alison,

The lack of contracted proactive monitoring and alerting is the root cause of this escalation.  We have all been doing this long enough to know that stuff is going to happen at hotel customers; it's how we react and respond that matters and is exactly what these hotels are buying from BPRF.

Had our proactive monitoring system been working as it should have been, then we could have gotten ahead of this issue with the customer and Hyatt Corp.  The issue still would have been there, and even if we could not have gotten ahead of this with regard to the group in-house, we would have been able to demonstrate that we are at least compliant with the terms of our MSA with Hyatt.

The hotel is already asking for credits for the tech dispatches, is asking for us to pay for any and all requisite repair to the infrastructure that may be needed, an are you know that if not part of our normal support, and as source of high margin work when we are able to bill the customer for this type of work.  And the hotel is also asking me what I inteed to d aotu the $10K they had to credit back to this customer, and the even greater lost revenue if this customer doesn’t return as a result of this inciudnt,  That is much bigger that just the wi-fi fees associated with this event.  It includes the rooms, the F&B, etc.  

From: Alison Perales <Alison_Perales@calltekinc.com> 
Sent: Wednesday, July 22, 2026 5:19 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Danny Wu <danny_wu@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point 

Hi Scott,

Understood. The RCA detailing the ticket generation failure at Grand Hyatt Vail has been provided. Let me know if you have any questions or need further details.

Thanks,

 
________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Wednesday, July 22, 2026 4:32 PM
To: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Danny Wu <danny_wu@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point 
 
Respectfully, I raised this escalation, not Helen. I raised it due to our failure to meet the contracted proactive monitoring requirement for Hyatt Hotels. The uplink flapping does appear to be a hotel infrastructure issue which we may or may not be responsible for. What we absolutely are on the hook for is the fact that this went on for quite a while with no proactive alert or response from BPRF. This flapping caused the large group event at the hotel to continually lose their Internet connectivity during the event. 

I need Helen focused on running the NOC, so my ask is that directives and tasks for her and the rest of my team be routed through me and Kyle and Marie. 

Thanks,
Scott

________________________________________
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Wednesday, 22 July 2026 15:19:02
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Danny Wu <danny_wu@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point 
 
Hi Scott,

I asked Helen to prepare the site-specific RCA because that report covers site downtime, operational impact, and the underlying physical root causes. My RCA focuses strictly on the failure within the monitoring system, its resulting impact, and the corrective actions being implemented to address it.

Please let me know if you need anything else from my end.

Thanks,

Alison Perales
Network Operations Support
Office: 866-931-9722 option 1

 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 

________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Wednesday, July 22, 2026 3:57 PM
To: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Danny Wu <danny_wu@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point 
 
This impacted a large recurring group event at the hotel. Was way more than a couple of APs going down.

I am away from my computer. I will send screen shots later from the hotel owner where he said he had to credit $10K back to the group for this event and has a meeting  next week with the board of directors to see if he can salvage / recover this group and convince them to return. 

@Helen Pantaleon - you don't need to reply to Alison's inquiry below. I will handle directly and reach out to you directly if I need any details. 

@Alison Perales - my preference is that if an escalation comes from me, that you direct inquiries about it to me and not my team. Helen's job is to manage my NOC. She is not a brand manager, and as such is and was not exposed to all the executive level communications on this escalation. 

Thanks,
Scott. 

________________________________________
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Wednesday, July 22, 2026 2:47 PM
To: Joshua Bergen <Joshua_Bergen@calltekinc.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Danny Wu <danny_wu@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point 
 
The RCA that I put together is for the monitoring issue. The core impact of this failure is that we are unable to catch offline devices in a timely manner, forcing us to rely on staff reports to identify outages.

Per Cosmos event logs, only two APs at the site were down but no monitoring tickets were generated when they dropped. There's a switch that has gone online/offline but even if ticket generation is working it will still not generate a ticket because as  I previously mentioned it was not offline long enough to reach the threshold. The default rule requires 5 minutes per polling cycle to generate an event and 3 consecutive polling cycles (15 minutes total) to trigger a ticket. 

When staff reported conference Wi-Fi issues on 7/15, the NOC investigated and identified missing configurations, CRC errors on the flapping switch, and underlying physical infrastructure issues (fiber/SFP). While the monitoring gap delayed our visibility, the outage itself was driven by hardware performance. I will have @Helen Pantaleon a separate RCA dedicated specifically to the on-site infrastructure and fiber/SFP issues which will detail the full impact, total downtime, and actual root cause.

Thanks,

Alison Perales
Network Operations Support
Office: 866-931-9722 option 1

 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 

________________________________________
From: Joshua Bergen <Joshua_Bergen@calltekinc.com>
Sent: Wednesday, July 22, 2026 1:54 PM
To: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>; Danny Wu <danny_wu@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Subject: RE: [EXTERNAL] Re: BPRF - Cosmos escalation point 
 
Can you add the impact to the resort?
 
What systems were down? How long? Did it stop sales/reservations/checkin/checkout? What functions were impacted and for how long.
 
Scott mentioned a $10,000 impact to the customer.  How can we support this by tying it to the issue and the impact at the site?
 
This will be key for most RCAs. 
 
If it caused the tracking of towel distribution at a pool vrs shut down a site from all revenue generating outlets.  BIG difference.
 
 
 
Book time with Joshua Bergen
 
 
 
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Wednesday, July 22, 2026 1:34 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>; Danny Wu <danny_wu@calltekinc.com>; Alison Perales <Alison_Perales@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Hi Scott,
 
Please see the attached file for the RCA.
 
 
Thanks,
 
 
Alison Perales
Network Operations Support
Office: 866-931-9722 option 1
 
 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 
 
________________________________________
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Tuesday, July 21, 2026 8:26 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Hi Scott,
 
My initial finding indicates that the switch going up and down did not generate a ticket because it was not offline long enough to reach the threshold. The default rule requires 5 minutes per polling cycle to generate an event and 3 consecutive polling cycles (15 minutes total) to trigger a ticket. 
 
I am continuing to coordinate with our development team to review further details.
 
 
Thanks,
 
 
Alison Perales
Network Operations Support
Office: 866-931-9722 option 1
 
 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 
 
________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Tuesday, July 21, 2026 7:46 PM
To: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Yes. 
 
________________________________________
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Tuesday, 21 July 2026 18:33:55
To: Joshua Bergen <Joshua_Bergen@calltekinc.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Hi Scott,
 
Are you referring to Grand Hyatt Vail or another site?
 
 
Thanks,
 
 
Alison Perales
Network Operations Support
Office: 866-931-9722 option 1
 
 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 
 
________________________________________
From: Joshua Bergen <Joshua_Bergen@calltekinc.com>
Sent: Tuesday, July 21, 2026 7:27 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Do we have the Hotel info and have we performed a RCA?
 
Alison, can you discuss with the team and parties involved?
 
Thanks,
 
Josh Bergen
Chief Growth Officer
949-674-0368
________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Tuesday, 21 July 2026 19:22:31
To: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>; Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
I have a hotel looking for $10K in reimbursement due to COSMOS not correctly alerting an outage which caused them significant lost revenue and reputation as a result. 
 
________________________________________
From: Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Sent: Tuesday, 21 July 2026 18:11:26
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Joshua Bergen <joshua_bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Hi Scott,
 
We have streamlined the Cosmos deployment process using the OAB tool, which now handles end-to-end agent deployment and monitoring. The tool was created so the team can manage the task on their own. Marie is correct: TDE handles Cosmos deployments via OAB specifically during TDE project implementations, and they should not be receiving support escalations.
 
For standard server replacements, the PNOC/NOC team handles the Cosmos deployment independently. I posted the standard operating procedure last March, and the escalation path does not include TDE. I'll work with Helen to  align with the NOC team to clarify why these escalations were routed incorrectly.
 
 
 
If an issue occurs during deployment using the OAB tool, it should be escalated to BPRF Dev team via ticket (assigned to Cosmos group). This escalation path applies to both TDE and the NOC team.
 
 
The OAB tool manages the following end-to-end processes:
* SF-Cosmos Sync (SF to Cosmos communication)
* Toggling Ticketing On/Off (BPRF Server to Cosmos communication)
* Cosmos Agent Deployment (BPRF Server to Cosmos communication)
The process follows a structured path. SF sync should be completed and successful before they can proceed to the next steps.
 
If communication fails at any of these stages, it must be escalated to the BPRF Dev team, as the BPRF Server initiates the requests to SF and Cosmos. Currently, we have not observed any communication failures between the BPRF Server and Cosmos, but any future occurrences should follow this escalation path and reported to Calltek if there is an issue.
 
We previously stop the weekly Cosmos alignment meetings after project completion, establishing that Dev issues could be handled via email or chat  and I haven't heard of any issues raised so far. However, if these operational gaps persist, I recommend resuming our weekly meeting cadence until the workflow is fully stabilized.
 
 
Thanks,
 
 
Alison Perales
Network Operations Support
Office: 866-931-9722 option 1
 
 
Leave Us a Google Review 
Follow Us on LinkedIn  •  Named #1 Marriott Provider 
 
________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Tuesday, July 21, 2026 6:18 PM
To: Joshua Bergen <Joshua_Bergen@calltekinc.com>; Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Cc: Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
We had some pretty major missteps with the COSMOS monitoring tool this week that cost me a significant dollar amount in credits back to the impacted hotel customer. 
 
So, if the process is going to be that my team has to escalate to someone who escalates to someone, then I need you to provide to me the CTC committed SLA's for this. 
 
This all started because CTC employees are telling my team to get with my TDE's for COSMOS related issues due to delayed responses and actions when following the current process. 
 
________________________________________
From: Joshua Bergen <Joshua_Bergen@calltekinc.com>
Sent: Tuesday, 21 July 2026 16:34:15
To: Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Cc: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: Re: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
You escalate to the Acct Mgr, they have an internal process for IT Development issues. But keeping the communication with the AMs are key.
 
If you feel you have a problem or concern, Alison is your next step.  She has all the authority to take actions for any of the tools we use to support BPRF that we supply.  COSMOS, CAS, MITEL/ZOOM etc
 
They will bring in any necessary IT leaders or programmers. 
 
Thanks,
 
Josh Bergen
Chief Growth Officer
949-674-0368
________________________________________
From: Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Sent: Tuesday, 21 July 2026 16:30:37
To: Joshua Bergen <Joshua_Bergen@calltekinc.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Cc: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: RE: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Hi Joshua,
 
I understand that Ops issues should go to BPRF Supervisors and Managers. However, the ask is for a COSMOS (which is a product of Calltek) escalation point. I can work with the Ops Team in our account to create an escalation path for COSMOS but if there’s no one to escalate to, not sure how complete that SOP document will be. Thanks!
 
Regards,
 
Marie Henson
TDE Supervisor
 
 
From: Joshua Bergen <Joshua_Bergen@calltekinc.com>
Sent: Tuesday, 21 July 2026 4:18 pm
To: Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Cc: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>; Helen Pantaleon <Helen.Pantaleon@calltekinc.com>
Subject: [EXTERNAL] Re: BPRF - Cosmos escalation point
 
Alison,
 
Please share with her the name of the new Sr Supervisor as that is her key point of contact. Helen is copied here.
 
Also, we have Pheobe and of course, Allison as Ops Mgr. 
 
You don't need multiple levels or above a VP to seek an Ops issue. We have a Director also if you feel the 100% dedicated leaders on site are not managing access or issues correctly. 
 
Please meet with your direct, onsite leader and review the SOP you want followed, they were can share with the team.
 
Thanks,
 
Josh Bergen
Chief Growth Officer
949-674-0368
________________________________________
From: Henson, Marie (Blueprint RF) <marie.henson@blueprintrf.com>
Sent: Tuesday, 21 July 2026 09:55:39
To: Joshua Bergen <Joshua_Bergen@calltekinc.com>; Perales, Alison (Blueprint RF) <alison.perales@blueprintrf.com>
Cc: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Davis, Kyle (Blueprint RF) <kyle.davis2@blueprintrf.com>
Subject: EXTERNAL!!! - Cosmos escalation point
 
CAUTION: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe.
Hi Joshua and Alison,
 
Good day! Following the recent leadership change at CallTek, our CTC staff have raised concerns regarding delayed responses and a lack of a clear escalation path for Cosmos issues. Furthermore, CTC staff are asked to reachout to TDEs for Cosmos related concerns. To clarify, I only approved TDEs installing Cosmos agent via OAB tool and not touch Cosmos system itself to troubleshoot. I also wish to get Cedrich’s involvement minimal and limited only for Salesforce synch issues when it comes to troubleshooting proactive monitoring issues. Previously, Alison and Kyle F. handled these escalations. Could you please clarify and inform us and the CallTek BPRF Team of the correct escalation path for Cosmos-related issues moving forward? It’s odd that they will reachout to me for this when they have a full Team there. Thanks!
 
Regards,
 
Marie Henson
TDE Supervisor
 
 

[File uploaded: ]

### CLAUDE (2026-07-22T23:06)

Cleaned up above. Two things I did beyond typo fixes:

1. **Added "As it stands, we cannot."** at the end of paragraph two. Your draft made the compliance argument but left the conclusion implied — landing it explicitly strengthens the record on the thread, especially with CTC leadership copied. Cut it if you'd rather leave it softer.

2. **Untangled the garbled third paragraph.** I read your intent as: the repairs the hotel wants us to eat would normally be *billable* high-margin work for us — so the exposure is both cost absorbed and revenue foregone. Confirm that's the right read.

One strategic flag, not added to the draft: Alison's defense on the record is that the switch flapping never hit the 15-minute threshold, so ticketing "worked as designed." Your reply asserts the monitoring failed but doesn't directly answer that. If you want to close that door, one sentence would do it — something like: *"A threshold configuration that cannot detect a sustained flapping condition impacting a live conference network is itself a monitoring deficiency, not a defense."* That also matters because her RCA framing (hardware root cause, monitoring merely "delayed visibility") is what CTC will lean on in any August SLA conversation. Also worth noting the Cosmos event logs showed two APs down with *no tickets generated* — that part isn't threshold-related, and her RCA concedes it. Want me to work either point in?

### SCOTT (2026-07-22T23:07)
ya.  add it.  all of this goes ont eh calltek record. for when I lobby to finally ger rid of them post merger close

### CLAUDE (2026-07-22T23:08)

Both points are in as a new paragraph three. It separates the two failure modes cleanly — the two-APs-with-no-tickets item first (her own RCA concedes it, and it has no threshold excuse), then the flapping-switch rebuttal with the "working as designed vs. working as required" close.

A few notes for the record you're building:

**This email does its job for that purpose as written.** It's factual, contract-anchored (MSA compliance, contracted monitoring requirement), quantified ($10K plus consequential exposure), and it pins their own RCA language against them. Nothing in it reads as anything other than an operator holding a vendor to contract — which is exactly how it should read.

**Keep the endgame out of everything written, including internal email.** You know this, but worth saying since the stakes are going up: the exit lobby stays verbal with Jady only. Any written trace of predetermined intent to exit gives CTC a "bad faith" argument if this ever gets to a formal dispute, and it also complicates the merger-context optics if it surfaces in diligence. The record should show a customer patiently documenting repeated failures — QA breaches since April 2025, the AI recording violations, SLA reporting gaps, leadership churn, and now a monitoring failure with quantified customer harm. That story assembles itself.

**One gap to close for the file:** get the hotel owner's screenshots ($10K credit, board meeting) attached to this thread once you're back at your computer, as you said you would. That converts the damages claim from your assertion to documented third-party evidence — the difference matters if this feeds an SLA credit demand or dispute notice in August.

**And per your own gate:** this thread plus the RCA is now strong enough that the Jady briefing you've been holding for the August cycle probably shouldn't wait for August. Josh is already asking Alison to build the impact case — CTC is preparing their version of this story for their own leadership. Better Jady hears yours first.

### SCOTT (2026-07-23T19:17)
reply and attachments from Alison.  Guess she cannot let this go.  reads t me once again like she is defending her syetm saying it worked as designed...
[File uploaded: 1784834197357_image.png]
[File uploaded: 703695_events.xlsx]
[File uploaded: Cosmos_Monitoring_Grand_Hyatt_Vail_RCA_and_Fixes.docx]

### CLAUDE (2026-07-23T19:19)
Let me read her attachments before we respond — I want to see what the updated RCA actually concedes versus defends.

Read both attachments. Before the reply — her email is doing a lot of work to soften what her own RCA actually says, and the RCA is a much bigger concession than "performed as designed":

**What the RCA actually admits:**
- **Automated ticketing for the entire property was dead from May 14 to July 21 — 68 days.** A misconfigured collectd agent locked the core Nomadix into a false "Down" state, and Cosmos's hierarchy suppression killed ticket generation for every downstream device at the site. That's not a threshold nuance; that's zero proactive ticketing at a Hyatt property for over two months.
- **The PNOC noted the core-down alert on May 14 and disregarded it**, and the RCA states outright that none of the verification or escalation protocols were followed. Human failure inside the monitoring operation, on the record, in their document.
- **Two APs logged down events on seven separate dates** (6/25, 6/26, 6/27, 7/11–7/13, 7/18) with no tickets — all suppression, not threshold.
- **The event log shows 649 WARNING events (49.5% of all records) at 20–85% packet loss and five FAILURE events at 98–100%** — and nothing happened until hotel staff called on July 14.
- **The "fixes" are confessions.** Suppression expiration and flapping detection were implemented 7/23 — after your escalation. Those capabilities didn't exist when the customer needed them. And flapping *ticketing* is still "pending development."
- **Section 5 commits to reviewing all Nomadix sites** — meaning they know other properties may be sitting in this exact state right now. That's fleet-wide Hyatt exposure, and you want that audit result before Hyatt Corp ever asks the question.

**One thing to have ready:** the May 14 trigger was Cedrich's agent deployment (your TDE side). Their RCA concedes the procedure was undocumented at the time — which is their product, their deployment guide — but expect CTC to lean on it. The clean counter is already in the record: whoever caused the initial misconfig, a monitoring operation that lets a core gateway sit "Down" for 68 days without investigation is the failure.

Here's the reply:

Draft's above. A few notes on how it's built:

**It converts her document into your evidence.** Every number in the reply comes from her RCA or her attached log — 68 days, seven AP-down dates, 649 WARNINGs, the disregarded May 14 alert, the 7/23 fix dates. Nothing is your assertion; it's all "per your own document." That's the strongest possible posture for the record.

**The three asks do double duty.** They're operationally legitimate (you genuinely need the fleet audit and the ticketing date), and each one forces CTC to either commit in writing or refuse in writing. The fleet audit is the big one — if that review turns up other suppressed Hyatt properties, the Vail incident stops being an isolated event and becomes a pattern, which changes both the SLA credit conversation and your Jady briefing materially.

**One deliberate omission:** I didn't press the Cedrich deployment point beyond the "undocumented procedure" line. Going further invites a whose-tech-broke-it exchange that muddies the clean story (their product, their deployment guide, their NOC disregarded the alert for 68 days). If they raise Cedrich in response, that's the moment to answer it — not preemptively.

**For the Jady briefing:** this RCA is now Exhibit A. The 68-day suppression window plus the fleet-audit admission is the kind of thing she'll want to know before any CTC leadership conversation, and before Hyatt Corp hears about it from anyone else. Worth also deciding with her whether the fleet audit results, if bad, trigger proactive disclosure to Hyatt — better to control that narrative than have it surface later.
