# Adjusting screen timeout on Zen laptop
Date: 2026-08-18
Conversation: 2397a7eb-913b-4f7c-8eb3-c56ce6ba9d52
Domain: skip

## Summary
**Conversation Overview**

The person asked for help preventing the screen from going dark too quickly on their Zen (ASUS Zenbook) laptop while sitting in front of it. The conversation focused on diagnosing and resolving a screen blanking issue on a Zenbook S14 with a 3K OLED display running Windows. Claude walked through several potential causes: Windows screen timeout settings, OLED-specific auto-dimming in the MyASUS app and Display settings, screen saver configuration, presence sensing, and a hidden console lock display-off timeout power setting.

A key correction occurred mid-conversation: the person pushed back on Claude's assumption that they hadn't checked both displays in the Advanced Display dropdown, and Claude acknowledged the error. The person then discovered the screen saver was set to "None" with a 1-minute timer, which they identified as the likely culprit. Claude noted that even with "None" selected, the registry value `ScreenSaveActive` can remain set to 1, causing the timer to still fire a blank screen, and provided registry query commands to verify this. Claude also provided PowerShell commands (`powercfg /requests`, `powercfg /lastwake`) and a command to unhide and extend the console lock display-off timeout on AC power as a remaining candidate if the issue persisted. The person's external monitor is a DELL S2725QC connected alongside the built-in OLED panel.

### SCOTT (2026-08-18T12:49)
on my zen laptop how can i set it so that the scrneed sdeosnt go balck so quickly ewhen I am sitting in front of it

### CLAUDE (2026-08-18T12:49)

Two different settings are probably doing this — the OLED one is the more likely culprit for "so quickly."

**1. Windows screen timeout**
Settings → System → Power & battery → Screen, sleep, & hibernate timeouts. Set "On battery power, turn off my screen after" and "When plugged in, turn off my screen after" to whatever you want (15–30 min, or Never when plugged in).

**2. OLED auto-dimming (Zenbook-specific)**
Your S14 has a 3K OLED, and both Windows and MyASUS run burn-in protection that dims or blanks the panel after ~30–60 seconds of no keyboard/mouse input — which is exactly what happens when you're sitting there reading and not typing.

- Settings → System → Display → Advanced display → look for the OLED/panel protection options and turn off "Dim the screen content" (and lengthen or disable "Turn off the screen after a period of inactivity" if it appears separately).
- MyASUS app → Customization → Display → OLED Care. Turn off **Auto screen dimming** (and pixel shift/taskbar auto-hide if they bother you). This is the one people usually miss.

**Also worth checking:** Settings → System → Power & battery → Battery saver — if it's set to kick in at a high percentage, it dims the screen independently. And under Power & battery → Power mode, "Best power efficiency" shortens timeouts.

One caveat on turning off the OLED dimming: it's there for a reason. Static bright elements (taskbar, Excel gridlines) on an OLED for hours at a time is how you get burn-in. If you disable auto-dim, at least leave pixel shift on.

### SCOTT (2026-08-18T12:55)
plugged in.  defintely not 20 mins.  more like a couople of minutes if that.  Nothing in your #2/.. no battery saver options eitehr
[File uploaded: 1787057494690_image.png]
[File uploaded: 1787057583902_image.png]
[File uploaded: 1787057683523_image.png]

### CLAUDE (2026-08-18T12:56)
Your #2 didn't apply because your Advanced display screenshot has **Display 2: DELL S2725QC** selected. The OLED-specific settings only appear when the internal panel is selected in that dropdown. Switch it to Display 1 (the Zenbook's built-in screen) and the OLED options will show up.

But given 20 minutes set and ~2 minutes actual, something is overriding the power plan entirely. Three candidates, in order of likelihood:

**1. Screen saver set to "Blank"** — this runs on its own timer, completely independent of the power settings you screenshotted. It's the most common cause of exactly this symptom.
Hit Start, type `screen saver`, open "Change screen saver." If it's set to Blank with a 1–2 minute wait, that's your answer. Set it to None.

**2. Presence sensing** — the Zenbook S14 has a human presence sensor. Windows can turn the screen off when it thinks you've walked away, and it misfires if the IR camera is blocked, if you're sitting slightly off-axis, or if the camera privacy shutter is closed.
Settings → Privacy & security → Presence sensing → turn off "Automatically turn off my screen when I leave." (Also check ASUS's own "Adaptive Lock" if MyASUS exposes it.)

**3. MyASUS OLED care** — you were on the Home page. The display controls are under **Device Settings** in the left nav, not Home. Look for a Display section with OLED protection / auto screen dimming.

One diagnostic that narrows this fast: when the screen blanks, does moving the mouse bring you straight back to your desktop, or do you have to enter your PIN?

- Straight back → screen saver or power/DPMS blanking (#1)
- PIN required → it's locking, not just blanking → presence sensing or Dynamic Lock (#2)

That single answer will tell you which of the three to fix.

### SCOTT (2026-08-18T12:59)
i did the drop down and checked both dumbass .  screen savewr was set to none and 1 minute,  i bet that was it.
[File uploaded: 1787057905907_image.png]

### CLAUDE (2026-08-18T12:59)
Fair — you had checked both. I called that wrong.

On the screen saver: if it truly said "None," the wait value is normally inert, which makes it a weaker suspect than it looks. But the registry value `ScreenSaveActive` can be stuck at 1 while the dropdown displays None, and in that state the 1-minute timer does fire a blank. So it's plausible.

Quick way to know for sure — open PowerShell and run:

```
powercfg /requests
```

then, right after the screen blanks, run:

```
powercfg /lastwake
```

More useful: check what's actually set, rather than what the UI claims.

```
reg query "HKCU\Control Panel\Desktop" /v ScreenSaveActive
reg query "HKCU\Control Panel\Desktop" /v ScreenSaveTimeOut
```

If `ScreenSaveActive` is 1, that was it — set it to 0. If it's already 0, the screen saver was never the cause and the timer value is a red herring.

The remaining candidate if it comes back: the hidden **console lock display off timeout**. It's a separate power setting from the one you screenshotted, defaults to 60 seconds, and is hidden from the UI by default. Unhide and set it:

```
powercfg -attributes SUB_VIDEO 8EC4B3A5-6868-48c2-BE75-4F3044BE88A7 -ATTRIB_HIDE
powercfg /setacvalueindex SCHEME_CURRENT SUB_VIDEO 8EC4B3A5-6868-48c2-BE75-4F3044BE88A7 1200
powercfg /setactive SCHEME_CURRENT
```

That sets it to 20 minutes on AC, matching your other timeout. It only applies after the machine locks, so it fits a "blanks fast even though I set 20 minutes" pattern.
