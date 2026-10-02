# Code cleanup assistance
Date: 2026-09-08
Conversation: e75595d0-1770-4cd0-9c99-4358dd339851
Domain: business-ops

## Summary
**Conversation Overview**

Scott asked Claude to clean up and rewrite a message he needed to send to a colleague named Rob regarding a ticket (Incident INC13726266) about setting up new BPO contractor accounts in a new system following a migration away from MyID. Claude composed a polished, forwardable email reply structured with a bottom-line-up-front format and numbered issues for traceability.

The email addressed five gaps in the new contractor account system: missing guidance on required form fields, email domain configuration for agents using @blueprintrf.com addresses, account expiration and renewal mechanics, delegated admin capabilities for supervisor-level contractors, and a quarterly access attestation workflow tied to SOC 2 and ISO 27001 compliance obligations. Claude ranked the first four as primary and the fifth as lower urgency, and embedded a request for a 45-minute call. Claude also flagged a count correction — the email body initially said "four" issues but actually listed five — and advised Scott to verify before sending.

Scott's role involves managing 100+ contractor agents for Blueprint RF. Rob appears to be a technical or IT contact on the receiving end of the ticket. Scott's communication style for external, forwardable emails favors structured, numbered formats with clear asks and ranked priorities.

### SCOTT (2026-09-08T16:54)
help me clean this up:

[Attachment: ]
I currently have around 100 contractors for my call center and NOC.  

I have a few new agents I need to set up accounts for.  I tried to compare the settings with one of my team members who migrated over, but the setup form has required fields that are blank on the existing one.  Plus, there are fields like mobile number that I do not have.  My team is based in the Philippines, and most don't have a company-provided mobile phone number I could use.

Since these agents represent Blueprint RF to our customers (not Cox or Spectrum), it is critical that they get assigned an @blueprntrf.com email address as their primary email.  I couldn't figure out where to define that in the setup form.

Additionally, under the legacy Cox myID system, contractor accounts were only valid for a year, and if they weren’t renewed, the entire account, email, SharePoint, etc. were deleted.  As such, my team had to closely manage this date to ensure renewals happened prior to the expiration date.  I need to know if any sort of expiry dates exist in this new system.    

Also, with 100+ agents and team members to manage, under the legacy Cox MyID system, I was able to set up some of my contractors as supervisors so that they could handle the creation and renewals themselves.  They could create new accounts, and then it would route to me for approval.

Finally, as part of our contracted SOC 2 and ISO 27001 certifications, I have to do a quartelty atestian that all fo the my agent an team members with acocutns are infact legitimate and should retain the access.  Under the legacy-cox myid system there was a work-flow that facilaited this.  I am trying to ascertain if something similar exists with this new system or not.

There is a lot to unpack here, which is why I was think a call would dbe easiest

From: Fox, Rob J <Rob.Fox@spectrum.com> 
Sent: Tuesday, September 8, 2026 12:26 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Lopez-Herrera, Denise <Denise.Lopez-Herrera@spectrum.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added

Scott, can you please summarize the concern(s).  

What specifically are you trying to accomplish that you’re having issues with?

Thank you,

 

Rob Fox | Sr. Director – Process Engineering | (972)589-4432
400 Washington Blvd.
Stamford CT, 06902 

From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Tuesday, September 8, 2026 12:07 PM
To: Lopez-Herrera, Denise <Denise.Lopez-Herrera@spectrum.com>; Fox, Rob J <Rob.Fox@spectrum.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added
Importance: High

	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance. 

Hi Rob and Denise,

I need help setting up new BPO contractors, and I want to discuss a few other items, like account renewals, contractor emails, etc.  Can I get 45 minutes on your calendar this week to discuss?  

Thanks,

Scott Watts
Senior Director, Hospitality Operations
Email: scott.watts@blueprintrf.com
 
         
 
Book time with Watts, Scott (CCI-Blueprint RF) 
 
 

From: Trotter, Jeffery <Jeffery.Trotter@spectrum.com> 
Sent: Friday, August 28, 2026 10:41 AM
To: Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com>; Horton, Mike M <Mike.Horton@spectrum.com>; Pinkey-Coleman, Lisa <Lisa.Pinkey-Coleman@spectrum.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>; Lopez-Herrera, Denise <Denise.Lopez-Herrera@spectrum.com>; Heidlberger, David A <David.Heidlberger@spectrum.com>; Fox, Rob J <Rob.Fox@spectrum.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added

	You don't often get email from jeffery.trotter@spectrum.com. Learn why this is important 

@Watts, Scott (CCI-Blueprint RF) – I believe your best bet is to connect with @Lopez-Herrera, Denise for guidance.  I have cc’d Denise and her leader @Fox, Rob J.

The short of it is that we will no longer be working out of MyID and will need to transition to IDM.  Our Field Ops team have been working through establishing processes for this over the past few days.

I’ve attached the user list you sent over.

Jeff

From: Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com> 
Sent: Friday, August 28, 2026 6:19 AM
To: Horton, Mike M <Mike.Horton@spectrum.com>; Pinkey-Coleman, Lisa <Lisa.Pinkey-Coleman@spectrum.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added

	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance. 

Mike, 
Since this is vendor related; please can you take the lead on helping Scott get access. I am asking around, but don’t have the right contacts on my side and I am working on the Charter to Cox access vs. Cox to Charter. 

Lisa 

From: Horton, Mike M <Mike.Horton@spectrum.com> 
Sent: Friday, August 28, 2026 7:13 AM
To: Pinkey-Coleman, Lisa <Lisa.Pinkey-Coleman@spectrum.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>
Subject: Re: [EXTERNAL] FW: Incident INC13726266 -- comments added

	You don't often get email from mike.horton@spectrum.com. Learn why this is important 

Good Morning,

Scott, you may want to connect with Tom Lake who may be working through the same scenarios as they onboard their offshore agents.  Apologies if you have already been down that path.

Mike
________________________________________
From: Pinkey-Coleman, Lisa <Lisa.Pinkey-Coleman@spectrum.com>
Sent: 28 August 2026 06:46
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added 
 
Thank you. I will see what I can do to help. 
 
Lisa 
 
 
Lisa Pinkey-Coleman | VP, Process Engineering 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
 
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Thursday, August 27, 2026 5:38 PM
To: Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance. 
 
Sorry for the delay.  I had to get my teams to make a consolidated list.  Please see attached. 
 
 
 
From: Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com> 
Sent: Thursday, August 27, 2026 3:50 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Horton, Mike (CCI-Atlanta) <Mike.Horton@cox.com>
Cc: Trotter, Jeff (CCI-California) <Jeff.Trotter@cox.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
Hi Scott, 
I am on with IT now, can you send the users? 
 
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Thursday, August 27, 2026 3:00 PM
To: Pinkey-Coleman, Lisa (CCI-Atlanta) <Lisa.Pinkey-Coleman@cox.com>
Subject: FW: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
Hi Lisa,
 
Please see the thread below.  I am having some MyID issues with my offshore teams that is starting to impact our service.  IT Helpdesk told me to get with Charter HR.  Charter HR pointed me to Joe Peeples, who pointed me to you.  Can you assist?
 
Thanks,
 
Scott Watts
Senior Director, Hospitality Operations
Email: scott.watts@blueprintrf.com
 
          
 
Book time with Watts, Scott (CCI-Blueprint RF) 
 
 
 
 
From: Peeples, Joe <Joe.Peeples@spectrum.com> 
Sent: Thursday, August 27, 2026 2:56 PM
To: Pehrson, Angie <Angie.Pehrson@spectrum.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
Thanks Angie.  Scott and I talked; he’s going to reach out to Lisa Pinkey-Coleman who is already working through MYID and IDM compatibility issues.
 
Joe
 
From: Pehrson, Angie <Angie.Pehrson@spectrum.com> 
Sent: Thursday, August 27, 2026 11:40 AM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Cc: Peeples, Joe <Joe.Peeples@spectrum.com>
Subject: RE: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
Hi Scott,
This is outside the HR access/wheelhouse.  I sent your email to Joe Peeples.  I believe he has a contact to connect with on this particular issue.  If he hasn’t yet, he will be reaching out.
 
 
 
Angie Pehrson, PHR, SHRM-CP | Director, Human Resources-Field Operations
Sierra Nevada and Las Vegas Management Areas
O: 775.850.1718| C: 775.684.9843| Fax 775.850.1229
9335 Prototype Drive | Reno, NV 89521
1700 Vegas Drive | Las Vegas, NV 89106
 
 
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com> 
Sent: Thursday, August 27, 2026 9:37 AM
To: Pehrson, Angie <Angie.Pehrson@spectrum.com>
Subject: [EXTERNAL] FW: Incident INC13726266 -- comments added
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance. 
 
Hi Angie,
 
My leader, Jady West, gave me your name as our new Charter HR point of contact.
 
As part of my role, I manage a large offshore team in the Philippines — roughly 100 call center agents and technical support engineers, all contractors hired through multiple BPO companies. Before the merger, my team and I used the Cox MyID system to manage their access to Blueprint RF email, tools, and systems.
 
MyID went down a few weeks before the merger closed. The site banner said full functionality would be restored by 8/21, but that hasn't happened. As a result, several team members' accounts have expired because we couldn't log in to renew them. Once an account expires, everything tied to it is immediately and irreversibly deleted — email, SharePoint files, system access, etc. Historically, I've worked around this by creating a new account, as I would for a new hire, but that function is also currently missing from MyID.
 
I raised this with the IT helpdesk, and they've directed me to the Charter HR team. I'm hoping you're the right person to help, or can point me to who is — this is now starting to affect my team's ability to support our customers.
 
Thanks,
Scott Watts
Senior Director, Hospitality Operations
Email: scott.watts@blueprintrf.com
 
          
 
Book time with Watts, Scott (CCI-Blueprint RF) 
 
 
 
 
 
From: ITHelp Notification <coxprod@service-now.com> 
Sent: Thursday, August 27, 2026 10:37 AM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Subject: Incident INC13726266 -- comments added
 
 
                                                                                                                                                                                                                                  
Requested for: Scott Watts
Short Description: myID - Enquiry
Description: The option to add non-employee users is gone. and for my existing contractors that need to be renewed before account is terminated, the date field is zeroed and greyed out for me
 
251-379-0451 anytime
Click here to view Incident: INC13726266
Severity: 3 - Low
Priority: Priority3
Category: Enterprise Application
Comments:
________________________________________
08-27-2026 10:36:23 EDT - SatyaNarayana Kola Additional comments
Hi,
 
Contractor contract date extensions and terminations will need to get initiated over the Charter contractor office.
please reach out Charter HR Team.
 
Thanks
________________________________________
08-26-2026 11:25:54 EDT - Scott Watts Additional comments
reply from: scott.watts@blueprintrf.com
 
I have that link. The option for me to create a non-employee account is gone..
 
[cid:image001.png@01DD354D.4756FCE0]
________________________________________
08-26-2026 07:31:26 EDT - Ruchi Yadav Additional comments
Below is the quicklink for non- employee addition.
https://myid.corp.cox.com/workitem/commonWorkItem.jsf#/commonWorkItem/session
 
For account re-newel, please let the know the user ID's.
 
Thank you,
The Cox ServiceNow Team
                                                                                                                                                                                                                                  
COX - ServiceNow 
 
Ref:MSG68077713
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 

[File uploaded: ]

### CLAUDE (2026-09-08T16:54)

Here's a clean, forwardable reply to Rob — bottom-line up front, numbered issues so each one is trackable:

That's the numbered summary Rob asked for — five gaps, ranked by urgency, tied back to your original ask for 45 minutes. Note I fixed "Four" to reflect five items in the body; check that before sending.
