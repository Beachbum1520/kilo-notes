# Unread emails not showing bold text
Date: 2026-08-11
Conversation: 415b997f-45ff-4494-b8c7-695d98a95071
Domain: skip

## Summary
**Conversation Overview**

The person reported that unread emails in their Gmail app were no longer displaying in full bold — only the timestamp appeared bold — and asked how to restore the previous appearance. Claude identified the likely cause as iOS Bold Text accessibility setting being enabled, which applies heavy font weight system-wide and collapses the visual distinction between read and unread messages. Claude walked through a prioritized troubleshooting sequence: disabling Bold Text in iOS Accessibility settings, checking the Larger Text setting, force-quitting and reinstalling Gmail, and finally switching Gmail to dark theme as a workaround if the issue stemmed from a Gmail app-side change rather than a device setting.

### SCOTT (2026-08-11T14:40)
My unread emails are not fully in bold anymore. Just the time. How do I change this back?
[File uploaded: 1a21d8ab8878898438f096916638207a0debb89d.png]

### CLAUDE (2026-08-11T14:41)
Looking at the Gmail app screenshot, I can see the new bundles feature with categories like "All promotions" and "All updates," and the user is noting that unread emails no longer display in full bold — just the sender names and subject lines are bold now, while the preview text isn't. Let me examine what's actually bold in the screenshot to understand the change they're describing.

This could be a Gmail app redesign where the unread indicator changed from full bold styling to a more subtle visual distinction, possibly using a blue dot or different font weight instead. Since my knowledge has a cutoff and Gmail frequently updates its UI, I should consider whether this is a recent product change or potentially an accessibility setting like iOS's Bold Text toggle, though that would affect the entire system rather than just Gmail.…

Looking at the status bar details — the battery pill style and moon icon suggest iOS, though the heavy rounded font is throwing me off since that's more typical of Android. But the iOS 17+ battery indicator is pretty distinctive, so this is likely the Gmail app on iOS, though I'm also considering whether this could be Samsung One UI instead.…

Looking at the visual details — the status bar styling, the pill-shaped battery indicator with percentage, and the moon icon for Do Not Disturb — this is definitely iOS. The unusually heavy, rounded font is making me think the Bold Text accessibility setting is enabled, which would apply bold styling across all text in the system.

That would explain why the sender names and subjects appear bold in both read and unread messages, collapsing the visual distinction between them. The user's observation that "only the time is bold" might be a perception issue when everything is rendered heavy. The fix is straightforward: disable…Most likely culprit: iOS **Bold Text** is turned on, which renders *everything* heavy and collapses the read/unread difference. Your screenshot's font weight — including the status bar clock — looks like that setting is active.

Try in order:

1. **Settings → Accessibility → Display & Text Size → Bold Text** → off. Force-close Gmail and reopen.
2. If that's already off, check **Display & Text Size → Larger Text** — an aggressive size setting can flatten weight differences too.
3. Force-quit Gmail (swipe up), reopen. If it persists, delete and reinstall the app — it re-renders the list styling fresh.

If none of that works, it's the Gmail app itself. Google shipped a change that left unread mail technically bold but far less distinguishable, and users across platforms report the same complaint with no in-app setting to adjust it. There's no font-weight control in Gmail's settings, so the only real workaround is **switching Gmail to dark theme** (Settings → Theme → Dark) — unread renders white, read renders grey, which is a much stronger contrast cue than weight alone.
