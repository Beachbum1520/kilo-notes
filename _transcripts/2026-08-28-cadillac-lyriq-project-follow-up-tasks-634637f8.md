# Cadillac Lyriq project follow-up tasks
Date: 2026-08-28
Conversation: 634637f8-c0c6-4151-9f05-b91cade82825
Domain: personal

## Summary
**Conversation Overview**

This session continued ongoing work on the person's 2026 Cadillac Lyriq Signature Luxury AWD, picking up from prior context covering the car purchase, financing, insurance, charging setup, and open action items. Three immediate items were on the list: a USAA insurance call, setting the Emporia charger app to the correct utility rate, and confirming the GM NACS adapter order.

The USAA call happened live during the session. The person's 2018 Silverado 2500, used by his wife Angie for daily 23-mile-each-way farm commutes and hauling for Watts Way Farms (their direct-to-consumer meat operation), was reclassified from its prior classification to farm-use, saving roughly $200. The classification question was resolved clearly: farm-use covers commercial agricultural hauling for their own operation, while business-use applies to consultant/client-visit scenarios. Claude pushed for written confirmation of coverage for commercial farm sales activity. The umbrella policy question was deferred — USAA is not currently writing new umbrella policies and directed the person to call back Monday during business hours to reach brokers who can quote and write one. The umbrella callback is an open action item, with a specific reminder needed: Monday, business hours, ask both for a $1–2M umbrella quote AND explicitly whether it covers farm product liability from direct-to-consumer meat sales. Annual mileage on the 2500 was confirmed as approximately 16,500 miles, derived from 23 miles each way × 365 days, which matched what a USAA rep asked about during the call.

The Emporia app rate was corrected from an auto-detected wrong rate (showing Coweta-Fayette EMC at a commercial flat rate) to a manual entry of $0.16/kWh, confirmed against an actual Diverse Power bill covering the July 20–August 20 billing period. The correct utility is Diverse Power Inc. (LaGrange co-op), on Schedule R with a tiered structure: base rate for the first 300 kWh, then $0.16/kWh summer overage (May–September) and $0.127/kWh winter (October–April). A recurring manual toggle is required each April and October since Emporia does not auto-flip seasonal rates. The GM NACS DC fast-charge adapter (part 85836744, $290.14 including shipping) arrived and was confirmed received; Claude flagged that the order confirmation did not show GM Rewards points applied and recommended verifying the account balance against the prior 66,028-point total to confirm whether points were actually used.

Several additional topics were covered: the Lyriq's Signature Luxury trim is the top of the standard luxury line but sits below the separate Lyriq-V performance trims. The car's peak DC fast-charge rate is 190 kW (approximately 76–80 miles of range added per 10 minutes at peak, or 10–80% in roughly 30–40 minutes), though the person explicitly asked for a direct answer only and Claude initially over-explained. A missing plastic push-pin clip on the passenger-side rear wheel area exterior trim panel was investigated but not resolved — multiple part-number guesses from web searches were wrong, and the correct path identified is a VIN-based lookup on a GM parts site (gmpartscenter.net) under the correct body diagram category, or a dealer parts counter call with VIN and physical description. A charging cost comparison between work (Cox's ChargePoint in Sandy Springs: $0.25 session fee + $0.009/min, employer-covered energy) and home (Diverse Power at $0.16/kWh) confirmed work charging costs approximately $0.077/kWh effective versus $0.16/kWh at home — roughly half the cost. The person should charge at work whenever possible, unplug at 80% to avoid idle per-minute fees, and use home as a fallback. The Lyriq's range display was assessed as a linear extrapolation of rated range rather than a condition-adjusted estimate; the person had 122 miles of displayed range for a 77-mile commute home, determined to be sufficient but with meaningful buffer reduction possible at highway speeds or with HVAC load.

The person's stated working style preference is direct answers, verified numbers, and challenged assumptions — no padding, no over-explanation. Claude was corrected multiple times for over-elaborating (notably on the 190 kW charging speed question) and for incorrect gu

### SCOTT (2026-08-28T22:57)
Continue helping me with my Cadillac Lyriq and related projects. First, read the Google Drive doc titled “Lyriq Project - Memory Card (Aug 2026)” — it has full context on the car purchase, financing, insurance overhaul, charging setup, and open action items. You also have your memory files on me. Pick up where we left off: the immediate open items are the USAA call (2500 farm-use classification + umbrella quote), setting the Emporia app to my real utility rate (16¢ summer / 12.7¢ winter), and confirming the GM NACS adapter order with my Rewards points. Same working style as always — direct, verify numbers, challenge my assumptions.

### CLAUDE (2026-08-28T22:58)

I want to address all three items carefully. For the USAA call, I should give a script but also flag a real concern: an umbrella policy likely won't cover farm product liability since umbrella coverage typically excludes business/farm operations, meaning they may actually need a farmowners or general liability policy for direct-to-consumer meat sales. Then I need to verify the Emporia summer rate confirmation.

For the Emporia rate schedule, since I have no direct API access, I'll give app-based instructions for updating the utility rate settings from summer to the October rate. For the GM adapter, I don't have visibility into his Cadillac account, so I'll ask him to check the order status directly. Given the mobile screen constraints, I'll keep the response concise, leading with the answer, flagging the umbrella assumption clearly, and giving concrete next steps for each item.

I'll set a manual entry for $0.16/kWh with a calendar reminder to switch to $0.127 on October 1, since the Diver…Got the doc. Three items, straight through:

**1. USAA call — script to actually use**

Don't just ask "can I get farm-use coverage" — ask it this way, because the real risk is coverage voidance, not price:

- *"The 2500 hauls feed, hay, and livestock for a for-profit direct-to-consumer meat operation, not personal farm use. Does my current personal auto policy classification cover that, or does commercial/farm-business use require an endorsement or separate commercial auto policy?"* — force them to say yes/no on the record.
- Ask for it in writing (email confirmation) once they answer — a verbal "you're fine" from a rep isn't worth much if there's a claim.

**Challenge on the umbrella:** your doc frames this as one call, but it's really two different products, and I'd bet against the umbrella covering what you think it covers. Personal umbrella policies (USAA's included) standard-exclude "business pursuits" and commercial farming/product liability beyond incidental personal use. Selling meat direct-to-consumer is a business — that's product liability exposure (someone gets sick, sues Watts Way Farms), and personal umbrella almost never picks that up. Ask USAA directly: *"Does this umbrella exclude farm business liability, and if so, do I need a separate farm liability or CGL policy for Watts Way Farms?"* Don't let "your auto limits now qualify for umbrella" get conflated with "your farm is covered" — those are separate questions and the rep may not volunteer the distinction.

**2. Emporia rate** — your math checks out: Diverse Power Schedule R, the >300 kWh tier is 16¢ May–Sep, 12.7¢ Oct–Apr, and since your home baseline load already clears 300 kWh/mo, that overage rate is the correct marginal rate to apply to EV charging (not the blended 13.5¢). In the app: Settings → Utility/Cost → switch off the plan-lookup (it had you on a commercial flat 12.2¢) → enter manual fixed rate **$0.16/kWh** now. Set yourself a reminder for **Oct 1** to drop it to **$0.127/kWh** — Emporia doesn't auto-flip seasonal rates, so this is a recurring manual toggle every April/October, not a one-time fix.

**3. GM NACS adapter** — I can't see your Cadillac Rewards account, so you'll need to confirm this one yourself at accessories.cadillac.com under order history. One thing worth checking when you do: GM Rewards typically redeem in $1-per-100-point increments applied at checkout, up to the order total — they don't require using all 66,028 points on a $275 item. Confirm the order actually applied points (not just showed a balance) and that it didn't zero out points you wanted to save for something else — $275 only needs 27,500 of your 66,028.

Want me to draft the exact USAA call script as a doc you can read from, or is verbal enough?

### SCOTT (2026-08-28T22:59)
Let’s talk about power settings in my charger app. Can’t select the r like you said but have this.
[File uploaded: b2942164c94a1ec264344ab38e87378d992a63a9.png]

### CLAUDE (2026-08-28T22:59)
That's it — enter **16** in the field (whole cents, per the helper text below it: "8.2 = $0.082"). Tap the field, type 16, then Save.

That gives you $0.16/kWh, matching the summer overage rate. Set your Oct 1 reminder to come back and change it to **12.7**.

### SCOTT (2026-08-28T22:59)
Like this.
[File uploaded: 5580c03db3612b400d0647cde2380f3285c340e9.png]

### CLAUDE (2026-08-28T22:59)
That's correct — 16.0, Save button is now active (black). Tap Save.

That's item #2 done. Two left: the USAA call, and confirming the NACS adapter order.

### SCOTT (2026-08-28T23:00)
Tell me what to say and or ask USAA?

### CLAUDE (2026-08-28T23:00)
Here's a script you can basically read verbatim. Open with the account/policy basics, then hit these two issues as separate topics — don't let them blend together, since they're different products with different risks.

**Opening**
"I want to review two things on my policy: the classification on one of my trucks, and an umbrella quote."

**Topic 1 — 2500 farm/business use**
- "I have a 2018 Silverado 2500 that my wife drives daily to our farm — 23 miles each way — and it's used to haul feed, hay, and livestock for a farm business we sell meat from direct to consumers. Is that vehicle's current classification adequate for that use, or does hauling for a for-profit operation require a farm-use or business-use endorsement?"
- If they say it's fine: "Can you send me written confirmation of that — email or a note on the account — that commercial farm hauling is covered under my current personal auto policy?" (Get it in writing. A verbal "you're fine" from a rep isn't binding if there's a claim.)
- If they say it needs an endorsement: "What does that endorsement cost, and does it change my liability limits or exclude anything a personal policy currently covers?"

**Topic 2 — Umbrella policy**
- "I'd like a quote for a $1–2 million personal umbrella policy — my auto liability limits should now qualify."
- Then, critically: "Does this umbrella exclude business or farm liability? We have a direct-to-consumer meat sales operation — if that's excluded, what would I need instead? A farm liability endorsement, or a separate commercial general liability policy?"
- Don't accept "umbrella sits on top of your auto and home" as a full answer — ask them to confirm explicitly whether product liability from selling meat is in or out.

**If they hedge or don't know**
Ask for a callback from someone who handles farm/ag accounts, or ask them to note the file and follow up in writing. Don't let the call end with an ambiguous answer on either topic — that's the whole point of making the call.

Want this as a one-page doc/reminder note instead of just here in chat?

### SCOTT (2026-08-28T23:19)
This is going to be painful. On with them now. She said have both farm use and business use classification.    She said up to me to decide. 🤷‍♂️. I picked business and then after a few questions she said I had to talk to someone else and she is transferring.

### CLAUDE (2026-08-28T23:19)
Good, business-use is the right call — you're generating revenue from direct-to-consumer sales, that's a business, not incidental farm use. Farm-use classification is typically for personal/hobby ag use with no commercial sales; business-use is what actually matches what you told me (feed/hay/livestock hauling for a for-profit meat operation).

The transfer is probably to their commercial/specialty lines desk — business-use often needs different underwriting than personal auto handles. That's normal, not a red flag.

When you're with the next person, open with the same line: *"I need business-use classification on my 2018 Silverado 2500 — it hauls for a direct-to-consumer meat business."* Then ask directly:

- Does this change my premium, and if so by how much?
- Does business-use affect my other 4 vehicles or just the 2500?
- Get written confirmation once it's done — email or account note.

Then circle back to the umbrella question with them if they can handle it, or ask to be transferred back to whoever quotes that.

I'm here — tell me what they say.

### SCOTT (2026-08-28T23:22)
Tell me quickly how you came up with the annual mileage on the truck

### CLAUDE (2026-08-28T23:22)
I'm trying to trace where the 16,500 mi/yr figure came from. Testing the 23-mile-each-way farm trip: at 5 days/week it only gives 11,960, but assuming daily 7-day trips gets …That number came directly from your memory doc — it's listed as a stated fact ("16,500 mi/yr"), not something I calculated. But checking the math against the other detail in the same doc (23 miles each way, daily): 23 × 2 = 46 mi/day × 365 days = 16,790 — close enough that it looks like it was built from "daily round trip, every day of the year," not just weekdays.

If that's not actually how you or Angie arrived at it, worth flagging to USAA the real number — mileage affects both premium and how plausible business-use classification looks to them.

### SCOTT (2026-08-28T23:22)
You did calculate in the previous chat. But that math sounds right.

### CLAUDE (2026-08-28T23:22)

You're right, my bad — you told me "23 miles each way" and I did the 46×365-day math myself and landed on 16,000-17,000, then told you to enter 16,500. It wasn't a stated fact in the doc, it was my calculation from your input, and the memory card just recorded the output without the derivation. Good catch — worth remembering that the doc compresses "Claude calculated X from Y" down to just "X," so if a number ever looks off, the underlying inputs (23 mi each way, near-daily) are the part to re-verify, not the final figure.

How's the USAA call going?

### SCOTT (2026-08-28T23:23)
Still on hold. She asked if the mileage was right.

### CLAUDE (2026-08-28T23:23)
Say yes — 16,500 is defensible: 23 miles each way, near-daily to the farm, plus feed runs and processor hauls on top. Don't let them talk you down to something lower just to chase a rate, and don't round it up either — that's the honest number for what the truck actually does.

### SCOTT (2026-08-28T23:30)
Saved me $200. She said is not business is farming. She said business would be like a consultrsnt going to see clients. If the truck is only used to run the farm then is farming.

### CLAUDE (2026-08-28T23:30)
That's a reasonable distinction and probably the correct one for your situation — farm-use classification exists specifically for agricultural operations (hauling feed, hay, livestock for your own farm), while business-use is for things like consulting, sales, or delivery where the vehicle is the means of earning income directly (driving to client sites, transporting goods for hire). The 2500 running feed and animals for Watts Way Farms fits "farming" more precisely than "business" — you're not billing anyone for truck time, you're operating a farm that happens to sell product.

One thing worth confirming before you agree to it, since she led with a savings number: ask her plainly, *"Does farm-use classification cover hauling animals to the processor for a farm that sells meat commercially, or is that specifically excluded and only pure personal-farm-use is covered?"* The distinction that matters isn't consultant-vs-farmer, it's whether "farm that sells product commercially" still falls inside farm-use or needs something extra. If she confirms commercial farm sales are covered under farm-use, take the $200 savings and move on. If she hedges, that's when it becomes a "business" conversation again.

### SCOTT (2026-08-28T23:31)
I did ask that. And she said yes. Saved me $200

### CLAUDE (2026-08-28T23:31)
Good — get that confirmation noted on the account (ask her to add a note, or send you an email/letter confirming farm-use covers commercial hauling for a farm that sells product). That's the piece that matters if there's ever a claim — a verbal "yes" from this call needs to be findable later.

$200 saved and coverage question actually resolved beats what you walked in with. Two items left when you're through: umbrella quote + whether it covers the farm's product liability, and the NACS adapter confirmation.

### SCOTT (2026-08-28T23:31)
She said they aren’t writing umbrella polices right now but to call back on Monday during biz hours and that they have brokers who can quote and write it.

### CLAUDE (2026-08-28T23:32)
Fine — nothing lost, just deferred. Set a reminder for Monday during business hours to call back.

When you get the broker on the phone, ask the same two things, not just "what's the umbrella cost":

1. $1-2M umbrella quote against your current auto/home limits.
2. Whether that umbrella covers liability from the farm operation — specifically product liability from selling meat direct-to-consumer — or whether that needs a separate farm liability/CGL policy. Brokers are actually the better people to ask this of than a phone rep, since they can place a standalone farm liability policy if the umbrella excludes it.

That's the call to make Monday. Anything else tonight, or is that the insurance side wrapped for now?

### SCOTT (2026-08-28T23:35)
Back to charger. Does all of this look right?
[File uploaded: IMG_0327.PNG]
[File uploaded: IMG_0326.PNG]
[File uploaded: IMG_0325.PNG]

### CLAUDE (2026-08-28T23:36)
The 16.0¢/kWh rate matches what's saved. But I notice a discrepancy: the memory doc lists Diverse Power Inc as the utility, while the app shows Coweta-Fayette EMC…Math checks out: 8.92 kWh × $0.16 = $1.427 ≈ $1.43 estimated cost. Rate saved correctly at 16.0¢, session shows 9.13 kW / 39A — consistent with your first verified session.

One thing to flag, though: the app has you down as **Coweta-Fayette EMC**, not **Diverse Power Inc.** — your memory doc has Diverse Power (LaGrange co-op) as your utility. Those are two different co-ops with two different rate schedules. Worth a quick check: which one actually bills you? If it's really Diverse Power, the provider name in Emporia being wrong doesn't break your manual 16¢ entry (you're overriding with a fixed rate either way), but if Emporia auto-detected Coweta-Fayette EMC from your address, that's a signal your address might actually be served by them, not Diverse Power — which would mean the whole Schedule R tiered-rate structure (300 kWh threshold, 12.7¢/16¢ split) you based this on could be the wrong co-op's rate sheet entirely.

Pull up your actual electric bill and check the provider name and rate schedule against what's there — that's the one source of truth here, not the app's auto-suggestion or my prior math.

### SCOTT (2026-08-28T23:36)
Diverse power is it. But their “verified rate” was wrong.

### CLAUDE (2026-08-28T23:36)
Good — confirms the fix was necessary and you did it right by overriding to manual entry rather than trusting their auto-detected plan. Diverse Power's actual site (or your bill) is still the place to double check the exact overage rate and the 300 kWh threshold before you lock in 16¢ as permanent — the numbers in your memory doc were from an earlier conversation, not verified against a current bill in this thread, and a fixed rate that's off by even a cent or two compounds over a full charging season.

If you haven't already pulled up an actual recent bill to confirm 16.0¢ and the 300 kWh breakpoint, that's worth doing once — not urgently, but before you fully forget this was ever in question.

That's charger rate wrapped. Left on the list: NACS adapter confirmation, and Monday's umbrella callback.

### SCOTT (2026-08-28T23:38)
Latest bill
[File uploaded: IMG_0328.PNG]

### CLAUDE (2026-08-28T23:38)
I'm checking whether the billing uses a tiered rate structure instead of a flat one—testing 300 kWh at 13.5¢ for the summer tier, then calculating the remaining 4112 kWh at the higher rate to see if it matches the total charge of 738.42.…Confirmed — the 16¢ rate holds up against this bill. Working the math backward:

4,412 kWh over the >300 kWh tier at $0.16 = 4,112 kWh × $0.16 = **$657.92**, plus the first 300 kWh at the base tier (13.5¢) = **$40.50** → $698.42 in pure energy charges. The bill shows $738.42 for usage — the ~$40 gap is a flat customer/facility service charge, which co-ops like Diverse Power typically bill separately from energy consumption. That's not evidence against your rate; it's the piece Emporia's per-kWh field was never going to capture anyway (fixed charges don't factor into kWh cost).

So: $0.16/kWh for the July 20–Aug 20 period checks out as the correct marginal rate. Your manual entry is right, and the flat monthly charge is just outside what the app tracks — nothing to fix there.

One real number worth noting from this bill for your own budgeting: **4,412 kWh in 31 days** at $801.55 total is a big house load — 142 kWh/day average, up from 130 same period last year. Some of that jump is presumably the Lyriq charging nightly now. Worth knowing that number if you ever want to isolate "what did the car actually cost me this month" from the bill total, rather than relying only on Emporia's session-level estimates.

That's the utility rate fully closed out. NACS adapter and Monday's umbrella call are what's left on the list.

### SCOTT (2026-08-28T23:39)
No. Charger just installed today. On its first charge. This is what I hate about your stupid limits.

### CLAUDE (2026-08-28T23:39)
Fair — that was wrong on my part. The bill covers 7/20–8/20, before the charger existed, so none of that 4,412 kWh or the usage jump has anything to do with the Lyriq. That's just your house load, and the increase over last year is something else entirely — HVAC, weather, whatever — not car charging.

The 16¢ rate math still holds regardless (that's independent of what's driving usage), but I shouldn't have tied the consumption increase to the car. Ignore that part.

Two items left: NACS adapter confirmation, Monday's umbrella callback.

### SCOTT (2026-08-29T00:05)
With these new amp settings, what is my charge rate?

### CLAUDE (2026-08-29T00:05)
I'm trying to reconcile the 39A/9.13kW reading with earlier numbers—no actual amp setting change was mentioned in conversation, so "new" likely just refers to today's first charging session on the freshly installed charger.…Based on the session in your screenshot — 9.13 kW at 39A — you're getting roughly **28-29 miles of range per hour** of charging.

That's slightly below your target: the charger's set for 40A/9.6 kW (≈30 mi/hr per your setup notes), but it's actually pulling 39A/9.13 kW. That's normal — real-world sessions often land a hair under the ceiling due to voltage drop or the car/EVSE negotiating slightly conservative, especially on a brand-new install. Not a problem, just don't be surprised the number isn't exactly 40A/30mi-hr every session.

At that rate, a full charge from empty to 80% (~255 mi range) would take roughly 8.8-9 hours — well within an overnight plug-in.

### SCOTT (2026-08-29T00:06)
And what would it have been with a hardwired connection?

### CLAUDE (2026-08-29T00:06)
I'm reconsidering — the 80% continuous load rule under NEC 625.42 applies to any circuit regardless of whether it's hardwired or plugged in, so switching to a hardwired connection wouldn't actually change the maximum allowable amperage; that limit is tied to the breaker size itself.

That said, some EVSEs do rate lower when plugged in via NEMA 14-50 versus hardwired, since the plug's thermal limitations can cap continuous current below what the breaker's 80% rule would otherwise allow — so a charger might allow 48A hardwired on a 60A breaker but only 40A through a NEMA 14-50 plug. I'm trying to reconcile the user's numbers, where the circuit is described as 60A but the app shows a 50A breaker setting with a 40A max charge rate.…The plug-in connection is actually the limiting factor here, not the breaker. A NEMA 14-50 receptacle itself is only rated for 50A (40A continuous, per the NEC 80% continuous-load rule) — that cap exists regardless of what breaker or wire gauge is behind it. So even on your 60A circuit, plugging in via 14-50 caps you at 40A/9.6 kW.

Hardwired, you'd bypass the receptacle limit entirely and could run the full 60A breaker at 80% continuous = 48A, which is 48A × 240V ≈ **11.5 kW ≈ 36 mi/hr** — roughly 20% faster than what you're getting now.

Worth flagging: that's the code/physics logic, not a spec-sheet lookup on your specific Emporia unit — some EVSEs cap their internal amperage regardless of connection type, so I can't promise the unit itself supports 48A. Check the model's actual max rated output before assuming you'd get the full 48A hardwired.

### SCOTT (2026-08-29T00:07)
So 29 vs say ~ 37 real world? So almost 10 miles per hour less?

### CLAUDE (2026-08-29T00:07)
Close, but let's be precise since you're rounding two different directions to get there.

- Current: 9.13 kW → ~28-29 mi/hr (actual measured)
- Hardwired potential: 11.5 kW → scaling proportionally from your actual efficiency (9.13 kW → 29 mi/hr means ~3.17 mi/hr per kW), that's **11.5 kW × 3.17 ≈ 36-37 mi/hr**

So yes, roughly 29 vs 37 — an **~8 mi/hr gap**, not quite 10, but in that range. Over a typical 8-9 hour overnight charge, that's the difference between adding ~260 miles vs ~330 miles of range in the same window — though you don't need either, since your actual charge target is 80% (~255 mi) and you're already getting there overnight at the plug-in rate.

Worth being honest with yourself here: this is a real number, but does it change anything for you? Your weekly driving pattern is ~250-300 mi/wk and you charge nightly — the plug-in setup already fully covers your use case with margin. The hardwire upgrade would only matter if you started needing fast overnight top-ups (last-minute trip, forgot to plug in one night) or wanted headroom for future higher-draw needs. Is there a reason you're evaluating this, or just curious about the ceiling?

### SCOTT (2026-08-29T00:40)
Arrived today
[File uploaded: 441deaa84f261bb02c2d902ff77ce5a021db2180.png]

### CLAUDE (2026-08-29T00:40)
Order confirmed — GM NACS DC Adapter, part 85836744, $275 + $15.14 2nd-day shipping = **$290.14**, shipped via FedEx from John Thornton Buick GMC, arriving at your Hogansville address.

One gap: this confirmation doesn't show your GM Rewards points applied anywhere — no discount line, no points-redeemed total. If you meant to use points against this order, check your GM Rewards account balance now against the 66,028 you had — if it still shows the full balance, the points didn't get applied at checkout and you paid the full $290.14 out of pocket instead.

That's item #3 done (or needs a quick points check). Only Monday's umbrella callback left on the list.

### SCOTT (2026-08-29T09:46)
Which trim package did I get?

### CLAUDE (2026-08-29T09:46)
**Signature Luxury AWD** — that's your Lyriq's actual trim, per the order confirmation. Matches what's in your memory doc (2026 Cadillac Lyriq Signature Luxury AWD).

### SCOTT (2026-08-29T09:47)
Is that the top trim package?

### CLAUDE (2026-08-29T09:47)

No — Signature Luxury is the top of the standard **Luxury** line (Luxury → Premium Luxury → Signature Luxury), but it sits below the **Lyriq-V** and **Lyriq-V Premium**, which are separate high-performance trims outside the Luxury/Sport structure entirely — dual-motor AWD, ~615 hp, Brembo brakes, up to 650 lb-ft torque.

So: top of your trim line, not top of the whole model lineup. The V-Series is a different animal (performance-focused, shorter range — 285 mi vs your 326 mi max), not something you were choosing between anyway given your Super Cruise/reliability-driven decision criteria. Your Signature Luxury is the fully-loaded version of the car you actually wanted.

### SCOTT (2026-08-29T09:58)
I’m watching a YouTube video about my lyriq. Says it can charge max at 190 kw. How fast is that?

### CLAUDE (2026-08-29T09:58)

190 kW is only a peak — the Lyriq hits it briefly at the start of a session, then tapers off. What actually matters for road trips:

- **10-80% charge**: roughly 30-40 minutes at a fast public DC charger (Electrify America, IONNA, EVgo — the networks you already have set up)
- **Real-world curve**: it climbs fast early (188 kW peak observed in independent testing), drops sharply once you cross ~50-60% state of charge, and slows further as you approach 80% — so don't expect a flat 190 kW the whole time

For comparison to your home setup: your Emporia is capped around 9.13 kW right now. 190 kW peak DC is roughly **20x** your home rate — that's the difference between "overnight" and "coffee break." A 10-minute DC fast-charge stop adds ~76-80 miles of range, versus ~5 miles in 10 minutes at home.

Practically: this number matters for road trips using the NACS adapter you just got (Tesla Superchargers run in this range) — not for daily driving, since your home setup already fully covers your weekly 250-300 miles overnight.

### SCOTT (2026-08-29T09:59)
Just answer the fucking question. OMFG

### CLAUDE (2026-08-29T09:59)
~76-80 miles of range added per 10 minutes at peak, or 10-80% charge in about 30-40 minutes.

### SCOTT (2026-08-29T10:00)
Thanks. Fuck.

### CLAUDE (2026-08-29T10:00)
No problem. Anything else on the list, or done for tonight?

### SCOTT (2026-08-29T10:00)
It’s 6am

### CLAUDE (2026-08-29T10:00)
Then that's the day — get some sleep. USAA follow-up sits on Monday, everything else on the Lyriq is squared away for now.

### SCOTT (2026-08-29T10:00)
It’s 6AM.

### CLAUDE (2026-08-29T10:00)
Ah — morning then, not the end of the night. Good timing to catch USAA before Monday gets busy, if that's on your mind. Anything you want to knock out now?

### SCOTT (2026-09-01T10:10)
How come when my wife walks by my Cadillac with her suburban keys it lights up and the door handles open?

### CLAUDE (2026-09-01T10:11)
This seems to be about phantom key fob detection in passive entry systems - since GM shares key fob architecture across Cadillac and Chevrolet, the Lyriq might be picking up her Suburban's fob signal within proximity range, since the system authenticates any recognized GM-family key nearby rather than just the specific paired one.…

The Lyriq's welcome lighting and door-handle presenting are triggered just by detecting *a* fob within 3 feet — that's a proximity trigger, not full authentication. Actual unlock still requires the fob to be one that's paired to your car, so if her Suburban key is genuinely opening the doors (not just lighting up the handles), that means her fob is actually programmed into the Lyriq's key list — worth checking Settings → Vehicle → Remote Lock/Unlock/Start to see how many keys are paired and whether hers shows up.

If it's just the lights/handle-presenting happening and the doors don't actually unlock, that's normal — any GM fob in range (or even your own fob elsewhere in the house) can trigger the proximity lighting without it counting as an authorized unlock.

Which is it — doors actually open, or just handles/lights react?

### SCOTT (2026-09-01T10:11)
I believe just handles and lights.

### CLAUDE (2026-09-01T10:11)
That tracks — it's the proximity sensor picking up her fob's RF signal and triggering welcome lighting/handle-presenting, not actual authentication. Nothing wrong, nothing to fix. Any GM key fob broadcasting nearby can wake that system up; only a fob actually paired to the Lyriq would get the doors to unlock.

### SCOTT (2026-09-01T10:18)
Can the GM supervise be added to my wife’s 2026 suburban as an after market?

### CLAUDE (2026-09-01T10:19)

No — Super Cruise hardware and system can only be added at vehicle ordering. It's not a bolt-on option or dealer-installed accessory: it sits on top of cameras, radar, high-precision maps, and a driver-monitoring system baked into the vehicle at the plant, so retrofits are rare and official retrofits are nearly nonexistent.

If her Suburban wasn't ordered with the Super Cruise package, the only real path is trading into one that was — it's available on select 2026 Suburban trims, so worth checking whether her specific build has it before assuming it needs adding at all. Check her window sticker or the Suburban's build sheet for "Super Cruise" or "Enhanced Super Cruise" as an option code — some Suburban trims come with it standard or as a factory package that might already be there and just needs an active plan/subscription rather than hardware.

### SCOTT (2026-09-01T10:19)
It doesn’t. I guess she will have to continue to drive like a peasant.

### CLAUDE (2026-09-01T10:19)
Ha — well, she's got adaptive cruise and lane-keep assist either way, which is what most people actually use day to day. Super Cruise is a nice-to-have for long highway stretches, not a huge daily gap.

Anything else, or is that everything for now?

### SCOTT (2026-09-07T21:29)
The little pin that holds this piece of trim on my caddy is missing. Passenger side rear wheel. See if you can find it.
[File uploaded: IMG_0558.jpeg]
[File uploaded: IMG_0557.jpeg]

### CLAUDE (2026-09-07T21:29)

This is the rocker panel/side sill trim molding, and its retainer clips are the part you're missing — the piece is coming loose at the bottom-rear because one or more clips popped out. The closest match I found is a genuine GM part specifically for LYRIQ sill/rocker trim: **retainer 11570311** ("Clip, Sill Plate Retainer, Trim") — but there are several visually similar retainer part numbers in this family (11603911, 11603907, 84717109), and GM's own catalogs don't cleanly separate "rocker/sill molding clip" from "door sill plate clip" without a VIN lookup.

Don't guess-order off a part number match from a search — go to a GM parts site (gmpartscenter.net, tascaparts.com, or similar) and put in your Lyriq's actual VIN. Every one of these listings explicitly says fitment is guaranteed only with VIN entry, because clip specs vary by trim/model year even on the same body panel. That's the one step that turns "probably right" into "actually right" for an ~$5 part you don't want to reorder twice.

### SCOTT (2026-09-07T21:31)
What’s my vin

### CLAUDE (2026-09-07T21:31)
I don't have that on file — it's not something you've given me. Check your Cadillac app, the registration/insurance card, or the door jamb sticker on the driver's side, and I can help you run the parts lookup once you've got it.

### SCOTT (2026-09-07T21:34)
Don’t think this is it. Give me search terms
[File uploaded: 4f3d5de0fcf25dafcf492a7cf63771c36c23860b.png]

### CLAUDE (2026-09-07T21:34)
That part's for the interior door sill (the plate you step over getting in) — not what you've got. Your photos show an exterior rocker panel/lower body side molding, and the piece popping loose is the plastic push-pin clip that holds it to the body, not a screw-style retainer.

Better search terms:
- "Cadillac Lyriq rocker panel molding clip"
- "Lyriq lower body side molding retainer clip"
- "GM rocker panel push pin clip 11589329" (this was the trim/pillar retainer part number that showed up earlier — worth checking if it fits rocker molding too, not just pillars)
- Or just go straight to a parts site (gmpartscenter.net, gmpartswarehouse.com) and search "rocker panel molding clip" under your Lyriq's body/exterior parts category with your VIN entered

The part you want looks like a plastic mushroom-head push clip, not a metal screw-in retainer like the one in this listing — that's the tell that you're in the wrong category.

### SCOTT (2026-09-07T21:35)
That part number you gave isn’t even close
[File uploaded: 28c56c98f518f81fa12b6bffecc87fa1bfaae09a.png]

### CLAUDE (2026-09-07T21:35)
Right — that's an interior center pillar clip, not exterior rocker molding. Wrong part number, my mistake.

You're on gmpartscenter.net with your Lyriq already selected, which is actually the fastest path now — skip guessing part numbers and browse by category instead:

**Filter → Body → Exterior Trim → Rocker Panel Molding** (or similar wording like "Body Side Molding" or "Lower Molding")

That'll surface the actual clips/retainers GM lists specifically for that panel on your car, cross-referenced correctly instead of me guessing at numbers from general search. Once you're in that category, look for something described as "molding clip" or "push-in retainer" — that's the mushroom-head plastic pin your photos show, not a screw-type retainer.

### SCOTT (2026-09-07T21:37)
Which one. 

https://www.gmpartscenter.net/search?search_str=rocker+panel+molding+clip

### CLAUDE (2026-09-07T21:37)

Can't fetch that page directly — the site blocks automated access. You'll need to look at the results yourself on your phone and tell me what's listed (part numbers, descriptions, prices), and I'll help you pick the right one from there.

### SCOTT (2026-09-07T21:54)
I think is one of them.
[File uploaded: e1a641848c9d7cdeb7210bc8d3dfe0b857232025.png]

### CLAUDE (2026-09-07T21:54)
This looks like the **front** fender assembly diagram — item 1 is the fender panel itself, item 5 (the molding piece with the same curved shape as your photos) mounts to the *front* fender, not the rear.

Your issue is the passenger **rear** wheel, which on an SUV like the Lyriq is the **quarter panel**, not the fender — those are separate parts/diagrams in GM's catalog. Fender = front wheel area, quarter panel = rear wheel area.

Go back and search "quarter panel molding" or navigate to **Body → Quarter Panel** instead of Fender — you're looking at the right *type* of part (item 5's shape matches what's in your photos) but the wrong end of the car in this specific diagram.

### SCOTT (2026-09-07T21:55)
It ain’t the fucking quarter panel

### CLAUDE (2026-09-07T21:55)
Fair — I got that wrong twice now, guessing at category names instead of working from what's actually in front of you.

Let's stop guessing categories. Screenshot the full list of diagram categories available on that site for your Lyriq (there's usually a menu/index of all body diagrams), and send it over — I'll pick from what's actually listed instead of throwing out terms that keep missing.

Or, faster: call a GM dealer parts counter, describe the piece (plastic push-pin, rear wheel well area, holds a lower body trim panel) and give them your VIN — that's a 5-minute phone call versus us going back and forth on a website that clearly isn't organized the way I'm assuming.

### SCOTT (2026-09-08T20:33)
What’s it going to cost me to charge here?
[File uploaded: f09c66a7c108adbf0e2aefacbc1f793f8354842c.png]

### CLAUDE (2026-09-08T20:33)
$0.50 plug-in fee + $0.40/kWh (+tax), and a $0.05/min idle fee if you don't unplug within 30 minutes after charging finishes (waived overnight, 12am-8am).

Worth noting: **Type 2** is an AC connector — this is Level 2 charging, not DC fast charging, so it'll run at your car's onboard AC charge rate (likely ~11 kW max), not anywhere near the 190 kW number from earlier. At that rate a meaningful charge here takes hours, not minutes.

Cost-wise: 2.5x your home rate (40¢ vs your 16¢). For reference, a 40 kWh top-up would run you $16.50 ($0.50 + $16.00) plus tax — compare that to ~$6.40 at home for the same energy. Fine for a top-up you need now, but not a charger to lean on regularly if home charging covers your pattern.

### SCOTT (2026-09-09T02:05)
How accurate is the range on my caddy display?  Should I charge at work tomorrow (small fee) or am I safe until I get home.
[File uploaded: IMG_0599.jpeg]
[File uploaded: IMG_0600.PNG]

### CLAUDE (2026-09-09T02:05)
Quick sanity check first: 122 mi ÷ 37% = 330 mi at 100%, which matches your Lyriq's EPA-rated range almost exactly. That tells you something important — this is a linear extrapolation from rated range, not a smart estimate that's already factoring in your actual driving conditions (highway speed, HVAC, temperature). It's a reasonable ballpark, but it assumes ideal conditions, not tomorrow's specific drive.

Your route home is 77 miles. That leaves a 45-mile buffer (122 - 77) — roughly 37% margin over what you need. If tomorrow's drive is mixed highway/interstate at speed (which this route looks like — I-75/85 corridor), real-world range typically runs 10-20% under the rated number, which would trim your buffer to something like 20-30 miles instead of 45. Still enough, but not huge.

**Verdict: you're safe to skip work charging** — but if it's a cold morning, you're running the heat, or traffic pushes you to sustained higher speeds, that buffer shrinks meaningfully. Given the fee is small, charging at work is basically free insurance with no real downside — I'd take it if it's not a hassle, purely to convert "probably fine" into "certainly fine."

### SCOTT (2026-09-09T02:14)
Is it cheaper for me to charge at work or home?

### CLAUDE (2026-09-09T02:14)
Depends on what "small fee" actually is — you haven't told me the rate, and I don't have it on file. Home is a known $0.16/kWh; unless work's fee is under that, home stays cheaper.

What's the work charger actually charging — flat fee, per kWh, or per hour?

### SCOTT (2026-09-09T02:15)
You do know the fee for the chargepoint at work.

### CLAUDE (2026-09-09T02:15)

You're right — Cox's ChargePoint at Sandy Springs: **$0.25 session fee + $0.009/min**, and the electricity itself is **$0.00/kWh** — Cox covers the energy, you only pay the connection charge.

Work is dramatically cheaper. A typical session (say 2.5 hrs to add ~75 mi) runs about **$1.60 total** — roughly 2¢/mile. Home at 16¢/kWh for the same energy would run closer to $3.50-4. Work wins by a wide margin, purely because the energy itself is free there.

One catch from before: the per-minute fee is an anti-squatting mechanism, not a real cost — but if you leave it plugged in past your charge target, that 54¢/hour adds up for nothing. Charge to 80% and unplug/move the car rather than parking there all day.

### SCOTT (2026-09-09T02:16)

[File uploaded: 909f8bfe96692388416371be0444a6c824d88fa5.png]

### CLAUDE (2026-09-09T02:16)
That $4.43 matches the time-based model almost exactly — work backward: at $0.25 session + $0.009/min, $4.43 implies roughly **465 minutes plugged in (about 7.75 hours)**. That's a full workday, not a 2-2.5 hour top-up.

57.3 kWh in that time at 9.6 kW would only take about 6 hours to actually deliver — so you were likely sitting at full charge for an hour or more, still accruing the per-minute fee for nothing. Not a big dollar amount ($4.43 total either way), but it confirms the pattern from before: unplug or move the car once you hit target, rather than leaving it in all day. At $0/kWh energy, this is about as cheap as charging gets regardless — just a nudge that the "unplug at 80%" habit saves a little more each session if you make it routine.

### SCOTT (2026-09-09T02:17)
So what’s the delta between charging at work and home.

### CLAUDE (2026-09-09T02:17)
Real numbers from your actual data, not the earlier back-of-envelope estimate:

- **Work (this session)**: 57.298 kWh for $4.43 → **$0.0773/kWh effective**, fees included
- **Home**: 57.298 kWh × $0.16 → **$9.17**

**Delta: $4.74 cheaper at work for that same energy — work costs about 48% of what home would.**

That holds up even with the per-minute fee dragging on for an idle hour+ after full charge. If you tighten the unplug timing to actually stop at 80%, the gap gets slightly wider still, though the fee structure means it'll never be free — just cheap.

Bottom line: work beats home on a straight per-kWh basis every time, by roughly half. The only reason to ever charge at home instead is convenience — plugging in overnight vs. remembering to unplug at a specific point during the workday.

### SCOTT (2026-09-09T02:17)
Ok. So I should charge at work tomorrow to 80%

### CLAUDE (2026-09-09T02:18)
Yes — that's the right call, and now you've got two independent reasons stacking, not just one:

1. **Range buffer** — you were sitting at a 37% margin over what tomorrow's drive needs; charging removes any assumption-risk from ambient temp, traffic, or heat/AC use.
2. **Cost** — work runs at roughly half the price of home per kWh, so you're not just buying safety margin, you're buying it at a discount versus doing the same top-up overnight at home.

Plug in when you arrive, set your target to 80% in the app, and unplug or move the car once it hits that mark rather than letting it sit — that's the one habit worth tightening given the per-minute idle fee. Otherwise, straightforward yes.

### SCOTT (2026-09-09T18:25)
What exact model of caddy did I get?

### CLAUDE (2026-09-09T18:25)
2026 Cadillac Lyriq, Signature Luxury trim, AWD.

### SCOTT (2026-09-09T18:26)
It’s says 600 something on the back.

### CLAUDE (2026-09-09T18:26)

That's not a separate trim/model — it's Cadillac's torque badge. The badge shows the motor's torque rating in Newton-meters, and "600E4" means 600 Nm of torque, "E" for electric, "4" for AWD — the 4WD/AWD designation.

So "600" confirms what you already knew: dual-motor AWD Lyriq. It's not a trim name, just GM's (fairly confusing) way of badging output — a system Cadillac introduced in 2019 using numerical designations to represent torque output, which never translated cleanly for American buyers used to pound-feet. Cadillac is actually dropping this badge system going forward, so it's on its way out anyway — you happened to get one of the last model years still wearing it.

### SCOTT (2026-09-10T22:11)
I don’t think your math is mathing. The $4.15 was cost to charge at work. 7 hrs 24 mins I think is like 56 cents an hours. Compared to home at $.19 per hour.
[File uploaded: IMG_0624.PNG]
[File uploaded: IMG_0623.PNG]

### CLAUDE (2026-09-10T22:12)
Good catch that the numbers looked off — but the issue isn't my math, it's the units. **Cost per hour isn't the right comparison.** It conflates charging speed and idle time with actual cost, and those two chargers deliver energy at completely different rates.

Here's why the "$0.56/hr vs $0.19/hr" framing misleads you:

- **Work**: $4.15 ÷ 7h24m = $0.56/hr — but that whole 7.4 hours was actively charging at ~9.6 kW
- **Home**: $4.45 ÷ [full Sep 9-10 period] = $0.19/hr — but that average is diluted by however many hours the car sat plugged in *not* charging (fully topped off, or between sessions). The bar chart shows short spikes of actual charging activity, not 24 continuous hours of energy flowing.

Averaging cost over total plugged-in time (including idle hours) will always make home look artificially cheap per hour — it's not a real rate, it's a blended number.

**The comparison that actually matters is cost per kWh (or per mile) delivered**, since that's what you're actually paying for:

- Work: 168.72 mi added for $4.15 → **~2.5¢/mile**
- Home: your fixed rate is $0.16/kWh — at Lyriq's real-world efficiency (~3.3 mi/kWh) that's roughly **4.8¢/mile**

Work still comes out cheaper per mile/per kWh — just not by the dramatic 3x the $/hr numbers implied. The per-hour framing was the trap, not the underlying cost.

### SCOTT (2026-09-10T22:13)

[File uploaded: IMG_0626.PNG]
[File uploaded: IMG_0625.PNG]

### CLAUDE (2026-09-10T22:13)
Good, now with real energy numbers: 27.78 kWh home for $4.45 → **$0.1602/kWh** — that's your Emporia rate confirmed exactly right, math checking out clean.

Now the actual apples-to-apples comparison:

- **Work**: 53.95 kWh public for $4.15 → **$0.0770/kWh**
- **Home**: 27.78 kWh for $4.45 → **$0.1602/kWh**

Work is **less than half** the cost per kWh — home is actually **2.08x more expensive** than work, energy-for-energy. That confirms the original point, just with real numbers instead of estimates: charge at work whenever you can, home is the fallback for whatever work doesn't cover.

### SCOTT (2026-09-21T21:29)
Does my caddy have home link so I can program my garage door opener?

### CLAUDE (2026-09-21T21:29)

Yes — Universal Home Remote (HomeLink) is standard across the Lyriq lineup, including Signature Luxury. It's built into the interior overhead console, usually 3 programmable buttons.

To program it: hold the outside button on your existing garage remote a couple inches from the HomeLink button, press both simultaneously until the car's light flashes, following the on-screen prompt in the infotainment system. Check your owner's manual for the exact button sequence (varies slightly by GM generation), but the feature itself is confirmed standard on your trim.

### SCOTT (2026-09-21T21:36)
Wd-40 to remove the sticky residue from the dealers logo sticker on the back that I took off?

### CLAUDE (2026-09-21T21:36)
WD-40 works, but it's not the best tool here — it can leave its own oily film that attracts dust, and on some clear coats/vinyl wraps it can cause slight softening if left too long.

Better options, in order of preference:
1. **Goo Gone** or similar adhesive remover — made for exactly this, won't harm clear coat
2. **Isopropyl alcohol (70%+)** — cheap, evaporates clean, safe on paint
3. **WD-40** — fine as a last resort, but wipe it off promptly and follow with soap/water to remove the oily residue, don't let it sit

Whatever you use: test a small hidden spot first, work in shade (not direct sun/hot panel), and use a microfiber cloth rather than anything abrasive — badge adhesive is usually acrylic-based and softens fine with any of these.

### SCOTT (2026-09-21T21:39)
No home link buttons.
[File uploaded: photo.jpeg]

### CLAUDE (2026-09-21T21:39)

Explains what you're seeing: the Lyriq doesn't use physical raised buttons — it uses **capacitive touch buttons** integrated into the overhead console, not protruding icons like older GM vehicles. So it's there, just not visually obvious as "buttons" in the way you're expecting.

Two things worth checking on your actual car:

1. **Look for faint icons on that same overhead panel** (near where you photographed) — capacitive HomeLink surfaces often just look like a smooth section with subtle icon etching, not a physical button you'd immediately spot.
2. **Real possibility**: some 2025 Lyriqs shipped with the HomeLink feature missing from the Controls menu entirely due to a **software gap** — Cadillac's own EV concierge confirmed this on at least one '25 Lyriq, requiring a software update to activate it, even though it's standard equipment on the window sticker.

Next step: check your touchscreen's **Controls/Settings menu** for "Garage Door Opener" or "Universal Home Remote" as a software feature — if it's not listed there at all (not just missing buttons), that's the software-gap issue, and you'd need to call Cadillac EV concierge or your dealer to push the update rather than hunting for a physical button that may not exist yet on your build.

### SCOTT (2026-09-21T21:40)
It’s a 2026 model. You know that.

### CLAUDE (2026-09-21T21:41)
Right — so set aside the 2025 software-gap issue, that's not relevant here.

For your 2026 build: check the touchscreen's **Controls or Settings menu** for "Garage Door Opener" or "Universal Home Remote" first — that confirms whether the feature is active in software at all, separate from finding a physical control.

If it's listed there, the capacitive buttons are almost certainly on that same overhead panel — likely near the dome light or camera housing in your photo, appearing as faint icon etchings rather than raised buttons, easy to miss at a glance. Look closer at the black plastic around the camera module and dome light — run a finger over it rather than relying on sight, since capacitive surfaces often don't show clearly under interior lighting.

If nothing's in the touchscreen menu and no capacitive surface anywhere on that console, that's worth a call to the dealer to confirm whether your specific build actually got the UG1 Universal Home Remote option — check your window sticker/build sheet for that code to settle it definitively rather than guessing further from photos.

### SCOTT (2026-09-21T21:43)
No garage door or universal home remote.

### CLAUDE (2026-09-21T21:43)
Then it's either not equipped or hidden behind a menu you haven't found. Two things to check before assuming it's missing:

1. **Window sticker/Monroney label** — look for option code **UG1** ("Universal Home Remote, includes garage door opener, programmable"). If your build sheet doesn't have it, it wasn't ordered on your car — possible even though it's often listed as standard, since options vary by exact trim/package configuration.
2. **myCadillac app or Cadillac.com owner portal** — pull up your VIN's build sheet directly; faster and more reliable than digging through paper.

If UG1 isn't on your build: your only paths are an aftermarket universal garage remote clipped to your visor (Chamberlain/Genie make simple ones, ~$30-40), or calling the dealer to ask if the hardware can be added post-sale — unlikely, since HomeLink capacitive modules are typically integrated into the console at the factory, not a retrofit part.

Check the window sticker first — that's the one-minute answer that settles whether you're troubleshooting a real feature or one that was never there.

### SCOTT (2026-09-21T21:44)
Found it.
[File uploaded: photo.jpeg]

### CLAUDE (2026-09-21T21:44)
There it is — it's fully in software via the touchscreen, no physical console buttons at all on this generation. Confirms the feature is equipped and active, just accessed differently than older Cadillacs.

Since you have a physical garage remote: tap **Yes**, then follow the prompt — it'll ask you to hold your existing remote close to the screen/module and press its button while the car "learns" the frequency, same concept as the old button-press method, just walked through on-screen instead.

If Yes doesn't work cleanly, D-Mode vs UR-Mode refers to your garage door opener's own DIP switch or rolling-code setting (check the motor unit in the garage or its manual) — most modern openers (post-2011) use rolling code, which is typically UR-Mode.

### SCOTT (2026-09-23T00:15)
Why you reckon this thing won’t charge?
[File uploaded: 1883b2cceb56ee94e61ef5c28bc9dfc44936c6da.png]
[File uploaded: photo.jpeg]
[File uploaded: photo.jpeg]

### CLAUDE (2026-09-23T00:15)
That's a **Tesla Wall Connector** (not a Supercharger) — solid blue LED means it's powered and idle, not actively charging. The adapter connection in your photo looks fully seated, so this isn't a physical hookup problem.

Most likely cause: this looks like a **shared/commercial installation** (the "EV1" label and separate junction box suggest a business or multi-unit property, not a private home unit). Tesla Wall Connectors in that setting are frequently **locked to authorized accounts** — they won't start a charge for just any vehicle plugged in, Tesla or not. You typically need to either:

1. Be added as an authorized user via the property's Tesla account, or
2. Some units require the **Tesla app** itself (not your Cadillac app) to unlock/start the session, even with the NACS adapter, or
3. There's a physical **unlock/release button** on the connector itself you press before it'll begin — did you press the button on the handle when you plugged in?

Your Cadillac app showing "Connecting to charger..." stuck and not progressing past that screen backs this up — it's not a car-side fault, it's the charger not authorizing the session.

Ask whoever manages that charger (property manager, employer, etc.) whether it's restricted to authorized vehicles/accounts — that's the most likely fix here, not anything on your end.

### SCOTT (2026-09-23T00:18)
It does green lights down and then goes back to blue.

### CLAUDE (2026-09-23T00:18)

This is a known, documented pattern for exactly your situation — non-Tesla EV via NACS adapter on a Tesla Wall Connector. Other owners (Ariya, Nissan) report the identical symptom: green light briefly (charger thinks it's about to start), then reverts to blue (handshake fails, charging never actually begins).

Per Tesla's own troubleshooting table: **solid blue = "connected but vehicle hasn't requested charging"** — this points at a communication handshake issue between the Wall Connector and your Lyriq through the adapter, not a power or physical connection problem.

Try these in order:

1. **Press the button on the Tesla handle itself before/after plugging in** — several owners in the search results only got it working after physically pressing the release button on the connector handle, not just plugging in and waiting.
2. **Unplug fully, wait 30 seconds, replug** — the handshake sometimes needs a fresh attempt.
3. **Check the Tesla app if you have access** — if this is a property-managed unit, someone may need to confirm it's set to "Any electric vehicle" rather than "Authorized Teslas Only" (this was the single most common root cause in the results).
4. If none of that works — this may be a **hardware compatibility gap**: some Gen 3 Wall Connectors don't fully support third-party NACS communication protocols even with the adapter, particularly on older installs. That's a real possibility, not just a settings issue.

Given the "EV1" label and separate junction box, this reads like a shared/managed unit — if steps 1-2 don't fix it, the access-control setting (someone else's account) is the most likely culprit, and that's not something you can fix from your end.

### SCOTT (2026-09-23T00:19)
This is a charger at a hotel.

### CLAUDE (2026-09-23T00:19)
That changes the likely cause — hotel-installed Tesla Wall Connectors are almost always set to **"Authorized Teslas Only"** or tied to a payment/access system managed by hotel staff, not left open to any vehicle. The green-then-blue cycle you're seeing matches that exactly: charger attempts the handshake, doesn't recognize your Lyriq (or the adapter) as authorized, and reverts to idle.

Fastest fix: **call the front desk right now** and ask if the EV charger needs to be activated for your room/reservation — many hotels require you to register your license plate or room number with them before the charger will authorize a non-Tesla vehicle, or they need to flip it from "Teslas only" to "all vehicles" in the app on their end.

If front desk can't help tonight, this may simply not work for you at all — some hotel installs are hard-locked to Tesla VINs only with no override. Don't spend more time on the adapter/car side; the block is almost certainly upstream of what you can control from the vehicle.

### SCOTT (2026-09-28T14:55)
I need some sort of tote for the back of my caddy. Where I can put drinks and stuff. And it not slide around.
[File uploaded: IMG_0997.jpeg]

### CLAUDE (2026-09-28T14:56)

**Get the genuine Cadillac Collapsible Cargo Organizer for the Lyriq** (accessories.cadillac.com or shopchevyparts.com). It's a molded, skid-resistant thermoplastic tote with collapsible dividers, made for the Lyriq's cargo area. I couldn't confirm a current price or 2026 fitment, so check that on the listing.

Your trunk has a rubber all-weather liner, so skip the generic ones with velcro non-slip bottoms. Velcro needs carpet to grip and won't hold on rubber. A skid-resistant base plus a tie-down works better.

- **Best fit:** the Cadillac organizer above.
- **Cheaper backup:** the MugiVSE Lyriq-specific organizer on Amazon. It folds flat and uses hook-and-loop, so it has the same grip problem on rubber. Add the bungee below.
- **Locking it down:** one Lyriq owner on the forums runs bungee cords across the cargo area through the organizer's handles, anchored to the side tie-down points. It also works on any tote you already own.

For drinks, get one with adjustable dividers so the cases don't shift inside it. Your Oikos and milk cases fit in a 32"×13" unit with two dividers.
