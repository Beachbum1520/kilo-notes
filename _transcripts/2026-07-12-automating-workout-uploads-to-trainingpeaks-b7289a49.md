# Automating workout uploads to TrainingPeaks
Date: 2026-07-12
Conversation: b7289a49-b885-43fb-a910-efd2fe02984a
Domain: wattsway-app

## Summary
**Conversation Overview**

The person shared a link to the TrainingPeaks API documentation and asked whether WattsWay should apply for API access, acknowledging low approval odds but expressing interest in eventually automating workout writes directly to the TrainingPeaks platform. Claude fetched the API page, assessed the opportunity, and provided a clear recommendation to apply despite the low odds, since the effort is minimal and the API supports exactly the desired functionality — pushing planned structured workouts to athlete calendars and reading completed workout data back for plan adjustment feedback loops.

Claude flagged a key framing consideration: the API is restricted to commercial fitness applications and explicitly excludes personal use, so the application must position WattsWay as a platform in development rather than a personal project. Claude noted that WattsWay has supporting infrastructure (live domain, privacy and terms pages, three data integrations) that strengthens the application. A ready-to-submit copy-paste draft was provided for the application's "what you'd like to achieve" field, using WattsWay's actual deployed details. Claude also recommended using "Watts Way Fitness" as the company name to match prior API registrations (specifically Garmin). The form was found to be in a paused state similar to Garmin's developer program, but Claude recommended submitting anyway to secure a queue position. Claude noted this is now the second paused API on the list alongside the Garmin ticket filed July 10, and that neither changes the current roadmap — the auto-sync scheduler remains next up, with TrainingPeaks push slotting into the plan builder phase if access is granted.

### SCOTT (2026-07-12T23:27)
See this link.  proaBLY A LOW CHANCE OF BEING APPROVED, BUT THINK WE SHOUDL TRY?  ONE DAY WOULD BE COol if we could auton write the workuts to tp.

https://help.trainingpeaks.com/hc/en-us/articles/234441128-TrainingPeaks-API

### CLAUDE (2026-07-12T23:27)
Scott mentioned a TrainingPeaks API opportunity with slim odds of getting approved, but it's something he's been wanting—the ability to automatically write workouts directly to the platform. I should grab that link he shared first.

The API requires developer approval and is restricted to commercial fitness applications, explicitly excluding personal use—which is the real barrier here since WattsWay is a family-only invite platform. It does support pushing planned workouts though, which is exactly what Scott needs. I should apply anyway since it's just 15 minutes of effort and the worst outcome is a rejection, but I need to be honest about WattsWay's status: frame it as a fitness platform in development with potential commercial direction, not as a personal project.

The app has real infrastructure—a domain, privacy and terms pages—which actually strengthens the application since those were added with API registration in mind. If the API rejects us, there's a fallback: TrainingPeaks accepts manual file uploads, and Kilo's output already targets TrainingPeaks format anyway, so the workflow aligns with the roadmap. I'll give Scott a single clear recommendation and a ready-to-submit application draft he can copy-paste directly.Yes, apply. It costs you 15 minutes and the worst outcome is a form rejection email. But go in clear-eyed:

**The blocker:** the API is available for approved developers only, aimed at developers of commercial fitness applications or devices, and access is explicitly not available for personal use. A "family app for four people" application gets rejected. An "early-stage fitness platform" application has a shot.

**Why it's worth trying:** the API does exactly what you want — it can push planned workouts to an athlete's TrainingPeaks calendar and upload completed workout files. That's the auto-write-workouts-to-TP dream, natively supported. It also reads back metrics and completed workouts, which would feed the plan builder's feedback loop. Note your coach-system-prompt.md already outputs TrainingPeaks format — this API is the missing wire.

**How to frame it (honestly):** WattsWay is a real deployed product — live domain, auth, privacy and terms pages (you added those for exactly this kind of registration), three data integrations, and a stated possible commercial path. Apply as WattsWay the platform, not Scott the individual. Don't claim revenue or users you don't have; do describe the roadmap.

**Application:** submit at https://api.trainingpeaks.com/request-access, and expect 7–10 days for a response.

Copy-paste draft for the "what you'd like to achieve" field:

> WattsWay (wattsway.com) is a fitness platform in active development that aggregates wearable data (Garmin, Oura, Withings) into per-athlete dashboards and generates adaptive two-week rolling training plans with an AI coaching layer. We are pre-launch, invite-only, with a commercial path under evaluation.
>
> With the TrainingPeaks API we would: (1) push planned structured workouts from our plan builder to athletes' TrainingPeaks calendars, (2) read completed workout data and metrics back to close the plan-adjustment feedback loop. Our privacy policy and terms are live at wattsway.com/privacy and wattsway.com/terms.

**Set expectations:** low approval odds today, and it changes nothing on the current roadmap either way. Auto-sync scheduler stays next. If approved, TP push slots in alongside roadmap #4 (plan builder) — same place the workout output already lives.

One decision before you submit: company name field. Recommend "Watts Way Fitness" — matches the Oura registration and the brand on the site.

### SCOTT (2026-07-12T23:28)

[File uploaded: 1783898885012_image.png]

### CLAUDE (2026-07-12T23:28)
The program's paused like Garmin's, but submissions are still being accepted and they'll process them once it reopens, so I should recommend submitting now to secure a spot in the queue.Same story as Garmin's developer program — paused, but the form still accepts submissions and they say they'll follow up when they reopen. Submit anyway. You lose nothing, and being in the queue before they reopen beats applying after.

Use the draft I gave you. This is now the second paused API on your list (Garmin ticket filed July 10, TrainingPeaks queued today) — both slot into existing architecture if they ever open, neither changes the roadmap.

One addition to their instructions: review the Partner API Wiki link before submitting — some of these forms ask questions the wiki answers (auth model, data scopes). Skim it so your answers use their vocabulary.

After you submit, I'll add it to the handoff doc's "on the horizon" section next time we version it. Auto-sync scheduler remains next up.
