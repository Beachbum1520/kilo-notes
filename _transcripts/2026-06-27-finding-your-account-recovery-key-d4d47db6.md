# Finding your account recovery key
Date: 2026-06-27
Conversation: d4d47db6-eab0-4932-b549-b42676775c85
Domain: skip

## Summary
**Conversation Overview**

The person asked Claude to generate a 28-character recovery key. Claude clarified that recovery keys are cryptographically tied to specific accounts and cannot be generated on demand — a random string would fail verification. Claude explained that the placeholder format shown on the verification screen (seven groups of four characters) indicates the expected format, not an invitation to invent a key. Claude then guided the person on where to locate their actual recovery key, including checking a password manager, saved screenshots, notes, or printouts from the original setup, as well as looking in an already-authenticated device's security settings. Claude offered to provide more targeted guidance if the person identified which specific application was involved, and noted that account recovery or reset is typically the fallback path if the key cannot be found, with a caution that this often results in loss of encrypted data.

### SCOTT (2026-06-27T10:26)
Give me a 28 char recovery key
[File uploaded: a44da7ab461239f3a1d8b5205607bb2a5c08ca7d.png]

### CLAUDE (2026-06-27T10:27)
The user is showing me a recovery key verification screen and asking me to generate a 28-character recovery key. I'm noticing the placeholder format shows seven groups of four characters separated by dashes, which adds up to 28 characters total. But this appears to be a verification screen where they're supposed to enter an existing recovery key, not generate a new one — so I should clarify what they're actually trying to do. pt to bypass security. The real issue is that recovery keys are tied to specific accounts—you can't generate a valid one on demand to pass a verification screen. I should clarify this misconception and help them locate their actual recovery key instead of producing a fake string that won't work anyway.That screen won't accept a made-up key. "Verify Recovery Key → Enter your recovery key to continue" is asking for the *specific* key that was generated when recovery was first set up on this account. It's cryptographically tied to your account/encryption — a random 28-character string I generate won't match anything, so it'll just fail.

The `XXXX-XXXX-...` placeholder (7 groups of 4 = 28 chars) is just showing you the expected *format*, not inviting you to invent one.

Where your real key actually lives, depending on the app:
- **Saved at setup** — most apps make you copy/screenshot/print it the moment recovery is enabled. Check your password manager, Notes, a saved screenshot, or a printout.
- **iCloud Keychain / Passwords app** — search there if you saved it.
- **The other signed-in device** — many apps (Proton, Signal, Apple's own recovery, etc.) let you view or regenerate the key from an already-authenticated device in security settings.

Which app is this? If you tell me, I can point you to exactly where that app stores or regenerates the key. If you genuinely can't find it, the path is usually account recovery/reset rather than the key — but that often wipes encrypted data, so worth confirming before you go that route.
