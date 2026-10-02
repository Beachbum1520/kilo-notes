# Steer yield calculation for 594 lb hang
Date: 2026-09-17
Conversation: f2cf73a9-6a96-450a-b426-8529708c91f8
Domain: watts-way-farms

## Summary
**Conversation Overview**

This conversation centered on a beef yield dispute involving a Dexter steer with a live weight of 594 lb and a hanging weight of 322 lb (54.2% dressing percentage), processed as two halves at 161 lb each. The person operates a farm beef business and uses a processor referred to as Daniel-Jackson. A return customer named Kim and Greg received 77.34 lb of take-home product from their half, representing a 48% yield against hanging weight — significantly below the farm's previously established and measured 65% yield baseline from prior batches. The person suspected the processor was shorting product; the processor denied any error and offered an invitation to observe future cuts in person, which the person intends to take up.

The conversation involved running multiple refund scenarios at different yield assumptions (65% → ~$284, 59% → ~$202, 54% → ~$120) before Claude conducted web research and located the North American Dexter Cattle Association's breed-specific documentation, which established 55.3% as the documented retail yield for Dexter beef (HW to take-home). At that figure, the calculated refund was ~$143, which the person rounded to $150 as a goodwill gesture. The person also asked Claude to research the weight loss differential between 14-day and 21-day dry aging hangs; research confirmed the difference is approximately 0.5–1% (under 1 lb on a half this size), ruling out hang time as an explanation for the shortfall. The person decided to offer Kim and Greg either a $150 credit toward a future order or cash, and requested a customer-facing message drafted without yield-percentage detail — warm, brief, and acknowledging that the processor claimed no fault while the farm was still making it right.

The person's pricing model is $6.75 per pound of hanging weight. They communicate directly and prefer concise, math-first responses with running comparisons across scenarios. They clarified mid-conversation that handwritten notes on the processor receipt were the customer's own tally, not the processor's documentation, which meaningfully changed the evidentiary read. The person corrected Claude's initial assumption that the farm's confirmed 65% yield was the appropriate baseline, prompting the breed-specific research that produced a more defensible number.

### SCOTT (2026-09-17T12:15)
Search all chats before replying. 

We have a steer that hung for 594. How much yield per half would you estimate in both percentage of hanging weight and total pounds per half.

### CLAUDE (2026-09-17T12:15)

At the farm's confirmed ~65% take-home yield:

- **Whole: ~386 lb** (594 × 0.65)
- **Per half: ~193 lb**

That's a notably heavy hang — well above your typical 475–550 lb band, so this is one of the bigger animals you've sent.

### SCOTT (2026-09-17T12:16)
Correction. Live weight was 594. Hanging weight was 322

### CLAUDE (2026-09-17T12:16)
At ~65% take-home yield:

- **Whole: ~209 lb** (322 × 0.65)
- **Per half: ~105 lb**

That 322 lb hang on a 594 lb live is a 54.2% dressing percentage — on the low side of your Dexter range, well below the 55.2% you've been using for estimates.

### SCOTT (2026-09-17T12:17)
Customer got 77.34 pounds. Processor says that’s right.

### CLAUDE (2026-09-17T12:18)
That's **48.0%** of half hanging weight (77.34 / 161) — not 65%.

That's a big gap from the number you had confirmed as measured across a full batch. Worth flagging before this becomes the new baseline: a single half at 48% could mean:

- **This cut sheet was different** — heavy bone-in, more waste cuts, or something atypical for this customer
- **This animal's meat-to-bone ratio was different** — older, leaner, or different frame than the batch that produced 65%
- **A reporting inconsistency** — is 77.34 lb the full box weight, or does it exclude something (bones taken home separately, a partial pickup, etc.)?

Given the 65% number came from tracking 4-6 animals across a full batch and held consistently, one half at 48% is either a real outlier worth understanding before you quote numbers to other 2026 customers, or there's a measurement mismatch. Do you have the cut sheet for this one, or is this the only data point so far from the current batch?

### SCOTT (2026-09-17T12:18)
I think the processor is fucking us

### CLAUDE (2026-09-17T12:19)
That gap is real and worth chasing down. Some context on why 48% stands out:

- Your measured yield (65%) came from tracking a full batch and held consistently — that's solid data, not a rule of thumb.
- 48% isn't just "on the low end," it's below any normal range. Even a heavy bone-in cut sheet (T-bones, thick roasts, no boneless-everything) typically lands 55-60% minimum. 48% suggests either missing product or a cut sheet nobody would actually choose.

Before assuming the processor is shorting you, a few things to nail down:

1. **Get the itemized cut sheet weights.** Not just the total — every cut, every package. If ground beef, roasts, steaks, and organs don't sum to 77.34 lb, something was miscounted or withheld.
2. **Check if this customer got everything.** Did they pick up in one trip, or could part of the order be sitting at the processor / went to someone else's order by mistake?
3. **Compare against the rest of this batch.** If the other halves from the same steer or same batch also came in around 48%, that's a processor-wide problem on this run. If it's just this one half, it's more likely a specific mix-up (mislabeled boxes, wrong cut sheet applied, partial pickup).
4. **Ask the processor for their scale ticket / breakdown**, not just a verbal "that's right." A number confirmed without documentation isn't confirmed.

Do you have the cut sheet or a breakdown by item for this order, or just the total?

### SCOTT (2026-09-17T12:25)

[File uploaded: 81128390890__6269E5A1-869C-4FB7-A123-860DA7444816.jpeg]
[File uploaded: IMG_4387.jpeg]

### CLAUDE (2026-09-17T12:25)
The receipt confirms it: **Hook ID 2304, half order, hang weight 161 lb** (matches — $159.39 processing ÷ $0.99/lb = 161.0 lb exactly). The whole animal hung 322 lb, live 594 — this is the same steer you've been asking about.

**77.34 / 161 = 48.0%.** That's a real, processor-confirmed number, not an estimate — and it's 17 points below your established 65%.

What that gap means in pounds: at your normal 65%, this half should have yielded **~105 lb**, not 77.34. That's a **~27 lb shortfall** — real money and real product that isn't showing up.

Looking at the itemized cuts on the sheet — ribeye, sirloin, NY, filet, boneless ribeye, chuck, shoulder, brisket — those sum to roughly **30 lb**, which lines up with the "30-34" you'd already scratched out yourself. Ground beef isn't fully itemized on this sheet (only two 1-lb packages shown, with a note that "some chubs not full pound"). That's almost certainly where the gap lives — ground beef and trim are the easiest place for weight to go missing, since they're the last cuts off the carcass and the most susceptible to being shorted or mislabeled.

**Before calling it theft, ask the processor for the ground beef package count and weights specifically** — how many chubs, and the actual weight of each. If GB alone comes in light (say, well under the ~35 lb you'd expect to close the gap), you've got your answer in writing. If the sheet was hand-cut, ground beef poundage is the number that gets rounded down or under-filled most often — worth checking whether "not full pound" chubs were counted as full pounds anywhere in their total.

### SCOTT (2026-09-17T12:27)
The hand written numbers on the itemized is from the customer.

### CLAUDE (2026-09-17T12:27)
Good — that changes the read. So it's the *customer* who wrote "we have: 30-34," "they said: 70 lbs," "GB 35 lbs," and "some of chubs not full pound" — meaning the customer is already doing their own audit and independently flagging the same thing I pointed at: **the ground beef chubs came in light.**

That's a stronger signal than anything Daniel-Jackson wrote. If the customer counted their steaks/roasts at ~30-34 lb (matches the itemized cut list math) and the processor told them GB should be ~35 lb but the actual chubs weren't full pound, that's your ~27 lb gap accounted for almost entirely in one place — ground beef.

Next step: get the actual chub count and weigh them yourself if the customer still has them, or ask the processor for the GB weight ticket specifically (not the total). If chubs were sold/labeled as "1 lb" but running under, that's a documentable shortage — not a "yield is just lower than usual" story. Worth checking this against other customers from the same batch (2305, 2310, 2405) to see if it's isolated to this half or systemic to how they're packaging ground beef right now.

### SCOTT (2026-09-17T12:28)
The processor doesn’t have itemized. What you see is all we got.

### CLAUDE (2026-09-17T12:28)
That means there's no official documentation of *where* the 27 lb went — the processor gives you a total hang weight and a total take-home weight, full stop. Everything else (the "30-34," "GB 35 lbs," "chubs not full pound") is the customer's own tally, not something Daniel-Jackson stands behind.

That's a weaker position than I gave it credit for. Without itemized weights from the processor, you can't point to ground beef specifically and say "that's where it went" — you can only say the *total* is 27 lb short of what your measured 65% would predict. The customer's breakdown is a reasonable hypothesis (GB/chubs are the likeliest place for shortage), but it's not proof, because it's not their scale.

Given the processor doesn't itemize, your only real options:

1. **Ask the customer to actually weigh everything they got** — total it up on a kitchen scale, package by package, and compare to 77.34 lb. If it matches, the shortfall is real and it's on the processor's cut, not a paperwork error on your end.
2. **Ask the processor point-blank whether 77.34 is the true post-cut weight** or an estimate/rounded number — some small processors eyeball totals rather than weighing every package.
3. **Watch the next few halves off this same batch** (2305, 2310, 2405). If they also land well under 65%, that tells you it's this processor/this run, not one bad half.

Without their itemization, you don't have a case to bring to the processor beyond "the math doesn't match what we've measured before" — which is worth raising, but it's a conversation, not an audit.

### SCOTT (2026-09-17T12:30)
1. The customer did weigh. Those are the weights in the sheet I gave you. 

2. The processor says they are perfect. No mistake. 

I need to make this right by the customer even though my processor is a piece of shit. Help me calculate.

### CLAUDE (2026-09-17T12:31)
**~$284 refund (or equivalent credit) makes this customer whole.**

Math:
- Customer paid for hanging weight, all-in: 161 lb × $6.75 = **$1,086.75**
- Your established price-per-take-home-pound, based on 65% yield, is $6.75 ÷ 0.65 = **$10.38/lb**
- What they actually got (77.34 lb) is worth 77.34 × $10.38 = **$802.94** at that standard
- Overpayment: $1,086.75 − $802.94 = **~$283.81**

Same number either way you slice it — expected take-home was 104.65 lb (161 × 0.65), they got 77.34 lb, the 27.3 lb shortfall × $10.38/lb ≈ **$283.60**.

Options to deliver that value:
1. **Cash refund ~$284** — cleanest, no argument later.
2. **Credit toward a future order** — keeps the cash in the business, works if this is a repeat customer.
3. **~27 lb of product from another animal** (ground beef, most flexible cut to pull from freezer stock) — makes them whole in kind rather than dollars, if you have inventory.

Whichever you pick, this is on the processor, not you — worth having this exact number ready when you call them, since "perfect, no mistake" doesn't hold up against your own measured yield history.

### SCOTT (2026-09-17T12:32)
Re run it at 59%

### CLAUDE (2026-09-17T12:32)
**~$202 refund at 59% yield.**

- Expected take-home: 161 lb × 0.59 = **94.99 lb**
- Price per take-home lb: $6.75 ÷ 0.59 = **$11.44/lb**
- Shortfall: 94.99 − 77.34 = **17.65 lb**
- Overpayment: 17.65 × $11.44 ≈ **$201.93**

For reference: 65% → ~$284, 59% → ~$202. The 6-point swing in assumed yield moves the refund by about $82, so it's worth being clear with yourself on which number you're standing behind before you quote it to the customer — 65% is what you've got measured and confirmed across a full batch; 59% would need its own justification if you're using it instead.

### SCOTT (2026-09-17T12:33)
What is at 54%?

### CLAUDE (2026-09-17T12:34)
**~$120 refund at 54% yield.**

- Expected take-home: 161 × 0.54 = **86.94 lb**
- Price per take-home lb: $6.75 ÷ 0.54 = **$12.50/lb**
- Shortfall: 86.94 − 77.34 = **9.6 lb**
- Overpayment: 9.6 × $12.50 = **$120**

Running total across the assumptions: 65% → ~$284, 59% → ~$202, 54% → ~$120. At 54% you're basically saying this half's yield wasn't abnormal at all — it's within shouting distance of the 55.77% dressing percentage you got on cow #911 — which would mean the "processor is screwing us" read doesn't hold up nearly as well as it did at 65%. Worth deciding which yield number you actually believe before picking a refund to offer.

### SCOTT (2026-09-17T12:36)
Just running different scenarios. Can you research and see if you can find any relevant data related to Dexter beef

### CLAUDE (2026-09-17T12:36)

Found a genuinely useful breed-specific source: the North American Dexter Cattle Association's "Raising and Marketing Dexter Beef" (Patti Adams, Wakarusa Ridge Ranch), with real data.

**Key numbers from that source:**

| Metric | Value |
|---|---|
| Live weight (29-mo steer) | 880 lb |
| Hanging weight | 539 lb (61.2% of live) |
| **Total retail product** | **298 lb = 55.3% of HW** |
| Breakdown | Chuck 54 lb, Rib 31 lb, Loin 51 lb, Round 48 lb, 85% lean ground 114 lb |

They also cite a 2002 Oklahoma State feed-out study of **30 grain-finished Dexter steers**: average dressing % (HW/live) was **53.7%**, ranging 41.6%–57.8%.

**What this means for your number:**

- **55.3% is the documented Dexter-specific retail yield** (HW → take-home), not the generic 65% commercial-beef rule of thumb you've been using. That's a big gap — 65% appears to be a mixed/commercial-breed average, while Dexters, being small-framed with proportionally more bone and organ weight in the hanging carcass, cut out lower.
- Your own processor-confirmed 65% batch data (2309, 2307, 2311, 2308 from earlier) still stands as *your* measured number on *your* animals — that doesn't get overridden by a general industry source. But it does mean 65% may be an unusually good number, possibly reflecting a favorable cut sheet (more bone-in) on that batch, not the Dexter norm.
- At **55.3%**, this half (161 lb hanging) should yield **~89 lb** — customer got 77.34 lb, a **~13% shortfall**, not the 26% shortfall implied by your 65% baseline.

This doesn't clear the processor, but it does mean the refund math using 65% was probably too aggressive an ask. **55%** is a defensible, citable, breed-specific number if you want documentation to point to rather than your own batch history (which the processor could just as easily dismiss as "not our animals, not our data").

### SCOTT (2026-09-17T12:37)
So based on the 55.3%. What is it

### CLAUDE (2026-09-17T12:37)
**~$143 refund at 55.3% yield.**

- Expected take-home: 161 × 0.553 = **89.03 lb**
- Price per take-home lb: $6.75 ÷ 0.553 = **$12.21/lb**
- Shortfall: 89.03 − 77.34 = **11.69 lb**
- Overpayment: 11.69 × $12.21 ≈ **$142.77**

Running tally: 65% → ~$284, 59% → ~$202, 55.3% (Dexter Cattle Association documented) → **~$143**, 54% → ~$120.

### SCOTT (2026-09-17T12:40)
Is that yield based on a 21 day hang?

### CLAUDE (2026-09-17T12:40)
Not stated for that specific example. The source's "Dry Aging" section says dry-aged Dexter beef is typically hung **14–28 days**, but that's presented as general practice guidance elsewhere in the deck — the 880 lb live / 539 lb HW / 298 lb retail (55.3%) example doesn't have a hang time attached to it in the source.

Worth knowing why it matters: another source I pulled (Oklahoma State Extension) notes chilled carcass weight runs **2–5% below hot hanging weight** just from moisture loss during aging — separate from what gets removed in cutting. If Daniel-Jackson's "hanging weight" on your receipt is the hot weight (typical for small custom processors) and they hung this animal 21 days, some of that 55.3%-vs-77.34lb gap could be ordinary aging shrink rather than a cutting/yield issue — you'd expect a longer hang to trend the take-home percentage down, not up.

So: I can't tell you whether the 55.3% figure assumes a comparable hang time to what you got on this steer. If you want a number you can stand behind, ask the processor directly how many days this carcass hung — that's the piece that would let you compare apples to apples against the Dexter Association's example instead of guessing.

### SCOTT (2026-09-17T12:41)
I just have a pissed off customer, who is a return customer, who feels she was shorted.

### CLAUDE (2026-09-17T12:42)
**Refund ~$150, framed as a credit toward her next order (or cash if she pushes) — round up from the $143 floor.**

Reasoning:
- $143 (55.3% Dexter-documented yield) is the number you can actually defend if anyone ever asks "how'd you get there" — it's not your batch history, not the processor's assertion, not her hypothesis. It's the floor.
- The processor won't move ("perfect, no mistake"), so whatever you give her comes out of your pocket regardless of which yield number is "true." That makes this a retention decision, not a forensic-accuracy one.
- $150 is a clean, round, slightly-generous number above the defensible floor. For a return customer, the gap between $143 and $150 is trivial money and buys you not looking like you nickel-and-dimed the yield math to the penny.
- Store credit protects margin (she spends it on more of your beef) vs. cash out the door. Offer credit first; if she wants cash, give cash — don't fight a pissed-off repeat customer over the delivery mechanism.

Want me to draft the message to her? Short, no yield-percentage lecture — just acknowledge she got less than expected, name the number, and make it right.

### SCOTT (2026-09-17T12:44)
Give me a brief message to give to this customer. Tell her we have spoken with the processor and he claims no foul and even invited me to come watch them cut next time which I intend to do.

### CLAUDE (2026-09-17T12:44)

Swap in her name and the payout method before sending.

### SCOTT (2026-09-17T12:44)
Customers name is Kim and Greg. Offer them credit or cash

### CLAUDE (2026-09-17T12:44)

Ready to send.

### SCOTT (2026-09-17T12:44)
Message ain’t consign through.

### CLAUDE (2026-09-17T12:44)
Here it is as plain text — copy/paste directly:

---

Hi Kim and Greg, I wanted to follow up on your half beef order. I hear you on the yield feeling off, and I take that seriously — you're return customers and I want you to feel good about every order.

I spoke with the processor directly. They're standing firm that the cut and weight were correct, no mistake on their end. That said, I'm not going to just leave it there — I've asked to come watch them cut next time so I can see the process myself and make sure everything's right going forward.

In the meantime, I'd like to make this right for you: I'll credit $150 toward your next order, or send cash instead — whichever works better for you. Thank you for bearing with me on this, and for being loyal customers — it means a lot.

### SCOTT (2026-09-17T12:48)
How much would you estimate the weight loss to be on a 21 day hang vs 14 day

### CLAUDE (2026-09-17T12:48)

**Roughly 0.5–1% additional weight loss for a 21-day hang vs. 14 days — a small difference, not a big one.**

The research is consistent on this: most carcass weight loss happens in the first 2-3 days, then it flattens out to a slow trickle.

- **OK State Extension:** 14-day hang shrink runs **5–7%** of carcass weight (30-40 lb on a 600 lb carcass) a carcass can lose on average 5-7% of the total weight from aging, which relates to 30-40lbs on a 600lb carcass.
- **SDSU Meat Lab study** (closest to your real-world custom-processor scenario, not restaurant-style dry-aging): the greatest change in carcass weight occurs from day 0 to day 3, and subsequently carcasses lost approximately 0.1% of initial weight each day from day 4 to 21. Over the full 21 days, each side lost 16 to 23 pounds — roughly 32 to 46 pounds per whole carcass.

Doing the math off that 0.1%/day rate: the extra 7 days (day 14 → day 21) adds only about **0.7 percentage points** of shrink on top of whatever's already lost by day 14. So on your 161 lb half, that's roughly **~1 lb** difference between a 14-day and 21-day hang — noise, not the explanation for a 27 lb gap.

**Bottom line for your dispute:** aging duration is not where the missing weight went. Whether Daniel-Jackson hung this 14 or 21 days, the difference is under a pound on a half this size. If they're citing a longer hang as their explanation for the shortfall, that doesn't hold up against the data.
