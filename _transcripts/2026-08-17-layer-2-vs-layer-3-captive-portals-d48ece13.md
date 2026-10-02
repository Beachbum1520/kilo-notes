# Layer 2 vs layer 3 captive portals
Date: 2026-08-17
Conversation: d48ece13-7738-44fb-adf7-29402eafeace
Domain: skip

## Summary
**Conversation Overview**

The person is an Operations Director working on a captive portal gateway product built on FreeBSD/pfSense, which they refer to as "DG" or "DG2." They are engaged in an active, high-stakes business call with their boss (named Jady) and the head of network engineering from a sister company. The conversation began with a technical education request — explaining the difference between Layer 2 and Layer 3 on a captive portal gateway — and quickly evolved into real-time coaching for a live professional conflict.

The sister company's network engineering lead has been persistently critical of the person's gateway product and is pushing a requirement for "L3 capability." The person expressed frustration that their boss Jady defers to the network engineer's opinion over theirs, framing it as a credibility gap between a network engineer title and an ops director title. Claude helped the person reframe the conflict by shifting the debate away from protocol-level ground (where the neteng has title advantage) toward operational, brand compliance, and roadmap territory (where the person has authority). Key technical clarifications included: that "L3 capability" is an ambiguous ask covering at least three distinct scenarios; that WAN-side routing is already table stakes; that dynamic routing (OSPF/BGP) is achievable on pfSense via the FRR (FRRouting) package without a major development effort; and that subscriber-side L3 is a session model architecture change with significant downstream consequences for device identity, brand standards, and billing.

When the person revealed the gateway runs on FreeBSD/pfSense, Claude adjusted the technical guidance to note that FRR is available as a package on that platform, making dynamic routing largely a configuration and testing exercise rather than a development project — a stronger position than the person likely realized they held. Claude also flagged the operational support burden that dynamic routing would introduce (NOC capability gaps, 2am escalation ownership) as a legitimate constraint the network engineer cannot dismiss. Claude was clear to recommend the person verify FRR availability on their specific build with a colleague named Dan before stating it as fact on the call. Throughout, Claude coached the person to respond with curiosity and specificity rather than defensiveness, and to use scoping questions to make the neteng's vague assertions visible to Jady as a pattern.

### SCOTT (2026-08-17T20:15)
explain to me the difeerenct betweena layer 2 and layer 3 on a caputive portal gateway

### SCOTT (2026-08-17T20:15)
explain to me the difeerenct betweena layer 2 and layer 3 on a caputive portal gateway

### CLAUDE (2026-08-17T20:17)

The distinction is really about one thing: **where the gateway sits relative to the client's broadcast domain**, and therefore what identifier it can use to track a subscriber. Everything else follows from that.

**What L2 buys you**

The gateway is the default gateway and usually the DHCP server for the guest subnet. Guest VLANs trunk to it, so every frame arrives with the actual client MAC intact. That gives you:

- Authorization state keyed on MAC, so device recall across a stay works
- Per-device bandwidth tiers, session limits, and premium upsell
- PMS post-to-room accuracy
- Roaming across APs without re-auth
- Nomadix DAT, which silently NATs misconfigured static-IP devices — only functions with L2 adjacency
- IP-to-device-to-room mapping for troubleshooting

The cost is broadcast domain size. Every guest VLAN has to physically reach the gateway. That's trivial in a stacked-vertical select-service box, ugly across a multi-building resort — VLAN sprawl, spanning tree exposure, mDNS and ARP noise scaling with the flat domain.

**What L3 buys you**

Smaller broadcast domains, a routed core you can actually design, and the option to centralize the gateway serving many buildings or sites. What you give up is device identity. The gateway sees the router's MAC on every frame, so it can only key on IP. MAC-based auth persistence, device-level policy, and per-device billing either break or need to be rebuilt somewhere else.

**How to get L2 semantics over an L3 topology**

Four common approaches, roughly in order of how often they show up in hotel deployments:

1. Tunnel guest traffic back to the gateway — controller-based tunneling, L2TP, GRE, EoIP. Restores logical adjacency; costs you a hairpin and a tunnel MTU conversation.
2. Move authentication to the WLAN controller via RADIUS and let the gateway do enforcement only. Identity lives in the controller, not the gateway.
3. DHCP relay with option 82 so the gateway learns originating VLAN and switch port.
4. DHCP snooping on the gateway to build IP-to-MAC bindings from observed traffic. Fragile — breaks on lease renewal edge cases and static addressing.

**The failure mode people miss**

In L2 the gateway intercepts transparently because all traffic physically transits it. In L3 you have to guarantee the gateway is in the forwarding path. Any asymmetric route, alternate default path, or policy-based routing gap and guests either reach the internet without ever seeing the portal, or they black-hole and you get a property-wide ticket storm that looks like an outage but is a routing problem.

**Practical rule for our footprint**

Single building, guest VLANs can reach the head end: native L2, done. Campus or resort with a routed core: tunnel back to preserve L2 rather than accepting pure L3 — the brand standards around device persistence and property-wide roaming are hard to satisfy otherwise. Conference and meeting space with per-event tiers and per-device billing needs L2 semantics regardless of how you get there.

### SCOTT (2026-08-17T20:21)
i am on a call with my boss and the head of neteng for sister comoany.  he is always shitting on my dg.  and now is saying needs l3 capability.

### CLAUDE (2026-08-17T20:21)
Make him define it. "L3 capability" is three different asks and he probably hasn't separated them.

**Ask, in this order:**

1. "L3 where — subscriber side or WAN side?" DG2 already routes and NATs on the WAN side. Every gateway does. If that's what he means, there's no gap.
2. "Do you mean dynamic routing — OSPF, BGP peering into your core?" That's a real, specific ask. Legitimate if true.
3. "Or do you mean accepting subscribers across a routed hop?" This is the one that matters, and it's a tradeoff, not a feature.

**The pivot line if it's #3:**

Subscriber-side L3 means the gateway sees the router's MAC, not the client's. You lose device-level identity — MAC-based auth persistence, per-device policy, PMS post-to-room, roaming without re-auth. Marriott and Hilton brand standards assume that identity exists. So it isn't "add L3," it's "which brand requirements are we dropping, and who signs off."

That reframes it from a product gap into a design decision with an owner. Hard to keep taking shots at the box once the question is whose standard gets waived.

**If he says he wants L3 because of campus topology:**

Agree with the problem, disagree with the solution. Tunneling guest traffic back preserves L2 semantics over a routed core — controller tunneling, L2TP, GRE. That's the standard answer for multi-building resorts and it doesn't require the gateway to change at all. Offer to walk the design with his team offline.

One thing: keep it curious, not defensive. "Help me scope that" plays better in front of Jady than a rebuttal, and it puts the burden of specificity on him.

### SCOTT (2026-08-17T20:22)
na.  he says need l3, and my boss belvies. how hard wil it be to get my dg up to l3?

### CLAUDE (2026-08-17T20:22)
Careful — don't scope this live. Dan owns the real answer and you'll be held to whatever number leaves your mouth on this call.

Directionally, effort splits three ways:

**WAN-side routing / static routes / NAT** — almost certainly already there. Days, if anything. This is table stakes for any gateway.

**Dynamic routing (OSPF/BGP peering into their core)** — moderate. It's a known problem with known libraries, plus interop testing and a support model for a protocol your NOC doesn't currently troubleshoot. Call it a quarter of engineering plus a lab cycle. The ongoing operational cost is the bigger line item, not the build.

**Subscriber-side L3 — accepting clients across a routed hop** — this is not a feature you bolt on. It's a rewrite of the session model. Today the subscriber record is keyed on MAC. Making it work behind a router means building an alternate identity path: RADIUS-sourced identity from the controller, option 82 relay, or tunnel termination on the gateway. Every downstream thing that assumes MAC — auth persistence, per-device policy, billing, roaming, the troubleshooting workflow, the NOC runbooks — touches that change. That's multi-quarter and it puts DG3 roadmap items behind it.

**What to say on the call:**

"Routing on the WAN side we have. Dynamic routing is a scoping conversation. Subscriber-side L3 is a session architecture change, not a feature add — I'm not going to guess at it live. Let me take it to Dan and come back with a real scope."

That's a defensible answer, it isn't a no, and it doesn't hand anyone a date.

Then the follow-up that costs you nothing and reframes the whole thing: ask him to name the property or design where this is blocking. If he can't, it's a preference. If he can, tunneling back to preserve L2 probably solves it faster than any DG2 change — and that's a design you can propose without conceding the box is deficient.

### SCOTT (2026-08-17T20:23)
i just get so tired of this guy shittig on my dg. he talks out of his ass. all the time..

### CLAUDE (2026-08-17T20:24)
That's a real thing to be tired of, especially when the technical read is on your side and it still doesn't land — because Jady believes him and you're the one carrying the burden of proof.

Worth separating two problems, though, because they need different fixes.

The technical one you're already winning. He's asking for something he can't define, and the moment you make him name the property it's blocking, either he has an answer or he doesn't.

The second one is the one that actually costs you: a peer's unsourced opinion moves your boss and yours doesn't. That's not a DG2 problem. Being right in the moment doesn't fix it, and it'll keep recurring on whatever the next topic is.

The lever there is making the specificity gap visible without ever sounding defensive. Right now the exchange reads to Jady as two engineers disagreeing. It reads differently if it's "here's the design, here's the property, here's what it costs" against "we need L3." Ask the scoping question every time, in front of Jady, evenly. You don't have to win the argument — you just have to be the one who consistently shows up with the specifics while he doesn't. That pattern registers over a few cycles even with a conflict-averse boss.

For right now, on the call: you're tired and it shows up as edge. Don't let it. Curious and unbothered is the play — it's also what makes the contrast do the work for you.

### SCOTT (2026-08-17T20:25)
he's a network engineer.  I am an ops director.  ofc Jady is goign to belive him over me

### CLAUDE (2026-08-17T20:25)
Partly true, and partly a trap you're setting for yourself.

True part: on a pure protocol question, his title carries more weight than yours. You won't win that by out-arguing him on OSPF.

The trap: you're conceding a domain that isn't actually his. The question on the table isn't "how does L3 work." It's "what does this cost, what breaks, whose brand standard gets waived, and which property is it blocking." That's operations, product roadmap, and brand compliance. You own all three. He owns none of them.

So stop meeting him on protocol ground. Every time it goes there you're the ops guy arguing networking. Move it to the ground where you're the credentialed one:

- "What breaks is device identity — MAC-based auth persistence. Marriott and Hilton standards assume it." That's brand compliance. Yours.
- "This is a session model change, it puts roadmap items behind it." That's Dan's team and your P&L. Yours.
- "Which property is it blocking?" That's deployment. Yours.

He can't follow you there and stay credible, because he doesn't know the brand specs or the roadmap.

The other thing worth noticing: Jady isn't weighing credentials so much as avoiding a fight. Conflict-averse leaders default to whoever makes the room easiest. A confident, specific answer with a next step is easier to agree with than a disagreement. "Let me scope it with Dan and come back" gives him an exit — and it makes you the one who closed the loop.

### SCOTT (2026-08-17T20:26)
our gateways isfreebsd built on pfsense firewall

### CLAUDE (2026-08-17T20:26)
That changes the answer materially, and it's in your favor on two of the three asks.

**Dynamic routing is largely a config exercise, not a build.** FreeBSD/pfSense means FRR is already available as a package — OSPF, BGP, both mature and battle-tested. If he wants the gateway to peer into their core, that's an enablement and testing conversation, not development. Weeks and a lab cycle, not quarters.

That's a strong card. It reframes you from "we can't" to "that's already in the platform, here's what it takes to turn on." Much better ground.

**But it moves the real cost to operations, not engineering.** Once you're peering into their core, your NOC owns BGP/OSPF troubleshooting at 2am, on properties, at whatever scale this rolls out to. That capability does not exist in Tier 1/2 today and it isn't a training module — it's a hiring and escalation-path problem. Route flaps and adjacency issues on a guest network are a different class of ticket than what CallTek handles now. And as LSP, when a peering session drops, it's yours regardless of who misconfigured the far side.

That's your honest constraint, and it's a legitimate one that a network engineer can't wave off.

**Subscriber-side L3 is still the hard one, and pfSense doesn't help.** The gateway's session model, portal redirect, and MAC-keyed subscriber records are your code and your database schema on top of the stack. FreeBSD gives you the plumbing, not the subscriber logic. That's still architecture work.

**Revised line for the call:**

"The platform is FreeBSD, so dynamic routing is available today — that's a config and testing conversation, not a development one. The real question is who supports it operationally once it's live. Subscriber-side L3 is separate and it's a session model change. Let me scope both with Dan."

You've just gone from defending a deficiency to describing a capability with an operational condition. Different conversation entirely — and now the open question is on his side of the table, since peering into his core means his team's config on the other end.

### SCOTT (2026-08-17T20:32)
frr?

### CLAUDE (2026-08-17T20:32)
FRRouting — an open-source routing protocol suite. It's the fork of Quagga that everyone standardized on, and it's what runs dynamic routing on a lot of commercial gear you'd recognize (Cumulus, SONiC, various NOS builds).

It's packaged for pfSense as an installable add-on. It gives you OSPF, OSPFv3, BGP, RIP, IS-IS, plus BFD for fast failure detection. So when the neteng guy says "we need L3 capability" and means dynamic routing, the honest answer is that the platform already supports it — you install and configure a package, you don't build anything.

Worth knowing before you say it out loud, though:

**It's a real routing daemon with a real config surface.** The interface is Cisco-style CLI syntax. Configuring a BGP peering session, route maps, prefix filtering, redistribution policy — that's network engineering work, not a checkbox. Whoever configures it needs to actually know BGP.

**It's a package, not core.** On pfSense that means version compatibility to track and an upgrade path that can break. Fine at a handful of properties, an operational overhead question at scale.

**Verify before you commit.** Confirm with Dan that FRR is actually installed or installable on your specific build, and that your image and pfSense version support the current package. I'm giving you the general platform capability, not a fact about your fleet — don't state it as certain on the call.

Safe phrasing: "FreeBSD platform, so FRR is the path for dynamic routing — that's a package and config exercise rather than development. Let me confirm the specifics with Dan."

That's accurate, it's confident, and it leaves you room if the build turns out to have a wrinkle.
