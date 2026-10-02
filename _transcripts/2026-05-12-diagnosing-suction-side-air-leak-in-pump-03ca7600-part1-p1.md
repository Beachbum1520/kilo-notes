# Diagnosing suction-side air leak in pump
Date: 2026-05-12
Conversation: 03ca7600-d85b-4302-a5e5-34fd19dff9de
Domain: home-pool

## Summary
**Conversation overview**

This conversation centers on diagnosing and managing a persistent air leak in a residential inground vinyl liner pool's suction system. The pool owner in Hogansville, Georgia has a 26,659-gallon pool with a CircuPool SWG cell, Intermatic mechanical timer, sand filter with multiport valve, and a single skimmer as the only suction point (no main drain). The pump setup involves a 1.5HP motor recently installed, with flex PVC on the suction side and a threaded adapter connecting to the pump suction port. The pool has a 10-foot concrete deck surrounding it with a gazebo over the skimmer area, severely limiting underground access.

The diagnostic process was extensive and iterative. Claude initially suggested pad-side causes (pump lid O-ring, drain plugs, threaded adapter) and shaving cream/water tests, but the owner progressively provided critical history that narrowed the diagnosis: last fall he installed an entirely new 3HP pump that also failed to prime, suggesting the leak predated any pad-side plumbing. The rigid PVC suction plumbing was done last fall during that pump swap, and the current flex PVC was only installed this week, ruling out both as the original leak source. The only constant across all pump attempts was the buried suction infrastructure — the underground line running from the skimmer bottom, under the concrete deck and gazebo, to the pump pad. A specific mechanical stress event was identified: when removing the original pump last fall, the owner may have pushed on the PVC and cracked a buried 90° elbow. Additional supporting evidence included water loss above normal evaporation the previous summer, and the characteristic off/on cycling behavior — the pump works well after restart then progressively ingests more air — which Claude explained is a textbook signature of a buried suction line crack in soil, where the soil saturates during pump-off (water leaks out under positive pressure) then dries during pump-on (air ingests under vacuum).

The owner dug down to expose the suspect buried elbow at the pad side. Counterintuitively, exposing the elbow and flooding the hole did not dramatically worsen or confirm the leak at that specific location, and after a pump-off period for a gauge replacement, the pump ran cleanly for several hours before air ingestion gradually returned around 8:45PM. The concrete deck and gazebo make excavation at the skimmer end impossible without major demolition, and above-ground bypass routing was ruled out because the skimmer is bottom-plumbed and surrounded by concrete with no accessible alternative entry point. CIPP trenchless pipe lining was explored but deemed impractical for 1.5" residential pool pipe with 90° elbows. The owner also noted that during backwash mode the pump basket appeared air-free, though Claude noted this observation is complicated by the SWG cell being bypassed during backwash (not in the flow path) and the brief duration of backwash cycles.

The resolution was a pragmatic workaround: using the existing Intermatic mechanical timer with additional on/off trip pins to cycle the pump off for approximately one hour several times daily. This exploits the soil-saturation reset behavior — brief off-periods allow water to leak out and re-saturate soil around the crack, so each restart gives several hours of clean pumping before air ingestion returns. The owner installed the trip pins and the pump is currently running on the cycling schedule. He expressed no urgency to pursue a permanent fix, reasoning that the workaround functions well and the proper repair should be deferred to a future project (such as liner replacement) that would justify the demolition required. Claude affirmed this approach and noted the owner should monitor for signs of worsening: pump struggling to prime after off-cycles, accelerating water loss, or needing progressively shorter on-cycles.

Throughout the conversation the owner corrected Claude multiple times on key facts — particularly the timeline of which plumbing was installed when, which pump components were reused versus replaced, and the skimmer geometry (deck-mounted with bottom plumbing, not a wall-mounted skimmer with a faceplate accessible from the pool). Claude repeatedly lost track of these corrections and had to be redirected. The owner also caught a significant chemistry error: Claude in this thread incorrectly suggested raising CYA mid-SLAM as a viable option, while Claude had correctly advised in a parallel conversation thread (focused on pool opening and chemistry) never to add CYA during SLAM. The owner flagged this contradiction and Claude acknowledged the error. The owner is running two simultaneous conversation threads on the same pool project — this thread covering the mechanical

### SCOTT (2026-05-12T08:33)
Check out the bubbles. I have an air leak somewhere. Need your help figuring out where. Nothing obvious. Only possible clue is that if I turn the pump off for a few minutes and turn it back on it works pretty good for an extended period, not perfect. Then as time goes on, it starts sucking more and more air and less water.
[File uploaded: IMG_6744.jpeg]

### CLAUDE (2026-05-12T08:33)
 That's a classic suction-side air leak signature, and your "works fine after restart, then degrades" clue is actually the most diagnostic piece of information here. Let me walk through what's happening and where to look.

## What the symptom tells you

When you stop the pump, the suction line refills/equalizes and any small air pocket gets pushed out. On restart, you're pulling solid water for a while. Then as the pump runs, air slowly works its way in through a small leak somewhere on the **suction side** (anything between the pool and the pump impeller — skimmer, suction lines, valves, pump lid, drain plugs, unions before the pump).

The fact that it's gradual rules out a big obvious leak. You're looking for something small: a hairline crack, a dried-out O-ring, a loose union, or a fitting that only leaks under vacuum (won't drip water when off).

## Most likely culprits, in order

**1. Pump lid O-ring and lid itself.** This is #1 by a wide margin. Pull the lid, inspect the O-ring for flat spots, cracks, or grit. Lubricate with pool-grade silicone (Magic Lube or similar — never petroleum). Check the lid sealing surface for nicks. Make sure the lid is hand-tight with even pressure.

**2. Pump drain plugs.** Those little plugs on the bottom/front of the pump volute have tiny O-rings that fail silently. Pull them, check the O-rings, lube, reinstall.

**3. Skimmer.** Since you have no main drain and skim-only, the skimmer is doing 100% of the suction work. Two failure modes:
- Water level dropping below the skimmer weir mid-run, causing it to suck air (check this first — does the level drop as the pump runs, or is it stable?)
- A crack in the skimmer throat or at the skimmer-to-pipe connection underground

**4. Suction-side unions and valve stems.** Any union between the skimmer and the pump. The valve stem O-rings on diverter valves are a common slow leaker.

## The shaving cream test (cheap and effective)

With the pump running and air being sucked in, spray shaving cream (or smear a thick soap lather) around each suspect joint: pump lid edge, drain plugs, unions, valve stems. Where the cream gets sucked in or develops a dimple, that's your leak. Do the pump lid first.

## The "fill the pump basket" test

Stop the pump, fill the pump basket completely with water until it overflows the lid seal area, then watch. If the water level in the basket drops while the pump is off, you have a leak on the pump itself or just upstream. If it stays full when off but degrades when running, the leak is somewhere that only opens under vacuum — almost always an O-ring or hairline crack.

## What the photo shows

That looks like your SWG cell flow chamber with significant bubbling — consistent with suction-side air making it all the way through the filter and into the return plumbing. That's not a leak at the cell itself; the cell is just the visible witness. The air is entering upstream of the pump.

Start with the pump lid O-ring and drain plugs. Probably 80%+ of cases like yours resolve there. Report back what you find and we'll work down the list if needed.

### SCOTT (2026-05-12T08:36)
Could it be underground?

### CLAUDE (2026-05-12T08:37)
 Yes, absolutely possible — and your symptom pattern is actually somewhat consistent with an underground suction leak, though I'd still check the easy stuff first before going there.

## Why underground is plausible here

Your pool is 4+ years past liner replacement, which usually means the underground plumbing is older (often original to the pool). PVC suction lines between the skimmer and the pad can develop:

- Hairline cracks at fittings (especially elbows) from ground settling or freeze cycles
- Failed glue joints that slowly weep
- Cracks at the skimmer throat where pipe meets the skimmer body (very common failure point)
- Damage from tree roots — and you've got pines and oaks all around

The "gradual air ingestion that resets on restart" pattern fits an underground leak because: when the pump is off, the line is full of water at static pressure (slightly positive from pool head). When running, that section goes to negative pressure (vacuum), and any crack that's water-tight under positive pressure will happily suck air under vacuum. Small leak, slow ingestion, exactly what you're describing.

## How to localize before digging

**Isolate the skimmer.** If you have a skimmer plug (the rubber expansion plug for winterizing) or can cap the skimmer suction, plug it and run the pump briefly off whatever else is available. If you're skim-only with no other suction source, you can't run the pump this way — but you *can* do the reverse: plug the skimmer and pressure-test the line.

**Pressure test the suction line.** This is the definitive test:
1. Plug the skimmer suction port at the bottom of the skimmer (Anderson plug or similar)
2. At the pump, disconnect the suction union and cap it with a threaded plug fitted with a Schrader valve or pressure gauge
3. Pressurize the isolated line to ~10 psi with a bike pump or small compressor
4. Watch the gauge. Holds pressure = line is fine. Drops = leak in that line.

If it drops, you can sometimes hear the leak with the line pressurized, or see bubbling in the ground if it's near the surface.

**Dye test the skimmer throat.** With pump running and water level at normal, put a few drops of dark food coloring (or pH reagent) right at the seam where the skimmer body meets the suction pipe at the bottom of the skimmer. If there's a crack there, you'll see the dye get sucked in. This is the single most common underground-ish leak point and the easiest to find.

**Listen at the skimmer.** With pump running and the suspected leak active (after it's been running a while and is pulling air), put your ear near the skimmer. Sometimes you can actually hear air hissing in at a skimmer crack.

## Order I'd actually work through this

1. **Pump lid O-ring + drain plugs + shaving cream test at the pad** — 15 minutes, free, catches most cases
2. **Dye test at the skimmer throat** — 5 minutes, free, catches the most common underground-adjacent leak
3. **Check skimmer water level behavior** — is it dropping below the weir during operation?
4. **Pressure test the suction line** — needs a couple of plugs and a gauge, ~$25 in parts, definitive

If 1 and 2 come up clean and the pressure test fails, then you're looking at an underground repair. The good news: skimmer throat cracks are often repairable from inside the skimmer with pool putty or a proper epoxy without excavation. Actual buried pipe leaks are the worst case and usually mean either excavation or running a new line above ground / through the deck.

Don't jump to digging yet. Work the cheap diagnostics first.

### SCOTT (2026-05-12T08:39)
Water line is fine.

### CLAUDE (2026-05-12T08:40)
 Good — that rules out the most common "false alarm" (skimmer sucking air because the water level dropped below the weir). So you genuinely have a leak somewhere in the suction path.

Given water level is stable, here's where I'd focus next:

## Quick wins to try first (10 minutes, no tools)

**Pump lid test.** With pump running and air ingestion active, pour a cup of water slowly around the pump lid O-ring seal. If the bubbling in the cell briefly stops or reduces, the lid is your leak — water temporarily seals the gap. This is a fast, definitive test.

**Same trick at every union and the drain plugs.** Pour water over each joint, watch the cell. Any change = leak at that spot.

**Pump lid O-ring.** Even if the water test is inconclusive, just pull it, inspect, and lube it. Cheap insurance and the #1 culprit statistically.

## Then the dye test at the skimmer

With pump running and air actively being ingested, get in the pool (or reach in) with a small squirt of dark food coloring or a dropper of pH reagent. Release it right at the base of the skimmer where the suction pipe enters. Watch carefully — if there's a crack at the skimmer throat, you'll see the dye get pulled in like a tiny tornado. This catches a huge percentage of "underground" leaks that are actually right at the skimmer.

Also dye-test around the skimmer faceplate screws and the seam where the skimmer body meets the pool wall (vinyl liner pools sometimes develop leaks at the gasket between skimmer and liner).

## Question that will narrow it down

When the pump has been running long enough that it's pulling significant air, does the **pump basket** show air accumulating in it (a visible air pocket at the top of the basket housing)? Or is the basket staying full of water and the air is somehow getting past it?

- **Air pocket forming in pump basket** = leak is upstream of the pump (skimmer, suction line, or pump inlet union/lid)
- **Pump basket stays full but air still in returns** = leak is at the pump itself (lid, shaft seal pulling air, drain plugs) or between pump and filter, which is rare on suction side

That observation will tell us whether to keep hunting at the skimmer end or focus on the pad.

### SCOTT (2026-05-12T08:45)
I doubt is at the pump. But will test. Actually tried to replace the pump at the end of last summer with a larger 3hp pump. The motor on original pump went bad. It would never get a prime, so I returned it thinking bad pump. Was end of summer so I didn’t reinstall a new pump. Now before the pool “opening ceremonies” you have been helping with, I installed a new motor (1.5hp) to the wet side of my pump and have been proceeding. That makes me think maybe the 3hp pump wasn’t bad. Attached is a pic of the 3hp pump I tried
[File uploaded: 5cea8f8085a7fc3ef774437ed90b32420f8fd624.png]

### CLAUDE (2026-05-12T08:45)
 That's a really important piece of history, and it changes the diagnostic picture significantly. Let me reframe.

## The implication

If the 3HP CIPU pump also couldn't get a prime last fall, and now your repaired 1.5HP pump is pulling air progressively worse over time — **the common factor isn't the pump. It's the suction side of your system.** Two different pumps with the same priming/air problem points strongly to a leak (or restriction) upstream of the pump, not at the pump itself.

A 3HP pump pulls a much stronger vacuum than a 1.5HP. A bigger pump on a leaky suction line will actually struggle *more* to prime, because it pulls air in faster than it can evacuate it. That's a classic symptom and it explains why the 3HP "wouldn't prime" — it probably wasn't defective at all. You may have returned a perfectly good pump.

## What this tells us about the leak

The leak has likely been there since at least last summer. It's been progressive or it was there all along and you're only now noticing it because:

- The 1.5HP pump can overcome a small leak enough to maintain prime (most of the time)
- The 3HP couldn't overcome it during initial prime attempts
- As debris/seasonal changes shift things, the leak is getting worse or more apparent

This also means: **whatever is wrong isn't going to fix itself, and replacing the pump won't fix it.** You need to find and fix the suction leak before any pump — old or new — will work properly.

## Revised priority

Skip the "is it the pump" diagnostics. Go straight to:

1. **Dye test the skimmer throat and faceplate** — most likely culprit on a 4+ year old vinyl pool, especially with no main drain so the skimmer carries the full suction load
2. **Pressure test the suction line** — definitive answer on whether the buried pipe between skimmer and pad is intact
3. **Inspect every suction-side union, valve, and the pump lid** — shaving cream test while running

The pump-lid-and-O-ring stuff is still worth 5 minutes since it's free, but I'd reorient toward the skimmer and the underground line as the prime suspects given this two-pump history.

## On the 3HP pump

For what it's worth: a 3HP variable speed is significantly oversized for a 26,659 gallon pool with a sand filter. Your sand filter has a maximum flow rate (probably 40-60 GPM depending on size) and a 3HP pump at full speed will exceed that, blow channels through the sand, and shorten filter cycles. Variable speed lets you run it slower so it's not catastrophic, but you'd basically never run it above maybe 40-50% — which means you're paying for headroom you can't use. A 1.5-2HP variable speed is the sweet spot for your pool. Don't let "bigger is better" thinking drive the next purchase.

But first: find the leak. Then decide on pump strategy.

### SCOTT (2026-05-12T08:48)
On the “Dye test the skimmer throat and faceplate”. I’m still a little confused. The skimmer throat is the piece at the bottom of the skimmer basket?  It’s under water. How can I see where the waters going with the dye test?

### CLAUDE (2026-05-12T08:48)
 Good question — let me clarify, because "skimmer throat" is one of those terms that gets used loosely.

## Anatomy refresher

Your skimmer has a few key parts:

- **Skimmer mouth/weir**: the opening at the waterline where water flows in (the flap)
- **Skimmer basket**: sits in the body, catches leaves
- **Skimmer throat**: the hole at the **bottom** of the skimmer body, below the basket — this is where water exits the skimmer and enters the suction pipe heading to the pump
- **Skimmer faceplate**: on a vinyl liner pool, this is the plastic frame screwed through the liner that seals the skimmer to the pool wall, with a gasket between liner and skimmer body

The throat itself is at the bottom of the skimmer, but yes — it's submerged when the pool is full. That's actually *why* the dye test works.

## How the dye test actually works

You're not looking for dye to disappear into a visible crack. You're using the dye as a **visible tracer** for water movement that you couldn't otherwise see.

Here's the physics: if there's a crack anywhere on the suction-side plumbing **above the water table** (which underground PVC often is, depending on depth and groundwater), the pump's vacuum pulls air in through that crack. But if the crack is **below the water table** or submerged (like at the skimmer throat or a leak in the pool wall side of the skimmer), the pump pulls *water* in through that crack instead of air — and that water comes from outside the system.

Either way, the dye test reveals it by showing water moving *toward* a spot it shouldn't be going.

## Where to release the dye

With the pump running, you want to release dye **right next to** suspected leak points and watch where it goes:

**1. Skimmer faceplate seam (most common)**: The seam where the plastic faceplate meets the liner around the perimeter of the skimmer opening. Get in the pool, get close, and release a few drops of dark food coloring right along that seam — top, sides, bottom of the rectangular opening. If there's a leak at the gasket, the dye will get pulled *into* the seam rather than dispersing into the pool. You'll see it as a thin stream getting sucked in like water down a drain.

**2. Inside the skimmer, at the throat**: Reach down into the skimmer (pump running, basket removed for visibility) and release dye right at the bottom hole where the suction pipe exits. You won't see anything unusual here normally — the dye will just get sucked down the pipe with the rest of the water, which is expected. But if there's a crack in the *side* of the skimmer body near the throat, you might see dye moving sideways into the crack instead of straight down.

**3. Around the skimmer body exterior** (harder, but useful): If you can see the outside of the skimmer body (sometimes visible through the deck if there's an access, otherwise not), dye along the joint where pipe meets skimmer.

## What you're looking for

- **Dye dispersing normally into the pool water**: no leak there, move on
- **Dye getting pulled in a clear directional stream toward a specific spot**: that's your leak. Water (and air, when the level changes or the leak shifts) is being drawn in through that spot.

It's a subtle visual. Use **dark** food coloring (red or blue work well), make sure the water near the skimmer is calm, and release the dye **slowly and close** to the surface you're testing — within an inch or two. If you squirt it from far away it just disperses and tells you nothing.

## Easier alternative for vinyl pools

Honestly, for a 4-year-old vinyl liner pool, the **skimmer faceplate gasket** is such a common failure point that you might just want to skip the dye test and inspect it directly. Drain the water a few inches below the skimmer (or just look closely with a mask on), and check the faceplate screws — are any loose? Is the gasket visible behind the faceplate, and does it look intact? Sometimes you can see daylight or water weeping around the edge.

If you want to be really sure, you can pull the faceplate (it just unscrews — usually 8-10 stainless screws around the perimeter), inspect the gasket, and reinstall with a new gasket if needed. That's a $15 part and an hour of work, and it's a likely fix.

Does that clarify the dye test? And do you want to walk through the skimmer faceplate inspection instead?

### SCOTT (2026-05-12T08:50)
Read my other convo in this project. I’m not getting in this pool right now.

### CLAUDE (2026-05-12T08:51)
 Fair enough — let me check what we've covered before so I'm not retreading ground.

Got it — you're not getting in the water (cold, just opening, probably still working on clarity from the SLAM). That rules out anything that requires being in the pool.

## Dye test from outside the pool

You can do a modified version standing on the deck. You need a dropper or small squeeze bottle with dark food coloring, and a way to release it slowly **right at the surface** near suspected leak points.

For the skimmer faceplate, the only accessible spot from the deck is the **inside of the skimmer itself**. Lift the skimmer lid, remove the basket, and look down into the skimmer body. With the pump running, slowly squirt dye:

- Around the **inside perimeter** of the skimmer body, especially where the body meets the pool wall (the back wall of the skimmer that faces the pool)
- At the **throat** (bottom hole)
- Along the **vertical seams** of the skimmer body if you can see any

You're watching for dye to deviate from the normal flow path. Normal flow = dye sucked straight down the throat with the water. Leak = dye pulled sideways into a crack in the skimmer body, or pulled toward the back wall where the faceplate gasket would be.

This is harder to interpret than the in-pool faceplate test, but it can still reveal a skimmer body crack.

## Skip ahead — better diagnostics from the deck

Given the constraints, I'd reprioritize:

**1. Pressure test the suction line.** This is the most definitive test you can do without getting wet and without guessing. You need:
- A skimmer plug (Anderson plug, ~$10, or the rubber expansion plug you'd use for winterizing)
- A threaded plug with a Schrader valve, or a pressure gauge that threads into your pump suction port
- A bike pump or small compressor

Process:
- Turn off pump
- Open pump lid, remove basket
- Plug the skimmer suction port from inside the skimmer (reach down with the Anderson plug on a stick, expand it)
- At the pump, screw your gauge-fitted plug into the suction side union after disconnecting
- Pressurize to 10-15 psi
- Watch the gauge for 15-30 minutes

Holds steady = suction line and skimmer are fine, leak is at the pump itself. Drops = leak is in the line or skimmer body. Drops fast = significant leak.

**2. Pump-side shaving cream test.** Pump running, spray foam around every joint between the pump suction union and the impeller: union O-ring, lid O-ring, drain plug threads, any visible fittings. Watch the foam — where it dimples or gets sucked in, that's air entering. This catches pad-side leaks in 5 minutes.

**3. Pump lid water test.** Pour water slowly over the pump lid while running. If bubbling in the cell briefly stops, lid O-ring is the leak.

If pressure test holds and shaving cream finds nothing, then we're probably looking at the skimmer faceplate gasket — and that's a fix that can be done from outside the pool by lowering the water below the skimmer mouth, pulling the faceplate, replacing the gasket, and reinstalling. No swimming required.

Which of these do you want to tackle first? The pad-side shaving cream test is the fastest — 5 minutes, no parts needed.

### SCOTT (2026-05-12T08:52)
I also don’t have a flap in mine. If it is the faceplate I assume to drain the pool down below the skimmer opening to replace?

### CLAUDE (2026-05-12T08:52)
 Correct on both counts — and the missing weir flap is normal/common, not a problem. Plenty of pools run without one. It just means more debris reaches the basket, which on your pine-and-oak property is just life. Not related to your air leak.

## Faceplate replacement — yes, drain below the skimmer

To replace the faceplate gasket on a vinyl pool, you need the water level **2-3 inches below the bottom of the skimmer opening**. This exposes the gasket area and lets you work without water pouring in while you have the faceplate off.

## How to drain down

You have a few options, in order of preference:

**1. Backwash + waste through the filter** (if your sand filter has a multiport with a "waste" setting). Pump water out through the waste line until the level drops. This is fastest and uses equipment you already have. Watch the skimmer — once water level gets near the bottom of the skimmer mouth, you'll start sucking air badly and need to stop. You can get down to skimmer level this way but not below.

**2. Submersible pump or transfer pump.** Drop it in the shallow end, run a discharge hose to wherever you're draining (away from the pool, not toward the house foundation, ideally into a yard area that can absorb it). This is how you get the level **below** the skimmer. A cheap 1/4 HP utility pump from Harbor Freight or Home Depot ($80-120) will do this in a few hours. If you don't own one, this is a worthwhile purchase — useful for liner work, partial drains for chemistry resets, and general utility.

**3. Siphon.** A garden hose siphon works if your drain point is lower than the pool. Slow but free. Probably 12-24 hours to drop a few inches.

## How far to drain

For faceplate work specifically, drop the water about **6 inches below the bottom of the skimmer opening**. That gives you working room and a margin so if you bump the water level (rain, splashing), you don't flood the opening while you're working.

**Important**: don't drain a vinyl pool more than necessary. With the pool partially drained:

- The liner is no longer being pushed against the wall by water pressure in that area, so it can shift
- If you drain too low, the liner can pull away from the walls/floor and refitting it is a nightmare ("floating the liner")
- On a hot sunny day, the liner can shrink and stretch unevenly when exposed

For a faceplate gasket replacement, you're only dropping 6-10 inches total. That's well within safe range — liner stays put.

## The faceplate job itself

Once drained:

1. **Unscrew the faceplate** — usually 8-10 stainless screws around the perimeter. Use a hand screwdriver, not a drill. Stainless screws into a plastic skimmer body strip easily.
2. **Pull the faceplate off** — it may stick due to old gasket and butyl sealant. Pry gently with a plastic putty knife.
3. **Inspect the old gasket** — you'll usually find one of:
   - Gasket is brittle, cracked, or compressed flat → that's likely your leak
   - Gasket is intact but butyl sealant behind it has failed → still likely your leak
   - Liner has torn around the opening → bigger problem, may need a liner patch
4. **Remove old gasket and clean both surfaces** (skimmer body face and liner face) of old sealant residue. Denatured alcohol or acetone on a rag.
5. **Apply new butyl sealant tape** to the skimmer body face (the side that meets the liner). This is the actual sealing element — the gasket is mostly a clamping pad.
6. **Install new gasket** over the butyl.
7. **Reattach faceplate** with screws. Tighten in a star pattern, snug but not gorilla-tight (you'll deform the gasket or strip threads).
8. **Refill pool above skimmer** before running pump.

## Parts you need

- **Skimmer faceplate gasket** — generic vinyl pool skimmer gaskets fit most standard skimmers (Hayward SP1084, Pentair, etc.). $5-10. Or you can cut your own from gasket material if your skimmer is non-standard.
- **Butyl sealant tape** for pool skimmers (sometimes called "pool putty tape" or "skimmer butyl") — $10-15
- **Replacement stainless screws** if any are corroded — usually #10 x 1" stainless pan head
- **New skimmer faceplate** itself only if the old one is cracked

Identify your skimmer brand/model before ordering. Look inside the skimmer body for any molded-in branding, or measure the faceplate opening (standard is usually around 9" x 14" but varies). Common brands on vinyl pools: Hayward SP1084 series, Pentair Admiral, Aquador.

## Before you commit to this

Faceplate gasket replacement is a real job — not hard, but a few hours and requires partial drain. Before you commit:

- **Do the pad-side shaving cream test first** (5 minutes, free, no drain)
- **Then the pressure test** if shaving cream is clean (~$25 in parts, definitive)

If pressure test shows the line holds, then the leak is between the suction side of the pump and impeller, or at the skimmer body itself (gasket included). At that point you've narrowed it down enough to justify the drain-and-replace.

Don't drain the pool yet. Knock out the cheap diagnostics first.

### SCOTT (2026-05-12T08:54)
Tell me again how to pressure test.

### CLAUDE (2026-05-12T08:55)
 ## Pressure testing your suction line

The goal: isolate the suction line (skimmer → pad), pressurize it with air, and watch if pressure holds. If it drops, you have a leak in that line.

## Parts you need

**1. Skimmer plug (Anderson plug / expansion plug)**
- A rubber expansion plug that goes into the skimmer's bottom port (the throat where the suction pipe begins)
- Has a wing nut on top — turn it, the rubber expands and seals the pipe
- Size: typically **1.5" or 2"** depending on your skimmer plumbing — measure the opening at the bottom of your skimmer first
- $8-15 at any pool supply or Amazon. Search "pool skimmer expansion plug" or "Anderson plug 1.5 inch"

**2. Pressure test plug with gauge**
- This is the plug that screws into the pump's suction port (or into the union after you disconnect the pump)
- Two options:
  - **Pre-made pressure test plug kit** — has the plug, a Schrader valve (like a tire valve), and sometimes a gauge built in. Search "pool pressure test plug" or "Anderson plug with Schrader valve." $20-40.
  - **DIY**: a threaded PVC plug + a Schrader valve installed in it + a separate gauge. More work, but cheaper if you have parts.
- Needs to match your pump suction thread size — usually **1.5" or 2" MPT** (male pipe thread)

**3. Pressure gauge**
- 0-30 psi range is ideal (low pressure, better resolution)
- If your test plug kit includes one, you're set. Otherwise, a separate gauge that threads into the Schrader fitting or T's into the line

**4. Bike pump or small compressor**
- Hand bike pump works fine — you only need 10-15 psi
- Or a small 12V compressor, or shop air

## The test, step by step

**1. Turn off the pump and SWG.** Pull the power. You don't want anything cycling on during the test.

**2. Plug the skimmer.**
- Remove the skimmer basket
- Reach down to the bottom of the skimmer where the suction pipe exits (the throat)
- Insert the expansion plug into that opening
- Turn the wing nut on top to expand the rubber and seal the pipe
- Tighten until snug — it should not pull out with hand pressure

This isolates everything between the skimmer and the pump from the pool water.

**3. Disconnect the pump from the suction line.**
- Find the union on the suction side of the pump (the threaded plastic collar between the pump inlet and the PVC pipe coming from the ground)
- Unscrew the union — water will spill out, that's expected
- Pull the pump side back enough to expose the threaded end of the suction pipe (the pipe coming up from underground)

**4. Install the pressure test plug into the suction pipe.**
- Screw your pressure test plug (the one with the Schrader valve) into the threaded end of the suction pipe where the union used to connect
- Hand-tight is usually enough; you can use Teflon tape on the threads for a better air seal
- Attach your pressure gauge if it's not already integrated

**5. Pressurize.**
- Connect bike pump to the Schrader valve
- Pump air in slowly — watch the gauge
- Stop at **10-15 psi**. Do not exceed 20 psi. Higher pressures can damage PVC fittings or pop the skimmer plug.

**6. Watch the gauge.**
- Mark the starting pressure
- Wait 15-30 minutes
- Check the gauge

## Reading the results

**Pressure holds steady (drops less than 1 psi over 30 min):** The suction line and skimmer body are airtight. Your leak is at the **pump itself** — lid O-ring, drain plugs, shaft seal, or the union you just disconnected. Focus diagnostics there.

**Pressure drops slowly (1-3 psi over 30 min):** Small leak somewhere in the line. Could be a hairline crack, a marginal fitting, or a slowly failing skimmer gasket. Need to localize.

**Pressure drops quickly (5+ psi in a few minutes):** Significant leak. Could be a cracked pipe, a failed glue joint, or the skimmer plug isn't sealing well (check that first).

**Pressure won't build at all:** Either a major leak, or your plug/connections aren't sealing. Double-check the skimmer plug and the threaded connections at the pump end before assuming the worst.

## If you have a leak — finding where

Once you know the line is leaking, you can localize:

**Listen.** With the line pressurized, walk along where the underground pipe runs and listen for hissing. Sometimes audible at a crack.

**Soap test visible joints.** Spray soapy water on any visible fittings, unions, or exposed pipe. Bubbles = leak.

**Wet spots.** If the leak is significant, you may see water seeping up through the ground above the pipe path (though air leaks don't always do this).

**Watch the skimmer.** If the leak is at the skimmer body itself (not the line), pressurized air will bubble out into the skimmer water. Look down into the skimmer with a flashlight while pressurized — bubbles coming up around the plug or from inside the skimmer body wall = your leak is right there.

## Reassembly when done

- Release pressure by depressing the Schrader valve
- Remove the test plug
- Remove the skimmer plug
- Reconnect the pump union (check that O-ring while you're at it — replace if worn)
- Refill pump basket with water before starting pump (it'll need to re-prime)

## What to buy

If you want a one-stop solution, search Amazon for "**pool pressure test kit**" — you'll find sets that include the expansion plug, the threaded plug with Schrader valve, and a gauge for $30-50. Anderson Manufacturing makes the standard ones. Make sure the sizes match your plumbing (1.5" is most common on residential pools, but verify).

Cheaper DIY route: expansion plug ($10) + threaded PVC plug ($3) + Schrader valve insert ($5) + small pressure gauge ($10) = ~$30, but you'll need to drill and tap the plug for the Schrader, which is fiddly. The kit is worth the extra few bucks.

Want me to look up specific products on Amazon, or do you want to figure out the sizing first?

### SCOTT (2026-05-12T08:58)
“Unscrew the union — water will spill out, that’s expected”

That entry point into the pump is not removable. It’s 1 1/2” PVC that is glued to the pipe that runs underground to the pool.

### CLAUDE (2026-05-12T08:59)
 Ah, that's a different situation — and actually a fairly common configuration on older pool installs. Someone glued the PVC directly into the pump's threaded suction port instead of using a union (or there was a union and a previous owner replaced it with a hard glue joint). Annoying for service, but workable.

## Your options

**Option 1: Test from inside the pump basket (easiest)**

You don't actually have to disconnect the line. You can pressurize from inside the pump itself:

1. Plug the skimmer at the throat as before
2. Make sure pump basket is empty (no water, no basket)
3. Install a **pressure test plug at the pump lid** — basically, you need to seal the pump's suction chamber so air can't escape past the impeller or out the discharge

The tricky part: the pump has both a suction inlet and a discharge outlet. You need to seal both sides of the impeller to pressurize just the suction side. In practice this means:

- Plug the discharge side of the pump (close a valve after the pump if you have one, or plug the discharge port)
- Or alternatively: plug the suction line through the pump basket

A simpler version of this: **use an expansion plug inside the pump basket housing**, sized to fit the opening where water enters the basket from the suction pipe. Look down into your pump basket — there's a hole on the side or bottom where water comes in from the suction line. Plug that opening with an expansion plug fitted with a Schrader valve.

This isolates the underground line between the skimmer plug and the pump basket plug, and you pressurize through the Schrader.

**Option 2: Cut in a union (recommended long-term)**

If the pump suction is hard-piped with no union, you should add one anyway. Pumps need to be serviceable — when you eventually replace the motor or the whole pump, you'll have to cut the pipe regardless. Better to put a union there now.

Process:
- Cut the suction pipe 6-8 inches before the pump
- Glue a union into the cut
- Use the new union to do your pressure test (and every future service)

A 1.5" PVC union is $5-8. PVC primer and glue if you don't have it, $10. 30 minutes of work. Then you have a serviceable pump forever.

This is actually the right answer here. You've already had to replace the motor once on this pump. You're going to need to break this connection at some point — might as well do it during diagnostics and solve two problems.

**Option 3: Test from the skimmer end (alternative)**

Instead of pressurizing from the pump end, you can pressurize from the skimmer end:

1. Plug the pump suction somehow (this still requires accessing the line at the pump — which is your problem)

Yeah, this doesn't really help. Skip.

## My recommendation

Given you'll eventually need to service this pump again, **cut in a union now**. Here's the case for it:

- $5-8 in parts
- 30 minutes of work
- Solves the immediate pressure test problem
- Makes every future service infinitely easier
- Required eventually anyway

If you've never glued PVC before, it's genuinely easy:
- Primer (purple stuff) on both surfaces
- Glue (clear or blue) on both surfaces while primer is still wet
- Push together, twist a quarter turn, hold for 30 seconds
- Wait 1-2 hours before pressurizing or running water

The hard part is the cut and dry-fit. Cut the pipe with a hacksaw or PVC cutter, deburr the end, make sure both union halves dry-fit onto their respective pipe sections before gluing.

If you want to avoid gluing, you can also buy **compression unions** or **push-to-connect PVC fittings** (SharkBite makes them for PVC now). More expensive ($15-25) but no glue. Some pool pros consider these less reliable long-term than glued unions, but for a suction-side connection that sees vacuum (not high pressure), they work fine.

## Want a simpler diagnostic first?

Before you commit to cutting pipe, let me ask: have you done the **shaving cream test at the pump** yet? With pump running and air being pulled, spray foam around:

- The hard-glued joint where pipe enters pump (yes, hairline cracks happen even at glue joints)
- Pump lid edge
- Drain plugs
- Any other visible joint

If the foam dimples or gets sucked in anywhere, you've found the leak without any plumbing work. Takes 5 minutes.

Also worth checking: **is the glue joint at the pump itself leaking?** That hard-piped connection is exactly the kind of spot where a marginal glue job from years ago could finally fail. Look at it closely with the pump running — any drips when off, any visible cracks at the fitting?

Do the shaving cream test first. If that's clean, then commit to cutting in a union.

### SCOTT (2026-05-12T09:02)
This?
[File uploaded: IMG_6753.PNG]

### CLAUDE (2026-05-12T09:03)
 Yes, that's the right part — Apollo 1.5" PVC Slip x Slip Union from Home Depot. Perfect for what you need.

## Confirming sizing

Verify your existing pipe is actually **1.5" PVC** (not 2"). The easiest check: look at the pipe diameter — 1.5" PVC has an outer diameter of about **1.9"** (just under 2 inches). 2" PVC has an outer diameter of about **2.375"**. Wrap a tape measure around the pipe if unsure: 1.5" PVC has a circumference of about **6"**, 2" PVC is about **7.5"**.

You mentioned 1.5" earlier so this is almost certainly right, but worth confirming before you cut.

## What else to grab while you're at Home Depot

- **PVC primer** (purple, small can) — ~$5
- **PVC cement** (clear or blue, for cold weather use "all-weather" or "wet/dry" formula) — ~$5. Get the small can, you'll use a tiny amount.
- **PVC pipe cutter** if you don't have one — the ratcheting kind for 1.5" pipe is ~$15-25. Makes cleaner cuts than a hacksaw. A hacksaw works too if you already have one.
- **Sandpaper or emery cloth** (any grit 80-150) — for deburring the cut and slightly scuffing the pipe surface for better glue adhesion
- **Rag** for wiping primer drips before they set

Total: ~$30 plus the union.

## A note on slip x slip

"Slip x Slip" means both ends are smooth sockets that glue onto the outside of plain PVC pipe. That's what you want here — you're cutting your existing pipe and gluing the union onto the two cut ends.

If your existing pipe at the pump had a **threaded** connection at any point, you'd want slip x thread or thread x thread. But since you said the pipe is glued solid into the pump, both cut ends will be plain pipe, and slip x slip is correct.

## Quick install preview

Once you have parts:

1. Decide where to cut — leave **6-8 inches of straight pipe** between the pump and the union so you have working room to disassemble in the future. Mark the cut line with a Sharpie.

2. Cut the pipe square. PVC cutter is one squeeze-and-rotate; hacksaw takes 30 seconds and a steady hand.

3. Deburr both cut ends with sandpaper — inside and outside edges. Burrs prevent a good seal.

4. Unscrew the union's middle nut so you have three pieces: two slip socket ends and the threaded collar.

5. **Dry fit first.** Slide one socket end onto each cut pipe end. Then thread the collar back on by hand. Everything should align without forcing. If pipes don't align, the cut wasn't square or you need to flex the pipe slightly to seat both sides.

6. Mark the depth on each pipe (a Sharpie line where the socket meets the pipe) so you know how far to push when gluing.

7. Disassemble. Apply primer to both the pipe and the inside of the socket. Apply glue while primer is still wet. Push together to your mark, give a quarter turn. Hold 30 seconds.

8. Do one side at a time. Glue one socket to its pipe, let it set, then do the other. This keeps the union halves properly aligned.

9. Once both halves are glued and set (1-2 hours minimum, ideally overnight), thread the collar back together hand-tight. **Do not use pliers** — over-tightening cracks the union or compresses the O-ring incorrectly.

## Heads up on the union O-ring

PVC unions have an O-ring inside that seals the two halves when the collar is tightened. Some unions ship with the O-ring already installed in one half. Make sure it's there before gluing — if you have to install it after the fact, it can be fiddly. The O-ring is also the part most likely to fail over years; keep a spare.

Once installed and set, you're ready to do the pressure test (and every future pump service is a 5-minute disconnect).

Grab it. This is a good investment.

### SCOTT (2026-05-12T09:05)
The exiting pipe is glued to a 1 1/2” PVC threaded adaptor that screws into the pump. Should I get a threaded adapter and install there?

### CLAUDE (2026-05-12T09:05)
 Yes — that's actually a better setup than a slip union. Use a **threaded union** that screws into the pump where the existing adapter is now. Here's why and how.

## Why threaded is better in your case

You already have a threaded port on the pump. Two big advantages over the slip union approach:

1. **No cutting required.** You can unscrew the existing threaded adapter and replace it with a threaded union. No PVC saw, no glue cure time, no risk of a botched cut.

2. **Future serviceability is even better.** A threaded union means the entire suction line can be disconnected from the pump in two ways: at the union itself (the standard service disconnect) AND at the pump threads if you ever need to swap pumps entirely. Belt and suspenders.

## What to get

You want a **1.5" PVC Union with one Slip end and one Male Threaded (MIPT/MPT) end** — sometimes called a "slip x male thread union" or "MPT x slip union."

Configuration:
- **Male threaded end** → screws into the pump's suction port (replacing your current adapter)
- **Slip end** → glues to the cut end of your existing PVC pipe

Search terms at Home Depot or online: "1.5 inch PVC union slip x MPT" or "1.5 inch PVC union slip x male thread."

## Wait — even simpler option

Actually, there's an even cleaner approach: leave the existing threaded adapter alone and just install a **slip x slip union** in the PVC line a few inches back from the adapter (what we discussed in the last message). The reason: if your existing threaded adapter is sealed well and not leaking, don't mess with it. Threaded plastic-to-plastic connections at pumps are a known leak point — disturbing a working one and re-sealing it introduces a new risk.

So you actually have two viable approaches:

**Approach A: Slip union in the line (originally discussed)**
- Cut the PVC pipe 6-8" from the pump
- Glue a slip x slip union into the cut
- Leave the existing threaded adapter alone
- Pros: Don't disturb existing threaded seal at pump
- Cons: Requires cutting and gluing

**Approach B: Replace the existing threaded adapter with a threaded union**
- Unscrew existing adapter from pump (the PVC pipe stays glued to it — you're removing the whole assembly)
- This means cutting the pipe somewhere to free the adapter, OR breaking the glue joint at the adapter (basically impossible cleanly)
- Realistically you'd still cut the pipe to free the old adapter, then glue the new slip-end of the union to the cut pipe and thread the union into the pump
- Pros: Cleaner finished result, two service points
- Cons: You're cutting AND disturbing the pump threads

## My actual recommendation

Stick with **Approach A** (slip x slip union in the line). Here's why:

- Your existing threaded adapter has been holding for years without issue — don't introduce risk by re-threading
- Approach B requires cutting the pipe anyway (you can't unscrew a glued adapter without breaking the pipe), so you don't save the cut
- Plumber's rule: don't disturb working joints

The threaded union approach is only better if your existing threaded adapter is itself the leak (which is possible — that's actually one of the suspect spots you should check). But if it's not leaking, leave it alone.

## Quick check before you decide

While you're at the pad anyway, put your finger or a tissue right at the threaded adapter-to-pump joint while the pump is running and air is being ingested. If you feel airflow or the tissue gets pulled toward the joint, that adapter or its thread sealant is your leak — and replacing it with a threaded union solves the problem directly. In that case, go with Approach B.

If that joint feels solid (no airflow, no movement), the leak is elsewhere and Approach A is the cleaner solution.

Want to do that 30-second tissue test before committing to which fitting to buy?

### SCOTT (2026-05-12T09:05)
I still have to cut. The PVC is glued to the threaded adaptor. It ain’t going to twist off.

### CLAUDE (2026-05-12T09:06)
 Right, you're correct — I overcomplicated it. The threaded adapter is glued to the pipe, so to remove the adapter you have to cut the pipe anyway. Cutting is happening either way.

Given that, here's the cleaner decision framework:

## If cutting is mandatory, threaded union is the better choice

Since you're cutting regardless:

**Get a 1.5" PVC union with Slip x MPT (male pipe thread).**

Process:
1. Unscrew the old threaded adapter + attached pipe stub from the pump (just turn the whole assembly off the pump threads — the pipe acts as your handle)
2. Cut the pipe a few inches back from the old adapter to free it for disposal (or keep as spare)
3. Thread the new union's male-threaded end into the pump (Teflon tape on threads, 2-3 wraps clockwise)
4. Glue the new union's slip end to the cut pipe end
5. Hand-tighten the union collar

You end up with a **proper serviceable connection at the pump itself**, which is the right way to plumb a pool pump. Every future service is now a 30-second disconnect.

## Why this beats slip-only

A slip union in the middle of the pipe still leaves the pump hard-piped at the threaded adapter — meaning if you ever need to remove the pump entirely (motor swap, full pump replacement), you'd need to cut the pipe again. Putting the union directly at the pump solves that permanently.

## Parts list

- **1.5" PVC Union, Slip x MPT** — ~$8-12. Search "1.5 inch schedule 40 PVC union slip x male thread" at Home Depot
- **Teflon tape** (PTFE thread seal tape) — for the male threads going into the pump. ~$2
- **PVC primer and cement** — as before
- **PVC cutter or hacksaw**

Optional: **Pool-grade thread sealant** (like Rectorseal T+2 or Permatex pool sealant) instead of or in addition to Teflon tape. Teflon alone works fine for most installs, but thread sealant gives a more reliable air-tight seal — which matters specifically for suction-side connections that see vacuum.

## One caution on threading into a plastic pump

When you screw the new union's male threads into the pump body:

- **Hand-tight, then no more than 1-1.5 turns with a wrench.** Plastic pump housings crack from over-tightening. This is one of the most common ways DIYers destroy pump housings.
- Use Teflon tape, not joint compound paste (paste lubricates too much and lets you over-tighten by feel).
- If it leaks slightly when you turn it on, snug a quarter turn more. Don't gorilla it.

Once installed, do your pressure test through the union, and you're set for every future service.

### SCOTT (2026-05-12T09:08)
The existing adapter has been holding for about 24 hours. I installed it when I installed the pump.

### CLAUDE (2026-05-12T09:08)
 Oh — that changes things significantly. Two important implications:

## You did the threaded connection recently

If you installed that threaded adapter 24 hours ago when you put the new motor on, then **the threaded adapter is a top suspect for the air leak**. It's a fresh joint, in the exact location where suction-side leaks commonly originate, on a connection that's notoriously finicky to seal air-tight.

Threaded PVC-to-pump connections need to be sealed correctly for air-tight performance under vacuum. Common ways a fresh install leaks:

- **Not enough Teflon tape** — needs 3-4 wraps minimum, wound clockwise (so it tightens as you thread in)
- **Teflon tape only, no thread sealant paste** — Teflon alone is often marginal for suction-side air-tight seals. Paste sealant (Rectorseal T+2, Permatex Pool Lube and Sealant, or similar pool-rated thread sealant) is what's actually recommended for pump suction threads.
- **Under-tightened** — must be snug, hand-tight plus 1-1.5 turns with strap wrench
- **Over-tightened** — cracked the pump housing threads (look for hairline cracks at the port)
- **Cross-threaded** — adapter didn't seat correctly
- **Old/cheap adapter** — some PVC threaded adapters have molded burrs or imperfect threads

## You don't need a union — you have a serviceable joint already

The threaded adapter IS your service disconnect. You can unscrew the whole suction pipe assembly from the pump at that adapter anytime. That's exactly what a union does. So:

**Skip the union purchase entirely.** No cutting, no gluing.

## What to do instead

**Step 1: Diagnose if the adapter is the leak (5 minutes, free)**

Pump running, air being pulled. Do the shaving cream / soap test specifically at the threaded adapter:
- Spray foam around the seam where the adapter meets the pump body
- Watch for the foam to dimple, get sucked in, or develop a hole
- Also check the glue joint where the PVC pipe meets the adapter

If foam moves at the threaded adapter → that's your leak. Easy fix.

**Step 2: If it IS the threaded adapter, re-do it**

1. Turn off pump and power
2. Unscrew the suction line from the pump at the adapter (the PVC pipe is your handle — turn the whole assembly counterclockwise)
3. Clean the male threads on the adapter with a rag — remove all old Teflon tape and any debris
4. Inspect threads on both the adapter and the pump port for cracks or stripping
5. Re-wrap with **3-4 wraps of Teflon tape, clockwise** (as you look at the threads with the end pointing at you)
6. Add a thin coat of **pool-rated thread sealant paste** over the Teflon tape (belt and suspenders — this is the trick that makes suction threads reliably air-tight)
7. Thread back into pump hand-tight, then snug **1 to 1.5 turns** with a strap wrench or pipe wrench. **Stop there.** Over-tightening cracks plastic pump housings.

**Step 3: Pressure test through the adapter**

Now you have the perfect pressure test access. Skip cutting pipe entirely:

1. Plug the skimmer (expansion plug at the throat)
2. Unscrew the suction pipe from the pump at the adapter
3. Cap the threaded end of the suction pipe with a **1.5" MPT plug fitted with a Schrader valve** (or a pressure test plug kit)
4. Pressurize to 10-15 psi
5. Watch the gauge

You already have a serviceable disconnect. Use it.

## The shopping list shrinks

- **Pool-rated thread sealant paste** (Rectorseal T+2 Blue, ~$8) — for the adapter re-seal
- **1.5" MPT plug with Schrader valve** OR a pressure test kit — for the pressure test
- **Teflon tape** if you don't have any
- Expansion plug for the skimmer (still needed for pressure test)

Total: ~$25-40, no PVC work required.

## My honest take

There's a good chance your air leak is the threaded adapter you just installed. Fresh threaded joints at the pump suction are a top-three failure mode, and the timing fits. Before you do anything else:

1. Soap test the adapter while pump is running
2. If foam moves, you've found it

Want to start there before buying anything?

### SCOTT (2026-05-12T09:09)
I used more than enough teflon tape. And pipe dope. And silicone sealant on the outside.

### CLAUDE (2026-05-12T09:09)
 Belt, suspenders, and a second belt. That's actually a *lot* of sealant, and counterintuitively, it could be part of the problem — but more importantly, it makes the threaded adapter a less likely culprit, not more. Let me reframe.

## What the over-sealing tells me

With Teflon + pipe dope + exterior silicone, that joint is sealed about as thoroughly as a DIY job gets. The silicone on the outside is overkill and won't help with an air leak (silicone doesn't bond well to wet/dirty PVC and doesn't hold against vacuum), but the Teflon + dope underneath is the real seal, and that combination is reliable when applied correctly.

**Caveats where it could still be the leak:**

- **Cross-threading** — if you started the threads at a slight angle, no amount of sealant fixes it. The threads aren't actually engaged on one side.
- **Under-tightened** — if you stopped tightening too early because it felt snug from the Teflon volume, the threads might not be fully seated. Common when there's a lot of tape.
- **Cracked pump port** — if you over-tightened (which is possible with a lot of leverage from the pipe acting as a handle), the plastic pump threads could have a hairline crack.
- **Pipe dope incompatible with the plastic** — some petroleum-based dopes degrade certain plastics over weeks/months, not hours. Probably not your issue at 24 hours.

Still worth doing the soap test on that joint just to rule it out — 5 minutes. But if it really is that well-sealed, your leak is somewhere else.

## So where else?

Let's go back to the candidates with fresh eyes. You have:

- A 24-hour-old pump motor installation (new motor on existing wet end)
- A 24-hour-old threaded adapter at the pump suction (heavily sealed)
- An underground suction line of unknown age
- A 4+ year old skimmer on a vinyl pool
- A history of the same air leak symptom with a different pump last fall

**The "different pump, same symptom last fall" detail is the key clue.** Whatever is wrong was already wrong before this latest install. So the leak is NOT in anything you just touched. It's something pre-existing.

That points away from the new threaded adapter and toward:

1. **The wet end of the pump itself** (which you reused) — lid O-ring, drain plug O-rings, shaft seal, volute gasket, diffuser. The wet end is several years old and has had a motor swap. Anything could be tired.
2. **The underground suction line** — including the glue joints at both ends
3. **The skimmer body or faceplate gasket**

## Highest-yield next move

Given the constraints (cold pool, no swimming, no obvious leaks):

**Run the soap test thoroughly at the pad.** Don't just spot-check. Pump running with air being ingested actively. Spray foam everywhere:

- Pump lid edge (entire perimeter)
- Pump drain plugs (front and bottom)
- The threaded adapter joint
- The glue joint where PVC meets adapter
- Any visible elbows, fittings, valves on the suction side
- Where the suction pipe enters the ground (if accessible)

Watch for **15-30 seconds at each spot** — air leaks can be subtle and the foam dimple develops slowly.

**Pay special attention to the pump wet end.** Specifically:

- Where the volute meets the seal plate (the seam around the middle of the pump body)
- The drain plugs (most missed leak point)
- The shaft seal area (behind the impeller, usually hidden — but if it's leaking, you'll see water dripping when off OR air being sucked when on)

## A different test that doesn't require shaving cream

**Cover the pump lid with plastic wrap and a wet rag.** Pump running, air being pulled. Wrap the entire pump lid and surrounding seal area tightly with plastic wrap, then drape a wet washcloth over it. If the air leak is at the lid, sealing it off should reduce or stop the bubbling at the cell. This is a quick "is it the lid?" test that takes 60 seconds.

Same principle works at other suspect spots — wrap tightly and watch the cell.

## My revised gut feeling

Given the two-pump history, I'd put money on either:

1. **Pump wet end** (lid O-ring, shaft seal, or volute gasket) — same wet end used both times, same symptom both times
2. **Underground suction line** — same line both times, same symptom both times

The fresh threaded adapter is statistically a likely culprit on a new install, but your history rules it out as the *primary* cause. It could be a contributing secondary leak, but probably not the main one.

Want to soap-test the whole pad now? That's the next concrete step.

### SCOTT (2026-05-12T09:10)
How is the soap test going to work?  The pump is sucking not blowing.

### CLAUDE (2026-05-12T09:10)
 You're right to push back on that — I was being sloppy with the explanation. Let me explain why it actually works, and then offer a better test.

## Why the soap test works on a suction-side leak (despite the vacuum)

You're correct that the pump is pulling air *in*, not pushing it out. The mechanism is different from how soap tests work on pressure-side leaks.

On a **pressure-side leak**: air/water blows out through the crack, hits the soap foam, and creates bubbles in the foam. Easy to see.

On a **suction-side leak**: the soap foam itself gets pulled into the crack. What you're watching for:

- The foam **dimples or develops a small pit** as it gets sucked toward the crack
- A **visible hole or stream** appears in the foam where air is entering
- Foam **disappears faster than gravity would explain** at that spot
- Sometimes you'll hear a faint **change in suction sound** as the foam temporarily seals the leak

It's a subtler visual than a pressure-side bubble test. You have to apply the foam thickly and watch carefully — 15-30 seconds per spot, not a quick glance.

## Better suction-side tests

Honestly, the foam test is mediocre for suction leaks. Here are better options:

**Water test (best for pad-side leaks)**

Pour a steady trickle of water over each suspect joint while pump is running and air is being ingested. Where the leak is, water will be pulled in — and **the bubbling at the cell will briefly stop or reduce** because the leak is temporarily sealed by water instead of air.

This is the most reliable test for a suction leak. The cell becomes your leak indicator. You're looking at the cell, not the joint.

Process:
1. Get the pump running until air is actively bubbling at the cell
2. Slowly pour water from a cup over one joint at a time
3. Watch the cell — does bubbling stop or reduce?
4. If yes, that's the leak
5. Move to the next joint

Spots to test:
- Pump lid (pour around the perimeter)
- Each drain plug
- The threaded adapter joint
- The glue joint at the adapter
- Any other visible suction-side fittings

**Smoke test**

Light a stick of incense, a match that you blow out (so it's smoking), or a small smoke pencil. Hold near each suspect joint. Smoke will be visibly pulled into a leak. Works for cracks too small to see.

Caveat: outdoors with any breeze, this is harder. Wait for a calm moment.

**Plastic wrap test**

For the pump lid specifically: wrap the entire lid area tightly with plastic wrap (cling film), pressing it into the seal. Run the pump. If bubbling at the cell reduces or stops, the lid is your leak. If no change, the lid is fine and you can rule it out.

You can do the same with a wet rag pressed against any flat-ish surface — wet rag creates a temporary seal.

## My recommendation

Skip the foam test. Do the **water test** as your primary diagnostic at the pad — it uses the cell itself as the indicator, which is far more reliable than trying to interpret subtle foam movements.

You already know exactly what "air at the cell" looks like (you have the photo). You're watching for that bubbling to change as you pour water over each joint. Binary indicator. Much easier to read.

Start with the pump lid since it's the statistical favorite. Pour water slowly around the perimeter while watching the cell. If bubbling drops — found it. If not, move to drain plugs, then the threaded adapter, then any other joints.

### SCOTT (2026-05-12T09:11)
The shaving cream test sounds better.

### CLAUDE (2026-05-12T09:11)
 Fair — and you're right that shaving cream has one real advantage: it **stays put** so you can watch it for 30+ seconds without continuously pouring. Water runs off in 2 seconds. Foam clings.

## How to read it for a suction leak

Apply a thick blob of shaving cream over the suspect joint — not a thin smear, a real **mound of foam, half an inch thick or more**. Then watch for 30 seconds:

- **A dimple, pit, or hole** developing in the foam → air being pulled in at that spot
- **Foam getting visibly drawn inward** at one point → leak
- **A small "tunnel" forming** through the foam → significant leak
- **Foam stays smooth and undisturbed** → no leak there

The key is **thickness**. Thin foam dries/falls too fast to read clearly. A thick mound gives you a stable foam volume that responds visibly to suction.

## Where to apply, in priority order

1. **Pump lid perimeter** — apply foam all the way around the lid where it meets the pump body. Cover the entire seal line.
2. **Each drain plug** — mound foam over the plug threads
3. **Threaded adapter at pump** — wrap foam around the joint where adapter meets pump
4. **Glue joint at adapter** — foam where the PVC pipe meets the adapter
5. **Any other visible suction-side joints** — elbows, valves, fittings between skimmer and pump

## Tips

- **Pump must be running and actively pulling air** when you apply. The leak only exists under vacuum.
- **Apply generously** — use the cheap stuff, don't be stingy
- **Watch each spot for 30 seconds before moving on** — air leaks can take time to develop visible movement in the foam
- **Work in shade if possible** — direct sun dries the foam fast and creates false "dimples"
- **Look from multiple angles** — a dimple might only be visible from one side

If you find the leak, the foam will tell you exactly where to focus the fix. If you do the whole pad and find nothing, the leak is either underground or at the skimmer, and we move to the pressure test.

Go for it.

### SCOTT (2026-05-12T09:12)
Since was happening with the old pump, my gut tells me is at the skimmer basket. My money is on the face plate.

### CLAUDE (2026-05-12T09:13)
 Your gut is probably right, and your reasoning is solid. The two-pump history is the strongest single clue you have, and it points away from anything on the pad.

## Why the faceplate is a good bet

On a 4+ year old vinyl pool with no main drain:

- The skimmer carries 100% of the suction load — every leak point in the skimmer body is under constant vacuum
- The faceplate gasket sits between the liner and the skimmer body, compressed by 8-10 stainless screws — this gasket compresses, hardens, and eventually fails
- Ground settling, freeze cycles, and liner movement all stress that gasket over years
- The leak path: air enters between the deck/coping and the liner edge above the skimmer, travels behind the liner, and gets pulled in through the failed gasket into the skimmer body

This produces exactly your symptom: small, vacuum-only leak that resets on pump-off (line refills with water) and degrades during run (gradually pulls more air as the leak path stabilizes under vacuum).

## A few skimmer culprits to keep in mind, not just the faceplate

When you tackle this, the faceplate gasket is the most likely, but check these while you're in there:

1. **Faceplate gasket** (between liner and skimmer body) — primary suspect
2. **Skimmer body cracks** — especially at the throat, where the suction pipe glues in. The plastic gets stressed and can develop hairline cracks. Inspect the entire skimmer body interior with a flashlight.
3. **The glue joint where the suction pipe meets the skimmer** — sometimes accessible from inside the skimmer, sometimes only from underneath
4. **The skimmer-to-deck seal** — if the skimmer has shifted relative to the deck, gaps can develop. Less common but possible.

When you have the faceplate off, inspect the visible interior of the skimmer body carefully before reinstalling. If you see cracks, the fix is different (epoxy or skimmer replacement, not just a gasket).

## Game plan

Since you're confident enough to commit:

**Phase 1: Confirm before draining**

Even if you're 80% sure, do **one** quick pad-side check first — 10 minutes max. Shaving cream the pump lid and the threaded adapter just to rule them out. If you find nothing at the pad, your skimmer hypothesis is essentially confirmed by elimination, and the drain-and-replace is justified.

**Phase 2: Drain and inspect**

- Lower the water to ~6 inches below the bottom of the skimmer opening
- Pull the faceplate (8-10 stainless screws around the perimeter, hand screwdriver only)
- Inspect: gasket condition, butyl sealant behind it, liner integrity around the opening, skimmer body for cracks
- Photograph what you find before doing anything else — useful for parts identification and for me to help you assess

**Phase 3: Parts identification**

Before you drain, try to identify your skimmer brand/model. Look for molded branding inside the skimmer body (often on the bottom or side walls). Common ones on vinyl pools:
- Hayward SP1084 / SP1085
- Pentair Admiral / Admiral S15
- Aquador
- Waterway Renegade

Knowing the brand lets you order the correct faceplate gasket in advance. Generic gaskets work for many but the screw spacing and shape vary. Generic "universal" gaskets are also a thing.

**Phase 4: The repair itself**

I'll walk you through it when you're ready. The job:
- Remove old gasket and butyl sealant residue (acetone or denatured alcohol)
- Apply new butyl sealant tape to skimmer body face
- Install new gasket
- Reinstall faceplate, star-pattern tightening, snug not gorilla
- Refill, run pump, test

## Shopping list (order ahead so you have parts on hand)

- **Faceplate gasket** for your specific skimmer — $5-15 (identify model first)
- **Butyl sealant tape** for pool skimmers (Pool Skimmer Butyl Tape, Pentair 808-0050, or generic equivalent) — $10-15
- **Replacement stainless faceplate screws** (#10 x 1" or similar — measure your existing ones first) — $5-10 for a set
- **Submersible utility pump** if you don't have one for draining — $80-120

## Before you commit to draining

Two reality checks:

1. **Run the pad-side shaving cream test first.** 10 minutes. If you find a leak at the pump lid or drain plug, you've saved yourself a partial drain and a faceplate job. Worth doing even if you're 80% sure it's the skimmer.

2. **Identify your skimmer brand before draining.** Get the parts on hand. Nothing worse than draining the pool, pulling the faceplate, and then realizing you need to wait 3 days for shipping while the liner sits exposed.

Once those two boxes are checked, commit to the skimmer fix.

What's the skimmer brand? Look inside it next time you're at the pool.

### SCOTT (2026-05-12T09:16)
Or the second most likely culprit, and harder to diagnose. From the pump going backwards from water flow at the intake, the PVC goes straight a few inches and then does a 90 into the ground. When the old pump was coming out l could have pushed on that PVC and cracked the joint below ground where it had to do another 90 to point towards the pool. The 90 about ground closest to the pump has already been replaced by me.

### CLAUDE (2026-05-12T09:17)
 That's a really plausible scenario, and it actually fits the evidence as well as the skimmer theory — maybe better. Let me think through what you just described.

## What you're describing

Your suction line geometry:

```
PUMP → straight pipe → 90° elbow (above ground, you've replaced this one) 
     → vertical pipe down → 90° elbow (below ground) 
     → horizontal pipe → skimmer
```

The below-ground 90° is the suspect. When you wrestled the old pump out, you could have stressed the vertical pipe enough to crack the buried elbow at its glue joint — invisible from the surface, sitting under ground where you can't inspect it.

## Why this is a strong candidate

1. **Mechanical stress history.** Pump removal is exactly the kind of event that loads a buried elbow. PVC is rigid, glue joints are the weakest point, and a buried elbow has nowhere to flex. A few pounds of leverage at the pump translates to significant torque at the underground fitting.

2. **The geometry concentrates stress at one point.** A buried 90° elbow taking the full bending moment from the above-ground pipe is the textbook location for stress-induced glue joint failure.

3. **Timing fits.** Old pump came out → fall → pool sat closed → new motor in → first time running under sustained vacuum reveals the leak. The crack might have been there since the old pump removal but only became symptomatic when there was a working pump pulling on it.

4. **The two-pump history fits BOTH ways.** Skimmer theory says the leak was there before the pump came out. Buried elbow theory says the leak was created BY the pump coming out. The 3HP pump struggling to prime last fall is consistent with either — if the elbow was already partially cracked, the 3HP couldn't overcome it. But the 3HP attempt itself involved disconnecting and reconnecting the suction line, which would have stressed that elbow too.

5. **Symptom pattern fits perfectly.** A hairline crack at a glue joint behaves exactly like what you describe: holds water under static pressure (when pump is off, line is full and at slight positive pressure from pool head), leaks air under vacuum (when pump runs, line goes negative). Crack opens slightly under vacuum, ingests air progressively.

## Why this is "harder to diagnose"

You're right that it's harder than the faceplate. You can't see it, can't soap-test it, can't dye-test it directly. Your options are:

1. **Pressure test** — this is the diagnostic that catches it definitively. If the line doesn't hold pressure but you can rule out the skimmer and the pad, the leak is buried.
2. **Excavate** — dig down to the elbow and inspect. Last resort.
3. **Process of elimination** — rule out everything else, conclude by inference.

## Updated diagnostic priority

Given this new information, here's how I'd reorder:

**Priority 1: Quick pad-side check (10 min, free)**
Shaving cream test the pump lid, drain plugs, threaded adapter, and the above-ground elbow you replaced. Rule out the easy stuff.

**Priority 2: Pressure test (an hour, ~$30 in parts)**
This is now even more important than the faceplate inspection. The pressure test will tell you:
- Pad-side leak (gauge drops, you hear/find it at the pad)
- Skimmer-side leak (gauge drops, you find it at or near the skimmer when looking)
- **Buried line leak** (gauge drops, you can't find it anywhere visible — points to the underground elbow)
- No line leak (gauge holds — leak is at the pump itself somewhere you missed)

You can do this through the threaded adapter you already have. Unscrew the suction pipe from the pump, install a 1.5" MPT plug with Schrader valve into the threaded end of the pipe, plug the skimmer, pressurize.

**Priority 3: Skimmer inspection or excavation**
Based on pressure test results. If gauge holds, no need to drain or dig. If gauge drops and you can localize the leak to the skimmer area (audible, visible at skimmer), do the faceplate. If gauge drops and you can't localize, it's the buried elbow.

## Hard truth about a buried elbow leak

If it turns out to be the underground 90°, you have three options:

1. **Excavate and repair.** Dig down, expose the elbow, cut it out, replace with new fitting, reglue. Probably 2-4 feet of digging depending on burial depth. Not fun but not terrible.

2. **Reroute above ground.** Cut the line above ground, run new pipe along the surface (or just under the deck) to a new entry point at the skimmer. Bypasses the buried section entirely. Cosmetically ugly but bulletproof and avoids excavation.

3. **Slip-line or pipe repair.** Various epoxy/slip-line repair kits exist for buried PVC. Mixed results, especially at fittings (vs straight pipe runs). Generally not recommended for elbow failures.

If it's the buried elbow, option 1 is the right answer if you can access it, option 2 if you can't.

## What I'd do in your shoes

The buried elbow theory and the faceplate theory are both plausible, both about equally likely, and **the pressure test discriminates between them cleanly**. Don't drain the pool yet. Don't dig yet.

**Order the pressure test parts today**:
- 1.5" expansion plug for the skimmer (~$10)
- 1.5" MPT plug with Schrader valve OR a complete pool pressure test kit (~$25-40)
- Small pressure gauge if not in the kit (~$10)

Run the test. The gauge will tell you which direction to go next.

This is exactly the kind of diagnostic where the $30 of parts pays for itself many times over by preventing wasted effort on the wrong fix.

### SCOTT (2026-05-12T09:18)
How deep you reckon that joint it. May not be too deep at all.

### CLAUDE (2026-05-12T09:19)
 Good instinct to think about this before committing to the pressure test — if the elbow is shallow, the cost-benefit of just digging exploratory shifts in your favor.

## Typical burial depth for residential pool suction lines

For above-ground-to-skimmer plumbing on a vinyl pool in Georgia (no frost line concerns to speak of), pool installers typically bury the line **12-18 inches deep**, sometimes less. A few factors that influence depth:

1. **Frost line in Georgia** — essentially nonexistent. Hogansville is roughly USDA zone 8a, frost line is maybe 4-5 inches. No code-driven reason to go deep.
2. **Just below the deck/coping** — pool builders bury the line just deep enough to clear the deck base and the dirt fill, then run it horizontally to the skimmer at that depth. Often 8-12 inches below grade once they're past the deck edge.
3. **Equipment pad transition** — at your pad, the line comes up out of the ground and turns 90° to enter the pump. That vertical pipe might only have 6-12 inches of buried length before the elbow turns horizontal.

## Your specific case

You said the geometry is:
- Pump (above ground)
- Short horizontal pipe to a 90° elbow (above ground, replaced)
- Vertical pipe going down into the ground
- 90° elbow underground that turns the line horizontal toward the skimmer

That underground 90° is probably **at the bottom of the vertical section** — i.e., the depth of the bottom of the vertical pipe. Likely **8-18 inches below grade**.

The good news: that's shovel depth, not backhoe depth. A 30-minute hand dig in most cases.

## How to estimate without digging

Look at:

1. **Where does the vertical pipe disappear into the ground?** If it goes straight down from the elbow you replaced, the buried elbow is directly below that entry point.
2. **What's the distance from pump pad to skimmer wall?** The buried run is roughly that distance, at a consistent depth.
3. **Any landscape clues?** Sometimes you can see a slight depression along the pipe path, or grass grows differently above buried lines. Less common but worth a look.
4. **The vertical pipe length above grade.** If you have, say, 18 inches of vertical pipe between the pump and where it enters the ground, the elbow below is probably another 6-12 inches down.

## The "exploratory dig" option

Here's a legitimate alternative to the pressure test:

**Dig a small exploratory hole** right where the vertical pipe enters the ground. You're not committing to a repair, you're just exposing the elbow to inspect it visually.

- Use a shovel, work carefully near the pipe (you don't want to punch the shovel through it)
- Excavate a 12" x 12" hole following the vertical pipe down
- Stop when you expose the elbow
- Inspect for cracks, especially at the glue joints where pipe enters the elbow

If you find a crack → you've diagnosed and you're already partially excavated for the repair.
If you find a clean elbow → not the leak, fill the hole back, move to faceplate or other diagnostics.

**Total time: 30-60 minutes. Total cost: free.**

This is arguably faster and cheaper than the pressure test, and gives you a visual answer. The downside: if the elbow is fine, you've done physical labor for no diagnostic information.

## My honest take

If you're willing to dig 30 minutes on a hunch:

**Just dig.** Your gut said skimmer first, but now your gut is saying buried elbow. Both are plausible. Digging takes the elbow off the table definitively in under an hour, and if you find the crack you're already halfway to fixing it.

Vs the pressure test: $30 in parts you may not use again, plus the time to acquire and run the test, and you still have to dig if the test points to the buried elbow.

**Caveat: do the pad-side shaving cream test first** — it's 10 minutes and catches the easy case. If that's clean, then dig.

## If you do dig and find the crack

Repair process:
1. Expose 4-6 inches of clean pipe on both sides of the elbow
2. Cut out the cracked elbow with a hacksaw or PVC cutter (one cut on each side)
3. Dry-fit a new 90° elbow + two short pipe stubs + two couplings to bridge the gap. You'll need a "slip-slip-slip-slip" connection sequence: cut pipe → coupling → short stub → new elbow → short stub → coupling → cut pipe.
4. Or use a single repair coupling like a SharkBite/compression fitting if you don't want to glue underground in tight quarters
5. Glue everything with PVC primer + cement (or use compression fittings)
6. Let cure for 2+ hours before pressurizing
7. Backfill once tested

Compression repair couplings (sometimes called "no-glue couplings" or "Dresser couplings") are particularly useful underground where it's hard to get a clean glue joint. About $15-25 each. Worth considering if the work area is cramped.

Want to dig before doing anything else?

### SCOTT (2026-05-12T09:21)
And with that skimmer plug if it is the joint I don’t have to drain pool to replace it.

### CLAUDE (2026-05-12T09:21)
 Exactly right — and that's actually a significant practical advantage of the buried elbow scenario versus the faceplate scenario.

## With the skimmer plugged

The expansion plug at the skimmer throat seals off the pool water from the suction line. Once that plug is in:

- The suction line is **isolated from the pool** — you can cut, repair, and reglue without pool water flooding the work area
- The pool **stays full** — no draining required
- You can take your time on the repair — glue cure, dry fit, refit — without water pressure pushing into the line

This is the same principle as winterizing. You're using the skimmer plug as a temporary isolation valve.

## Practical workflow if it's the buried elbow

1. **Plug the skimmer** (expansion plug at the throat, tightened firmly)
2. **Disconnect the suction line at the pump** (unscrew at your threaded adapter)
3. **Dig down to expose the elbow** — line is now empty of pressure, just gravity-drained
4. **Open the line** — any residual water in the pipe drains out at the dig site. That's a small mess but localized.
5. **Cut out the cracked elbow, replace it** — work at your own pace
6. **Let glue cure 2+ hours minimum** (overnight ideal)
7. **Reconnect at the pump**
8. **Remove skimmer plug**
9. **Prime and start pump**

The pool sits full and stable the whole time. Skimmer doesn't function during the repair (the only suction point is plugged), but that's fine for a day.

## One thing to watch

When you remove the skimmer plug after the repair, the suction line will be full of air (from being open during repair). The pump won't prime easily on a fully air-filled line.

**Pre-fill the suction line before removing the plug:**
1. With skimmer still plugged and pump still disconnected at the threaded adapter, fill the suction pipe from the pump end with a garden hose. Water flows down toward the buried elbow and fills the line.
2. When water starts overflowing at the pump end, the line is full
