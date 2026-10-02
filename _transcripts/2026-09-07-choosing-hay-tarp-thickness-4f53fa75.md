# Choosing hay tarp thickness
Date: 2026-09-07
Conversation: 4f53fa75-e2df-43d8-9282-5559d239a6fe
Domain: watts-way-farms

## Summary
**Conversation Overview**

The person is engaged in hay storage and is working out tarp specifications for covering round bales stored outdoors. The conversation centered on selecting the right tarp thickness and calculating coverage for their specific bale setup. Claude recommended 16 mil tarps over 10 mil for durability under repeated use, UV exposure, and grommet stress, and noted that a "limited availability" countdown on a tarp listing was likely a sales tactic rather than genuine scarcity.

The person uses 4x5 round bales (4 ft wide, 5 ft diameter, following standard baler naming convention) stacked in a 2-on-bottom, 1-on-top pyramid configuration with 3 bales per stack. Their row contains 45 bales total, which equals 15 pyramid stacks. Claude calculated the full row length at 60 ft (15 stacks × 4 ft per bale width), determining that 2 standard 20x40 tarps would cover the entire row. Claude also worked through the cross-sectional drape geometry using the pyramid's curved envelope, finding the 20 ft tarp width covers approximately 17.9 ft of curved surface over the pyramid, landing roughly 1 foot short of full ground contact on each side — meaning the tarp edges should be weighted or tied at that point rather than expected to lie flush on the ground.

The person provided two important corrections during the conversation: first, they questioned whether Claude had the 4x5 bale dimensions reversed (Claude confirmed width-first is standard convention); second, they clarified that "45 per row" meant 45 individual bales, not 45 stacks, which significantly changed the tarp count from 5 down to 2. Claude used a Python geometry calculation to derive the pyramid drape math precisely.

### SCOTT (2026-09-07T00:45)
10mil or 16 mil for hay tarps?
[File uploaded: 7ce52491-2f1c-4a4b-8a05-981d5cfcf58e.jpeg]
[File uploaded: fcc137c416dc8ab6da364a84c2678485359d93ea.png]

### CLAUDE (2026-09-07T00:45)
16 mil, no question — for hay bales sitting outside long-term, thickness is what stands between you and rot.

- **16 mil** holds up to UV, wind flapping, and getting dragged on/off bales repeatedly without splitting at grommets. Hay tarps take abuse — you're pulling them on and off, they're getting walked on, snagged on stems.
- **10 mil** is fine for short-term or occasional cover but will tear at stress points faster, especially at the grommets and folds, and UV degradation shows up sooner.

Given you're already stacking bales in the open like in that photo, go 16 mil — cheaper in the long run since you're not replacing it every season.

One flag: that $129 tarp shows "only 16 left" and a 3-hour countdown — classic urgency pressure, not a real scarcity signal. Price yourself against a couple other 16 mil options before pulling the trigger.

### SCOTT (2026-09-07T00:46)
Those a 4x5 bales. How much will these tarps cover. How far down will they go?

### CLAUDE (2026-09-07T00:47)
For 4x5 round bales (4 ft wide, 5 ft diameter) laid in a single row on their sides, here's the math on that 20x40 tarp:

**Length-wise coverage:** 40 ft ÷ 4 ft per bale ≈ **9-10 bales** in a row, assuming they're lined up end-to-end and you leave a little slack for tying off.

**How far down the sides:** Going up and over the curve takes roughly the diameter (5 ft) out of your 20 ft width. That leaves 15 ft split between both sides — about **7-7.5 ft of hang-down per side**. Since the bale's total height is only 5 ft, that means the tarp reaches well past the ground on both sides, giving you extra material to weight down with tires, sandbags, or straps instead of it just barely reaching dirt.

**Caveats:**
- If your bales are stacked two-high or in a pyramid (like some in your photo), the math changes — you'd need way more overhang or a second tarp for the ends.
- "4x5" bale dimensions do vary a bit by baler, so measure one of yours if you want to nail this down exactly.
- Wind is the real enemy of loose hang-down — that extra 7 ft per side needs real weight/anchoring or it'll flap itself apart in a season.

If you've got a double row or stacked pallets like the photo shows, tell me the actual layout and I'll redo the coverage math for that.

### SCOTT (2026-09-07T00:48)
Are you sure this is right?  “For 4x5 round bales (4 ft wide, 5 ft diameter)” and it’s not the other way?

### CLAUDE (2026-09-07T00:48)
Yes, I'm confident — width first, diameter second is the standard convention for round bales. A "4x5" bale is 4 ft wide by 5 ft in diameter, same way a "5x6" baler (like a New Holland Roll-Belt or Vermeer 5x6) makes bales 5 ft wide by 6 ft diameter.

So my math holds: 4 ft width per bale for the row-length calc, 5 ft diameter for the height/hang-down calc.

One caveat worth naming: this convention isn't bulletproof — I've seen it used inconsistently by different guys and different equipment brands, and rarely diameter-first. If you know your specific baler model, that spec sheet will confirm it definitively. But "4 wide, 5 across" is what everyone around here means by "4x5."

### SCOTT (2026-09-07T00:49)
I stack them in the 2 on the bottom one on the top, mini pyramid, 3 per stack. And 34 in a row.

### SCOTT (2026-09-07T00:49)
I stack them in the 2 on the bottom one on the top, mini pyramid, 3 per stack. And 45 in a row.

### CLAUDE (2026-09-07T00:51)

Here's the geometry for a 2-bottom-1-top pyramid stack (4x5 bales, 45 per row):

**Pyramid dimensions** (bales touching, resting on the two bottom bales):
- Height: ~9.3 ft (top of the third bale)
- Footprint width: 10 ft (outer edge to outer edge of the two bottom bales)
- Length taken per stack (bale width direction): 4 ft

**Row length:** 45 stacks × 4 ft = **180 ft total row length**

**Tarp orientation — 40 ft dimension along the row:**
- Covers 40 ft ÷ 4 ft = **10 stacks per tarp**, lengthwise
- To cover all 45 stacks: 180 ft ÷ 40 ft = **4.5 → 5 tarps** needed for the full row

**20 ft dimension draped over the pyramid cross-section:**
- The actual curved distance up-and-over the pyramid (from the widest point of the bottom bales, over the top bale, to the widest point on the other side) is about **17.9 ft**
- That leaves only ~1 ft of slack per side beyond that point — the tarp will get close to the ground but likely falls about **1–1.5 ft short of full ground contact** on each side, rather than draping all the way down like it would on a single row of bales.

**Practical takeaway:**
- **5 tarps** (20x40 each) covers your 45-stack row, 10 stacks per tarp
- Expect the sides to stop a foot or so short of the ground — you'll want to weight/tie the edges at that height rather than assume ground contact, or overlap tarps slightly and let gravity/wind do less work
- This assumes bales are touching tightly in the pyramid; any gap between the bottom two bales increases both height and required width

If your stacks aren't tight (some air gap between the bottom two), let me know the actual spacing and I'll rerun the numbers.

### SCOTT (2026-09-07T00:52)
Not 45 stacks. 45 bales per row

### CLAUDE (2026-09-07T00:52)
Got it — that changes the count significantly.

**45 bales ÷ 3 bales per stack = 15 stacks in the row**

**Row length:** 15 stacks × 4 ft = **60 ft total**

**Tarps needed (40 ft dimension along the row):**
- 60 ft ÷ 40 ft = **1.5 → 2 tarps** to cover the full row
- One tarp covers 10 stacks; the second tarp covers the remaining 5 stacks (with overlap room to spare)

The cross-section math from before still holds — 20 ft width gets you over the pyramid (~17.9 ft envelope) but lands roughly a foot short of full ground contact per side, so plan to weight/tie down at that point rather than expect it flush to the dirt.

So: **2 tarps**, not 5, for 45 bales stacked as 15 pyramids in a single row.
