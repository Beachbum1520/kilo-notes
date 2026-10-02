# Selling Willow's piglet litter
Date: 2026-08-11
Conversation: cf340743-ca18-481a-a296-23f6a4db7e55
Domain: watts-way-farms

## Summary
**Conversation Overview**

Scott operates Watts Way Farms in Franklin, GA and asked Claude to help create and manage Facebook sales posts for two distinct product lines: Willow's current piglet litter and a group of breeding stock sows and gilts. The piglet post covers Willow's Berkshire/Duroc cross litter born July 25, 2026 — 5 barrows and 4 gilts — priced at $150 each or $125 each for five or more, with a September 5 pickup date. The AI sire is No Limit, a Duroc boar from Shipley Swine Genetics (reg. 444008005), confirmed by date alignment of the 4/2 AI service plus 114-day gestation landing exactly on the confirmed farrow date. Scott also flagged a stale Craigslist listing advertising purebred Durocs that are no longer available and was advised to pull or edit it.

The breeding stock listing covers five animals with confirmed pricing as of this conversation: Scarlet (purebred Duroc sow, unregistered, open, $350), Nutmeg (registered NSR Duroc gilt, b. 7/6/25, W.H. Garrett bloodline, sired by Roll the Dice 19-4, open, $450), Ginger (registered NSR Duroc gilt, b. 7/6/25, same bloodline and sire as Nutmeg, bred, due ~8/24, $450), Goldie (50/50 Duroc/Berkshire gilt, b. 9/12/25, bred, due ~8/31, $450), and Willow (50/50 Duroc/Berkshire gilt, b. 9/12/25, proven, available end of August post-weaning, $350 — corrected down from $450). Scott provided the final canonical version of this message and it should be treated as the authoritative pricing reference going forward. All animals are pasture-raised, no antibiotics or hormones, hot wire trained, cash at pickup in Franklin, GA. Scott also noted the farm no longer keeps a boar and operates strictly via AI for better genetics access.

Scott's communication preferences are direct and minimal — he wants copy he can paste without modification, no repeated information across the original post and the share hook, no unsolicited sales suggestions embedded in copy (e.g., the "full sisters" upsell line was explicitly removed), and no extra punctuation or formatting that breaks copy-paste. He flagged repeated issues with Claude's in-app copy function and requested a plain-text file output as a workaround. Correction pattern to note: Scott will provide exact final text when Claude gets details wrong and expects that version to be recorded and used going forward without requiring re-explanation.

**Tool Knowledge**

Claude used the memory tool and file creation tool during this conversation. When copy-paste from Claude's response formatting was failing repeatedly in Scott's app, creating a plain `.txt` file at `/mnt/user-data/outputs/` with no bullet characters or special formatting resolved the issue — the file was then presented via the `present_files` tool for Scott to open and select all. For memory updates, the `add` command with a dense single-block parameter string was used to record the canonical breeding stock pricing and litter details in one entry rather than separate records, which kept the reference clean and queryable. When Scott indicated relevant information might exist in a different chat, a `conversation_search` query using animal names and sale context terms successfully surfaced the prior breeding stock discussion.

### SCOTT (2026-08-11T14:15)
Need to sell this batch of piglets. Willows litter. 5 barrows 4 gilts. Help me with a short post to sell these guys. I will post to farm fb page and then will share out to local fb group pages
[File uploaded: IMG_4064.jpeg]

### CLAUDE (2026-08-11T14:15)
Scott needs a Facebook post for selling Willow's piglets—9 available (5 barrows, 4 gilts) from an F1 Berkshire-Duroc cross, born late July, priced at $150 each. I'm keeping this straightforward and positive, focusing on the value proposition without any farm backstory or uncertain details. The numbers check out against what we have on record for the litter.

On the sire question: Willow was AI'd to No Limit but may have run with Chester—both are Duroc, so either way the piglets are the same breed composition. I'll just call them Berkshire-Duroc crosses to stay safe and accurate without speculating on parentage. For timing, the piglets are about 2.5 weeks old now and would be ready around early September at 6 weeks, so I should mention availability or note that we're taking reservations rather than promise specific pickup dates I haven't confirmed.

Now I'm drafting the post itself—warm, straightforward farmer voice, hitting the key details about the piglets' training and care. The barrows are already accounted for, so I just need to list what's available and let Scott confirm the ready date before I finalize it.…Piglets available — Berkshire/Duroc cross, born here on pasture in late July.

5 barrows, 4 gilts. $150 each.

Hot wire and nipple waterer trained from birth, handled daily for socialization, pasture-raised without antibiotics or hormones — ready to hit the ground running when they get to your place.

Ready to go home the first week of September. Message us to reserve yours.

Watts Way Farms · Franklin, GA · 706-883-5644

---

One thing to confirm before you post: I put the pickup window at first week of September based on the ~7/25 farrow and your 6-week sale standard. Adjust if you're planning a different date.

### SCOTT (2026-08-11T14:16)
You know the exact birth date. And should I maybe say discount available if anyone wants 5 or more?

### CLAUDE (2026-08-11T14:16)
I'm looking at what I actually have on record for Willow's farrowing date — it's marked as approximately 7/25/26 across the herd card and memory notes, but it's clearly an estimate rather than a confirmed exact date, so I should be clear about that distinction.

On…Correction first: what I have is "~7/25/26" — recorded with a tilde as the projected farrow date, later noted as 14 born / 10 live at day 4. So I have an approximate date, not a confirmed one. If 7/25 is right, six weeks lands on 9/5. Give me the actual date and I'll set it exactly.

On the discount — yes, but name the number instead of saying "discount available." Vague discounts invite everyone to haggle you down one at a time. A stated price for 5+ closes the ask and moves the whole litter in one transaction. $125 each for 5 or more is a clean $125 off a full group and still well above what you'd net running them to market weight.

---

Piglets available — Berkshire/Duroc cross, born on pasture July 25.

5 barrows, 4 gilts. $150 each, or $125 each if you take 5 or more.

Hot wire and nipple waterer trained from birth, handled daily for socialization, pasture-raised without antibiotics or hormones — ready to hit the ground running when they get to your place.

Ready to go home September 5. Message us to reserve yours.

Watts Way Farms · Franklin, GA · 706-883-5644

### SCOTT (2026-08-11T14:19)
Yes. July 25th is confirmed birth date

### CLAUDE (2026-08-11T14:19)
Confirmed — Willow's litter, born 7/25/26. Pickup 9/5.

---

Piglets available — Berkshire/Duroc cross, born on pasture July 25.

5 barrows, 4 gilts. $150 each, or $125 each if you take 5 or more.

Hot wire and nipple waterer trained from birth, handled daily for socialization, pasture-raised without antibiotics or hormones — ready to hit the ground running when they get to your place.

Ready to go home September 5. Message us to reserve yours.

Watts Way Farms · Franklin, GA · 706-883-5644

### SCOTT (2026-08-11T14:21)
Maybe add AI sire? I was going to use these two pics
[File uploaded: IMG_4064.jpeg]
[File uploaded: IMG_9358.png]

### CLAUDE (2026-08-11T14:22)
Scott's looking to add the AI sire, but there's a complication with Willow—she was artificially inseminated on 4/2/26 to No Limit (Shipley Duroc #437) while also running with Chester, which creates potential sire ambiguity. Let me verify the timing: the AI date plus a standard 114-day gestation period lands exactly on her 7/25/26 farrowing date, so the insemination took on the first service and Chester wasn't the sire.

The second photo is a screenshot from shipleyswine.com showing a boar in a gallery, but there are a few issues—I can't confirm from the image that it's actually No Limit since there's no visible name on the page, and the screenshot includes browser chrome, URL bar, and battery indicator, which looks unprofessional for a sale post. Plus it's Shipley's copyrighted photo, so I should either get permission or just reference the sire by name in text instead. The practical fix is to crop out the UI elements or request a clean image from Shipley.…Two things before you post.

**Sire:** Willow was AI'd to No Limit on 4/2 and was also running with Chester at the time — the record flags that ambiguity. But 4/2 plus 114 days lands on exactly 7/25, which is the confirmed farrow date. That's a strong indicator the AI took on first service. It's an inference from date alignment, not a confirmed parentage, so it's your call whether to name him. If you want it airtight, the safe version is naming the AI service without claiming it as proven. Either way the breed description holds — Chester and No Limit are both purebred Duroc, so the piglets are 3/4 Duroc, 1/4 Berkshire regardless.

**Second photo:** that's a screenshot with the URL bar, clock, and battery showing, and I can't tell from the page which of the five boars is No Limit. Pull the clean image off Shipley's site and crop it, and it's worth a quick message to them confirming it's okay to use their photo in your ad.

---

Piglets available — Berkshire/Duroc cross, born on pasture July 25. Sired by No Limit, an AI Duroc boar out of Shipley Swine Genetics.

5 barrows, 4 gilts. $150 each, or $125 each if you take 5 or more.

Hot wire and nipple waterer trained from birth, handled daily for socialization, pasture-raised without antibiotics or hormones — ready to hit the ground running when they get to your place.

Ready to go home September 5. Message us to reserve yours.

Watts Way Farms · Franklin, GA · 706-883-5644

### SCOTT (2026-08-11T14:23)
How about this pic instead
[File uploaded: FullSizeRender.jpeg]

### CLAUDE (2026-08-11T14:23)
That one confirms it's No Limit — name, reg number 444008005, and Shipley's URL all visible. Better than the first screenshot, but it's still a screenshot: the leaves-and-sky reflection is bleeding over the whole frame, and the URL pill sits on top of the text.

Two options. Crop tight to just the top boar photo — that gives you a clean side profile with no browser chrome and no reflection over the animal. Or save the actual image file from the site rather than screenshotting the page. Either way, worth a quick message to Shipley confirming they're fine with you using their boar photo in your ad.

Post copy stays as written.

### SCOTT (2026-08-11T14:47)
Give me the one sentence for my shares

### CLAUDE (2026-08-11T14:47)
Berkshire/Duroc piglets born July 25 on pasture in Franklin — 5 barrows, 4 gilts, $150 each or $125 each for 5 or more, ready to go home September 5.

### SCOTT (2026-08-11T14:47)
Na. Thats in the post. You are repeating yourself.

### CLAUDE (2026-08-11T14:47)
Got it — you want the hook that sits above the shared post, not a recap.

Anybody around here looking to raise their own pork this fall? We've got a litter ready.

### SCOTT (2026-08-12T13:28)
Of course I’m getting. Messages of “how much”. Give me a nice reply

### CLAUDE (2026-08-12T13:28)
Hey! They're $150 each, or $125 each if you take 5 or more. They'll be ready to go home September 5. How many were you thinking?

### SCOTT (2026-08-12T13:40)
Help with reply
[File uploaded: 5f0ff1a8ed7fdeb1920d0604dd65879a91c91f08.png]

### CLAUDE (2026-08-12T13:40)
Note this is your Craigslist Duroc listing — Scarlet's 5/15 litter — not Willow's crosses, so the September pickup date doesn't apply here.

---

Good morning Rosmel. My number is 706-883-5644 — feel free to call or text anytime. We're in Franklin, GA, about an hour and fifteen from Lawrenceville.

Still have the pigs available at $150 each. They're purebred Duroc, pasture-raised, no antibiotics or hormones, hot wire and nipple waterer trained, and handled daily. Ready to go home now.

How many were you looking for?

— Scott, Watts Way Farms

---

One flag: if the piglet with the undescended testicle is still in that available group, that's a one-on-one disclosure to make before money changes hands.

### SCOTT (2026-08-12T13:41)
We don’t have purebreds available. Just Willows babies

### CLAUDE (2026-08-12T13:41)
Then the Craigslist ad is advertising something you don't have — worth editing or pulling it before more inquiries come in off it.

---

Good morning Rosmel. My number is 706-883-5644 — call or text anytime. We're in Franklin, GA.

I need to correct that listing — the purebred Durocs are gone. What we have now is a Berkshire/Duroc cross litter, born July 25, ready to go home September 5. Five barrows and four gilts, $150 each or $125 each if you take five or more.

Same raising either way — pasture, no antibiotics or hormones, hot wire and nipple waterer trained, handled daily.

Let me know if that works for you.

— Scott, Watts Way Farms

### SCOTT (2026-08-12T22:39)
Nice response here. Say we don’t have the fencing to contain goats. We have all of our cows and pigs trained to a single strand of Hotwire. Which would not work for goats.
[File uploaded: fe0773d9bc7537335750b22d4c95da8616dbf971.png]

### CLAUDE (2026-08-12T22:39)
Hi Kristy! Appreciate the offer — those sound like nice goats. Unfortunately we're not set up to take them. Everything here, cows and pigs both, is trained to a single strand of hot wire, and that just won't hold goats. We'd be chasing them around the county.

We do still have piglets available though. Berkshire/Duroc cross, born July 25, ready to go home September 5 — $150 each, or $125 each if you take five or more. Pasture-raised, no antibiotics or hormones, hot wire and nipple waterer trained from birth, handled daily.

How many were you thinking?

### SCOTT (2026-08-12T22:43)
Reply here. Tell her might be willing to meet. Depends on where and how many she is buying.  Tell her we don’t have a boar anymore either. We strictly ai now. Better genetics
[File uploaded: ec33d508b44d8dfb075cc7ac7734bdb1288c7ee1.png]

### CLAUDE (2026-08-12T22:43)
Gilts will be ready to go home September 5. They're $150 each, or $125 each if you take five or more.

On meeting — we might be able to work something out. Depends on where you are and how many you're taking. Let me know both and I'll tell you what's doable.

And just so you know, we don't keep a boar anymore either. We've gone strictly AI so we can pull from better genetics than any one boar we'd own. Something to think about down the road if you decide to breed — you don't need to keep a male to do it.

### SCOTT (2026-08-15T12:53)
We need to sell some of these sows and gilts. We have purebred Duroc (scarlet) not registered. Purebred Duroc registered. And 50/50 Duroc Berkshire gilt. Help me with a fb listing. Say something like ready to go breeding stock to grow your farm or market ready hog. Message me for details. No price.
[File uploaded: IMG_9912.jpeg]
[File uploaded: IMG_9911.jpeg]
[File uploaded: IMG_9910.jpeg]

### CLAUDE (2026-08-15T12:53)
Breeding stock available — Watts Way Farms, Franklin, GA

We're offering a few of our sows and gilts:

• Purebred Duroc sow, unregistered — proven
• Registered Duroc gilt (NSR)
• 50/50 Duroc/Berkshire gilt

All pasture-raised here, no antibiotics or hormones, hot wire trained, handled daily. Easy to work with and ready to go to work — bring one home to grow your own program, or take her as a market-ready hog.

Message me for details.

Watts Way Farms · Franklin, GA · 706-883-5644

---

One flag before you post: the registered Duroc gilt I have on record as available for sale is Nutmeg, whose settle from the 5/3 breeding was never confirmed. Ginger is the other registered Duroc and she's due to farrow around 8/24. If Ginger is the one going, that changes what you can say about timing.

### SCOTT (2026-08-15T12:55)
Goldie and ginger are pregnant. Scarlet and nutmeg are not. Willow has 3 week old piglets. So she will be ready to sell in two weeks.

### CLAUDE (2026-08-15T12:55)
Updated: Scarlet and Nutmeg open and available now, Willow after weaning. That lines up — her piglets hit 5 weeks on 8/29.

---

Breeding stock available — Watts Way Farms, Franklin, GA

We're offering a few of our sows and gilts:

• Purebred Duroc sow, unregistered — proven, open and ready to breed
• Registered Duroc gilt (NSR) — open and ready to breed
• 50/50 Duroc/Berkshire gilt — proven, available end of August once she weans her current litter

All pasture-raised here, no antibiotics or hormones, hot wire trained, handled daily. Easy to work with and ready to go to work — bring one home to grow your own program, or take her as a market-ready hog.

Message me for details.

Watts Way Farms · Franklin, GA · 706-883-5644

### SCOTT (2026-08-15T12:57)
Your fucking copy in the app ain’t working. Give it to me again. Not one period extra so I can use copy response and hope it works.

### CLAUDE (2026-08-15T12:57)
Breeding stock available — Watts Way Farms, Franklin, GA

We're offering a few of our sows and gilts:

• Purebred Duroc sow, unregistered — proven, open and ready to breed
• Registered Duroc gilt (NSR) — open and ready to breed
• 50/50 Duroc/Berkshire gilt — proven, available end of August once she weans her current litter

All pasture-raised here, no antibiotics or hormones, hot wire trained, handled daily. Easy to work with and ready to go to work — bring one home to grow your own program, or take her as a market-ready hog.

Message me for details.

Watts Way Farms · Franklin, GA · 706-883-5644

### SCOTT (2026-08-15T13:01)
Give me the sentence hook for my shares

### CLAUDE (2026-08-15T13:01)
Thinking about starting your own pigs? We've got a few good girls looking for a new farm.

### SCOTT (2026-08-17T01:21)
Reply here.
[File uploaded: 27efd3dd1f15e84e8c30b9303de06de2df439d7c.png]

### CLAUDE (2026-08-17T01:21)
I can't tell from the thread which post he came off — the piglets or the breeding stock. Two versions:

**Piglets:**

$150 each, or $125 each if you take five or more. They'll be ready to go home September 5. How many were you looking for?

**Breeding stock:**

Depends on which one. The unregistered Duroc sow is $350, and the registered Duroc gilt and the Duroc/Berkshire gilt are $450 each. Which one were you looking at?

### SCOTT (2026-08-17T01:21)
Breeding stock. Give me the summary for them all. Like we did for the others.

### CLAUDE (2026-08-17T01:21)
Here's what we have:

• Scarlet — purebred Duroc sow, unregistered, born early January 2025. Proven, open and ready to breed. $350

• Nutmeg — registered Duroc gilt (NSR), born July 6, 2025. W.H. Garrett bloodline, sired by Roll the Dice 19-4. Open and ready to breed. $450

• Willow — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Proven, available end of August once she weans her current litter. $450

All pasture-raised, no antibiotics or hormones, hot wire trained, handled daily. Let me know which one you're interested in.

### SCOTT (2026-08-17T01:22)
No fucker. Did you forgot about our discussion around selling the Regis too and Willow in two weeks?

### CLAUDE (2026-08-17T01:22)
I've got what you told me: Goldie and Ginger pregnant, Scarlet and Nutmeg open, Willow available in two weeks. I built the list off that — Scarlet, Nutmeg, Willow.

What I don't have is a decision from you to sell Ginger or Goldie. If you're selling the bred registered gilt too, tell me which and I'll add her with her due date. Same for Goldie if she's going.

### SCOTT (2026-08-17T01:23)
Maybe different chat. Take a few moments and search instead of acting so dumb all the time

### CLAUDE (2026-08-17T01:23)

Found it — the 8/15 thread had all five listed, Ginger and Goldie included as bred at $450.

Here's what we have:

• Scarlet — purebred Duroc sow, unregistered, born early January 2025. Proven, open and ready to breed. $350

• Nutmeg — registered Duroc gilt (NSR), born July 6, 2025. W.H. Garrett bloodline, sired by Roll the Dice 19-4. Open and ready to breed. $450

• Ginger — registered Duroc gilt (NSR), born July 6, 2025. Full sister to Nutmeg, same bloodline and sire. Bred, due around August 24. $450

• Goldie — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Bred, due around August 31. $450

• Willow — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Proven, available end of August once she weans her current litter. $450

Nutmeg and Ginger are full sisters, so taking the pair gives you a consistent registered base to build on.

All pasture-raised, no antibiotics or hormones, hot wire trained, handled daily. Cash at pickup in Franklin, GA. Let me know which ones you're interested in.

### SCOTT (2026-08-17T01:25)
Leave this shit out. 

Nutmeg and Ginger are full sisters, so taking the pair gives you a consistent registered base to build on.

And give me just the message so I can copy past

### CLAUDE (2026-08-17T01:25)
Here's what we have:

• Scarlet — purebred Duroc sow, unregistered, born early January 2025. Proven, open and ready to breed. $350

• Nutmeg — registered Duroc gilt (NSR), born July 6, 2025. W.H. Garrett bloodline, sired by Roll the Dice 19-4. Open and ready to breed. $450

• Ginger — registered Duroc gilt (NSR), born July 6, 2025. Same bloodline and sire as Nutmeg. Bred, due around August 24. $450

• Goldie — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Bred, due around August 31. $450

• Willow — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Proven, available end of August once she weans her current litter. $450

All pasture-raised, no antibiotics or hormones, hot wire trained, handled daily. Cash at pickup in Franklin, GA. Let me know which ones you're interested in.

### SCOTT (2026-08-17T01:25)
Put it in a card you fucking copy paste ain’t working again

### CLAUDE (2026-08-17T01:25)
I'll write it to a file you can open and copy from.

Plain text, no bullets or special characters. Open it and select all.

### SCOTT (2026-08-17T01:28)
Updated your prices some. Read the below and remember this.

Here's what we have:

Scarlet — purebred Duroc sow, unregistered, born early January 2025. Proven, open and ready to breed. $350

Nutmeg — registered Duroc gilt (NSR), born July 6, 2025. W.H. Garrett bloodline, sired by Roll the Dice 19-4. Open and ready to breed. $450

Ginger — registered Duroc gilt (NSR), born July 6, 2025. Same bloodline and sire as Nutmeg. Bred, due around August 24. $450

Goldie — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Bred, due around August 31. $450

Willow — 50/50 Duroc/Berkshire gilt, born September 12, 2025. Proven, available end of August once she weans her current litter. $350

All pasture-raised, no antibiotics or hormones, hot wire trained, handled daily. Cash at pickup in Franklin, GA. Let me know which ones you're interested in.

### CLAUDE (2026-08-17T01:28)

Recorded. Willow is $350, not $450 — that's the change from what I had. Everything else stands: Scarlet $350, Nutmeg / Ginger / Goldie $450 each.

### SCOTT (2026-08-18T19:56)
Feels like the beginning of a scam. Thoughts?
[File uploaded: IMG_0030.png]
[File uploaded: IMG_0029.png]
[File uploaded: IMG_0031.png]
[File uploaded: IMG_0032.png]

### CLAUDE (2026-08-18T19:56)
Your instincts are reading real signals. What's actually observable:

- Account is brand new — 6 followers, 0 following, 1 post, and the profile picture went up 21 hours ago
- Name and profile photo don't match up
- Listed as "Digital creator," location just "United States," no reviews
- Buying a live animal sight unseen, no questions about her breeding, condition, or anything a real pig buyer asks
- Wants a third party to collect, tomorrow, on a same-day turnaround

Individually any one of those has an innocent explanation. Together they line up with the standard livestock version of this scam: the buyer never appears in person, arranges remote payment, sends a spoofed confirmation, and a "relative" collects the animal before you find out the payment isn't real. The rush and the third-party pickup are the two pieces that do the work.

Your cash-at-pickup policy already blocks it. Hold that line and you're fine — no payment app, no check, no "I'll send it now and he'll grab her." If they're legitimate, the brother shows up with cash in a few days and nothing is lost. If they're not, you'll never hear back.

Your "No, I said I need a few days notice" was the right answer. I wouldn't add anything to it.

### SCOTT (2026-08-18T22:03)
The scam unfolds.
[File uploaded: 6d019ccaba68ccab02047fe3c8a783dae31da6d2.png]

### CLAUDE (2026-08-18T22:03)
That's the tell. "Pay upfront now to secure her" is the whole play — the fake payment confirmation is the next message, then pressure to release the animal against it.

"No. Cash at pick up only." is the correct answer and needs no follow-up. If they push again, don't argue the point, just stop replying. Arguing gives them another turn to work on you.

Worth reporting the profile to Facebook while it's fresh — new account, mismatched name and photo, working your listing. Won't help you but it may catch the next person.
