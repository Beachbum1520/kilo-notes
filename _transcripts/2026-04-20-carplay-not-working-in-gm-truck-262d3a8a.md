# CarPlay not working in GM truck
Date: 2026-04-20
Conversation: 262d3a8a-8c6f-4343-a0f9-b315632622aa
Domain: skip

## Summary
**Conversation Overview**

The person asked for help troubleshooting a connectivity issue between their iPhone and their vehicle's infotainment system after replacing the cable without resolving the problem. Claude identified a terminology distinction upfront, clarifying that the feature in question is CarPlay (Apple's phone projection system) rather than AirPlay, and that GM labels this feature "Projection" in its interface.

Claude walked through a prioritized list of potential causes: cable quality issues (noting that even new cables may lack MFi certification and data capability), using the wrong USB port (charge-only vs. data-enabled), CarPlay settings disrupted by an iOS update, head unit needing a soft reset via the power knob, Screen Time restrictions blocking CarPlay, and the CarPlay feature being disabled within the truck's settings menu. Claude closed by asking diagnostic follow-up questions about whether the phone charges when plugged in, whether any error appears on screen, and whether the Projection icon responds when tapped. The conversation ended without the person providing further details or confirming which step resolved the issue.

### SCOTT (2026-04-20T12:59)
Why would the AirPlay quit working?  I got a new cable. And nothing.
[File uploaded: photo.jpeg]

### CLAUDE (2026-04-20T12:59)
 A few likely culprits, roughly in order of probability for a GM/Chevy infotainment setup like yours:

1. **It's CarPlay, not AirPlay.** GM calls it "Projection" (that icon in your photo). AirPlay is Apple's wireless audio/video streaming to Apple TVs and HomePods — it doesn't run on GM head units. If you're plugging your iPhone in to mirror maps/music, that's CarPlay. Worth naming correctly because the fixes are different.

2. **Cable issue even with a new cable.** "New" doesn't mean "works." CarPlay is picky — it needs a data-capable, MFi-certified Lightning/USB-C cable. Cheap Amazon cables often charge fine but fail the data handshake. Try a genuine Apple cable if you haven't.

3. **USB port.** On these GM trucks, only specific USB ports support CarPlay (usually the one marked with a phone/data icon, not the charge-only ports). If you're plugged into the wrong one, it'll charge but not project.

4. **iOS update broke it.** Very common. After an iOS update, CarPlay can stop handshaking until you toggle it off/on or reset. On your phone: Settings → General → CarPlay → tap your vehicle → Forget This Car. Then replug.

5. **Head unit needs a reset.** Hold the power knob (bottom left in your photo) for ~10 seconds until the screen restarts. Clears a surprising amount.

6. **Restrictions toggled on.** Settings → Screen Time → Content & Privacy Restrictions → Allowed Apps → make sure CarPlay is on.

7. **Projection disabled in the truck.** Tap that Settings gear → Apple CarPlay → make sure it's enabled for your phone.

What happens when you plug in now — does the phone charge? Any error on screen? Does the Projection icon do anything when tapped?
