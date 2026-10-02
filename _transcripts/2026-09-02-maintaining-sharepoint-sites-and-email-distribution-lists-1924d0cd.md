# Maintaining SharePoint sites and email distribution lists
Date: 2026-09-02
Conversation: 1924d0cd-bb6a-4992-8151-50b894fa9c02
Domain: business-ops

## Summary
**Conversation Overview**

Scott is a senior leader at Blueprint RF (BPRF), a hospitality technology company that provides WiFi and network operations center (NOC) services to major hotel brands including Marriott, Hilton, and Hyatt. The conversation centered on helping Scott navigate an ongoing email thread and then draft an internal leadership update regarding the migration of the blueprintrf.com domain from the Cox/CEI tenant to the Charter/Spectrum tenant. Key colleagues referenced include Dan and Kyle (Scott's technical leads handling inventory and site identification), Rachael McIntosh (Cox-Atlanta, point of contact on Salesforce/Rapidscale questions), Megan and Brian (Charter/Spectrum migration team contacts), Dale Brannock (raised earlier technical constraints in the thread), Marie Henson, and Julian Cayetano.

The core business stakes Scott emphasized throughout are that @blueprintrf.com email addresses, distribution lists (DLs), and SharePoint sites are not internal administrative tools — they are customer-facing infrastructure. Hotel customers, property managers, and Marriott/Hilton/Hyatt corporate offices use brand-specific NOC DLs as their primary intake channel for support and ticketing. Scott's non-negotiable position is that all users including contractors retain @blueprintrf.com as their primary address. The call with the Spectrum migration team confirmed this: the end state will be @blueprintrf.com as primary with @spectrum.com and @charter.com as aliases. The migration team also confirmed there will be downtime but that emails will be queued rather than rejected or bounced during the cutover window. No migration timeline has been set, though the team indicated they want to move quickly. The Rapidscale Salesforce instance is moving to an independent instance outside Spectrum, which may affect BPRF if they are still attached to it — Scott flagged Rachael McIntosh to confirm.

Scott's communication style is direct and informal in his own drafts but wants polished, professional output for both the external email thread with Charter IT and the internal leadership update. He pushed back on Claude's initial draft when it unnecessarily repeated scale figures (30k sites, 18k DLs) that Brian already knew, preferring a tone that acknowledges context without over-explaining. He also corrected Claude's framing on DL routing to make clear the scope is not just his team but all external hotel customers and brand corporate contacts. For the leadership update, Scott explicitly wanted the closing call-to-action to convey urgency — his concern is that his leadership team will delay compiling their app inventory lists until after things break, so the message was drafted to be direct that any app not identified and configured in advance will lose access post-migration, with no softening of that consequence.

### SCOTT (2026-09-02T12:44)
read this entire thread and help me fisinh my rpely.  feels to me like thaey are aksing a bunch of quesitons to make it harder thatn it is.  i need all of my shapeporint sites and emails address and distro list maintined.  its how we presnt to our brands and our ciusotmers and how they commuctioe with us and our entiure care and support org.

[Attachment: ]
+ Dan, and Kyle form my teams.

Hoping they have some of the answers. 

But some of these questions, like “All user identities need to maintain the blueprintRF domain email addresses,” and distribution lists and SharePoint sites?

Are you not able to get that from our current active instance?  

Sort version is, everyone that has an @blueprintrf.com email address will ne to keep it.  All of my teams, contractors included, will need to have the @blueprintrf.com email set as their 



From: Dover, Megan <Megan.Dover@spectrum.com> 
Sent: Wednesday, September 2, 2026 7:57 AM
To: Tucker, Brian <Brian.Tucker1@spectrum.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses

	You don't often get email from megan.dover@spectrum.com. Learn why this is important 

Jady and Scott, who on your team can get Brian the detail he needs? 

Sent from my Verizon, Samsung Galaxy smartphone
Get Outlook for Android
________________________________________
From: Tucker, Brian <Brian.Tucker1@spectrum.com>
Sent: Wednesday, 02 September 2026 07:51:02
To: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses 
 
Megan,

As we scope the migration of BlueprintRF to Spectrum, we need to understand the following so we can “Lift and Shift” all BlueprintRF assets to Spectrum, retaining your BlueprintRF access.

This list would include:

•	All User Identities needing to maintain the blueprintRF domain email addresses
•	All Application Registrations (SSO apps) that need to migrate
•	All Security Groups specific to BluePrintRF
•	All Teams Groups (Sharepoint backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
•	All SharePoint Sites that are owned/managed by BlueprintRF
•	All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns 
•	All Email Distribution lists owned or managed by BluePrintRF
•	All Lucid spaces that need to be migrated for support

We will need this as quickly as possible in order to properly plan and inject the Blueprint RF team into the plans that are already laid out for other migrations.  

Regards,

Brian
From: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Date: Wednesday, August 19, 2026 at 11:13 AM
To: West, Jady (CCI-Southwest) <Jady.West@cox.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
Brian, Jeff Breaux is asking if BPRF will stay in the CCI tenet along with RapidScale.  And, who do we need to work with to ensure no disruption beyond Day 15. 
Thank you!
 
From: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Sent: Tuesday, August 18, 2026 2:24 PM
To: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Ok thanks
________________________________________
From: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>
Sent: Tuesday, August 18, 2026 11:09 AM
To: West, Jady (CCI-Southwest) <Jady.West@cox.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Email for all Cox users will remain active on Day 1-15.  BlueprintRF will continue to work past Day 15 until we migrate everything to Charter.
 
Regards,
Brian Tucker
Manager, Modern Workplace Engineering
 
 
 
From: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Date: Tuesday, August 18, 2026 at 2:02 PM
To: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
Brian,
 
To be clear on the no change for day one I assume that this means that the email for Blueprint will continue to work on day 1.  Please clarify.
 
Jady
________________________________________
From: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>
Sent: Tuesday, August 18, 2026 9:54 AM
To: West, Jady (CCI-Southwest) <Jady.West@cox.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Megan and Team,
 
I have confirmed there will be no changes to Day 1.  However, we’re working on a plan to save BlueprintRF.com and keep it alive.  It will move to Charter quickly after Day 1 and everyone will keep their BluePrintRF email address.  More to come after Day 1.
 
Regards,
Brian Tucker
Manager, Modern Workplace Engineering
 
 
From: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Date: Monday, August 17, 2026 at 7:51 PM
To: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
Thanks for your help on this important topic.
 
Jady
________________________________________
From: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Sent: Monday, August 17, 2026 1:51 PM
To: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Thank you Brian.  Let us know what you hear.
 
From: Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>
Sent: Monday, August 17, 2026 4:48 PM
To: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Good afternoon Megan & Team.  I’ve reached out to my Charter counterparts for a discussion around this.  I recall asking and reporting to them that blueprinted.com would need to be retained.  I’ll remind them that we do need to have that conversation and see what options we have.
 
Regards,
Brian Tucker
Manager, Modern Workplace Engineering
 
 
 
From: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Date: Monday, August 17, 2026 at 3:50 PM
To: West, Jady (CCI-Southwest) <Jady.West@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
Brian, Bill and Lauren, could you take a look at this thread and help us please?  Quick summary – Back in March we were asked if we needed to maintain the email domain for BPRF and we responded that we did.  There is now some confusion/pushback from Spectrum.  It is imperative that BPRF not have a change in email domain for the foreseeable future. 
 
How do we get Charter IT aligned with that quickly?  Please let me know if I need to escalate this to Commercial leadership at Charter.
 
From: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Sent: Monday, August 17, 2026 3:17 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Pause everyone.  Please allow Megan to respond.
________________________________________
From: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Sent: Monday, August 17, 2026 12:14 PM
To: Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
If the BPRF emails stop working, my NOC operation basically stops. 
 
Most of our B2B ticketing comes from emails sent to the various brand-specific NOC@blueprintrf.com addresses.
 
 
 
From: Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>
Sent: Monday, August 17, 2026 3:12 PM
To: West, Jady (CCI-Southwest) <Jady.West@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Jady,
 
Is Cox IT involved with Spectrum IT on this? Lewis and I were just chatting, and marketing has not been involved in the email domains.
 
Not sure what we do here with the BPRF emails. This will be problematic for the brands if we change our domain name. Not sure how this impacts the Helpdesk emails (support, etc) all having BPRF emails.   
 
 
Kathy
 
 
 

 
From: West, Jady (CCI-Southwest) <Jady.West@cox.com>
Sent: Monday, August 17, 2026 3:05 PM
To: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>
Cc: Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Lewis,
 
As Blueprint is coming over in full we will need the email addresses.  Does RapidScale plan to keep their email address? Or Segra?  I assume the answer is yes.
 
Megan,
 
I believe you had noted this in an earlier conversation so I am pulling you in to add any context that you may have here.
 
Jady
________________________________________
From: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Sent: Monday, August 17, 2026 12:01 PM
To: Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>
Subject: FW: [EXTERNAL] Help Needed | Email Addresses
 
Don’t believe this is the response we wanted.  See below please.
 
From: Brannock, Dale <dale.brannock@spectrum.com>
Sent: Monday, August 17, 2026 1:59 PM
To: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
No alias email addresses will be moved from the CCI mailbox to the Spectrum mailbox. It is not technically feasible to have a domain on two separate tenants.
 
Down the line, domain migrations from the CCI tenant to the Spectrum tenant will be performed, and at that time, any alias email address with that domain will be removed from the CCI mailbox and placed on the Spectrum mailbox.
 
Thanks,

Dale
 
From: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Sent: Monday, August 17, 2026 1:55 PM
To: Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance.
 
Is there any way we could keep the blueprintrf.com for our reps as these are related to our relationships with our clients like Marriott, Hyatt, etc.?  This is extremely important.
 
Also, assuming the other emails related to customer support for CPN and HN that I sent over will transfer to spectrum mailbox but just want to confirm. 
 
Thanks
 
Lewis
 
From: Brannock, Dale <dale.brannock@spectrum.com>
Sent: Monday, August 17, 2026 1:46 PM
To: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
On day 1, CCI user mailboxes and shared mailboxes are being duplicated on the Spectrum mail system. Forwarding will be setup on the CCI user and shared mailboxes to forward all mail received to the corresponding Spectrum mailbox. Sending will still be allowed from the CCI mailbox (and any alias such as David.Ruggieri@blueprintrf.com therein). On day 14, CCI mailboxes will lose the ability to send. At that time, all emails will need to be authored from the Spectrum mailbox using the @spectrum.com addresses.
 
Thanks,
 
Dale
 
From: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Sent: Monday, August 17, 2026 1:18 PM
To: Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
Importance: High
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance.
 
I wanted to follow up regarding the email addresses to ensure we have a plan in place for supporting the CPN and HN email domains after Day 1.
 
In addition, I learned this morning that the Blueprint RF sales team utilizes unique email addresses in addition to their standard cox.com accounts.
 
Please see the note I received from the Blueprint RF sales leader below, as it may impact our email transition planning and requirements.
 
BPRF employees all have BlueprintRF emails. 
 
As Cox (CCI) employees transfer to Spectrum this week, Spectrum IT has everyone requesting the Spectrum emails and passwords for Day one in computers. 
 
The Blueprint RF team should keep their Blueprint RF emails. 
 
For instance: David.Ruggieri@blueprintrf.com would stay the same and not transfer to a Spectrum email.
 
This would be important for all BPRF employees - not only for customer consistency but also for the brands we support. All Marriott, Hilton and Hyatt corporate point to the blueprintrf domain. Changing this to Spectrum would be problematic for the brands as well. 
 
Please let me know if we will have all these emails secured on Day 1.
 
Thanks
 
Lewis
 
From: Lemoine, Lewis (CCI-Southeast)
Sent: Tuesday, August 11, 2026 3:22 PM
To: Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <rebecca.rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Team attached are other emails we will need to have with spectrum.com at the end.  These are related to our “Convention Services” team which is part of the Hospitality Network group of businesses. 
 
Please let me know if there are questions.
 
Thanks
 
Lewis
 
From: McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Sent: Tuesday, August 11, 2026 2:36 PM
To: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
Sorry for the confusion. To clarify, the individual users and recipients associated with these email addresses should remain active and transfer to Spectrum.
I also understand that DKIM applies to outbound email. My concern is ensuring continuity for CPNSupport@cox.com. This address serves two business-critical functions:
•	It is connected to CPN’s separate Salesforce instance.
•	Customers use it to open service tickets through Salesforce Email-to-Case.
This is not simply a shared or intermittently monitored mailbox. It is an active customer support channel and part of our case-management workflow. If the @cox.com address must eventually be retired, we will need a replacement address and a coordinated transition plan that preserves inbound customer email and Salesforce Email-to-Case functionality without interruption.
 
Rachael McIntosh
Sr. Manager, Operations
 
C: 404.316.4643
E: rachael.mcintosh@cox.com
Schedule Time With Me:
http://coxpn.info/callRachael
 
From: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Date: Tuesday, August 11, 2026 at 2:15 PM
To: Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
Rachael, since you manage these emails, would you mind providing answers to the questions below please?
 
Thanks

Lewis
 
From: Brannock, Dale <dale.brannock@spectrum.com>
Sent: Tuesday, August 11, 2026 1:13 PM
To: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Maybe I’m not seeing the whole picture—DKIM is related to sending email. I would recommend that no sending addresses or domains change on day 1. These would be more like Spectrum Day activities.
 
It is my understanding thus far that the below is all in response to receiving mail.
 
Can someone clarify the statement “Ensuring that the recipients and owners are the same on both CPN and SPN versions of all emails”. Does this mean that anyone who has access to the mailbox at cox should have access to the corresponding mailbox at Charter? If so, this is already part of the plan.
 
Thanks,

Dale
 
From: Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Sent: Tuesday, August 11, 2026 1:05 PM
To: Brannock, Dale <dale.brannock@spectrum.com>; Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; McIntosh, Rachael (CCI-Atlanta) <Rachael.McIntosh@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance.
 
Hi everyone,
 
I did receive the following request from Rachel McIntosh, who manages these email addresses. 
 
No concern as long as someone can help me with this stuff prior : 
•	Setting up the DKIM and other validations for SPNSupport@spectrum.com in Salesforce 
•	Ensuring that the recipients and owners are the same on both CPN and SPN versions of all emails
 
Please let us know who will be able to assist her with these.
 
Thanks
 
Lewis
 
From: Brannock, Dale <dale.brannock@spectrum.com>
Sent: Tuesday, August 11, 2026 10:13 AM
To: Kim, Amy H <Amy.Kim@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
	Some people who received this message don't often get email from dale.brannock@spectrum.com. Learn why this is important

This is opposite of what was proposed yesterday. We can forward from COX > Spectrum (whatever message lands in the COX mailbox via SMTP, either internal or external, will be forwarded to Spectrum mailbox), but doing the opposite of this is not recommended given that COX mailboxes will only be accessible for 30 days.
 
Thanks,

Dale
 
From: Kim, Amy H <amy.kim@spectrum.com>
Sent: Tuesday, August 11, 2026 10:01 AM
To: Redman, Tom <Tom.Redman@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>; Brannock, Dale <dale.brannock@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Thank you –
To confirm, we are able to use these email addresses externally and the messages will forward to the associated email box?
 
•	External: spectrumprivatenetworks@spectrum.com forwards to coxprivatenetworks@cox.com  
•	External: SBS-SPN@spectrum.com forwards to CBS-CPN@cox.com
•	External: SPNSupport@spectrum.com forwards to CPNSupport@cox.com
 
Amy
 
Amy Kim | Senior Director, Marketing | 203.705.0858
400 Washington Blvd | Stamford, CT 06902
 
  
 
 
From: Redman, Tom <Tom.Redman@spectrum.com>
Sent: Monday, August 10, 2026 6:35 PM
To: Kim, Amy H <amy.kim@spectrum.com>; Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Robson, Jim W <Jim.Robson@spectrum.com>; Brannock, Dale <dale.brannock@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
 
+ Jim and Dale 
 
We did not plan to forward those to specific mailboxes. Our plan was to create a shared mailbox on the charter side for each on the cox side. With this info, we could bypass the creation of a new and forward these as they are set below.
 
________________________________________
From: Kim, Amy H <amy.kim@spectrum.com>
Sent: Monday, 10 August 2026 17:09:35
To: Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>; Makonnen, Yohannes <Yohannes.Makonnen@spectrum.com>; Claudio, Suzel A <Suzel.Claudio@spectrum.com>; West, Sherry A <Sherry.West@spectrum.com>; Redman, Tom <Tom.Redman@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
+ Suzel/Yohannes/Sherry/Tom: Pls let us know if the below are on the list of domain transitions to spectrum.com.
 
•	coxprivatenetworks@cox.com   → spectrumprivatenetworks@spectrum.com
•	CBS-CPN@cox.com  → SBS-SPN@spectrum.com
•	CPNSupport@cox.com  → SPNSupport@spectrum.com
 
Thanks,
Amy
 
 
Amy Kim | Senior Director, Marketing | 203.705.0858
400 Washington Blvd | Stamford, CT 06902
 
  
 
 
From: Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>
Sent: Monday, August 10, 2026 1:03 PM
To: Kim, Amy H <amy.kim@spectrum.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance.
 
•	Coxprivatenetworks@cox.com is a general catch-all that we get inquiries to on occasion. We have found that sometimes leads and vendors will inquire via this email when they cannot locate alternate email addresses or are unsure who would handle something specific.
 
•	CBS-CPN@cox.com is provided on collateral as a follow up email for general inquiries related to sales and support.
 
•	CPNSupport@cox.com is the inbox that is used for our email-to-case support tickets and is tied to our instance of Salesforce for use by our OEM partner systems as well.
 
Rachel McIntosh (Rachael.McIntosh@cox.com) owns these addresses.
 
Rebecca
 
From: Kim, Amy H <amy.kim@spectrum.com>
Sent: Monday, August 10, 2026 5:31 AM
To: Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>; Gupta, Madhvi <Madhvi.Gupta@spectrum.com>
Cc: Torrico, Jessy (CCI-California) <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>
Subject: RE: [EXTERNAL] Help Needed | Email Addresses
 
Hello Rebecca—
Will look into this for you. Can you tell us how these are used, who checks the email box and how often they are utilized?
Thanks,
Amy
 
 
Amy Kim | Senior Director, Marketing | 203.705.0858
400 Washington Blvd | Stamford, CT 06902
 
  
 
 
From: Rosen, Rebecca (CCI-California) <Rebecca.Rosen@cox.com>
Sent: Friday, August 7, 2026 2:34 PM
To: Kim, Amy H <amy.kim@spectrum.com>; Gupta, Madhvi <madhvi.gupta@spectrum.com>
Cc: Jessica.Torrico <Jessica.Torrico@cox.com>; Sims, Cody (CCI-Southwest) <Cody.Sims@cox.com>; Bruce, Dana (CCI-Atlanta) <Dana.Bruce@cox.com>
Subject: [EXTERNAL] Help Needed | Email Addresses
 
	CAUTION: The e-mail below is from an external source. Please exercise caution before opening attachments, clicking links, or following guidance.
 
Hi Amy and Madhvi,  
 
I am not sure where to direct this, but we have a handful of email addresses that are included in customer facing materials.  
 
With email and domain changes impending, we wanted to make sure that these email addresses are being addressed as we’re assuming below.  
 
•	coxprivatenetworks@cox.com   → spectrumprivatenetworks@spectrum.com
•	CBS-CPN@cox.com  → SBS-SPN@spectrum.com
•	CPNSupport@cox.com  → SPNSupport@spectrum.com
 
Is there a way that you can help us validate this information? I am guessing your IT teams are converting our directories while keeping the routing in place, but we would love to have visibility to that as well.
 
Thanks for helping us investigate. Have a nice weekend.
 
Rebecca
 
 	Rebecca Rosen
	Verticals, Product and Content Marketing, Senior Director
	P: 949-563-8435 | Follow me on LinkedIn

	 rebecca.rosen@cox.com
 coxbusiness.com

	 	 
	 
 
 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited.
 

The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 
The contents of this e-mail message and any attachments are intended solely for the addressee(s) and may contain confidential and/or legally privileged information. If you are not the intended recipient of this message or if this message has been addressed to you in error, please immediately alert the sender by reply e-mail and then delete this message and any attachments. If you are not the intended recipient, you are notified that any use, dissemination, distribution, copying, or storage of this message or any attachment is strictly prohibited. 

[File uploaded: ]

### CLAUDE (2026-09-02T12:45)
Here's a completed draft — I kept your point about not wanting your team to re-create an inventory Charter IT can already pull, and led with the non-negotiable (everyone keeps @blueprintrf.com, contractors included):

---

**Subject:** RE: [EXTERNAL] Help Needed | Email Addresses

Megan, Brian —

Dan Apa and Kyle Davis are looped in on my side; between the two of them, Marie Henson, and Julian Cayetano, we can pull together anything specific to my org.

On the underlying ask, though — user identities, distribution lists, and SharePoint sites — most of that should already be visible from our current active tenant rather than something my team needs to compile manually. Can someone from the migration team pull a direct export (Entra/AD for identities and security groups, SharePoint admin center for sites, Exchange admin for DLs and shared mailboxes)? That will be faster and more accurate than a list assembled by hand, and it avoids us missing something that's already sitting in the tenant.

What my team can add on top of that export is the business context — which of those addresses, DLs, and sites are customer- or brand-facing, and why they have to stay in place. Short version, and this doesn't change: everyone with an @blueprintrf.com address — contractors included — keeps it. Most of our B2B NOC ticketing runs through the brand-specific NOC@blueprintrf.com addresses, and Marriott, Hilton, and Hyatt corporate all point to the blueprintrf.com domain for our entire care and support org. Losing that isn't a migration inconvenience — it's an outage for those relationships.

Once we have the tenant export, happy to have Dan or Kyle sit down with Brian's team to reconcile it against what's actually in active use.

Scott

---

Couple of things worth flagging before you send:

1. **The ask for a manual inventory is the real friction point.** Charter IT already has admin access to the tenant — asking your team to hand-build a list of DLs/SharePoint sites they can export themselves is what's making this feel harder than it is. The draft pushes that back explicitly rather than just complying.
2. **"Everyone keeps @blueprintrf.com" is your one immovable line** — I kept it as its own short paragraph so it can't get lost or negotiated away in the back-and-forth.
3. Dale Brannock's earlier reply in the thread said aliases can't live on two tenants and only move at actual domain migration — so at some point Charter IT will push back with that same "not technically feasible" answer. Worth deciding now whether your position is "keep the domain indefinitely" or "keep it until an actual planned domain cutover with notice," since those are different asks and this draft implies the former.

### SCOTT (2026-09-02T13:17)
his reply.
[File uploaded: 1788355044070_image.png]

### CLAUDE (2026-09-02T13:17)
Brian's reply changes the calculus — this isn't stonewalling, it's a genuine scale problem (30k SharePoint sites, 18k DLs org-wide, self-managed) plus a real legal constraint (CEI/Microsoft contract forcing full Cox tenant evacuation by June 2027). Worth reflecting that back to you before the draft: your frustration was fair given how the thread read up to this point, but Brian's answer is substantive, not evasive. That changes what you should be asking for.

A few things his reply raises that the draft below addresses:

1. **He's right that a full self-managed inventory isn't realistic to ask for.** The ask should narrow to what BPRF actually needs identified — brand-facing addresses, DLs, and sites — not the universe of 30k/18k org-wide.
2. **DLs are already migrated to Spectrum**, and you can't send to them from a Cox address, only from Spectrum. If any of your NOC/brand workflows send *to* DLs (not just receive), that's a live gap — worth confirming which direction matters for your operation.
3. **June 2027 full evacuation is a hard deadline** — this is the first time a real date has surfaced. It doesn't contradict Brian's earlier "we'll move blueprintrf.com to Charter and keep it alive" promise (domain moves tenants, addresses persist) — but you should get that confirmed explicitly now that a legal deadline exists, rather than assuming it.
4. **Take the call.** This has gone six rounds in email; a call gets you a real answer on the domain-retention question faster than another thread reply.

---

**Subject:** RE: [EXTERNAL] Help Needed | Email Addresses

Brian —

Understood on scale — asking your team to hand-inventory 30,000 SharePoint sites and 18,000 DLs isn't reasonable, and I appreciate the context on CEI/Microsoft and the June 2027 evacuation deadline.

Let's narrow this to what actually matters for my operation rather than the full self-managed universe:

1. **Domain retention:** Given the June 2027 evacuation date, I want to confirm the earlier plan still holds — blueprintrf.com moves to the Charter/Spectrum tenant and everyone (contractors included) keeps their @blueprintrf.com address. If that's still the plan, I don't need anything further on this point. If the evacuation deadline changes that, I need to know now, not close to cutover.

2. **DLs — send direction matters more than the list itself.** You noted DLs are already migrated to Spectrum and reachable from a Spectrum address but not from Cox. My team sends to and receives from brand-specific DLs (Marriott, Hilton, Hyatt) as part of NOC ticketing. Can you confirm whether that's a send-only limitation (fixed once we're on Spectrum mailboxes) or whether inbound routing from the brands into those DLs is affected? That's the piece that would actually break something.

3. **SharePoint sites — I'll have Dan and Kyle identify the specific BPRF-owned/customer-facing sites** rather than asking your team to surface them from the 30k. Give me a few days to get that list together.

Let's get on a call — faster than working this in email, and I want to walk through the DL send/receive question live.

Scott

---

This keeps your position intact (domain/address retention, NOC continuity) while dropping the parts of the original ask that were genuinely unreasonable to push on Brian's team — which should also take the "they're stalling" edge off future rounds if that turns out not to be the case.

### SCOTT (2026-09-02T13:19)
on #2 - not just my teams, all of our hotel cusotmers, mamage,ent comapnies and copurate brand relationships use these dl's

### CLAUDE (2026-09-02T13:19)
Good catch — that's a materially bigger point than what I had. It's not "my team sends to a DL," it's that Marriott/Hilton/Hyatt corporate, individual property GMs, and management companies all send *into* your NOC/brand DLs as their entry point for support. If migration breaks inbound routing from external senders, that's an outage for the entire BPRF service relationship, not an internal workflow hiccup.

Revised #2:

---

**2. DLs — this isn't just my team's workflow, it's the external intake channel for the entire BPRF relationship.** You noted DLs are already migrated to Spectrum and reachable from a Spectrum address but not from Cox. To be clear on scope: our brand-specific DLs aren't used just by my team — they're the primary point of contact our hotel customers, management companies, and brand corporate offices (Marriott, Hilton, Hyatt) use to reach BPRF support and open NOC tickets. Any of them emailing in externally has to land correctly regardless of which side of the migration we're on. Can you confirm whether the send limitation you described only affects outbound from a Cox mailbox, or whether it also affects inbound routing from external senders into those DLs? If external mail into these DLs is at risk at any point in the migration, that's a customer-facing outage, not an internal one, and I need to know before it happens, not after.

---

That should land the actual stakes without sounding like you're overselling it — the distinction ("your limitation vs. their limitation," "internal vs. customer-facing") is what makes it not negotiable in the way #1 and #3 aren't.

### SCOTT (2026-09-02T13:19)
give me the entire reply

### CLAUDE (2026-09-02T13:19)
**Subject:** RE: [EXTERNAL] Help Needed | Email Addresses

Brian —

Understood on scale — asking your team to hand-inventory 30,000 SharePoint sites and 18,000 DLs isn't reasonable, and I appreciate the context on CEI/Microsoft and the June 2027 evacuation deadline.

Let's narrow this to what actually matters for my operation rather than the full self-managed universe:

1. **Domain retention:** Given the June 2027 evacuation date, I want to confirm the earlier plan still holds — blueprintrf.com moves to the Charter/Spectrum tenant and everyone (contractors included) keeps their @blueprintrf.com address. If that's still the plan, I don't need anything further on this point. If the evacuation deadline changes that, I need to know now, not close to cutover.

2. **DLs — this isn't just my team's workflow, it's the external intake channel for the entire BPRF relationship.** You noted DLs are already migrated to Spectrum and reachable from a Spectrum address but not from Cox. To be clear on scope: our brand-specific DLs aren't used just by my team — they're the primary point of contact our hotel customers, management companies, and brand corporate offices (Marriott, Hilton, Hyatt) use to reach BPRF support and open NOC tickets. Any of them emailing in externally has to land correctly regardless of which side of the migration we're on. Can you confirm whether the send limitation you described only affects outbound from a Cox mailbox, or whether it also affects inbound routing from external senders into those DLs? If external mail into these DLs is at risk at any point in the migration, that's a customer-facing outage, not an internal one, and I need to know before it happens, not after.

3. **SharePoint sites — I'll have Dan and Kyle identify the specific BPRF-owned/customer-facing sites** rather than asking your team to surface them from the 30k. Give me a few days to get that list together.

Let's get on a call — faster than working this in email, and I want to walk through the DL send/receive question live.

Scott

### SCOTT (2026-09-02T13:21)
no need to aprrt back they 30 k and 8k.  he knows what he knows  jsut thaks for the addtioanl detials and context

### CLAUDE (2026-09-02T13:21)
**Subject:** RE: [EXTERNAL] Help Needed | Email Addresses

Brian —

Appreciate the additional detail and context — that's helpful.

Let's narrow this to what actually matters for my operation rather than a full inventory:

1. **Domain retention:** Given the June 2027 evacuation date, I want to confirm the earlier plan still holds — blueprintrf.com moves to the Charter/Spectrum tenant and everyone (contractors included) keeps their @blueprintrf.com address. If that's still the plan, I don't need anything further on this point. If the evacuation deadline changes that, I need to know now, not close to cutover.

2. **DLs — this isn't just my team's workflow, it's the external intake channel for the entire BPRF relationship.** You noted DLs are already migrated to Spectrum and reachable from a Spectrum address but not from Cox. To be clear on scope: our brand-specific DLs aren't used just by my team — they're the primary point of contact our hotel customers, management companies, and brand corporate offices (Marriott, Hilton, Hyatt) use to reach BPRF support and open NOC tickets. Any of them emailing in externally has to land correctly regardless of which side of the migration we're on. Can you confirm whether the send limitation you described only affects outbound from a Cox mailbox, or whether it also affects inbound routing from external senders into those DLs? If external mail into these DLs is at risk at any point in the migration, that's a customer-facing outage, not an internal one, and I need to know before it happens, not after.

3. **SharePoint sites — I'll have Dan and Kyle identify the specific BPRF-owned/customer-facing sites** rather than asking your team to surface them from the full tenant. Give me a few days to get that list together.

Let's get on a call — faster than working this in email, and I want to walk through the DL send/receive question live.

Scott

### SCOTT (2026-09-02T13:24)
and what about the down time?  not sure how my teams can operae if they are down for an wntie weekend.  surely there are some mitigation steps we can tak.  temporary forwards while we move one at a time or something?

### CLAUDE (2026-09-02T13:24)
**Subject:** RE: [EXTERNAL] Help Needed | Email Addresses

Brian —

Appreciate the additional detail and context — that's helpful.

Let's narrow this to what actually matters for my operation rather than a full inventory:

1. **Domain retention:** Given the June 2027 evacuation date, I want to confirm the earlier plan still holds — blueprintrf.com moves to the Charter/Spectrum tenant and everyone (contractors included) keeps their @blueprintrf.com address. If that's still the plan, I don't need anything further on this point. If the evacuation deadline changes that, I need to know now, not close to cutover.

2. **DLs — this isn't just my team's workflow, it's the external intake channel for the entire BPRF relationship.** You noted DLs are already migrated to Spectrum and reachable from a Spectrum address but not from Cox. To be clear on scope: our brand-specific DLs aren't used just by my team — they're the primary point of contact our hotel customers, management companies, and brand corporate offices (Marriott, Hilton, Hyatt) use to reach BPRF support and open NOC tickets. Any of them emailing in externally has to land correctly regardless of which side of the migration we're on. Can you confirm whether the send limitation you described only affects outbound from a Cox mailbox, or whether it also affects inbound routing from external senders into those DLs? If external mail into these DLs is at risk at any point in the migration, that's a customer-facing outage, not an internal one, and I need to know before it happens, not after.

3. **SharePoint sites — I'll have Dan and Kyle identify the specific BPRF-owned/customer-facing sites** rather than asking your team to surface them from the full tenant. Give me a few days to get that list together.

4. **Cutover downtime:** A full weekend outage isn't something my team can absorb — NOC ticketing and brand-facing support run continuously, including weekends. Before we land on that approach, I want to understand what mitigation options exist: staggered/phased migration by mailbox or DL rather than a single cutover, temporary forwarding from Cox to Spectrum during the transition window, or some form of dual-delivery while we move pieces over one at a time. If a hard cutover really is the only option, I need to know the exact window as far in advance as possible so we can staff around it and give our brand contacts a heads-up.

Let's get on a call — faster than working this in email, and I want to walk through the DL send/receive and downtime mitigation questions live.

Scott

### SCOTT (2026-09-03T16:04)
had a call with the specturm migration team.  I am sending this update email to the bprf leadership.  help me compete it for both detail and accuracy.

Hi Guys,
 
We had a call with Spectrum migration team, and we have a bit of work to do as they prepare to migrate the blueprintrf.com domain over to Spectrum.  This is bigger than just email.  This is everything you use your “@blueprintrf.com” email address to log in to.  Think Salesforce, Blueprint One, Zendesk,  OAB, SharePoint, distribution list workflows, etc. etc.
 
On the call, the team stated that the Rapidscale Salesforce instance is moving to its own independent instance outside of Spectrum, and that the Rapidscale team is handling this move on their own.  If our Salesforce instance is still hanging off the Rapidscale instance, then we will need to solve for this.  [@McIntosh, Rachael (CCI-Atlanta)](mailto:Rachael.McIntosh@cox.com) – can you confirm whether or not we are still a part of the Rapidscale Salesforce instance?
 
Below is the start list that we were provide.  There is most likely more to this list we need to identify and think about but this should get us started. 
 
 

* All User Identities needing to maintain the BluePrintRF domain email addresses
* All Application Registrations (SSO apps) that need to migrate
   * PowerBI
   * Salesforce
   * Etc.
* All Security Groups specific to BluePrintRF
* All Teams Groups (Sharepoint backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
* All SharePoint Sites that are owned/managed by BlueprintRF
* All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns 
* All Email Distribution lists owned or managed by BluePrintRF
* All Lucid spaces that need to be migrated for support

### CLAUDE (2026-09-03T16:05)
I don't have the outcomes of the call itself — did they confirm domain retention holds, what they said on downtime/cutover mitigation, and whether inbound DL routing from external senders is at risk? I don't want to guess at those and put wrong information in front of leadership. I've drafted the parts I can complete accurately (task breakdown, owners, structure) and flagged the three items where I need you to fill in what was actually said.

---

Hi Guys,

We had a call with the Spectrum migration team, and we have a bit of work to do as they prepare to migrate the blueprintrf.com domain over to Spectrum. This is bigger than just email. This is everything you use your "@blueprintrf.com" email address to log in to. Think Salesforce, Blueprint One, Zendesk, OAB, SharePoint, distribution list workflows, etc. etc.

On the call, the team stated that the Rapidscale Salesforce instance is moving to its own independent instance outside of Spectrum, and that the Rapidscale team is handling this move on their own. If our Salesforce instance is still hanging off the Rapidscale instance, then we will need to solve for this. [@McIntosh, Rachael (CCI-Atlanta)](mailto:Rachael.McIntosh@cox.com) – can you confirm whether or not we are still a part of the Rapidscale Salesforce instance?

**Three items I raised on the call that leadership should be aware of:**

* **Domain/address retention:** [fill in — did they reconfirm blueprintrf.com moves to the Charter tenant and all users, contractors included, keep their addresses? Any change tied to the June 2027 evacuation deadline?]
* **DL inbound routing:** Our brand-specific DLs (NOC, support) aren't just internal — they're the intake channel our hotel customers, management companies, and Marriott/Hilton/Hyatt corporate use to reach BPRF. [fill in — did they confirm external inbound mail into these DLs is protected during migration, or is this still open?]
* **Cutover downtime:** [fill in — what did they say about staggered migration, temporary forwarding, or dual-delivery vs. a single hard-cutover weekend? NOC and brand support run continuously including weekends, so an unmitigated full-weekend outage is a real operational risk.]

Below is the start list they provided. There is most likely more to this we need to identify and think about, but this should get us started:

* All User Identities needing to maintain the BluePrintRF domain email addresses
* All Application Registrations (SSO apps) that need to migrate
   * PowerBI
   * Salesforce
   * Zendesk
   * OAB
   * Etc.
* All Security Groups specific to BluePrintRF
* All Teams Groups (SharePoint-backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
* All SharePoint Sites that are owned/managed by BlueprintRF
* All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns
* All Email Distribution lists owned or managed by BluePrintRF
* All Lucid spaces that need to be migrated for support

**Next steps on our side:** I've asked Dan and Kyle to pull together the SharePoint sites and application registrations specific to our team's operations rather than waiting on a full tenant-wide inventory from Charter IT — given the scale (30,000+ SharePoint sites, 18,000+ DLs org-wide), a self-managed org-by-org identification is faster and more accurate than a centrally-generated list. I'll circulate that once it's ready.

Scott

---

Once you tell me what was actually said on those three points, I can also tighten the "next steps" section — right now it only reflects the SharePoint/app-registration piece, not whatever follow-up the domain/DL/downtime answers require.

### SCOTT (2026-09-03T16:08)
for the domain email, they said the end result is that we will all have @bleuprintrf.com emails as our primart adn @spectrum and @charter and alias's. 

no timing yet on when the migration will happen but they are qantign to move quickly .  it will create somedowntine with our cusotmer facing email workflow distro's, but i will woork with the teams to fevleop contingency and commucatin plans before this happens.

### CLAUDE (2026-09-03T16:08)
**Subject:** RE: Blueprint RF → Spectrum Domain Migration Update

Hi Guys,

We had a call with the Spectrum migration team, and we have a bit of work to do as they prepare to migrate the blueprintrf.com domain over to Spectrum. This is bigger than just email. This is everything you use your "@blueprintrf.com" email address to log in to. Think Salesforce, Blueprint One, Zendesk, OAB, SharePoint, distribution list workflows, etc. etc.

On the call, the team stated that the Rapidscale Salesforce instance is moving to its own independent instance outside of Spectrum, and that the Rapidscale team is handling this move on their own. If our Salesforce instance is still hanging off the Rapidscale instance, then we will need to solve for this. [@McIntosh, Rachael (CCI-Atlanta)](mailto:Rachael.McIntosh@cox.com) – can you confirm whether or not we are still a part of the Rapidscale Salesforce instance?

**Three items I raised on the call that leadership should be aware of:**

* **Domain/address retention — confirmed.** The end result will be that everyone keeps @blueprintrf.com as their primary address, with @spectrum.com and @charter.com set up as aliases. No timing has been set yet for when the domain migration itself will happen, but the team indicated they're aiming to move quickly.
* **Cutover downtime — expected, mitigation TBD.** The team confirmed there will be some downtime affecting our customer-facing email workflows and distribution lists during the migration. I'll be working with the teams to develop contingency and communication plans before this happens — for both our internal teams and, where needed, a heads-up to our brand and customer contacts.
* **DL inbound routing:** Still open — I haven't gotten confirmation on whether external mail into our brand-specific DLs (from hotel customers, management companies, and Marriott/Hilton/Hyatt corporate) is protected during the downtime window, or whether that's part of what the downtime will affect. I'll follow up on this specifically as we build the contingency plan.

Below is the start list they provided. There is most likely more to this we need to identify and think about, but this should get us started:

* All User Identities needing to maintain the BluePrintRF domain email addresses
* All Application Registrations (SSO apps) that need to migrate
   * PowerBI
   * Salesforce
   * Zendesk
   * OAB
   * Etc.
* All Security Groups specific to BluePrintRF
* All Teams Groups (SharePoint-backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
* All SharePoint Sites that are owned/managed by BlueprintRF
* All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns
* All Email Distribution lists owned or managed by BluePrintRF
* All Lucid spaces that need to be migrated for support

**Next steps on our side:** I've asked Dan and Kyle to pull together the SharePoint sites and application registrations specific to our team's operations rather than waiting on a full tenant-wide inventory from Charter IT — given the scale (30,000+ SharePoint sites, 18,000+ DLs org-wide), a self-managed org-by-org identification is faster and more accurate than a centrally-generated list. I'll also be working through the downtime contingency and communication plan and will share that once it's further along, including the answer on DL inbound routing.

Scott

### SCOTT (2026-09-03T16:10)
"DL inbound routing: Still open — I haven't gotten confirmation on whether external mail into our brand-specific DLs (from hotel customers, management companies, and Marriott/Hilton/Hyatt corporate) is protected during the downtime window, or whether that's part of what the downtime will affect. I'll follow up on this specifically as we build the contingency plan"

they said will be downtime but emaisl will be queued, nit rejected

### CLAUDE (2026-09-03T16:11)
**Subject:** RE: Blueprint RF → Spectrum Domain Migration Update

Hi Guys,

We had a call with the Spectrum migration team, and we have a bit of work to do as they prepare to migrate the blueprintrf.com domain over to Spectrum. This is bigger than just email. This is everything you use your "@blueprintrf.com" email address to log in to. Think Salesforce, Blueprint One, Zendesk, OAB, SharePoint, distribution list workflows, etc. etc.

On the call, the team stated that the Rapidscale Salesforce instance is moving to its own independent instance outside of Spectrum, and that the Rapidscale team is handling this move on their own. If our Salesforce instance is still hanging off the Rapidscale instance, then we will need to solve for this. [@McIntosh, Rachael (CCI-Atlanta)](mailto:Rachael.McIntosh@cox.com) – can you confirm whether or not we are still a part of the Rapidscale Salesforce instance?

**Three items I raised on the call that leadership should be aware of:**

* **Domain/address retention — confirmed.** The end result will be that everyone keeps @blueprintrf.com as their primary address, with @spectrum.com and @charter.com set up as aliases. No timing has been set yet for when the domain migration itself will happen, but the team indicated they're aiming to move quickly.
* **Cutover downtime — expected, mitigation TBD.** The team confirmed there will be some downtime affecting our customer-facing email workflows and distribution lists during the migration. Importantly, they confirmed mail during that window will be **queued, not rejected or bounced** — so we shouldn't lose inbound email from hotel customers, management companies, or brand corporate contacts, but there will be a delay in delivery. I'll be working with the teams to develop contingency and communication plans before this happens — for both our internal teams and, where needed, a heads-up to our brand and customer contacts, since even a delay could affect ticket response times.

Below is the start list they provided. There is most likely more to this we need to identify and think about, but this should get us started:

* All User Identities needing to maintain the BluePrintRF domain email addresses
* All Application Registrations (SSO apps) that need to migrate
   * PowerBI
   * Salesforce
   * Zendesk
   * OAB
   * Etc.
* All Security Groups specific to BluePrintRF
* All Teams Groups (SharePoint-backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
* All SharePoint Sites that are owned/managed by BlueprintRF
* All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns
* All Email Distribution lists owned or managed by BluePrintRF
* All Lucid spaces that need to be migrated for support

**Next steps on our side:** I've asked Dan and Kyle to pull together the SharePoint sites and application registrations specific to our team's operations rather than waiting on a full tenant-wide inventory from Charter IT — given the scale (30,000+ SharePoint sites, 18,000+ DLs org-wide), a self-managed org-by-org identification is faster and more accurate than a centrally-generated list. I'll also be working through the downtime contingency and communication plan and will share that once it's further along.

Scott

### SCOTT (2026-09-03T16:21)
add a sentence to the end that I need them to start making a list of all apps that they and their teams use their @blueprintrf.com to log into . What is normal for these folks is that they will ignore these types of asks until the last minute or after shit breaks. So let's tell them something to the effect that i need their help to know what all apps they are using.  that once this migration happens they will lose access to any apps we do not properly identify and configure in advnce of this migration

### CLAUDE (2026-09-03T16:22)
**Subject:** RE: Blueprint RF → Spectrum Domain Migration Update

Hi Guys,

We had a call with the Spectrum migration team, and we have a bit of work to do as they prepare to migrate the blueprintrf.com domain over to Spectrum. This is bigger than just email. This is everything you use your "@blueprintrf.com" email address to log in to. Think Salesforce, Blueprint One, Zendesk, OAB, SharePoint, distribution list workflows, etc. etc.

On the call, the team stated that the Rapidscale Salesforce instance is moving to its own independent instance outside of Spectrum, and that the Rapidscale team is handling this move on their own. If our Salesforce instance is still hanging off the Rapidscale instance, then we will need to solve for this. [@McIntosh, Rachael (CCI-Atlanta)](mailto:Rachael.McIntosh@cox.com) – can you confirm whether or not we are still a part of the Rapidscale Salesforce instance?

**Three items I raised on the call that leadership should be aware of:**

* **Domain/address retention — confirmed.** The end result will be that everyone keeps @blueprintrf.com as their primary address, with @spectrum.com and @charter.com set up as aliases. No timing has been set yet for when the domain migration itself will happen, but the team indicated they're aiming to move quickly.
* **Cutover downtime — expected, mitigation TBD.** The team confirmed there will be some downtime affecting our customer-facing email workflows and distribution lists during the migration. Importantly, they confirmed mail during that window will be **queued, not rejected or bounced** — so we shouldn't lose inbound email from hotel customers, management companies, or brand corporate contacts, but there will be a delay in delivery. I'll be working with the teams to develop contingency and communication plans before this happens — for both our internal teams and, where needed, a heads-up to our brand and customer contacts, since even a delay could affect ticket response times.

Below is the start list they provided. There is most likely more to this we need to identify and think about, but this should get us started:

* All User Identities needing to maintain the BluePrintRF domain email addresses
* All Application Registrations (SSO apps) that need to migrate
   * PowerBI
   * Salesforce
   * Zendesk
   * OAB
   * Etc.
* All Security Groups specific to BluePrintRF
* All Teams Groups (SharePoint-backed) that files need to migrate (Teams will not migrate, but the files behind the Team can)
* All SharePoint Sites that are owned/managed by BlueprintRF
* All Shared Mailboxes (non-user mailboxes) BluePrintRF uses/owns
* All Email Distribution lists owned or managed by BluePrintRF
* All Lucid spaces that need to be migrated for support

**Next steps on our side:** I've asked Dan and Kyle to pull together the SharePoint sites and application registrations specific to our team's operations rather than waiting on a full tenant-wide inventory from Charter IT — given the scale (30,000+ SharePoint sites, 18,000+ DLs org-wide), a self-managed org-by-org identification is faster and more accurate than a centrally-generated list. I'll also be working through the downtime contingency and communication plan and will share that once it's further along.

I also need each of you to start a list now — today, not closer to cutover — of every application your team logs into using an @blueprintrf.com credential. If we don't identify and properly configure an app in advance, your team will lose access to it once the migration happens, full stop. This isn't a "get to it when you can" item — please start compiling this and send it to me as you go.

Scott
