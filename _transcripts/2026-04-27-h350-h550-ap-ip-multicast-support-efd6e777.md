# H350/H550 AP IP multicast support
Date: 2026-04-27
Conversation: efd6e777-4e2e-4b67-9527-b8d75e0f8aef
Domain: business-ops

## Summary
**Conversation Overview**

The person works at Blueprint RF (likely in a Technical Design Engineer or field-facing role, given Brian Napier's explicit callout of "Scott" as the TDE who will be "at the frontline" of the deployment) and is part of a multi-stakeholder email thread evaluating a proposed IPTV deployment for an independent new-build hotel called StayAPT. The conversation began with the person asking Claude whether Ruckus H350/H550 access points support IP multicast, then shifted to a writing assistance task: refining a draft email reply to a thread about the technical and business risks of the proposed IPTV architecture.

The technical discussion centered on whether Ruckus H350/H550 wall-plate APs can reliably support an IPTV solution where each AP serves both Wi-Fi and wired IPTV delivery via a LAN port, with both ports assigned to the same IPTV VLAN. Key terminology used included IGMP snooping, Directed Multicast, SmartCast, GRE tunneling, IPTV VLAN, FTG, multicast flooding, and IGMP querier. The IPTV vendor is MVM Technologies using a Dish solution. The person's draft reply asked clarifying questions about the physical topology ("jumper cable" interpretation), whether STBs are involved, and whether any GRE overlay is in play, while noting the H350/H550 support multicast via SmartCast but not full Layer 3 routing.

Claude refined the draft into a polished professional email, preserving the person's clarifying questions while sharpening technical framing, adding TDE ops risk perspective (post-install multicast flooding, support burden), and maintaining a tone that supports taking the deal with guardrails rather than blocking it. Key colleagues mentioned include Brian Napier (Senior Sales Engineer, who originated the thread), Markos Prifti (Engineering SME at CCI-Southwest), and several other stakeholders across Blueprint RF and Cox. The person demonstrated a pattern of wanting to appear technically credible without overclaiming expertise ("I am not the techie here"), and Claude's revision preserved that posture while strengthening the substance.

### SCOTT (2026-04-27T15:40)
does the H350/H550 AP's support IP multicast?

### CLAUDE (2026-04-27T15:41)

Short answer: **yes, with nuance** — the H350 and H550 support IP multicast, but primarily through Ruckus' **SmartCast** framework (IGMP snooping + Directed Multicast), not full Layer 3 multicast routing.

Here's how it breaks down:

**What they support:**
- **IGMP snooping** — through SmartCast, all APs and mesh nodes are aware of multicast group membership tables, ensuring consistent multicast service across the wireless network.
- **Directed Multicast** — Ruckus' proprietary multicast-to-unicast conversion for wireless clients (first 5 IGMP group members). This is particularly relevant for IPTV and video streaming, which is a primary use case for the H-series wall plates.
- **SmartCast traffic prioritization** — the H550 specifically includes the SmartCast engine to maximize reliability and performance of video and IP-based voice over Wi-Fi networks.

**Practical context for hospitality/MDU deployments:**
- Both the H350 and H550 are explicitly designed to connect IPTV set-top boxes and IP phones, so multicast delivery (particularly for IPTV streams) is a core, validated use case for these APs.
- IGMP snooping can be configured per LAN port and WLAN, and is manageable through SmartZone, ZoneDirector, or Unleashed.

**What they don't do:**
- They don't perform Layer 3 multicast routing (PIM-Sparse/Dense). That function sits upstream on your routing infrastructure (or ICX switches if you're using Ruckus switching).

**Bottom line:** If you're asking because of IPTV or a similar multicast video/audio service being delivered to wired or wireless in-room devices, the H350/H550 are well-suited for that. If you need multicast to cross VLAN boundaries, that's handled by your upstream router/switch — not the AP itself.

What's the specific use case you're evaluating this for?

### SCOTT (2026-04-27T15:43)
read my draft beginning reply and the rest of the thread and help with the reply

You say “jumper cable,”  do you mean there will be a homerun cable from the IDF switch to an AP in every single room, and then one of the ports on the AP will be patched over to the TV for the IPTV solution?  Is there any sort of GRE soltuon in pale?  Are there STB’s going oin?  If so, which ones?
 
I am not the techie here, but base don some brief research, it looks like the H350 and H550 support IP multicast, but primarily through Ruckus' SmartCast framework (IGMP snooping + Directed Multicast), not full Layer 3 multicast routing.
 
From: Napier, Brian (CCI-Bluprint RF) <[brian.napier2@blueprintrf.com](mailto:brian.napier2@blueprintrf.com)> Sent: Monday, April 27, 2026 10:58 AM To: Watts, Scott (CCI-Blueprint RF) <[scott.watts@blueprintrf.com](mailto:scott.watts@blueprintrf.com)>; Prifti, Markos (CCI-Southwest) <[Markos.Prifti@cox.com](mailto:Markos.Prifti@cox.com)>; Peeples, Joe (CCI-Southwest) <[Joe.Peeples@cox.com](mailto:Joe.Peeples@cox.com)>; Hatala, Kathy (CCI-Atlanta) <[Kathy.Hatala@cox.com](mailto:Kathy.Hatala@cox.com)>; Moore, Aaron (CCI-Bluprint RF) <[amoore@blueprintrf.com](mailto:amoore@blueprintrf.com)>; Thompson, Tony (CCI-Blueprint RF) <[tony.thompson@blueprintrf.com](mailto:tony.thompson@blueprintrf.com)>; Cayetano, Julian (CCI-Bluprint RF) <[Julian.Cayetano@blueprintrf.com](mailto:Julian.Cayetano@blueprintrf.com)>; Henson, Marie (Blueprint RF) <[marie.henson@blueprintrf.com](mailto:marie.henson@blueprintrf.com)> Subject: StayAPT Hotel - IPTV Question
 
All,
 
We have a pending design with an Independent New Build hotel who is looking to implement a unique ITPV deployment to save on cabling costs. From my knowledge of IPTV and multicasting, I believe this may result in issues with streaming and know brands such as Hilton do not allow for this, however the IPTV Vendor is adamant they have deployed this exact scenario with no issues and is what they recommend for new builds.
 
We need to decide as a company if this opportunity is worth the potential risks of this request:
 
The Setup:

* They want to run 1x cable run per room with a jumper cable so that the H350/H550 AP can service both IPTVs.
* Hotel will deploy a 1:1 ratio so every room has an AP.
* IPTV Vendor is MVM Technologies which will utilize a Dish solution for FTG and IPTV.
* IPTV vendor says no special requirements needed. Ports on AP to both be assigned to the same designated IPTV VLAN.
 
The Risk:

* Extended downtime at install for additional configuration and troubleshooting.
* Additional support calls should problems arise post-install, including dispatches.
   * Multicast flooding problems wouldn’t occur until the TVs were in operation over time, so it could seem fine at install but then issues happen after the hotel opens.  
* ~$6K additional cost to the customer to enable a wireless solution per IPTV vendor, should all else fail.
* The opportunity is an estimated $55K total revenue with $232.50 in support MRC.
   * Customer is convinced this solution will work and will likely go with another vendor if we can’t comply.
 
Possible Alternative Solutions:

* We can (and should) charge additional labor for IPTV configuration due to the unique nature of it.
* We can build out statements in the SOW to direct any change orders should this solution fail to be at the customer’s expense, including any dispatches for IPTV once the hotel opens.
* If we are adamant this solution won’t work, we can propose a 1:2 Ratio to offset some of the additional cabling costs, although we may still lose the deal.
 
[@Prifti, Markos (CCI-Southwest)](mailto:Markos.Prifti@cox.com) As the Engineering SME, I would also ask for your recommendation and if you have any concerns about a setup like this.
[@Watts, Scott (CCI-Blueprint RF)](mailto:scott.watts@blueprintrf.com) The TDE will be at the frontline for this deployment so would ask your thoughts as well.
 
We can set up a call to discuss once all the stakeholders have had a chance to review and give their initial feedback.
 
Thanks,
 
Brian Napier
Senior Sales Engineer
Cell: 404-791-0011
 

 
[Leave Us a Google Review](https://www.google.com/search?q=blueprint+rf&rlz=1C5GCEA_enUS849US849&oq=blueprint+rf&aqs=chrome..69i57j46j69i61j69i60l2j69i65l3.1397j0j7&sourceid=chrome&ie=UTF-8)
 
[Follow Us on LinkedIn](https://www.linkedin.com/company/1253658/)  •  [Named #1 Marriott Provider](https://www.blueprintrf.com/blueprint-rf-awarded-first-place-overall-partner-performance-from-marriott-international/)

### CLAUDE (2026-04-27T15:44)
 Good draft start — you've got the right instinct to ask clarifying questions before taking a position. Let me tighten it up, sharpen the technical credibility, and make sure your TDE ops perspective comes through clearly since Brian specifically tagged you for that angle.

Here's a revised version:

A few notes on the changes made:

- **Topology question reframed** — your "homerun cable" question was right but needed to account for both possible interpretations of "jumper." The revised version asks both.
- **STB question expanded** — smart TV vs. STB is actually a meaningful technical distinction for multicast group management, so it's worth asking that way rather than just "are there STBs."
- **GRE question kept** — solid instinct on your part; if they're tunneling, the multicast behavior changes significantly.
- **Your technical paragraph tightened** — the "not full L3 routing" point is accurate but needed the downstream implication spelled out (wired port behavior, IGMP querier dependency) to sound credible to an engineering audience.
- **TDE ops angle added** — Brian asked for your perspective specifically in that capacity, so the reply leans into the post-install/support risk, which is your domain.
- **Tone** — collegial but not a pushover. You're not blocking the deal, you're putting conditions on it.
