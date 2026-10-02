# Bypassing email retention policy with Outlook rules
Date: 2026-09-18
Conversation: 30e3f4b0-b659-470f-bbd6-901389203f22
Domain: business-ops

## Summary
**Conversation Overview**

The person is navigating a 90-day email retention policy at their new organization and wanted to know whether an Outlook rule could automatically move emails to a local folder to preserve them beyond the retention window. Claude walked through two approaches: AutoArchive (which retroactively sweeps aging mail to a local .pst file) and inbox rules (which only handle new incoming mail going forward), noting that AutoArchive is the more useful option for this use case. Claude also flagged upfront that the effectiveness of either workaround depends entirely on how the retention policy is enforced — native Exchange MRM tags versus Microsoft Purview compliance labels — since Purview operates at the item level and cannot be circumvented by moving mail to a local store.

Through a series of screenshots shared by the person, Claude helped diagnose the retention mechanism step by step. The Outlook Account Settings dialog was ruled out as a useful diagnostic location. Checking the Inbox folder's Policy tab in Outlook confirmed the presence of a native Exchange MRM retention tag rather than a Purview-managed policy, which is relatively favorable for the PST workaround. However, the tag's disposition action (delete versus move to Online Archive) remained unclear because the self-service retention policy settings page in the browser rendered an empty content pane, providing no detail on what actually happens to mail at 90 days.

Claude's final recommendation was to check the Outlook folder pane for a secondary "Online Archive" mailbox node — which would confirm mail is being archived rather than deleted, eliminating the need for any workaround — and if that's inconclusive, to ask IT directly whether the 90-day tag deletes permanently or moves to Online Archive. Claude framed this as a factual configuration question rather than a request to bypass policy, to avoid raising compliance concerns. The person's email domain is blueprintrf.com.

### SCOTT (2026-09-18T13:55)
For our new org, there is a 90-day email retention policy, which is stupid to me.  is there an outlook rule i can wrtie to automagically move all my emaisl to a local folder or soemthing so ic an still get to my emails?

### CLAUDE (2026-09-18T13:56)
Short answer: yes, there are two ways to do this in Outlook, but whether it actually beats the retention policy depends on how that policy is enforced.

**Option 1 — AutoArchive (built-in, handles existing 90-day-old mail)**
File → Options → Advanced → AutoArchive Settings:
- Set "Clean out items older than" to something under 90 days (e.g. 60)
- Point "Move old items to" at a local .pst file
- Apply to Inbox/Sent/etc. (can set per-folder too)

This is the one you actually want, because it retroactively sweeps aging mail — a rule alone won't.

**Option 2 — Inbox rule (only catches new mail going forward)**
Rules → New Rule → "Apply rule on messages I receive" → no conditions → "move to folder" → point at a folder inside a local .pst data file (not an Exchange Online folder). This just relocates new mail as it arrives; it won't reach back and grab anything already sitting in the cloud mailbox past 90 days.

**The catch:** if your 90-day retention is a mailbox rule (Outlook/Exchange native retention policy tag), moving to a local PST gets you out from under it — a .pst on your local disk isn't part of the Exchange mailbox. But if it's enforced through Microsoft Purview (compliance/retention *labels* or an org-wide retention policy, common in a Cox/Charter merger integration scenario with legal-hold considerations), that operates at the item level independent of which folder or even which store the item lives in — it can still expire, delete, or hold a copy regardless of where you move it. A lot of orgs specifically disable PST export and AutoArchive via Group Policy/M365 compliance settings for exactly this reason — worth checking whether that's even available to you before you build a workflow around it.

Quick way to tell which kind you're dealing with: check Outlook → File → "Account Settings" → mailbox properties for a retention tag, or ask IT/compliance whether it's a Retention Policy or a Purview Retention Label. If it's Purview-driven, this workaround won't hold up under an actual audit or e-discovery pull.

### SCOTT (2026-09-18T13:59)
no properites here
[File uploaded: 1789739972590_image.png]

### CLAUDE (2026-09-18T13:59)
That screen just shows the accounts and their data files — not what you want. Here's where the retention tag actually shows up:

**Check via folder properties (fastest):**
1. In the main Outlook window (not this dialog), right-click **Inbox** in the left folder pane
2. Choose **Properties**
3. Look for a **Policy** tab — if present, it'll show the assigned retention policy/tag name (e.g. "90 Day Delete" or similar)
4. No Policy tab at all = it's likely not an Exchange native retention policy, which points more toward Purview

**Check via Outlook Options (often more reliable for merger-integrated tenants):**
1. **File → Options → Advanced**
2. Scroll to **AutoArchive** — click "AutoArchive Settings"
3. If it's greyed out / says "your organization has set policies" — that confirms IT/compliance has locked it down centrally, which is the strongest sign this is a Purview-managed policy, not a simple mailbox rule

**Also worth a quick look:**
- **File → Info** on the main Outlook window (not this popup) — sometimes displays a banner like "This account has policies applied by your organization" with a link to details

If AutoArchive is greyed out or the Policy tab is missing, that's your answer: the workaround I described won't work, because the org has locked local archiving down at the tenant level specifically to prevent people from routing around retention. In that case the real move is asking IT/compliance directly what the retention mechanism is and whether exceptions or a formal hold/export request exist — not building a rule that may just get flagged in an audit.

### SCOTT (2026-09-18T14:05)

[File uploaded: 1789740342222_image.png]

### CLAUDE (2026-09-18T14:06)
This confirms it: it's a native Exchange retention policy tag (MRM), applied specifically at the Inbox folder level — not Purview. That's actually somewhat good news, since native MRM tags are more mechanical and predictable than Purview labels, and the PST workaround is more likely to actually work here.

But the tag name alone doesn't tell you the important part: **what happens at 90 days** — delete, or move to an online archive. That changes everything about whether you need to do anything at all.

**Find the action:**
Click "Add or Remove Retention Policies" — it'll open a browser to the M365 compliance/Exchange admin retention tag details, or ask IT for the tag definition. You're looking for one of:
- **"Delete and Allow Recovery"** — items get deleted, recoverable for a short window (typically 14 days) via Recover Deleted Items, then gone. This is the case where you actually need a workaround.
- **"Move to Archive"** — items just relocate to an Online Archive mailbox after 90 days. If this is what's happening, you don't need PST/AutoArchive at all — your mail isn't disappearing, it's just moving to a second mailbox node (visible in Outlook's folder pane as a separate "Online Archive" entry) that you can still search and browse normally.

**Quick check:** look in your Outlook folder pane (left side) for a second mailbox entry below your main one, often labeled "Online Archive - scott.watts@blueprintrf.com" or similar. If that exists, your 90-day-old mail is likely already sitting there, not deleted — worth confirming before building anything.

If it turns out to be genuine delete-after-90, then go back to the AutoArchive-to-PST approach — but check whether AutoArchive is greyed out first (File → Options → Advanced), since orgs running MRM tags sometimes lock that down too to prevent exactly this kind of self-service export.

### SCOTT (2026-09-18T14:07)
this is what i see
[File uploaded: 1789740467447_image.png]

### CLAUDE (2026-09-18T14:08)
That page loaded but the content pane on the right is empty — that's telling you something too: end users typically don't get visibility into the retention tag's actual disposition (delete vs. archive) through this self-service settings page. That detail usually lives in the Exchange Admin Center or Purview compliance portal, which requires admin access you likely don't have.

A few things to try before giving up on self-service:

1. **Refresh the page** — sometimes this panel just fails to render on first load
2. **Scroll down in the left settings list** — there may be a distinct "Retention" or "Archive" entry separate from "Retention Policies" that has more detail
3. **Check the folder pane in classic Outlook (not this browser view)** for a second mailbox node like "Online Archive" — this is the fastest way to answer the delete-vs-archive question without needing admin visibility at all. If your >90-day mail is sitting there, it's archived, not deleted, and you don't need a workaround.

If none of that resolves it, this is the point where guessing stops being useful. Your fastest accurate answer is a one-line question to IT: **"Does the 90-day Inbox retention tag delete permanently or move to Online Archive?"** That's a factual/config question, not a request to bypass anything, so it shouldn't raise flags — and it settles in one reply what several more screenshots won't.
