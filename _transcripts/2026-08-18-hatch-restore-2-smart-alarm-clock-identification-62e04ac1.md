# Hatch Restore 2 smart alarm clock identification
Date: 2026-08-18
Conversation: 62e04ac1-4b0d-4147-bbbb-dff883fbf074
Domain: skip

## Summary
**Conversation Overview**

The person shared network information about a device and asked Claude to identify it. Claude identified it as a Hatch Restore 2, a smart sunrise alarm clock and sound machine, explaining that the device naming convention (`Restore2-XXXXXX`) using the last six characters of the MAC address is the identifying pattern. Claude also noted that the Restore 2 operates exclusively on 2.4 GHz with no 5 GHz radio support, and that near-zero bandwidth usage is normal behavior since the device is largely offline except for firmware updates, routine sync, and content library access. The device is named Restore2-D87BDA and is located in the main bedroom on the 2.4 GHz network.

### SCOTT (2026-08-18T11:55)
What type of device is this?
[File uploaded: 68360d3a400f0a2d4f0518df254cc5c3ffd8c541.png]

### CLAUDE (2026-08-18T11:55)

A Hatch Restore 2 — the smart sunrise alarm clock / sound machine. The device name is the giveaway; Hatch units self-report as `Restore2-XXXXXX` using the last six of the MAC.

Two details that fit: it's on 2.4 GHz (Restore 2 is 2.4-only, no 5 GHz radio), and it's showing 0 kbps because it idles almost entirely offline — it only phones home for firmware, routine sync, and the Hatch+ content library.
