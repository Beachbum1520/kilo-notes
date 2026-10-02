# iPhone WiFi signal strength scanner
Date: 2026-07-20
Conversation: df076326-2846-4b9e-a178-845184a31752
Domain: skip

## Summary
**Conversation Overview**

The person asked about iPhone apps that can display WiFi signal strengths. Claude explained that Apple's iOS platform restricts WiFi scanning APIs, preventing App Store apps from showing signal strength for nearby networks the way Android apps can. Claude identified two practical options: the AirPort Utility app (Apple's own tool, which includes a hidden WiFi Scanner accessible by enabling a toggle in iOS Settings before the scan option appears in the app), and Ubiquiti WiFiman (which shows signal data only for the currently connected network). Claude also noted that for more comprehensive site survey needs — such as all access points, per-channel utilization, and interference data — a laptop-based solution like WiFi Explorer on Mac or dedicated hardware tools such as NetAlly or Ekahau would be more appropriate than an iPhone. The AirPort Utility scanner was highlighted as the most capable option available on iOS for quick RSSI checks, with the specific note that the Settings toggle must be enabled first or the scan feature will not appear in the app.

### SCOTT (2026-07-20T21:33)
I need an iPhone app that will tell me WiFi signal strengths.

### CLAUDE (2026-07-20T21:33)
iOS has strict WiFi scanning limitations compared to Android, so apps can't display signal strength for nearby networks the way they can on other platforms. AirPort Utility does have a hidden WiFi scanner mode though, which might be relevant since Scott works in hospitality WiFi and probably needs site survey tools. This doesn't seem like something worth storing as a memory.Apple locks down WiFi scanning APIs on iOS, so no App Store app can show you signal strength of nearby networks the way Android apps can. Two workarounds:

- **AirPort Utility** (Apple's own app) — install it, then go to Settings → AirPort Utility → toggle on "Wi-Fi Scanner." Open the app and tap "Wi-Fi Scan" in the top right. Shows SSIDs, BSSIDs, RSSI, and channel. It's the only real scanner on iOS.
- **Ubiquiti WiFiman** — shows signal for your *connected* network plus speed tests and device discovery, but can't scan neighboring APs due to the same API restrictions.

If you need proper site survey data (all APs, per-channel utilization, interference), an iPhone won't cut it — you'd want a laptop with something like WiFi Explorer on Mac, or a NetAlly/Ekahau tool.

The AirPort Utility scanner is probably what you're after for quick RSSI checks — just remember the toggle in Settings first, or the scan option won't appear.
