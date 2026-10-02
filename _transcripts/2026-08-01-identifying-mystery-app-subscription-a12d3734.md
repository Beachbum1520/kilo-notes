# Identifying mystery app subscription
Date: 2026-08-01
Conversation: a12d3734-9534-482a-a742-60b12708e1a5
Domain: skip

## Summary
**Conversation Overview**

Scott was auditing recurring charges on his card and asked Claude to help identify and cancel several subscriptions. The conversation began with Claude identifying a subscription by its app icon as Fitbod, a workout programming app. Scott canceled it, then corrected Claude's outdated memory note that assumed Fitbod was still driving his lift programming — he indicated he had moved well beyond that tool and Claude updated its notes accordingly.

Scott then asked about whether charges appearing as "AplPay" on statements are manageable through iOS Subscriptions. Claude clarified the distinction: Apple Pay is a payment rail, not a billing relationship, meaning merchant-billed charges post under the merchant's name and never appear in Settings → Subscriptions. This distinction became practically important as Scott identified two charges — Soundiiz and Primal — that were merchant-billed and therefore invisible to an iOS subscription audit. Soundiiz turned out to be a playlist migration service Scott had used once roughly a year prior and forgotten about; Claude directed him to cancel via their web account settings. Primal was identified as an AI entertainment product; their in-app account screen provided no cancellation control, only a retention button. Claude drafted two email cancellation options for Scott to send to support@getprimal.app, advised him to screenshot the lack of a cancel control as evidence, and explained that if charged again he could dispute with his card issuer and request the merchant be blocked at the network level. Scott's working pattern across this conversation was direct and practical — he wanted identification, action steps, and drafts without extended explanation. He pushed back clearly when Claude operated on stale context, which Claude incorporated immediately.

### SCOTT (2026-08-01T13:03)
Any idea what this is?
[File uploaded: IMG_9343.png]

### CLAUDE (2026-08-01T13:04)
Looking at the subscription details in the screenshot—a purple app icon with a yellow-green droplet shape, showing a $89.99/year premium subscription—I'm trying to identify which app this is. The icon design doesn't immediately match the apps I'm thinking of, so I'm working through possibilities like Waterllama, Fabulous, or Oura, though none seem quite right based on their typical icon designs.

Since the app name isn't visible in the subscription management screen itself, the most reliable way to identify it would be to check the App Store account settings where the full app name appears next to the subscription, or look at the receipt email from Apple. The icon does suggest it could be a hydration or health-tracking app given the droplet imagery, but I can't pinpoint it with certainty from the visual alone. I'm running through more subscription apps with similar pricing and icon styles — TrainerRoad at $189, Strava at $79.99 with its orange icon, various fitness and plant tracking apps. The purple square with yellow droplet is tricky; I'm considering whether it could be a hydration or plant-related app, but none of the obvious candidates quite fit the visual description.

Without seeing the app name directly on the subscription screen, I can't definitively identify it. The most reliable way to confirm would be checking the App Store subscriptions list, the device settings, or looking at Apple receipt emails, which would all show the actual app name.

Fitbod's icon is a purple gradient square with a lime-green droplet or flame shape, and the Elite subscription costs around $79.99 to $89.99 per year depending on current pricing.That's Apple's "Manage Subscription" screen, and the header is showing the plan name ("Premium") rather than the app name — which is why it's not obvious.

The icon is the giveaway: purple gradient tile with a lime droplet/flame is Fitbod. $89.99/yr matches their current annual tier, and it'll auto-renew Nov 6 unless you cancel.

To confirm: App Store → tap your profile photo → Subscriptions. That list shows actual app names, so you can match the Nov 6 renewal to the right one.

### SCOTT (2026-08-01T13:05)
Fitbod. Good to know. Canceled

### CLAUDE (2026-08-01T13:05)
Scott canceled his Fitbod subscription, which affects his training setup since he relies on it to determine his lifts. I should update the memory note to reflect this change and flag the access expiration date of November 6th. This also has downstream implications for his lifting programming since Fitbod is a key part of how he structures his workouts.

Worth thinking through before November 6, since Fitbod has been the thing generating your lifts — I've just been labeling the Push/Pull/Legs split and adding accessories on top of what it prescribes.

Three options as that access lapses:

- **Fixed program.** Pick a proven template (5/3/1, GZCLP, a simple PPL) and run it. More durable than Fitbod's day-to-day autoregulation, and it costs nothing — but you lose the auto-adjustment around heavy run weeks.
- **Let me generate the lifts.** I can build the sessions directly instead of relabeling Fitbod's, with the advantage of actually accounting for your run load and cold plunge timing, which Fitbod never saw.
- **Re-subscribe before Nov 6.** Only worth it if the exercise-selection variety is what you valued, rather than the tracking.

Given a sub-4 target, lifting should be subordinate to the run block anyway — Fitbod optimizes for hypertrophy progression, not for staying fresh on quality run days. Cancelling may be an improvement, not just a cost cut.

### SCOTT (2026-08-01T13:07)
Stop. You don’t know what you’re talking about. We have way moved up from Fitbod.

### CLAUDE (2026-08-01T13:07)
Scott's pointing out that my memory on Fitbod is outdated — he's moved well beyond that tool. I need to update my notes to remove that stale reference and mark it as no longer relevant, rather than guessing what he's using now.

Let me ask what his current lift tracking source is so I can get that on record.

Fair — I built that on a stale note and should have checked it against you first rather than running with it.

What's driving the lifts now?

### SCOTT (2026-08-01T13:08)
Is it fair to say that any charge that shows up as AplPay is managed through my subscriptions?
[File uploaded: IMG_9342.PNG]

### CLAUDE (2026-08-01T13:08)
So "AplPay" just indicates Apple Pay was the payment method used, not that it's managed through Apple's subscription system. The actual subscription billing comes through the merchant directly—in this case, Soundiiz charged via Apple Pay on their web platform, which is why it shows the merchant location in France rather than Apple's billing infrastructure.No — those are two different things.

"AplPay" on a statement just means the card was tokenized through Apple Pay at checkout. The merchant (Soundiiz, billing out of Couëron, France) charged your card directly. Apple was the payment rail, not the biller.

Apple-billed subscriptions — the ones you can cancel in Settings → Subscriptions — post as **APPLE.COM/BILL** or **Apple Services**, never as the merchant's name. The Fitbod one was that type. This one isn't.

Practical consequence: recurring charges like this are invisible in your iOS subscription list, so they won't get caught in an audit there. To stop Soundiiz, log into their site and cancel in your account settings.

### SCOTT (2026-08-01T13:16)
What is soundiiz?

### CLAUDE (2026-08-01T13:17)
Soundiiz transfers playlists and music libraries across streaming platforms like Spotify, Apple Music, YouTube Music, and Tidal, with a monthly premium subscription around $5.Soundiiz is a music playlist migration service — it transfers playlists, albums, and followed artists between streaming platforms (Spotify, Apple Music, YouTube Music, Tidal, Deezer, etc.), and can keep playlists synced across two services on an ongoing basis.

The $5.00 is their Premium tier, billed monthly. The statement string "PREMCOUERON L/" is just "Prem" plus Couëron, the French town where the company is based.

Two things worth checking: whether you actually still need it (most people subscribe for a one-time library move, then forget it), and whether it's still holding OAuth access to your streaming accounts. If you cancel, revoke Soundiiz in each platform's connected-apps settings too.

### SCOTT (2026-08-01T13:17)
Yup. That was me. So tell me where to go to cancel.

### CLAUDE (2026-08-01T13:17)
I'm thinking through how to help with canceling Soundiiz — it's billed directly by the merchant, so the process involves logging into soundiiz.com, navigating to account or subscription settings, and canceling from there. If they're billed through a payment processor like Paddle or Stripe, the cancellation link might be in their receipt email instead. I'm considering whether I should search to verify the exact current process for this specific service.

On soundiiz.com (web, logged in):

1. Settings icon next to your username, top of the left panel
2. **Plan** in the left list
3. **Cancel** → confirm

Premium access runs through the end of the current billing cycle, and they don't issue refunds once a paid feature has been used. Cancellation also needs to land at least 72 hours before the period ends to take effect that cycle — since the charge hit Jul 26, do it well before Aug 26.

Two gotchas: any active syncs get disabled when the subscription ends, and their execution history is deleted — so export anything you want to keep first. And if the login email doesn't show a Premium plan, search your inbox for a Stripe receipt to find which email the paid account is under.

### SCOTT (2026-08-01T13:19)
FML. I signed up for that around a year ago and used it once. Only $5 a month but shit. Still sucks.

### CLAUDE (2026-08-01T13:20)
I should keep this brief and practical—he's already found two wasted subscriptions, so a lecture isn't helpful. The Soundiiz and Fitbod cancellations aren't worth documenting since they're already handled. The real value is pointing him toward merchant-billed recurring charges that won't show up in iOS subscriptions, which is a concrete next step he can actually take.$60 for one playlist migration. Annoying, but the real lesson is the category, not the $60.

You just found two of these in one sitting — and the Soundiiz type is the dangerous one, because merchant-billed charges never appear in your iOS subscription list. Nothing prompts you to review them. That's how a one-time-use tool bills for twelve months.

Worth 20 minutes: pull the last 12 statements on that card and sort by amount. Recurring charges under $15 are where the leaks hide — you don't notice them individually, and they don't trigger the "should I still be paying for this?" reflex the way a $90 hit does. Anything you don't recognize on sight, you're almost certainly not using.

### SCOTT (2026-08-01T13:24)
Help me figure out this one.
[File uploaded: IMG_9346.PNG]

### CLAUDE (2026-08-01T13:25)
I'm searching for information about primalstudios.ai to identify it, though the amount details aren't visible in what I can see.

I'm checking out primalstudios.ai to understand what PRIMAL AI actually does — the initial fetch showed mostly hiring content, but they're recruiting for "AI Filmmakers" roles, so it's likely an AI video or filmmaking platform. Let me pull the full site to see if there's a consumer product behind the hiring page.

The corporate website is minimal with no clear product name, so the charge from Primal AI Inc in San Francisco doesn't immediately reveal what they actually sell. Their consumer product might be listed under a different name in the App Store, possibly an AI entertainment app with a subscription model. I'm trying to figure out what product they're actually charging for based on the merchant name alone.

The corporate site doesn't list a specific product, so I need to figure out what Scott actually purchased. The best approach is to look for the merchant details and trace the transaction — checking his email for a receipt from Stripe or the merchant, the phone number on the card statement, or any apps installed on his phone. The LA area code (310) 897-0666 is a mobile number, which is unusual for a merchant descriptor, but probably not significant. I should search his email for "Primal" receipts and remember this was billed directly by the merchant, not through the App Store.The merchant is PRIMAL AI, Inc. (SF) — a self-described new kind of entertainment studio, a small team of Hollywood and gaming veterans working on new entertainment formats. Their site is essentially a hiring page: no named product, no pricing, no login. That's typical of a company whose consumer app ships under a different brand than the corporate entity.

So the descriptor tells you who got paid, not what you bought. Fastest way to close the gap:

- Search your email for "Primal" — a Stripe or merchant receipt will name the actual product and give you the account email
- Check for a recent app install around the charge date; the App Store listing will show the developer as Primal AI, Inc.
- (310) 897-0666 is on the record as their contact number if the paper trail comes up empty

Same structure as Soundiiz: Apple Pay was the rail, so this bills direct and won't appear in Settings → Subscriptions. Worth confirming from the receipt whether it's recurring or one-time before you decide anything.

### SCOTT (2026-08-01T13:29)
Ain’t this some bullshit. Go through the cancel options and this is all you get.
[File uploaded: 96f00b979f13de47de03b3657d539dbb4a980e9f.png]

### CLAUDE (2026-08-01T13:30)
Scott's stuck in a dark-pattern cancellation flow with no visible cancel button, just options to keep his founder status. I'm helping him navigate this by drafting a clear cancellation email to support@getprimal.app that creates a documented record, and since his subscription is merchant-billed through Apple Pay on an Amex card, he can also revoke the merchant's payment authorization directly if the email approach stalls.

The FTC's 2024 Negative Option Rule was vacated by the 8th Circuit in July 2025, so that legal leverage is uncertain now—but state laws like California's still require an online cancellation mechanism. His strongest practical move is contacting Amex to block recurring charges from this merchant; Amex has a "cancel recurring payments" process where they'll request the merchant stop billing. The strategy: send the cancellation email, keep proof of it, then if he gets charged again, dispute it with Amex and request they block future charges from Primal.

I should draft a couple of email variants for him—one firm and direct, another that references the dispute option if they don't comply. I'll also note that screenshotting the app's lack of a cancel button gives him evidence for any dispute claim.Classic. No cancel control anywhere, just a retention button and an email address — the burden shifted onto you deliberately.

How to close it out so it actually sticks:

1. **Screenshot what you're looking at** — the Account screen with no cancel option. That's your evidence if you end up disputing.
2. **Email support@getprimal.app** with an unambiguous cancellation request, dated. Don't ask a question; state an instruction. Keep the sent copy.
3. **If they charge you again**, call Amex, dispute it as a cancelled recurring transaction, and ask them to block future charges from that merchant. Amex can do that at the network level regardless of what Primal does — your email is the proof you cancelled.

Here's the email:

Send it from whatever address the account is under — a mismatch gives them an easy reason to stall.
