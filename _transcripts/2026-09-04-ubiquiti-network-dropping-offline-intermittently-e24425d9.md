# Ubiquiti network dropping offline intermittently
Date: 2026-09-04
Conversation: e24425d9-c241-4aeb-88b3-58cb91f9b003
Domain: watts-way-farms

## Summary
**Conversation Overview**

The person operates a farm and sought help troubleshooting intermittent full network outages on their UniFi setup, which consists of a Ubiquiti UniFi Cloud Gateway, a USW Lite 8 Port PoE switch, and two U7 Outdoor access points. These connect to seven Eufy WiFi solar cameras and a Eufy Homebase. The symptom is the entire LAN going offline while Spectrum-provided internet remains up, with reboots resolving the issue temporarily before it recurs within days. The network had been stable for approximately one year before these failures began.

Claude initially outlined a broad set of troubleshooting paths including checking UniFi event logs, PoE budget on the switch, overheating, potential broadcast storms from the Eufy Homebase, power quality, and firmware issues. Through follow-up, the conversation narrowed toward heat as the leading suspect when the person confirmed the failures coincided with an unusually hot stretch of weather. The network gear is mounted in a sealed environmental enclosure on the interior wall of a barn, not in direct sunlight but in a space that can trap ambient heat combined with the devices' own waste heat. Claude walked through why a sealed enclosure is a heat trap even in shade, and outlined passive venting or small enclosure fans as the practical fix.

When the person asked where to find temperature data and logs in the UniFi app, Claude corrected an earlier implication that temperature readouts were readily available in the GUI — clarifying that most UniFi devices do not expose thermal data in the app, and that logs are found via the mobile app under the device's Insights/Details tab or in the web UI under Insights > All Activity or Settings > System Log. Claude recommended placing a Govee WiFi Thermo-Hygrometer sensor inside the enclosure as a practical workaround to log temperature remotely via the Govee Home app, noting the limitation that live alerts depend on the barn WiFi being up but that local logging would still capture a historical trace to correlate against UniFi event log timestamps after the network recovers.

### SCOTT (2026-09-04T15:43)
at my famr i have a ubiquiti unifi cloud gateway, an usw lite 8 port poe switch and 2 u7 outdoor ap's.  these connectr to my 7 eufy wifi solar cameras and eufy homebase.  twice now over the past few days,. the entire network goes offline.  but the spectrum privided internet is up.  reboot seems to reoslve for a little while.  how can i torubleshoot this

### CLAUDE (2026-09-04T15:43)
Since Spectrum stays up, this is isolating to something between your UniFi gear and your LAN — not the ISP handoff. A few likely culprits given your setup (gateway → switch → 2x U7 outdoor APs, plus a Eufy Homebase hanging off the LAN):
```
Troubleshooting steps for intermittent full LAN outages with ISP still up

```

Biggest suspects given your gear: PoE budget on the switch (two outdoor U7s can push close to the Lite 8 PoE's limit, especially on long cable runs) and overheating in whatever enclosure the gateway/switch sit in. Both produce exactly your symptom — dies, reboot fixes it temporarily, recurs in a few days.

One more thing worth doing right now: which Cloud Gateway model do you have (UCG-Ultra, UCG-Fiber, Cloud Gateway Max, etc.)? Some models have had specific firmware bugs tied to DHCP server crashes that match this pattern exactly, and knowing the model would let me point you at the right known-issue thread if the log check doesn't turn up an obvious cause.

### SCOTT (2026-09-04T15:45)
has been workign fine for about a year now.  but you think may be a heatr issue?  It has been stupid hot lately.

### CLAUDE (2026-09-04T15:45)
That timing lines up well — a year of stable operation then sudden failures during a stretch of extreme heat is the classic signature of a thermal problem, not a config or firmware issue. Heat-related failures often don't show up until ambient temps push a device that was already running warm over its threshold.

A few things to check/do:

- **Where are the gateway and switch physically mounted?** If they're in an enclosure, closet, cabinet, or anything without airflow, that box can run 15-20°F+ above ambient. In a heat wave, that's enough to push it over the edge.
- **Feel the units (once cooled down after a reboot) or check temps in the app** — Devices > [gateway] and [switch] > Overview, if your models report a temperature reading. Compare against the enclosure's typical daytime temp.
- **Any dust/debris on vents?** Farm environments accumulate dust fast, and that alone can be the difference between "handles heat fine" and "cooks itself."
- **Quick mitigation for now:** add airflow — crack the enclosure, add a small fan, or relocate the gear somewhere shadier/ventilated if that's feasible. Even a $15 USB fan blowing across the switch can be enough to get through a heat wave.
- **Longer term:** if it's boxed in, consider a vented enclosure or moving it to a spot with better passive airflow before next summer.

If outages stop once temps break, that basically confirms it. If they keep happening even after things cool off, then it's worth circling back to the PoE budget and firmware checks from before.

### SCOTT (2026-09-04T15:45)
they are in an environmental envluces on the wall of my barn.  not in any sort of environmental enclousre.

### CLAUDE (2026-09-04T15:46)
Good to know — that changes things a bit. Open wall-mount means no enclosure trapping heat, but a barn can still run brutally hot inside, especially if it's metal-roofed/metal-walled (barns act like ovens in direct sun) or if the units are mounted in a spot that gets direct sun through a window/door for part of the day.

Worth checking:

- **Is the mounting spot in direct sunlight at any point in the day?** Even a couple hours of direct sun hitting the gateway/switch casing can spike its internal temp well past what "ambient barn temp" would suggest.
- **How hot does the barn actually get inside** during the afternoon right now? If it's sitting at 100°F+ inside during a heat wave, that alone can be enough for gear rated for ~104-113°F ambient to start hitting its ceiling, since the internal components run hotter than the case.
- **Airflow around the units themselves** — even mounted in open air, if they're tucked against the wall with nothing behind/around them, or near other equipment generating heat, they can self-heat in still air.
- **Check the temp readouts in the UniFi app** (Devices > gateway/switch > Overview) next time it's hot, before it fails — that'll tell you directly if it's running hot rather than guessing from ambient.

Cheap fix if this is it: a small shade panel over the units if they get direct sun, or a $15-20 clip-on fan aimed at them during the worst part of the day. That's a lot easier than solving PoE budget or firmware theories if heat turns out to be the actual cause.

### SCOTT (2026-09-04T15:46)
sorry.  typ.  they absolutely are in a sealed environ,mental enclisre.  mounbted to the wall of my barn

### CLAUDE (2026-09-04T15:46)
Ah, that makes much more sense then — got it, sealed enclosure on the barn wall. That's a classic heat trap: a sealed box in direct sun or in a hot barn with no ventilation can easily run 20-40°F above ambient inside, and with the gear itself generating heat too, a sealed box in a heat wave is a very plausible failure mode.

A few things worth doing:

- **Check the temp readouts in the app** next hot afternoon (Devices > gateway/switch > Overview) before it fails again, to confirm you're actually hitting a thermal ceiling.
- **Ventilate the enclosure** — this is usually the real fix. Options, roughly in order of effort:
  - Add vents (with screened openings to keep bugs/dust out) if it doesn't already have them.
  - Add a small enclosure fan (12V computer-style fans wired to a wall wart, or PoE-powered fan kits made for network cabinets) to actively exhaust hot air.
  - If it's fully sealed with no vents at all, that's likely the core problem — even passive vents at top and bottom (chimney effect) can drop internal temp significantly.
- **Check enclosure placement** — is it in direct sun on the barn wall for part of the day? If so, even a simple shade panel or moving it to a north-facing wall could meaningfully help.
- **Short-term stopgap** during this heat stretch: crack the enclosure door/lid open if security/dust isn't a big concern, or point a small fan at it from outside.

If you confirm via the app that temps are spiking, that's your answer and ventilation is the fix. If temps look fine even during a failure, we're back to PoE budget or firmware as the more likely cause.

### SCOTT (2026-09-04T15:47)
its not in the sun at under  under the barn roof

### CLAUDE (2026-09-04T15:47)
That rules out solar loading, but it doesn't rule out heat as the cause — a sealed enclosure traps the heat the gear itself generates even with zero sun on it. Network gear in a fully sealed box is running in still, non-circulating air, so ambient barn temp plus the units' own waste heat builds up inside with nowhere to go. In a stretch of unusually hot weather, that's enough to push it past thermal limits even in shade, especially if the barn itself runs hot inside (metal roofing barns can trap heat even without direct sun hitting the box).

So the check is still the same:

- **Confirm via the app**: Devices > gateway and switch > Overview, check the temperature stat next time it's hot out, ideally right before or during a failure if you can catch it.
- **If it's sealed with no vents**: that's the most likely fix, regardless of sun exposure. Passive vents (screened, to keep dust/bugs out) at the bottom and top of the enclosure let hot air rise and escape while cooler air enters low — that alone often solves this without adding any powered fan.
- **If it does have vents already** but is just a tight fit with no airflow: a small fan inside the enclosure (12V fan on a wall wart, or a PoE-cabinet fan kit) pulling in from outside is a cheap fix.

If the app shows normal temps during a hot stretch, then it's not thermal and we should go back to the PoE budget/firmware angle instead. But given "worked fine for a year, then broke during unusually hot weather," heat trapped in a sealed box is still the leading suspect even without direct sun.

### SCOTT (2026-09-04T15:48)
where exaclty in the unifi app do i see temps or logs of

### CLAUDE (2026-09-04T15:48)
Let me check current documentation, since UniFi's app navigation has changed across versions.

Good thing I checked — this is less straightforward than I implied. Most UniFi gear does **not** show a temperature readout in the app GUI. A few community threads confirm people SSHing into devices to pull thermal sensor data manually rather than finding it in the UI, since the UniFi GUI doesn't expose it, though on some AP models you can SSH in and read the on-chip thermal sensor directly from the filesystem. Some newer Cloud Gateway models (UDM-SE and similar) have community requests asking for a temperature view, suggesting it's still not standard/reliable across the line even now.

So, practically:

**For logs (this part is solid):**
- **Mobile app**: open the site → tap the device (gateway or switch) → there's an "Insights" or "Details" tab showing recent events for that device. For the whole-network view: Site → hamburger menu / "..." → **Insights** → **All Activity**, which is a timestamped feed of connects/disconnects/reboots/adoptions.
- **Web UI**: left sidebar → **Insights** → **All Activity**, or under **Settings > System Log** for lower-level system events.

**For temperature**, don't count on finding it in the app for your Cloud Gateway or switch model — it may simply not be exposed. If you want to actually confirm a thermal issue, your realistic options are:
- Feel the enclosure/units by hand right when it fails (best real-world signal you have).
- Use a cheap wireless temp/humidity sensor (like a Govee or similar) placed inside the enclosure to log ambient temp over time and correlate against your outage timestamps — this sidesteps the UniFi app limitation entirely and is honestly the more reliable approach here.
- If you're comfortable with it, SSH into the gateway/switch and check `/sys/class/thermal/thermal_zone*/temp`, though exact paths vary by model.

Given the app can't reliably tell you this, I'd lean toward the cheap sensor-in-the-enclosure approach — it'll give you a clean before/during/after temperature trace next time it fails, without depending on UniFi exposing something it may not expose at all.

### SCOTT (2026-09-04T15:50)
give me a recomnedatrion of the temp sensor.  would be grwat if i could some hopw read it remotely

### CLAUDE (2026-09-04T15:51)

One catch worth flagging up front: the WiFi-connected version connects through your own WiFi to phone home, so during the exact moment your network goes down, it won't push a live alert to your phone — but it logs locally and syncs the graph once things reconnect, so you'll still get a clean historical trace of exactly what the temp did right before and during the outage.
```
Govee WiFi thermo-hygrometer recommendation for the network enclosure

```

Set an alert threshold around 110-120°F and just tape/velcro the sensor to the inside wall of the enclosure near the gateway. Next time it fails, pull up the graph in the app and check what the temp was doing right at that timestamp — cross-reference against the UniFi event log timestamps from earlier, and you'll have your answer.
