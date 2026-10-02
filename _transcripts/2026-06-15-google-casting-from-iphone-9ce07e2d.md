# Google casting from iPhone
Date: 2026-06-15
Conversation: 9ce07e2d-9f80-4ee4-a41b-cc05a40fe441
Domain: skip

## Summary
**Conversation Overview**

The person was staying at a SONIFI-equipped hotel and sought help casting video from their iPhone to the in-room TV. The conversation progressed through systematic troubleshooting: starting with general Google Cast instructions for iOS, then diagnosing the hotel network context, then identifying the specific protocol mismatch at the root of the problem. Key technical diagnosis reached: SONIFI's deployment at this property is Google Cast only (no AirPlay), Apple's first-party apps including Photos only surface AirPlay (no Cast SDK integration), and hotel client/AP isolation was blocking mDNS/SSDP discovery, preventing any Cast-compatible app (including Google Photos) from seeing the "1851 Bedroom" receiver. The person confirmed the Cast button was absent from Google Photos, validating the network-isolation hypothesis rather than an app configuration issue.

The conversation covered why Chromecast cannot serve as a wired passthrough (power-only USB port, wireless-only video input), why Chrome for iOS lacks the tab-casting feature present in desktop Chrome, and why every app-based casting route fails identically under client isolation regardless of which app is used. Recommended paths in priority order were: asking the front desk whether a dedicated guest-cast SSID exists (the only no-hardware wireless option), using a Lightning or USB-C-to-HDMI adapter (hardware solution bypassing all network and protocol issues entirely), or watching on the phone as a practical fallback. The person does not currently have a USB-C-to-HDMI adapter and confirmed the Chromecast plug-in path was not viable. Claude explicitly noted that third-party screen-mirroring apps are unreliable in hotel environments specifically due to the same isolation constraints. The person demonstrated familiarity with HSIA networking concepts, so Claude used technical terminology (client isolation, mDNS, SSDP, VLAN, back-channel) without simplification.

### SCOTT (2026-06-15T21:42)
How do I Google cast from an iPhone?

### CLAUDE (2026-06-15T21:42)
Casting from an iPhone to a Chromecast or Google Cast device works a bit differently than on Android, since there's no native AirPlay-style Cast button built into iOS. You do it through individual apps:

1. **Connect to the same Wi-Fi.** Your iPhone and the Cast device (Chromecast, Google TV, Nest Hub, etc.) must be on the same network.

2. **Open a Cast-compatible app.** YouTube, Netflix, Disney+, Spotify, HBO Max, and many others support Google Cast on iOS.

3. **Tap the Cast icon.** It looks like a small rectangle with a Wi-Fi symbol in the corner, usually at the top or bottom of the screen.

4. **Pick your device** from the list, and playback shifts to your TV. You can then control play/pause and volume from your phone.

A few things worth knowing:

- **There's no system-wide screen mirroring to Chromecast from iOS** the way AirPlay works with Apple TV. iOS doesn't allow it natively. If an app doesn't have a Cast button, you generally can't cast its content.
- **The Google Home app** is useful for setting up and managing your Cast devices, but it doesn't add a universal mirroring feature on iPhone.
- **Third-party mirroring apps** (e.g. Replica, Streamer for Chromecast) exist to approximate screen mirroring, but they're often laggy and hit-or-miss, especially for video with audio.

If you tell me what specifically you're trying to cast — a single app's content vs. your whole screen vs. a browser tab — I can point you to the cleanest method.

### SCOTT (2026-06-15T21:42)
Was trying to cast video from my iPhone to my hotel tv

### CLAUDE (2026-06-15T21:43)
Hotel TVs are notoriously problematic for casting due to their network configurations, so I should address this directly as a practical concern rather than a generic solution.Hotel TVs are the worst-case scenario for casting, and it's worth understanding why before you waste more time on it.

The core problem is **network isolation**. Even if the hotel TV has a Chromecast built in (many now use platforms like Google TV or proprietary systems like Enseo), the hotel's Wi-Fi almost always puts every device on its own isolated segment — client isolation / AP isolation — specifically to stop guests from seeing each other's devices. Your phone and the TV can't discover each other even when they're both "on the hotel Wi-Fi," because the network is deliberately built to prevent exactly that. This is standard security practice in hospitality HSIA deployments — which, given your background, you already know better than most.

So your options, roughly in order of reliability:

- **Chromecast with a guest/pairing mode.** Some hotel casting systems (Google Chromecast's "guest mode," or platforms like Enseo, SONIFI, Telkonet) generate an on-screen PIN or let you pair via a QR code rather than network discovery. If the TV shows a "Cast" welcome screen with instructions, follow that — it's the only path that routes around the isolation.

- **HDMI cable.** If the TV has an accessible HDMI port (many hotels lock these down or hide them behind the panel), a Lightning-to-HDMI or USB-C-to-HDMI adapter is the most reliable method, full stop. No network needed.

- **Your own travel router / hotspot.** If you put both your phone and a travel Chromecast on *your own* network (travel router pulling from hotel Wi-Fi, or even a phone hotspot), discovery works because you control the segment. This obviously requires carrying your own Cast dongle.

- **Just use the phone.** For a single video, sometimes not worth the fight.

For your situation this week — if it's the conference hotel and you're trying to throw something up for a quick review, the HDMI adapter is the move if the port's reachable. The built-in casting is going to fight you because of how these properties are architected, and that's not something you can fix from the guest side.

What's the TV showing — a branded hotel welcome screen, or does it look like a standard smart TV interface?

### SCOTT (2026-06-15T21:43)
Hotel has cast ability. And is set up. But my videos only have airplay as an option

### CLAUDE (2026-06-15T21:44)
So the key issue here is that only AirPlay is showing up as a casting option when they try to cast their videos. This suggests the app or service they're using to play the videos only supports AirPlay, not Google Cast — regardless of whether the TV itself has casting capabilities set up. The problem isn't with the TV's setup, but with what the source app actually supports.

If they're playing videos from Apple's native apps like Photos or the camera roll, Google Cast won't be an option at all since Apple doesn't integrate the Cast SDK into their first-party apps. Meanwhile, many modern hotel casting systems support both AirPlay and Chromecast, so if the TV is showing AirPlay as available, that might actually be the more reliable option for them to use.

But here's the catch: AirPlay faces the same network isolation problem over hotel Wi-Fi that Chromecast does — the discovery mechanism relies on Bonjour/mDNS, which client isolation typically blocks. However, hotel systems that advertise AirPlay support usually work around this with a PIN or QR code pairing method, similar to how Chromecast guest mode operates.

So the practical next step is to try AirPlay and watch for a code prompt on the TV — if the hotel system supports AirPlay, it'll likely use code-based pairing to establish the connection.That's the tell. "My videos" — meaning your own clips in the Photos app or camera roll — is the explanation, and it has nothing to do with the hotel network this time.

Apple's first-party apps (Photos, Files, Safari's native player) only implement AirPlay. They do not implement the Google Cast SDK at all. Google Cast only shows up inside apps where the *developer* built Cast support — YouTube, Netflix, Spotify, etc. Your personal video in Photos has no Cast pathway to offer, so iOS only surfaces AirPlay. No setting will change that; the option doesn't exist because the protocol was never integrated into that app.

So the practical question becomes: does the hotel's casting platform support AirPlay, not just Chromecast? Many modern hospitality systems (Enseo, SONIFI, the newer Google TV-based deployments) support both precisely because half the guests are on iPhones. If the TV's cast welcome screen lists AirPlay alongside Cast, you're in luck:

- **Select AirPlay from your video and watch for a PIN/QR prompt.** A properly deployed hotel AirPlay setup gets around the client-isolation problem the same way Chromecast guest mode does — code-based pairing instead of network discovery. If it asks you for a code shown on the TV, that's the system working as designed.
- **If AirPlay only finds nothing (or only offers to search endlessly),** then the hotel set up Chromecast but *not* AirPlay, and isolation is blocking native discovery. Dead end for your Photos videos.

Two workarounds if AirPlay won't bridge:

- **Upload the clip to YouTube (unlisted) or Google Photos / Drive,** then cast from *that* app, which does speak Cast. Roundabout, but it routes through an app with real Cast support.
- **HDMI adapter** remains the bulletproof option if the port's reachable.

Quick check: does the TV's casting/welcome screen actually name AirPlay as supported, or just "Cast"? That single detail tells you whether the AirPlay option in your video has any chance of landing.

### SCOTT (2026-06-15T21:45)
It is a sonifi hotel. Bit nothing comes up when I try to AirPlay.
[File uploaded: photo.jpeg]

### CLAUDE (2026-06-15T21:46)
That screen confirms the diagnosis: it's Google Cast only. Every instruction names Google Cast — "Tap Google Cast," select "1851 Bedroom" — and AirPlay appears nowhere. SONIFI's standard cast deployment is Chromecast-based; AirPlay is a separate add-on most properties don't license. So your AirPlay search finding nothing isn't a network glitch, it's that there's no AirPlay receiver running on that TV to find. You're trying to hand off to a protocol the TV doesn't speak.

Which means the path forward is to get your video into an app that *does* speak Cast, then cast "1851 Bedroom" from there. Concretely:

- **Google Photos.** Upload the clip from your camera roll, open it in the Google Photos app, and the Cast icon (same square-with-Wi-Fi glyph on that TV screen) appears. Select 1851 Bedroom. This is the cleanest route for a personal video — it's literally Google's own app talking to Google's cast target.
- **YouTube unlisted.** Upload as unlisted, then cast from the YouTube app. More steps and a transcode wait, but rock-solid once it's up.
- **VLC for Mobile** has a built-in Chromecast renderer and can cast a local file straight from your phone without uploading anywhere — worth it if the video's large or you'd rather not push it to the cloud.

The catch on all three: they still rely on network discovery to see "1851 Bedroom," and hotel client-isolation can block that even when the cast welcome screen is sitting right there. The screen showing up doesn't prove your phone can reach the device — the TV reaches the SONIFI head-end over a back-channel, which is separate from whether your phone's traffic is allowed to find it. If you open Google Photos and 1851 Bedroom doesn't appear in the cast list, that's isolation, and the fix is usually the property's dedicated guest cast SSID — SONIFI typically runs one. Worth a quick call to the front desk to ask which network the casting works on; it's often not the same SSID you used for general Wi-Fi.

Given you've got the Hyatt meeting and conference load this week, I'd set a time box: if Google Photos casting doesn't land in five minutes, the HDMI adapter is the unfrustrating answer.

Try Google Photos first and tell me whether 1851 Bedroom shows up in the cast list — that's the single fact that tells us whether you're fighting an app problem or a network problem.

### SCOTT (2026-06-15T21:46)
What about videos from the web. Anyway to cast them?

### CLAUDE (2026-06-15T21:46)
So the user wants to stream web video to a SONIFI Chromecast TV, but there's a fundamental incompatibility—Safari only supports AirPlay while the TV only accepts Cast. I need to think through what actually works given these constraints.Depends on where the video lives, and the splits are pretty clean:

**Sites with a built-in Cast button** — YouTube, Vimeo, Twitch, most major streaming services in their own apps. These speak Cast natively. Open in the app (not Safari), tap the Cast glyph, pick 1851 Bedroom. Same as before. The app is doing the work, not your phone's OS.

**Random web video in Safari** — this is the dead end. Safari on iOS only knows AirPlay, exactly like your Photos app. There's no Cast button in mobile Safari and no way to add one. So a video embedded on some webpage gives you AirPlay or nothing, and the SONIFI TV won't take AirPlay. Tapping the iOS share sheet won't surface Cast either, because no system-level Cast pathway exists on iPhone.

The workaround that actually bridges Safari-to-Cast:

- **Google Chrome for iOS doesn't help** — a common assumption, but even desktop Chrome's "Cast tab" feature is stripped out of the iOS version because Apple won't allow it. So don't bother installing Chrome expecting the desktop cast behavior.

- **Get the video URL into a Cast-aware app.** If you can grab the direct video link, VLC for Mobile can open a network stream and cast it to the Chromecast itself. Fiddly, and many sites obfuscate the actual file URL, so hit-or-miss.

- **Screen-mirror-to-Cast apps** (Replica, Streamer, etc.) attempt to capture your whole iPhone screen and push it to a Chromecast. This is the only thing that approximates "cast anything from Safari." But they transcode the screen capture in real time, so expect lag, compression, and frequently broken audio sync on video — and they *still* depend on the phone reaching the cast target through hotel isolation. Low success rate in a hotel specifically.

Honest read: for arbitrary web video on an iPhone to a Cast-only hotel TV, there's no clean native path. If it's on YouTube/Vimeo/a real streaming service, use that service's app and you're fine. If it's a one-off clip on some webpage, the HDMI adapter sidesteps the entire protocol mismatch — Safari plays through the cable, AirPlay/Cast becomes irrelevant, and you're not fighting SONIFI or client-isolation at all.

What's the source — a specific site, or a particular service's content?

### SCOTT (2026-06-15T21:52)
There’s no case button in Google Photos.
[File uploaded: aa63d325bd36104aefaf9c256021ba1eda20a8d0.png]

### CLAUDE (2026-06-15T21:53)
Looking at the screenshot, I can see the Google Photos video player with the standard controls — back arrow, date stamp, star, and menu at the top, plus a "Back up now" button indicating this video hasn't been synced to the cloud yet. The bottom shows the typical action buttons like Share, Edit, Ask, Add to, and Delete, along with playback controls, but there's no Cast button visible in this interface.

The absence of the Cast icon is actually the key diagnostic here. In Google Photos, the Cast button appears in the top toolbar only when the app detects a Cast-compatible device on the network. Since it's not showing up at all, Google Photos isn't discovering the bedroom speaker — which points directly to network isolation preventing the app from seeing available cast targets.

This confirms the network-isolation hypothesis. The cloud-based casting routes like Google Photos and YouTube both rely on local mDNS discovery to find cast receivers, so they'd all fail the same way under client isolation. But I should check whether YouTube has any fallback mechanisms that might bypass local discovery.

Actually, YouTube does have a "Link with TV code" feature where you can pair by entering a code shown on the TV, which doesn't require local discovery. But the SONIFI interface doesn't expose that option — it just shows the discovery-based "select 1851 Bedroom" flow. So if discovery is blocked, every app-based casting path fails, and the HDMI adapter becomes the only viable solution.

Though I should also consider whether the Cast button might just be hidden elsewhere in the Google Photos UI — maybe it moved to the three-dot menu in some versions, or there's a prerequisite like needing to back up the video first. I should focus on the diagnosis rather than hunting for the current button location. The missing Cast icon in Google Photos combined with the backup status tells me this is a network-isolation problem—the hotel's client isolation is blocking mDNS discovery that all casting apps depend on. I'll confirm this is the network branch and pivot him decisively to HDMI, while mentioning the guest network as a long shot. I'm realizing I should be more direct here rather than hedge—Scott's an HSIA expert running hotel WiFi services, so he understands client isolation deeply. I can be technical and concise without over-explaining. The farm video content isn't relevant to the isolation question, so I'll focus on what matters.

The core diagnosis is straightforward: Google Photos isn't showing a Cast icon because it can't discover the bedroom receiver on the LAN—that's client isolation at work. Since discovery-based casting fails, every other app route (YouTube, VLC, SONIFI) hits the same wall. They all need to see the device on the local segment, and SONIFI's flow here is discovery-only without manual pairing options.

The fix is either asking the front desk if there's a dedicated guest-cast SSID where casting lives, or going straight to an HDMI adapter as the bulletproof solution. Given his timeline, I'll lead with the answer and keep it decisive.

One more thing to check first though — the Cast button might be hiding in the three-dot menu on iOS, so I should suggest that as a quick sanity check before we assume it's a network discovery issue. It's worth testing since it's free, but I'll be honest about what's most likely.That screenshot is the answer, and it's the network branch, not the app branch.

Two tells. First, the Cast icon is absent from the toolbar entirely — Google Photos doesn't show a static Cast button, it renders one only when the app actually discovers a Cast receiver on the local network. No "1851 Bedroom" visible to the app means nothing to cast to, so no button appears. That's the client-isolation fingerprint you already know cold from the HSIA side: the welcome screen reaches the SONIFI head-end over its own back-channel, but your phone's mDNS/SSDP discovery traffic is being dropped between guest devices. The TV can advertise all it wants; your phone never hears it. Second, "Back up now" tells me this clip is local-only, not yet synced — though that's secondary, since the discovery failure is what's actually killing you.

Quick sanity check before you conclude: tap the ⋯ menu and confirm there's no Cast option buried there. If it's not in the toolbar and not in the menu, the app sees no target — confirmed isolation.

The hard consequence: every app route fails the same way. YouTube, VLC, all of them rely on that same local discovery to find 1851 Bedroom, and this SONIFI flow is discovery-only — there's no "enter a TV code" escape hatch on that screen the way YouTube's TV-pairing offers. So uploading the clip somewhere doesn't help; the bottleneck isn't the app, it's the network segment.

Two real moves:

- **Front desk / SONIFI guest network.** Ask specifically whether casting runs on a separate SSID. SONIFI deployments frequently put Chromecast discovery on a dedicated guest-cast VLAN that allows the multicast the main guest SSID blocks. If you're on the wrong SSID, switching is the whole fix. This is the only path that salvages wireless casting.

- **HDMI adapter.** USB-C/Lightning-to-HDMI into the TV's port if it's reachable. Ends the fight completely — no discovery, no isolation, no SONIFI.

Given your week, I'd make the front-desk call a 60-second ask and not a project. If they don't have a cast SSID, stop fighting it and use the cable.

### SCOTT (2026-06-15T23:04)
How to connect iPhone to tv

### CLAUDE (2026-06-15T23:04)
Cleanest method given everything above: a wired HDMI adapter. It sidesteps the SONIFI/Cast discovery problem entirely — no network, no isolation, no app dependency.

What you need:

- **Apple Lightning Digital AV Adapter** (if your iPhone has a Lightning port) or **USB-C-to-HDMI adapter** (iPhone 15 and later, USB-C). Apple's first-party Lightning adapter is overpriced but actually works; many cheap Lightning knockoffs fail because they skip Apple's authentication chip. USB-C is more forgiving on third-party brands.
- **A standard HDMI cable.**

Steps:

1. Plug the adapter into your iPhone's charging port.
2. Run the HDMI cable from the adapter to an open HDMI port on the TV.
3. Grab the TV remote and switch the input source to that HDMI port (HDMI 1, 2, etc.).
4. Your iPhone screen mirrors automatically — open the video in Photos and it plays through, audio included.

The one catch in a hotel: the HDMI ports are often hidden behind the TV or on a locked-down side panel, and some properties disable the input switching on the remote to force you onto their platform. If you can reach a port and the remote will change inputs, this works in about 60 seconds. If the inputs are locked, you're back to needing the SONIFI guest-cast SSID from the front desk.

Do you know whether your iPhone is Lightning or USB-C? That decides which adapter — and if you don't already have one, whether it's even worth chasing tonight versus just watching on the phone.

### SCOTT (2026-06-15T23:06)
Can I plug it in via the chromcast?  I don’t have a usb c to hdmi cable.

### CLAUDE (2026-06-15T23:06)
Short answer: no. The Chromecast isn't a passthrough — you can't run a cable from your iPhone into it and have it relay the signal. Chromecast only accepts video wirelessly over Google Cast; its USB port is power-only, not a video input. There's no physical-input path through it. So without the HDMI adapter, plugging in isn't an option tonight.

That collapses your choices to:

- **The SONIFI guest-cast SSID** — the one wireless path that might still work, if the front desk confirms casting runs on a separate network than the one you're on. This is your only no-hardware option.
- **Watch on the phone** — unfrustrating fallback for tonight.
- **Buy a USB-C-to-HDMI adapter tomorrow** if this is going to be a recurring need this week (you've got several more conference nights). A hotel gift shop or any nearby electronics store will have one; for an iPhone 15/16 USB-C, third-party brands work fine, so you don't need to hunt for Apple's.

Honestly, given it's nearly 5 and you've got the Hyatt meeting and conference load bearing down, I'd make the front-desk call the single attempt — "does casting run on a different Wi-Fi network than the guest one?" — and if that's a dead end, watch it on the phone and grab an adapter tomorrow. Not worth burning an evening on a protocol mismatch the property half-deployed.
