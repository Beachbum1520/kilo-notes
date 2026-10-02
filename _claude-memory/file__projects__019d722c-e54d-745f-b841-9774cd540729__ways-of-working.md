---
name: ways-of-working
description: How to work with Scott — communication style, workout/card delivery formats, logging conventions, equipment corrections, and data workflow
sources: [backfill, chat]
aliases: [logging conventions, delivery formats]
---

## Communication style

- [stated] Direct, terse, frequent typos. Corrections are immediate and firm — absorb them cleanly without defense or backsliding
- [stated] "Yup. Yup. Yup." = clean close
- [stated] No hedging, no coach-speak, no emojis, no moralizing, no repeated caveats on settled topics, no unsolicited regulatory lectures (he works with a progressive physician)
- [stated] Corrections are to be owned, not defended
- [stated] Under pushback: hold correct positions with reasoning. Do not revise a correct answer simply because Scott expresses skepticism — he may be testing or venting. Concede only on a legitimate factual correction
- [stated] Never fabricate run numbers; always parse or use the Garmin FIT Capture doc
- [stated] Don't re-propose dropped races, retired apps, or settled decisions
- [stated] Never present two conflicting working weights in the same message

## Workout delivery

- [stated] One day or one exercise at a time — never front-load multiple days; errors in bulk dumps force scrolling and rework
- [stated] RP exercise notes format: `## lbs (stack/dial or spelled-out plates per side) – ## reps – ## RIR – notes/cues`, pasted into each RP exercise Notes field for the week. Set count leads every line
- [stated] DON'T-MAKE-ME-GUESS RULE: on every barbell/trap-bar/plate-loaded-sled lift, spell out exact plate math per side in plain English (e.g. "45 bar + two 45s and a 10 each side = 245"). Machines = "set dial/pin to X lbs, no math"

## TrainingPeaks card format

- [stated] One activity per card — cold plunge is its own separate card, NEVER appended
- [stated] Header: "Location – Type – Duration / Distance." Run headers carry duration AND distance
- [stated] Run blocks: "X min – Zone X (HR bpm | pace min/mi | exact single mph)." Treadmill runs include exact mph; outdoor omits mph
- [stated] Strength: "Strength – RP Push/Pull/Lower – 1:00." Cold Plunge: "Cold Plunge – 0:03:00 – 56°F"
- [stated] Notes: shoe, fed/fasted
- [stated] Farmer's Carry + Dead Hang are RP custom exercises (Farmer's Carry = Traps/Dumbbell, log 80 lb in weight + steps in reps; Dead Hang = Forearms/Bodyweight, log seconds in reps, thumbs-on-top). They sync through the strength session — do NOT also write standalone TP cards (no double-log)

## Equipment and logging corrections (permanent)

- [stated] MTS machines at Newnan (Chest Press, Incline, Shoulder Press) = selectorized with independent stacks; log as TOTALS (160 = 80/side). M1 numbers are valid — do NOT re-anchor
- [stated] Hack squat at OneLife Perimeter = Cybex plate-loaded sled; log PLATE WEIGHT ONLY (carriage adds unlisted resistance; numbers don't cross to stack machines)
- [stated] Nautilus hack sled at Newnan and Cybex sled at Perimeter = separate ledgers, never cross
- [stated] Chest-supported row at Newnan = plate-loaded Nautilus, not pin-loaded; single center horn — all plates on one side (middle), never "each side"
- [stated] Farmer's carry steps: 22 out and back = 44 total (not 22 total)

## Bailey communications

- [stated] Warm but concise tone; brief pleasantries, plain language, no technical codes or clinical jargon
- [stated] Deliver portal message drafts as downloadable files, not inline

## Data workflow

- [stated] Pull Oura, Withings, and Garmin data directly from Google Drive — do not ask Scott to self-report numbers he has already provided
- [stated] FIT file parsing requires a session with code execution (Python). If it fails, Scott parses FIT files in a separate sandbox Claude chat and pastes the Garmin FIT Capture doc — that doc is the authoritative substitute
- [stated] FitnessSyncer pipeline lags ~1 day

## Thread workflow

- [stated] Keeps one weekly-coaching thread going until it's full rather than starting a new one each week; uses a New Thread Start command once per new thread (names the previous thread) and a Weekly Kickoff command at the start of each week, both saved in his notepad