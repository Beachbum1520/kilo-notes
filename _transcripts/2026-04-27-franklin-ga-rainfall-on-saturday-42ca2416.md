# Franklin GA rainfall on Saturday
Date: 2026-04-27
Conversation: 42ca2416-16d3-4c07-99f8-e28d80e2eabb
Domain: watts-way-farms

## Summary
**Conversation Overview**

The person is a farm operator located in or near Franklin, Georgia (Heard County area) who asked about local rainfall data and then explored options for weather monitoring equipment. The conversation began with a question about Saturday's rainfall in Franklin, GA, which Claude researched and reported as approximately 0.18 inches on April 25th, with light activity in the early morning hours.

The discussion then shifted to selecting a rain gauge for the farm. Claude outlined three tiers of options — manual gauges (Stratus Precision), wireless consumer systems (Tempest Weather System, AcuRite Atlas), and telemetry-focused systems (Davis Vantage Vue, Ecowitt) — and recommended either the Tempest or a Stratus/Ecowitt combo given the farm context. The person then asked about pole sizing for both the Tempest and Starlink antenna, with Claude confirming both use 1.5"–2" OD pipe. This led to a practical question about whether an existing Starlink mast on top of the barn could be repurposed for the Tempest after the person switched from Starlink to Spectrum internet. Claude identified several concerns with that approach — roof access difficulty, rain splash affecting haptic sensor accuracy, wind turbulence from the barn structure, and lightning grounding considerations. The person quickly agreed it was a poor plan, and the conversation concluded with a recommendation to install a dedicated 10-foot galvanized pole sunk in concrete at an accessible, open location such as a pasture edge. The person has a pfSense-based network setup and an interest in self-hosted dashboards, noted as relevant context for equipment recommendations.

### SCOTT (2026-04-27T08:59)
How much rain did Franklin da get on Saturday

### CLAUDE (2026-04-27T09:00)
 

Let me check Weather Underground for actual rainfall totals at Franklin, GA for Saturday.

Franklin, GA picked up about 0.18 inches of rain on Saturday, April 25th — light rain shower activity, with most of it falling in the early morning (around 6–10 AM) and a small bit again late at night. Not enough to make a meaningful dent in the ongoing drought conditions.

### SCOTT (2026-04-27T09:00)
What’s the best rain gauge for my farm

### CLAUDE (2026-04-27T09:01)
 Depends on what you actually want from it. Three meaningful tiers:

**Manual (best accuracy, cheapest):** Stratus Precision Rain Gauge (~$40). 11" capacity, 0.01" resolution, NWS/CoCoRaHS standard. If you ever wanted to join CoCoRaHS as a citizen observer (Heard County is thinly covered), this is the required gauge. Downside: you walk to it and read it.

**Wireless to your phone (best for a working farm):** Either the Tempest Weather System (~$330) or AcuRite Atlas (~$200). Tempest uses a haptic rain sensor — no moving parts, no clogging from leaves or pollen, syncs to your phone, integrates with smart home stuff. Atlas is tipping-bucket (more traditional, generally accurate but needs occasional cleaning). For a pasture operation where you're already running between the house, the field, and the processor, having rainfall on your phone alongside temp/wind/lightning is genuinely useful.

**Pure tipping-bucket telemetry (if you want to feed a system):** Davis Vantage Vue (~$400) or Ecowitt GW1100 + WH40 (~$80–120). Ecowitt is the budget play and surprisingly capable — it'll push to Weather Underground, Ambient Weather, MQTT, etc. Given your pfSense/proactive monitoring leaning, Ecowitt is the one that actually plays nice with self-hosted dashboards.

My take for Watts Way: **Tempest** if you want one device that just works and gives you useful farm data (lightning alerts matter when you've got cattle and people working outside), or **Stratus + Ecowitt WH40 combo** (~$120 total) if you want ground truth plus telemetry and don't mind two devices.

Counterpoint to consider: if rainfall is the *only* thing you care about, a $40 Stratus mounted on a fence post will outlast and out-accurate everything else on this list. The wireless gauges are really paying for the ecosystem, not the rain measurement.

### SCOTT (2026-04-27T09:06)
How big of a pole for the tempest?

### CLAUDE (2026-04-27T09:06)
 Tempest needs a **1.5" to 2" outer diameter pole** for the included mounting bracket — standard chain-link fence top rail (1-3/8" or 1-5/8" OD) works, as does 1.5" or 2" Schedule 40 PVC or galvanized pipe.

Height-wise, WeatherFlow recommends mounting it **at least 5 feet above any nearby surface** (roof, ground, deck) and ideally **6 feet above ground** for the rain haptic sensor to work accurately — splashing from grass or hard surfaces will inflate readings. For wind accuracy, higher and more exposed is better (10+ feet clear of obstructions if you can swing it), but that trades off against rain accuracy if the pole sways.

Practical setup for a pasture: 10-foot section of 1.5" galvanized pipe, sunk 2-3 feet in concrete, gives you ~7 feet of exposed sensor height. Stable, won't sway, and clears most ground splash. If you go taller for wind, add a guy-wire kit — a swaying pole will throw off the haptic rain readings.

### SCOTT (2026-04-27T09:07)
What size pole does a Starlink antenna moount to?

### CLAUDE (2026-04-27T09:07)
 Starlink's official pole mounts (Pipe Adapter and Long Wall Mount) accept **1.5" to 2" outer diameter pipe** — same range as the Tempest, conveniently. Standard 1.5" Schedule 40 pipe (1.9" OD) is the sweet spot.

A few notes specific to Starlink:

The **Pipe Adapter** (~$45 from Starlink) is the cheapest option and clamps onto an existing pole. The **Long Wall Mount** comes with its own pole. Third-party options on Amazon are plentiful and usually cheaper.

For the Gen 3 (Standard) dish, the antenna is heavier and has more wind load than older versions, so a flimsy pole will sway and cause obstruction issues — Starlink is sensitive to even small movements. Same advice as the Tempest: **galvanized or steel, sunk in concrete**, not just driven into the ground.

If you're thinking about co-locating Starlink and the Tempest on one pole — doable, but keep about 3 feet of vertical separation and put the Tempest **above** the dish if possible. The dish will throw a shadow/obstruction in the Tempest's wind reading otherwise, and you don't want the dish blocking sky for the haptic sensor either.

One more thing worth flagging given your pfSense setup: if this Starlink is for the farm, the Gen 3 router has limited bypass options compared to Gen 2. Bypass mode works but you lose Wi-Fi entirely on the Starlink side — fine if pfSense is handling everything downstream, just plan for it.

### SCOTT (2026-04-27T09:08)
I already have a Starlink antenna on top of my barn. I have switched to spectrum. So could take the Starlink down and put the tempest on it?

### CLAUDE (2026-04-27T09:08)
 Yes, that works well — and it's a smart reuse. The Starlink mast is already sized in the 1.5"–2" OD range that the Tempest bracket fits, already anchored to handle wind load, and already sited high on the barn with sky exposure. That's most of the install work done.

A few things to check before you swap:

**Height above the roof** — Tempest wants the haptic rain sensor at least 5 feet above any nearby surface. If your Starlink mast is short and the dish was sitting close to the roof, you may need a taller pole or extension. Roof splash will inflate rain readings.

**Wind exposure vs. roof turbulence** — barns create wind eddies. If the mast is on the ridge or peak, you're fine. If it's on a side wall or low slope, wind readings will be skewed. Not a dealbreaker, just know your wind data will be directionally off.

**Lightning consideration** — a barn-mounted metal pole with electronics on it is a lightning target. Starlink had its own grounding path through the cable; the Tempest is wireless and battery-free (solar), so no cable to ground. If your area gets active storms, consider a separate ground wire from the pole to a grounding rod. Cheap insurance for a $330 device.

**Bracket compatibility** — Starlink's pipe adapter clamps differently than the Tempest bracket. You'll likely remove the Starlink hardware entirely and mount the Tempest's included bracket directly to the existing pipe. Confirm the pipe OD with calipers or a tape measure before you order/unbox.

One thing to think about: a barn rooftop is a pain to service. Tempest batteries are solar-charged and the unit is sealed, so maintenance is essentially zero — but if it ever fails or needs the firmware reset trick, you're going up there. Worth it for the install convenience now.

### SCOTT (2026-04-27T09:08)
Ya. All of those reasons mean not a good plan.

### CLAUDE (2026-04-27T09:09)
 Fair call. Roof access alone is enough to kill it — a "free" mount that requires a ladder every time something acts up isn't free.

Better plan: dedicated 10-foot pole sunk in concrete somewhere accessible, away from the barn turbulence. Pasture edge, garden corner, somewhere you walk past anyway. You'll get cleaner wind data, easier service, and you can co-locate a manual Stratus gauge at the same spot for ground truth on the rain readings.
