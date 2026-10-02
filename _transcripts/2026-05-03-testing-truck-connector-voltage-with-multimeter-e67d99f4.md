# Testing truck connector voltage with multimeter
Date: 2026-05-03
Conversation: e67d99f4-5280-49ce-8da4-e53a52711b9c
Domain: skip

## Summary
**Conversation overview**

The person was troubleshooting a non-functional dog box fan on a 2018 Chevy Silverado 2500HD diesel (Duramax). The conversation was a step-by-step electrical diagnostic session using a multimeter. The person had an Ideal brand auto-ranging multimeter and was comfortable following technical instructions. Key domain terminology used throughout included: DC volts (V⎓), continuity testing, relay terminals (30, 85, 86, 87), CHMSL (center high-mount stop light), inline fuse holder, upfitter circuits, ISO relay pinout, and T-tap wiring. The fan was installed as aftermarket equipment on a dog box mounted in the truck bed, wired with a sealed illuminated toggle switch in the cab and a 40A relay (HTT7101-12V) in the bed area.

The diagnostic process began with testing for voltage at the fan's 2-pin connector (reading 0V), then moved upstream through the underhood fuse box, where Claude incorrectly identified fuse #43 ENG (15A) as the likely culprit based on discolored blades. The person correctly challenged this when the "bad" fuse tested fine in another slot (powering the windshield washer). A dead third brake light (CHMSL) was investigated as a possible related failure, but fuse #38 tested good, ruling out a shared circuit. The person then physically traced the fan wire from the truck bed connector back through the harness, discovering a 40A relay the circuit ran through. While identifying relay terminals using the diagram on the relay body, the person located a connector on the switch trigger wire showing heavy green corrosion on the white wire, with the blue and black wires appearing intact. This corroded connector was identified as the root cause — preventing the cab switch from receiving power, which meant the relay never triggered and the fan stayed dead.

Claude made two notable errors that the person corrected: (1) misidentifying frayed wire ends in an early photo that turned out to be loom fuzz or a zip tie tail, and (2) prematurely concluding fuse #43 was blown based on discolored blades without confirming it. The person also clarified that the dirty 2-pin connector photographed early in the session was the truck-side connector (not the fan side), and that the toggle switch in the cab was fully sealed with no accessible wiring. The resolution reached was to splice only the corroded white wire using an adhesive-lined heat-shrink butt connector or solder plus heat shrink, verify clean copper on the blue and black wires by stripping them back slightly, and apply dielectric grease to protect remaining connections. The CHMSL failure was assessed as likely a separate, unrelated issue — probably a burned-out bulb.

### SCOTT (2026-05-03T19:27)
I am trying to determine if this plug is getting juice from my truck. Which setting on my multi meter for this?
[File uploaded: IMG_6548.jpeg]
[File uploaded: IMG_6547.jpeg]

### CLAUDE (2026-05-03T19:28)
 That looks like a 2-pin connector on your Duramax — likely the GPCM harness side or a similar 12V feed. To check if it's getting juice, here's what you do:

**Setting:** Turn the dial to **V⎓** (DC Volts) — that's the V with the straight line and dashes above it on the left side of your dial. Your meter has auto-ranging, so you don't need to pick a range.

**Lead placement:**
- Red lead → **VΩ** jack (right side, where it already is)
- Black lead → **COM** jack (middle)

**How to test:**
1. Key on, engine off (KOEO) — turn the ignition to "run" but don't crank
2. Touch the **black probe to a good ground** (battery negative, or bare metal on the engine/frame)
3. Touch the **red probe** into one of the two female sockets on the connector
4. Read the voltage, then repeat on the other socket

**What you're looking for:**
- ~12V (battery voltage) on the hot pin = circuit is live
- 0V on both = no power getting there (broken wire, blown fuse, bad relay, or PCM not commanding it)
- One pin hot, one pin not = normal for a power + signal/ground setup

**Tip:** If this is the GPCM connector, the glow plug controller only gets commanded power for a short window after key-on (and only when it's cold enough). On a warm Georgia day the PCM may not energize it at all, or only for a second or two. If you want to catch it, use the **HOLD** button or just watch closely right when you turn the key. Cold-soaking the truck overnight gives the cleanest test.

Want me to walk through interpreting the readings once you take them?

### SCOTT (2026-05-03T19:34)
This is a fan for my dog box. Got 0 volts.

### CLAUDE (2026-05-03T19:35)
 Ah — totally different situation then. Dog box fan, 12V accessory circuit. Zero volts means power isn't making it to the connector. Here's how to hunt it down:

**Work backward from the connector toward the source:**

1. **Confirm your meter and ground are good.** Touch red probe to battery positive, black to battery negative — you should see ~12.6V. If yes, meter and leads are fine.

2. **Is the fan on a switch?** Make sure whatever controls it (toggle, ignition-switched, etc.) is actually on when you test. Sounds dumb but it's the #1 cause.

3. **Check the fuse.** Pull the fuse for that circuit and either:
   - Visually inspect (blown filament)
   - Or with the fuse in place and circuit powered, touch red probe to each of the two little metal tabs on top of the fuse — both should read ~12V. One hot, one dead = blown fuse.

4. **Check at the power source.** If it's wired to a battery, accessory block, or trailer plug — test voltage right at that connection point. No voltage there = problem is upstream (loose ring terminal, corroded connection, bad ground on the source side).

5. **Walk the wire.** If power is good at the source but dead at the connector, you've got a break somewhere in between. Common failure points:
   - Where the harness flexes (tailgate area, hinges)
   - Anywhere it could get pinched, chewed, or chafed
   - Inline connectors or splices

6. **Don't forget the ground side.** A "12V circuit" needs both. If the fan has its own ground wire back to chassis, check that ring terminal — corroded or loose grounds will also kill the circuit, but usually you'd still see 12V at the connector with key on. Worth eyeballing anyway.

**Quick sanity check:** Are you testing with the black probe on a *known good ground* (battery negative or clean bare metal), not on the connector body or the other pin? If you tested pin-to-pin on the connector itself with no load, you'd read 0V even on a live circuit because there's no return path.

What's the power source for this fan — wired to the battery directly, an accessory fuse panel, or running off the trailer plug?

### SCOTT (2026-05-03T19:41)
Runs to that plug.
[File uploaded: IMG_6549.jpeg]

### CLAUDE (2026-05-03T19:41)
 OK, that picture tells the story. I can see frayed wire ends sticking out of the loom on the left side — looks like the harness got cut, chewed, or pulled apart and someone wrapped it back up but the conductors aren't connected to anything. That's almost certainly your 0V.

**What I'm seeing:**
- Frayed/exposed copper strands poking out of the split loom
- A small box/relay or splice point in the middle
- Multiple wires routed through that bundle, then your fan harness branches off

**Next moves:**

1. **Pull back the loom and tape carefully** at the frayed spot. Find out if those loose wire ends are *supposed* to connect to something (maybe a previous trailer plug or accessory that got removed) or if they're the actual fan feed that got severed.

2. **Trace the fan wire backward from the connector you tested.** Follow it physically until it either:
   - Disappears into that bundle (likely — and probably terminates at those frayed ends)
   - Connects to a fuse tap, relay, or battery somewhere

3. **Once you find the source end**, test voltage there with the meter. Same setting (V⎓), red probe on the wire, black on a clean ground.
   - 12V at the source but 0V at the connector = break in between (probably right at those frayed strands)
   - 0V at the source too = problem is further upstream (fuse, switch, relay, or whoever wired this never finished the job)

4. **Check that little box/relay** in the middle of the photo. If the fan is supposed to run through it, test for power on both sides — input pin should have 12V, output pin should have 12V when the relay is triggered. A dead relay or one that lost its trigger signal will kill the circuit.

**Honest read:** This looks like aftermarket wiring (dog box fan isn't factory) and it's showing its age. Frayed strands like that are how shorts and fires start. Whatever you find, when you fix it, do it right — solder + heat shrink, or a proper crimp connector, and re-loom it. Don't just twist and tape.

Can you get a closer shot of those frayed wire ends and the little metal box? I want to see if there's a connector that came apart vs. wires that were just cut.

### SCOTT (2026-05-03T19:42)
Not frayed wires there.

### CLAUDE (2026-05-03T19:42)
 Fair enough — that's just loom fuzz or a zip tie tail then, not exposed copper. My bad on the read.

So back to the hunt. You've got 0V at the fan connector. The wiring runs into that bundle and that little box visible in the photo. Couple of questions to narrow it down:

1. **What is that small metal box?** Looks like it could be a relay, an inline fuse holder, or a splice block. If you can pop it open or get a closer look, that's a likely failure point.

2. **How is this fan supposed to be powered?** Switched by a toggle in the cab? Always-hot from the battery? Tied into the trailer harness? Ignition-switched?

3. **Has it ever worked, or is this a new install you're commissioning?**

**Regardless, the troubleshooting flow is the same — work from the connector back to the source:**

- Test voltage at the **fan connector** (already done — 0V)
- Test voltage at the **output side of that little box** (relay/fuse/splice)
- Test voltage at the **input side of that little box**
- Test voltage at the **power source** (battery terminal, fuse panel tap, wherever it originates)

Wherever you go from 0V to 12V is the spot where your problem lives. If it's 0V all the way back to the source, then the source itself is the issue — blown fuse, bad switch, dead relay, or never properly connected.

What is that little box, and where does the wire ultimately originate?

### SCOTT (2026-05-03T19:42)
Always hot with a switch in the cab. I think is probably a fuse.

### CLAUDE (2026-05-03T19:43)
 Good — that narrows it way down. Inline fuse holder is the most likely culprit on an always-hot accessory circuit, especially one that's been bouncing around under a truck for years.

**Order of attack:**

1. **Pop open that inline fuse holder.** Most are either a screw-apart cylinder or a pull-apart waterproof type. Pull the fuse and look at it — blown filament is usually visible. While you're in there, check for corrosion on the fuse clips and the fuse blades. Green/white crusty buildup will kill continuity even with a good fuse.

2. **Test the fuse with your meter.** Switch the dial to the **continuity setting** — that's the spot with the speaker/sound wave icon (looks like `))` ) on your Ideal meter, usually shares a position with the diode/ohm symbol on the lower left. Touch the probes to each end of the fuse. Good fuse = beep + reads near 0. Bad fuse = no beep, reads OL or "1".

3. **If the fuse is good**, put it back in and test voltage:
   - **Input side of the holder** (battery side) — should read 12V always. No 12V here = problem is between here and the battery (broken wire, loose ring terminal at the battery, corroded connection).
   - **Output side of the holder** (load side) — should also read 12V with a good fuse. 12V in, 0V out = bad fuse or corroded clips.

4. **If 12V is making it past the fuse holder**, then with the cab switch ON, you should see 12V at the fan connector. If you don't, the break is between the fuse and the connector — either at the switch, in the wiring run, or at a connection point you haven't found yet.

5. **Don't skip the switch itself.** Cab switches fail too. Test voltage on both sides of the switch with it in the ON position — should be 12V on both terminals. 12V on one side, 0V on the other = bad switch.

**One more thing:** Make sure the fan's ground wire is actually grounded. An always-hot + switched setup needs both legs intact. If the ground ring terminal fell off the chassis or corroded through, the circuit is dead even with perfect 12V supply. Easy to check — pull the ground end and look at it.

Get the fuse out and test it first. That's the 80% answer.

### SCOTT (2026-05-03T19:43)
I don’t think that is an inline fuse. I think is just a harness connector.

### CLAUDE (2026-05-03T19:44)
 Got it — so that little box is just a connector/junction where two harness sections plug together. That's actually useful info because connectors are a very common failure point, especially under-truck where they get road spray, mud, and vibration.

**Test the connector itself:**

1. **Unplug the two halves.** Look inside both sides for:
   - Green/white corrosion on the pins
   - Pushed-back pins (one side won't seat properly)
   - Water, mud, or crud inside
   - Bent or broken pins

2. **With it unplugged and switch ON in the cab**, probe the **supply side** (the half coming from the battery/switch direction):
   - Red probe into the pin socket, black to ground
   - Should read 12V on the hot pin

3. **Based on what you find:**
   - **12V at the supply side of this connector** = power is making it this far. Problem is downstream — between here and the fan. Reconnect, then test at the next point downstream.
   - **0V at the supply side** = problem is upstream. Keep working back toward the battery/switch.

**Where to test next if 0V here:**

Work your way back toward the cab. Logical test points:
- **At the cab switch** — both terminals with switch ON should read 12V. If only the input side is hot, the switch is bad or the output wire is broken.
- **At the battery / fuse tap** where the always-hot feed originates — should always read 12V. No voltage here means a blown inline fuse you haven't found yet, a disconnected ring terminal, or a broken wire between the battery and this point.

**Most likely culprits in order:**
1. Corrosion inside that under-truck connector (very common)
2. Broken wire where the harness flexes or got snagged
3. Bad cab switch
4. Inline fuse you haven't located yet (there almost certainly is one somewhere near the battery — if there isn't, that's a fire hazard you'll want to fix)

Pop that connector apart and tell me what it looks like inside.

### SCOTT (2026-05-03T19:44)
Where’s the fuses on a 2018 Chevy 2500hd diesel. I will check there first.

### CLAUDE (2026-05-03T19:44)
 Good call — start at the source. A 2018 Silverado 2500HD Duramax has fuses in three main spots:

Your 2018 2500HD has **three fuse boxes**:

**1. Underhood fuse box** — driver's side of the engine compartment, big black box near the battery. This is where most accessory/aftermarket taps end up. Pop the lid; the legend is usually printed on the inside.

**2. Driver's side instrument panel** — end of the dash on the driver's side, behind a removable cover. Open the driver's door and look at the edge of the dash.

**3. Passenger's side instrument panel** — same deal on the passenger end of the dash, behind a cover.

**For your dog box fan**, start at the **underhood box**. Aftermarket installers almost always tap into a constant-hot circuit there because:
- It's close to the battery
- Easy to run a wire through the firewall or down to the frame
- Some years/trims have empty "add-a-fuse" slots designed for accessories

**What to look for:**
- Any fuse that doesn't match the factory legend (added by whoever wired the fan)
- An "add-a-circuit" piggyback adapter sticking out of a slot
- A wire tapped directly to a fuse terminal
- Any fuse that looks aftermarket or out of place

**Test each suspect fuse the same way:**
- Multimeter on V⎓ (DC volts)
- Black probe to a clean ground (battery negative or bare metal)
- Red probe to each of the two little metal tabs on top of the fuse (you don't have to pull it)
- Both tabs should read 12V on a good always-hot fuse. One hot, one dead = blown.

Also worth checking: **is there a wire running from the battery directly?** Some installers skip the fuse box entirely and just put a ring terminal on the battery positive with an inline fuse a few inches down the wire. Look at your battery posts for any aftermarket ring terminals and follow that wire — your inline fuse may be hiding right there in the engine bay.

### SCOTT (2026-05-03T19:45)
Which one you think?
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T19:45)
 Perfect — you've got the underhood box open and that legend is gold. Good news: this truck has **factory upfitter circuits** specifically designed for accessories like your dog box fan. Whoever installed it almost certainly tapped one of these.

**Look at these "UPFTR" fuses on your legend:**

- **#22 UPFTR SW1 (5A)** — switch input
- **#26 UPFTR SW2 (5A)** — switch input
- **#27 UPFTR SW3 (5A)** — switch input
- **#31 UPFTR SW4 (5A)** — switch input
- **#37 UPFTR 1 (30A)**
- **#23 UPFTR 2 (30A)**
- **#30 UPFTR 3 (30A)**
- **#32 UPFTR 4 (30A)**

The 30A fuses (#37, 23, 30, 32) are the **load side** — that's where a fan would actually pull power from. A dog box fan likely runs through one of these.

**My bet:** Check **#23, #30, #32, and #37** first — pull each one, look at it. A 30A fuse blade is big and easy to inspect visually. Or test in place with your meter on V⎓: probe both little tabs on top of the fuse with key on (or just on, since these may be hot all the time depending on configuration). Both tabs hot = good. One hot, one dead = blown.

**Important caveat:** The factory upfitter circuits on a 2018 2500HD are typically **switched by the cab-mounted aux switches** on the dash (those little rocker switches near the headlight knob if your truck has them). If your dog box fan was wired into one of those factory switch positions, the cab switch I assumed earlier might actually be a *factory* upfitter switch, not an aftermarket toggle. Worth knowing because the upfitter switches themselves can fail.

**Order of attack:**
1. Pull and inspect fuses **23, 30, 32, 37** (the four 30A UPFTR fuses)
2. Also check **22, 26, 27, 31** (the 5A switch-side fuses) — if one of those is blown, the relay won't trigger and the 30A side stays cold
3. If all fuses look good, test for 12V on the load side with the cab switch ON

**Also worth a glance:** Is your dash switch a factory rocker labeled AUX1/AUX2/etc., or an aftermarket toggle someone drilled in? That tells us whether to trust the factory upfitter circuit theory or go hunting for an aftermarket tap.

### SCOTT (2026-05-03T19:46)
That what they installed with the dog box and fan.
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T19:47)
 OK that confirms it — that's a classic aftermarket toggle with red/green LED indicators, definitely not a factory upfitter switch. So forget the UPFTR fuses; the dog box installer wired this independently.

**Important clue from that switch:** Is the **green LED lighting up** when you flip it to ON? That tells us a lot:

- **Green LED ON** = the switch is getting power and passing it through. Problem is downstream of the switch (broken wire between switch and fan, or bad ground at the fan).
- **Red LED only / no LED** = switch isn't getting power, or the switch itself is bad. Problem is upstream (between battery and switch).
- **No LEDs at all** = switch is dead, no power reaching it, or the LED itself failed (rare).

**Where the power tap likely is:**

Aftermarket installers on a 2018 2500HD typically do one of these:
1. **Ring terminal directly on the battery positive** with an inline fuse a few inches down the wire (most common, quickest install)
2. **Add-a-circuit piggyback** on an existing fuse in the underhood box
3. **Tap on the underhood "stud"** — there's a power distribution stud near the underhood fuse box on these trucks

**Next step — open the hood and look at the battery positive terminal.** You're looking for any aftermarket ring terminals stacked on the post (anything that's not the factory cable). Follow that wire — within 6–12 inches you should find an inline fuse holder. That's almost certainly your culprit.

While you're at it, check both batteries (the 2500HD diesel has two). The dog box could be tapped to either one.

**Tell me:**
1. Does the green LED come on when you flip the switch?
2. Any aftermarket ring terminals on the battery posts?

### SCOTT (2026-05-03T19:49)
No lights on it at all.

### CLAUDE (2026-05-03T19:49)
 That's the answer right there — **no power reaching the switch.** Problem is upstream of the cab, between the battery and that toggle.

**Now go straight to the battery.** Open the hood and look at the positive terminals on both batteries. You're hunting for:

- An aftermarket ring terminal stacked on the positive post (anything that isn't a factory GM cable)
- A wire leading away from that ring terminal toward the firewall
- An **inline fuse holder** within the first 6–12 inches of that wire — it'll be a small cylindrical or rectangular black plastic housing spliced into the wire

**Most likely failure points, in order:**

1. **Blown inline fuse** at the battery — fan motor surge, short somewhere, or just age. Pull it and inspect/test.
2. **Loose or corroded ring terminal** on the battery post — wiggle it. If it moves or has green/white crust under it, clean and re-torque.
3. **Ring terminal fell off entirely** — sometimes the nut backs off and the whole ring drops down behind the battery. Look for a wire dangling with nothing on the end.
4. **Wire chafed through** somewhere between the battery and the firewall pass-through. Less common but possible.

**Test sequence once you find the tap:**

- Probe the **battery side** of the inline fuse → should read 12V always. No 12V here = bad ring terminal connection at battery.
- Probe the **load side** of the inline fuse → should also read 12V. 12V in, 0V out = blown fuse.
- If both sides of the fuse are hot, the break is further down the wire toward the cab switch.

**If you don't find an aftermarket tap on either battery**, then it was wired through the underhood fuse box with an add-a-circuit. In that case, look for any fuse with an extra wire coming off it that doesn't match the factory harness.

Go check the batteries and report back what you find.

### SCOTT (2026-05-03T19:51)
Nothing at the batteries. I think they wired into an exiting line. This tail light over the back window also doesn’t work. Think may be related?
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T19:51)
 Yeah, that could absolutely be related — and it's actually a really useful clue.

**Why it's plausible:**

The CHMSL (center high-mount stop light) circuit runs from the cab fuse box, up the headliner or B/C-pillar, through the rear cab seal, and out to that light. That's a constant-or-switched 12V wire that already passes through exactly the area where someone installing a dog box fan would be looking for power. A lazy installer might have:

1. **T-tapped into the CHMSL wire** for switched/running power
2. **Tapped the CHMSL ground** and overloaded it
3. **Damaged the CHMSL harness** while running their fan wire through the same grommet or seal
4. **Tapped a nearby always-hot wire** in the same bundle and chafed/shorted the CHMSL line in the process

If both circuits went dead together, that points to a shared fuse, shared ground, or physical damage to a shared bundle.

**But — important caveat:**

The CHMSL is a **brake light**, not a constant-hot circuit. It only powers up when you press the brake pedal. Your dog box fan needs always-hot. So they wouldn't tap the CHMSL itself for the fan power source — but they might have tapped something *next to it* and damaged both.

**Check fuse #38 CHMSL (10A)** in that underhood box you already have open. If it's blown, that's interesting — could mean the installer caused a short that took out the brake light fuse, and your fan circuit might share a fault path.

**More likely scenario:** Look at fuse **#43 ENG (15A)** or any of the other always-hot accessory fuses. But honestly, since you already have the underhood box open, the fastest move is:

**Pull every fuse one at a time and visually inspect.** Takes 10 minutes. A blown fuse will be obvious. Pay extra attention to anything labeled with general accessory/auxiliary functions, and to #38 CHMSL specifically given your tail light symptom.

**Also worth checking inside the cab:** The driver's side and passenger's side instrument panel fuse boxes. The dog box installer might have tapped into a cab fuse instead of going under the hood. Look for any fuse with an "add-a-circuit" piggyback (looks like a fuse with a wire coming off it).

**One more angle:** Trace the dog box fan wire backward from the switch you photographed. That switch has to have a power wire coming into it from somewhere. Pull the panel below it (kick panel) and see where the red/hot wire goes. That's the fastest path to finding the source — much faster than guessing at fuses.

### SCOTT (2026-05-03T19:55)
#43 doesn’t look blown. But looks a little burnt.
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T19:56)
 Found it. That fuse is **toast** — and it tells a story.

**What I'm seeing:**
- The blades are dark brown/black and discolored — that's heat damage from sustained high current
- The element inside the blue housing actually does look broken or melted (hard to tell through the housing, but combined with the blade discoloration, it's done)
- This is a **15A mini fuse** (blue = 15A), matches #43 ENG on your legend

**Why this is the answer:**

Discolored blades like that mean the fuse was running near or at its limit for a long time, *then* finally let go. That's classic for an aftermarket tap that piggybacked onto an already-loaded circuit. Whoever installed the dog box fan likely ran it through fuse #43 (ENG, 15A) which was already powering factory stuff, and the combined load — fan + factory load — eventually cooked the fuse and the holder contacts.

**Before you just slap a new fuse in, slow down:**

1. **#43 ENG is a factory engine circuit, not an accessory tap.** If your CHMSL (brake light) and fan both went dead at the same time, and they're both downstream of #43, that's a sign the installer T-tapped this circuit. Not great, but explains the symptoms.

2. **Check the fuse holder itself.** Look in the slot where #43 came out. If the metal contacts inside the box are also brown/black/melted, the fuse box socket is damaged too. A new fuse will just cook again — or worse, melt the holder. If the contacts look clean and silver, you're probably OK.

3. **Replace with the correct rating — 15A, not bigger.** Do NOT put a 20A or 25A in there to "make it hold." That's how you start fires. If a 15A keeps blowing, the load is too high for the circuit, period.

4. **Investigate the load.** Before reinstalling, disconnect the dog box fan at that under-truck connector. Put in a new 15A fuse. If the fuse holds and your brake light works but the fan doesn't, you've confirmed the fan circuit is the problem child. Then you can reconnect the fan and see if it pops the fuse again — if it does, the fan motor is drawing too much (failing bearings, seized, shorted) or there's a short in the fan wiring.

**The right long-term fix:**

That dog box fan should be on its **own circuit** — own fused tap at the battery, own ground, own switch — not piggybacked onto #43 ENG. Once you confirm everything still works, I'd seriously consider re-doing the install:
- Fused tap at the battery (10–15A inline fuse sized to the fan)
- Properly run wire through the firewall grommet
- Quality switch in the cab
- Dedicated chassis ground at the fan end

That's a 30-minute job and it eliminates this whole class of problem forever.

**Right now:** Get a new 15A mini fuse (blue), inspect the holder contacts, and try it. Report back what happens.

### SCOTT (2026-05-03T19:56)
It worked fine for a few years.

### CLAUDE (2026-05-03T19:57)
 Fair point — and that actually changes the diagnosis. If it ran fine for years, the install probably wasn't undersized from the start. Something *changed* recently to push the current over 15A or cause an intermittent short. Worth finding out what before you just keep replacing fuses.

**What changed scenarios — most likely first:**

1. **Fan motor is failing.** Brushes wearing, bearings dragging, or windings starting to short internally. A motor that pulled 8A when new might pull 14A as it ages, then spike to 20A on startup and pop the fuse. This is the most common cause of "worked fine for years, now blows fuses."

2. **Wire chafed through somewhere.** Years of vibration, road debris, or that under-truck connector area getting wet/corroded. A wire that's mostly intact but occasionally touches ground will pop the fuse intermittently. Your truck lives on a farm — plenty of opportunity for a wire to get nicked or pulled.

3. **Corrosion at the under-truck connector.** That dirty 2-pin connector you showed me earlier could have enough resistance now to cause arcing and heat, which can pop a fuse over time.

4. **Something got added to the circuit.** Did anyone tap into this circuit for another accessory? A second light, another fan, anything? Doubling up loads on the same fuse will eventually cook it.

**Practical path forward:**

1. **Replace the 15A fuse.** Cheap, easy.
2. **Leave the dog box fan disconnected** at that under-truck connector for now.
3. **Turn the cab switch on.** Does the new fuse hold? Does your CHMSL come back to life? If yes, the fan circuit was definitely the load that killed it.
4. **Reconnect the fan and turn it on.** Three outcomes:
   - **Fuse holds, fan runs normal** = old fuse was just tired, you're done. Drive on.
   - **Fuse pops immediately** = dead short somewhere. Fan motor or pinched wire. Disconnect fan again, ohm-check the motor terminals — should read some resistance, not 0.
   - **Fan runs but slow/weak, or fuse pops after a minute** = motor is drawing too much. Fan is on its way out.

**Get an inexpensive clamp meter** (Harbor Freight has them for $30) if you want to actually measure the current draw with the fan running. Fan should pull whatever its rated amperage is — usually printed on the motor housing. If a "5A fan" is pulling 12A, the motor is failing.

**Honest read:** Given the burnt blade discoloration, this fuse has been getting hot for a while, not just popped once. Something has been gradually drawing more current than the circuit was designed for. Replace and test, but don't be surprised if you're shopping for a new fan motor soon.

Get a fresh 15A mini fuse in there and see what happens.

### SCOTT (2026-05-03T20:04)
I don’t have any fuses. Does this have any spares or is there one I can borrow from another spot?
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T20:04)
 Yes — these GM fuse boxes almost always have spare slots, and you can also borrow from a non-essential circuit to test.

**First, look for spares:**

Look at the **far left and right edges** of the fuse box, and the **bottom row**. GM typically leaves several empty fuse positions for upfitter use. Sometimes there are also spare fuses clipped into the underside of the fuse box lid — flip the lid over and check. Common spare values: 10A, 15A, 20A, 25A.

**If no spares, borrow from one of these "safe to test without" circuits:**

A 15A blue mini fuse you can pull temporarily without consequence:
- **#34 ECM IGN (15A)** — NO, don't pull this, truck won't run
- **#36 HTD MIR (15A)** — heated mirrors, totally safe to borrow if you have them
- **#39 MISC IGN (10A)** — wrong size
- **#43 ENG (15A)** — that's the one you're replacing
- **#47 THROT CONT (15A)** — NO, throttle control, leave it
- **#48 HORN (15A)** — safe to borrow, you just won't have a horn
- **#49 FOG LAMP (15A)** — safe to borrow, fog lights only

**Best candidates to borrow from (in order):**
1. **#36 HTD MIR** — heated mirrors, you don't need them today
2. **#49 FOG LAMP** — fog lights, you don't need them today
3. **#48 HORN** — works but you'd lose your horn temporarily

**What you're looking for:** A **15A mini blue fuse**. Mini fuses are the smaller ones (about half the size of a standard ATO blade fuse). Make sure you grab the right size — there are mini, standard, and micro2 fuses in modern GM boxes and they're not interchangeable.

**Important:** Looking at your fuse box photo, I see a mix of fuse styles. The blown one you showed me earlier was a **Micro2** style (the tall narrow one with both blades on one end, not standard mini). Double-check the shape of the slot at position #43 and match it. If it's Micro2, you need a Micro2 15A — and Micro2 fuses are less common, so check the lid for a spare specifically.

**Cleanest path:** Run by an auto parts store (or even a Walmart/Dollar General) and grab a multi-pack of fuses for $3–5. While you're at it, get a few extra in case this happens again or you cook another one testing.

Pop the lid off the fuse box and check the underside for spares first — that's the quickest answer.

### SCOTT (2026-05-03T20:05)
What is #54 for?

### CLAUDE (2026-05-03T20:05)
 **#54 is FRT WASH (15A)** — Front Washer.

That's the windshield washer fluid pump. Totally safe to borrow from for testing — you just won't be able to spray washer fluid on your windshield until you put it back. Probably the safest "borrow" option on the whole box, since you almost never need it on demand.

Pull #54, drop it into #43, flip the cab switch on, and see what happens. Just remember to swap it back (or replace with a fresh fuse) when you're done.

### SCOTT (2026-05-03T20:08)
Still nothing. And I put the “bad” fuse in 54 and the washer works. So not the fuse.

### CLAUDE (2026-05-03T20:08)
 Smart troubleshooting — that rules out the fuse entirely. The "bad" fuse is actually fine, and #43 is getting power to the fuse (otherwise borrowing wouldn't matter, but the fact that it ran the washer in #54 confirms the fuse itself is good).

**What this tells us:**

The fuse isn't blown, the fuse holder at #43 is presumably getting power, but **no power is reaching your cab switch** (no LEDs lit). So the break is somewhere between fuse #43's output and the switch.

**Wait — important question:** Did you actually verify that #43 ENG is the fuse feeding your dog box fan? We assumed it because the blade looked discolored, but discolored ≠ blown, and you just proved that. The fan circuit might be on a completely different fuse.

**Better approach — find the actual fuse:**

1. **Test for power at the cab switch wires.** Pull the switch out of the dash (it'll pop out from behind, just pry gently). You'll see two or three wires on the back: one power in, one going to the fan, sometimes a ground for the LED.

2. **With switch removed and meter on V⎓**, probe each wire (red probe to wire, black to clean ground). The wire that's *supposed* to be hot all the time should read 12V. If none of them read 12V, the break is upstream of the switch.

3. **Then pull fuses one at a time** with key off, and have someone watch the switch (or test the supply wire each time). When you pull the right fuse, that wire will go from 12V to 0V. That's your circuit.

**Faster method if you want to skip the hunt:**

Just **bypass the fuse box entirely** and run a temporary jumper from the battery positive to the supply side of the cab switch. Use an inline fuse holder with a 15A fuse for safety. If the switch lights up and the fan runs, you've confirmed:
- The switch works
- The wiring from switch to fan works
- Original problem is upstream (in the fuse box or between fuse box and switch — broken wire, bad connection at the fuse box, etc.)

Then you can decide whether to chase the original wiring or just permanently re-do it with a clean tap at the battery (which is what I'd do — that's the right way for an aftermarket accessory anyway).

**Honest take:** You've spent enough time hunting this. If you have an inline fuse holder and some wire, running a fresh feed from the battery to the switch with an inline fuse takes 20 minutes and gives you a circuit you can trust. The existing wiring has been compromised somewhere — chasing the exact failure point is academic at this stage.

Want to keep hunting, or take the shortcut?

### SCOTT (2026-05-03T20:10)
No that switch is sealed. No getting to the wires.

### CLAUDE (2026-05-03T20:10)
 OK, sealed switch — that's actually fine. We can test from the other end.

**Test at the under-truck connector instead:**

You already had the fan-side connector unplugged earlier (the dirty 2-pin you photographed). The mating half of that connector is the **truck side** — that's where power should be coming from when the switch is on.

1. **Locate the truck-side half** of that connector (the one you separated from the fan plug)
2. **Flip the cab switch to ON**
3. **Meter on V⎓**, black probe to clean ground (frame, battery negative)
4. **Probe each pin/socket on the truck side**

Results tell you everything:
- **12V on one pin** = power is making it from the switch all the way to the connector. Problem is the fan itself or the fan-side wiring/ground. Switch is fine.
- **0V on both pins** = break is somewhere between the fuse box and this connector. Switch may or may not be working.

**Sanity check on the switch:**

Even though you can't probe the wires, you can still tell if the switch is functional by what you find at the under-truck connector. If 12V shows up there only when the switch is ON, the switch works. If 12V is there regardless of switch position, the switch is bypassed/shorted. If never any voltage, switch or upstream is broken.

**Also worth a look:**

The wire run between the cab and the under-truck connector is probably the most exposed part of this whole circuit — it goes through a grommet somewhere and gets weather, road spray, and farm debris. If you find 0V at the under-truck connector, walk that wire visually before pulling more fuses. Look for:
- Chafing where it exits the cab
- Damage near the frame rail
- Pinch points at body mounts
- Rodent damage (you're on a farm — mice love wire insulation)

Get the meter on the truck-side of that under-truck connector with the switch on, and tell me what you read.

### SCOTT (2026-05-03T20:10)
No. That dirty two pin was the truck side connector.

### CLAUDE (2026-05-03T20:11)
 Got it — so the **dirty 2-pin you photographed first IS the truck side**, and that's where you read 0V with the switch on. That's actually clearer data than I was working with.

**So we know:**
- Switch ON → 0V at the truck-side connector under the truck
- No LEDs on the cab switch
- Fuse #43 is good (proven by washer test)

**The break is between the fuse box and that under-truck connector** — somewhere in the wire run that includes the cab switch.

**Best move now: bypass and test.**

Since you can't probe the sealed switch, treat it as a black box and test what's on each side of it.

**Step 1 — Confirm the fan circuit's actual fuse.**

Pull #43 and check if the cab switch was getting its power from there. With #43 removed:
- If something else stops working that you didn't expect, that's the circuit's real purpose
- The dog box fan circuit may be on a completely different fuse than we assumed

To find the *actual* fuse, you need to find which fuse is feeding the switch. Without probing the switch wires directly, the way to do this is:

**Step 2 — Trace from the under-truck connector backward.**

That truck-side connector has a wire going somewhere. Follow it. It should run up the frame, into the cab through a grommet, and ultimately to the switch. Anywhere along that path is a possible failure point. Most likely spots:

1. **Where the wire enters the cab** (grommet at the firewall or floor) — chafing, pinching, or rodent damage
2. **Behind/under the kick panel** where it transitions from harness to switch
3. **At the back of the switch itself** — even sealed switches have a connector behind them; the wire can be loose, pulled out, or the switch internals can fail

**Step 3 — The shortcut.**

Honestly, given:
- Sealed switch (can't probe)
- Truck-side connector under the truck is dead
- This was an aftermarket install that's now failing
- You've already spent significant time on this

The fastest fix is to **abandon the old wiring and run a new circuit**. Here's the minimum-effort version:

1. **New inline-fused tap at the battery** (10–15A inline fuse, $5)
2. **New switch in the cab** — or reuse the old one if you can get to its wires from behind the dash
3. **Run new wire** through the firewall (use existing grommet) and down to the dog box
4. **Splice into the fan-side connector** (or just hardwire to the fan, skip the connector entirely)

This is a 30–45 minute job with $20 of parts and gives you a circuit you can trust. Chasing the original failure point through a sealed switch and corroded under-truck connector is going to cost more time than rewiring it.

**One last thing to check before you commit to rewiring:**

Pull the **kick panel on the driver's side** (or wherever that switch is mounted). The switch may be sealed on the *cab side* but the wiring behind it usually has a connector or pigtail you can probe. Even just getting eyes on the wires behind the switch will tell you a lot — disconnected wire, melted insulation, rodent damage, etc.

What's your tolerance — keep hunting, or rewire it?

### SCOTT (2026-05-03T20:12)
Which fuse controls that tail light. These have to be connected somehow. And you said was #43. Not me

### CLAUDE (2026-05-03T20:13)
 Fair callout — yes, I said #43, and I jumped to that without doing the homework. Let me actually look it up instead of guessing.

Good — and you're right to push back. Looking at your fuse legend photo from earlier, **CHMSL is fuse #38 (10A)**, not #43. I conflated two different things and owe you a correction.

**So the connection theory:**

- **#38 CHMSL (10A)** = your dead third brake light
- **#43 ENG (15A)** = the one I had you pull and inspect (looked discolored but is actually fine, as you proved with the washer test)

These are **separate factory circuits**. They shouldn't be connected to each other through the factory wiring.

**But here's where they CAN be connected:**

The dog box installer likely **T-tapped into the CHMSL wire** somewhere — either at the cab fuse box, behind the headliner, or at the brake light itself. That CHMSL wire runs along the cab roof or rear cab seal, which is exactly where someone running a dog box accessory would look for a wire to tap. They might have used CHMSL as a switched-power source or as a convenient pass-through point.

If they did that and the tap shorted (corroded splice, water intrusion, chafe), it could:
- Blow fuse #38 → CHMSL goes dead
- Send back-current or break the path to the dog box switch → fan goes dead

**Test this theory — pull fuse #38:**

1. Pull #38 (10A red mini)
2. Inspect it — blown? Discolored?
3. If blown, replace it with a fresh 10A and see if the CHMSL comes back on (with brake pedal pressed)
4. If the fan also comes back to life, you've confirmed they're tapped together

**Also test #38 in place with your meter:**

Probe both blade tabs on top of #38 with the brake pedal pressed:
- Both hot (12V) = fuse good, problem is downstream (wire to light, light bulb, ground)
- One hot, one dead = fuse blown
- Both dead = no power getting to the fuse (BCM issue or upstream break)

**Honest assessment of where we are:**

You've done a lot of good diagnostic work. Three things we know for sure:
1. Fan-side connector reads 0V with switch on
2. Cab switch LEDs don't light
3. CHMSL is also dead

If #38 is also blown, it's strong evidence the dog box was tapped into that circuit and something shorted. If #38 is fine, then the dog box is on a different circuit and the CHMSL being dead is unrelated coincidence (or both got damaged by the same physical event — water, rodent, harness chafe).

Pull #38 and let me know what you find.

### SCOTT (2026-05-03T20:14)
#38 is fine.

### CLAUDE (2026-05-03T20:14)
 OK — so the CHMSL being dead and the fan being dead are likely **two separate problems that just happened to surface around the same time**. Frustrating, but at least we can stop chasing the connection theory.

**Where that leaves the fan circuit:**

Going back to confirmed facts:
- Truck-side connector under the truck: 0V with switch on
- Cab switch LEDs: not lighting
- Fuse #43 ENG: fine
- Fuse #38 CHMSL: fine

We don't actually know which fuse feeds this fan. We assumed #43 because of the discolored blades, but that was wrong. The fan circuit is on *some* fuse, somewhere — we just haven't found it.

**Two paths forward:**

**Path A — Find the actual fuse (slow, thorough)**

Pull fuses one at a time with the cab switch ON. After each pull, walk to the back of the truck and probe the under-truck connector. When you pull the right fuse, voltage at the connector should change (though it's already 0V, so this won't help unless we first restore power).

Better version: Have someone hold the cab switch ON while you pull fuses and watch the dash switch LEDs. Except the LEDs aren't lighting either, which means the switch isn't getting power *now* — so pulling fuses won't change anything visible. Dead end without more info.

**Path B — Bypass and rewire (fast, definitive)**

This is what I'd do at this point. You've spent real time on this, the original install is clearly compromised somewhere we can't easily reach, and the proper fix is a clean dedicated circuit anyway.

**Minimum-effort rewire:**

1. **Inline fuse holder + 15A fuse** ring-terminaled to battery positive
2. **Run wire** through firewall grommet (use existing if you can find it)
3. **New toggle switch** mounted somewhere accessible (or splice into the existing switch's output wire if you can reach behind the dash trim)
4. **Continue down the original wire run** to the under-truck connector
5. **Reconnect the fan-side connector**
6. **Verify ground** at the fan end — clean it up if corroded

Parts you need: ~10 ft of 14ga wire, inline fuse holder, 15A fuse, basic toggle switch, a few crimp connectors. Maybe $25 at any auto parts store.

**One more thing worth trying before you commit to rewiring:**

Get under the truck and **inspect the wire run from the cab down to that under-truck connector**. You're looking for:
- Obvious chafe points
- A wire pulled out of a connector
- Rodent damage (mice love the insulation, especially soy-based stuff GM uses)
- A spot where the wire visibly broke or got pinched

A 5-minute visual inspection of the wire run might reveal the failure point and save you a rewire. If you see something obvious, you can splice it. If everything looks intact, then the failure is hidden inside the cab harness or the sealed switch — and rewiring is the right call.

Your move — want to crawl under and look, or just rewire it?

### SCOTT (2026-05-03T20:24)
What is this. This is what the wire runs to
[File uploaded: photo.jpeg]
[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T20:24)
 **That's your answer.** That's a 40A automotive relay — and it's a huge clue about how this circuit is actually wired.

**What the relay tells us:**

The label says **HTT7101-12V, 40A, 14VDC** with a standard 5-pin relay schematic. That's a heavy-duty relay rated for 40 amps. **A dog box fan doesn't need anywhere near 40A** — typical RV/dog box fans pull 2–8A. So this relay isn't there because the fan needs that much current. It's there because the circuit was designed differently than I assumed.

**Likely actual circuit design:**

```
Battery (+)  →  Heavy-gauge wire  →  Relay terminal 30
                                      ↓ (when energized)
                                     Terminal 87  →  Fan
                                      
Cab switch  →  Low-current trigger wire  →  Relay terminal 86
Relay terminal 85  →  Ground
```

So the cab switch isn't carrying the fan's actual current — it's just sending a small trigger signal to energize the relay, which then closes the heavy-duty contacts and lets battery power flow to the fan. This is actually a *better* wiring design than what I'd been assuming.

**What this changes:**

The break could be in any of these places:
1. **Battery feed to terminal 30** (heavy wire from battery — there IS an inline fuse on this somewhere, almost certainly)
2. **Trigger wire from cab switch to terminal 86** (small wire)
3. **Ground at terminal 85**
4. **The relay itself** (failed coil or burnt contacts)
5. **Output wire from terminal 87 to the fan**

**Test the relay — easy and definitive:**

You're holding it in your hand, perfect. Two things to check:

**1. Test the coil with your meter on continuity (or ohms):**
- Probe terminals **85 and 86**
- Should read 50–120 ohms (typical relay coil resistance)
- Should also beep on continuity if your meter has it
- **Open circuit / OL = bad relay coil, replace it**

**2. Test the contacts:**
- Probe terminals **30 and 87** with the relay NOT energized → should read OL/open (no continuity)
- Probe terminals **30 and 87a** (if 5-pin) → should read closed/continuity
- **Apply 12V to 85 and 86** (touch leads from a battery, you'll hear a click) → now 30-87 should beep/close
- **No click when energized = bad relay**
- **Click but no continuity 30-87 = burnt contacts inside, bad relay**

**While the relay is out of the socket, test the socket too:**

Put your meter on V⎓, black to ground. With cab switch ON:
- **Socket terminal 30** (battery side) → should read 12V always. If 0V here, the inline fuse from battery is blown or the wire is broken.
- **Socket terminal 86** (trigger from switch) → should read 12V with switch ON. If 0V, the switch or trigger wire is the problem.
- **Socket terminal 85** → should be ground (0V relative to battery+, but should show continuity to chassis)

This will pinpoint exactly where the failure is.

**My bet:** Given the burnt fuse blade theory turned out wrong, and given the age and exposure of this install, I'd guess either:
- The relay coil is dead (most common failure)
- The battery feed has a corroded inline fuse holder somewhere upstream

Test the relay first since it's literally in your hand. That's a 30-second test.

### SCOTT (2026-05-03T20:25)
Not the cab switch I am tracing the fan plug that is in the truck bed back. And that is what it runs to.

### CLAUDE (2026-05-03T20:25)
 Oh — that completely reframes this. Sorry, I had the wrong mental model.

**So the actual circuit is:**

```
Cab switch  →  (somewhere)  →  Relay terminal 86 (trigger)
Battery (+) with inline fuse  →  Relay terminal 30
Relay terminal 87  →  2-pin connector  →  Fan
Relay terminal 85  →  Ground
```

The relay you're holding is the one that powers the fan directly. The cab switch only triggers it. That's exactly why the fan-side connector reads 0V — the relay isn't closing.

**Now we have a clean test sequence. Put the relay back in its socket and probe each terminal at the socket with switch ON:**

Standard 5-pin relay terminal layout (matches the diagram on your relay):
- **30** = battery feed (always hot)
- **87** = output to fan (hot only when relay is energized)
- **85** = ground for coil
- **86** = trigger signal from cab switch
- **87a** = normally-closed (probably unused here)

**Test at the relay SOCKET (relay removed), meter on V⎓, black probe to clean ground:**

1. **Terminal 30** → should be **12V always**, regardless of switch position
2. **Terminal 86** → should be **12V only when cab switch is ON**
3. **Terminal 85** → should show continuity to ground (switch meter to continuity mode, probe 85 and chassis — should beep)
4. **Terminal 87** → 0V with relay removed (it's only hot when relay closes)

**What each result tells you:**

- **30 dead** = battery feed broken (inline fuse blown, ring terminal off, wire damaged between battery and relay)
- **86 dead with switch ON** = cab switch dead, switch wiring broken, or switch not getting its own power
- **85 not grounded** = ground wire broken or ring terminal corroded/off
- **All three good** = relay itself is bad. Test it as I described before (coil resistance + bench-test the contacts with 12V applied)

**Most likely culprit, given the symptoms (no LEDs on switch + 0V at fan connector):**

I'd actually bet on **terminal 86 being dead**, because:
- The cab switch LEDs require power *through* the switch to light up
- If the switch isn't getting its supply voltage, the LEDs won't light AND the trigger signal won't reach the relay
- That points back to the cab switch's power feed (which still goes through *some* fuse upstream we haven't found)

But test all four points and the answer will be obvious.

**Quick alternative — bench-test the relay itself first while it's in your hand:**

- Meter on continuity, probe **85 and 86** → should beep, ~50–100 ohms (good coil)
- Probe **30 and 87** → should NOT beep (open contacts at rest)
- Now grab a fresh 9V or 12V source, touch wires from + to **86** and − to **85** → relay should click audibly
- While energized, probe **30 and 87** → should beep (closed contacts)

If the relay fails any of those tests, the relay itself is the problem and you can stop hunting. $5 part, plug in a new one.

### SCOTT (2026-05-03T20:26)
Which is term 30, 86, etc??

### CLAUDE (2026-05-03T20:26)
 Good question — relay terminals are stamped right on the relay itself, but they're tiny and hard to read in the dirt and sun. Look at the **bottom of the relay** (where the metal blades are) — each blade has its number molded or stamped into the plastic next to it.

**On the relay you're holding, the schematic on the side (the little drawing you can see in the photo) tells you the layout:**

The diagram shows:
- **85 and 86** = the coil (the squiggly line / rectangle in the diagram)
- **30** = the common contact (where battery feeds in)
- **87** = the normally-open output (where power goes when relay clicks on)
- **87a** = normally-closed (if your relay has 5 pins; some are 4-pin without 87a)

**Standard ISO relay pinout (looking at the bottom of the relay, blades pointing down):**

```
    85    86
     |    |
    [ COIL ]
    
    30    87a   87
     |     |    |
```

Most automotive relays follow this standard layout. The two blades on one end are the coil (85, 86), and the two or three blades on the other end are the contacts (30, 87, and optionally 87a).

**Easiest way to identify them on YOUR relay:**

1. Look at the **bottom of the relay** — the numbers are molded into the plastic next to each blade
2. Or look at the **schematic on the side label** — it shows which number is which terminal
3. The **two blades that connect to the coil symbol** (the rectangle/squiggle in the schematic) are 85 and 86
4. The **blade that's the "common" point** in the schematic (where the switch arm pivots from) is 30
5. The **blade the switch arm closes onto** is 87

**Pro tip if you can't read the numbers:**

Use your meter on continuity mode. Probe pairs of blades:
- The pair that reads **50–100 ohms** = the coil = those are 85 and 86
- The remaining blades are the contacts = 30 and 87 (and 87a if 5-pin)
- 30 and 87 will be **open** (no beep) at rest
- 30 and 87a (if present) will be **closed** (beep) at rest

That tells you which is which without needing to read the tiny stampings.

**For the socket** (where the relay plugs into, on the truck): the same numbers are usually molded into the plastic of the socket too, next to each terminal hole. Look closely — they're there, just small.

Can you get a clear photo of the bottom of the relay (the blades end)? I can identify the pins for you directly.

### SCOTT (2026-05-03T20:34)
With the key swith in. The 87 was the only one giving me a reading. With the relay out.

### CLAUDE (2026-05-03T20:34)
 Hmm — that's actually backwards from what we'd expect, and it's a really useful clue. Let me think through this carefully.

**With the relay REMOVED from the socket, you should see (with cab switch ON):**
- **30** = 12V (battery feed, always hot)
- **86** = 12V (trigger from cab switch)
- **85** = 0V but grounded (continuity to chassis)
- **87** = **0V** (this terminal is only hot when the relay is plugged in AND energized — with no relay, nothing connects 30 to 87)

**But you're reading 12V on 87 and nothing on the others.** That's weird and tells us the wiring isn't standard. A few possibilities:

**Possibility 1: The pins are labeled differently than I assumed**

The relay diagram on the label is the standard, but **the socket** could be wired with the supply going to what *looks* like terminal 87. Whoever installed this might have wired the socket "backwards" relative to convention. Functionally fine, but confusing for diagnosis.

**Possibility 2: You're identifying the wrong terminal**

The relay socket terminals are mirrored from the relay itself (the relay's pins go DOWN into the socket, so left/right flip when you look at the socket from above). Easy to get turned around.

**Possibility 3: This is the battery feed, and 30/86/85 wiring is broken**

The 12V you're reading might actually be the always-hot battery feed. If that's the case, then:
- The "30" terminal we expected = actually dead/broken
- The 12V terminal you found = the actual battery feed (just wired to a non-standard socket position)
- Nothing else has voltage because the cab switch circuit (which feeds 86) is dead — which is why the switch LEDs don't light

**Let's verify which terminal is actually which.**

**Test 1 — Identify the always-hot battery feed:**
Test that 12V terminal again with the **cab switch OFF**. 
- If still 12V → that's the battery feed (terminal 30, regardless of what position it's in)
- If 0V → that's a switched feed, meaning it's actually terminal 86 (cab switch trigger)

**Test 2 — Find the ground:**
Switch your meter to **continuity** (the speaker icon). Probe each socket terminal against a clean chassis ground. The one that beeps = ground = that's terminal 85.

**Test 3 — The remaining terminals:**
After identifying the hot feed and the ground, the other two are 86 (trigger) and 87 (output). 
- **86** should go from 0V to 12V when cab switch flips
- **87** should always be 0V with relay removed

**What I expect you'll find:**

If the cab switch is dead (which we know — no LEDs), then:
- One terminal = 12V always (battery feed = 30)
- One terminal = grounded (85)
- Two terminals = 0V (86 because switch is dead, and 87 because relay is removed)

So finding only one terminal hot is actually consistent with a dead cab switch circuit. **The 12V terminal you found is your battery feed (30), regardless of which position it's in.**

**This narrows the failure to:**

1. **Cab switch isn't getting power** (no fuse feed to switch, or switch internal failure)
2. **OR the trigger wire from switch to relay is broken**

**Next test — verify with switch OFF:**

Take that same probe position that read 12V. Flip the cab switch to OFF. Still 12V?
- **Yes** → it's the always-hot battery feed (30). Confirms relay has battery power, problem is upstream of the cab switch.
- **No, drops to 0V** → it's actually the trigger wire (86), and the cab switch IS working but somehow only sending power and the relay's battery feed (30) is dead.

That one test will tell us which side of the relay is failing. Run that and report back.

### SCOTT (2026-05-03T20:35)

[File uploaded: photo.jpeg]

### CLAUDE (2026-05-03T20:36)
 Perfect, that's exactly what I needed. I can read the markings clearly now.

**Your relay pinout (looking at the bottom, blades up):**

- **87** = top center (the larger blade) — output to fan
- **30** = top left/bottom-left corner — battery feed (the other large blade, opposite 87)
- **86** = lower left — coil / trigger from cab switch
- **85** = lower right (next to the "F" mark) — coil ground

The two big blades (30 and 87) are the high-current contacts. The two smaller blades (85 and 86) are the low-current coil.

**Now — about your reading:**

You said only **87** had voltage at the socket with the relay removed. That's actually the **output to the fan**. With the relay out, terminal 87 should be **floating/dead** — there's no path to it without the relay's contacts closing.

**12V on terminal 87 with relay removed is unusual and suggests one of these:**

1. **You misidentified which socket position you were probing.** Easy to do — the socket is mirrored from the relay (relay pins point down into the socket, so left/right flip when you look at the socket from above). What you thought was 87 might actually be 30.

2. **The wiring is non-standard.** Whoever installed this might have swapped 30 and 87 in the socket — wired the battery feed to the 87 position. Functionally the relay still works (contacts are bidirectional), but it's confusing for diagnosis.

3. **There's a back-feed from somewhere.** Less likely but possible.

**Easiest path forward — just identify what's actually live:**

Plug the relay back in, flip the cab switch ON, and probe each WIRE coming out of the socket from the back/side (where the wires enter):

- The wire that's **always 12V** (switch on or off) = battery feed (should be on terminal 30)
- The wire that goes **0V → 12V** when cab switch flips = trigger (should be on terminal 86)
- The wire that's **grounded** (continuity to chassis) = ground (should be on terminal 85)
- The wire going to the **fan connector** = output (should be on terminal 87)

Forget what's "supposed" to be on which pin. Just identify what each wire actually does.

**Then the diagnosis is straightforward:**

- **Battery feed wire dead** = inline fuse blown or wire broken back to battery
- **Trigger wire dead with switch on** = cab switch or its wiring failed
- **Ground wire not grounded** = ground connection failed
- **All three good but fan wire stays dead with relay in and switch on** = relay itself is bad

Test the relay itself while you have it in your hand — easiest test of all:

**Bench test the relay:**
1. Meter on continuity, probe **85 and 86** (the two coil pins) → should beep softly, ~50–100 ohms. No beep = dead coil = bad relay.
2. Probe **30 and 87** → should NOT beep at rest.
3. Connect a 9V or 12V battery: **+ to 86, − to 85** → relay should click loudly. Now 30 and 87 should beep when probed.

If the relay clicks and passes continuity tests, it's good. If not, $5–10 replacement at any auto parts store — get a standard 5-pin Bosch-style 40A relay, they're universal.

What does the bench test of the relay show?

### SCOTT (2026-05-03T20:49)
Think I found it. This is the connector at the switch wire.
[File uploaded: IMG_6550.jpeg]

### CLAUDE (2026-05-03T20:50)
 **There it is.** That's the answer right there.

I can see **green corrosion** crusted on that connector — classic copper corrosion from moisture intrusion. That whitish-green powder is what happens when copper conductors get wet over time. The connection is either fully open or has so much resistance that no meaningful current can pass.

That also perfectly explains every symptom:
- Cab switch LEDs don't light → switch isn't getting its 12V supply through this corroded connector
- Relay never triggers → no signal reaches terminal 86
- Fan stays dead → relay never closes
- And critically: **the relay itself, the fuse, the wiring downstream, the fan motor** — all probably fine

**Fix it right:**

1. **Cut the connector off entirely.** Don't try to clean it — once corrosion has wicked into the strands, the wire itself is compromised for an inch or two back. Cut back to clean, bright copper.

2. **Strip both wires** to clean copper on both sides of the cut. If you see green/black discoloration in the strands, keep cutting back until you hit shiny copper.

3. **Splice with a proper connection.** Best options in order:
   - **Solder + adhesive-lined heat shrink** (best, most durable)
   - **Heat-shrink butt connectors** (the kind with adhesive that seals when heated — good)
   - **Posi-Lock or Posi-Tap connectors** (decent, reusable)
   - **Plain crimp butt connectors with regular heat shrink over them** (acceptable)
   - **AVOID: scotch-locks, wire nuts, electrical tape alone** — that's how you end up here again

4. **Match wire colors** when you reconnect — should be obvious which wire goes to which.

5. **Seal it well.** This thing lives in the truck bed exposed to weather. Adhesive-lined heat shrink is non-negotiable. Don't skip it.

6. **Relocate if possible.** If you can route the splice to a more protected spot (under a body panel, inside the cab, somewhere out of direct water spray), do it. Where it sits now is exactly why it failed.

**Test before you finalize:**

Before you heat-shrink everything closed:
1. Strip and twist the wires together temporarily (or use alligator clips)
2. Flip the cab switch ON
3. Check for the LEDs lighting up
4. Have someone listen at the relay for the click
5. Check for 12V at the fan-side connector

If everything wakes up, you've found it. Then make the splice permanent.

**About the CHMSL (third brake light):**

That's almost certainly a separate, unrelated failure — probably just a bulb. Once you get the fan working, swap the CHMSL bulb and you'll likely fix that too. Burned out bulb is the most common cause of CHMSL failure, so start there before chasing wiring.

Nice work running this down. That corroded connector was hiding in plain sight, and you found it by tracing the wire instead of guessing at fuses. Get a good splice in there and you're back in business.

### SCOTT (2026-05-03T20:52)
Can I do just the white?  The blue and black look fine

### CLAUDE (2026-05-03T20:52)
 Yes — if the blue and black wires look clean (no green crud, no discoloration in the strands when you strip them back a bit), you can absolutely just repair the corroded white wire. No reason to redo healthy connections.

**Quick verification before you commit:**

Strip back about 1/2" of insulation on the blue and black wires. Look at the copper strands:
- **Bright/shiny copper** = good, leave them alone
- **Dull copper or slightly tarnished** = OK, still conductive, leave them
- **Green, black, or white powdery residue on the strands** = corroded, cut back further until clean
- **Strands break or feel brittle when you twist them** = corroded internally, cut back further

Corrosion wicks up the wire under the insulation, so check an inch or two back from the connector end, not just the very tip.

**For the white wire:**
1. Cut off the corroded section completely — keep cutting back until you see clean, shiny copper
2. Strip both ends
3. Splice with adhesive-lined heat-shrink butt connector (best for outdoor/bed-exposed wiring) or solder + heat shrink
4. Seal it up

**One thing worth doing while you're in there:**

Hit the blue and black connections with a shot of **dielectric grease** before you reassemble or close anything up. It's $4 at any auto parts store, prevents future corrosion, and doesn't interfere with conductivity. The fact that this connector failed once means moisture is getting in — protect what's still good.

Get the white wire spliced and test it before sealing everything up. Should be running once you reconnect.
