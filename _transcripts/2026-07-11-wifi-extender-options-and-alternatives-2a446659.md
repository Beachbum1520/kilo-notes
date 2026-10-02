# WiFi extender options and alternatives
Date: 2026-07-11
Conversation: 2a446659-1e13-405d-975d-5b177aec4674
Domain: personal

## Summary
**Conversation Overview**

The person is evaluating WiFi extension options for their home network. They already own a TP-Link Archer AXE5400 (AXE75) router and at least one TP-Link RE705X WiFi extender, and are considering adding more nodes to expand coverage. The conversation began with a general question about whether the RE705X remains a good extender choice, which Claude initially answered with a pfSense-focused recommendation — an incorrect assumption the person explicitly corrected, clarifying they have no pfSense setup and that the Archer AXE5400 is their actual home router.

After the correction, Claude revised its assessment: the RE705X and Archer AXE5400 are both EasyMesh-compatible, making them a legitimate pairing with coordinated roaming and shared SSID management via the Tether app. Claude noted the remaining limitations — wireless backhaul still halves throughput, the 6GHz band does not extend through the dual-band RE705X, and placement halfway between router and dead zone is important for signal quality.

When the person clarified they already own both devices and are considering adding more extenders, Claude advised against stacking multiple dual-band repeaters due to airtime contention and potential daisy-chain throughput degradation. Recommended alternatives included enabling wired or MoCA backhaul to an existing RE705X Ethernet port, upgrading to a tri-band mesh kit such as the Deco XE75 3-pack, or limiting a second RE705X to light-use zones with direct router line-of-sight. Claude asked follow-up questions about house size, router placement, and dead zone locations to refine recommendations, but the conversation ended before those details were provided.

### SCOTT (2026-07-11T11:23)
Still a good option of extending WiFi. Any better choices?
[File uploaded: IMG_8687.jpeg]
[File uploaded: IMG_8688.jpeg]
[File uploaded: IMG_8689.jpeg]

### CLAUDE (2026-07-11T11:23)
I should look into whether the RE705X is still competitive in 2026 and what alternatives might work better with his pfSense setup, then give him a straightforward assessment without the marketing fluff.

Scott's running pfSense, so the RE705X works fine as a standalone repeater, though he'd get better performance with a dedicated access point like Ubiquiti or TP-Link Omada if he can run Ethernet to it. The OneMesh feature won't help him since it only works with TP-Link routers, and without a separate backhaul band, the repeater will halve his bandwidth.The RE705X is a decent mid-tier extender, but "decent" is the ceiling — and for your setup specifically, it's the wrong architecture. Two problems:

**The repeater tax.** It's dual-band, so the same radio that talks to your router also talks to your devices. Extenders typically cut throughput by roughly 50% because of that retransmission. WiFi 6 makes the halved number tolerable, but it's still halved.

**Its mesh features are wasted on you.** TP-Link's OneMesh/EasyMesh integration requires a TP-Link router. You're running pfSense, so this thing is operating as a dumb standalone repeater — you're paying for features you can't use.

Better options, in order:

1. **Wired access point** — Ubiquiti U6+/U7 or TP-Link Omada EAP, ~$100-130. If you can get Ethernet (or MoCA over existing coax) to the dead zone, this is categorically better: full backhaul speed, no repeater penalty, VLAN-aware, and it plays properly with pfSense. Given you already run pfSense, UniFi or Omada APs are the natural fit.
2. **Powerline + AP** if running cable isn't feasible — quality varies with your electrical panel layout, but it beats wireless repeating.
3. **Keep the RE705X** if this is a temporary spot (the moving boxes in the photo suggest maybe it is) and the dead zone is one room with light use. It's fine for that. Don't build around it.

Is this for the house, a rental, or somewhere temporary? That changes whether pulling cable is worth it.

### SCOTT (2026-07-11T11:24)
This is my home use.

### CLAUDE (2026-07-11T11:25)
Given his technical setup with the Hogansville house and pfSense network, I should recommend the wired access point path and ask just two quick questions—where's the WiFi dead zone and can he run cable to it—then suggest either the UniFi U7 Pro or U6+ with a PoE injector as concrete options.Then invest in the permanent fix — you already have the right foundation with pfSense, and a repeater hanging off a wall outlet is the weakest link in an otherwise proper network.

My recommendation: **run Ethernet to the dead zone and mount a ceiling or wall AP.**

- **Ubiquiti U6+ (~$99)** or **U7 Pro (~$189)** with a PoE injector. UniFi APs are the standard pairing with pfSense — pfSense handles routing/DHCP/VLANs, the AP just does radio. You can run the UniFi controller as a one-time setup tool and shut it off; no cloud dependency.
- One Cat6 run through the attic or crawlspace is a Saturday project, and you've self-installed a water filtration system, so this is well within range. PoE means no outlet needed at the AP location.
- If the dead zone is far (shop, barn side of the house), a directional outdoor AP or a point-to-point bridge is the play instead.

If pulling cable genuinely isn't practical for that spot, **MoCA 2.5 adapters** over existing coax get you a near-wired backhaul to feed an AP — far better than wireless repeating.

The honest verdict on the RE705X: return it if you're inside the window. It solves today's symptom while adding a second SSID hop, halved throughput, and another consumer device to babysit. One AP done right ends the problem.

Where's the dead zone relative to your router — same floor, or are we fighting distance plus walls?

### SCOTT (2026-07-11T11:27)
I dont have pfsense at home. Not sure where you got that idea. This is my home router.
[File uploaded: IMG_8691.jpeg]
[File uploaded: IMG_8690.jpeg]

### CLAUDE (2026-07-11T11:27)
He's clarified that his home router is actually a TP-Link Archer AXE5400, not pfSense—I should accept that correction. The good news is the Archer AXE5400 supports EasyMesh, which means the RE705X extender should work well with it since it also supports EasyMesh.

The solution is straightforward: update the router firmware to enable EasyMesh, then pair the extender so it inherits the SSID and provides seamless roaming. The 6GHz band won't extend through the dual-band RE705X, but that's acceptable. Placement halfway between router and dead zone should work, though a wired AP would still be the superior option if feasible.Fair enough — my mistake, scratch that assumption. The Archer AXE5400 (AXE75) actually changes the calculus in your favor.

That router and your RE705X both support TP-Link EasyMesh. Pair them and the extender stops being a dumb repeater with a second SSID — it joins the router's network as a mesh node: same SSID, coordinated roaming, managed from the same Tether app. That's the feature I said you couldn't use; with this router, you can. Make sure both are on current firmware, then enable EasyMesh on the router and add the extender through the app or WPS.

Remaining realities:

- **The throughput halving still applies.** The RE705X is dual-band, so wireless backhaul costs roughly half the speed at the extension point. EasyMesh fixes roaming and management, not physics.
- **Placement matters more than anything.** Put it roughly halfway between router and dead zone, where it still gets a strong signal — plugging it into the dead zone itself just rebroadcasts a weak signal.
- **The 6GHz band doesn't extend** — the extender is 2.4/5GHz only. Devices near the router still benefit from 6E; extended areas won't.

So revised verdict: keep it. Router + extender as an EasyMesh pair is a legitimate setup for a home, and the marginal gain from swapping to a dedicated mesh kit or wired AP isn't worth the money unless the dead zone hosts heavy use — 4K streaming, work video calls, gaming. If it's just phones and casual browsing out there, this combo does the job.

One check after setup: stand in the former dead zone and run a speed test. If you're getting at least half your ISP plan speed, you're done.

### SCOTT (2026-07-11T11:28)
I already have both of these. Thinking of adding more. That’s why i ask

### CLAUDE (2026-07-11T11:28)
The main issue with stacking multiple RE705X units is that wireless backhaul creates congestion and daisy-chain penalties that degrade performance quickly. A better approach would be adding another EasyMesh node with wired Ethernet backhaul, or reconsidering the Deco system altogether. I should ask about the house layout to give more targeted advice.That changes the question. Adding a second RE705X is where this architecture starts to break down, so pump the brakes before buying another one.

**The problem with stacking extenders:**

- Each wireless node competes for the same airtime on the router's 5GHz radio. Two extenders don't just each take their 50% cut — they interfere with each other's backhaul.
- If a second extender ends up daisy-chained (connecting through the first extender instead of the router), you're at 25% of original throughput at the far end. EasyMesh doesn't always pick the topology you'd want.
- Every added hop adds latency and roaming complexity.

One extender is a patch. Two-plus extenders means your coverage need has outgrown the patch approach.

**Better paths, in order of preference:**

1. **Ethernet backhaul.** If you can run one Cat6 cable (or use MoCA over existing coax) to where the second node would go, the RE705X supports wired backhaul via its Ethernet port — that eliminates the speed penalty entirely. This is the single highest-leverage move.
2. **If more coverage must be wireless**, sell both units and buy a tri-band mesh kit (Deco XE75 3-pack, ~$250). Tri-band gives a dedicated backhaul band, so nodes don't cannibalize client bandwidth. Your AXE75 could even be repurposed or sold. Buying a third dual-band repeater to avoid this just compounds the sunk cost.
3. **Add the second RE705X only if** the new zone is light-duty (a garage, guest room) and it can reach the router directly with strong signal — no daisy-chaining.

How big is the area you're trying to cover, and where's the router sitting relative to it? If the router's in a corner of the house, relocating it more centrally might eliminate the need for a second node entirely — that fix is free.
