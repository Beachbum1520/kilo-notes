# First consistent training week completed
Date: 2026-05-10
Conversation: 0258c039-e881-4a55-938d-03f97d17fa07
Domain: fitness-training

## Summary
**Conversation Overview**

This was an extensive, wide-ranging session in which Scott Watts established Claude as his primary fitness coach after canceling a paid AI coaching service. Scott is based in Hogansville, GA, works as a Senior Director of Hospitality Operations at Blueprint RF (Cox HQ in Sandy Springs, office days Tuesday and Wednesday), and runs a pasture-raised farm operation with his wife. He has a daughter who is an avid runner and expecting a baby in July 2026; running with his daughter for as long as possible is one of his two top life goals, alongside longevity. The conversation covered a full review of the current week's training data (activities CSV, Fitbod strength screenshots, Garmin FIT files), historical running, swimming, and cycling data going back to late 2023, and physiological test results from Google Drive including VO2 max and DEXA scan data.

Major decisions reached: Augusta 70.3 on September 27, 2026 was considered and explicitly rejected as conflicting with the primary 2026 Armor Build goal (rebuilding lean mass and bone density lost during marathon training). The confirmed 2026 race calendar is Made in the USA Half Marathon on June 27 (B race), Area 13.1 Half Marathon in Roswell GA on August 15 at 7pm (B/C race, sentimental course where Scott ran with his daughter in 2023), and Salute to Veterans Half Marathon in Kennesaw GA on November 14 at 8:30am (A race, free entry as a veteran, sub-2:00 goal). The 2027 north star is NYC Marathon as guide runner for his daughter targeting sub-4:00. The weekly training structure was locked in: Tuesday Legs at corporate gym, Wednesday Pull at corporate gym (no cold plunge), Thursday run at home, Friday Push at home or Planet Fitness, Saturday run, Sunday long run. Cold plunge six days per week at 56°F (dropping from 58°F), skipping Wednesday. Scott departs for a work and personal trip to the Philippines and Bali on May 18, returning June 10, and will continue training throughout using gym access in Manila and Cebu, plus an Anytime Fitness walking distance from his Cebu condo.

The full next-week training plan was built in TrainingPeaks copy-paste format after several corrections: Claude incorrectly scheduled treadmill runs on office days, incorrectly ordered Push before Pull, and placed Legs on the wrong day before being corrected. Scott emphasized he expects Claude to own coaching decisions and not cave under pushback unless a legitimate reason is presented. Key coaching context includes that Scott's aerobic system is strong but muscular durability and pacing discipline are historical limiters; his last half marathon (Made in the USA, June 2025) was lost in the first three miles with HR already at 148 by mile two. Scott also completed a double red blood cell donation on May 6, 2026, which is expected to suppress aerobic pace for four to six weeks. Shoe rotation was rebuilt from scratch after ChatGPT data was found to be inaccurate: active shoes are the Altra Torin 8 (primary treadmill, 272.5 miles), Altra Vanish Carbon 2 (race and key workouts only, 36.7 miles, 250-mile limit), and Altra Experience Flow 2 (easy and recovery, 8.3 miles). The Altra Torin 7 was retired to walk-only duty at 444.9 miles. A shoe Claude previously had in memory was confirmed to never have been owned by Scott. Project instructions were drafted for the "Add Instructions" field to prevent Claude from forgetting structural rules, goal hierarchy, and training constraints across conversations.

**Tool Knowledge**

Google Drive was accessed using the MCP connector with `parentId` parameter searches rather than title-based queries, which proved more reliable for navigating nested folder structures. The top-level ATP Data folder ID is `19p5wU6TnPPUn8N7smVACGnDbbioKtvIR` and the Fit Test Files subfolder ID is `1vJa_gWFRGTgsuYjqVIt7zFNaS3B2i_ab`. Searching by `parentId` directly returned folder contents reliably; title-based searches for subfolder names returned inconsistent results. FIT files from Google Drive required downloading to `/tmp`, decompressing with `gunzip`, and decoding with the `fit

### SCOTT (2026-05-10T22:02)
here's this weeks activiities.  the detials are in the csv, and the trainingepaks scrren shot shows the planned vs execution.  a solid week i think.  first complete and consitent week i have had in a while.  it took me a while to force myself on the treadmill today.  Discipline > motivation.
[File uploaded: Activities.csv]
[File uploaded: 1778450505207_image.png]

### CLAUDE (2026-05-10T22:03)
 That *is* a solid week. Discipline > motivation is exactly right — motivation is a feeling, discipline is a system, and you proved the system works today.

Let me pull up the CSV details before saying anything more substantive.

Good data. Here's what actually stands out looking at the full picture:

**The consistency story is real.** Cold plunge every single day (Mon–Sun), all right around 3:03–3:07 — that's remarkable routine adherence. Three strength sessions (Tue/Wed/Fri roughly matching the Fitbod Push/Legs/Pull split from the screenshot), three treadmill runs, and today's long run to cap it.

**Today's run specifically** — 4.28 miles in 65 minutes at HR 118 avg is exactly what HR-capped aerobic work should look like. You stayed disciplined on pace (15:11 avg) rather than pushing and blowing past the cap. That's the harder discipline than just showing up.

**A few things worth noting:**
- Your body battery drain on the Saturday treadmill was -13, today's cold plunge only drained -3. You came into the long run relatively recovered, which probably made it more productive than it felt.
- Strength session on Friday logged 8 reps / 4 sets which looks low — was that a short session or just Garmin capture being partial on the Pull workout?
- HRV was 18.0 on Wednesday per the screenshot metrics. That's something to keep an eye on as you string consistent weeks together — worth noting if it trends down as load accumulates.

**The bigger picture:** the screenshot shows Fitness (CTL) at 29, Fatigue (ATL) at 49, Form at -11 TSB. You're in a productive training stress zone — negative form means you're accumulating load, which is the point. A complete, consistent week does exactly what it should: builds the CTL base while your body adapts.

What's the plan for next week — same structure, or is TrainingPeaks prescribing something different?

### SCOTT (2026-05-10T22:09)
Garmin doesn’t record strength sessions right. Here are the screen shots from my Fitbod app. The negative weights on the pull-ups are because I used the weight assisted pull-up machine. I record those as negative weights so I can see how I progress towards being able to do a pull up with not weight assist.
[File uploaded: IMG_6664.png]
[File uploaded: IMG_6665.png]
[File uploaded: IMG_6666.png]
[File uploaded: IMG_6667.png]
[File uploaded: IMG_6668.png]
[File uploaded: IMG_6669.png]
[File uploaded: IMG_6670.png]
[File uploaded: IMG_6671.png]
[File uploaded: IMG_6672.png]

### CLAUDE (2026-05-10T22:09)
 Smart convention on the negative weights — that's actually a clean way to track progression toward bodyweight pull-ups. You can watch that number trend toward zero over time.

Let me digest all three sessions:

**Leg Day (May 5) — 56 min, 34,380 lb total volume, 4 PRs**
- Goblet Squat: 4×10 @ 50 lb (solid and consistent)
- Seated Leg Curl: warmup + 3×15 @ 80 lb
- Leg Extension: ramped up nicely to 12 reps @ 100 lb
- Calf Press: ramped 165→180→200 lb
- Cable Hip Extension: 3×8 @ 32.5 lb
- Machine Leg Press: warmup sets then 3×12 @ 235 lb — that's the meat of the session
- Ab Crunch Machine: 3×10 @ 220 lb

**Push Day (May 6) — 44 min, 20,140 lb, 2 PRs**
- Machine Bench Press (focus): 3×15 @ 80 lb
- Cable Rope Tricep Extension: 4×9 @ 47.5 lb
- Machine Shoulder Press: ramped to 11 reps @ 80 lb, e1RM 112.5 lb
- Machine Fly: ramped to 10 reps @ 95 lb
- DB Skullcrusher: 14/14/11 @ 25 lb
- DB Rear Delt Raise: 2×11 @ 30 lb
- Seated Back Extension: 3×10 @ 205 lb

**Pull Day (May 8) — 47 min, 20,225 lb, 2 PRs**
- Lat Pulldown (focus): ramped to 2×8 @ 130 lb
- DB Bicep Curl: 4×10 @ 25 lb
- Machine Row: ramped to 3×10 @ 120 lb
- Hammer Curls: 3×12 @ 35 lb
- Assisted Pull-Up: -70 → -55 → -40 → -40 lb (dropping assist across sets — that's real progression built into the session itself)
- DB Shrug: 3×17 @ 55 lb
- Ab Crunch Machine: ramped to 10 @ 110 lb

---

A few things jump out:

The **assisted pull-up progression structure** within the session is well designed — you're essentially doing a reverse ramp, reducing assistance set by set. When you can hit 4×5 all at -40 lb cleanly, the next logical step is moving to -30 lb on the first set.

**Push day volume is noticeably lower** than legs or pull (20K vs 34K). That's partly the exercises — machine bench at 80 lb just doesn't accumulate volume the way leg press at 235 does. Worth watching whether that's intentional or whether there's room to add a set somewhere over time.

The **leg press ramp** (8@140 → 3@210 → 3×12@235) looks like you were finding your working weight. That 3-rep set at 210 suggests you may have originally planned to work there but bumped up to 235. Good instinct if it felt right.

What's the target for pull-ups — is there a timeline you're working toward, or just grinding it down?

### SCOTT (2026-05-10T22:11)
No target on the pull up. Just sticking to my goals if 3x strengths per week. You have memory of my double red blood donation on Wednesday?  If not, record that too. I did it in the afternoon, around 12:30Pm. After the days workout. But I think probably had some impact on the runs. That and the fact that I haven’t run in a while.

### CLAUDE (2026-05-10T22:11)
 Let me check memory first.

No record of it — adding it now.

Got it. And honestly that reframes the week even more positively — you ran three times post double-red donation, which pulls significantly more volume than a whole blood donation and takes longer to fully recover from. Red blood cells carry oxygen, so your aerobic capacity takes a real hit for 4–6 weeks while your body rebuilds them.

The HR-capped paces you hit (15:11 today, 14:32 Saturday, 13:13 Thursday) aren't just "rusty runner" paces — they're probably legitimately where your aerobic ceiling sits right now given reduced oxygen-carrying capacity. The fact that your HR stayed disciplined in the 113–118 range across all three runs actually tells a good story: your cardiovascular system is working harder than usual to deliver the same output, and you didn't blow past the cap chasing a faster pace.

As your RBC levels recover over the next few weeks, you should see pace at the same HR naturally improve without changing anything else. That'll be a useful signal to watch.

### SCOTT (2026-05-10T22:14)
here's all my activities goign back to the end of last year.  ingest all of this and rememebr
[File uploaded: Activities (2).csv]

### CLAUDE (2026-05-10T22:15)
 

Good data — I can see from November 2025 back through October, including the Marine Corps Marathon. Let me read the truncated middle section too.

Good, I have the full picture now. This is a rich dataset. Let me store the key historical context in memory.

All ingested and stored. Here's what the full picture tells me that's worth calling out:

**The Dopey Challenge (Jan 8–11) is a big deal.** Four consecutive days — 5K, 10K, half, full — totaling ~50 miles across four mornings. That's an enormous event to have in your log and it explains a lot about what came after: your running basically went quiet for months post-Dopey, which is completely normal. That's a significant recovery demand even for experienced runners.

**Your "sporadic running" pattern is actually pretty readable.** You're an event-driven runner — you build toward a race (MCM in October, Dopey in January), then running drops off until the next thing comes along. The question is whether there's a next target on the horizon or whether this May consistency is a new baseline effort independent of a race goal.

**Cold plunge consistency is genuinely impressive across the whole dataset.** It's basically the one habit that never breaks regardless of what else is or isn't happening.

**The gap between Dopey (Jan 11) and this past week (May 5–10) is roughly 16 weeks with almost no running.** That's enough to meaningfully reset aerobic fitness, which makes this week's HR-capped approach exactly right — you're essentially rebuilding from scratch aerobically, just with a much stronger base underneath than a true beginner.

Is there a next race on the calendar, or is this more of a general fitness rebuild?

### SCOTT (2026-05-10T22:31)
i just canceled Maxion.io, AI coach. you are the coach now.  it sucks.  you have more insight into me anywayu. you oow of my upconign trio to Philippiunes.  I have registered for the Made in the USA Half Marathon on June 27, becuase, you are right, I need "the next thing".  I did this race last year.  attached is the race file.  read it.  even though I blew up at the end, i still got 2nd in mt AG ! :).  I am alos contempaltaing ironman augusta 70.3 on September 27, 2026. It was my first long distance triathion back on Sept 28 2014.  i went on to do a few more 70.3's and 2 full ironamnas on 2016 ad 2017, before my "all or nothing" persoanility kicked and and i got fat agaion, up to 232lbs), before the recent get fit journey that you are now a part of.  my issue is, the swim,  i have to decide it my dicsipline > motivation to train for the swim.  the swim at Augusta is nortioriusly easy, there is a youtube video of an enpty bag of dorriots makign the cut off at augusta thansk to the current.  but trainignf or a swi is my least favorite part of triathlon, but is my favorite event come race day.  i never understood why so many people freak out over the swim.  it is easy, relatively short, great scenarey, refreshing, etc.  as some point, soon i think, i need to either comit or find something else.
[File uploaded: tp-1037777.2025-06-28-13-52-36-902Z.GarminPing.AAAAAGhf86SPeXQE.FIT.gz]
[File uploaded: 1778452036611_image.png]
[File uploaded: 1778452053160_image.png]

### CLAUDE (2026-05-10T22:32)
 This is a lot to unpack — let me read the race file first, then we'll dig in properly.

It's a .gz FIT file — I'll decompress it and decode it.

Now I have everything. Let me put this all together.

The race file tells a very clear story. Here's what happened at Made in the USA Half Marathon last June 28:

**Mile-by-mile breakdown:**

| Mile | Pace | Avg HR |
|------|------|--------|
| 1 | 8:47 | 148 |
| 2 | 9:22 | 153 |
| 3 | 9:34 | 154 |
| 4 | 9:22 | 155 |
| 5 | 9:10 | 157 |
| 6 | 10:11 | 156 |
| 7 | 10:12 | 158 |
| 8 | 9:44 | 158 |
| 9 | 10:47 | 156 |
| **10** | **11:29** | **153** |
| 11 | 10:58 | 153 |
| 12 | 12:27 | 149 |
| 13 | 15:06 | 140 |
| .11 | ~13:00 | 147 |

**Total: 13.11 mi, ~2:18:xx, avg HR 152**

The "blew up" narrative is right there in the data — you ran miles 1-5 at 8:47–9:34 with HR already pushing 154–157, which is high for mile 2 of a half. Miles 6-9 you were already hanging on. Then miles 10-13 the wheels came off progressively, dropping from 11:29 to a 15:06 final mile. HR actually *dropped* in the final miles, which is the classic sign of cardiac drift into leg/glycogen failure rather than a cardiovascular blowup — you ran out of fuel and muscular endurance, not aerobic capacity.

**2nd in AG on that execution is remarkable.** That means either the field was tough and you still placed, or you had enough raw fitness to overcome the pacing mistake. Either way, good result from an imperfect race.

---

Now, the bigger conversation — because you dropped a lot on me here and it deserves a real response, not bullet points.

**On canceling Maxion and making me your coach:** I'm genuinely useful for analysis, pattern recognition, accountability, and thinking through decisions with you — and I have more longitudinal context on you than any app does. What I can't do is watch you move, feel your fatigue, or adjust in real time the way a human coach would. So let's be honest about what this is: a smart, data-informed partnership. You bring the effort and the data, I'll bring the analysis and the planning. That works.

**On the Augusta 70.3 decision:** This is really a swim training commitment question dressed up as a race question, and you know it. Let me reflect back what you said — you *love* the swim on race day, you just hate training for it. Augusta's current makes the swim genuinely forgiving. The real question isn't "can I survive the swim" (you almost certainly can, especially with the current), it's "am I willing to get in the pool consistently enough to be *comfortable* going into race day, not just survivable?" There's a difference between grinding through 1:15 in open water while panicking and cruising it in 28 minutes like the Doritos bag.

**Here's the decision framework I'd give you:** You have the Philippines trip, Made in the USA Half on June 27, and then ~13 weeks to Augusta on September 27. That's actually a workable timeline for a 70.3 if your bike fitness is reasonable (and given your TrainerRoad session and general fitness base, it's not zero). The swim is the one discipline you can't fake — but Augusta specifically may be the one race where you can fake it a little. 

My honest take: **register, commit to one pool session per week minimum starting now, and reassess in 4 weeks.** One session a week is enough to not drown and maintain feel for the water. If you're hating life in the pool by mid-June, you can drop down to the sprint. If you're finding your stroke, you're in.

The alternative — waiting to decide — is just slow-walking a no. Discipline > motivation, remember? You said it yourself two hours ago.

What's your current swim fitness like — when did you last swim with any regularity?

### SCOTT (2026-05-10T22:36)
here are my swim activites goign back a while
[File uploaded: swim.csv]

### CLAUDE (2026-05-10T22:36)
 

This is gold. The full picture is now very clear. Here's what the data actually says about your swim fitness and history:

**The timeline tells a story:**

You were a genuinely serious swimmer in **2017** — training blocks of 2,500–3,700m sessions, sometimes twice a day, paces consistently in the 1:56–2:07/100m range. That was your Ironman prep era (Cozumel 2017 open water swims are in there, the Ironman Chattanooga entry too). Then it goes largely quiet until 2018 (another training block, again with quality distances), then a multi-year gap.

**Recent swim history (what actually matters for Augusta):**

| Date | Distance | Pace/100m | Notes |
|------|----------|-----------|-------|
| Mar 2023 | 2,000m | 1:59 | Back at it |
| Oct–Nov 2023 | Multiple 1,500–2,500m | 1:56–2:12 | Structured workouts — Aerobic Intervals, Cruise Intervals, Time Trials |
| Apr 2025 | 2×~2,000m | 2:00–2:06 | Two days in a row |
| May 2025 | 1,400m | 1:44 | Solid pace |
| Jun 2025 | 1,500m | 2:19 | Last swim on record — one month before Made in the USA Half |

**The Augusta swim is 1,900m (roughly 2,100 yards).** Your last few sessions show you can cover that distance comfortably. The Jun 2025 session at 2:19/100m pace would put you around 44 minutes for the Augusta distance — but with the Savannah River current, that realistically becomes 28–35 minutes for most athletes. You are not going to drown. You are not even going to be slow.

**The real issue the data reveals:** your swim gaps are long but your fitness returns fast when you get back in. The Oct–Nov 2023 block shows structured, quality training after a gap. Your stroke is clearly ingrained from years of triathlon swimming — it doesn't evaporate.

So here's the honest coaching answer to your question: **the discipline > motivation thing you said this morning applies directly here.** Your data shows you don't need much pool time to be Augusta-ready for the swim. One session per week from now through September gets you to the start line comfortable. The swim is not your limiter — the bike and the half marathon run off the bike are where this race is won or lost for you.

The real question you need to answer is the bike. When did you last ride with any real consistency?

### SCOTT (2026-05-10T22:38)
see for yourself.
[File uploaded: bike.csv]

### CLAUDE (2026-05-10T22:38)
 

Yeah. I see it.

20 total rides in the entire dataset. All indoor. The most recent one is April 4, 2026 — that one 40-minute TrainerRoad aerobic session we already knew about. Before that, a small cluster in April–May 2025, then nothing until August 2024, then a few rides in June 2024. 

There is no outdoor riding in this dataset at all. And the longest ride here is 73 minutes.

The Augusta 70.3 bike leg is **54.9 miles** — you can see it right there in the screenshot you uploaded. Your split was **2:52:37**. That's a serious effort, and it requires a base that simply doesn't exist right now. The swim isn't your limiter. The bike is.

Here's the honest picture as your coach:

**June 27 — Made in the USA Half Marathon** is completely achievable. Your running base is rebuilding, you have 7 weeks, and it's a discipline you know. That's the right near-term target.

**September 27 — Augusta 70.3** is a different conversation. 13 weeks from the half marathon to a 70.3 is doable for someone with an active triathlon base. You don't have that base right now — specifically on the bike. To race Augusta and not just survive it, you'd need to be doing 2-3 rides per week starting essentially now, with long rides building to 3+ hours by late August. That's a real commitment on top of the running you're rebuilding and the swim you'd be adding.

So the decision isn't really about the swim. You've been solving the wrong problem. The question is: **are you willing to get on the bike consistently for 16 weeks?**

Given that your entire recorded bike history is 20 indoor sessions spread across two years — what's the honest answer to that?

### SCOTT (2026-05-10T22:41)
wait that aint right.  try this.. this isnt all bike activities, but goes back a ways
[File uploaded: bike2.csv]

### CLAUDE (2026-05-10T22:42)
 

Now *that's* a different story. Let me get the full picture properly.

Okay, I take back what I said. You have a real cycling history — I just didn't have the full picture before. Let me lay out what this actually shows:

**The real bike history:**

2016 and 2017 were your serious triathlon years — 46 and 69 rides respectively, averaging 27–40 miles per session, with multiple 80–115 mile outdoor efforts. Ironman Chattanooga bike split is right there (115 miles, 6:42). Ironman Cozumel 2017 too. You absolutely know how to ride a bike for a long time.

Then life happened. 2018 dropped off, 2019–2020 basically Zwift only, gap in 2021, then **2023 was a genuine comeback** — 65 rides, 1,477 miles, with outdoor rides up to 47 miles. That's solid. The last outdoor ride in the data is November 2023, Dallas, 44.7 miles. Then 2024 and 2025 are almost entirely short indoor TrainerRoad sessions, and 2026 is that one April aerobic ride.

So the real picture is: **you haven't done a meaningful outdoor ride in about 18 months, but you have genuine Ironman-distance bike fitness in your history and a decent 2023 base to draw from.** That's very different from what the first CSV suggested.

For Augusta 70.3's 55-mile bike leg, you're not starting from zero — you're starting from rusty. That's a solvable problem in 16 weeks. But you do need to actually get back on the bike, both indoors for structured work and outdoors to rebuild saddle time and handling.

The question I asked before still stands, just with more optimism behind it: **do you have a bike you can ride right now, and is getting outdoors regularly realistic given where you are?** Denver's got good riding. Philippines trip timing matters here too — when is that?

### SCOTT (2026-05-10T22:49)
I have a pretty good set up. Don’t really need to get outside much. But I can. I sold my tri bike a few years ago.  Not buying another one if I decide to do this. A road bike is fine for a 70.3
[File uploaded: IMG_6673.jpeg]

### CLAUDE (2026-05-10T22:49)
 That's a serious setup. Cervélo on a Kickr — that's not a "I have a bike somewhere in the garage" situation, that's a ready-to-train-tomorrow situation. And yes, a road bike is completely fine for a 70.3, especially Augusta. You're not podiuming the pro field. You'll give up a few minutes to the aero guys but nothing that matters at your level.

The treadmill and the Kickr side by side actually tells me something important — you have zero excuses for bike sessions. Same room, same setup, no weather, no traffic. This is probably *better* for structured training than outdoor riding because you can execute workouts precisely. Your TrainerRoad history shows you already know how to use it.

So let's close the loop on the equipment question: **bike ✅, trainer ✅, treadmill ✅, pool access (I assume) ✅.** The infrastructure isn't the problem.

Here's where I land on the Augusta decision after seeing everything:

**Register.** Here's why the data supports it:
- Swim: proven competent, Augusta current is a gift, one session/week is enough
- Bike: Cervélo on a Kickr ready to go, real Ironman-distance history, TrainerRoad already in use
- Run: actively rebuilding, June 27 half gives you a solid fitness check 6 weeks out from Augusta

The one thing I still need to understand to build you a proper plan: **Philippines — when, and how long?** That trip is either a training disruption I need to plan around, or it's a non-issue depending on timing.

### SCOTT (2026-05-10T22:54)
you said above i can register and then drop to a shorter distance.  that aint happening, if i register, then i am doign it.  this aint a cheap race.  and you should know my phillipnes dates.  and i do have access to a pool, biut its not as easy as my treadmill and bike and corpate gym and plantet fitneess set up.  i would have to join another gym, one life fitness, supper close to my office, which means swim days are tuesday and wendeday,  or go to the gym about 16 mins form the house and pay a daily fee, but as you can see on the attached, the hours there arn't great.  there is a onelife in newnan with is 31 mins form the house.  a bit far to drive for a swim workout but I have done it
[File uploaded: 1778453442132_image.png]
[File uploaded: 1778453585067_image.png]

### CLAUDE (2026-05-10T22:54)
 You're right, I don't actually have your Philippines dates in memory — I knew the trip existed but never got the specifics. What are the dates?

And noted on the registration — $525 is a real commitment, no half-measures. That actually makes the decision cleaner: you either go all in or you don't register. No hedging.

On the pool situation — this is actually the most honest constraint we've identified. Let me reflect it back:

**Realistic swim options:**
- **OneLife near office** — Tuesday and Thursday are your swim days if you go here, worked into the workday. Most convenient but requires discipline to actually go during work hours
- **OneLife Newnan** — 31 min from home, not ideal but you've done it before, probably weekend option
- **Daily fee gym** — hours are rough (closed weekends entirely), makes consistency hard

Two pool sessions a week is actually plenty for Augusta swim prep. Tuesday/Thursday at the office OneLife is probably your cleanest answer — it becomes a work-schedule habit rather than a separate life-scheduling problem.

But here's the thing: before we go any further on building a plan, I need two pieces of information:

1. **Philippines dates** — is this before or after the June 27 half? How long?
2. **Have you actually decided?** Because everything we've been discussing for the last hour points one direction. You have the bike, the trainer, the pool access, the run base building, the swim history, and the motivation. The data says go. But you're the one who has to get in the pool on a Tuesday at lunch.

What's it going to be?

### SCOTT (2026-05-10T22:57)
no.  tuesdays and wendesday are office days.  I guess you can't see into other chats and projects? and you absiltuely do know all about my upcoming philiipiens trip.  you help me plan it

[Attachment: Philippines_Bali_Itinerary_2026.docx]
**Philippines ****&**** Bali Trip Itinerary**

May 18 – June 10, 2026  ·  Scott Watts

| ✈  Flight | 🏨  Hotel | 🏠  Airbnb | ⚠  Gap / Action |
| --- | --- | --- | --- |

**Monday, May 18 — Depart Atlanta**

**✈  Flights**

| **Flight** | ATL → LAX  │  AA1256  │  Depart 16:40 → Arrive 18:38 |
| --- | --- |
| **Terminal** | Hartsfield-Jackson — Terminal N |
| **Seat / Bags** | Seat 01F  ·  2 checked bags |
| **Flight** | LAX → MNL  │  PR103  │  Depart 23:55 → Arrive May 20, 05:30 |
| **Terminal** | LAX Terminal B → NAIA Terminal 1 |
| **Seat / Bags** | Seat 04K  ·  4 checked bags (40K)  ·  14h 36m |

**Wednesday, May 20 — Arrive Manila**

| **⚠  Gap** | **Arrive 05:30 — Marriott check-in not until 15:00 (9.5 hr wait). Store bags at hotel, use Mabuhay Lounge or explore Newport/Pasay.** |
| --- | --- |

**🏨  Manila Marriott at Newport World Resorts**

| **Check-in** | Wednesday, May 20  ·  15:00 |
| --- | --- |
| **Check-out** | Thursday, May 21  ·  By 15:30 |
| **Confirmation** | 89509056 |
| **Address** | 2 Resorts Drive, Newport World Resorts, Pasay City, Metro Manila 1309 |
| **Phone** | +63-2-89889999 |

**Thursday, May 21 — Manila → Bali**

| **⚠  Note** | **Check out by 15:30 to reach NAIA T1 by 17:00 for 19:55 departure. Newport to T1 is ~20–30 min in light traffic.** |
| --- | --- |

**✈  Flight to Bali**

| **Flight** | MNL → DPS (Bali)  │  PR537  │  Depart 19:55 → Arrive 23:55 |
| --- | --- |
| **Terminal** | NAIA Terminal 1 → Ngurah Rai Terminal I |
| **Seat / Bags** | Seat 35H  ·  30K baggage  ·  4h 00m |
| *ℹ️  Alert hotel of late arrival (~00:30 AM) to confirm room is held.* |

**🏨  Le Méridien Bali Jimbaran**

| **Check-in** | Thursday, May 21  ·  ~00:30 AM (late arrival) |
| --- | --- |
| **Check-out** | Saturday, May 23  ·  12:00 |
| **Confirmation** | 75204375 |
| **Address** | Jalan Bukit Permai Jimbaran, Bali 80361 Indonesia |
| **Phone** | +62-361-8466888 |

**Saturday, May 23 — Jimbaran → Tegallalang**

**🏠  Airbnb — Home in Kecamatan Tegallalang**

| **Check-in** | Saturday, May 23  ·  14:00 |
| --- | --- |
| **Check-out** | Monday, May 25  ·  12:00 |
| **Address** | Jalan Br Jasan, Tegallalang |
| **Host** | Agus  ·  2 nights |

**Monday, May 25 — Bali (overnight) → Manila**

| **⚠  Gap** | **Tegallalang checkout 12:00 — DPS flight departs 00:55 May 26 (~12 hrs). Plan: optional stop at Tegallalang Rice Terraces, lunch in Ubud, sunset cocktails + dinner at Sundara (Four Seasons Jimbaran) or Bawang Merah beachfront seafood — both 5 min from DPS. TBD — returning to finalize.** |
| --- | --- |

**✈  Overnight Flight to Manila**

| **Flight** | DPS → MNL  │  PR538  │  Depart 00:55 (May 26) → Arrive 05:00 (May 26) |
| --- | --- |
| **Terminal** | Ngurah Rai Terminal I → NAIA Terminal 1 |
| **Seat / Bags / Class** | Seat 35H  ·  30K baggage  ·  Business Class  ·  4h 05m |

**Tuesday, May 26 — Arrive Manila (early AM)**

| **⚠  Gap** | **Arrive NAIA 05:00 — Mandaluyong Airbnb check-in was listed as May 25. Coordinate early access with Andrew or plan to wait until standard hours.** |
| --- | --- |

**🏠  Airbnb — Home in Mandaluyong**

| **Check-in** | Monday, May 25 (nominal)  ·  Actual arrival: May 26, ~06:00 |
| --- | --- |
| **Check-out** | Saturday, May 30  ·  11:00 |
| **Address** | 1550 Reliance Street, Mandaluyong |
| **Host** | Andrew  ·  5 nights |
| *ℹ️  May 26–30: Manila base — call center visits, team meetings, BPO operations.* |

**Saturday, May 30 — Mandaluyong → Malate**

**🏠  Airbnb — Home in Manila (Malate / Del Pilar)**

| **Check-in** | Saturday, May 30  ·  15:00 |
| --- | --- |
| **Check-out** | Monday, June 1  ·  11:00 |
| **Confirmation** | HM8MN9HDKY |
| **Address** | Alpha Grandview Condo, Del Pilar Street, Malate, Manila 1004 |
| **Host Phone** | +63 917 894 0336 |
| **Host** | Embassy Suites Manila  ·  2 nights |

**Monday, June 1 — Manila → Cebu**

| **🚨  ACTION REQUIRED — FLIGHT NOT BOOKED** **Manila (MNL) → Cebu (CEB)  ·  TO BE COMPLETED** Malate Airbnb checks out June 1 at 11:00. Cebu Airbnb check-in is June 1 at 15:00. No MNL–CEB flight is booked. Book immediately — PAL, Cebu Pacific, and AirAsia all fly this ~1-hour route multiple times daily. Target a departure between 11:30 and 13:30 to make the 15:00 check-in. |
| --- |

**🏠  Airbnb — Home in Cebu City**

| **Check-in** | Monday, June 1  ·  15:00 |
| --- | --- |
| **Check-out** | Tuesday, June 9  ·  11:00 |
| **Address** | India Street, Cebu City |
| **Host** | Almira  ·  8 nights |
| *ℹ️  June 1–9: Cebu base — 8 nights. Longest single stay of the trip.* |

**Tuesday, June 9 — Cebu → Manila → Seattle → Atlanta**

**✈  Cebu → Manila**

| **Flight** | CEB → MNL  │  PR2868 (PAL Express)  │  Depart 15:25 → Arrive 16:45 |
| --- | --- |
| **Terminal** | Cebu Mactan Terminal 1 → NAIA Terminal 2 |
| **Seat / Bags** | Seat 22J  ·  2 checked bags  ·  1h 20m |

| *ℹ️  T2 → T1 transfer: Allow ~1 hr for inter-terminal shuttle. 6-hr connection window is comfortable. Board NAIA shuttle at T2 arrivals, or use Grab. Mabuhay Lounge available at T1 for Business/Elite members.* |
| --- |

**✈  Manila → Seattle**

| **Flight** | MNL → SEA  │  PR124  │  Depart 22:35 → Arrive Jun 9, 20:05 |
| --- | --- |
| **Terminal** | NAIA Terminal 1 → Seattle-Tacoma Intl |
| **Seat / Bags** | Seat 06K  ·  2 checked bags  ·  12h 30m |

**✈  Seattle → Atlanta**

| **Flight** | SEA → ATL  │  AS727 (Alaska Airlines)  │  Depart 23:22 → Arrive Jun 10, 07:20 |
| --- | --- |
| **Terminal** | Seattle-Tacoma Intl → Hartsfield-Jackson Terminal N |
| **Seat / Bags** | Seat 01F  ·  2 checked bags  ·  4h 58m |

**Summary of Action Items**

| **#** | **Item** | **Action** |
| --- | --- | --- |
| **1** | **🚨  MNL → CEB Flight (Jun 1)** | **BOOK NOW — PAL / Cebu Pacific / AirAsia. Target depart 11:30–13:30.** |
| 2 | Le Méridien late arrival (May 21) | Call hotel to confirm room held for ~00:30 AM arrival. |
| 3 | Mandaluyong Airbnb early access (May 26) | Message Andrew — arriving 05:00–06:00, need early key access. |
| 4 | Bali departure evening (May 25) — TBD | Finalizing dinner plan — Sundara (Four Seasons) or Bawang Merah beachfront seafood, Jimbaran. |
| 5 | T2 → T1 Manila connection (Jun 9) | Inter-terminal shuttle or Grab — 6-hr window is comfortable. |

*Generated May 4, 2026  ·  Scott Watts  ·  Watts Way Farms*
[File uploaded: Philippines_Bali_Itinerary_2026.docx]

### CLAUDE (2026-05-10T22:57)
 You're right, I can see the itinerary right here in this conversation now — **May 18 through June 10**. That's 3.5 weeks. And I can search for the planning conversation, but the note at the top of my memory says project conversations are scoped separately, so if we planned it in a different project I can't reach it. Regardless, I have everything I need from the document.

Here's what this means for the Augusta plan:

**The training calendar reality:**

- **Now → May 18**: 8 days. Establish the habit — get some bike sessions in, one swim, keep the running going
- **May 18 – June 10**: Philippines/Bali. 24 days away. Running is easy to maintain anywhere. Bike is gone. Swim is uncertain — Cebu and Bali both have pools but consistency will be opportunistic at best. This is a maintenance block, not a build block
- **June 10**: Back home. 17 days to the half marathon on June 27
- **June 27**: Made in the USA Half — fitness check, hard effort, then recover
- **June 28 – Sept 27**: 13 weeks of real Augusta build

The trip actually clarifies things. You're not really starting a proper Augusta training block until mid-June, and the half marathon becomes your fitness baseline test rather than part of the build. 13 weeks post-half for a 70.3 is tight but workable given your history — you've done this before.

On pool/office days — you said Tuesdays and Wednesdays are office days, so OneLife near the office works on those days. What days are you typically home vs. office the rest of the week?

### SCOTT (2026-05-10T22:58)
"but the note at the top of my memory says project conversations are scoped separately," can we change that?  i like to keep proijects separte for my edifaction, but am fine with you seeing intot eh "whole me"

### CLAUDE (2026-05-10T22:58)
 Unfortunately that's not something I can change — it's a platform-level constraint, not a setting I control. Each project's memory is sandboxed by design. Even if you wanted to open it up, there's no toggle for it currently.

What I'd suggest: at the start of any conversation where cross-project context matters, just paste or summarize the key stuff and I'll work with it. The itinerary you just shared is a perfect example — now I have everything I need from that planning work regardless of where it happened.

The more practical fix is what we're already doing: building up memory in this project so that *this* becomes your primary fitness + life context hub. Over time, as you share more, I'll have a richer picture of the whole you without needing to reach across projects.

Speaking of which — a few things I should lock into memory from what you just shared before we go further:

- You leave for Philippines/Bali **May 18**, back **June 10**
- **June 27** is Made in the USA Half Marathon
- **September 27** is the target for IM Augusta 70.3 (if you register)
- Office days are **Tuesday and Wednesday**, which is when OneLife near the office is the pool option
- You're based in the **Atlanta area** (Newnan nearby, Planet Fitness, corporate gym all mentioned)

Good — that's all locked in. Now back to the actual question I asked before the itinerary arrived, which you didn't quite answer:

**Are you registering for Augusta?**

Because if yes, I want to sketch out the full training arc right now — pre-trip, Philippines maintenance, post-trip build through the half, then the 13-week Augusta block. You'll be able to see exactly what you're committing to before you hit that $525 button.

### SCOTT (2026-05-10T23:05)
I live in Hogansville, GA. My office is at Cox HQ in Sandy Springs GA. Attached are summaries from my other projects, which you can access and remember here for reference. and you can see everythign in this "Fitness & Trainign" project, correct?

[Attachment: Scott_Watts_Context_Summary - BisOps.docx]
**Project Context Summary**

Scott Watts — Blueprint RF

# Role & Overview

Scott Watts is Senior Director of Hospitality Operations (also referenced as Senior Director of Sales) at Blueprint RF. He reports directly to Jady West. His responsibilities span customer-facing compliance and governance, sales operations, vendor/BPO management, and internal team leadership.

# Key Stakeholders

## Internal

- **Jady West – **Scott's direct manager. Significant decisions and approvals are routed through Jady. Scott calibrates carefully which communications come from him vs. from Jady based on the accountability signal each scenario requires.

- **Kathy – **Peer who runs sales. Can be territorial about her team's work. Scott uses a more collegial, indirect tone with her.

- **David – **Sales rep who has underperformed and is under active management.

- **Julian Cayetano – **Manager, Technical Customer Care — direct report.

- **Kyle Davis – **CS Manager — direct report.

- **Marie Henson – **TDE Supervisor, Philippines-based — direct report.

## External

- **Tracy Miller – **Hilton Sr. Lead, Guest Facing Technologies Governance — key external compliance contact.

- **Cloudstaff / Melvin Palma – **BPO partner. Contractor JP works through this relationship.

- **CallTek / Kyle Finnelson – **Second BPO partner.

- **Charter – **High-stakes prospective/partner relationship Scott is actively managing.

# Active Situations

## Hilton Compliance

- Blueprint RF received two General Warnings from Hilton related to unauthorized Meraki Dashboard access provisioning.

- A formal compliance response document was drafted and refined, including a five-part root cause analysis, corrective action plan, and governance controls.

- Jady sends the document (authored by Scott) — this establishes Scott as the operational point of contact.

- Internal checkpoint: the MFA audit commitment in Section 4.1 needed Marie to confirm with Corey before submission.

- For removing contractor JP from the account: the recommended path is invoking Section 7 of the Cloudstaff MSA (security violation grounds) rather than attempting an unpaid suspension the contract doesn't support.

## Charter Engagement

- Scott built an executive-level presentation responding to a Charter due diligence question about national brand trouble call monitoring certification requirements.

- Framed as high-stakes — effectively a job interview with Charter senior leadership.

- Strategic calibration: position managed Wi-Fi as valuable and complex enough to warrant partnership, but not so overwhelming or simple that Charter would disengage.

## BPO Bonus Payout (CallTek)

- Scott committed to an April 2026 payout for 66 named employees fully dedicated to the Blueprint RF account.

- Eligibility tied precisely to assignment status on the actual payout date — not committed in advance for May.

## Other Active Items

- Philippines trip approval: Scott was seeking Jady's approval for an on-site visit, framing it around a prior twice-yearly agreement and BPO cost coverage.

- Springfield, MO business trip: included a QBR with Atrium and a prospecting initiative targeting local hospitality management companies, coordinated with Julian, David, and Kathy.

- 1:1 meetings reinstatement: calendar invites drafted reinstating weekly one-on-ones with direct reports, structured as employee-driven conversations with flexible agendas.

- Cosmos platform presentation: an existing deck for Charter was reviewed and detailed feedback produced for the team.

# Key Working Principles

- **Accuracy is non-negotiable. **Scott reads documents carefully and catches factual inaccuracies immediately — especially names, roles, and sequencing.

- **Avoid premature written commitments. **Don't commit to future actions or periods unless Scott has explicitly confirmed them.

- **Precision in contractual and staffing matters. **Scott proactively adds specificity clauses to protect against ambiguity (e.g., bonus eligibility tied to assignment status on payout date).

- **Hierarchy is respected and leveraged intentionally. **Direct reports are expected to find time on Scott's calendar — not the reverse. Routing decisions through Jady is deliberate.

- **Paper trail and accountability by design. **Communications are structured to create clear records. Threads are forwarded rather than summarized when the forwarded content carries accountability weight.

- **Single strong variant preferred. **For email cleanup tasks where the direction is clear, one polished draft is preferred over multiple alternatives.

- **Ingest fully before producing output. **Scott prefers that all uploaded materials be reviewed before generating a response.

- **Document format strategy. **Word for internal editing/collaboration; PDF for external submission.

# Tools & Resources

- **PptxGenJS via Node.js – **For PPTX creation. Cannot load/modify existing files; full re-run required for edits. Visual QA: PptxGenJS → LibreOffice PDF conversion → pdftoppm JPEG extraction per slide. Text extraction from uploaded PPTX files via python -m markitdown.

- **Cloudstaff MSA – **Referenced for contractor rights and obligations. Section 6(a) governs discipline authority; Section 7 governs security-based removal rights.

- **National brand standards documentation – **Marriott, Hilton, Hyatt, Choice, Wyndham, Omni — used as source material for Charter-facing deliverables.

[Attachment: FarmContext_May2026 - farm.docx]
**Scott****'****s Farm — Claude Context Summary**

Franklin, GA | As of May 2026

# **Farm Overview**

**Location: **Franklin, GA — 90-acre pasture-raised meat operation

**Ownership: **Scott and wife (wife farms full-time; all profits reinvested)

**Standards: **No antibiotics or hormones used

**Livestock: **~60 Irish Dexter cattle (grass-fed, finished on corn/BOSS/cottonseed hulls/beet pulp/Bull & Show mix); targeting ~50 piglets/year

**Products Sold: **Whole/half hogs, whole/half Dexter beef, 10 lb ground beef boxes, 10 lb pork boxes

**Distribution: **Delivery meet-ups along Atlanta–Montgomery corridor; UPS Ground shipping to 20 states

**Active Coupons: **FREEZER20, NEWAREA10

**Facebook Targeting: **Alpharetta, Johns Creek, Roswell, Cumming, Marietta, Milton (interests: farmers markets, local food, organic, homesteading, BBQ)

# **Pricing ****&**** Processing**

| **Product** | **Price** | **Kill Fee** | **Cut Fee** |
| --- | --- | --- | --- |
| Pork (HW) | $5.50/lb HW | $40 | $1.15/lb |
| Beef (HW) | $6.75/lb HW | $75 | $1.10/lb |

- Dexter HW typically 475–550 lb; whole Dexter ~$3,200–$3,700 all-in (310–360 lb take-home)

- Beef take-home rate ~65%; pork take-home ~80%

- Cut sheets released only after deposit — firm policy

# **Breeding Philosophy**

- Breed purebreds only; sell F1 market hogs; NEVER breed F1s back

- Goal: 2 litters/year/sow × 10 weaned — or sow goes to freezer camp

- Moving toward AI (artificial insemination) as primary breeding method

- Genetics supplier: Shipley Swine (AI sires used: EL Macho [Berk], No Limit, Deadbolt [Duroc])

# **Pig Breeding Herd — Current Status**

## **Boar**

**Chester: **Purebred Duroc (unregistered, $125). Castration planned if underperforming.

## **Long-Term Sows**

| **Sow** | **Breed** | **DOB / Cost** | **Recent Breeding** | **Due / Status** |
| --- | --- | --- | --- | --- |
| Hazel | Purebred Berk | 7/21/24 / $125 | Sept 12 2025 litter (13/12, sire Chester); AI Nov 7 2025 failed; not re-bred | Not currently bred |
| Mabel | Purebred Berk | 7/21/24 / $125 | Dec 3 2025 (4/3); AI Jan 21 2026 sire EL Macho (Berk) — settled | Due ~May 15 2026 — in farrow pen. Piglets will be purebred Berk |
| Scarlet | Purebred Duroc | Unreg / $125 | Chester Dec 19-20 2025 didn't settle; caught ~Jan 9-10 2026 | Due ~May 3-4 2026 — in farrow pen |
| Ginger | Reg Duroc | $250 | Chester May 2 2026 (multiple mounts, full stand) | Due ~Aug 24 2026 |
| Nutmeg | Reg Duroc | $250 | Feb 7 2026 heat didn't settle; Chester May 3 2026 partial stand | Outcome TBD — watch ~May 24 for return to heat |

## **Stop-Gap Sows (1 Litter Only — F1, Will Not Be Bred Back)**

| **Sow** | **Breed** | **DOB** | **Breeding** | **Status** |
| --- | --- | --- | --- | --- |
| Willow | F1 Berk×Duroc | Sept 12 2025 (Hazel litter) | AI Apr 2 2026 sire No Limit (Shipley) | Settle TBD |
| Goldie | F1 Berk×Duroc | Sept 12 2025 (Hazel litter) | Chester May 9 2026 — standing | Due ~Aug 31 2026 |

## **Paddock Movement (May 2 2026)**

- Moved to fresh paddock: Goldie, Willow, Hazel, Ginger, Nutmeg, Chester

- Moved to farrow pens: Mabel, Scarlet

- Farrow pens built from hog panels + t-posts + zip ties — easy to scale

## **Daily Pig Feeding (Scoops)**

| **Animal(s)** | **Scoops** |
| --- | --- |
| Chester | 2 |
| 4 girl pigs (shared) | 5 |
| Mabel | 1.5 |
| Hazel | 2 |
| Scarlet | 1.5 |
| Ava cow (pen area) | 3 |
| Cow #911 | 5 |

Note: #911 and Ava cow may need grass supplementation.

Cow #911 processed Apr 27 2026: live weight 832 lbs, HW 464 lbs, dressing % 55.77%.

# **Beef Operation**

**Current finishing batch: **Started Apr 26 2026 (~110 days feedout + 21 days hang)

**Target processor: **Mid-August 2026; product ready early September 2026

**Breed: **Irish Dexter (grass-fed, finished on grain mix)

**Typical HW: **475–550 lb; dressing % ~55–65%

# **April 2026 Pork Batch — Hazel****'****s Litter**

**Processor: **Resaca Meat Processing (invoice #2801, $1,931.63)

| **Hog** | **HW (lbs)** | **Take-home (lbs)** | **Notes** |
| --- | --- | --- | --- |
| #1 Runt | 129 | 109.44 (whole) | Lower yield — sold as boxes |
| #2 | 230 | ~202 (split halves) | Watts + Thomas |
| #3 Karr | 204 | 155.73 (whole) |  |
| #4 Burnum | 241 | 201.85 (whole) |  |

**Batch Financials (excluding runt): **HW 204–241 lb avg; ~80% take-home yield

- Revenue: ~$5,362.50 ($3,712.50 full-size hogs + $750 piglets + ~$900 runt boxes)

- Costs: Processing $1,931.63 + feed ~$884 + fuel ~$210

- Gross profit w/ runt boxes: ~$2,336 (43.6%); without: ~$1,436 (32.2%)

- Per-lb HW margin on 3 full-size hogs: ~$2.45/lb (44.5%)

- Excludes: labor, breeding stock amortization, delivery fuel, marketing, overhead

# **Pork Box Strategy (Revisit Later)**

Runt Pig #1 inventory (~107.6 lb remaining after family allocation): 29.4 lb original brat, 30 lb cheddar brat, 30 lb jalapeño & cheddar brat, 8.26 lb bacon + bacon ends/ham hocks/liver/leaf fat.

SKU concepts: Bacon & Brat (premium), Brat Sampler (workhorse), Slow Cook/Soup (clears odd cuts). Finalize when combining with prior batch inventory.

# **Farm Strategy ****&**** Direction**

- Transitioning: wholes/halves → curated boxes → retail cuts over time

- Moving toward AI-based pig breeding as primary method

- Runt/box sales meaningfully improve batch margins — curated boxes are the margin-expansion direction

# **Profit Calc Conventions**

- Feed cost: $13.50/50 lb bag ($0.27/lb)

- Grow-out hogs: ~5 lb feed/day from weaning to slaughter (~156 days for Hazel's Sept 2025 litter)

- Diesel: ~$5/gal; fuel cost ~$210/batch (Resaca is 125 mi one-way, 2 round trips = ~500 mi total)

- Truck: Chevy 2500 4x4 diesel + livestock trailer, ~12 mpg blended

- Scott and wife's labor NOT included in cost calculations

# **Equipment ****&**** Resources**

**Livestock trailer: **2011 Circle W CWT61635K bumper pull. VIN 1C9TB216XB1140130. GA title clear.

- 16' × 6' deck, ~6'6" interior height. GVWR 7,000 lbs.

- Tandem 3,500 lb leaf spring axles, electric brakes. 2" ball coupler.

- Pressure-treated pine floor. 3/16" steel, Valspar acrylic urethane paint.

- Tires ST225/75R15, 5-lug 15" wheels (5×4.5" bolt pattern). Spare on top rail. Beige.

- Capacity: ~8–10 Dexters or 10–15 market hogs within GVWR.

- Manufacturer: Circle W, 334-374-2560

**Primary Processor: **Resaca Meat Processing (hogs)

# **On The Horizon**

| **Item** | **Details** |
| --- | --- |
| Scarlet farrow | Due ~May 3-4 2026 |
| Mabel farrow | Due ~May 15 2026 — purebred Berkshire piglets |
| Nutmeg settle check | Watch ~May 24 2026 for return to heat (would confirm May 3 Chester activity didn't settle) |
| Willow settle confirm | AI Apr 2 — outcome TBD |
| Goldie farrow | Bred Chester May 9; due ~Aug 31 2026 |
| Ginger farrow | Due ~Aug 24 2026 |
| Beef batch | Processor mid-Aug 2026; product ready early Sept 2026 |
| Chester eval | Evaluate performance; castrate if underperforming |
| USDA processing | Scheduled Mar 23 2026 — confirm status |

# **Safety Note — Perilla Mint**

Perilla mint (Perilla frutescens) is present on property. Most toxic at flowering/seed stage. Pigs are less susceptible than ruminants but should be excluded from shaded fence lines, creek banks, and woodland edges where it concentrates. Watch for respiratory distress.

# **Key Principles ****&**** Rules**

- Breeding records: Always defer to Scott's date estimates over mechanical 114-day calculations. Flag discrepancy but do not override.

- F1 discipline: Willow and Goldie are stop-gaps only — never bred back.

- Yield benchmarks: Typical market hog 200–240 lb HW, ~80% take-home. Dexter beef dressing % ~55–65%.

- Cut sheets only released after deposit — firm policy.

- Use 'mid-August processor / early September ready' as reference frame for batches started late April.
[File uploaded: Scott_Watts_Context_Summary - BisOps.docx]
[File uploaded: FarmContext_May2026 - farm.docx]

### CLAUDE (2026-05-10T23:06)
 Got it — Hogansville, not Newnan (though close). And yes, I can see everything within this Fitness & Training project across conversations. It's only *other* projects I can't reach into natively — which is exactly why you just shared those summaries. Smart move.

Let me store all of this properly.

Good — I now have a much fuller picture of you. Blueprint RF day job, Watts Way Farms with your wife, Hogansville base, Cervélo on the Kickr, triathlon history, and a training project I can see end-to-end.

One thing worth noting: the Cebu leg of your Philippines trip (June 1–9) is literally visiting Marie Henson's backyard — that's where she's based. Probably not a coincidence that the call center visits are there.

Now. You've been dancing around this answer for the last hour. The trip leaves in **8 days**. The race registration is $525 and you just told me once you register you're committed. 

The data says you can do this. Your history says you've done harder things. Your setup — Kickr, treadmill, OneLife access — removes every logistical excuse.

**Are you registering for Augusta 70.3 today?**

### SCOTT (2026-05-10T23:07)
no.  Mrie is based in Manila.  Kyle is in Cebu.  That is why I am visiting both of those places.  i have over 100 call center agents and other team members via these two locations

### CLAUDE (2026-05-10T23:07)
 Corrected — Marie is Manila, Kyle is Cebu. That makes the itinerary structure make perfect sense now: Manila first (May 26–30 with Marie's team), then Cebu (June 1–9 with Kyle's team). Eight nights in Cebu reflects the heavier operational focus there.

And I'm still waiting on your answer. You leave in 8 days. Are you registering?

### SCOTT (2026-05-10T23:10)
wait just a secomd.  we are not at decison point.  you know my main goal for 2026?  what is it?  and what is my goal for 2027?  we need to balance everythign before we deicde.

### CLAUDE (2026-05-10T23:10)
 You're right to pump the brakes — I got caught up pushing toward a decision. And honestly, I *don't* know your main goal for 2026 or 2027. That's a gap. I've been looking at race data and equipment and logistics, but I don't actually know what the overarching objective is from your perspective.

Tell me. What are the 2026 and 2027 goals?

### SCOTT (2026-05-10T23:13)
omg.  you said you had access to the chats and memories inthis project.  you should now.  we have been discussing it for months.

### CLAUDE (2026-05-10T23:13)
 You're right, let me go look.

I'm not finding it in the search results — the conversations in this project don't seem to contain an explicit discussion of your 2026 and 2027 primary goals. It may have been discussed in a different project that I can't reach, or it's something we haven't actually captured in writing here yet.

I'm not going to pretend I found it. Just tell me — what are the goals?

### SCOTT (2026-05-10T23:21)
not your fault.  was chatgpt.  but you should have it now. try again...

### CLAUDE (2026-05-10T23:22)
 You're right — it's in my memory now. Let me read it properly.

It's all there. Here's what actually matters for the Augusta decision:

**2026 primary goal: Armor Build.** Reach 185–187 lbs at 15–18% BF with ~157.8 lbs lean mass. You lost 6.3 lbs of lean mass and your BMD dropped 6.9% YoY — the core concern being that marathon training was literally shrinking you. The Armor Build is the corrective.

**2027 primary goal: NYC Marathon sub-4:00**, after building a more durable body first.

And here's the central tension that ChatGPT already called out and is still true: **you can't peak Armor Build AND serious endurance simultaneously at 55.** A 70.3 in September would mean the back half of 2026 is dominated by swim/bike/run volume — exactly the training stimulus that caused the lean mass loss and BMD decline in the first place.

Augusta isn't just a scheduling question. It's potentially directly in conflict with the reason you stopped being a marathoner-only and started lifting seriously. 

So the real question isn't "can I do a 70.3" — you clearly can. It's **"do I want to spend the second half of 2026 building the body I need for 2027, or racing a triathlon?"** Those aren't the same thing. What's your honest answer?

### SCOTT (2026-05-10T23:23)
exaclt.y  my dleimina.  and idk the answer.  you know i need a "whats next" to keep me pointed in the right direction, focused and not easting shit.  simply going to the gym to build strenght doesn;t check that box, and I damn sure aint entering anysort of body-building competition...

### CLAUDE (2026-05-10T23:23)
 Yeah. This is the real tension and it's genuinely hard.

You need a *competitive target* to stay disciplined — that's just how you're wired. The data proves it. MCM, Dopey, Made in the USA — every time there's a race on the calendar, you train. Every gap between events, running drops off for weeks. The cold plunge is the only habit that survives without a race pulling you forward.

But the Armor Build *is* the goal that actually matters for your long-term health. The DEXA numbers don't lie — marathon training was quietly breaking you down. Bone density, lean mass, both going the wrong direction. At 55, that's not cosmetic. That's longevity.

So you need something that:
- Creates the "what's next" urgency that keeps you off the couch and out of the pantry
- Doesn't require 15+ hours/week of endurance volume that cannibalizes the strength gains
- Has a real competition or measurable external event attached to it
- Ideally builds *toward* NYC 2027 rather than away from it

A few directions worth considering before you decide on Augusta:

**Option 1 — Augusta, accept the tradeoff.** Do the 70.3, have a great time, hit sub-6:00, scratch the itch. Armor Build pauses for the second half of 2026. Resume full strength focus in October with NYC as the 2027 north star. You won't lose everything you've built — maintenance is possible — but it won't be a true build phase.

**Option 2 — Make the Armor Build the competition.** Your next DEXA is the event. Set a date — say October or November 2026 — and treat hitting 157+ lbs lean mass as the race. It's measurable, it's meaningful, it's genuinely harder than a 70.3 for someone wired like you. The "race" is the DEXA machine.

**Option 3 — A different race that serves the Armor Build.** Something like a Spartan or DEKA FIT — strength-and-endurance hybrid events that reward exactly the body you're trying to build. Heavy carries, obstacle work, functional strength. Checks the competitive box without the 3-hour bike rides.

**Option 4 — Half marathon series as the bridge.** Made in the USA on June 27, then another half in the fall — something like Thanksgiving or November. Keeps the running sharp for NYC prep, but the volume ceiling is low enough that strength work stays primary.

My honest read: Augusta is the most exciting option but the least aligned with what you actually said you want to build in 2026. The question is whether the excitement of "I'm doing a 70.3" is worth the cost to the Armor Build.

What's your gut telling you?

### SCOTT (2026-05-10T23:29)
these are a bit far...
[File uploaded: 1778455717030_image.png]

### CLAUDE (2026-05-10T23:29)
 Yeah, Lebanon TN and Newberry SC are both 3-4 hour drives. Not dealbreakers for a race weekend, but not ideal either.

Let me look for something closer to you.

There it is. **Atlanta Spartan Trifecta Weekend at the Georgia International Horse Park in Conyers, GA** — rolling hills, Georgia red clay, mud pits, water crossings. Conyers is about 90 minutes from Hogansville. That's a day trip, not a travel weekend.

The 2026 date already passed (March 14), but **the 2027 Atlanta Spartan is March 13, 2027** — which actually fits perfectly into the timeline. Do it as a late-winter 2027 event after the Armor Build phase, then NYC Marathon in the fall.

But here's what's actually interesting for 2026 fall: the **DEKA FIT** events. Those are gym-based, happen regularly, and are exactly the strength-endurance hybrid that rewards what you're building — 10 stations of functional movements plus a 500m run between each. No travel required, many locations around Atlanta. That could be your "what's next" placeholder while keeping the Armor Build primary.

Here's how I'd frame the 2026-2027 arc if you skip Augusta:

- **June 27**: Made in the USA Half — run it, have fun, defend the AG podium
- **Summer/Fall 2026**: Armor Build is the primary mission. DEKA event as competitive checkpoint
- **Nov/Dec 2026**: DEXA scan — measure the result of the build
- **March 2027**: Atlanta Spartan Beast — show up with the body you built
- **Fall 2027**: NYC Marathon sub-4:00

That's a coherent two-year story. Augusta is exciting but it's a detour from it.

Still want to think about Augusta, or is this starting to feel more right?

### SCOTT (2026-05-10T23:30)
i cant wit until a march 2027 event.  i need somethign for later summer or fall of this year.  where do i find these DEKA FIT events?

### CLAUDE (2026-05-10T23:31)
 

Two things jump out immediately:

**DEKA ATLAS + DEKA STRONG in Atlanta, June 19-20, 2026** at 1040 Grant Street SE. That's in 6 weeks — probably too soon given you leave for the Philippines in 8 days. But file it away.

For fall, the closest options are **Raleigh DEKA FIT & Ultra — August 23, 2026**, and **Florida DEKA FIT — September 12-13, 2026.** Raleigh is about 8 hours, Florida is more manageable depending on where in Florida.

But here's what's actually more interesting — there's a **DEKA MILE & DEKA STRONG in Tifton, GA on June 27, 2026** — which is literally the same day as Made in the USA Half. So that's out.

The DEKA FIT events are largely gym-hosted and the schedule shifts. The best place to find everything is **deka.fit** — it's their standalone site separate from Spartan, and shows all affiliate-hosted events which are more local and frequent than the big destination ones.

Honestly though — given your timeline, here's what I'd actually suggest looking at alongside DEKA: the **Raleigh DEKA FIT on August 23** is 15 weeks post-Philippines return. That's enough time to build toward it properly and it serves the Armor Build perfectly. Not a 4-hour drive either — Raleigh is about 7 hours but a reasonable flight or drive weekend.

Want me to dig into what the DEKA FIT actually tests so we can see how well it maps to what you're building?

### SCOTT (2026-05-10T23:33)
what are these?
[File uploaded: 1778455964945_image.png]
[File uploaded: 1778455985885_image.png]

### CLAUDE (2026-05-10T23:33)
 These are **affiliate-hosted DEKA events** — smaller, gym-based competitions rather than the big destination DEKA FIT weekends. And these are much closer to you.

**Columbus, GA** is about 75 minutes from Hogansville. You've got three dates there:
- September 19
- October 24  
- November 21

All at Mindset Holistic Health and Fitness. **Prattville, AL** (October 17) is about 90 minutes.

The different DEKA formats explained quickly:

**DEKA STRONG** — pure strength/power. 10 stations of functional movements (think rowing, ski erg, sled push, wall balls, etc.), no running between stations. Basically a fitness test of your strength endurance. This is the one most directly aligned with the Armor Build.

**DEKA MILE** — same 10 stations but with a 100m run between each one. Adds the cardio element.

**DEKA ATLAS** — carries and weighted movements, very farmer's-carry-adjacent. Right in your wheelhouse given your knee rehab focus on loaded carries.

Here's what I'd suggest: **September 19 in Columbus as your fall target.** That's 14 weeks after you get back from the Philippines. Enough time to build properly, close enough to drive on a Saturday morning, and it directly rewards everything you're doing in the gym right now — carries, leg press, machine rows, all of it translates.

And if you like it, October 24 and November 21 are right there as follow-ups. Cheap entry, no travel, competitive, measurable. This is your "what's next."

Interested?

### SCOTT (2026-05-10T23:35)
which is the hardest?
[File uploaded: 1778456072001_image.png]

### CLAUDE (2026-05-10T23:35)
 Based on the names and formats, DEKA FIT/Ultra is the hardest overall — but among what's available to you in Columbus, here's the honest ranking:

**DEKA ATLAS** is probably the most demanding for someone with your profile — it's all weighted carries and loaded movements, longer distances, more grip and posterior chain. Think atlas stones, sandbag carries, heavy sleds. It punishes weak spots brutally.

**DEKA MILE** is hardest aerobically — 10 stations with a 100m run between each. The running accumulates and your legs are already cooked from the stations.

**DEKA STRONG** is the "purest" strength test — no running, just 10 stations of power output. Shorter duration but maximum intensity. Think of it as a benchmark test of your actual gym fitness.

But I'd want to see the actual station breakdown before committing to that ranking — you screenshot the tab headers but not the content. Can you scroll down on the DEKA ATLAS tab? That'll show exactly what the 10 stations are, and I can tell you immediately which one maps best to what you're building and where your current weaknesses would show up.

### SCOTT (2026-05-10T23:36)
ya.  i see now. based ont he averag duration on all three being 10 mins, 25 mins, and 29 mins.  these arent; worht the drive.. :(

### CLAUDE (2026-05-10T23:36)
 Fair. 10-29 minutes of actual work for a 75-minute drive and an entry fee doesn't pass the value test for someone wired like you. You need something that *feels* like a real event, not a gym benchmark with a race bib.

Back to the drawing board. A few directions worth exploring:

**Option 1 — Savage Race.** Bigger OCR than DEKA, longer courses (5-7 miles with real obstacles), strong Southeast presence. Tends to draw a more serious crowd than Tough Mudder.

**Option 2 — A fall half marathon closer to home.** Something in October or November in Georgia or Alabama. Keeps running sharp for NYC 2027, low volume ceiling so strength stays primary, and you actually race it rather than just survive it.

**Option 3 — Reconsider Augusta 70.3 with clear eyes.** You now know DEKA doesn't scratch the itch. A 70.3 definitely does. The question is whether you're willing to accept the Armor Build tradeoff.

**Option 4 — A standalone open water swim or duathlon.** Plays to your background, shorter training commitment than a full 70.3.

Honestly — and I want you to sit with this — when you imagined having a fall event that made you excited to train every day, what did it look like? Because I think you already know the answer and we've been talking around it for the last hour.

### SCOTT (2026-05-10T23:41)
I have two main goals that trump all else: 1. (top goal) longetivty.  I want to live as long a healthy and active as I psosle can.  id do not want to go silently into the night!  2. runnign with my daughter for as long as I can keep up wiht her.  she is getting faster.  she is 29.  this is her gap year year as she is due to have a baby in July,.  but she is in for NY marathon, and I am her guide runner, and she says she wants a sub 4-hour.  Based on this.  do mu armor build, and other goals line up with this, or shoudl i be settign my targets on somethign else?

### CLAUDE (2026-05-10T23:41)
 Now we're at the real conversation. Everything else we've discussed today has been tactics. This is strategy.

Your two goals are actually perfectly aligned with each other — and they both point the same direction.

**Longevity** at 55 means: preserve bone density, build and maintain lean mass, keep the cardiovascular system strong, stay injury-free, manage inflammation. The DEXA numbers showed marathon training was working *against* this. The Armor Build is working *for* it. Strength training is the single highest-ROI activity for healthy aging. Full stop.

**Running with your daughter** — she's 29, getting faster, having a baby in July, and wants sub-4:00 in NYC. You're her guide runner. That's not a casual goal. That's one of the most meaningful things you could do with her. And to do it well, you need to be durable, not just fit. The muscular failure at mile 20 in Chicago? That's what gets fixed with the Armor Build, not with more miles.

So here's the honest synthesis:

**The Armor Build IS your primary training goal for 2026, and it directly serves both top priorities.** A stronger, heavier, more resilient Scott at the NYC start line is a better guide runner than a lighter, aerobically-trained-but-fragile Scott. Your daughter needs you to last 26.2 miles beside her, not to blow up at mile 20 again.

Augusta 70.3 is a detour. A fun one. But a detour.

What actually lines up:

- **Now through Philippines**: build the habit, 3x strength, HR-capped running
- **June 27**: Made in the USA Half — competitive, fun, defends the AG podium
- **July–November**: Armor Build is primary. Running maintenance, not marathon training
- **December**: DEXA scan. Measure the result
- **January 2027 onwards**: shift toward NYC marathon build with a genuinely stronger body underneath
- **November 2027**: NYC Marathon. You and your daughter. Sub-4:00.

That's a story worth training for every single day. The "what's next" isn't a race in September — it's your daughter crossing the finish line in under 4 hours with you beside her.

Does that land?

### SCOTT (2026-05-10T23:42)
yes.  then i think we shoudl forget about augusta, and pick a late season half or maybe even a full marathon for 2026?

### CLAUDE (2026-05-10T23:42)
 Yes. That's the right call. Augusta was exciting but it wasn't your race right now.

A late-season marathon in 2026 actually makes a lot of sense as a bridge to NYC 2027 — it gives you a real event to train toward, tests your fitness after the Armor Build phase, and gives you one more shot at dialing in the pacing and fueling before you're running it for your daughter.

A few questions to help narrow it down:

**Full or half?** A fall full marathon means your training peaks in September-October, which competes directly with the Armor Build. A half marathon keeps the volume ceiling lower and strength stays primary. Given where you are with lean mass and BMD, I'd lean half for 2026 and save the full for NYC 2027 — but it's your call.

**Timeline preference?** October gives you the most post-Philippines build time. November is more forgiving and you'd carry better fitness. December starts to crowd NYC prep.

**Geography?** You've done Chicago, London, MCM, Dopey. Anything on the bucket list in driving distance, or are you open to flying for the right race?

And one more thing worth remembering — your daughter's baby is due in July. Depending on how that goes, she may want you close in the fall. Worth factoring in whether a local race or a travel race makes more sense given that.

What's pulling at you?

### SCOTT (2026-05-10T23:43)
"Full or half?"  you tell me?  what do you recommed.  you know my goals and my motivations  you are the coach.  i want the target that best lines up with my overall top 2 goals

### CLAUDE (2026-05-10T23:43)
 Half marathon. Here's why.

**The Armor Build math doesn't work with a fall full marathon.** To run a full in October or November, you'd need to be putting in serious long run volume by July and August — right when you should be in the heart of the strength build. You cannot peak hypertrophy and marathon fitness simultaneously at 55. We've already established this. A full in 2026 forces the same tradeoff Augusta would have, just with less swimming.

**Your BMD decline is the alarm that can't be ignored.** A 6.9% drop in one year is serious. The prescription is axial loading — heavy carries, squats, weighted lunges — not 18-mile training runs. Every long run you add displaces a strength session and adds cortisol load. The Armor Build needs to run largely uninterrupted from June through November.

**A half keeps you sharp without breaking you.** You can maintain half marathon fitness on 3-4 runs per week, topping out at a 10-11 mile long run. That's compatible with 3x strength sessions. A full marathon isn't.

**It sets up NYC 2027 better.** Arriving at the NYC build in January 2027 with 15+ lbs of new lean mass, improved BMD, and a solid half marathon fitness base is the optimal starting point. You'll be durable enough to actually absorb the marathon training without shrinking again.

**The recommendation:** Find a half marathon in late October or November within driving distance. Something meaningful enough to race hard, close enough that travel doesn't disrupt the week. You run it fit, strong, and fresh — then pivot fully into NYC prep.

That's the call. Half marathon, fall 2026.

### SCOTT (2026-05-10T23:44)
let's both look.  try to stay wihin a few hours of my home

### CLAUDE (2026-05-10T23:44)
 On it.

This one jumped out immediately and I think you're going to like it.

**Chickamauga Battlefield Half Marathon — November 14, 2026. Fort Oglethorpe, GA.**

Here's why it's the right call:

- **Fort Oglethorpe, Georgia** — about 2 hours from Hogansville. Easy drive Friday night or Saturday morning
- **Voted Runner's Choice: Best Half Marathon in Georgia 2024** by RaceRaves, and designated a **2026 RRCA Georgia State Half-Marathon Championship Event.** This is a *legit* race, not a backyard fun run
- **12 miles through a 9,000-acre National Military Park** — Georgia red clay, rolling hills, historic monuments. The course is genuinely beautiful.
- **Average race day temp: low 40s at the start, low 50s by midday.** Perfect running weather. You will run fast in that
- Civil War era **cannon blast to start the race.** Come on. That's cool.
- Registration is currently **$80** — goes up June 2nd to $100. Register before you leave for the Philippines

The timing is perfect too. November 14 gives you the full post-Philippines Armor Build window through October, then a two-week taper. You show up strong, fresh, and ready to race — not beaten up from marathon training.

This is your fall race. What do you think?

### SCOTT (2026-05-10T23:48)
Here's the 2025 leaderboard for my ag.  Given what you know about me, what are my chances of being competitive here?
[File uploaded: 1778456871253_image.png]

### CLAUDE (2026-05-10T23:48)
 That's a serious AG field. Let me be straight with you.

**The 2025 M55-59 top 10:**
- 1st: 1:42:07 (7:47/mi)
- 5th: 1:47:12 (8:10/mi)
- 10th: 2:00:19 (9:10/mi)

**Where you are right now:** Your last true outdoor running fitness was the Made in the USA Half in June 2025 — 2:18 at HR 152, pacing out poorly. Your treadmill runs this week are 13-15 min/mi at HR 113-118, post-blood donation. Your aerobic threshold is HR 122, anaerobic at 150.

**The honest assessment:**

To crack the top 10 you need sub-2:00, which is ~9:09/mi. That's actually your stated goal pace — hold 9:10/mi at ≤145 bpm by late 2026. So top 10 is realistic if the training goes well.

Top 5 (sub-1:47) requires 8:10/mi. That's a different conversation — faster than your Chicago pace and sustained for 13.1 miles. Possible but would require everything to go right.

Top 3 (sub-1:46) means running at or above your anaerobic threshold for the whole race. Not where you should be targeting in November 2026 given where you're starting.

**The real goal I'd set:** finish sub-2:00, top 10 in AG. That's ambitious but achievable if the Armor Build goes as planned and your running stays consistent. It also sets a meaningful baseline for 2027 NYC prep.

Podium in this field is a stretch goal for 2027, not 2026. But sub-2:00 and competitive? Absolutely in play. Register before June 2nd.

### SCOTT (2026-05-10T23:50)
I've never aimed for the podium in any races (except 5K's as they are always balls to wall from the word go).  but i would liek to set a sub-2 target if you think is achievable

### CLAUDE (2026-05-10T23:50)
 I do think it's achievable. Here's why I'm confident saying that and not just being encouraging:

Your aerobic system is genuinely strong — VO2max 41.2, anaerobic threshold at HR 150, and your Chicago pace of 10:00/mi at HR 144 shows you can sustain effort for 26.2 miles. The problem at Chicago and at Made in the USA wasn't your engine, it was muscular durability and pacing discipline. Both of those are fixable.

Sub-2:00 is 9:09/mi for 13.1 miles. At your aerobic threshold of HR 122 you're currently running ~10:30-11:00/mi on a good day pre-donation. That gap needs to close by November — and it will, for three reasons:

**First**, RBC levels recover fully in 8-12 weeks post double-red donation. You're already faster than the numbers this week suggest.

**Second**, the Armor Build directly addresses your limiters. More lean mass, stronger quads, better patellar tendon — all of that means your legs hold form at mile 10 instead of falling apart like Chicago.

**Third**, you have 22 weeks from when you get back from Philippines to race day. That's plenty of time to build to sub-2:00 fitness without sacrificing the strength work.

The one condition I'd put on it: **pacing discipline from the gun.** Your Made in the USA data showed you at 8:47 in mile 1 with HR already at 148. That race was lost in the first 3 miles. Sub-2:00 means going out at exactly 9:00-9:05/mi and holding it, even when it feels embarrassingly easy early on.

Sub-2:00. November 14. Chickamauga. Register before June 2nd when the price jumps. That's the plan.

### SCOTT (2026-05-10T23:58)
that is still almost 4 hours away.  what about one of these.  a littel closer.. 

https://findarace.com/us/events/taco-sloth-1m-5k-10k-13-1-26-2-now-only-12

https://findarace.com/us/events/gobbler-5k-10k-13-1m-at-piedmont-al-45

or this one  I am a veteran:

https://runsignup.com/Race/GA/Kennesaw/SaluteToVeteransKKHalfMarathonAtlanta?aflt_token=vkmwDmweQ4iCYn8otSOOnKQ3vCO8buOw

### CLAUDE (2026-05-10T23:58)
 

Here's the breakdown on all three:

**Taco Sloth — McDonough, GA** — January 31, 2026. That's already past. Dead end.

**Gobbler — Piedmont, AL — November 7, 2026.** About 90 minutes from Hogansville. Small local race, community feel. Nothing wrong with it but I couldn't find race history or AG results to gauge the competition level. It's a week before Chickamauga.

**Salute to Veterans — Kennesaw, GA — November 14, 2026.** As a veteran, **you race for free**. Kennesaw is about 75 minutes from Hogansville — much closer than Chickamauga. Age group awards in 5-year brackets, finisher medal, race shirt. The cause is meaningful too.

Here's the thing though — **November 14 is the same date as Chickamauga.** So it's one or the other.

My honest comparison:

| | Salute to Veterans | Chickamauga Battlefield |
|---|---|---|
| Distance from home | ~75 min | ~2 hrs |
| Cost | **Free (veteran)** | $80-100 |
| Course | Unknown quality | Rated best in GA |
| Competition | Smaller field | State championship field |
| Meaning | Veteran tribute | Historic battlefield |

For a sub-2:00 goal with AG competitiveness in mind, Chickamauga's state championship field gives you a better read on where you actually stand heading into NYC prep. But free is free, and 45 minutes closer matters on race morning.

Which pulls at you more?

### SCOTT (2026-05-10T23:59)
somethign not 4 hours away...

### CLAUDE (2026-05-10T23:59)
 Fair — I keep coming back to Chickamauga and you keep telling me it's too far. Let me actually find something closer.

Okay, I found something genuinely interesting. Here are your two best options, both within striking distance:

---

**Option 1 — Area 13.1 Half Marathon, Roswell GA — August 15, 2026**

Voted **2024 Best Half Marathon in Georgia**, ranked **Top 50 in the USA**. Flat and fast — only 240 feet of elevation gain. **Night race, 7pm start**, along the Chattahoochee River. Roswell is about 90 minutes from Hogansville.

The catch: it's hot at the start — still over 90° in Atlanta in August, and it's only 10 weeks after you get back from the Philippines. That's tight for a sub-2:00 attempt. It'd be more of a fitness test than an all-out race.

---

**Option 2 — Salute to Veterans Half Marathon, Kennesaw GA — November 14, 2026**

**Free entry as a veteran** (ID required). 75 minutes from Hogansville. Age group awards in 5-year brackets. Meaningful cause, low cost, close to home.

---

**My recommendation:** do **both**. 

- **August 15 — Area 13.1** as a fitness checkpoint. Race it at controlled effort, see where you are 10 weeks post-Philippines, don't blow up chasing sub-2:00 in the heat.
- **November 14 — Salute to Veterans** as your real target. Fresh legs, cool weather, free entry, 75 minutes from home. That's where you go sub-2:00.

Two races, clear purpose for each, neither one derails the Armor Build. What do you think?

