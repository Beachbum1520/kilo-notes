# Whole hog pricing and hanging weight details
Date: 2026-09-16
Conversation: ebfa35bf-5493-4168-a574-7bb6793d2fbf
Domain: watts-way-farms

## Summary
**Conversation Overview**

This conversation focused on pork pricing, actual hanging weight data, and developing standard customer-facing language for whole hog sales. The person runs a pasture-raised livestock operation and was preparing to quote a customer on a whole hog purchase. They use hanging weight (HW) pricing at $5.50/lb all-in, with processing done through Resaca. The person directed Claude to search prior conversations for actual processed batch data, update memory records to replace outdated estimates with real figures, and develop finalized customer messaging.

The actual hanging weight data on record comes from a single April 2026 Resaca batch (invoice #2801), covering four physical hogs: a runt at 129 lb HW, one hog split into two half orders (Orders #22 and #23, 115 lb each side, customers Watts and Bruce/Sheila Thomas), Peter and Amy Karr's whole hog at 204 lb HW/155.73 lb take-home, and Amanda Burnum's whole hog at 241 lb HW/201.85 lb take-home. Excluding the runt, hanging weights ran 204–241 lb. The person confirmed the decision to stick with per-pound hanging weight pricing after reviewing actual cost-per-take-home-pound figures across the three non-runt whole/combined orders. A flat fee was considered and rejected due to weight variance between animals.

A key policy decision was made: the all-in $5.50/lb price includes curing and smoking on up to 20 lb per half (40 lb per whole), with additional cure/smoke beyond that potentially carrying an extra per-pound charge. Claude drafted the full standard customer pricing message incorporating this cap, saved it to memory, and produced a plain .txt file for easy mobile copying after the formatted version caused copy issues. The person corrected Claude mid-conversation when a "customer wants all brats" interpretation was wrong — the actual concern was protecting margin against excessive cure/smoke requests, not sausage volume. The person also explicitly instructed Claude not to forget the finalized pricing message language in future sessions.

**Tool Knowledge**

Memory updates in this conversation used `memory_str_replace` with `if_version` parameter, which requires the current version hash to succeed — two separate updates were made as the hash changed between edits. Conversation search used multiple distinct query phrasings in sequence (invoice terms, weight terms, customer name terms, processing event terms) because single searches returned incomplete results; the full hanging weight picture only emerged after four separate searches with different terminology. The person's key memory file paths are `/projects/019d7227-50e5-759a-81b0-a4476c2309b1/overview.md` and `/projects/019d7227-50e5-759a-81b0-a4476c2309b1/operating-knowledge.md`. File output for easy mobile copying was handled via `/mnt/user-data/outputs/` as a plain `.txt` file, which resolved a formatting/copy issue the person encountered with the in-chat formatted version.

### SCOTT (2026-09-16T00:28)
Search all chats and get all details around pigs hanging weight and final cost to customer. Have a customer that wants a whole hog and wants to know how much to set aside.

### CLAUDE (2026-09-16T00:28)

**Pork whole hog — quote for the customer:**

- **Price:** $5.50/lb hanging weight, all-in (kill, cut & wrap, vacuum seal, frozen — no back-end fees)
- **Typical hanging weight:** 200–240 lb (actual recent batch data ranged 115–241 lb per animal; full-size hogs cluster 200–240 lb)
- **Whole hog cost range: ~$1,100–$1,320**
- **Take-home:** ~78–84% of hanging weight (running well above the generic 65–70% industry figure — customers who keep fat, hocks, jowls, leaf fat see the higher end)
- **Process:** 50% deposit reserves the spot → cut sheet sent after deposit → customize cuts (bacon, ham, chops, ribs, sausage, ground, roasts, etc.)

So tell the customer to set aside **$1,100–$1,320** for a whole hog, refundable estimate firming up once the animal is actually on the rail.

One flag: your master memory card still lists HW as 220–240 lb / take-home ~180–200 lb (an [ESTIMATE]), but actual processed batches from your chats ran a wider 115–241 lb band with better yield (78–84%, not 65–70%). Worth updating the card with that real data if it hasn't been folded in yet.

### SCOTT (2026-09-16T00:29)
Update the card with the real data. Forget the estimates. Give me a list of all the actual hanging weights you have.

### CLAUDE (2026-09-16T00:30)

Saved. Here's everything I've got.

**All actual pig hanging weights on record** (Apr 2026 batch, Resaca invoice #2801 — the only processed-batch data that exists in your history):

| Pig | Customer | Hang weight | Take-home | Yield |
|---|---|---|---|---|
| #1 | Runt (whole) | 129 lb | 109.44 lb | 85% |
| #2 | Watts + Bruce/Sheila Thomas (split halves) | 230 lb combined | ~202 lb | 88% |
| #3 | Peter & Amy Karr (whole) | 204 lb | 155.73 lb | 76% |
| #4 | Amanda Burnum (whole) | 241 lb | 201.85 lb | 84% |

**Excluding the runt:** hang weights ran 204–241 lb (avg 225 lb), take-home yield averaged ~79% (range 76–84%) — well above the generic 65–70% industry figure.

I've updated the operating-knowledge file to replace the old 220–240 lb HW / 180–200 lb take-home *estimate* with this actual data. Two things to flag:

1. This is one batch, four hogs. It's real data, not a large sample — I'd call it "actual results, small sample" rather than a settled long-run average until you've got a second batch to compare against.
2. This is my memory store, not the Google Doc the master card mirrors — if you want the card itself (and the Herd Inventory workbook) updated, you'll need to paste this into the doc directly, since I can't write back to it from here.

### SCOTT (2026-09-16T00:30)
You should have more than those 4.

### CLAUDE (2026-09-16T00:31)

I ran several more searches (different terms, different date ranges) and this is genuinely all the actual processed-batch data that exists in your chat history — it's one batch, but I found more precision on it than I gave you last time. The "230 lb combined" figure was two separate order records that get more specific:

**Apr 2026 batch — Resaca invoice #2801 (the only actual processed-batch data in your chats):**

| Order | Customer | Hang weight | Take-home | Yield |
|---|---|---|---|---|
| #1 | Runt (whole) | 129 lb | 109.44 lb | 85% |
| #22 | Watts (half) | 115 lb | 105.6 lb | 92% |
| #23 | Bruce & Sheila Thomas (half) | 115 lb | 96.4 lb | 84% |
| #3 | Peter & Amy Karr (whole) | 204 lb | 155.73 lb | 76% |
| #4 | Amanda Burnum (whole) | 241 lb | 201.85 lb | 84% |

That's still 4 physical hogs (5 orders, since #22/#23 are the two halves of one animal) — no additional batch turned up despite searching under invoice numbers, roaster processing, cut-sheet terms, and later 2026 dates. The roaster-pig conversations (Willow's litter, the cryptorchid boar, the $80/head roaster pricing) are all projections and planning — I never found a chat where you reported back actual roaster hanging weights after they were processed.

Two honest possibilities: either that's genuinely the only batch you've discussed with me, or you have more processing data that lives in photos/yield sheets you shared but that a search on these terms isn't surfacing. If you have another batch's numbers handy, send them and I'll add them.

I've updated the memory file with the corrected per-half breakdown (115/105.6 and 115/96.4 instead of the vaguer 230/202 combined).

### SCOTT (2026-09-16T00:32)
What do you think of us moving to a flat fee for a whole pig?

### CLAUDE (2026-09-16T00:32)
**Short answer: no — the actual weight data argues against it.**

Your own numbers show why. Whole hogs (excluding the runt) ran 204–241 lb hanging weight — an 18% spread on hang weight alone, and that's from just 2 animals. At $5.50/lb, that's $1,122 vs $1,325.50 — a $203 gap on animals both sold as "whole hog."

A flat fee forces you to pick a number, and either way you lose:
- **Price it at the heavy end (~$1,325):** light animals cost you nothing extra to overcharge for, but you're now selling a 204 lb hog for the price of a 241 lb hog. That's a trust problem the first time a customer compares notes with someone who got a bigger pig for the same money.
- **Price it at the light end (~$1,122) or the average (~$1,224):** you're giving away real product on every heavy animal. Your marginal cost per pound is just processing ($1.15/lb) — you're pricing meat at $5.50/lb, so every pound above your flat-fee assumption is basically pure margin you're handing back for free.

The per-lb model exists specifically to transfer weight variance risk to a price mechanism instead of to you or the customer eating a bad number. You'd be reintroducing the exact problem hanging-weight pricing solves — and you already know this, because that's the reasoning you settled on for beef and pork both.

**Where flat pricing *does* make sense for you:** roasters. You already moved that way ($80 flat processing, $350 flat retail) — because roasters are young, narrow-window animals with much tighter weight variance than a full grow-out hog. That's the right use case for flat fee: low variance, low stakes per animal. Whole hogs at 6+ months don't have that property.

**If the motive is simplifying the sales conversation** (not actually changing margin exposure), the fix isn't a flat fee — it's quoting a tight, believable range up front ("whole hogs run $1,100–$1,325, billed at $5.50/lb on the actual hang weight") and billing per-lb at the end like you already do. That gets you the simple pitch without eating the variance.

What's actually driving the ask — is a customer pushing back on not knowing the number until after processing, or is this about making your own sales copy easier to write?

### SCOTT (2026-09-16T00:33)
Give me a list of hanging weight and total cost only. Nothing else. Don’t include runt.

### CLAUDE (2026-09-16T00:33)
- 115 lb — $632.50
- 115 lb — $632.50
- 204 lb — $1,122.00
- 241 lb — $1,325.50

### SCOTT (2026-09-16T00:33)
Combine the two half

### CLAUDE (2026-09-16T00:33)
- 230 lb — $1,265.00
- 204 lb — $1,122.00
- 241 lb — $1,325.50

### SCOTT (2026-09-16T00:35)
What does that work out to be for price per pound for take home yield

### CLAUDE (2026-09-16T00:35)
- 230 lb → 202 lb take-home → $6.26/lb
- 204 lb → 155.73 lb take-home → $7.20/lb
- 241 lb → 201.85 lb take-home → $6.57/lb

### SCOTT (2026-09-16T00:43)
Ok. We will stick to hanging weight. What was the language we used in the past for the standard amount of curing included.

### CLAUDE (2026-09-16T00:43)
The language you settled on and used repeatedly in customer replies:

**"$5.50/lb hanging weight, all-in — that price includes everything: processing into retail-style cuts to your specifications, vacuum sealing, and deep freezing at the processor at zero degrees or below, so the meat will basically last forever in your freezer."**

And the master card's shorthand version for curing specifically: **"processing included (smoking, curing, bacon/hams/brats — no upcharge)."**

### SCOTT (2026-09-16T00:44)
We had something we used in case a person said they wanted all brats.

### CLAUDE (2026-09-16T00:44)

I searched several angles (customer-facing copy, cut-sheet strategy, processor ratio limits) and couldn't find a chat where you and I settled on specific customer-facing language for a "wants everything as brats" request. I don't want to make up wording and hand it to you as if it's the phrase you've used before.

Two honest options:
1. If you have the actual wording saved somewhere else (a saved reply, a text you sent), paste it and I'll get it into memory correctly.
2. If you want, I can draft new language now for that scenario (e.g., explaining that a cut sheet can be brat-heavy but a processor can't turn 100% of an animal into sausage/brats — there's a practical max ratio) — just tell me and I'll write it.

### SCOTT (2026-09-16T00:44)
Draft new

### CLAUDE (2026-09-16T00:45)
Here's draft language for that scenario:

---

**Short version (for a quick reply):**

"We can load your cut sheet heavy on brats, but a processor can't turn the entire hog into sausage — some of the animal (bone-in cuts, fat ratios) has to come out as standard cuts for the sausage itself to grind and stuff correctly. We can max out brats and sausage on everything that *can* go that way and keep the rest to a minimum — happy to build you a brat-forward cut sheet."

**Longer version (if they push back or ask why):**

"Totally get the appeal — brats are our most popular item too. The limit isn't us, it's how sausage actually works: it needs the right lean-to-fat ratio, and there's only so much trim and shoulder meat on one hog to hit that ratio. We can't stuff a rib or a whole ham into a casing. What we can do is grind everything grindable — shoulder, trim, odd cuts — into brats and sausage, and keep chops/ribs/bacon to the bare minimum you're comfortable with. That'll get you a hog that's 70–80% brats and sausage, which is about as far as it goes."

---

Both keep it factual (yield ratio problem, not a preference of ours) and steer them toward the maxed-out-brat cut sheet rather than a flat "no." Want me to save one of these to memory as the standard reply?

### SCOTT (2026-09-16T00:46)
No. No. No. Customer is not saying they want all brats. I am saying we need to say something that the price is processing and included but only cover reasonable vire and smoke. Maybe whatever normal is for our avg log size. Maybe we say up to xx poinds incoiddd.

### CLAUDE (2026-09-16T00:46)

No prior instance of that language exists — I searched and this is a new policy you're proposing, not something we've said before. Here's a draft, using your own batch data to anchor a real number instead of a vague "reasonable":

**Draft clause:**

"Price includes standard processing: cutting, wrapping, and vacuum sealing, plus curing and smoking on up to [X] lbs of ham and bacon per [whole/half] hog — in line with what a typical hog yields. Requests for cure/smoke beyond that amount may carry an additional per-pound charge."

**Why a number, not "reasonable":** "Reasonable" is unenforceable — you and a customer can disagree about what's reasonable after the fact, and by then the hog's already at the processor. A number is enforceable at cut-sheet time.

**What number to use:** Your actual last batch ran ~7 ham packages (~14.7 lb) + ~7 bacon packages (~7.4 lb) per half — call it ~22 lb cured/smoked per half, ~44 lb per whole. That's not a guess, it's what a normal hog on your own processing sheet produced. I'd round it to something clean like **20 lb per half / 40 lb per whole** as your included allowance.

**Why this matters cost-wise:** cure & smoke runs ~$1.95/lb at Resaca on top of standard cut & wrap — plus 25–30% yield loss on top of that. A customer who cures/smokes way more than a normal hog's worth (e.g., turning most of the shoulder/loin into ham-style cuts) is quietly pushing processing cost above what your $5.50/lb all-in price assumes. The cap protects your margin without you having to say no in the moment.

Want me to fold this into the standard customer pricing language we already have, or keep it as a separate line only used when someone's cut sheet looks unusual?

### SCOTT (2026-09-16T00:47)
Go with this :  20 lb per half / 40 lb per whole 

Give me the entire message. And don’t forget it this time.

### CLAUDE (2026-09-16T00:47)
**Standard Pork Pricing Message (with cure/smoke cap):**

---

Our pasture-raised hogs are **$5.50/lb hanging weight, all-in** — that price includes everything: processing into retail-style cuts to your specifications, vacuum sealing, and deep freezing at the processor at zero degrees or below, so the meat will basically last forever in your freezer.

This includes curing and smoking on up to **20 lb of ham and bacon per half (40 lb per whole)** — in line with what a typical hog yields. Cure/smoke requests beyond that amount may carry an additional per-pound charge.

Our hogs typically hang between 200–240 lbs, so estimated totals are:

- **Whole hog:** ~$1,100–$1,320
- **Half hog:** ~$550–$660

You'll fill out a cut sheet to customize exactly what you want — bacon, sausage, chops, ribs, roasts, ground, etc. A deposit reserves your spot, and we'll send the cut sheet once it's received. Pickup is at the processor or an arranged meetup along the Atlanta–Montgomery corridor.

---

Saved to memory now.

Done — the cure/smoke cap and the full standard pricing message are saved. I'll pull it verbatim next time instead of you having to re-supply it.

### SCOTT (2026-09-16T00:49)
Fucking message ain’t copying right. Give it to me as a card I can easy copy

### CLAUDE (2026-09-16T00:49)

Below — plain .txt file, should copy clean on mobile.
