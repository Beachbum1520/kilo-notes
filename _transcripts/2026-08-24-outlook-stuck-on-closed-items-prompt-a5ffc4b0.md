# Outlook stuck on closed items prompt
Date: 2026-08-24
Conversation: a5ffc4b0-1c1f-465c-80e1-093dfbf702ee
Domain: skip

## Summary
**Conversation Overview**

This conversation focused on diagnosing and resolving a persistent Microsoft Outlook startup hang for a user named Scott Watts, who operates under the username `swatts1` on a Windows machine. Scott runs two mailboxes simultaneously: `scott.watts@blueprintrf.com` (BPRF/Blueprint RF) and `scott.watts1@spectrum.com` (Spectrum), connected through a cross-tenant forwarding/dual-mailbox setup. The session walked through a full troubleshooting sequence: clearing the RoamCache (renamed to `.old` rather than deleted), attempting safe mode launch (`outlook /safe`), checking the Outlook connection status dialog, locating and running SCANPST (the Inbox Repair Tool), and scanning and repairing both OST files located at `C:\Users\swatts1\AppData\Local\Microsoft\Outlook\`.

Real corruption was found and repaired in both OST files — notably, the blueprintrf.com.ost was 12.2 GB and the spectrum.com.ost also showed errors. There was a tracking error mid-session where Claude incorrectly identified which OST had been scanned first; Scott caught this and corrected the record. After repairs, Outlook launched but remained in a spinning/loading state for 20+ minutes. Task Manager confirmed Outlook was still active (5.9% CPU, 0.2 MB/s disk) rather than truly hung, but ultimately a broader known service issue affecting classic Outlook desktop was identified (communicated via what appeared to be an internal notification from a colleague named Charlie), which explained why the hang persisted despite successful OST repairs.

As a resolution for the immediate need, Scott was directed to use Outlook Web Access (OWA) at outlook.office.com while on an active Webex call. Since Scott needed access to both mailboxes simultaneously in OWA, Claude explained the approach of using two different browsers or an InPrivate/Incognito window for the second account to maintain separate session cookies. Key colleagues referenced include Bill Prescott, Megan Dover (involved in the cross-tenant/merger setup), and Charlie (who flagged the broader Outlook service issue). Scott communicates concisely with brief messages and appreciates step-by-step guidance broken into small, actionable chunks rather than large blocks of instructions at once. AppData is a hidden folder on Scott's machine and required either direct path entry or enabling hidden items in Explorer to navigate.

### SCOTT (2026-08-24T14:34)
I can’t get past this screen. Multiple reboots. Any suggestions?
[File uploaded: photo.jpeg]

### CLAUDE (2026-08-24T14:34)
That "Outlook closed while you had items open" prompt getting stuck (even through reboots) is usually a corrupt session-restore cache, not a real crash. A few things to try in order:

- **Click "No" first**, not Yes — Yes tries to reopen whatever was open when it crashed, which can trigger the same freeze again.
- **Clear the reopen-items cache**: close Outlook completely, then delete `%localappdata%\Microsoft\Outlook\RoamCache` (or the `Wunderbar` file in older versions) — that's what stores "last session" state.
- **Start Outlook in safe mode**: Win+R → `outlook /safe` — if it opens fine, an add-in is likely hanging on startup. Check File > Options > Add-ins if so.
- **Reset the nav pane** in case it's a corrupted view: Win+R → `outlook /resetnavpane`.
- **Check Task Manager** before relaunching — make sure no orphaned `OUTLOOK.EXE` process is still running in the background from the previous crash; kill it if so.

Given the dual-mailbox/cross-tenant forwarding setup you're running right now, it's also worth flagging this to Bill Prescott or Megan Dover if it keeps recurring — sync conflicts between the two profiles can sometimes manifest as exactly this kind of hang on startup.

### SCOTT (2026-08-24T14:35)
How do I get to the local app data. Need the exact path

### CLAUDE (2026-08-24T14:35)
Type this directly into the Windows Explorer address bar (or Win+R):

```
%localappdata%\Microsoft\Outlook
```

Steps:
1. Close Outlook completely first (check Task Manager to confirm no `OUTLOOK.EXE` process is lingering).
2. Press **Win+R**, paste `%localappdata%\Microsoft\Outlook`, hit Enter.
3. Look for a file/folder named **RoamCache** — delete it (or rename it to `RoamCache.old` if you want a fallback).
4. Also check for a file called **Wunderbar** in the same folder — delete that too if present, it's an older version of the same cache.
5. Relaunch Outlook.

If Explorer won't let you type `%localappdata%` directly for some reason, the fully expanded path is typically:
```
C:\Users\<YourUsername>\AppData\Local\Microsoft\Outlook
```

### SCOTT (2026-08-24T14:37)
no wiunderbar.  so can try and resater outlook now

### CLAUDE (2026-08-24T14:37)
Yes — go ahead and relaunch Outlook now. Since you deleted RoamCache, it should rebuild a clean session cache on startup rather than trying to reopen whatever was hung before.

If it still throws the "Reopen items" prompt, click **No**. If it hangs again after that, next step is `outlook /safe` to rule out an add-in.

### SCOTT (2026-08-24T14:38)
i didnt delete. i renamed it .old

### CLAUDE (2026-08-24T14:38)
That works just as well — renaming it accomplishes the same thing since Outlook won't recognize `RoamCache.old` and will just build a fresh `RoamCache` on launch. You've still got the original as a fallback if needed.

Go ahead and relaunch Outlook now. Same next steps if it still hangs: click **No** on the reopen prompt, then try `outlook /safe` if it freezes again.

### SCOTT (2026-08-24T14:38)
nope.  same thing
[File uploaded: 1787582306583_image.png]

### CLAUDE (2026-08-24T14:38)
Okay, so that prompt is coming from somewhere else — not RoamCache. Click **No** on it first, then let's isolate what's actually hanging:

1. **Start in safe mode** to rule out an add-in: close Outlook, Win+R → `outlook /safe`. If it opens clean and fast, an add-in is the culprit — go to File > Options > Add-ins and disable anything non-Microsoft, especially any Cox/Charter-deployed ones from the merger.

2. **If safe mode also hangs**, it's not add-ins — try resetting the nav pane: Win+R → `outlook /resetnavpane`.

3. **Still stuck?** Try the full profile reset: Control Panel > Mail > Show Profiles > create a new profile and let it re-add your Exchange account. This is more involved (it'll resync), but it rules out a corrupted profile entirely.

Given you're running the dual-mailbox/forwarding setup with Spectrum, it's also worth checking whether there's a **second Outlook profile or cached credential conflict** — Win+R → `control panel` → Mail → "Show Profiles" — see if there are two profiles or duplicate accounts fighting on startup.

Try safe mode first and tell me what happens.

### SCOTT (2026-08-24T14:45)

[File uploaded: 1787582722048_image.png]

### CLAUDE (2026-08-24T14:45)
Good data point — safe mode still hangs, so it's **not an add-in**. That narrows it to profile corruption, OST/data file issue, or a server-side connection stall (which given your dual-mailbox/cross-tenant forwarding setup is a real possibility).

Next steps, in order:

1. **Check Outlook's connection status directly** — hold Ctrl and right-click the Outlook icon in the system tray → "Connection Status." This shows if it's actually stuck trying to talk to Exchange/O365 rather than a local UI hang. If one of your two mailbox connections (BPRF vs. Spectrum) is timing out, you'll see it here.

2. **Check OST file size/health** — Win+R → `%localappdata%\Microsoft\Outlook`, look for large `.ost` files. If one is huge or shows as recently corrupted, that's often the real cause of a hang that survives safe mode.

3. **Run SCANPST** (Inbox Repair Tool) on the OST — search Windows for `SCANPST.EXE` (usually under `C:\Program Files\Microsoft Office\root\OfficeXX\`), point it at the OST file, and let it scan/repair.

4. **If none of that resolves it, create a new profile**: Control Panel → Mail → Show Profiles → Add → let it re-add your Exchange account fresh. This is the most reliable fix for corruption but means a resync (can take a while depending on mailbox size).

Given this is happening right when you're mid cross-tenant migration, I'd also loop in Bill Prescott or Megan Dover now rather than after — a hang that persists through safe mode smells like it could be server-side on their end, not just a local Outlook glitch.

Try the Connection Status check first — that'll tell us if it's local or server-side.

### SCOTT (2026-08-24T14:48)
i have not idea what all of that os.
[File uploaded: 1787582842209_image.png]
[File uploaded: 1787582856623_image.png]

### CLAUDE (2026-08-24T14:48)
No worries — here's the short version: **everything on that screen says "Established" with 0 failures** in the Req/Fail column, and response times look normal (100–200ms range). That means Outlook is talking to the server just fine. So this rules out a server-side/connection problem — it's local to your machine.

That means it's down to either a corrupted data file or a corrupted profile. Next steps, in order:

1. **Close this window and close Outlook** (check Task Manager, kill any lingering `OUTLOOK.EXE`).
2. **Run the Inbox Repair Tool (SCANPST)**:
   - Press Win+R, paste this (adjust year if different): `C:\Program Files\Microsoft Office\root\Office16\SCANPST.EXE`
   - If that path doesn't exist, search Windows for "SCANPST" and it should find it.
   - Click Browse, navigate to `%localappdata%\Microsoft\Outlook`, and select your `.ost` file (there may be two — one for each mailbox).
   - Run the scan, let it repair anything it finds.
3. **Relaunch Outlook normally** (not safe mode) and see if it still hangs.

If it hangs again after that, the next move is a clean profile rebuild (Control Panel → Mail → Show Profiles → Add new), which is more of a hassle but reliably fixes this class of issue.

Want me to walk you through finding SCANPST step by step, or do you see it when you search for it?

### SCOTT (2026-08-24T14:50)

[File uploaded: 1787583046101_image.png]

### CLAUDE (2026-08-24T14:50)
Good, that's running exactly right. Let it finish — Phase 1 of 8 will move through consistency checks on the OST file.

A few notes while it runs:

- **Don't touch Cancel or close it** until it completes all 8 phases — interrupting mid-scan can create more corruption than it fixes.
- **This may take a few minutes** depending on mailbox size (yours has a lot of folders/PSTs based on that connection list, so give it time).
- **When it finishes**, it'll either say "no errors found" or list repairs made and ask you to confirm applying them — say yes if prompted.
- Once done, **repeat the same process for the Scott.Watts1@spectrum.com OST** if there's a separate one in that same folder — you've got two mailboxes syncing, so it's worth checking both.
- Then relaunch Outlook normally (not safe mode) and see if the hang is gone.

Let it run and let me know what it reports at the end.

### SCOTT (2026-08-24T14:54)

[File uploaded: 1787583249653_image.png]

### CLAUDE (2026-08-24T14:54)
That confirms it — errors found in the OST file, which lines up with what was causing the hang.

Go ahead and click **Repair**. Leave "Make backup of scanned file before repairing" checked (it already is) — that gives you a fallback copy if anything looks off afterward.

It'll take a few minutes given 86 folders and 48,325 items. Once it finishes:

1. Relaunch Outlook normally (not safe mode).
2. See if the "reopen items" prompt still appears or if it hangs.
3. If this OST had errors, the BPRF one likely does too — worth running SCANPST on `scott.watts@blueprintrf.com.ost` next using the same steps, once this one's confirmed fixed.

Let me know what happens after it repairs and you relaunch.

### SCOTT (2026-08-24T14:57)

[File uploaded: 1787583419299_image.png]

### CLAUDE (2026-08-24T14:57)
Repair's done. Click **OK**, then:

1. Run SCANPST again on the same file just to confirm it comes back clean (no new errors) — quick pass, good to verify.
2. Then do the same repair process on the other OST: `scott.watts@blueprintrf.com.ost` (should be in `%localappdata%\Microsoft\Outlook` under your main BPRF profile path, not the `swatts1` one).
3. Once both are clean, relaunch Outlook normally and test.

Let me know if the BPRF file also shows errors — given both mailboxes are running through that cross-tenant forward setup, it wouldn't be surprising if it does.

### SCOTT (2026-08-24T14:58)
last time it auto populated the fied
[File uploaded: 1787583517083_image.png]

### CLAUDE (2026-08-24T14:58)
That's fine — it just didn't remember the path this time. Click **Browse** and navigate to:

```
C:\Users\swatts1\AppData\Local\Microsoft\Outlook
```

You'll see two OST files in that folder:
- `scott.watts1@spectrum.com.ost` (or similar — the one you just repaired)
- `scott.watts@blueprintrf.com.ost` (the one you still need to check)

Select the **blueprintrf** one this time, then click **Start** to scan it.

### SCOTT (2026-08-24T15:00)
no app data folder there
[File uploaded: 1787583650200_image.png]

### CLAUDE (2026-08-24T15:00)
AppData is a hidden folder by default, so it won't show in that list even though it's there. Two ways around it:

**Fastest — just type the path directly** into the "File name" field at the bottom of this dialog:
```
C:\Users\swatts1\AppData\Local\Microsoft\Outlook
```
Hit Enter and it'll jump straight into that folder.

**Or show hidden folders** so you can navigate normally:
1. Click the **View** icon (the three-line icon near the top right, next to the split-pane icon) — or press **Alt** to bring up the menu bar, then View > Show > Hidden items.
2. AppData will then appear (slightly greyed out) inside your `swatts1` folder.

Try the first option — just paste that path into the File name box and press Enter.

### SCOTT (2026-08-24T15:02)

[File uploaded: 1787583725458_image.png]

### CLAUDE (2026-08-24T15:02)
Good, you found it. Select **scott.watts@blueprintrf.com.ost** (12.2 GB — that's a big one, so this scan will take longer than the last file) and click **Open**, then **Start** to run the scan.

Worth noting: the `scott.watts@blueprintrf.com.bak` file (12.2 GB) sitting there is the backup created during the previous repair — good to leave that alone for now in case it's needed as a fallback.

Once this scan finishes, if it finds errors, repair it the same way, then relaunch Outlook normally and test.

### SCOTT (2026-08-24T15:03)
runnign that now.  shoud I also scan the spectrum one?

### CLAUDE (2026-08-24T15:03)
No need — the spectrum.com.ost is the one you already repaired earlier (that's the one that showed "Repair complete"). This current scan is the blueprintrf.com.ost, which is the last one that needed checking.

Given it's 12.2 GB, let it run — could take a while. Once this one's done (and repaired if errors show up), you'll have covered both mailboxes and can relaunch Outlook normally.

### SCOTT (2026-08-24T15:05)
looks like same as before??
[File uploaded: 1787583901053_image.png]

### CLAUDE (2026-08-24T15:05)
Good catch — that's worth pausing on. Those numbers (86 folders, 48,325 items) are **identical** to what you saw on the spectrum.com.ost scan earlier. That's either:

1. A coincidence (less likely with that specific a number), or
2. This dialog is actually still referencing the same file as before (didn't properly switch), or
3. Because of the forwarding/mirroring setup between your two mailboxes, the content genuinely is near-identical in folder/item count.

Before clicking Repair, can you widen that dialog or hover over the truncated path at top to confirm it says **blueprintrf** and not **spectrum**? The filename is cut off at "scott.watts@" so we can't tell from this screenshot which one it actually scanned.

If it confirms as blueprintrf and just happens to match — fine, go ahead and click Repair (it's flagged as "minor," so it's a quick, low-risk one). But let's verify the path first so we know we didn't just re-scan the same file twice.

### SCOTT (2026-08-24T15:06)
C:\Users\swatts1\AppData\Local\Microsoft\Outlook\scott.watts@blueprintrf.com.bak

i think that is the same one scanned last itme.  i do not think spectrum has been scanned yet

### CLAUDE (2026-08-24T15:06)
You're right, and that's my error — good catch. Looking back, the very first SCANPST scan auto-populated with a path ending in **blueprintrf.com.ost**, not spectrum. So that first "repair complete" was actually the blueprintrf file, not spectrum like I told you. That's why this scan is showing identical folder/item counts — it's genuinely the same file, scanned twice.

So the real status is:
- **blueprintrf.com.ost** — scanned twice now, repaired once, only minor optional inconsistencies remain
- **spectrum.com.ost** — not actually scanned yet

Since you're already in this dialog, go ahead and click **Repair** anyway (it's optional/minor, low risk, and you're here). Then run SCANPST one more time, and this time explicitly browse to:

```
C:\Users\swatts1\AppData\Local\Microsoft\Outlook\scott.watts1@spectrum.com.ost
```

Type or paste that full filename directly into the "Enter the name of the file to scan" field rather than relying on browse/autopopulate, so we don't lose track again.

### SCOTT (2026-08-24T15:38)
this is the spectrum scan
[File uploaded: 1787585860486_image.png]

### CLAUDE (2026-08-24T15:38)
Good — this is the actual spectrum.com.ost this time (path confirms `scott.watts1`), and errors were found. Go ahead and click **Repair** (backup checkbox is already checked, leave it).

Once this finishes:
- Both OSTs will have been genuinely scanned and repaired.
- Close this dialog and relaunch Outlook normally.
- See if the "reopen items" hang is gone.

If it still hangs after both files are confirmed clean, the next step is a full profile rebuild — but let's see if this clears it first.

### SCOTT (2026-08-24T15:44)
outlook open.  but cursor is jsut spoinning.  should i give it a while and see if it works itself out?

### CLAUDE (2026-08-24T15:44)
Yes, give it a few minutes — this is actually expected. After a repair on a file that size (12+ GB), Outlook's first launch has to rebuild indexes and reconcile the data file, which can make it look frozen even though it's working in the background.

What to do:
- **Give it 5–10 minutes** before assuming it's stuck. Don't click anything or force-close.
- **Check Task Manager** in the meantime — look at the OUTLOOK.EXE process. If CPU or disk usage is active (even a few percent), it's working. If it's sitting at 0% CPU and 0% disk for several minutes straight, that's a sign it's actually hung.
- **Watch the disk activity light/Resource Monitor** if you want more certainty — heavy disk I/O right now would confirm it's reindexing rather than frozen.

If it's still spinning with no resource activity after ~10 minutes, then it's genuinely hung and we'd move to the profile rebuild. But given the file size and that real repairs just happened, this is very likely just it catching up.

### SCOTT (2026-08-24T15:59)
ya.  still spinning after at least 10 mins or more,.

### CLAUDE (2026-08-24T15:59)
Okay, that's long enough — let's check what's actually happening before deciding it's fully hung.

1. **Open Task Manager** (Ctrl+Shift+Esc), go to the **Details** or **Processes** tab, find `OUTLOOK.EXE`.
2. **Check CPU and Disk columns** for that process specifically:
   - If Disk is showing consistent activity (even 1-5 MB/s) → it's still working, could still be reconciling that large OST. Give it more time.
   - If both CPU and Disk are flatlined at 0 for a sustained stretch → it's actually hung, not just slow.

If it's flatlined:
- **Don't force-close yet** — right-click Outlook in the taskbar, see if "Close window" is responsive at all (sometimes the UI thread is dead but it'll still process a close request).
- If nothing responds, **End Task** via Task Manager.
- Then relaunch. If it hangs again immediately, that points toward profile corruption rather than the OST — next step would be **Control Panel → Mail → Show Profiles → Add** a new profile and let Outlook rebuild it clean against your Exchange account.

Check Task Manager first and tell me what CPU/Disk show for Outlook right now.

### SCOTT (2026-08-24T16:00)

[File uploaded: 1787587201490_image.png]

### CLAUDE (2026-08-24T16:00)
That's actually good news — Outlook is showing **5.9% CPU and 0.2 MB/s disk activity**, which means it's not truly hung, it's still actively working (likely still reconciling that 12GB+ OST file post-repair).

One thing worth flagging: your overall **system memory is at 83%**, which is high. If other apps (Chrome with 14 tabs, Teams, Webex, all open) are competing for RAM, that can slow Outlook's reindexing down further.

Given it's still active:
- **Give it more time** — for a file that size, post-repair reconciliation can genuinely take 20-30+ minutes, sometimes longer.
- **Consider closing Chrome tabs/Webex temporarily** to free up memory and let Outlook get more resources to finish faster.
- **Keep checking Task Manager every few minutes** — as long as CPU/Disk for Outlook stays above 0%, it's working, not stuck.

If it's still spinning with zero progress after another 15-20 minutes *and* CPU/Disk finally drop to flat 0%, that's when we'd say it's truly hung and move to ending the task. But right now the data says it's still processing.

### SCOTT (2026-08-24T16:00)
i cant close. webex.  i am working.  on a call now

### CLAUDE (2026-08-24T16:00)
Understood — don't close Webex, that makes sense. Leave it running.

Just let Outlook keep working in the background for now since it's still active (not hung). No need to babysit it constantly — check back in periodically, maybe every 10 minutes or so, and it should finish reconciling on its own.

If you need email in the meantime, Outlook Web Access (OWA) at outlook.office.com would let you check messages without touching the desktop app while it finishes in the background.

Focus on your call — this can wait.

### SCOTT (2026-08-24T16:04)
lookie lookie at what I just got
[File uploaded: 1787587468746_image.png]

### CLAUDE (2026-08-24T16:04)
Ha — well, that explains a lot. This is a known, broader issue affecting the classic Outlook desktop app for multiple users, not something isolated to your machine. All that OST repair work wasn't wasted (real errors were found and fixed), but it wasn't the root cause of the hang — this is.

Given that:

1. **Use OWA for now** (outlook.office.com) exactly like Charlie says — that'll get you back into email while you're on your call.
2. **Outlook Mobile is unaffected**, so your phone is a fine fallback too.
3. Once you're off your call, it might be worth a quick note to Charlie or whoever's tracking this letting them know your specific case: you saw the hang, ran repairs, found real corruption in both OSTs, and it's still not resolving — that's useful signal for them, especially if the dual-mailbox/cross-tenant setup makes your profile more exposed to whatever this broader issue is.

For now — just switch to the web version and get back to your call.

### SCOTT (2026-08-24T16:07)
from OWA, how do i open both my bprf and spectrum emails

### CLAUDE (2026-08-24T16:07)
Since these are two separate mailbox accounts (not just folders in one mailbox), OWA generally won't let you have both open in the same browser session — one login will overwrite the other's session cookie. A few ways to get both open at once:

1. **Use two different browsers**: e.g., BPRF mailbox in Chrome, Spectrum mailbox in Edge. Each browser keeps its own session, so both stay logged in simultaneously.

2. **Use an InPrivate/Incognito window for the second one**: Open outlook.office.com normally for your primary (BPRF) account, then open a separate **InPrivate/Incognito window** and sign into outlook.office.com again with the Spectrum credentials. Incognito windows don't share session cookies with your regular browser window.

3. **Or just switch back and forth in one browser**: Sign into outlook.office.com with BPRF, then when you need Spectrum, sign out and sign back in with the other account. Slower, but simplest if you don't need both live at once.

For your situation right now (mid-call, need quick access), **option 2 (incognito for the second account)** is probably fastest — no need to juggle two full browsers.
