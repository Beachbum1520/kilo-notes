# Weekly workout tracking prompt template
Date: 2026-05-29
Conversation: a37698ed-d984-42ee-8a6b-b5090d9a1321
Domain: fitness-training

## Summary
**Conversation Overview**

Scott outlined a recurring weekly workflow he wants to establish with Claude acting as his coach: each week he will open a new conversation, upload completed workouts as they happen, add relevant observations and context, and then work with Claude to analyze the week and build the next one or two weeks of scheduled training. The conversation focused on designing a reusable kickoff prompt he can paste at the start of each new weekly chat to ensure Claude immediately loads all relevant memory and Drive files before responding.

The session involved iterative refinement of that kickoff prompt. Claude drafted an initial version, then flagged a structural conflict Scott had not explicitly raised: the strength block non-negotiable he described as a fixed three-day split (Tue=Legs, Wed=Pull, Fri=Push) was already superseded by his settled commitment to a four-day RP "Armor Build M1" mesocycle starting June 15 (Mon=Push, Tue=Lower A, Wed=Pull, Fri=Lower B). Claude rewrote the strength invariant to reference the current active block dynamically and documented the transition explicitly within the prompt itself so it is self-contained. Scott also pushed back on the line "HR cap always overrides pace," directing Claude to search memory and prior chat context around this topic and his recent blood donation. Claude corrected the rule to distinguish between easy and aerobic runs (where the HR cap governs and pace is secondary) versus prescribed quality sessions (where pace and effort are the target and HR rises to the session ceiling). The post-donation HR cap of 122 was clarified as a temporary recovery constraint tied to a May 6 donation, not a permanent zone boundary, and the prompt was updated to require Claude to confirm recovery status before prescribing each week rather than treating 122 as a standing rule. Scott approved the final version without further changes.

Scott's stated preferences throughout: no coach-speak, no emojis, no ranges or vague values in TrainingPeaks output — every segment must have exact HR, pace, and a single mph treadmill value. He wants Claude to own coaching calls and push back when his choices conflict with his goals, and he expects Claude to surface tool failures (such as Drive connector issues) plainly rather than work around them silently. His two primary training objectives are the RP Armor Build goals (lean mass, bone mineral density, axial loading) and the NYC 2027 sub-4:00 guide-runner arc.

### SCOTT (2026-05-29T23:26)
So I think that going forward I want to start a new convo each week where I will upload the weeks scheduled workouts as they are completed and I have time. The. I can also add any relevant insights to this same convo. From there we can discuss and analyze the week with the goal of developing the following week or two schedule that aligns with for formations, scheduling right workouts for right days and adequate progressions toward my goals. 

So all of that said, is there an initial prompt I should save and use to kick off each new week?  A prompt that ensure ls you are calling on all the right memories and other established inputs?

### CLAUDE (2026-05-29T23:27)
 Scott wants a reusable kickoff prompt template he can paste at the start of each weekly conversation to make sure I'm pulling in all the relevant context and previous work. This is about designing a prompt structure that fits his workflow—uploading workouts as they're completed, adding observations, analyzing the week, and planning ahead—rather than needing to access his data right now.

The prompt needs to trigger me to retrieve his memories and Drive files, establish the non-negotiables that should stay active in our conversation, clarify what he'll provide and what he expects back, and account for his current situation: recovering from blood donation, wrapping up before his Philippines trip on June 10, and starting the Armor Build M1 RP Strength mesocycle on June 15. I'll write something clean and direct that matches his preference for no fluff or coach-speak—just executable instructions he can save and reuse. I'm torn between inline and artifact format, but for a single reusable prompt block that Scott needs to grab and paste weekly on mobile, a code block inline is faster and more practical than opening a file. Now I need to design the actual prompt itself — it should be lean and guide me through the right steps each week, starting with loading memory and pulling the Drive folder, anchoring to current context, and laying out what needs to happen.

The tricky part is balancing brevity with guardrails. Memory should auto-load, so I don't need to restate everything, but restating the highest-risk scheduling rules as a safety check is worth the space. I'm drafting something that triggers the right mode and relies on memory for the bulk of context rather than bloating the prompt itself. I'm laying out the hard constraints that govern the training week — strength days locked to specific days, no running on office days, cold plunge timing, protein baseline, and the non-negotiable TrainingPeaks format with exact metrics for every segment.

Now I need to pull the current phase and week from memory to see what's actually scheduled, then flag any conflicts between the stated rules and what's been programmed into the Armor Build mesocycle starting June 15. I see the real issue here—he's got a 3-day structure he mentioned as non-negotiable, but he actually built and committed to a 4-day RP Strength program starting June 15. As his coach, I need to flag this contradiction rather than let it slip into the prompt, especially since he explicitly asked me to push back on conflicts. I should deliver the kickoff prompt he requested but also surface this mismatch so we're not hardcoding something that contradicts his actual settled plan.

The timeline clarifies it: Philippines trip through June 10 means Fitbod maintenance-only during travel, then the 4-day RP Armor Build M1 kicks off June 15. So the "Tue=Legs, Wed=Pull, Fri=Push" structure he mentioned is the old framework—the prompt should reference his current strength block dynamically rather than hardcoding days that'll be wrong once June 15 hits. I need to rethink the prompt design here. Rather than hardcoding the strength block schedule, which will become outdated, I should ask him to confirm which program I'm currently following and let that drive the day-mapping. I'll keep only the truly stable constraints—the nutrition targets, HR limits, activity restrictions on office days, and the cold plunge timing—and flag the June 15 transition directly so he's aware of the conflict.

I don't need to pull Drive right now since he's asking me to design the prompt, not analyze anything this week. The prompt itself will instruct me to check Drive when it's actually needed. I could mention that if the Drive connector acts up at kickoff, I'll flag it rather than work around it silently, but I won't waste a tool call testing it now—that's not what he asked for.

For the format, he wants it mobile-friendly and copy-paste ready, so I'll put the prompt in a code block and keep my explanation brief. I'm focusing on the one thing I changed and why, keeping the whole response to about a screenful. The prompt itself needs to be tight and match his preference for no-fluff writing.

I'm also building in the two-year arc and current-state awareness without hardcoding dates that'll go stale. The prompt should instruct me to state what phase we're in. And since he wants to ensure I'm calling on all the right memories and inputs, I'll add an explicit line that tells me to load memory, pull from Drive, and confirm the phase before responding. I'm locking in the non-negotiables that govern everything: no running on office days, cold plunge six mornings a week before workouts, strength work stays locked to the current block with lower body only on Tuesdays, protein floor of 200g, and heart rate always trumps pace targets. I need to confirm which strength phase you're actually in right now since the block switches mid-June, and I'm tracking everything through TrainingPeaks.

For the output itself, I'm building a fully executable plan with no ambiguity—every segment gets a specific heart rate cap, exact pace, and single mph value for the treadmill, nothing vague or coach-speak. I'll start by pulling your current week and phase from memory and Drive, then ask only for the specific gaps I need filled in.

I'm catching that you clarified the strength split—your settled RP Armor Build M1 starting June 15 is actually Mon Push, Tue Lower A, Wed Pull, Fri Lower, which doesn't match the Tue Legs / Wed Pull / Fri Push pattern from earlier, so I'm adjusting the rule to match what you're actually running.Here's a kickoff prompt built for your workflow. It's written as a directive to me, so pasting it at the top of each new weekly convo forces me to load the right context before I say anything.

```
WEEKLY COACHING KICKOFF — Week of [DATE]

You're my coach. Before you respond:
1. Load all project memory and treat it as active context — goals, physiology, history, constraints, formats.
2. Pull my current files from the "Scott Watts 2026 ATP Data" Drive folder: completed workouts, test data, planning docs. Don't wait for uploads. If Drive won't respond, say so plainly — don't work around it silently.
3. Before anything else, tell me where I am in the arc: today's date, current phase, recovery status, which strength block/meso + week I'm in, days out from the next race, and any active travel.

What I'll give you this week:
- Completed workouts from the past week (uploaded as I get to them)
- Insights, symptoms, sleep/HRV, work + travel + farm context

What I want back:
1. Week analysis — what landed, what slipped, trends against Armor Build (lean mass, BMD, axial loading), aerobic efficiency, and recovery (sleep/HRV). Call out stress accumulation.
2. Next 1–2 weeks scheduled — right workout, right day, real progression toward Armor Build now and the NYC 2027 sub-4:00 guide-runner arc.
3. Push back where what I did conflicts with where I'm going. Own the call. "I don't want to" doesn't move you.

Invariant rules — apply without asking, never violate:
- No runs on office days (Tue/Wed). Treadmill = home only.
- Cold plunge 6x/week, first thing AM, every day except Wed. Never after a workout.
- Strength stays on my current active block — confirm which one you have me in. Lower/Legs only ever Tuesday.
- 200g protein floor. HR cap always overrides pace.
- TrainingPeaks output: copy/paste ready, fully executable, every segment has HR + pace + mph (treadmill, single exact value), no ranges, no missing values, no coach-speak, no emojis.

Start by pulling memory + Drive and telling me my week/phase. Then ask only for what you're missing.
```

One catch before you save it. Your message listed the strength non-negotiable as **3x: Tue=Legs, Wed=Pull, Fri=Push** — but that's your *old* structure. The block you settled on, RP "Armor Build M1," is **4-day starting June 15: Mon=Push, Tue=Lower A, Wed=Pull, Fri=Lower B.** So from June 15, Push moves to Monday and Friday becomes a second lower day for bone density.

If I hardcoded "Fri=Push, strength 3x" into the prompt, I'd be wrong every week from June 15 on. So I wrote the strength rule to point at your *current active block* and confirm which one I have you in — the 3-day Fitbod structure holds through the Philippines trip, then the 4-day RP meso takes over. The thing that stays invariant either way is Lower/Legs on Tuesday only.

Want me to bake the explicit June-15 transition (3-day → 4-day) into the prompt so it's self-documenting, or keep it lean and let memory carry that?

### SCOTT (2026-05-29T23:29)
Good. But “HR cap always overrides pace.” I don’t think is accurate. Search memory and other chats around this and my blood donation

### CLAUDE (2026-05-29T23:30)
 Scott is pushing back on the HR cap override rule and wants me to look through our past conversations to find context around this and his blood donation history. I should search my memory for relevant discussions.

 I'm finding the critical distinction Scott made about HR training zones — 122 isn't actually a hard guardrail but rather a boundary marker for controlling workout intensity, while his real physiological guardrails are based on heart rate caps tied to specific goals, like staying at or below 145 for efficiency work and keeping most volume sub-threshold.

Now I'm realizing the nuance he's pushing back on: when I said "HR cap overrides pace," I meant it as an absolute rule, but the 122 cap itself is temporary and context-dependent — it's a post-donation recovery measure he should follow through early June, then reassess and potentially increase. So the real issue is that "always" doesn't apply to the current 122 limit; it's a temporary constraint, not a permanent principle. Looking at the HR zones and thresholds, 122 is the aerobic threshold marking the top of Z2, so the principle isn't that HR always overrides pace—it's that on easy/base work the HR cap governs, but quality sessions intentionally push past it to hit the prescribed effort. I need to give Scott the corrected framing and own the inaccuracy in the original prompt. I'm clarifying the rule structure for Scott: easy runs follow the HR cap, quality sessions follow the prescribed pace/effort with HR allowed to rise to the session ceiling, and the current 122 cap is temporary post-donation recovery through early June, not a permanent zone boundary. I'll keep the response concise since this is a substantive coaching question but he prefers brevity on mobile.You're right, and the chats back you up. "HR cap always overrides pace" overstates it in two ways:

**The "always" is wrong.** That principle only governs easy/base/aerobic volume — where the cap holds and pace falls where it falls. On prescribed quality sessions (threshold, intervals, race-pace), the logic flips: pace or effort is the target and HR is *allowed* to climb to the session ceiling (≤145 for your efficiency work, up toward threshold ~150 for harder efforts). If "HR cap always overrides pace" were a real invariant, you could never run a quality session.

**The current cap is temporary, not a rule.** The 122 you're living under right now is a post-donation recovery measure — you donated May 6, and the plan was to hold 122 through ~June 6, then retest a 30-min run at HR 120–125 and open the throttle if pace is back under 12:00/mi. Separately, you corrected me on May 14 that 122 itself is a *zone boundary* (your aerobic threshold / top of Z2), not a guardrail. So baking "122" or "HR cap always" into a standing weekly prompt would have me coaching a temporary constraint as if it were permanent.

Here's the corrected invariant line for the prompt:

```
- On easy/aerobic runs, HR cap governs — pace is whatever pace is. On prescribed quality sessions, pace/effort is the target and HR rises to the session ceiling (≤145 efficiency, up toward threshold for hard work). The current post-donation cap is temporary (donated May 6) — confirm where I am in recovery before prescribing, don't treat it as permanent.
```

That also forces me to do the right thing each week: check recovery status before I prescribe, rather than reflexively slapping 122 on everything.

Want me to drop that into the full kickoff prompt and hand you the clean final version to save?

### SCOTT (2026-05-29T23:33)
Yes

### CLAUDE (2026-05-29T23:33)
 Now I'm putting together the final version of the kickoff prompt with the corrected HR information, keeping it as a single block for easy copying, and making sure the strength block transition from the earlier discussion is factored in properly—the strength rule will point to the current active block so it handles the June 15 shift from 3-day to 4-day smoothly.Here's the clean final version to save and paste at the top of each new weekly convo:

```
WEEKLY COACHING KICKOFF — Week of [DATE]

You're my coach. Before you respond:
1. Load all project memory and treat it as active context — goals, physiology, history, constraints, formats.
2. Pull my current files from the "Scott Watts 2026 ATP Data" Drive folder: completed workouts, test data, planning docs. Don't wait for uploads. If Drive won't respond, say so plainly — don't work around it silently.
3. Before anything else, tell me where I am in the arc: today's date, current phase, recovery status, which strength block/meso + week I'm in, days out from the next race, and any active travel.

What I'll give you this week:
- Completed workouts from the past week (uploaded as I get to them)
- Insights, symptoms, sleep/HRV, work + travel + farm context

What I want back:
1. Week analysis — what landed, what slipped, trends against Armor Build (lean mass, BMD, axial loading), aerobic efficiency, and recovery (sleep/HRV). Call out stress accumulation.
2. Next 1–2 weeks scheduled — right workout, right day, real progression toward Armor Build now and the NYC 2027 sub-4:00 guide-runner arc.
3. Push back where what I did conflicts with where I'm going. Own the call. "I don't want to" doesn't move you.

Invariant rules — apply without asking, never violate:
- No runs on office days (Tue/Wed). Treadmill = home only.
- Cold plunge 6x/week, first thing AM, every day except Wed. Never after a workout.
- Strength stays on my current active block — confirm which one you have me in. Lower/Legs only ever Tuesday. (Fitbod 3-day through the Philippines trip; RP "Armor Build M1" 4-day from June 15: Mon=Push, Tue=Lower A, Wed=Pull, Fri=Lower B.)
- 200g protein floor.
- On easy/aerobic runs, HR cap governs — pace is whatever pace is. On prescribed quality sessions, pace/effort is the target and HR rises to the session ceiling (≤145 efficiency, up toward threshold for hard work). The current post-donation cap is temporary (donated May 6) — confirm where I am in recovery before prescribing, don't treat it as permanent.
- TrainingPeaks output: copy/paste ready, fully executable, every segment has HR + pace + mph (treadmill, single exact value), no ranges, no missing values, no coach-speak, no emojis.

Start by pulling memory + Drive and telling me my week/phase. Then ask only for what you're missing.
```

I baked the June-15 strength transition right into the rule so the prompt is self-documenting — you won't have to remember to tell me when Push moves to Monday. Everything else stays lean.

One honest flag so it doesn't surprise you mid-week: the Drive connector has historically been unreliable in-session (read worked, write failed with a permissions error). The prompt tells me to surface that immediately rather than fake it, but if you want guaranteed file access, dropping the week's files straight into the convo is the sure path.
