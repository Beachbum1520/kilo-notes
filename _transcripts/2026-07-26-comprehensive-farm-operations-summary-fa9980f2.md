# Comprehensive farm operations summary
Date: 2026-07-26
Conversation: fa9980f2-5308-44fd-af50-40fd0ec36852
Domain: watts-way-farms

## Summary
**Conversation Overview**

Scott operates Watts Way Farms, LLC, a 90-acre pasture-raised heritage livestock operation in Franklin, GA raising Irish Dexter cattle and heritage pork (Berkshire and Duroc breeds). He runs sales, strategy, marketing, and farm operations while his partner Angie handles daily animal care, AI breeding, and hands-on husbandry. Scott asked Claude to compile a comprehensive master memory card covering every aspect of farm operations and write it to his Google Drive, explicitly because Claude had been losing context between sessions and claiming ignorance of established details.

The memory card Claude produced and saved covers beef pricing and economics (customer price $6.75/lb hanging weight all-in, typical Dexter HW 475–550 lb, confirmed processing data from Cow #911), pork pricing ($5.50/lb HW all-in, processor at Resaca Meat Processing USDA), the full pig breeding herd with farrowing dates and settle statuses, the five-ingredient finishing ration with exact mix ratios and feeding rates, EQIP contract details through 2031 with NRCS contact Andrew Cobb, GrazeCart shipping zone structure, pork box SKU strategy, and all relevant tools and accounts. A critical standing correction is preserved: the old 250–350 lb Dexter hanging weight figure used in April 2026 was wrong and was corrected to 475–550 lb — any quote issued before May 2026 may be off by roughly $1,000. Scott's core epistemic standard — report only what is directly observed, label inferences explicitly, never state conclusions as facts — is documented as the governing rule for all Claude outputs, referenced by his own framing from Heinlein's Fair Witness concept.

Scott communicates informally and expects context to be understood without re-explanation. He treats factual corrections as authoritative and expects immediate updates. He wants clean output for copy requests with no surrounding commentary. He has explicitly instructed that date calculations should not override his provided dates without flagging the discrepancy first, and that approved messaging should be searched for before new variations are drafted. The document was written to Google Drive with a direct link provided, organized into 15 sections with confidence markers ([CONFIRMED], [ESTIMATE], [VERIFY]) on all figures, and 10 open action items flagged as of the session date of July 26, 2026.

---

**Tool Knowledge**

Claude used the Google Drive MCP integration to create a new file using `Google Drive: create_file` with `contentMimeType` set to `text/plain` and the full document text passed in the `textContent` parameter. This approach successfully created the file and returned a shareable document link. The file was titled with a datestamp convention ("rev 2026-07-26") which Scott should continue using for future revisions to maintain version clarity. No search or retrieval of existing Drive files was needed for this task; creation was a single-step operation. For future updates to this specific file, the document ID from the returned link (`1f2cyWsEY-waTTO4-9gVXMfNkyT-aA_LO9elPxJRToKE`) should be used to target edits directly rather than creating duplicate files.

### SCOTT (2026-07-26T23:45)
give me a summary very detiualed of everythign you know about our farm operations.  leave nothong oput.  beef sales, prices. hjangfong wihgts., everything

### CLAUDE (2026-07-26T23:46)

Here's the full picture, Scott. I've flagged anything where my records conflict or may be stale.

---

## THE OPERATION

**Watts Way Farms, LLC** — wattswayfarms.com — 90 acres, Franklin, GA. Pasture-raised heritage pork (Berkshire, Duroc) and Irish Dexter cattle. No antibiotics, no hormones. All profits reinvested.

- **You:** sales, strategy, marketing, farm ops; GC/PM/supervisor on infrastructure — you hire out physical labor
- **Angie:** full-time farming, daily animal care, AI breeding, hands-on husbandry
- **Structure:** sole proprietor / single-member LLC, Schedule F on the personal 1040. Substantial W-2 income makes farm loss deductions particularly valuable. Georgia conforms to Section 179 but **not** bonus depreciation.
- **Cattle herd:** ~60 Irish Dexters (that figure is from April 2026 — verify current count)

---

## BEEF — PRICING, WEIGHTS, ECONOMICS

**Customer price: $6.75/lb hanging weight, all-in.** Processing is baked in — no back-end fees at pickup. This is the message that's been going out to Carly, Mandy, Rene, and Lisa.

| Item | Figure |
|---|---|
| Price | $6.75/lb HW, all-in |
| Typical Dexter HW | **475–550 lb** |
| Whole beef, all-in | ~$3,200–$3,700 |
| Whole take-home | ~310–360 lb (~65% of HW) |
| Half beef | ~$1,725 |
| Processor cost | $75 kill + $1.10/lb cut & wrap |
| Your cost basis | ~$2.20/lb HW |

⚠️ **Conflict flag:** Back in April I was quoting **250–350 lb HW** on Dexters (that's what went to Mandy). By May that was corrected to **475–550 lb**, which is what I've used since. If Mandy is still in the pipeline off that April quote, her numbers are wrong by roughly $1,000.

**Actual processing data on file — Cow #911 (4/27/26):**
- Live weight: 832 lb
- Hanging weight: 464 lb
- Dressing: 55.77%
- Note: 464 lb came in just under the 475–550 band. #911 was on the 5-scoop ration, your heaviest.

**Beef economics (8-steer batch, run 5/27):**
- Finishing feed: ~$475/steer
- Halves at ~$1,725 × 2 = ~$3,450/steer revenue
- Operating contribution: ~$2,970/steer → **~$23,700 for the batch**
- Annual herd overhead (fixed, doesn't scale): hay $7,500 (150 bales @ $50) + protein/mineral $2,400 ($200/mo) = **$9,900**

**The headline number:** 14 of 16 halves from the current batch sold organically, zero ad spend. Dexter whole/half beef is the only demonstrably profitable segment of the operation. The farm has never been profitable overall. This is the model to replicate.

**Hide:** saved at no extra charge, raw and uncured — buyer handles tanning.

**Beef processor:** Daniel Jackson Farms, 5160 Co Rd 49, Ranburne, AL 36273 — ~34 miles one way.

---

## CURRENT BEEF CYCLE

| Milestone | Date |
|---|---|
| Batch started | 4/26/26 |
| Group 1 processing (4 head) | **Aug 10** |
| Group 2 processing (4 head) | **Aug 17** |
| Hang | ~21 days |
| Group 1 ready | ~Aug 31 |
| Group 2 ready | ~Sep 7 |

**Customer-facing anchor:** "mid-August processing, early September ready." Don't drift off that language.

**Known deposit on file:** Lisa Melzer, $200 down, August 2026.

---

## FINISHING RATION

Five ingredients: **cracked corn 65%, cottonseed hulls 15%, beet pulp 10%, soybean meal 5%, BOSS 5%.**

- Actual batch weight: ~970 lb (beet pulp and BOSS come in 40 lb bags)
- **Mix per bag of corn:** 1.5 scoops cottonseed hulls, 1 scoop beet pulp, 0.5 scoop SBM, 0.5 scoop BOSS
- **Clean batch = 20 bags:** 13 corn, 3 cottonseed hulls, 2 beet pulp, 1 SBM, 1 BOSS ≈ 3 barrels
- **Feeding rate:** ~16–18 lb/head/day (~30 scoops), always split AM/PM, free-choice hay and mineral alongside
- **Cost:** $0.283/lb → ~$274.60/batch

---

## PORK — PRICING & PROCESSING

**Customer price: $5.50/lb hanging weight, all-in.** Includes smoking, curing, and specialty products — bacon, hams, brats — at no upcharge.

| Item | Figure |
|---|---|
| Price | $5.50/lb HW, all-in |
| Typical hog HW | 220–240 lb |
| Whole hog | ~$1,200–$1,320 |
| Take-home | ~180–200 lb |
| Processor cost | $40 kill + $1.15/lb cut |

**Pork processor:** Resaca Meat Processing, USDA — 125 miles one way. Each batch = 2 round trips ≈ 500 miles ≈ **$210 fuel/batch** (Chevy 2500 4x4 diesel, ~12 mpg, ~$5/gal, pulling the 2011 Circle W). Resaca recently acquired a scalder, which is what opened up whole roaster pig sales.

**Piglets: $150 each.** Wean at 5 weeks, sell at 6. Boars not reserved within the first week get castrated.

---

## PIG BREEDING HERD

| Animal | Breed | Status |
|---|---|---|
| **Chester** | Purebred Duroc boar | b. ~mid-Jan 2025, arrived 3/9/25 at ~7 wks |
| **Hazel** | Purebred Berkshire sow | b. 7/21/24; to paddock w/Chester 5/2 → farrow ~8/24/26 |
| **Mabel** | Purebred Berkshire sow | b. 7/21/24; farrowed 5/19/26 — 10 born, 9 live (4B/5G), sire EL Macho |
| **Scarlet** | Purebred Duroc sow | farrowed 5/15/26 — 12 born, 9 live (5B/4G), sire Chester |
| **Ginger** | Registered Duroc sow | Chester 5/2 → farrow ~8/24/26 |
| **Nutmeg** | Registered Duroc gilt | Chester 5/3, partial stand, settle unconfirmed |
| **Willow** | F1 Berk×Duroc, stop-gap | AI 4/2/26 sire No Limit/Shipley, settle unconfirmed → farrow ~7/25/26 if settled |
| **Goldie** | F1 Berk×Duroc, stop-gap | Chester 5/9 → farrow ~8/31/26 |

**Breeding philosophy:** breed purebreds, sell F1 crosses to market, never breed F1s back. Willow and Goldie are one-litter stop-gaps — their offspring are market hogs. Target is 2 litters/year × 10 weaned; animals that don't hit it go to the freezer.

⚠️ **Two stale flags:** Nutmeg's return-to-heat watch window was ~5/24/26 — two months gone, so her status should be resolved by now one way or the other. And **Willow's projected farrow date was yesterday, 7/25** — that one's live right now.

**Late-August farrow cluster:** Hazel ~8/24, Ginger ~8/24, Nutmeg ~8/25 (if settled), Goldie ~8/31. Three to four farrows inside about a week. Pen logistics and Resaca scheduling need to be worked out well ahead.

**Spring 2026 piglets (Scarlet + Mabel, 18 total):** majority sold. Last remaining were a small group of purebred Durocs plus the one piglet where **one testicle was found and removed; a second was never observed.** Disclose exactly that wording — not "retained testicle," which is an inference. Recommend processing before ~5 months, price at a discount to the $150 standard.

**Litter-splitting default:** sell 8, raise 2. Mathematically validated. Only raise more than 2 if specific buyers are pre-identified **with deposits**.

---

## DISTRIBUTION & LOGISTICS

- **Whole/half hogs and beef:** in-person meetup only, **not shipped**
- **Live animals:** 5+ may qualify for a halfway meetup
- **Retail cuts:** shipped via UPS Ground (20 states) or 2nd Day Air, through the GrazeCart storefront
- **Delivery meet-ups:** Atlanta–Montgomery corridor
- **Cut sheets:** released only after deposit. No exceptions.

**Shipping structure** (rebuilt 5/27 in GrazeCart Delivery Zones — GrazeCart only supports flat fee or per-pound, no tiering):

| Zone | Rate | Minimum | Free shipping |
|---|---|---|---|
| Ground states | $2.50/lb | $75 | $300 |
| Air (rest of lower 48) | $5.50/lb | $150 | $450 |

⚠️ **Verify:** earlier in May you were running a $35 flat fee for 1-day out of LaGrange. My records show the per-pound zone structure was configured after that but I don't have confirmation every zone got saved.

**Box cost floor:** ~$33 (10×10) / ~$38 (12×12) all-in with packaging. Ground shipping cost floor ~$38 on any shipment. Known pitfall: a customer can add à la carte items that force a second box and GrazeCart won't charge again — you eat it.

---

## PORK BOX STRATEGY (open item)

Pig #1 runt inventory after family pull, ~107.6 lb: ~29.4 lb original brat, ~30 lb cheddar brat, ~30 lb jal/cheddar brat, ~8.26 lb bacon, plus small amounts of ends, hocks, liver, leaf fat.

Economics: at retail box pricing that runt pulls ~$1,400–$1,600 vs. ~$710 sold whole at $5.50/lb HW. Processing on it ran $532 for 109 lb take-home — $4.88/lb in processing alone, more than your sale price. Sold whole it would have lost money.

**SKU concepts:** Bacon & Brat (premium), Brat Sampler (workhorse), Slow Cook/Soup (clears odd cuts). Finalize when combining runt inventory with the prior batch.

Whole/Half Hog deposit reservations were set to pause/hide on the site during the no-supply window — **check whether those are still hidden**, because the late-August farrows change that picture.

---

## EQIP CONTRACT (USDA NRCS, through 2031)

Multi-year conservation buildout. Primary contact: **Andrew Cobb.**

Practices: virtual fencing (collars replace daily hot-wire moves inside large paddocks — this changes labor, not the grazing strategy), water well + solar pump, livestock pipeline and watering, stream crossing, rock-lined waterway (field 1 erosion headcut), brush management (2028 clearing ahead of 2029 excavation), permanent cross-fencing (weaning/isolation/sorting — not rotation), grazing management payments.

**Rules that bind:**
- No work inside a practice footprint until that year's items are approved
- NRCS pays 50% in advance; **must be spent within 90 days**
- Time advance requests to contractor mobilization, not bid collection
- **Hard deadline: end of 2031**

**2028 is the hardest year** — well driller books far out, pipeline and tanks stage behind the well. Use fall bidding cycles to prep each following year.

---

## DAILY FEEDING (scoops)

Chester 2 · four girl pigs 5 (shared) · Mabel 1.5 · Hazel 2 · Scarlet 1.5 · Ava (cow, pen area) 3 · #911 5

Note on file: #911 and Ava may need grass access as well. ⚠️ #911 was processed 4/27 — this list needs updating.

---

## OPERATING PRINCIPLES

**Epistemic precision — your core standard.** Report only what's directly observed. Label inferences as inferences. Never present a conclusion as fact when only an observation was made. "The side of the house facing me is white." Fair Witness Anne, *Stranger in a Strange Land*. This applies to every output I produce for you.

**Marketing:**
- Standard piglet value prop: hot wire trained, nipple waterer trained from birth, handled daily for socialization, pasture-raised, no antibiotics or hormones — "ready to hit the ground running"
- Sale posts are strictly positive and buyer-focused. No farm-direction backstory, no uncertain animal details, nothing that gives a buyer pause
- Customers buy the story, not just the beef — warm, conversational, real farm detail over polished marketing
- Never fabricate product details
- Scarcity and honest disclosure over vague or inflated claims
- Pickup/meetup logistics stay private, not in public posts
- Urgency tactics (unreserved boars getting cut) are DM-only
- **No discount codes exist.** FREEZER20 and NEWAREA10 are dead and permanently out of strategy — they conflict with a relationship-driven brand
- When messaging is already established and approved, I search for the saved version rather than writing a new variation

**Husbandry:**
- Blue-Kote (gentian violet) is FDA-prohibited in food animals — use Triodine (7% iodine) for castration wound care
- Dexters readily nurse calves that aren't theirs; udder condition is unreliable for dam ID. Use post-calving vulvar condition/discharge and head count
- Year-round bull exposure costs you calving-season anchors for tracking losses
- Boar pheromone priming improves conception. Hybrid model preferred: Chester with the group by default, AI reserved for specific outside genetics with brief separation to avoid sire ambiguity
- Large litters (12+): intervene after 30–45 min of stalled late progress; always do a final manual check after the apparent last piglet
- **Perilla mint** — serious cattle toxicity, peaks Aug–Oct. That's **right now through fall.** 2,4-D Amine 400 for control; wait until plants are visibly dead and brown before letting cattle in
- Sweet gum near wood lines is long-term suppression, not a one-time fix
- USDA processor relationship means DIY fat-heating taint tests and out-of-cycle runs aren't practical — factor that into disposition on problem animals

---

## TOOLS

- **GrazeCart** — storefront. Pricing unit: Weight for individual items, Package for boxes. Stock-out threshold 3. Packing group Frozen. Itemized display for boxes. No back-ordering. Backlog: tags and protocols were skipped during SKU buildout, plus SEO on all existing products — both flagged as winter slow-season work
- **Mailchimp** — email
- **Facebook Ads Manager** — pixel 1099315745596325; UTM `utm_source=facebook&utm_medium=cpc&utm_campaign=[campaign]&utm_content={{ad.name}}`. Targeting Alpharetta, Johns Creek, Roswell, Cumming, Marietta, Milton. **Known issue: Meta's AI has rewritten your ad copy — it inserted "grass-finished beef" into a pork ad.** Watch that
- **Upwork** — social media contractor · **WhatsApp** — direct contractor comms
- **TaxAct online** — business/farm returns · **QuickBooks** — bookkeeping, Philippines-based accountant does monthly reconciliation
- **Shipley Swine** — AI semen. Sires used: EL Macho (Berkshire), No Limit (Duroc #437, Guaranteed Settle pricing), Deadbolt (Duroc)
- **National Swine Registry** — papers on Ginger and Nutmeg
- **2011 Circle W trailer** — VIN 1C9TB216XB1140130, model CWT61635K. 16'×6' bumper pull, ~6'6" tall, 7,000 lb GVWR, tandem 3,500 lb leaf spring axles, electric brakes, 2" coupler, PT pine floor, ST225/75R15 tires, 5-lug 15" wheels (5×4.5"), spare on top rail. Fits ~8–10 Dexters or 10–15 hogs. Circle W: 334-374-2560
- **Kubota RTV1140CPX** — shift lever grip part K7561-42530; retaining screw is M5 Phillips pan-head SEMS (03024-505xx series); test M5×16 and M5×20 for fit

---

## OPEN ITEMS AS OF TODAY (7/26/26)

1. **Willow** — farrow date was yesterday. Live situation.
2. **Nutmeg** — settle status should be resolved; my last note is two months stale
3. **Late-August farrow cluster** — pen logistics and Resaca scheduling need locking now
4. **Perilla mint** — in peak toxicity window
5. **Facebook roaster pig ad** — the recommendation was to hold and run a small targeted ad in early August, with an Aug 20 decision date. Early August is next week
6. **Beef batch** — Aug 10 processing is 15 days out
7. **Pork box SKUs** — combine runt inventory with prior batch, finalize
8. **Nutmeg breeding stock sale** — listed; farm exiting that line
9. **Whole/Half Hog SKUs** — verify whether still hidden on the site
10. **Daily feed list** — needs #911 removed

### SCOTT (2026-07-26T23:48)
turn this into a memory card and wroit it to my drive so you can unfuck youself when you keep telloing me you don;t knwo these detials

### CLAUDE (2026-07-26T23:50)

Written to your Drive:

**[Watts Way Farms — Claude Memory Card (rev 2026-07-26)](https://docs.google.com/document/d/1f2cyWsEY-waTTO4-9gVXMfNkyT-aA_LO9elPxJRToKE/edit)**

15 sections. Paste the whole thing at the top of a chat, or just the section you need.

A few things I built in deliberately:

**Confidence markers on every number.** [CONFIRMED] / [ESTIMATE] / [VERIFY]. Your Fair Witness rule is section-zero, before any data, so it's the first thing read.

**The 250–350 lb Dexter error is called out by name** with a "do not reuse" warning, so it can't creep back into a quote.

**Every stale item is tagged [VERIFY] rather than silently dropped** — Willow's 7/25 farrow, Nutmeg's settle, the GrazeCart shipping zones, the hidden hog SKUs, #911 still on the feed list.

**Section 14 is how you work** — corrections are authoritative, don't override your dates with arithmetic, clean copy with no commentary, search for approved messaging before writing new.

Two gaps worth filling when you get a minute: the current Dexter head count (my number is from April) and whether the GrazeCart zone settings actually saved. Send me either and I'll update the doc.
