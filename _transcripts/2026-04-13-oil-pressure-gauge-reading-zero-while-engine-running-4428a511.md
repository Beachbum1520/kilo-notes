# Oil pressure gauge reading zero while engine running
Date: 2026-04-13
Conversation: 4428a511-ecb9-4a36-947c-b6b0bb99b7f5
Domain: personal

## Summary
**Conversation Overview**

The person is a hands-on vehicle owner and farmer based in the Franklin, GA area (Heard County) who owns two vehicles currently experiencing issues: a 2011 Chevy Yukon Denali (purchased new, now over 220,000 miles) and a 2018 Chevy 2500HD diesel truck (180,000 miles). The conversation focused on diagnosing warning lights and gauge issues on both vehicles using an OBD2 scanner the person purchased during the conversation.

For the Yukon, the oil pressure gauge was reading zero with the engine running. Claude walked through the diagnostic logic, confirmed oil level was fine and no unusual noises were present, then recommended pulling codes. The person purchased an Autel MaxiLink ML629 (2026 model, ~$114 on Amazon) based on Claude's recommendation. Codes pulled from the Yukon were P0521 and P0523 (oil pressure sensor performance and high voltage circuit codes), confirming a failed oil pressure sending unit rather than actual oil pressure loss. The recommended fix is ACDelco part number 12616646 (also sold as ACDelco Professional D1846A), a $15–35 part and approximately 15-minute DIY job. A third code, P162B, was identified as unrelated and low priority. The Yukon repair has not yet been completed but the person intends to do it.

For the 2500HD Duramax diesel, multiple glow plug codes were present (P0672, P0673, P0675, P06C6, P06C7, P06C9, P1339, P133A) across cylinders 2, 3, and 5. However, the person noted glow plugs were replaced by the dealership roughly one to two years ago and the truck starts and runs perfectly. Claude assessed the most likely culprits as a failing Glow Plug Control Module (GPCM) or improperly reseated connectors from the dealership service, rather than failed plugs again. The person cleared all codes to monitor how quickly and under what conditions they return, which will help narrow the diagnosis. Claude also recommended coolant flush and transmission fluid service at this mileage given the Allison transmission. The person plans to ask around locally for a trusted independent diesel mechanic through their farming network rather than returning to the dealership, which they distrust. The person maintains both vehicles conscientiously, with religious oil changes and proactive repairs including injector replacement already completed on the 2500HD.

One notable correction: Claude incorrectly referenced the Atlanta area when suggesting where to find a mechanic. The person firmly corrected this, clarifying they are in the Franklin, GA area and have no connection to Atlanta.

### SCOTT (2026-04-13T17:46)
The car is running and driving and this gauge is on zero. Is that normal?
[File uploaded: IMG_6122.jpeg]

### CLAUDE (2026-04-13T17:46)
 **No, that's not normal — and it's serious.**

That's your **oil pressure gauge**, and it's reading **zero** with the engine running. That's a red flag.

**What it means:**
- Either you have **genuinely zero oil pressure** (catastrophic — engine damage is occurring right now)
- Or the **oil pressure sensor/sending unit has failed** and is giving a false reading

**What to do immediately:**
1. **Pull over and shut the engine off** if you haven't already. Running an engine with no oil pressure can destroy it in minutes.
2. Check the **oil level** on the dipstick — if it's low or empty, that's your answer.
3. Look for an **oil pressure warning light** on the dash (it may not have triggered separately).

**The sensor failure scenario** is the more hopeful possibility — these do fail and read zero falsely. But you cannot assume that without confirming oil level and pressure.

**Bottom line:** Don't drive it until this is diagnosed. If oil level is fine and the gauge is the only symptom, a mechanic can test actual pressure with a manual gauge. If oil level is low, you may already have engine damage depending on how long it's been running.

What vehicle is this, and did you notice any warning lights or unusual sounds?

### SCOTT (2026-04-13T17:48)
A 2011 Yukon Denali that we bought new back in 2011. It has over 220,000 miles on it.

### CLAUDE (2026-04-13T17:48)
 That context actually matters a lot here.

**The good news:** The oil pressure sending unit on these GMT900-platform trucks (Tahoe, Yukon, Silverado, Sierra) is a **extremely common failure point** — it's almost a scheduled maintenance item by high mileage. At 220k, a failed sender is far more likely than catastrophic oil loss.

**The bad news:** At 220k miles, you also have to take zero oil pressure seriously on face value until proven otherwise.

**Immediate checklist:**
1. **Engine off** — check the dipstick. Is oil level normal?
2. Any **lifter tick, knocking, or unusual engine noise** when running?
3. Did the **oil pressure warning light** illuminate, or just the gauge drop?

**If oil level is full and engine sounds normal**, the sending unit is the overwhelming favorite. It's a cheap fix — the sensor is ~$20-30 and sits right on the engine block, usually a 10-minute job.

**The risk calculus at 220k:** Even if it's just the sensor, these LS-based engines (5.3 or 6.2?) are also known for **AFM/DOD lifter failures** at high mileage, which can cause real oil pressure drops. Worth knowing your maintenance history on oil changes.

**Don't drive it** until you've confirmed oil level at minimum. What does the dipstick show?

### SCOTT (2026-04-13T18:00)
No unusual noises. Engine oil level is fine.

### CLAUDE (2026-04-13T18:00)
 Good news — that points strongly toward a **failed oil pressure sending unit**. That's the most likely culprit given:

- No knocking or lifter noise
- Oil level is full
- 220k miles on a platform known for sender failures

**The fix:**
The sending unit is located on the **driver's side of the engine block**, near the oil filter. On the 6.0L Yukon Denali it's straightforward to access. Parts run $15–40 depending on brand (ACDelco is the OEM choice — worth the few extra dollars over a generic on a pressure sensor).

**One additional thing to check:** These trucks also have a **known issue with the oil pressure sensor circuit** in the gauge cluster itself, but the sender is almost always the culprit first.

**What I'd do:**
1. Drive it minimally and carefully to a shop or parts store for diagnosis — or have someone come to you
2. Ask them to test **actual oil pressure with a mechanical gauge** before just swapping the sender — takes 10 minutes and rules out any real pressure issue definitively
3. If mechanical pressure is confirmed normal, swap the sender

Given the truck has 220k and has been reliable since new, this is almost certainly a cheap fix. These LS engines are legendarily durable — plenty of them run to 300k+ with basic maintenance. You're probably fine, but confirm it before logging more miles.

### SCOTT (2026-04-13T18:01)
Since part is so cheap and fix is so easy, why not start there. Oh. And the check engine light is on. But other than that, all seems normal.

### CLAUDE (2026-04-13T18:01)
 Totally reasonable call — swap the sender first, it's a $20 bet on the most likely answer.

**The check engine light changes things slightly though.** Before you swap the sender, it's worth pulling the codes — could be completely unrelated (O2 sensor, EVAP, etc.) or it could be **P0520/P0521/P0522**, which are oil pressure sensor circuit codes. That would essentially confirm the sender is the problem.

**Free options to pull codes:**
- Any AutoZone, O'Reilly, or Advance Auto will read them for free
- If you have a Bluetooth OBD2 dongle and your phone, takes 2 minutes

**If the code is P052X series** — you have your answer, swap the sender with confidence.

**If the code is something unrelated** — still swap the sender given the gauge reading, but know you have a second issue to address separately.

Given you're in the Atlanta/Franklin area, there's an AutoZone or O'Reilly within easy reach. Pull the codes first, then grab the ACDelco sender while you're there. Thirty minutes total, probably a $25 fix.

What's your mechanical comfort level — are you doing this yourself or handing it off?

### SCOTT (2026-04-13T18:05)
Recommend a good OBD2 scanner from Amazon.

### CLAUDE (2026-04-13T18:05)
 For your use case — a working farm, a high-mileage daily driver, and someone who's clearly hands-on — I'd skip the cheap Bluetooth dongles and get something with a real screen and bidirectional capability.

**Best value for your situation:**

**Autel MaxiLink ML629** (~$65–80)
- Reads and clears codes
- Shows live data including **real-time oil pressure sensor voltage** — relevant right now
- Covers all systems (not just engine)
- Standalone — no phone required

**Step up if you want more:**

**Autel AutoLink AL619** or **Autel ML919** (~$100–130)
- Adds ABS and SRS (airbag) system scanning
- Worth it on a vehicle this age

**What I'd avoid:**
- Generic Bluetooth ELM327 dongles — unreliable on GM vehicles specifically, inconsistent app support
- Cheap no-name handheld units under $30 — miss GM-specific codes regularly

**My actual recommendation for you:** The **Autel MaxiLink ML629**. It'll serve the Yukon, any farm equipment with OBD2, and anything else you buy going forward. Pays for itself the first time you avoid a diagnostic fee at a shop.

Search "Autel ML629" on Amazon — usually Prime eligible. Want me to look up current pricing and reviews?

### SCOTT (2026-04-13T18:07)
This?
[File uploaded: 947ab01ff35712739398ecd600716627874a54e8.png]

### CLAUDE (2026-04-13T18:07)
 Yes, that's the one — and it's actually the **2026 upgraded model** which is better than what I originally referenced. It now includes:

- ABS, SRS, and **Transmission** diagnostics (that's the upgrade over the older ML619)
- Live data in text and graph
- Auto VIN — just plug in and it reads the vehicle automatically
- DTC lookup built in

**$114 is a fair price** for what you're getting. This covers every system you'd care about on the Yukon.

**Buy it.** It'll pay for itself today on the Yukon diagnosis alone, and you'll use it on the farm trucks for years.

### SCOTT (2026-04-13T18:08)
What’s the part number for my $20 gamble?

### CLAUDE (2026-04-13T18:08)
 For a 2011 Yukon Denali, the oil pressure sending unit part number is:

**ACDelco 12616646** (OEM spec)

Also sold as **ACDelco Professional D1846A** — same sensor, just the aftermarket line.

Search either number on Amazon or just walk into AutoZone/O'Reilly and give them the year/make/model. Should be $15–35 depending on source.

**Pro tip:** Grab it at a parts store rather than waiting on Amazon shipping — you want to get this resolved today rather than waiting 2 days.

### SCOTT (2026-04-17T21:38)
From my yukon
[File uploaded: IMG_6168.jpeg]
[File uploaded: IMG_6169.jpeg]
[File uploaded: IMG_6170.jpeg]
[File uploaded: IMG_6171.jpeg]

### CLAUDE (2026-04-17T21:38)
 **Case closed. Swap that sender.**

Here's what your codes show:

**P0521** — Oil pressure sensor performance (sensor reading out of range)
**P0523** — Oil pressure sensor circuit **high voltage** (current, active, failing right now)
**P162B** — Remote vehicle speed limiting signal (unrelated, ignore for now)

**What this tells you:**
- P0521 and P0523 together are a **textbook failed oil pressure sending unit** — the sensor is sending a bad/high voltage signal to the ECM, which is why the gauge reads zero
- Both are **current active codes**, meaning it's failing every ignition cycle
- **Zero engine damage concern** — this is 100% a sensor/circuit issue, not actual oil pressure loss

**P162B** is likely a ghost code related to OnStar or a speed limiter module — common on these trucks, low priority, clear it after you fix the sender and see if it comes back.

**Your action items:**
1. Grab ACDelco 12616646 at the parts store today
2. Swap the sender (15 minutes)
3. Clear all codes with the MaxiLink
4. Confirm gauges read normal and no codes return

Your $20 gamble just got confirmed. The MaxiLink already paid for itself.

### SCOTT (2026-04-17T21:40)
From my truck. A 2018 Chevy 2500HD diesel. May be a few dups here.
[File uploaded: IMG_6172.jpeg]
[File uploaded: IMG_6173.jpeg]
[File uploaded: IMG_6174.jpeg]
[File uploaded: IMG_6175.jpeg]
[File uploaded: IMG_6176.jpeg]
[File uploaded: IMG_6177.jpeg]
[File uploaded: IMG_6178.jpeg]
[File uploaded: IMG_6179.jpeg]
[File uploaded: IMG_6180.jpeg]
[File uploaded: IMG_6181.jpeg]

### CLAUDE (2026-04-17T21:40)
 Ah — different vehicle entirely. That's your **Duramax diesel**, which changes everything. Here's the full breakdown:

**The glow plug codes — this is the main story:**
- **P0672** — Cylinder 2 glow plug circuit (history, currently passing)
- **P0673** — Cylinder 3 glow plug circuit (history, currently passing)
- **P0675** — Cylinder 5 glow plug circuit (history, passing)
- **P06C6** — Cylinder 2 glow plug incorrect (active, current, MIL on)
- **P06C7** — Cylinder 3 glow plug incorrect (active, current, MIL on)
- **P06C9** — Cylinder 5 glow plug incorrect (history, passing)
- **P1339** — Cylinder 2 glow plug offset exceeded (active, current)
- **P133A** — Cylinder 3 glow plug learning limit (active, current)

**Bottom line:** You have **multiple failing glow plugs** — at minimum cylinders 2 and 3 are actively failing right now. Cylinder 5 has a history but is currently passing.

**What this means practically:**
- Hard cold starts, especially below 40°F
- Rough idle until engine warms up
- That check engine light is earned

**The fix:** Glow plugs on an LML/L5P Duramax are a **shop job** — they're recessed deep, require proper torque, and broken plugs in the head are a nightmare. Budget $400–700 at a diesel shop depending on how many they replace.

**Recommendation:** Replace all 8 while they're in there. At 2018 with however many miles, if 2-3 are failing the rest aren't far behind. Don't do half the job.

How many miles on the 2500?

### SCOTT (2026-04-17T21:41)
I literally just replaced them all about a year or two ago. Any chance a false alarm.

### CLAUDE (2026-04-17T21:42)
 That's very relevant context — and yes, absolutely a possibility worth investigating before paying for another round.

**Two likely culprits given recent replacement:**

**1. Glow plug controller/module failure**
The L5P Duramax has a known glow plug control module (GPCM) issue. The module controls and monitors each plug — if it's failing or has a bad connection, it throws plug codes even when the plugs themselves are fine. This is actually more common than the plugs failing again.

**2. Wiring/connector issue**
If the harness connectors weren't fully seated during the last replacement, or have since corroded, you get exactly these codes. Cylinders 2, 3, and 5 being the problem cylinders is a pattern worth noting — could point to a specific connector or harness branch.

**What I'd do before spending money:**
1. Pull the GPCM connector and inspect for corrosion or pushed-back pins
2. Check the individual glow plug harness connectors at cylinders 2, 3, and 5
3. Clear all codes and see what comes back — and how fast

**The tell:** If the plugs were the actual problem, you'd feel it on cold starts. Are you experiencing any hard starting or rough cold idle? If the truck fires up perfectly, the GPCM or wiring is the far more likely story.

Who did the glow plug replacement — shop or DIY?

### SCOTT (2026-04-17T21:44)
The dealership, or the “steal-ership” as I like to call it. Did the swap. The truck was starting and running fine then. And it still starts and runs fine today.

### CLAUDE (2026-04-17T21:44)
 That seals it — **this is almost certainly not the glow plugs themselves.**

**Here's the real picture:**

The truck runs and starts perfectly, which means the plugs are doing their job. What you likely have is one of these:

**Most probable: GPCM issue**
The Duramax Glow Plug Control Module is a known weak point on these trucks. It monitors plug resistance and throws codes when readings fall outside spec — even if the plugs are functional. A marginal or failing module generates exactly this scatter pattern across multiple cylinders.

**Second possibility: Dealership didn't fully reseat connectors**
Not uncommon. They replace the plugs, rush the reassembly, a connector on cylinder 2, 3, or 5 isn't fully clicked home. Vibration over a year or two loosens it further. Codes follow.

**The honest truth about the dealership angle:**
If you go back to them with these codes, they'll quote you glow plugs again. Don't let that happen. Find a good independent diesel specialist — someone who works Duramax specifically — and have them test the GPCM and inspect the connectors before touching anything else.

**GPCM replacement runs $200-400 parts and labor** — far cheaper than another set of plugs you don't need.

Is this truck still under any powertrain warranty given it's a 2018?

### SCOTT (2026-04-17T21:45)
I doubt it. How long is the power train warranty?

### CLAUDE (2026-04-17T21:45)
 GM's standard powertrain warranty is **5 years / 60,000 miles** — whichever comes first.

A 2018 is now 7-8 years old, so **you're out on time regardless of mileage.** That ship has sailed.

**However — one angle worth checking:**

If the dealership replaced the glow plugs and the GPCM failure is directly related to that service, you might have a **warranty of workmanship argument**. Most shops warranty their own labor for 12 months / 12,000 miles. If the connector issue stems from their reassembly, that's on them.

Probably a long shot at this point given the time elapsed, but worth knowing the principle.

**The more important question is mileage.** How many miles on the 2500? That determines how aggressively I'd chase this repair versus just monitoring it. If you're at 60k miles it's a different conversation than 150k miles.

### SCOTT (2026-04-17T21:45)
180,000

### CLAUDE (2026-04-17T21:45)
 At 180k on a Duramax, here's the honest assessment:

**The good news:** L5P Duramax engines routinely go 300k+ with proper maintenance. 180k is mid-life on this platform. The engine itself is not a concern.

**The pragmatic take at this mileage:**

Don't ignore the GPCM codes indefinitely, but you're not in crisis mode either. The truck starts and runs fine, which means you have time to be strategic about it.

**What I'd actually do:**
1. Find a reputable independent diesel shop — not the dealership
2. Have them scan and specifically test the GPCM output to each cylinder
3. If it's the module, replace it — it's a reasonable repair at this mileage
4. If it's a connector, that's a cheap fix

**The number that matters most at 180k on a Duramax:**
- Is your EGR system clean or carboned up?
- Has the CP4 fuel pump been addressed? The L5P actually moved to a CP3-style pump which is more reliable, but still worth knowing your fuel system history
- Transmission fluid history?

At 180k a Duramax that starts and runs perfectly is worth maintaining properly. The glow plug codes are annoying but not existential. **Budget $300-500 to get the GPCM diagnosed and resolved and move on.**

What's your maintenance history been like on it?

### SCOTT (2026-04-17T21:47)
I get the oil changed religiously. Have had work like the glow plugs and injectors replaced as needed.

### CLAUDE (2026-04-17T21:47)
 That's exactly the right way to maintain a Duramax. Injectors already done is a big one — that's often a $4-6k job and you're past it.

**Honest assessment of where you stand:**

A religiously maintained L5P Duramax with injectors already replaced and 180k on the clock is in genuinely good shape. These engines with proper care have well-documented 400k+ examples. You're not even halfway there potentially.

**Your actual risk profile right now is low:**
- Oil changes handled ✅
- Injectors done ✅
- Glow plugs recently replaced ✅
- Starts and runs perfectly ✅

The GPCM/connector issue is the only real open item and it's not a reliability threat — it's an annoyance and a check engine light.

**The one thing I'd add at 180k if not already done:**
- **Transmission fluid and filter** if it hasn't been serviced in the last 50k miles — Allison trans behind that Duramax is bulletproof but it likes fresh fluid
- **Coolant flush** if overdue — Duramax cooling systems develop DCA (diesel coolant additive) depletion issues over time that silently cause liner pitting

**Bottom line:** You've got a truck that could easily go another 150-180k with your maintenance approach. Fix the GPCM, keep doing what you're doing, and don't let anyone sell you anything you don't need.

### SCOTT (2026-04-17T21:48)
I’ll find a diesel mechanic who can do all of that. For now I cleared the codes to see how long before they come back.

### CLAUDE (2026-04-17T21:48)
 Smart move on all counts.

**Clearing the codes tells you a lot:**

- **Come back immediately (1-2 start cycles)** → GPCM or wiring issue, not the plugs
- **Come back after a few weeks** → Intermittent connection problem, still not the plugs
- **Come back only in cold weather** → Possibly a marginal plug or two, but GPCM still suspect
- **Don't come back at all** → Ghost codes, monitor and move on

**The diagnostic value here is real** — you just turned the truck into its own test instrument. Note the date and outside temperature when they return.

**On finding a diesel mechanic:** In the Atlanta area you have good options. Look for shops that specifically advertise Duramax or diesel truck experience — not general mechanics who "also do diesels." The difference in diagnostic accuracy is significant. Google reviews mentioning Duramax or 6.6 specifically are a good filter.

**Recap of your open items across both trucks:**
- Yukon: Oil pressure sender swap (do it soon)
- 2500HD: Monitor code return, then GPCM diagnosis, coolant flush, trans fluid if overdue

You've got a solid handle on both vehicles. The MaxiLink is already earning its keep today.

### SCOTT (2026-04-17T21:48)
I’m not in Atlanta. You know that. I fucking hate Atlanta.

### CLAUDE (2026-04-17T21:48)
 Ha — fair point, my mistake. **Franklin, GA area** — you're right, I know that.

Smaller pool of shops out that way, but honestly that works in your favor — good independent diesel mechanics in rural areas tend to be the real deal. Word of mouth from other truck and farm equipment owners in Heard County will get you further than Google reviews anyway.

Anyone in your farming network running Duramaxes who has a guy they trust?

### SCOTT (2026-04-17T21:49)
I’m going to ask around.

### CLAUDE (2026-04-17T21:49)
 That's the right call. A personal referral from someone running similar equipment carries more weight than any review site.

Let me know what the codes do — whether they come back fast, slow, or not at all will tell you a lot about what you're actually dealing with on the 2500. And update me when you swap the oil pressure sender on the Yukon. Should be a satisfying 15-minute win.
