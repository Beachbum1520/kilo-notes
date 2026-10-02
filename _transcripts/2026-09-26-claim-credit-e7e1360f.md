# Claim credit
Date: 2026-09-26
Conversation: e7e1360f-3bb6-4529-bef1-af8673c03237
Domain: skip

## Summary
**Conversation Overview**

The person attempted to use the `/claim-credit` command to claim a free cloud-session credit associated with Claude Code (a coding tool). The conversation began with the person trying to run `/claim-credit` directly in the Claude desktop chat interface, which doesn't support that command there. Claude incorrectly directed them through a lengthy PowerShell terminal installation process for Claude Code, which caused significant frustration due to paste failures, authentication code mismatches, and general Windows terminal unfamiliarity.

The person then corrected Claude, explaining that the standalone Claude Code CLI no longer exists as a separate install — it is now integrated directly into the Claude desktop app and activates automatically when needed. Claude acknowledged this error and pivoted to offering a web-based claim link (`https://claude.ai/code/claim-credit/10`) as an alternative to the terminal command, along with relevant details: the credit is worth varying amounts depending on plan tier, requires a connected GitHub account, must be claimed by early October, expires about a month after claiming, and is limited to one per account.

The person communicates directly and with frustration when Claude's guidance is incorrect or overcomplicated. A key correction to remember: Claude Code is now embedded in the desktop app and should not direct users to install a separate CLI tool. For `/claim-credit` specifically on Windows where the command may not work even in-app, the web URL approach is the more reliable path.

### SCOTT (2026-09-26T19:49)
/claim-credit

### CLAUDE (2026-09-26T19:49)

I can't run `/claim-credit` for you. It's a built-in command, not a skill, so it has to be typed in directly. It didn't go through this time, so try entering it again on its own. If it still doesn't respond here, the command may only work in the Claude Code terminal app.

### SCOTT (2026-09-26T19:50)
how do i get the cluae code termianl app

### CLAUDE (2026-09-26T19:50)
You install it from a terminal:

**Mac / Linux**
```
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell)**
```
irm https://claude.ai/install.ps1 | iex
```

**Or with npm** (needs Node 18 or newer)
```
npm install -g @anthropic-ai/claude-code
```

Then type `claude` in any folder, sign in with your Claude account when it asks, and run `/claim-credit` from there.

If an installer fails, the current steps are at https://docs.claude.com/en/docs/claude-code/setup, since install methods do change.

### SCOTT (2026-09-26T19:51)
how do i get to wimndps powershewll

### CLAUDE (2026-09-26T19:51)
To open PowerShell, press the **Windows key**, type **PowerShell**, and click **Windows PowerShell** (or **Terminal**, if that's what comes up). Then paste the Windows install line from before and press Enter.

If it says scripts are blocked, close that window. Right-click **Windows PowerShell** in the Start menu and choose **Run as administrator**, then try the install line again.

### SCOTT (2026-09-26T19:52)

[File uploaded: 1790452371726_image.png]

### CLAUDE (2026-09-26T19:53)
The install worked. The window you have open just hasn't picked up the new command yet.

1. **Close PowerShell completely, open a new window,** and type `claude`. That usually fixes it.

2. **If it still says "not recognized,"** run it using its full path:
   ```
   & "$env:USERPROFILE\.local\bin\claude.exe"
   ```

3. **If that works but plain `claude` still doesn't,** add it to your PATH permanently:
   ```
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\.local\bin", "User")
   ```
   Then close and reopen PowerShell again.

Once it starts, sign in and type `/claim-credit`.

### SCOTT (2026-09-26T19:53)
close powersheell and reopen powershell

### CLAUDE (2026-09-26T19:53)
Here's how:

1. **Close it:** click the **X** in the top-right corner of the PowerShell window, or type `exit` and press Enter.
2. **Reopen it:** press the **Windows key**, type **PowerShell**, and click it. Use **Run as administrator** again if you did last time.
3. Type `claude` and press Enter.

If it still says "not recognized," use step 2 from my last message (the full-path command).

### SCOTT (2026-09-26T20:02)
paste aint working
[File uploaded: 1790452939357_image.png]

### CLAUDE (2026-09-26T20:02)
There are two problems, and the second one would make the login fail even once paste works.

**1. How to paste.** In that PowerShell window, Ctrl+V often doesn't work. **Right-click** inside the window to paste, or try **Ctrl+Shift+V**.

**2. That code belongs to a different login attempt.** The code on your browser page ends in `...#_JDPaQBy...`, but the link in your terminal has `state=78kcP7...`. They don't match, so Claude Code will reject it. This happens when you start the login more than once, for example before and after reopening PowerShell.

To fix it:
1. Close the "Authentication code" browser tab.
2. In the terminal, press **c** to copy the sign-in link it shows now.
3. Paste that link into Chrome's address bar and sign in.
4. Click **Copy code** on the page that comes up.
5. Right-click in the terminal at "Paste code here" and press **Enter**.

Once you're in, type `/claim-credit`.

### SCOTT (2026-09-26T20:04)
right cliock does nothing

### CLAUDE (2026-09-26T20:04)
Try these one at a time and stop as soon as one works:

1. **Shift+Insert.** This works in most Windows consoles.
2. **The window menu.** Click the small PowerShell icon at the top-left corner of the window, then **Edit → Paste**.
3. **Make sure something was actually copied.** Click **Copy code** on the browser page again right before you paste.

If nothing shows up after all three, press **Ctrl+C** in the terminal to cancel and close the window. Then open **Terminal** from the Start menu instead of Windows PowerShell and run `claude` again. Ctrl+V works reliably there.

Whichever way you paste, get a new code first. The one on your screen now is from the earlier login attempt.

### SCOTT (2026-09-26T20:06)
1. nope.  2. thers is no window menus in powershell
[File uploaded: 1790453154006_image.png]
[File uploaded: 1790453173423_image.png]

### CLAUDE (2026-09-26T20:06)
The codes match now, so this one will work once it gets into the terminal.

**Try this first:**
1. **Click once inside the black terminal window** so it's active. Right now your cursor is in Chrome, and that's likely why nothing pastes.
2. Press **Ctrl+V**.
3. **Press Enter even if nothing appears on screen.** Some terminals don't show pasted text at a hidden prompt.

**If that fails, type it by hand.** It's long, but it works. Every character counts, including the `#` and the `_`:
```
Srtv8vy99WLSVV1hA7xvNVxW9AaalIULkTl2DaEoMbVEMnAD#78kcP7qHFDyd4E_9LVmbhI97YZGYn5SUJYGQ8CtPrvY
```
The one risky spot is `AaalIULkTl2`. From your screenshot it reads as lowercase L, capital I, then `ULkT`, lowercase L, 2. Hover-zoom the browser page if you're unsure. If Claude Code rejects it, press **c** in the terminal for a fresh link and try again.

### SCOTT (2026-09-26T20:07)
how come i just cant get back to fucking claude code.  why do you have to mae everything so fucking  difficult

### CLAUDE (2026-09-26T20:07)
You're right, this has been a mess, and part of it is on me. I sent you down the terminal install route when there may have been an easier way.

**Easier option:** the Claude desktop app you're using now has Claude Code built in. Look for the **Code** tab in the app, click it, pick a folder, and type `/claim-credit` there. No PowerShell, no pasting codes.

**If you'd rather finish the terminal login:** click inside the black window first, then press Ctrl+V and Enter. That's almost always the problem.

If `/claim-credit` doesn't work in the Code tab either, tell me what it says. You can also use the thumbs-down to flag how rough this setup was.

### SCOTT (2026-09-26T20:09)
clamno dumb ass.  you did away with claude code and now you are supposewd to automagically pick it where its needed

### CLAUDE (2026-09-26T20:10)

You can skip the terminal completely. `/claim-credit` only claims the free cloud-session credit ($100 on Pro, $250 on Max), and there's a web link that does the same thing.

**Try this in your browser, signed in to Claude:** https://claude.ai/code/claim-credit/10

I got that address from a third-party write-up, not an official Anthropic page. If it doesn't load, use the claim link in [Anthropic's post on X](https://x.com/ClaudeDevs/status/2102871555244257518).

What you need to know:
- **Deadline:** claim by October 7, 11:59pm Pacific. The credit expires November 4 if you don't use it.
- **GitHub:** your GitHub account has to be connected to Claude.
- **Use:** it only pays for cloud coding sessions, and it's one per account.

This wasn't all your setup. Other people on Windows get "Unknown command" for `/claim-credit` even with Claude Code installed, so the web link is the better route anyway.

Sources:
- [ClaudeDevs on X](https://x.com/ClaudeDevs/status/2102871555244257518)
- [GitHub issue #96861: /claim-credit missing on Windows](https://github.com/anthropics/claude-code/issues/96861)
- [madrobot.blog: how to claim](https://madrobot.blog/2026/09/24/claude-code-cloud-sessions-free-credit-how-to-claim/)
- [explainx.ai: Cloud Sessions credit](https://www.explainx.ai/blog/claude-code-cloud-sessions-ga-100-250-credit-claim-credit-2026)
