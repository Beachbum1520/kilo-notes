# Extracting shoe mileage from Garmin data
Date: 2026-07-11
Conversation: 8cd0b525-c777-43a0-8437-6b3eabbf0971
Domain: wattsway-app

## Summary
**Conversation Overview**

This conversation is part of an ongoing project building WattsWay, a fitness tracking application. The person uses Garmin for activity tracking and FitnessSyncer to bring Garmin data into WattsWay. They asked whether Garmin's shoe mileage tracking feature could be pulled through this data pipeline.

Claude explained that gear/shoe assignments are stored only in Garmin Connect's database and are not included in TCX or FIT file exports, meaning FitnessSyncer has no access to this data. The Garmin API does not expose gear data either, so no existing integration path can retrieve it. Claude proposed that WattsWay build its own shoe tracker natively using the activity distance data already stored in the activities table, with a `shoes` table, per-activity assignment logic (manual or default rules by activity type), and optional starting mileage entry for historical Garmin data.

The person confirmed the feature should stay at position #6 in the development roadmap and clarified a key business rule: all activity miles count toward shoe wear — running, walking, treadmill, outdoor, and any other distance-generating activity with no filtering. This simplifies the implementation since no activity type exclusions are needed. The next planned topic is the auto-sync scheduler.

### SCOTT (2026-07-11T17:23)
I use garmin to track mileage on my shoes. And as you know we use fitness syncer to get garmin data. Can we get shoe mileage from this?

### CLAUDE (2026-07-11T17:24)
Scott is asking whether gear data from Garmin's shoe tracking feature gets exported through TCX files or FitnessSyncer. The answer is no — TCX files don't include gear information, and while Garmin Connect tracks shoe mileage, that data lives only in Connect itself since the gear API isn't exposed through FitnessSyncer's exports. Even FIT files don't carry gear assignments, though you can set default shoes per activity type on the watch.

For WattsWay, the better approach would be building a shoe tracker directly in the app (which is already on the roadmap) where users assign shoes per run and the system calculates mileage from the activities table, or implementing default-shoe rules to auto-assign based on activity type like treadmill versus outdoor runs.Short answer: no. Gear assignments live in Garmin Connect's database, not in the activity files. TCX has no gear field at all (the schema simply doesn't include one), and FIT files don't carry it either — when you tag a shoe to a run, that association stays on Garmin's servers. FitnessSyncer exports the file, so shoe data never travels down our lane. The official Garmin API doesn't expose gear anyway, so even that reopening wouldn't help.

The good news: we don't need it. The shoe tracker (roadmap #6) can live entirely in WattsWay since we already have every run's distance in the activities table. Design would be:

1. A `shoes` table (name, purchase date, replacement threshold, retired flag)
2. Assignment per activity — either manual per-run, or default rules that cover most cases automatically (e.g., "treadmill runs → Shoe A, outdoor runs → Shoe B"), with per-run override
3. Mileage = sum of assigned run distances, shown against the threshold

If your Garmin gear history matters, you'd read the current totals off Garmin Connect once and enter them as starting mileage per shoe — from then on WattsWay accumulates on its own.

One decision to park for when we build it: whether treadmill miles count toward shoe wear at the watch-estimated distance or whether this is another spot where the distance-edit feature (roadmap #3–4) matters. Given the ~8% one-directional error, watch-estimate is probably fine for wear tracking.

Still #6 in the order, or do you want it pulled forward?

### SCOTT (2026-07-11T17:25)
Na. Leave it at 6. But all miles count. Running walking etc. treadmill, outdoors, etc.

### CLAUDE (2026-07-11T17:25)
I'm confirming the approach: shoe mileage totals all miles from running, treadmill, and walking combined.Noted for when we build it: shoe wear = all mileage — run, treadmill, walk, outdoor, everything with distance. That's actually simpler than the training-volume logic since there's no filtering; just sum distance for any assigned activity.

Stays at #6. Next up is still the auto-sync scheduler when you're ready.
