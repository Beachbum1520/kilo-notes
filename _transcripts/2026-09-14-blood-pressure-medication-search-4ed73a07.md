# Blood pressure medication search
Date: 2026-09-14
Conversation: 4ed73a07-88b5-4345-ba8c-31f84fc72a15
Domain: health

## Summary
**Conversation Overview**

Scott Watts initiated a conversation asking Claude to search prior chats related to a wellness tracking topic. Claude surfaced context from previous conversations, confirming that Scott takes Losartan 50mg once daily (confirmed 6/23/2026) and has no current statin prescription — a prior open action item about statins was noted as already resolved in a 6/30 coaching chat and flagged for removal from his active list.

Scott then launched a new project to systematically track blood pressure readings across both arms, motivated by a suspected difference in systolic readings between left and right arm. The goal is to generate clean, trended data to bring to a prescriber conversation rather than relying on a hunch. Claude drafted a detailed project instruction card (v1) in Scott's preferred terse, direct format — consistent with how his other project cards are written. The card covers protocol (paired readings, alternating arm order, seated position, rest period, caffeine/exercise exclusions), data handling (running interarm delta, trend direction, protocol-deviation tracking, weekly rollups), escalation thresholds for concerning readings, and standing context about his current wellness regimen. Claude also raised a practical open question about whether Scott is using a single cuff moved between arms or two separate devices, noting that sequential different-device readings introduce noise relevant to interpreting small interarm differences.

Scott's stated communication preference across his projects is direct and terse with no hedging or coach-speak — state numbers and trends plainly, flag errors immediately, and avoid softening language.

### SCOTT (2026-09-14T13:04)
Search all chats related to my blood pressure.

### CLAUDE (2026-09-14T13:04)

This resolves the "Confirm statin" open item — it's already closed and can drop from your action list.

**Blood pressure: Losartan Potassium 50mg, 1 tab/day** — confirmed 6/23/2026, logged into the memory card.

**Statin: NONE currently.** You were on one years ago when heavier, dropped it after weight loss. That "confirm statin" action item was closed in the 6/30 coaching chat — it shouldn't still be on your open list.

Want me to strike it from the v3-FINAL card now, or are you doing a broader cleanup pass on the two diverging v3 cards first?

### SCOTT (2026-09-14T13:07)
I’m going to start a new project track my BP. I think I have a difference in sys reading between left arm and right arm. Help with the project instructions. I am going to try an take left and right arms readings at least morning and evening if not more.

### CLAUDE (2026-09-14T13:07)
Draft below — same terse/direct format as your other project cards. Paste and adjust arm-order/cuff specifics if I've got the equipment wrong.

---

**PROJECT INSTRUCTIONS — SCOTT WATTS BP TRACKING (v1)**

You are tracking my blood pressure data to identify patterns, flag anomalies, and prep me for the conversation with my prescriber about the interarm differential.

**1. PURPOSE**
Primary question: is there a persistent, clinically meaningful systolic (and diastolic) difference between left and right arm? A sustained gap ≥10 mmHg systolic is the threshold generally flagged as worth investigating (vascular/subclavian concern) — not diagnosing here, just tracking toward that threshold so I walk into the appointment with data, not a hunch.

**2. PROTOCOL (log every reading against this)**
- Both arms, same sitting, back-to-back — note which arm first (alternate order each session to cancel order-effect).
- Minimum: morning + evening daily. More if I log them.
- Seated, back supported, feet flat, arm at heart level, 5 min rest before first reading, no caffeine/exercise in the prior 30 min — flag any reading where I note a protocol deviation, don't silently average it in with clean readings.
- Log: date, time, arm order, L sys/dia/pulse, R sys/dia/pulse, any deviation notes.

**3. WHAT YOU DO WITH THE DATA**
- Running interarm delta (L−R) for sys and dia, trended over time — not just single-reading deltas.
- Flag any single reading ≥10 mmHg interarm sys delta immediately, not buried in a weekly summary.
- Flag if the delta is consistently one direction (same arm higher every time) vs. noisy/random — consistency is the signal that matters more than any one number.
- Track against Losartan 50mg/day dosing — note timing of readings relative to dose (pre-dose trough vs. post-dose).
- Weekly rollup: avg L, avg R, avg delta, trend direction, any protocol-deviation readings excluded from the trend calc but listed separately.

**4. ESCALATION TRIGGERS — surface these plainly, don't soften them**
- Any single reading ≥180/120 (hypertensive crisis threshold) — flag as "call provider now," not a data point.
- Interarm sys delta ≥15 mmHg on a clean (protocol-compliant) reading.
- Consistent ≥10 mmHg delta same-arm-high pattern over 2+ weeks.

**5. STYLE**
Same as fitness project: direct, terse, no hedging, no coach-speak. State the number and the trend, not reassurance. Own errors in the running average immediately if I correct a logged value.

**6. STANDING CONTEXT**
- On Losartan 50mg/day for BP (confirmed 6/23/2026, no statin currently).
- This is educational/tracking prep for a live conversation with my prescriber — not a diagnosis.

**OPEN ACTION ITEMS**
- Establish baseline: first 2 weeks of clean paired readings before drawing any conclusion on the interarm delta.
- Bring the trended data to next prescriber visit.

---

One thing to nail down before you start logging: what cuff are you using, and is it validated for both arms (same cuff, moved) or two separate devices? Sequential-different-device readings introduce noise that'll muddy a small delta.
