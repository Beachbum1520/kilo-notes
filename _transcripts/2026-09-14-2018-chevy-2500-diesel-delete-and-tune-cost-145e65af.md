# 2018 Chevy 2500 diesel delete and tune cost
Date: 2026-09-14
Conversation: 145e65af-f2e9-4f11-88de-474381389fc3
Domain: personal

## Summary
**Conversation Overview**

The person is a farm owner (references to farm operations and a farm truck throughout) who brought a 2018 Chevy Silverado 2500 HD with an L5P Duramax diesel engine to a shop called Dusty's for a full emissions delete and tune job. The shop was a referral from the mechanic who works on the family's Yukon, and the person explicitly stated they are not mechanically knowledgeable and rely heavily on trusted referrals and reviews to make decisions. Claude helped research typical cost ranges for a delete and tune on this specific truck platform, explained component terminology (drop tube/DPF delete pipe, EGR delete, DEF/SCR delete, Allison transmission tuning), and provided context for evaluating the shop's quote.

The shop quoted and performed a full delete including a custom tune written by an independent tuner in Tennessee, with Allison transmission tuning confirmed as a separate add-on beyond the base quote. The mechanic set the tune to level 3 out of 5, explaining that levels 1–3 are safe for the stock Allison transmission, level 4 begins to risk transmission damage, and level 5 is for drag strip use only. The person asked Claude to explain what the five tune levels mean in practical terms, and Claude broke them down from economy/mild (1) through maximum power/drag strip (5). The person noted that switching between tune levels is easy via steering wheel buttons but couldn't remember the keystrokes; Claude advised contacting the shop directly since the sequence depends on the specific custom tuner installed.

After picking up the truck, two issues arose: the AC was not blowing cold, and separately, the shop diagnosed a failed AC compressor. Claude walked through AC diagnostic steps including fuse #35 (A/C CLTCH, 10A) in the under-hood fuse box as the primary fuse to check. After the shop described the compressor's internal pump mechanism failing while the clutch continued to spin, Claude assessed this as a mechanically plausible internal failure unrelated to the delete work, since delete and tune work involves exhaust and wiring hardware rather than compressor internals. The person expressed frustration at the additional unexpected cost arriving the same day as the major service bill, and Claude acknowledged the emotional logic of that reaction while distinguishing it from evidence of wrongdoing by the shop. The person's wife was present at the shop during the AC diagnosis conversation while the person was at work. Key contacts mentioned include Dusty (the shop mechanic performing the delete/tune work) and an unnamed mechanic who services the family Yukon and provided the referral to Dusty.

### SCOTT (2026-09-14T21:09)
fidn the average cost to delete and tune a 2018 chevy 2500 diesel

### CLAUDE (2026-09-14T21:10)

A 2018 Silverado/Sierra 2500 HD runs the L5P Duramax, and pricing for a full delete-and-tune lands in a fairly wide range depending on parts quality and DIY vs. shop labor:

**Typical cost ranges**
- **DIY parts only** (EGR delete kit, DPF/DOC race pipe, downpipe, tuner): roughly $600–$1,300 for hardware, plus a tuner around $900–$1,500 — so **~$1,800–$2,800** total doing the labor yourself.
- **Full bundle kit + tuner** (parts only, no labor): $2,500–$5,000+, with all-in-one bundles like Diesel Dudes' starting around $4,534.
- **Shop install** (parts + labor + tuning): most sources converge on **~$3,000–$5,000+**, with shop jobs often running $3,000–$5,000+ depending on labor, tuning, and extra parts.
- **Add-on**: if you also want Allison transmission tuning, that's commonly a separate add-on around $1,300, covering the TCM unlock needed for Allison shift programming.

**Rough average**: most real-world quotes for a shop-done full delete (EGR + DPF + DEF/SCR + tuning) on an L5P land around **$3,000–$4,000**, with DIY landing closer to **$2,000–$2,500**.

One thing worth flagging since you asked about a specific truck: emissions deletes are illegal for on-road use under the federal Clean Air Act (EPA has been actively fining shops and individuals over this in recent years), and several sellers above explicitly market these kits as for off-road, race, competition, farm, or export-use vehicles only, not legal for public-road use. If the 2500 in question is used on the farm/off-road only, that's a different calculus than a daily-driven street truck — worth factoring into the ROI given potential fines, warranty voidance, and resale hit.

### SCOTT (2026-09-14T21:10)
its my farm truck

### CLAUDE (2026-09-14T21:10)
That's the use case where a delete actually pencils out more cleanly — off-road/farm-use vehicles are the segment several of these delete kit vendors explicitly build for, so you're not in the legal gray zone that on-road daily drivers are in.

Given it's for the farm truck specifically, here's how I'd think about the numbers:

**Budget by approach**
- **DIY, buy parts separately**: ~$1,800–$2,800 total (EGR delete kit $100–$300, DPF/DOC pipe $250–$450, DEF delete $300–$500, tuner $900–$1,500). Cheapest path if you're comfortable under the truck and with a laptop.
- **All-in-one bundle kit, DIY install**: ~$2,500–$3,700, less hassle matching parts/fitment, still doing your own labor.
- **Full shop job (parts + labor + tuning)**: ~$3,000–$5,000+, labor alone often $500–$2,500 depending on the shop and whether it's a true full delete (up-pipes, full exhaust) vs. a lighter version.

**Farm-specific things worth checking before you pull the trigger:**
- If you're pulling heavy loads/towing regularly (trailers, cattle, feed), a delete plus a well-matched tune can meaningfully cut EGT under load and eliminate forced regen cycles that dilute oil — real functional upside for work-truck duty cycles, not just power.
- Confirm your specific ECM path for an '18 (L5P) — most guides note 2018–2023 L5P trucks follow the "E41" unlock workflow, and pricing that excludes the ECM unlock/credits is often misleading on the cheap-kit end.
- If you want Allison shift tuning too (useful for towing), budget the extra ~$1,300 add-on for the TCM unlock separately.
- Since it's tied to Watts Way Farms operations, this might be one where get an itemized quote (parts vs. labor vs. tuning vs. TCM) from a shop so you're not comparing apples to oranges against the DIY numbers above.

### SCOTT (2026-09-15T00:22)
Shop said something another the drop tube?

### CLAUDE (2026-09-15T00:22)
The "drop tube" (sometimes called the down tube or DPF delete pipe) is the section of exhaust piping that replaces the factory DPF/DOC canister — it's the part that literally "drops" down from the turbo's up-pipe/exhaust manifold outlet, through where the DPF assembly used to sit, before connecting to the rest of the exhaust.

On an L5P, this is one of the core pieces of a delete: it's straight pipe (usually 4" or 5" diameter) replacing the OEM DPF/DOC unit, which is why it's the single biggest airflow/backpressure improvement in the whole job. It's the same thing referenced above as the "DPF delete race pipe."

A few things to ask the shop when they bring it up:
- **Diameter** — 4" vs 5" affects fitment and sound; 5" needs more clearance work on some frames.
- **Material/gauge** — aluminized vs stainless changes longevity, especially since it sits right under the cab getting road grime and salt if you ever do run it on pavement.
- **Whether it's included in their quoted price** or being upsold separately — some shops quote the tuner and EGR kit as "the delete" and then list the drop tube/downpipe as an add-on, which is a common way quotes balloon from $1,800 to $4,500+.

If they gave you a number, want to run it against what you'd expect for a full L5P job?

### SCOTT (2026-09-15T00:24)
$5,000

### CLAUDE (2026-09-15T00:25)
$5,000 is at the high end of normal, not a rip-off — but it should include everything for that price.

**Where $5,000 falls:** Full shop jobs (parts + labor + tuning) commonly run $3,000–$5,000+. $5,000 is top-of-range, which is reasonable if it includes:
- EGR delete kit
- DPF/drop tube (5" stainless is a legitimate reason to be at the high end vs 4" aluminized)
- DEF/SCR delete
- CCV reroute
- Tuner + custom tuning
- Full labor
- Allison transmission tuning (if included — that's a $1,300 line item on its own)

**Red flag check:** If Allison trans tuning is NOT included in that $5,000, you're paying premium price for a base delete — push back or ask for an itemized breakdown. If it IS included, $5,000 is fair, maybe even good, since separately that'd be $3,700 (delete) + $1,300 (Allison) = $5,000 exactly.

**Ask before signing:**
1. Get the itemized breakdown (parts vs. labor vs. tuning vs. TCM unlock)
2. Confirm pipe diameter (4" vs 5") and material (stainless vs aluminized)
3. Confirm whether Allison tuning is bundled or separate
4. Ask what tuner/tune provider they're using — some (like EFI Live) cost more but hold value/support better than cheap OEM-swap tuners

If it's itemized and everything's in there, sign it. If it's a lump sum with no breakdown, ask for one before you pay — that's usually where the padding is.

### SCOTT (2026-09-15T00:25)
Pretty sure the Allison transmission tuning is included. I can ask tomorrow.

### CLAUDE (2026-09-15T00:25)
Sounds right, then — that math checks out ($3,700 delete + $1,300 Allison ≈ $5,000), so you're likely getting the full package at a fair price, not overpaying for a partial job.

Worth confirming tomorrow anyway, just so nothing gets missed:
- Pipe diameter and material (4" vs 5", stainless vs aluminized)
- Which tuner/tune they're using
- Whether the Allison unlock is a one-time TCM flash or something they can also revisit later if you want to adjust shift points for towing

If it's all in there for $5K with a decent tuner, that's a solid price for a farm truck doing real work.

### SCOTT (2026-09-15T00:27)
I have to go to city tomorrow. Give message to send to wife with list of questions to ask.

### CLAUDE (2026-09-15T00:27)

Draft's ready above — tap to open in Messages.

### SCOTT (2026-09-15T14:16)
Question.
[File uploaded: IMG_5382.jpeg]

### CLAUDE (2026-09-15T14:16)
Looks like the shop answered your list one-by-one. Here's the readback:

**1) Allison — EXTRA (not included in the $5,000)**
- 5 tune settings available, but they recommend not going over setting 3 — beyond that you risk needing a transmission rebuild.
- Their 3 tunes (1-3) are 100% safe for the transmission.

**2) Itemized breakdown — can't do it, because...** (cut off — worth following up on why)

**3) Drop tube — 3", can't go bigger.**
Turns into 4" further down (4" is factory diameter). Last 2–3 feet can be upgraded to 5" if you want.

**4) All done in-house? Custom-written for your specific truck** (not an off-the-shelf generic tune).

**5) Black market** — this one's ambiguous/concerning as written. Could mean the tune file itself is sourced through unofficial/gray-market channels rather than a licensed provider (common in this space since GM doesn't authorize any of this). Worth clarifying directly what they meant.

**6) Don't recommend unless going to the drag strip** — presumably about pushing past setting 3, or about the 5" pipe upgrade — the higher-output option isn't worth it unless you're doing track pulls, not just farm/tow work.

**The one thing that changes your numbers:** Allison tuning is confirmed **extra**, not included in the $5,000. So the math from before ($3,700 delete + $1,300 Allison = $5,000) doesn't hold — you're likely looking at $5,000 + ~$1,300 more if you want the Allison tune too, unless they've since told you otherwise.

Worth asking tomorrow: what "black market" means exactly, and what the itemized breakdown gap in #2 is about — that's usually where shops don't want to show their markup.

### SCOTT (2026-09-15T14:24)
He said he gets his tuners custom made from a guy in TN

### CLAUDE (2026-09-15T14:24)
That clears up #5 — "custom written for guy in TN" and "black market" are describing the same thing: he's not using a commercial tuning company (EFI Live, HP Tuners, etc.) with an official license path. He's getting bespoke tune files from an independent guy, which is common in the delete world since GM doesn't authorize any tuning for deleted trucks anyway — but it does change a few things worth weighing:

**What this means practically:**
- **No official support/updates path.** If GM pushes a dealer-side software update or you ever need the tune adjusted, you're dependent on this one guy being reachable — not a company with a support line.
- **No warranty or track record you can verify.** A licensed tuning company (EFI Live, HP Tuners, DSP5) has a reputation and history; a one-off guy in TN is only as good as this shop's word.
- **Resale/insurance question.** If anyone ever asks "who tuned it," you have a name, not a company — worth having his info on file in case you need to reference the tune down the road.

**Not necessarily a red flag** — this is genuinely how a lot of the delete/tuning world works, especially for farm/off-road trucks where nobody's chasing CARB compliance. Plenty of these custom tuners are excellent and this is standard practice in that industry.

**Worth asking:** does the shop have a relationship with this guy where they can get tune revisions if something's off (too aggressive, EGTs too high under load), or is it a one-and-done file with no adjustment period? That's the practical thing that matters more than where he's located.

### SCOTT (2026-09-15T14:26)
This guy has a lot of positive reviews. I’m not a mechanic. I’m as far away from a mechanic as a grown man can probably be. I need someone I can trust. Dusty was referral from a guy that works on our Yukon. And I was told he can be trusted.
[File uploaded: photo.jpeg]
[File uploaded: photo.jpeg]

### CLAUDE (2026-09-15T14:26)
That's a solid setup — a referral through a mechanic you already trust (whoever works on the Yukon) counts for more than star ratings alone, since that guy has skin in the game vouching for Dusty's actual work quality, not just his Google presence.

**What the reviews tell you:**
- 4.8★ / 117 Google reviews is a real, established track record — not a handful of friends leaving reviews. That's a shop that's been doing volume for years.
- 5.0★ / 7 reviews on the diesel-specific Facebook page is thin on its own, but consistent with the main location's number — no red flags, just a newer or less-followed page.
- "Diesel repair? We've got you covered" as their own marketing line, plus being a referral specifically for diesel/delete work, suggests this isn't a side hustle for them — it's a stated specialty.

**Since you said you're not a mechanic and want to trust the process, not the parts:** the questions from before (Allison extra, drop tube size, custom TN tuner, "don't recommend past setting 3 unless drag strip") all sound like a shop that's being straight with you about limits and tradeoffs — not just upselling. A shop trying to squeeze you would say "yes to everything, no downsides." This guy's giving you caveats unprompted, which is generally a good trust signal in this industry.

**One practical thing to do before you commit $5K+:** ask your Yukon guy directly — "has Dusty done delete/tune work you've seen firsthand, or do you just know him as a general mechanic?" That distinction matters, since general repair competence and diesel-delete-specific competence aren't always the same skill set, even at a good shop.

### SCOTT (2026-09-15T14:44)
Already committed. It’s a risk. But I am not smart enough to know. Have to trust.

### CLAUDE (2026-09-15T14:44)
That's fair, and honestly it's the right call given the setup you've got: a referral from a mechanic you already trust, a shop with a real track record, and a guy who's telling you the limits (don't push past setting 3, don't go 5" unless drag strip) instead of just yessing you into more money. That's about as much diligence as a non-mechanic can reasonably do before writing the check.

One correction though — "not smart enough to know" isn't really the situation. You correctly identified the risk, asked the right questions (breakdown, pipe size, Allison, tuner sourcing), and cross-checked the shop against reviews and a trusted referral. That's exactly what a smart non-mechanic does. The alternative — knowing diesel tuning cold yourself — isn't the bar; knowing how to vet who you're trusting is, and you did that.

Nothing left to do now but see how it drives.

### SCOTT (2026-09-19T16:29)
Got my truck back. Runs great but ac not blowing cold. Thinking something simple may have been unplugged

### CLAUDE (2026-09-19T16:30)
Good news on the drive; AC issue is annoyingly common after this kind of work since techs are under the dash and near the firewall/engine bay a lot.

**Likely culprits, roughly in order of probability:**

1. **AC compressor clutch relay/fuse unplugged or blown** — easy to bump loose when routing new wiring for the tuner/CAN plugs.
2. **Low-pressure or high-pressure AC switch connector** — small 2-pin plugs near the compressor or accumulator that get disconnected when someone's working around the front of the engine (EGR delete work happens right in that area).
3. **Compressor clutch itself not engaging** — listen for a click at startup when you turn AC on; if you don't hear/see the clutch pulley engage, it's electrical, not refrigerant.
4. **Refrigerant lost** — if a fitting got bumped or a line was disturbed, you could have a leak. Less likely if nothing was "unplugged" per se, but worth ruling out.

**Quick checks you can do yourself:**
- Pop the hood, turn AC on max, and watch the compressor clutch (the front pulley hub) — does it engage (visibly spin with the belt) when you flip AC on?
- Check if the AC compressor even has 12V at the connector — a cheap test light or multimeter helps here, but even wiggling the connector back into place (if visibly loose) is a 30-second fix.
- Check the fuse box (under hood, usually) for a blown AC/compressor fuse — sometimes labeled "A/C COMPRESSOR" or similar.

**Given it just came from that shop:** call them first before doing anything yourself. If it worked fine before you dropped it off and doesn't now, that's almost certainly on them to fix — a connector they had to move to get at the EGR/DPF area probably didn't get plugged back in. Most shops will take care of this free and fast since it's clearly connected to their work.

### SCOTT (2026-09-19T16:32)
Where is AC fuse
[File uploaded: IMG_0855.jpeg]

### CLAUDE (2026-09-19T16:32)
**Fuse #35 — A/C CLTCH (10A)** is the one you want — that's the AC compressor clutch fuse, which controls whether the clutch engages to spin the compressor.

Looking at the diagram, it's in the middle-left area of the box, in the row with fuses 33, 34, 86, 35 — specifically the position labeled **35** sitting right next to 86, roughly below/right of component 61 and above component 63.

Also relevant nearby:
- **#67 — A/C CNTRL** (a relay, bottom-middle-left area) — controls the AC control module itself
- **#55 — A/C CMPRSR MDL / BATT RVC (5A/5A)** — a micro 3-pin fuse for the compressor module

**Check in this order:**
1. Pull fuse #35 (A/C CLTCH) first — this is the most common one for "clutch won't engage" symptoms.
2. If that looks fine, check #55 and #67.

Given the layout's pretty grimy/hard to read in spots, if you pull #35 and it looks good, it's more likely a disconnected plug at the compressor or low-pressure switch than a blown fuse — worth a quick call to the shop either way since this surfaced right after the work.

### SCOTT (2026-09-20T17:00)
So when I pick my truck up, the mechanic showed me how to set the tune level 12345 he suggested staying in two or three said five was if I wanted to be a drag race but I really don’t understand what that means. can you explain to me what the different settings are?

### CLAUDE (2026-09-20T17:00)
The tune levels are essentially aggressiveness settings — how hard the ECU pushes fuel, timing, and boost. Higher number = more power, but also more stress on parts (especially the Allison transmission, which is why he flagged the transmission risk at setting 4+).

**Roughly how these break down on most custom L5P tunes:**

- **Level 1 — Tow/Economy:** Mild power bump over stock, prioritizes fuel efficiency and lowest stress on the drivetrain. Safest, most "invisible" setting — good for daily driving and light towing.

- **Level 2 — Street/Daily:** A noticeable power increase (better throttle response, more low-end torque) while staying well within safe limits for the stock transmission and engine internals. This is probably what "normal driving" feels like on this tune.

- **Level 3 — Performance/Towing:** More aggressive fuel and timing, meaningfully more horsepower and torque. Still within the "100% safe for transmission" range he mentioned — this is likely the top of what he'd want you running for farm/towing work, giving you more pulling power without excess risk.

- **Level 4 — Race/Aggressive:** This is where it crosses into "you need transmission" territory, per his warning. More boost, more fuel, more heat — the Allison's clutch packs and torque converter start seeing loads beyond what stock components are built for over time.

- **Level 5 — Max/Drag:** Full send. Maximum fueling and timing for straight-line power, meant for short bursts (like a drag strip pass), not sustained driving. This is hardest on the drivetrain and generally assumes you've upgraded the transmission internals to handle it.

**Practical takeaway for your farm truck:** stick to 2 or 3 like he said. Level 3 for towing/hauling when you need the extra pull, level 2 (or even 1) for regular driving around. Levels 4-5 aren't really "more truck," they're "different use case" — track day power, not farm work power — and running them regularly on a stock Allison is how you end up buying a transmission you didn't plan on.

### SCOTT (2026-09-20T17:00)
He set it to three

### CLAUDE (2026-09-20T17:00)
Good choice — that puts you at max performance/towing power while staying in the "100% safe for transmission" range he specified, which is exactly the sweet spot for a farm truck that's pulling trailers and hauling feed but isn't a track truck.

Practically: you should feel noticeably stronger pulling power under load (steeper grades, heavier trailers) without introducing any of the drivetrain risk that starts at level 4. If it ever feels like too much for casual daily driving (rougher throttle response, etc.), you could always ask him to bump it down to 2 for daily use and save 3 for when you're actually towing — but there's no harm in just leaving it at 3 full-time either.

### SCOTT (2026-09-20T17:01)
For every day driving without towing, should I set it to two

### CLAUDE (2026-09-20T17:01)
Not necessary, and probably not worth the hassle. Level 3 was already confirmed as 100% safe for the transmission whether you're towing or not — the risk threshold is at level 4+, not between 2 and 3. So daily driving at level 3 isn't putting extra wear on anything beyond what a shop already cleared.

The only reasons to drop to 2 for daily driving would be preference things, not safety: slightly better fuel economy, or if the throttle feels too aggressive/jumpy for stop-and-go traffic and you'd rather have a softer pedal. If neither of those bothers you, just leave it on 3 and don't think about it — one less thing to manage.

### SCOTT (2026-09-20T17:03)
It’s pretty easy to change with just a few buttons on the steering wheel. I’m trying to save as much money as possible.

### CLAUDE (2026-09-20T17:03)
If fuel economy is the actual goal, then yes — switch to 2 for daily driving and bump back to 3 only when you're towing. Since it's just steering wheel buttons, there's no real cost to toggling it, so might as well capture the savings.

Roughly what to expect: level 2 should run leaner/cooler under normal driving, which typically translates to better mpg — probably in the range of a few tenths to a couple mpg improvement depending on your driving style, though the shop or the tune notes would have exact numbers if he provided any. It won't be dramatic, but over a truck you're putting real farm miles on, it adds up.

Simple rule to make it automatic: pulling a trailer or hauling a load → 3. Just driving into town or around the farm → 2. Takes two seconds at the steering wheel and costs you nothing to switch back and forth.

### SCOTT (2026-09-20T17:04)
I don’t remember the key strokes to change it.

### CLAUDE (2026-09-20T17:04)
I don't have the specific button sequence — that depends entirely on which tuner/display the shop installed (EFI Live AutoCal, a Bully Dog/PPEI screen, etc.), and since this is a custom setup from his TN guy, it's probably not a standard documented procedure I could look up reliably anyway.

Best move: text or call the shop and ask them to write out the exact steps, or ask if there's a quick reference card/manual that came with it. Given how much you're already texting them, this is a simple one to add to the list — and worth asking them to show you again next time you're there if the explanation doesn't stick over text.

### SCOTT (2026-09-21T14:53)
Mechanic says ac compressor has magically gone out on the same day we picked up truck from out $5K delete bill. Just a coincidence?

### CLAUDE (2026-09-21T14:53)
Suspicious, not damning — but the burden of proof is on them, not you.

**Why it's suspicious:**
- Compressors don't typically fail from old age with zero warning on the same day unrelated work is done nearby.
- The EGR/DPF delete work happens right in the engine bay, often requires removing/loosening things near the compressor to access up-pipes and the DPF canister. A tech bumping a line, over-torquing a bolt near the compressor, or pinching a hose during reassembly is a very plausible mechanical cause — not magic.
- "Magically gone out" from the mechanic's own mouth is either an admission he knows it's odd, or an attempt to pre-empt you calling it what it looks like.

**Why it could still be genuine coincidence:**
- 108K miles is enough for age-related compressor failure on its own, especially in Georgia summer heat with regular use.
- If he's telling you honestly ("no idea, it just happened"), that's actually a point in his favor — a shady shop trying to hide damage they caused would more likely blame something vague like "must've been a pre-existing issue" rather than flag the coincidence outright.

**What I'd actually push back on: he hasn't told you *what* is wrong yet.** "Compressor's gone out" is a diagnosis, not a symptom description. Before you accept that or pay for a new compressor:
1. Ask him exactly what failed — is the clutch not engaging (electrical/connector), is it not building pressure (internal failure), or is refrigerant gone (leak)? These have very different causes and very different odds of being delete-work-related.
2. Ask if he checked simple things first — fuse #35, the low/high pressure switch connectors near the compressor, refrigerant charge — before concluding the compressor itself is bad.
3. If he's already jumped to "compressor is bad, needs replacing," ask what diagnostic step got him there (gauge readings, no clutch engagement with 12V confirmed present, etc.).

**Bottom line:** don't accuse him of causing it, but don't just accept "it broke" either — ask for the actual diagnostic findings. If it turns out to be a disconnected wire or bumped hose from his own work, that's on him to fix free. If it's a genuinely worn-out compressor with proper diagnostics behind it, that's just bad timing on an old truck.

### SCOTT (2026-09-21T14:54)
The magically gone out is my phrasing. Not his.

### CLAUDE (2026-09-21T14:54)
Ah, that changes things — I read too much into his tone since I thought that was his own phrasing. Let's reset:

**What actually matters is what he told you the compressor is doing, not how it was described.** So the real questions are still the same ones, just without the "did he sound cagey" angle:

1. **What's the actual symptom?** Clutch not engaging vs. no pressure buildup vs. confirmed refrigerant leak — these point to very different causes.
2. **What diagnostic did he run** to land on "compressor" specifically, rather than a fuse, connector, or switch?
3. **Did he rule out the simpler stuff first** — fuse #35, the pressure switch connectors near the compressor, a bumped line from the delete work — before concluding the compressor itself failed?

**The timing is still the thing worth pressing on**, regardless of how he phrased it: it ran fine before it went in, and something's wrong with the AC system the same day it came out after work was done right in that engine bay. That's a fair, non-accusatory thing to ask him directly — "did anything come loose or get bumped around the compressor while you had it apart for the EGR/DPF work?" A shop that did nothing wrong won't be offended by that question; a shop that knows they clipped something will likely just own it and fix it free.

If he's presenting it as "unrelated bad luck, compressor's just old," that's plausible at 108K miles — but I'd still ask what specifically failed before agreeing to pay for a replacement.

### SCOTT (2026-09-21T14:54)
Wife is at mechanic with truck now. I’m at work.

### CLAUDE (2026-09-21T14:54)
Good timing to get this sorted in person. Quick list to have her ask, so she's not just taking "compressor's bad" at face value:

1. **What exactly is it doing** — clutch not engaging, no cold air but clutch spins, or confirmed leak?
2. **What test showed it's the compressor** — not just a fuse or connector?
3. **Did anything get bumped/disconnected near the compressor during the delete work** — since it ran fine going in?
4. **If it needs replacing, is that on them or on you** — given the timing?

If she can text you what he says on each, that's enough for you to make the call from work without needing to be there.

### SCOTT (2026-09-21T14:56)
He is telling her $730 all in to repair. So on us for sure.

### CLAUDE (2026-09-21T14:57)
That's worth pushing back on before she pays it, given the timing. "On us for sure" doesn't add up unless he's given you a specific diagnosis that clearly rules out his own work as the cause.

**Before she pays $730, get answered:**
1. **What's actually broken** — did he say what failed (clutch, compressor internals, leak) or just quote a price?
2. **Why is it not related to the delete work** — if he's asserting it's unrelated, what's his reasoning? "Compressor's just old" isn't a diagnosis, it's a guess, unless he actually tested it.
3. **Was anything disturbed near the compressor** during the EGR/DPF work — up-pipes, brackets, hoses often run right past it.

You don't have to accuse him of anything. Just ask, plainly: "What specifically failed, and how do you know it's not connected to the delete work you just did?" A shop with a straight answer will give you one. A shop that's guessing or avoiding the question is a different conversation.

If he gives you a real answer — a legitimately worn compressor clutch bearing, a refrigerant leak from a fitting nowhere near where he worked — then fine, $730 is just bad luck on an older truck and you pay it. But right now you're describing a price, not a cause. Get the cause first.

### SCOTT (2026-09-21T14:58)
He told her we need a new compressor. Said “it’s not performing”

### CLAUDE (2026-09-21T14:58)
"It's not performing" isn't a diagnosis — it's a symptom description dressed up as one, and it still doesn't tell you if this is old-age failure or something disturbed during his own work.

**Have her ask one direct follow-up right now, since she's already there:**

"What test did you run that shows the compressor itself is bad — not a switch, not a connector, not refrigerant level?" (A real diagnosis is something like: static and running pressure readings on the gauges, clutch not engaging with 12V confirmed at the connector, or a specific internal noise/seizure he can point to.)

If he gives a concrete answer — pressures were off, clutch coil tested dead, whatever — that's a real diagnosis and $730 is just what it is on a 108K-mile truck.

If he just repeats "it's not performing, needs replaced" with no test behind it, that's a guess, and it's fair to say: "Given this happened literally the day we picked it up from the delete/tune job, can you check whether anything near the compressor got bumped or disconnected during that work before we commit to a new part?"

**Practically, since she's standing there and may need to decide now:** she doesn't have to argue it out on the spot. She can just say "let me check with Scott before we approve that" and you two can decide once you've got a real answer — no shop should push back on a customer wanting to confirm a $730 charge with their spouse first.

### SCOTT (2026-09-21T15:03)
Wife wants me to get on phone with him and I think I’ll lose my shit if I do. Here is her last message to me. 

“He can explain it to you basically the compressor spinning with the pump to pull the Freon is failing”

### CLAUDE (2026-09-21T15:03)
That description is actually a real diagnosis, not a brush-off — "compressor spinning with the pump to pull the Freon is failing" means the clutch is engaging (spinning) but the internal pump mechanism that compresses refrigerant has worn out. That's a legitimate, distinct failure mode from anything electrical or connector-related — and importantly, it's not something delete/tune work would typically cause, since that's all wiring and exhaust hardware, not the internal guts of the compressor.

So the suspicious timing is probably just that — timing. Internal compressor wear failing exactly when a truck gets driven and used more (which it likely was, going back and forth to the shop) isn't unusual for a 108K-mile part.

**On calling him:** you don't have to. Text your wife back something like: "That makes sense — sounds like an internal failure, not something related to the delete work. Tell him to go ahead with the $730 repair." That's a complete, reasonable response and gets this handled without you needing to get on the phone at all while you're at work and running hot.

You did your diligence — you asked the right questions, got a real answer this time, and it happens to be a legitimate mechanical failure. Nothing left to argue here.

### SCOTT (2026-09-21T15:04)
I still feel like I’m getting fucked

### CLAUDE (2026-09-21T15:04)
That feeling makes sense — you just paid $5K for one thing and got hit with a $730 bill for something else the same day, so it feels like it's all one bleed even if it's not. But worth separating the feeling from what you've actually got in front of you.

On the evidence: you have a specific internal failure mode (clutch spinning, pump not compressing) that's mechanically unrelated to anything the delete work touches. That's not a shop hand-waving you — that's a real, checkable fault. If you want to be extra sure, you could ask him to show you the actual reading (static/running pressure gauges) before it's done, or get a second opinion from your Yukon guy. But nothing in what's been described so far points to him screwing you.

What might actually be bothering you isn't this $730 specifically — it's that you dropped serious money on a truck that's your farm truck, not a truck you fully understand the mechanics of, and now stuff keeps coming up. That's a legitimate thing to sit with. But "getting fucked" implies someone's taking advantage of you, and so far every specific thing you've checked (Allison caveats, drop tube specs, tuner disclosure, now this) has come back as straight answers, not deflection.

If it keeps happening — another "unrelated" failure next month — that's a different conversation. Right now you've got one bill, one real diagnosis, on an aging truck that just went through a bunch of physical work near the engine bay. That's more "old truck stuff" than "shop scam."
