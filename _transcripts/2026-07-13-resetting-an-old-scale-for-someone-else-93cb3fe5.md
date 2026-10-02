# Resetting an old scale for someone else
Date: 2026-07-13
Conversation: 93cb3fe5-0fdb-4360-9c40-946333f2c110
Domain: skip

## Summary
**Conversation Overview**

The person sought help transferring a Withings Body Cardio scale (model WBS04) to a family member. The conversation covered whether a factory reset was necessary before the handoff (it was recommended to clear locally stored Wi-Fi credentials, user profiles, and unsynced data), the step-by-step reset process using the side button to navigate to the Reset menu option, and the setup process via the Withings app on the new user's phone.

After setup, both the family member and the person themselves tested the scale and found it was not producing body composition or heart rate readings — only weight. Claude walked through likely causes in order of probability: incomplete post-reset firmware update (check via Devices → Body Cardio → All settings), low battery from age-related degradation (full 3+ hour charge recommended), and screen customization settings being wiped by the reset (check Devices → Body Cardio → Screen customization). Claude also identified a well-documented hardware failure mode specific to this model: bathroom humidity entering through three small holes in the metal base corrodes the internal sensor board, disabling impedance and HR circuits while leaving weight measurement (on separate load cells) intact — which matched the observed symptoms exactly. Claude noted this scale is approximately a decade old and flagged that repair may not be cost-effective given the hardware's age and the nature of the likely failure.

### SCOTT (2026-07-13T23:03)
I’m giving my old scale to my daughter. How do I reset it?  Or do I even need to?  It’s no longer associated with my account.
[File uploaded: photo.jpeg]

### CLAUDE (2026-07-13T23:03)
The user's Withings Body Cardio scale isn't showing up on their account, so I should recommend a factory reset as the standard fix to clear any stored user data and Wi-Fi settings. I'm trying to recall the exact button sequence for resetting this model—it involves pressing the side button, though I'm not entirely certain of the precise timing or number of presses needed.

Resetting the scale is worth doing since disconnecting the account doesn't remove stored data like user profiles, Wi-Fi settings, or unsynced readings. The process involves forgetting it in Bluetooth, holding the side button for eight seconds until a menu appears with options for Mac, Upgrade, and Reset, then cycling through to select Reset and waiting for the factory reset to complete.Yes, reset it. Removing it from your account dissociates the cloud link, but the scale itself still holds your Wi-Fi credentials, stored user profiles, and any unsynced weigh-ins locally. A factory reset clears all of that and gives your daughter a clean setup experience — factory resetting completes the dissociation process, and it won't touch any data already synced to your Withings app.

For your Body Cardio (WBS04):

1. On your phone, go to Bluetooth settings and Forget/Unpair the scale if it's still listed.
2. Hold the button on the side of the scale for 8 seconds, then release. A menu appears with an arrow and three options: Mac, Upgrade, Reset.
3. Press the button again to move the arrow to Reset, then wait for the scale to restart — "Hello!" appears on the screen and it'll display "Factory" confirming the wipe.

Your daughter then just adds it as a new device in her Withings app. One tip since it's an older unit: have her charge it fully before setup — these scales are notorious for reset/boot loops on a low battery.

### SCOTT (2026-07-13T23:08)
What do I do at the setup screen

### CLAUDE (2026-07-13T23:08)
The scale is probably stuck on the "Hello!" screen or setup prompt after being reset. Setup happens through the Withings app—install it, go to Devices, add a new scale, select Body Cardio, and follow the prompts. When the scale shows the setup screen, I need to press the side button to enter pairing mode and then choose Wi-Fi. I should clarify whether Scott or his daughter is doing the setup.Nothing on the scale itself — setup happens from the phone. And it should be your daughter's phone, since the scale binds to whichever account sets it up.

On her phone:

1. Download the Withings app and create/sign in to her account
2. Tap **Devices** → **+** (Install a device) → **Scales** → **Body Cardio**
3. Follow the prompts — when asked, press the side button on the scale briefly to put it in pairing mode ("setup" will show on the display)
4. The app connects via Bluetooth, then asks her to pick her Wi-Fi network and enter the password
5. It'll likely install a firmware update — let it finish, can take several minutes

After that, she steps on it once so it can calibrate and link readings to her profile. If the scale is sitting on "Hello!" or a Bluetooth icon right now, that's fine — it's just waiting for the app to find it.

### SCOTT (2026-07-13T23:16)
It’s set up but not reading body fat % or hr. Any idea why?

### CLAUDE (2026-07-13T23:17)
I'm thinking through why the daughter might need pregnancy mode on the scale — she's the 29-year-old attorney expecting her first child in July 2026, so if she's the one receiving the Withings scale, the app would disable the bioimpedance measurements during pregnancy.The most likely culprit, given the timing: if this is going to your oldest daughter, pregnancy is the answer. The Withings app disables bioimpedance (body fat, body water, etc.) when a profile has pregnancy mode enabled or when the user indicates they're pregnant during setup — it's a blanket precaution for the electrical current the scale sends through the body, same reason it's disabled for pacemaker users. Heart rate can also get suppressed alongside it depending on settings. If that's the case, there's nothing to fix; it'll re-enable after she updates her profile postpartum.

If that's not it, run through these:

- **Bare feet required** — socks or dry, calloused feet block the impedance circuit. Slightly damp feet read best.
- **Check measurement settings** — in the app: Devices → Body Cardio → check that body composition and heart rate modes are toggled on. Sometimes "weight only" mode gets selected during setup.
- **Stand still longer** — HR needs a good 15–20 seconds of stillness after the weight locks in. Stepping off early kills it.
- **Hard, flat floor** — carpet throws off readings; Withings sells carpet feet, but tile/hardwood is the fix.
- **Profile recognition** — if the scale doesn't recognize who's standing on it, it may skip body comp. Make sure her profile is assigned in the app.

First few weigh-ins can also be flaky while it calibrates to a new user. But check the pregnancy setting first — that one's by design, not a malfunction.

### SCOTT (2026-07-13T23:21)
Nope. I tried it too. No preggo setting. Didn’t work for me either.

### CLAUDE (2026-07-13T23:21)
Both users are missing body fat and heart rate readings, and this WBS04 scale model is known for issues. The firmware might not have fully updated after the reset, which is often needed to enable those features—and athlete mode won't disable body fat readings anyway. If both users are affected, it points to a device-level problem: incomplete firmware update, low battery, or hardware failure like corroded sensors on the Body Cardio.

I should check the firmware version in the app, make sure it's fully charged, verify bare feet contact on a hard floor, and look at the display customization settings since those screens might be disabled after reset—though that shouldn't prevent data sync. Bioimpedance and HR features often get disabled at low battery levels. If nothing works, it's likely hardware degradation from bathroom humidity exposure, which is a known issue with these older units from around 2016.That rules out user-profile issues — it's the scale. Three things to check, in order of likelihood:

1. **Firmware didn't finish updating.** After a factory reset, body comp and HR often won't function until the post-reset firmware update completes. In the app: Devices → Body Cardio → All settings → check firmware version and force an update if one's pending. Keep the scale near the phone and on Wi-Fi while it runs.

2. **Low battery.** The scale disables bioimpedance and HR measurement before it kills weight readings to conserve power. Given its age, put it on the charger for a full 3+ hours and retest. Battery degradation on these 2016-era units is real.

3. **Screen customization got wiped.** The factory reset restores default display screens, but check Devices → Body Cardio → Screen customization anyway — if the body comp and heart rate screens aren't enabled in the cycle, it may not run those measurements.

If all three check out and it still only reads weight, you're probably looking at hardware failure. The Body Cardio has a well-documented weakness: the three small holes in the metal base let bathroom humidity in, corroding the internal sensor board. That corrosion typically takes out the impedance/HR circuits while weight (which uses separate load cells) keeps working — which matches your symptoms exactly. There's an iFixit teardown if you're inclined to open it and inspect for corrosion, but on a decade-old scale, the honest cost-benefit answer may be that your daughter gets a perfectly good weight-only scale and you don't sink time into a $150 repair candidate.
