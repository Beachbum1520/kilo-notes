# Email forwarding issues after merger
Date: 2026-08-21
Conversation: 57d93125-d37f-4347-a881-926ce5cbcea4
Domain: business-ops

## Summary
**Conversation Overview**

Scott Watts is a professional at Blueprint RF (BPRF) navigating a complex dual-mailbox situation on day two of a corporate merger between BPRF and Spectrum/Charter. His two email addresses are scott.watts@blueprintrf.com (primary, customer-facing, tied to brand certifications with Marriott, Hilton, Hyatt, and other hotel brands) and Scott.Watts1@spectrum.com. The conversation focused on diagnosing and building interim workarounds for four interconnected problems caused by an admin-level forward from BPRF into Spectrum: mailbox overflow on the BPRF side, replies defaulting to the Spectrum address instead of BPRF, BPRF inbox rules not functioning on the Spectrum side, and duplicate calendar entries appearing in both mailboxes simultaneously.

Claude and Scott worked through a systematic diagnosis, ruling out self-service fixes after Scott confirmed the forward was not visible in OWA Rules or OWA Sync/Forwarding settings, establishing it as a tenant/admin-level configuration. Scott drafted and sent an email to IT leadership (Jady West, with Bill Prescott, Brian Tucker, Megan Dover, Kathy Hatala, Lewis Lemoine, and Lauren Taylor cc'd) requesting that BPRF be set as the primary mailbox with Spectrum as an alias. Bill Prescott replied explaining the forward is intentional while licensing for a proper mailbox migration is evaluated, and Megan Dover followed up noting the issue is broader than BPRF alone. Scott drafted replies to both, with Claude refining them. A key escalation point Scott raised — and Claude helped him articulate — is that BPRF is the customer-facing domain tied to brand LSP certifications, and a Marriott brand contact had already reached out to Par (BPRF's Marriott brand manager) about the email inconsistency, giving the issue external urgency beyond internal workflow friction.

For interim fixes, Scott implemented a Spectrum inbox rule routing forwarded BPRF mail to a parking folder using "sent to/cc contains blueprintrf.com" and "body contains blueprintrf.com" as combined OR conditions (the header-search option was discussed but not available in his environment, leading to the body-text workaround). For the calendar duplication problem, the fix was disabling automatic meeting request processing on the Spectrum profile specifically via File > Options > Mail > Tracking > uncheck "Automatically process meeting requests." Scott confirmed both fixes were implemented. The conversation concluded with Claude drafting a team-facing summary document Scott could send so colleagues could apply the same interim fixes, which included the confirmed IT end-state: BPRF as primary mailbox, Spectrum as alias only, once domain migration licensing is resolved. Key colleagues referenced include Par (Marriott brand manager), Julian, Kyle, Marie, and Dan (Scott's team). Scott's working style is direct and action-oriented; he prefers concise, paste-ready drafts over explanations, and pushes back quickly when suggestions don't match his actual environment or are redundant given steps already taken.

### SCOTT (2026-08-21T17:57)
The mereger is done.  we are on day 2.  one bypriduct is that I  now hwaw 2 emails address.  scott.watts@b;ueprintrf.cpom and scot.watts1@spectrum.com.  they have gone in and forwarded all of my brpf email to my spectrum email which is caung me probles.  replies are fillign up mu bprf mailsbox, my replies are showing as coming from Spectrum and not bprf, and all my my bprf accunt ruls and not activing on my spectrum profile .  any recpmedation on howe to fix this without goign through it

### CLAUDE (2026-08-21T17:57)
Three separate problems here, and they need different fixes. Given the Cox/Charter merger context, I'll assume both accounts are M365/Exchange (standard for a merger like this) — let me know if that's wrong.

**1. BPRF mailbox filling up**
This means IT set up a straight *forward* (copy stays + copy sent to Spectrum), not a *redirect* (mail moves, no copy retained). You can't fix the forwarding type yourself — that's a transport rule or mailbox-level setting your admin controls. Self-service workaround: set up an Outlook rule on the BPRF mailbox that auto-archives or deletes items older than X days from Inbox, so it doesn't hit quota. Not a real fix, just a stopgap.

**2. Replies showing as Spectrum, not BPRF**
This is almost certainly because you're now working out of the Spectrum mailbox/profile as your primary send account, and Outlook defaults "From" to whichever account owns the conversation view. Fix without IT:
- In Outlook, add the BPRF account as a **secondary account with Send As / Send on Behalf** permission (if you already have credentials or it's already added as an account, this is just a client-side setting, not a ticket).
- When replying to anything that's a BPRF-context thread, manually enable the **From field** (Options → From) and pick scott.watts@blueprintrf.com before sending.
- This is not sustainable at volume — worth flagging to whoever owns your identity migration, but you don't need a full ticket, just a one-line ask: "confirm Send As permissions are provisioned on the BPRF mailbox for my Spectrum profile."

**3. BPRF rules not running on Spectrum profile**
This is expected, not a bug. Inbox rules are server-side and mailbox-specific — they live on the BPRF mailbox, not on you. Once mail is forwarded to Spectrum, it's arriving in a *different* mailbox with no rules of its own. Two options:
- Rebuild the rules manually in the Spectrum mailbox (fastest, fully in your control, takes 10–15 min if you know your existing rule set).
- Ask IT for a rules export/import between mailboxes if you're on the same M365 tenant now — but this is the one thing you likely can't self-serve if the tenants haven't merged yet.

**Bottom line:** #2 and part of #3 you can fix yourself today in Outlook client settings. #1 and full rule migration need a minimal, targeted IT ask — not a full ticket, just a two-line message confirming forward type and Send As provisioning. Want me to draft that message so it reads as a quick clarifying ask rather than an escalation?

### SCOTT (2026-08-21T17:58)
how do i add this: In Outlook, add the BPRF account as a secondary account with Send As / Send on Behalf permission

### CLAUDE (2026-08-21T17:59)
Depends on whether IT already granted you Send As permission on the BPRF mailbox at the server level — that's the actual permission grant, and it has to exist before Outlook will let you send as that address. Adding it in Outlook is just exposing a permission that already exists; it doesn't create one.

**Step 1 — Check if the permission already exists**

Try this quick test first: New Email → click **From** (if you don't see a From field, go to Options → From in the new message window) → click **Other Email Address** → type scott.watts@blueprintrf.com → send a test to yourself.

- If it sends without error → permission already exists, you're done, skip to Step 3.
- If it errors ("You do not have permission to send as this account") → you need IT to grant Send As (or Send on Behalf) rights on the BPRF mailbox to your Spectrum identity. That's a one-line ask, not a project.

**Step 2 — Add BPRF as a full secondary account (recommended over the "Other Email Address" trick above, since it also lets you see the BPRF mailbox's folders/rules)**

1. File → Add Account
2. Enter scott.watts@blueprintrf.com
3. If prompted for a password and you know the BPRF credentials, sign in directly.
4. If it instead authenticates you automatically (common when both accounts sit in the same tenant post-merger) or asks for the Spectrum account's credentials, that means it's relying on delegated/Send As permission rather than a full separate login — this only works if Step 1's permission is already granted.
5. Once added, the BPRF mailbox appears as a second set of folders in the left-hand pane in Outlook.

**Step 3 — Set From correctly on replies**

- On any new message: click the From field, select scott.watts@blueprintrf.com from the dropdown.
- On a reply to a BPRF-context thread: Outlook should default From to whichever account received the mail, but since it's arriving via forward into Spectrum, it'll default to Spectrum — you'll need to manually switch From every time until forwarding is fixed at the source.

**If Step 1 fails:** the message to IT is simply — *"Please confirm Send As (or Send on Behalf) permission is granted on the BPRF mailbox for my Spectrum identity, so I can reply as scott.watts@blueprintrf.com from Outlook."* That's a permissions grant, typically same-day, not a migration ticket.

### SCOTT (2026-08-21T18:00)
but i have both emails accounts set up as different profiles.  i thinl the from drop dwon is indicting wheic accoutn it sends from.
[File uploaded: 1787335181210_image.png]

### CLAUDE (2026-08-21T18:00)
That screenshot actually answers Step 1 for you — good news. Since **scott.watts@blueprintrf.com** already shows up as a selectable option in the From dropdown (not grayed out, not an error), that confirms Send As permission already exists on the BPRF mailbox for your profile. You don't need to ask IT for that permission — it's already there.

What this dropdown means practically:

- This is a **per-message** setting, not a default. Every time you compose or reply, Outlook will default to whichever account/profile you're currently working in — likely Spectrum, since that's where mail is landing now — and you'll need to click **From** and manually select scott.watts@blueprintrf.com each time you want a BPRF-branded reply.
- There's no persistent "always send as BPRF" toggle in this dropdown — it resets to default behavior each new message.
- **Manage List** in that dropdown lets you add/remove which addresses show up as options, but it won't let you set a permanent default From account within a single profile.

Two ways to reduce the manual step:

1. **Reply from within the BPRF profile itself, not Spectrum.** If mail didn't have to be forwarded, replying from the BPRF profile directly would default From to BPRF automatically. Since forwarding is copying everything into Spectrum, you're now doing all your work in the wrong profile by default. If you can, check the BPRF profile — mail may still be arriving there too (forwards usually don't remove the original), so you could just work from that profile for BPRF-context threads instead of clicking From every time.
2. **If you must stay in the Spectrum profile,** the manual From-switch is your only option per Outlook's design — there's no rule that auto-sets it based on which thread you're replying to.

Given you already have Send As working, the real fix isn't a permissions ask anymore — it's a **process decision**: which profile do you treat as "home" for BPRF replies going forward until the mailboxes are truly merged?

### SCOTT (2026-08-21T18:02)
thats the probelm.  two profiules two calendar. to inboxes, etc.  not sustainable
[File uploaded: 1787335271305_image.png]

### CLAUDE (2026-08-21T18:02)
Confirmed — you're maintaining two live mailboxes, two calendars, two rule sets, and mail is duplicating into Spectrum via subfolders ("BPRF Helpdesk," "Support & NOC Tickets") instead of actually consolidating. That's a forward-with-copy, and long-term it's not fixable from your end — it needs an admin change. But there's a real first move you should try before escalating.

**Check whether the forward is a mailbox rule you control, or an admin-level transport rule.** This determines everything else.
```
Fixing duplicate BPRF/Spectrum mailboxes and calendars post-merger

```

The core issue: right now you're maintaining the forward *and* both accounts natively side-by-side, which is why you're getting duplication instead of consolidation. Once you turn off the copy-forward (either yourself if it's a mailbox rule, or via one narrow IT ask if it's transport-level), the "two profiles" setup actually becomes fine — you'd just be checking two native inboxes with no duplication, no misattributed From, and rules working correctly in each because they're each running on their own real mailbox instead of a forwarded copy landing in the wrong one.

That's a very different ask than "please merge my mailboxes" — it's "please stop copying mail I'm already getting natively," which should move fast even on day 2 of a merger.

### SCOTT (2026-08-21T18:05)
calendar already there.  everything is duplicated. so your suggestiosn to overal doesnt help
[File uploaded: 1787335493942_image.png]

### CLAUDE (2026-08-21T18:05)
Fair — that screenshot shows the real cause, and it invalidates the overlay idea. This isn't a display problem, it's duplicate calendar items being created independently in both mailboxes, which is the same forwarding root cause as your email, just showing up as calendar entries instead.

Here's what's actually happening: when a meeting invite email gets forwarded from BPRF into Spectrum, Outlook doesn't just show you a copy — it processes that invite and creates its own independent calendar entry in the Spectrum calendar the moment it's opened or auto-accepted. So now you have two separate, unlinked appointment objects for the same meeting. That's why overlay didn't help — overlay stacks two *different* calendars together; it doesn't merge duplicate *copies of the same event* sitting in each one.

**Fix has two parts:**

**1. Stop future duplication** — same fix as email: get the calendar-invite forward turned off (or confirm it's a rule you can kill yourself in OWA settings). Once organizers' invites go only to the address they actually invited, new meetings will land in one calendar, not both.

**2. Clean up what's already duplicated** — this part is manual, there's no bulk dedup in Outlook for this:
- Pick one mailbox as canonical per meeting (whichever address the organizer *actually* invited — check the meeting's "Invite" details/organizer field, it'll usually show which address was targeted).
- Delete or decline the duplicate copy sitting in the other calendar.
- For recurring series (like your daily "Spectrum Updates" and "GRET RFP" blocks), you only need to do this once per series, not per instance — deleting the recurring master should clear all future duplicate instances at once.

Given the volume you're showing (nearly every block duplicated), this is worth doing systematically rather than piecemeal: pick a day, go slot by slot, decide canonical vs. duplicate, delete the duplicate. Painful once, but there's no shortcut — and it stops growing once the forward is off.

### SCOTT (2026-08-21T18:06)
i downt see the forward in owa

### CLAUDE (2026-08-21T18:06)
That actually confirms it — if it's not in Settings > Mail > Rules, check one more spot first, since OWA splits this into two separate settings:

**Settings (gear) > Mail > Sync email > Forwarding** — this is a distinct toggle from Rules, specifically for auto-forwarding, and won't show up under Rules at all.

If that's also empty, then this is being done at the tenant/admin level — most likely one of:

- **A mailbox-level forwarding attribute** set directly on your account in Exchange Online by an admin (via PowerShell or admin center), which is invisible to you in OWA entirely — not a rule you'd ever see from your side.
- **A transport/mail-flow rule** at the organization level (Exchange admin center, not your mailbox), redirecting based on your address — also invisible to end users by design.

Either way, you've now ruled out the self-service option. This isn't something you can find or fix from your seat — it's configured centrally, likely as part of the merger identity/migration plan (forwarding old-domain mail to new-domain mailboxes is a standard interim step).

**Ask to send IT, tightened up now that you've confirmed it's not user-visible:**

> "Can you confirm whether my BPRF mailbox has a forwarding rule or mailbox-level forward set to my Spectrum address? It's not visible in my own OWA Rules or Forwarding settings, so it must be admin-configured. It's duplicating both email and calendar invites into both mailboxes. Can this be changed to a clean redirect (or turned off, since I have both accounts natively in Outlook already)?"

That's specific enough that whoever handles it can look in the right place (mailbox forwarding attribute or transport rule) instead of telling you to check Rules again.

### SCOTT (2026-08-21T18:07)
give me a summary of the issues and my ask to solve it (borf needs to be proay reply email on spectrum account and the spetcrum shoudl be listed as an alsis. so I can send to leaderhio

### CLAUDE (2026-08-21T18:07)
**Summary of issues (for leadership context):**

Since the Spectrum/BPRF email transition took effect, mail and calendar invites addressed to scott.watts@blueprintrf.com are being forwarded to Scott.Watts1@spectrum.com. This is causing:

1. **Mailbox overflow** — BPRF mail is accumulating unread/unmanaged since it's being worked from Spectrum instead.
2. **Misattributed replies** — Replies to BPRF-context threads default to sending From Spectrum, so external partners and hotel brand contacts see a Spectrum address instead of BPRF.
3. **Broken automation** — Inbox rules configured on the BPRF mailbox don't carry over, so BPRF-side routing/triage isn't functioning on the Spectrum side.
4. **Duplicate calendar entries** — Meeting invites are creating separate, unlinked calendar objects in both mailboxes rather than a single synced entry, so the calendar is now fully duplicated across both accounts.
5. **No self-service fix available** — Confirmed the forward isn't a rule visible in OWA (checked both Mail > Rules and Mail > Sync email > Forwarding), meaning it's configured at the mailbox or tenant level and requires IT/admin action.

**The ask:**

Rather than continuing to run two parallel identities, request Spectrum.com be set up as a **secondary alias** on the primary scott.watts@blueprintrf.com mailbox — so:

- BPRF remains the **primary send/reply address** externally (preserving brand identity with hotel partners, vendors, and BPRF-side stakeholders).
- Spectrum.com becomes an **alias only**, allowing mail sent to either address to land in one unified mailbox, with replies defaulting to BPRF.
- This eliminates duplicate mail, duplicate calendar entries, and restores BPRF-side rules/automation, since there'd be one mailbox instead of two forwarding into each other.

---

Here's a paste-ready draft:

---

**Subject: Email Consolidation Request — BPRF Primary / Spectrum Alias**

Jady,

Since the merger transition, I've been operating with two separate mailboxes (scott.watts@blueprintrf.com and Scott.Watts1@spectrum.com), with BPRF mail currently set to auto-forward into Spectrum. This is creating several operational problems:

1. BPRF mail is accumulating unmanaged since I'm now working primarily from Spectrum.
2. Replies to BPRF-context threads are defaulting to sending from my Spectrum address, which is inconsistent with our external-facing BPRF brand identity with hotel partners and vendors.
3. BPRF-side inbox rules and automation aren't functioning on the Spectrum side, so routing/triage is broken.
4. Calendar invites are duplicating as separate, unlinked entries across both calendars rather than syncing to one.

I checked whether this is something I can resolve myself (OWA Rules and Sync/Forwarding settings on my end), and it's not — this is configured at the mailbox or tenant level, so it needs IT/admin action.

**Requested fix:** Rather than maintaining two parallel accounts, I'd like scott.watts@blueprintrf.com set as my primary mailbox and send/reply address, with Scott.Watts1@spectrum.com added as a secondary alias only. This would consolidate mail into a single inbox, preserve BPRF as my external identity, and resolve the duplication on both email and calendar.

Happy to loop in IT directly if that's the faster path — let me know how you'd like this routed.

Scott

### SCOTT (2026-08-21T18:10)
put a nice sentece at the bootm askign if it can be done pretty quicly so as not cause confusion with my team son our cutomers

### CLAUDE (2026-08-21T18:10)
Here's the draft with that line added at the bottom:

---

**Subject: Email Consolidation Request — BPRF Primary / Spectrum Alias**

Jady,

Since the merger transition, I've been operating with two separate mailboxes (scott.watts@blueprintrf.com and Scott.Watts1@spectrum.com), with BPRF mail currently set to auto-forward into Spectrum. This is creating several operational problems:

1. BPRF mail is accumulating unmanaged since I'm now working primarily from Spectrum.
2. Replies to BPRF-context threads are defaulting to sending from my Spectrum address, which is inconsistent with our external-facing BPRF brand identity with hotel partners and vendors.
3. BPRF-side inbox rules and automation aren't functioning on the Spectrum side, so routing/triage is broken.
4. Calendar invites are duplicating as separate, unlinked entries across both calendars rather than syncing to one.

I checked whether this is something I can resolve myself (OWA Rules and Sync/Forwarding settings on my end), and it's not — this is configured at the mailbox or tenant level, so it needs IT/admin action.

**Requested fix:** Rather than maintaining two parallel accounts, I'd like scott.watts@blueprintrf.com set as my primary mailbox and send/reply address, with Scott.Watts1@spectrum.com added as a secondary alias only. This would consolidate mail into a single inbox, preserve BPRF as my external identity, and resolve the duplication on both email and calendar.

Happy to loop in IT directly if that's the faster path — let me know how you'd like this routed.

If we could get this turned around fairly quickly, I'd appreciate it — I want to avoid any confusion for my team or our customers in the meantime.

Scott

### SCOTT (2026-08-21T18:20)
email sent.  what can i do in the meantime to make this more manabeable?  Set riule to auto archive all things specturm and jsut deal with the spectrum email?

### CLAUDE (2026-08-21T18:20)
That's a reasonable interim strategy — since the fix is pending, the goal now is to stop fighting two mailboxes and just pick one to actually live in until IT resolves it. A few refinements to make it work cleanly:

**1. Don't archive Spectrum — archive/mute BPRF instead**
Since mail is being forwarded *into* Spectrum, Spectrum is your live, complete copy of everything. BPRF is now just the leftover half that's piling up. So:
- In the **BPRF mailbox**, set up a rule: move all incoming mail straight to a folder (call it "Legacy — Archived") instead of Inbox. This stops the unread count from climbing and keeps BPRF out of your way, while still preserving anything that lands there in case you need to reference it later.
- Don't delete BPRF mail — just get it out of your active view.

**2. Rebuild your critical rules in Spectrum, not BPRF**
Since BPRF rules aren't carrying over, pick the handful that actually matter operationally (VIP senders, ticket routing, whatever you rely on daily) and recreate just those in the Spectrum mailbox. Don't try to port everything — just the ones with real operational cost if missed.

**3. Fix the From default once, not per-email**
Since you'll be working from Spectrum: for any recurring external contact (Marriott, Hyatt, vendors, etc.) where BPRF identity matters, get in the habit of checking From before every send — there's no way to force a permanent default per-thread in Outlook, so this is just discipline until the alias fix lands.

**4. Calendar — stop the bleeding, don't backfill-clean yet**
Given the request is already in and hopefully quick, I'd hold off on manually deduping the whole calendar right now — that's real time spent on something that may partially resolve itself once IT actions the alias (new invites will stop duplicating; old duplicates will still need manual cleanup either way, but no reason to do it twice). For the next few days, just mentally treat one calendar (pick Spectrum, since that's your working copy) as canonical for your own reference, and ignore the duplicate side unless someone else is checking your BPRF calendar directly for availability.

**5. One heads-up to your team**
Worth a quick one-line note to Julian, Kyle, Marie, and Dan: *"Working primarily from Spectrum.com for now during the email transition — if something urgent doesn't get a response, resend to my Spectrum address."* Cheap insurance against something falling in the gap while this sorts out.

This keeps you functional without doing double work that a system fix will make irrelevant in a few days anyway.

### SCOTT (2026-08-21T18:26)
already gotreply, and my draft.  help me clean it up.

Thanks for the reply Bill.
I completely understand.  If that is the case, can we turn off the forward that has been applied to my BRF email accoumt. Much easier to live with in two if evwerythign doesn’t have to be reviewed twice. 
From: Prescott, Bill <Bill.Prescott@spectrum.com> 
Sent: Friday, August 21, 2026 2:24 PM
To: Watts, Scott (CCI-Blueprint RF) <scott.watts@blueprintrf.com>; Tucker, Brian (CCI-Atlanta) <Brian.Tucker@cox.com>; Dover, Megan (CCI-Atlanta) <Megan.Dover@cox.com>; West, Jady (CCI-Southwest) <Jady.West@cox.com>; Hatala, Kathy (CCI-Atlanta) <Kathy.Hatala@cox.com>; Lemoine, Lewis (CCI-Southeast) <Lewis.Lemoine@cox.com>; Prescott, Bill (CCI-Atlanta) <bill.prescott@cox.com>
Cc: Taylor, Lauren (CCI-Atlanta) <Lauren.Taylor@cox.com>
Subject: Re: [EXTERNAL] Help Needed | Email Addresses
	You don't often get email from bill.prescott@spectrum.com. Learn why this is important 
Scott,
In order to facilitate the ultimate move of the BPRF domain into the Charter tenant, you'll need to live in two mailboxes for now with BPRF being your primary while you monitor your Spectrum mailbox for any corporate communication.  We'll continue the maintain the forwarding to help facilitate an easy mailbox transfer once the plan timing is defined to move the BPRF domain into the Charter tenant; until then we can't set either side as authoritative for the other since the we're straggling two tenants for now. 
I can appreciate this creates some workload challenges, but it's not necessarily avoidable until we get the domain swung over the Charter in the coming weeks.
Thanks for understanding.
Bill
________________________________________

### CLAUDE (2026-08-21T18:27)
Here's a cleaned-up version — I tightened the grammar/typos but kept your ask intact, since it's a fair pushback even though Bill just explained the forward is intentional:

---

Thanks for the context, Bill — that makes sense given the tenant timing.

Given that, is there any way to turn off the forwarding on the BPRF side specifically, and just have me monitor Spectrum separately for corporate communications? Living in two mailboxes is manageable, but having everything duplicate into both (including calendar invites, which are now creating separate duplicate entries in both calendars) means I'm reviewing everything twice rather than once. If I can just check Spectrum on its own for anything corporate, that would cut the workload significantly until the domain move happens.

---

One thing worth flagging before you send: Bill's reply just told you the forward is intentional and necessary until the domain migration — so simply asking to "turn it off" may get a repeat of the same explanation. The version above reframes the ask as **stop the duplication specifically**, while still doing what he asked (monitoring Spectrum separately) — that's a more answerable ask than a flat "turn it off," and it also flags the calendar duplication problem, which he may not know about yet.

### SCOTT (2026-08-21T18:31)
if they say no to removing the forward, which is likely, on the spectrum side, I should be able to set a rule that says anything from my bprf email gets auto-delted?  Here is an email as it shows up in my spectrum email account
[File uploaded: 1787337071419_image.png]

### CLAUDE (2026-08-21T18:32)
Yes, that's workable — and actually a cleaner version of the "auto-archive Spectrum" idea from before, just flipped to match what Bill just told you (BPRF is primary, Spectrum is for monitoring corporate comms only).

**How to build the rule**, based on what's visible in that screenshot: the message landed in your Spectrum mailbox, but the **To field still shows "Watts, Scott (CCI-Blueprint RF)"** — meaning it was actually addressed to your BPRF address and got forwarded in. That's your reliable filter condition, not sender:

- Rule condition: **"Sent to" contains scott.watts@blueprintrf.com** (not sender domain — plenty of legitimate Spectrum-native mail will come from cox.com/spectrum.com contacts too, so filtering by sender would catch things you actually need)
- Rule action: move to a folder (e.g., "BPRF — Forwarded Copy"), not straight to Deleted Items

**One change I'd push back on: don't auto-delete, auto-archive instead.** Two reasons:
1. That email thread is tagged **"Internal Use Only"** with a **90-day retention policy** — auto-deleting could interfere with retention/compliance requirements before that window closes, especially with Cox/Charter leadership on the thread.
2. If something ever gets missed on the BPRF side (out sick, BPRF mailbox has an issue, etc.), you'd have zero fallback if it's already deleted. A parking folder costs you nothing and gives you a safety net.

**Net effect:** BPRF stays your primary working mailbox as Bill directed, and Spectrum quietly collects the forwarded duplicates out of your way in a folder you basically never have to open — instead of landing in Inbox and forcing a second review of everything you already handled in BPRF.

### SCOTT (2026-08-21T18:35)
ok.  that rulw is done.  but wont catch where my bprf address is a a part of a distro that someone is rpelying to
[File uploaded: 1787337293281_image.png]

### CLAUDE (2026-08-21T18:35)
Good catch — you're right, that rule only catches mail sent directly to your personal address. This message is To Corey Stevens, Cc'd to a distro (**BPRF - Hilton Directives**) — your address never appears in the recipient line at all, so the "sent to blueprintrf.com" condition won't trigger on it.

Two ways to close that gap:

**1. Broader, more reliable: filter on message header instead of To/Cc field**
In the rule wizard, use the condition **"with specific words in the message header"** and search for `blueprintrf.com`. Forwarded mail generally retains the original envelope/header info even when the visible To/Cc shows a distro name — this catches it regardless of which BPRF distro list you're on, without you having to enumerate every list.

**2. Belt-and-suspenders: add known BPRF distros as explicit conditions**
Since header-based catching depends on how the forward preserves headers (and that can vary), it's worth also explicitly adding any BPRF distros you're regularly on — "BPRF - Hilton Directives" being one you now know about. Add these as additional "sent to" conditions (Outlook lets you OR multiple recipients in one rule). You'll likely discover more of these over time as you see them show up in Spectrum — just add each one to the rule as you spot it.

**Practical approach:** Start with the header-based rule (#1) since it's the most durable single fix, then treat #2 as an ongoing patch list — every time you see a BPRF-context email land in Spectrum that the header rule missed, add that distro to the rule so it's caught next time.

One caveat: this Hilton one is flagged **"Internal Use Only" / 90-day retention**, same as the Bill Prescott thread — worth double-checking your rule routes to a parking folder, not deletion, for the same compliance reason as before.

### SCOTT (2026-08-21T18:45)
here is bills reply
[File uploaded: 1787337950372_image.png]

### CLAUDE (2026-08-21T18:46)
That's actually a better answer than a flat no — Bill's not defending the forward as necessary long-term, he's saying it's a stopgap **specifically because of licensing uncertainty** for a real mailbox migration. That's a concrete blocker you can track, not just "policy." It also implies if licensing *is* available, a real migration (not just alias/forwarding) could happen — which is actually a better outcome than what you originally asked for.

**You don't need to push further right now.** Bill's actively checking something on your behalf; a follow-up push would just be noise. A short acknowledgment is enough:

> Sounds good, Bill — appreciate you checking. Let me know what you find out, and happy to help however I can if there's anything on my end that speeds up the licensing check.

**What to actually do while you wait:** Treat this as open and unresolved, not closed. A few things worth doing given it's now a licensing/procurement question rather than a pure workflow one:

- Keep the interim rules you've built (BPRF-primary, Spectrum parking folder, header-based catch-all) — they're your bridge regardless of how long licensing takes.
- If you don't hear back in a week or so, a light check-in is fair — this is the kind of thing that can quietly stall behind other merger priorities.
- Worth noting internally (not to Bill) that this may take longer than "coming weeks" if it's gated on licensing procurement — so don't assume the current workaround is short-term. Build your rules as if you'll be living this way for a while.

### SCOTT (2026-08-21T19:00)
give me a sympatheitc rpely here but state nciely that wth bprf as this is out cutser facoing domain tied to brand certifactiosn, etc. and thta our maaiort brand conatcty has alrweady reached out my brand maage askign to get this fixed.
[File uploaded: 1787338808715_image.png]

### CLAUDE (2026-08-21T19:00)
Here's a draft:

---

Megan,

Appreciate you flagging that — good to know it's not isolated to BPRF, and helpful context that IT is still working the broader problem.

That said, I'd gently push that BPRF carries a bit more urgency than a typical internal duplication annoyance. BPRF is our customer-facing domain tied directly to brand LSP certifications with Marriott, Hilton, Hyatt, and others — so external-facing consistency on this address isn't just a convenience issue for us, it has real weight with our brand partners. In fact, our Marriott brand contact has already reached out to Par, our Marriott brand manager, asking about the email inconsistency — so this is already visible outside our walls, not just an internal workflow hiccup.

Not trying to jump the line ahead of others dealing with the same issue — just wanted to flag why BPRF may need to be prioritized a bit differently given the external/brand-certification exposure. Happy to provide more detail if it helps build the case with IT.

Thanks again for keeping this on their radar.

Scott

### SCOTT (2026-08-21T19:48)
no optin for with specific words in the message header

### CLAUDE (2026-08-21T19:48)
Right — that granular header-search option is a classic desktop Outlook feature and typically isn't exposed in OWA's rule builder. Here's the workaround using what OWA actually offers:

**1. Combine "Sent to" and "Cc" conditions in one rule**
OWA's rule wizard lets you add multiple conditions with OR logic. Build the rule as:
- "Sent to" includes blueprintrf.com **OR**
- "Cc" includes blueprintrf.com

That covers the Hilton example, since your BPRF address was on the To/Cc line even though it was a distro, not you personally.

**2. For distro lists like "BPRF - Hilton Directives," add the distro address itself as a condition**
Same OR-condition approach — add the actual distro email address as another "Sent to" or "Cc" match. This is really just an extension of the "add known BPRF distros" patch-list approach from before, just now doing double duty since the header option isn't there.

**3. Best substitute for header-matching: search message body content instead**
OWA's rule builder has a condition like **"includes these words in the subject or body."** Since every forwarded message you've shown me has the original headers reproduced as visible text in the body (the "From: / To: / Cc:" block), a body-text search for `blueprintrf.com` will actually catch nearly everything the header search would have — because the header info isn't hidden, it's just quoted as plain text in the message.

**Recommended build:** Combine #1 and #3 together — Sent-to/Cc OR body contains "blueprintrf.com" — since between them you're catching both direct addressing and forwarded-header text, which is functionally very close to what the header-search option would've done on desktop.

### SCOTT (2026-08-21T19:49)
i a in cloiassice outlook, not owa

### CLAUDE (2026-08-21T19:49)
Good — that actually changes things, because classic desktop Outlook *does* have "with specific words in the message header" — it's just buried differently than expected. Here's exactly where to find it:

**File > Manage Rules & Alerts** (or Home tab > Rules > Manage Rules & Alerts) > **New Rule** > choose **"Apply rule on messages I receive"** (start from a blank rule, don't pick a template) > **Next**

On the conditions list, scroll down — it's not near the top with "from," "sent to," etc. Look for:

**"with specific words in the message header"**

Click the underlined **"specific words"** link in the description box at the bottom, type `blueprintrf.com`, click Add, then OK.

**If you genuinely don't see that condition at all** — a few things can cause that:
- You're on a **Microsoft 365 shared/hosted mailbox** or the rule is being built as a **server-side rule** (some conditions are client-only and get grayed out or hidden when Outlook detects the rule will run server-side instead of client-side) — header-matching is sometimes one of the conditions that gets dropped in that scenario.
- Which account are you building the rule on — BPRF or Spectrum? Try switching and building it from the other account's context if it's missing on one.

If it's truly not available regardless, fall back to the same combination I gave for OWA — "sent to/cc contains blueprintrf.com" OR "body contains blueprintrf.com" — since classic Outlook has both of those as standard, always-available conditions, and together they'll functionally cover the same ground the header search would have.

### SCOTT (2026-08-21T21:48)
ok.  what abut my calendar?  any workarounds there?

### CLAUDE (2026-08-21T21:49)
Yes — and this one has a cleaner fix than email, because the root cause is different: meeting invites are likely **auto-processing into your calendar** in Spectrum the moment they arrive, rather than needing you to open/accept them. You can turn that off specifically on the Spectrum profile.

**1. Stop auto-adding invites to the Spectrum calendar**
File > Options > **Mail** > scroll to **Tracking** section > uncheck **"Automatically process meeting requests and responses to meeting requests and polls."**

This has to be set per-profile, so do this while working in the **Spectrum** profile specifically (leave it on for BPRF, since that's your real, primary calendar). Once unchecked, forwarded meeting invites will just sit as regular email in Spectrum — they won't silently create a calendar entry anymore. You can flat-out ignore them the same way you're now ignoring forwarded mail.

**2. Clean up what's already duplicated (one-time)**
For the backlog already on the Spectrum calendar:
- Switch Calendar view to **List** (View tab > Change View > List) — much faster to review/delete in bulk than the grid view.
- Sort by **Organizer** or **Subject** to group duplicates together.
- For recurring series (your daily standups, RFP calls, etc.), delete the **recurring master**, not each instance — one delete clears the whole series.
- Since Spectrum isn't your canonical calendar going forward, you don't need to be careful here — bulk-delete freely.

**3. Ongoing habit**
Since BPRF stays primary, treat Spectrum's calendar as disposable from here forward — you're not maintaining it, just occasionally glancing at forwarded invite emails if something looks corporate/relevant. No need to keep it clean day-to-day once #1 is set; it just won't grow anymore.

This is a smaller fix than the email situation since you're not fighting an org-level policy — it's a client setting fully within your control.

### SCOTT (2026-08-24T13:40)
write me a brief summary of this isse and te step by step instructins we foowed to address for now.  i want to send to my team so that they can apply fixes to if thaey want.  stte that Spetrum IT is workign to migrate our domain and what the hiofule end resutl will be (i.e. brpf as primaty, spectum as alis)

### CLAUDE (2026-08-24T13:40)
**Subject: Duplicate Email & Calendar Issue — Interim Fixes (BPRF/Spectrum)**

Team,

As part of the merger, many of us now have both a BPRF and a Spectrum mailbox, with BPRF mail currently set to auto-forward into Spectrum. IT confirmed this is intentional and temporary — they're still working licensing/timing for a full mailbox migration, and this isn't unique to BPRF; several teams are seeing the same thing.

**End goal (per IT):** Once the domain migration completes, BPRF will become your primary mailbox and identity, with Spectrum set up as an alias only — one unified inbox, no more duplication. Until then, we're stuck living across two mailboxes.

In the meantime, here's what I've set up to make it manageable. Feel free to apply the same on your end if you're seeing similar issues.

**Email — reduce duplicate review**

1. In your **Spectrum** mailbox, create a rule to catch forwarded BPRF mail: condition = "Sent to" or "Cc" contains blueprintrf.com, OR "body contains" blueprintrf.com (catches forwarded messages where BPRF only shows up in a distro, not directly to you).
2. Action: **move to a folder** (e.g., "BPRF – Forwarded Copy") — don't auto-delete. Some of this mail carries retention/compliance tags, so we want a parking spot, not deletion.
3. Continue working primarily from BPRF as your source of truth; only check the Spectrum folder if something's missing on the BPRF side.
4. As you spot BPRF distro lists that aren't getting caught by the rule, add them as additional conditions over time.

**Calendar — stop new duplicates, clean up old ones**

1. In your **Spectrum** profile: File > Options > Mail > Tracking section > uncheck "Automatically process meeting requests and responses to meeting requests and polls." This stops new invites from creating duplicate calendar entries. (Leave this checked on your BPRF profile — that stays your real calendar.)
2. For calendar duplicates already there: switch to List view, sort by Organizer, and delete the recurring master (not each instance) for repeating meetings — clears the whole series at once.
3. Going forward, treat the Spectrum calendar as disposable — no need to maintain it day-to-day once step 1 is set.

This is a workaround, not a fix — but it should cut down on reviewing everything twice while we wait on the migration. I'll update the team once IT confirms timing on the real solution.

Scott
