# WiFi installation dispute at Hyatt property
Date: 2026-07-02
Conversation: e71aa0e7-962d-4b6d-8970-0047a0955e6e
Domain: business-ops

## Summary
**Conversation Overview**

Scott works at CCI Blueprint RF in a leadership role (likely VP or Director level based on context) and was seeking help with two related tasks involving a disputed Wi-Fi installation at Hyatt Place San Francisco (property code SFOZS). His company designs and installs enterprise Wi-Fi systems for hospitality clients, and Hyatt is a key account relationship. Key internal colleagues mentioned include Tony Thompson (Field Operations Manager), Wynn, Ray, Cyrus (network/configuration engineer), and Marie (appears to lead the TDE/technical design engineer team). On the Hyatt corporate side, David is a contact Scott knows personally from the industry (met at HITEC conference) who has moved to the hotel brand side. The property's GM and a maintenance manager named Anthony Salinas are also involved, with Stonebridge Companies as the hotel management company; Scott Barker is noted as a Stonebridge contact who declined a review call in favor of dispatching a tech.

For the first task, Scott provided a rough, typo-heavy internal email draft and asked Claude to clean it up to be professional and friendly for sending to David at Hyatt corporate. The context was a billing dispute: a completed $60K installation is being withheld by the property GM citing guest complaints (slow lobby speeds, dropped video calls on floors 9 and 10, roaming issues in stairwells and elevators), despite heatmaps showing coverage within standard and the property's own maintenance manager confirming roaming improvements. Claude produced a polished single draft that preserved Scott's key arguments while softening combative phrasing, and flagged a strategic vulnerability — the absence of a basement engineering AP not being on the approved design — as a point the GM could use as leverage.

For the second task, Scott shared a follow-up from David citing "best practices" around channel width configuration (specifically 40 MHz on 2.4 GHz and 5 GHz bands, visible in a Ruckus ChannelFly screenshot), and asked Claude — before reacting — whether this was a legitimate technical point his team should have known or whether David was overreaching. Claude confirmed that the 2.4 GHz at 40 MHz setting is a genuine and well-documented industry error that the TDE and Cyrus's configuration review should have caught, explaining the interference math specific to the 2.4 GHz band and noting it contradicts Ruckus's own high-density design documentation. Claude assessed the 5 GHz at 40 MHz point as a defensible judgment call, not a clear miss. Claude then gave Scott a concrete strategic sequence: fix the 2.4 GHz setting remotely (no truck roll needed), use that as evidence that this was never an install deficiency, and keep the invoice dispute factually separated from the config optimization. Claude also flagged that Scott's prior email asserting the system had been reviewed and was within standard now looks inconsistent on the record, and recommended waiting for Mike Penny's technical validation before conceding anything in writing. Scott's communication style is direct, informal, and candid internally; he adjusts to professional and diplomatic for external correspondence. He prefers plain-language strategic framing alongside technical accuracy.

### SCOTT (2026-07-02T17:41)
email I need to send to david at hyatt corporate aboiut one o fhis hotels.  help me clean it up.  I want it to be profesionnal and firendly.   thread bekow and a copule of relevant threads attached

Hi David,
It was great seeing you at HITEC.  With you being on the hotel brand side now, I am sure it was a very different experience from years past.
I was hoping I could get your assistance on something.  Please see the thread below and attachments.  
For this hotel, the installation was completed as per the design, and we have heatmaps that show coverage well within the standards.  However, the GM is saying we are not complete and cites one of two guest complaints as reasoning to withhold payment and insist on us sending a tech out. Candidly, I'm not inclined to eat those costs when our heat maps show good.  
As you know, there are many contributors that could cause an isolated guest wi-fi issue.  Not sure what this hotel has with regards to ISP bandwidth, but that may be at pay here since we have seen it at other Hyatt hotels (and the fix coming with your Supercharged Wi-Fi) initiative.
Anyway, I was wondering if you had suggestions on how we could proceed or might be willing to liaise for us with this property.
We want the hotels to be happy with our services and we are more than willing to make reasonable accommodations and concessions to ensure same.  But a Hotel holding up a $60K install invoice and demanding techs and refusing to even get on a call to discuss, just not the making of a good partnership, and I am hoping you might be able to assist there.
From: Thompson, Tony (CCI-Blueprint RF) <tony.thompson@blueprintrf.com> 
Sent: Wednesday, July 1, 2026 6:20 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>
Subject: SFOZS WiFi Issues
Scott, This is the hotel we talked about.  I've attached a couple of different email threads above.  Below is the history on the complaint.  
1.	 The hotel said we didn't complete install because there was no AP in the Engineering area of the basement.  There was not one on the design so we referred it back to Sales.  Please note the heatmap is solid green on the basement except for the parking area.  
2.	Wynn had Cyrus go through the network and check configurations etc.  The property IT, Anothony Salinas reported that the roaming issues were corrected but that 2 guest had complained about slow speeds in Lobby and three guests had complained about dropped video calls on the 9th and 10th floors.
3.	When Wynn followed up and it seems the GM still has complaints about dropped signal when roaming but it appears that the major complaint is the stairways and elevators.
What we have done:
Wynn and Ray verified that all of the installed AP were online.
Had Cyrus review the system for any configuration issues.
We all reviewed the heatmap.
We requested a call with the property and IT to discuss the current state, however, they want a tech dispatched to correct what they perceive as install issues.  
I could not get the heatmap to compress small enough to send via email.  
Kind regards, 
 
 	 	Tony Thompson, PMP (he/him)
Field Operations Manager
Hospitality Group
 
CCI - Blueprint RF
6250 Peachtree Dunwoody Rd
Sandy Springs, GA 30328
 
Cell – 678.446.4906
[File uploaded: EXTERNAL Re BPRFSFOZS.msg]
[File uploaded: EXTERNAL Hyatt Place San Francisco Wi-Fi.msg]

### CLAUDE (2026-07-02T17:42)
Scott needs his email polished for a professional tone while keeping it friendly—I should draft it as a single, clean version suitable for a written record to David at Hyatt corporate. I'll remove the candid language about costs and reframe it diplomatically, plus fix any typos. Let me check those attached .msg files to see the original content.

I need to be careful about the name collision here—Scott's email is addressed to David at Hyatt corporate, but the property GM is also David Cook. I should reference the GM by property name (Hyatt Place San Francisco / SFOZS) to avoid confusion, and note that Stonebridge Companies is the management company involved.

Now I'm cleaning up the email itself: softening the tone from Scott's candid draft while keeping it direct and professional, fixing typos like "at pay here" to "at play here," and removing any language that reads as an admission of fault. I'll compose a single polished email variant that weaves in the key facts—the install was completed per design, heatmaps show coverage within standard, complaints are isolated (2 lobby slow-speed issues, 3 dropped video calls on the 9th/10th floors), roaming improved per the property's own maintenance manager—while addressing the invoice holdback and the property's reluctance to take a call. The subject line will be "Hyatt Place San Francisco (SFOZS) – Wi-Fi Install / Assistance Request" to keep things clear and professional.I've reviewed the threads and cleaned up the draft to avoid name confusion, soften language that might not hold up if forwarded, and fix typos — the facts now speak for themselves without inflammatory phrasing.

One thing worth a quick gut-check before you send: the June 24 note from Scott Barker (Stonebridge) explicitly declined another call in favor of a dispatch, so "declining to review the technical data with us" is defensible but pointed — if you want it a notch softer, "the property has preferred a dispatch over a technical review call" makes the same point with less edge. Also flagging that the original design had no AP in the basement engineering area; if David digs in, that's the one item where the property has a toehold, so having Tony's referral-back-to-Sales paper trail handy would be useful.

### SCOTT (2026-07-07T13:52)
latest ont his thread.  daivd is kind o fpissing me off quitong these "best practives" we design, and install to a standard that he sets.  and is bull shot if he think i have to now design and install to his AI.  Before I overreact, is this some sort of baisc knoweldge my tde shoudl ahve known but missed?
[File uploaded: FW_ [EXTERNAL] RE_ Hyatt Place San Francisco (SFOZS) – Wi-Fi Install _ Request for Guidance.pdf]

### CLAUDE (2026-07-07T13:53)
Scott's asking whether his TDE missed a basic wireless best practice by using 40 MHz channel width on 2.4 GHz and 5 GHz. The honest answer is yes for 2.4 GHz — bonding 40 MHz channels in a high-density hospitality environment goes against established industry standards, since the 2.4 GHz band only has about 83.5 MHz of spectrum with just three non-overlapping channels available.

On 5 GHz, it's more defensible — 40 MHz is common in hotel deployments depending on AP density and DFS channel availability, though 20 MHz is often recommended for very high-density environments. The screenshot shows Ruckus ChannelFly with 40 MHz on 2.4 GHz, which contradicts Ruckus's own documentation recommending 20 MHz for that band. Whether this misconfiguration actually explains the reported issues — slow lobby speeds and dropped video calls on higher floors — is worth investigating, since 2.4 GHz interference could definitely contribute to those problems.

The real strategic shift here is that David found a legitimate, well-documented best-practice error that Cyrus should have caught during the configuration review. This undermines Scott's position that everything was properly configured and makes the "$60K due and payable" stance riskier. The move is to fix the 2.4 GHz bandwidth setting remotely, get Mike Penny to validate the change, then reposition the conversation around what was actually remediated versus what remains unresolved.Straight answer, before Mike even weighs in: **yes, the 2.4 GHz point is legitimate, and your TDE should have caught it.** David's sourcing was lazy, but his substance on that one is correct.

Here's the breakdown:

**2.4 GHz at 40 MHz — a real miss.** The 2.4 GHz band is only ~83 MHz wide, which gives you exactly three non-overlapping 20 MHz channels (1, 6, 11). Bond to 40 MHz and you consume most of the band with a single channel — in a multi-AP hotel deployment, that guarantees co-channel interference between your own APs, plus interference from microwaves, Bluetooth, and neighboring networks. This isn't a Hyatt standard or an AI hallucination; it's CWNA-level fundamentals and it's in Ruckus's own design documentation (the screenshot shows ChannelFly, so this is Ruckus gear — their high-density design guides say 20 MHz on 2.4). Any TDE doing hospitality Wi-Fi should know it cold. It's also configurable in the controller in about two minutes, which cuts both ways — easy to fix, but also should have been caught when Cyrus did the config review.

**5 GHz at 40 MHz — defensible, not a miss.** This one is genuinely a judgment call. 40 MHz on 5 GHz is common and acceptable in moderate-density deployments; the very-high-density guidance is 20 MHz, but plenty of properly designed hotels run 40. If David lumps this in with the 2.4 issue, that's him overreaching, and Mike can push back on that half.

**Does it explain the complaints? Only partially.** Most modern guest devices prefer 5/6 GHz, so a 2.4 misconfiguration is unlikely to be the whole story behind lobby speeds or dropped video calls on the 9th/10th. And the stairwell/elevator roaming complaints are a coverage/physics issue, not a channel-width issue — no config change fixes concrete shafts that weren't in the approved design. So fixing this probably improves things at the margin but doesn't necessarily make the GM's complaints disappear.

**What this means for your positioning:** The hard-line "$60K due and payable" note got riskier, because David found a genuine config error *after* your email asserted the system had been reviewed and was within standard. If you take the hard line now and he forwards your email alongside his findings, you look wrong on the record. The stronger play is to separate the two issues explicitly:

1. Concede the 2.4 GHz point cleanly and fix it remotely today — no truck roll required, which itself proves the point that this was never an "install issue" requiring a dispatched tech.
2. Then hold the line on the invoice: a remotely-correctable radio setting is a config optimization, not an incomplete installation, and it doesn't touch the AP-not-on-approved-design claim the GM is actually using to withhold payment.

That sequence lets you give David a win on the technical point (which he'll appreciate and which buys his advocacy with the property) while keeping the $60K completely severed from it. Wait for Mike to confirm before conceding anything in writing — but I'd bet Mike comes back agreeing on 2.4 and pushing back on 5.

One more thing worth doing before your next reply to David: have someone confirm whether the 40 MHz setting was BPRF's hand config or a controller default that ChannelFly/initial provisioning left in place. It doesn't change the fix, but it changes your internal coaching conversation with Marie's team — and whether "Cyrus reviewed configurations" needs a harder look as a QA process gap.
