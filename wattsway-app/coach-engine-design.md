# Coaching engine design

Single function: assemble context → call model → return formatted plan.
System prompt (static, versioned file): athlete profile and non-negotiables.
Per-run user message: current mesocycle state (program, week, RIR target, what's next); recovery window last 7–14 days (Oura HRV trend, RHR, sleep, deep sleep); body-comp trend last 4–6 weeks (Withings, direction only); completed training last week (pasted RP sessions + run summaries); subjective notes; race calendar + current phase.
Output: next 1–2 weeks of training in his TrainingPeaks format, as paste-ready text or JSON rendered into blocks.

**Approx date:** June 2026

**Source:** personal-coach-tool-spec.md — Watts Way Fitness App, 2026-06-12
