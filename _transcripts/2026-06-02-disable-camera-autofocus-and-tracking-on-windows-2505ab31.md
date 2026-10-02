# Disable camera autofocus and tracking on Windows
Date: 2026-06-02
Conversation: 2505ab31-0b83-4ecc-bf34-0404293c3d54
Domain: skip

## Summary
**Conversation overview**

The person sought help disabling unwanted automatic camera tracking and zoom behavior on a Windows laptop using Microsoft Teams — behavior they compared to the iPhone 17's camera features. Claude diagnosed two independent layers that can cause this: Teams' own auto-framing setting and Windows Studio Effects (a system-level AI camera feature available on newer laptops with NPUs). The conversation involved some back-and-forth troubleshooting, including a clarification that "Bluetooth & devices" in Windows Settings is where all cameras appear regardless of connection type, which the person initially found confusing.

The person shared a screenshot of their Windows Studio Effects panel, which revealed that Automatic framing and Eye contact were already toggled off before the screenshot was taken — a detail that caused brief confusion before being clarified. Portrait blur (under Background effects) remained on, and Claude noted this doesn't cause tracking behavior. With the Windows-level settings confirmed off, Claude directed the person to Teams' own separate auto-framing toggle (via profile picture → Settings → Devices, or mid-call via the video controls more options menu) as the remaining likely cause of the behavior. The person confirmed they had turned off auto-framing and eye contact in the Windows panel prior to the screenshot. The conversation ended without confirmation of whether the Teams-level toggle had been addressed or whether the tracking behavior had fully stopped.

### SCOTT (2026-06-02T15:44)
on y windows pc laptip using MS teams, my integrated camera has started to do funky autozooms and tracking and other weoird shit. kind of like how the new iphone 17 camera does.  i dont like.  how do i turn it off.

### CLAUDE (2026-06-02T15:44)
 The user is asking about disabling the auto-zoom feature in Teams on Windows, which is likely either the "Auto-framing" feature or a Windows Studio Effects feature on newer laptops with NPU support. I know this is fairly stable functionality, though I'm considering whether to search given that Windows Studio Effects is relatively recent and the exact feature names might have shifted.Two different things can cause this, and you may need to kill both because they stack.

**1. Teams' own auto-framing.** In Teams, go to **Settings → Devices**, scroll to the camera section, and look for **Auto-framing** (sometimes under "Camera effects" or a toggle right below the camera preview). Turn it off. In the newer Teams you can also toggle it mid-call: click the **video/camera options** (the "···" or the up-arrow next to your camera button) and uncheck **Auto-framing**.

**2. Windows Studio Effects** — this is the more likely real culprit, and it's the one that mimics the iPhone Center Stage behavior. If your laptop has an NPU (recent Intel Core Ultra, Snapdragon X, or AMD Ryzen AI machine), Windows itself is doing the tracking at the OS level, *underneath* Teams, so turning it off in Teams alone won't fully stop it. To kill it:

Go to **Settings → Bluetooth & devices → Cameras**, pick your integrated camera, and turn off **Automatic framing** (and while you're there, Background effects / Eye contact if you don't want those either). 

Alternatively, the fast way: open **Quick Settings** (click the battery/wifi/volume cluster in the taskbar, or Win+A). If your hardware supports it you'll see a **Studio effects** tile — click it and toggle **Automatic framing** off there.

A couple of things worth knowing: the Windows Studio Effects setting is sticky and applies system-wide, so turning it off there fixes it for Zoom, Webex, etc., not just Teams. And if you *don't* see a Studio Effects tile or an Automatic framing option in camera settings, then it's purely Teams doing it and step 1 is your whole fix.

If you turn off the Teams toggle and it still tracks you, that confirms it's Studio Effects and you go to step 2. Which laptop is it (or does it have a Core Ultra / Ryzen AI / Snapdragon chip)? That tells us immediately whether Studio Effects is even in play.

### SCOTT (2026-06-02T19:13)
my camera is integrated, not bluetooth

### CLAUDE (2026-06-02T19:14)
 I see the confusion now — the user thought "Bluetooth & devices" meant it only applies to Bluetooth cameras, but in Windows 11 that's actually where all camera settings live, regardless of whether they're integrated, USB, or Bluetooth. I should clarify this without being patronizing.Yeah, that menu name is misleading — "Bluetooth & devices" is just the name Microsoft gave the whole category, but it's where *all* cameras live, including integrated ones. Your built-in webcam will show up under **Settings → Bluetooth & devices → Cameras** even though it's hardwired, not Bluetooth. There's no separate "integrated camera" section; that's the one.

So the path still holds: open it, click your integrated camera, and look for **Automatic framing** to toggle off.

That said — if you open that Cameras page and *don't* see an "Automatic framing" toggle under your camera, that tells you something useful: it means your laptop doesn't have Windows Studio Effects (no NPU), and the auto-zoom/tracking is coming purely from Teams. In that case the fix is entirely in Teams' own settings, not Windows.

What laptop is it? If you tell me the model I can tell you straight off whether it has the Windows-level effects or whether it's all on the Teams side.

### SCOTT (2026-06-02T19:17)
there is no camera section there

### CLAUDE (2026-06-02T19:17)
 The absence of a Cameras section in Settings suggests this isn't a standard Windows 11 setup with NPU support, so the auto-framing is likely coming directly from Teams or the camera's own driver software. If the Cameras page isn't showing up at all, this could indicate an older Windows build, Windows 10, or a connectivity issue with the camera itself.

Rather than keep digging for the laptop model, I should just give them the practical answer: the auto-zoom is almost certainly either a Teams feature or bundled software from the camera manufacturer like Lenovo, Dell, HP, or Logitech.Good — that actually narrows it down. If there's no Cameras section at all under Bluetooth & devices, your laptop almost certainly doesn't have Windows Studio Effects (that page only shows up on newer Windows 11 builds with the right hardware). So Windows isn't the one doing the tracking. That leaves two suspects:

**1. Teams itself** (most likely). This is where you fix it:
- Click your profile picture (top right) → **Settings → Devices**, scroll to the camera area and look for an **Auto-framing** toggle, turn it off.
- Or do it live in a call: hover your camera button / click the **···** more options near the video controls and uncheck **Auto-framing**. Doing it mid-call lets you watch the preview snap back to normal, which confirms you killed the right thing.

**2. Your camera vendor's companion app** (the other common cause). A lot of integrated webcams ship with manufacturer software that does AI tracking at the driver level — examples: **Lenovo Commercial Vantage / Glance**, **Dell Optimizer / "Express Sign-in" camera tools**, **HP Enhanced Lighting / Presence**, or an effects panel from the camera's image-processing chip. If Teams' toggle alone doesn't stop it, open whatever camera/webcam app your laptop maker installed and look for "auto-framing," "tracking," "subject framing," or "smart camera" and switch it off there.

Quick test to tell which one it is: turn off the Teams Auto-framing toggle. If the tracking stops → done. If it *keeps* tracking → it's the vendor app, and you go hunting in your manufacturer's camera software.

What brand is the laptop (Lenovo, Dell, HP, etc.)? That's the one detail that lets me point you straight at the exact app and setting instead of guessing.

### SCOTT (2026-06-02T19:19)

[File uploaded: 1780427942572_image.png]

### CLAUDE (2026-06-02T19:19)
 Looking at the screenshot, Windows Studio Effects is definitely installed and Automatic framing is already disabled, so the zoom behavior they're experiencing isn't coming from that feature. The toggle is off, which means I should focus on other potential causes for the tracking issue they mentioned.So you do have Windows Studio Effects after all — it was just buried (this panel usually lives in Quick Settings or under the camera page, depending on your build). And here's the key thing: **Automatic framing is already showing Off.** That's the toggle responsible for the auto-zoom/tracking-you-around behavior you're describing. So at the Windows level, it's not the culprit right now.

That tells you the funky tracking is almost certainly coming from **Teams' own auto-framing**, which runs independently of this panel. Go fix it there:

- Profile picture → **Settings → Devices**, scroll to the camera section, turn off **Auto-framing**.
- Or mid-call: click the **···** / more options by your video controls and uncheck it so you can watch the preview snap back.

Two other things in this screenshot worth flagging while you're here:

**Eye contact** is off — good, leave it. That's the one that subtly warps your gaze to fake looking at the camera, and it looks uncanny.

**Background effects** is **On** with **Portrait blur** selected. That's not what's causing the zoom/tracking, but it's an active AI effect on your feed. Portrait blur keeps you in focus while softening the background. If you want a totally untouched, raw camera image, flip that toggle off too. If you like the blur, leave it — it doesn't move or track you.

So: this panel isn't your problem (framing's already off). Kill the Teams auto-framing toggle and the tracking should stop. If it somehow *doesn't*, come back and we'll look at whether your camera vendor's app has its own tracking layer.

### SCOTT (2026-06-02T19:19)
i just turned the auto framing off

### CLAUDE (2026-06-02T19:19)
Right — but look again at what you described versus what you just did: the screenshot showed Automatic framing **already off** before you touched it, and now you've toggled it... which means you may have just turned it *on*, or toggled it off from a state it was already in. Worth a quick double-check that it actually reads **Off** now, since that's the one that does the tracking.

But here's the more important point: if Windows-level framing was already off when you took that screenshot, then it was never the thing causing your problem in the first place. The tracking you're seeing in Teams is coming from **Teams' own auto-framing**, which is a separate setting that this Windows panel doesn't control.

So the real fix is still in Teams:

- Profile picture (top right) → **Settings → Devices** → scroll to the camera section → turn off **Auto-framing** there.
- Or do it live in a call via the **···** more options by your video controls, so you can watch your preview snap back to normal and confirm you got the right toggle.

Turn off the Teams one, hop into a test call or check the preview, and see if the tracking stops. That's the setting that matches the behavior you're describing.

### SCOTT (2026-06-02T19:20)
no i turned off the ati framign and the eye contact before the screens hot

### CLAUDE (2026-06-02T19:20)
Ah, got it — so you'd already turned both off *before* grabbing the screenshot, which is why they read Off. That clears up my confusion.

So at the Windows level you've now handled it: Automatic framing off, Eye contact off. The only AI effect still running there is **Portrait blur** (Background effects is On), and that one doesn't track or zoom — it just softens your background — so it's not your problem unless you also want a totally raw image.

That means if you're *still* seeing the funky zoom/tracking, it's coming from **Teams itself**, which has its own auto-framing independent of this panel. Fix it there:

- Profile picture → **Settings → Devices** → camera section → turn off **Auto-framing**.
- Or mid-call via the **···** more options by your video controls, so you can watch the preview snap back.

So the real question now: **with both Windows toggles off, is the tracking still happening?** If yes → it's the Teams setting, go flip it. If it's already stopped → you're done, and Portrait blur is the only thing left to kill if you want the camera fully untouched.
