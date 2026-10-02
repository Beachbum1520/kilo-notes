# Adding others to Zendesk tickets without CC
Date: 2026-08-20
Conversation: d113bbe6-4c1b-4a7d-b681-8c094bab57c7
Domain: skip

## Summary
**Conversation Overview**

The person sought practical IT and productivity help across two unrelated topics. First, they asked about changes to Zendesk's updated UI, specifically how to add others to a ticket for ongoing updates since the CC field appeared to have moved or disappeared. Claude explained that CC functionality still exists but is now accessed through the reply composer rather than a standalone field at the top of the ticket, and also outlined the Followers option for internal-only visibility. The person followed up to confirm whether adding a CC persists for all future ticket updates, and Claude confirmed that CCs remain on the ticket for its full lifecycle, receiving notifications on all subsequent public updates, with a noted cap of 48 CCs per ticket.

Second, the person asked how to prevent attendees from forwarding an Outlook meeting invite. Claude walked through the "Allow Forwarding" toggle under Response Options, available in both New Outlook/Outlook Web and Classic Outlook for Windows. Claude noted this setting must be manually toggled each time a meeting is created (no default-off option exists), that existing meetings require a resent update for the change to take effect, and that the restriction has limitations with older Exchange environments, third-party calendar clients, and Mac Outlook in some versions.

The person's questions were brief and typed with informal spelling, suggesting they prefer concise, direct answers over lengthy explanations.

### SCOTT (2026-08-20T11:59)
new zendesk ui does not allow cc:' anymore.  how do i ad otehrs to the ticket for udates so that they wul leav ee alone

### CLAUDE (2026-08-20T12:00)

CC didn't disappear — it moved. In the new Zendesk ticket UI, it's not a persistent field anymore; it's tucked into the reply composer.

**To add someone who should get updates and be able to reply:**
Use **CC**, now accessed via the **"CC" button/link in the corner of the reply box** (next to where you write your public reply), rather than a separate field at the top of the ticket. CCs are now added by selecting "CC" in the right corner of your message / reply box.

**To add someone internal who just needs visibility without appearing in the thread:**
Use **Followers** instead — internal users can add followers from the Followers field from the properties panel in the ticket interface, and followers receive email notifications when a ticket is updated. That field is on the left-hand side of the ticket, under "Followers."

Key distinction for your "leave me alone" goal:
- **CC** = external/internal people who can see and reply publicly, and their email is visible to others in the thread.
- **Follower** = internal-only, silent — followers remain hidden from CC'd end users and other followers on email notifications; their name and email address do not appear in email notifications sent to other users. But agents added as followers are able to see all ticket details, even if you are in a private group — so if you want someone updated but *not* granted full access, CC is actually the more restrictive option, not followers.

If you genuinely can't find the CC button anywhere in your instance (not even in the reply box), that's likely because your Zendesk account hasn't been migrated to the updated CC/follower model yet — accounts that haven't migrated to the new experience by October 28, 2026 will be migrated automatically on that date, so it's possible your org is mid-transition and things look unfamiliar. Worth asking your Zendesk admin to check Admin Center → Objects and rules → Tickets → Settings → CCs.

### SCOTT (2026-08-20T12:03)
and does the cc add thrm to all future updates otn eh ticket

### CLAUDE (2026-08-20T12:03)
Yes — once someone is added as a CC, they stay on the ticket and get notified of all future updates, not just the reply where you added them. CCs allow you to include end users and agents on ticket notifications, and that's ongoing for the life of the ticket unless someone removes them.

A few specifics worth knowing:

- They don't need to be re-added each time — they're now part of the ticket's CC list, so every subsequent public update (agent replies, end-user replies) triggers a notification to them.
- CCs can respond to ticket notifications publicly, or they can remove the requester from the notification to submit a private response — so once CC'd, they can also jump into the conversation themselves, not just watch it.
- Anyone already on the thread can remove a CC later — internal and external users can add CCs (copied users) to tickets, and per Zendesk's docs, CCs (or agents) can also remove themselves or others from that list if they no longer need to be updated.
- Cap to be aware of: a ticket can have up to 48 email CCs.

So it's a "set and forget" way to keep someone in the loop — exactly what you want if the goal is updates without you having to manually loop them in on every reply.

### SCOTT (2026-08-20T12:17)
restrict outlook inviute from forward

### CLAUDE (2026-08-20T12:18)

Turn off "Allow Forwarding" when you create/edit the meeting. As organizer, you can still add attendees yourself — this just blocks *them* from forwarding it further.

**New Outlook / Outlook Web:**
1. Open the meeting on your calendar (or create a new one).
2. Click **Response Options**.
3. Uncheck/toggle off **Allow Forwarding**.
4. Send (or Send Update if it's an existing meeting).

**Classic Outlook for Windows:**
1. Open the meeting → **Meeting** tab.
2. Click **Response Options** → toggle off **Allow Forwarding**.

Things to know:
- The option is turned on by default, and there's no way to make it off by default — you have to toggle it every time you create a meeting.
- If it's an existing meeting, you need to resend the update for the restriction to take effect — if you do this for a meeting you've already set up, you need to remember to send out an update to the invitation.
- It's not bulletproof: Outlook can't prevent forwarding if an attendee's mailbox is hosted on an older/on-prem Exchange or a third-party service like Google Calendar, and it won't stop someone forwarding the meeting as an iCalendar attachment. If your attendee gets it on an older client, they'll still see a forward option, but the server blocks the action and notifies them it was blocked.
- Mac Outlook client has historically lacked this control in some versions — if an attendee is on Mac desktop Outlook, results may vary. Worth testing with one internal recipient first if this matters for something sensitive (e.g., a meeting link you don't want spreading).
