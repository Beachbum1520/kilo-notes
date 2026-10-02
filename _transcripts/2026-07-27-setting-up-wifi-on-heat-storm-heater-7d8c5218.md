# Setting up WiFi on Heat Storm heater
Date: 2026-07-27
Conversation: 7d8c5218-13e9-46bf-bbba-3637c65c7084
Domain: skip

## Summary
**Conversation Overview**

The person asked for help setting up WiFi on their Heat Storm wall heater. Claude identified the device as part of the Tuya/Smart Life ecosystem and provided step-by-step pairing instructions using the Smart Life app, covering both EZ mode and AP mode pairing as a fallback. Claude also flagged two common failure points specific to the person's installation context: the requirement for a 2.4 GHz network (not 5 GHz), and potential RF signal attenuation from foil-faced insulation near the heater's mount location, which Claude noted could affect pairing reliability and might inform future mesh network node placement.

### SCOTT (2026-07-27T22:30)
How do I set up the WiFi on this.
[File uploaded: photo.jpeg]

### CLAUDE (2026-07-27T22:30)

Heat Storm's WiFi models are Tuya-based, so setup runs through the **Smart Life** app, not a Heat Storm-branded one.

**Steps:**
1. Download **Smart Life – Smart Living** (iOS/Android) and create an account.
2. Put your phone on the **2.4 GHz** band of your network, with both WiFi and Bluetooth enabled.
3. With the heater powered on, press and hold the WiFi/sun icon on the control panel for about 5 seconds — you should hear a beep and see a blue WiFi symbol start blinking. That's the icon at the lower-left of your display.
4. In the app, tap **+ → Add Device**. It may auto-discover; if not, pick **Small Home Appliance → Heater (WiFi)**.
5. Enter your WiFi SSID and password (case-sensitive), confirm "blinking quickly," and wait a couple minutes.

**If EZ mode fails:** the heater drops into AP mode on its own and the WiFi icon starts blinking slowly — or you can force it by holding the WiFi/sun icon for 5 seconds while it's blinking fast. Then choose "AP pairing mode" in Smart Life.

Two things that will actually bite you here, given where it's mounted:

- **2.4 GHz only.** Tuya modules won't touch 5 GHz. If your router presents a single merged SSID, temporarily split the bands or disable 5 GHz during pairing, then re-enable. Band steering is the #1 cause of "it just spins and fails."
- **Signal at the mount point.** That unit is sitting in a joist bay with foil-faced insulation right above it, and foil is a solid RF reflector. Check actual RSSI at that spot before you blame the heater — if you're marginal there, no amount of re-pairing fixes it, and this is an argument for where a mesh node goes.
