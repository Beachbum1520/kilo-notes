Given (a) you've marked it private, (b) no one has delegate access, and (c) Jady is your boss but not your delegate, the practical exposure is **minimal**. Jady would have to specifically go looking at your calendar for that day, notice a private block, and think it's worth asking about. And even if he did ask, "personal appointment" is a completely normal answer.

The reason to check the permissions tab isn't because you expect a problem — it's because you'll sleep better knowing exactly what he can and can't see. Two minutes of your time for full clarity. Worth it.

Want me to walk you through checking the permissions in more detail on a specific Outlook version, or is the above enough to go on?

### SCOTT (2026-07-29T22:28)
i right click on the calendar icon in left tool bar and there is no properites or sharing.  there is an option,  but nothing under there is about sharing

### CLAUDE (2026-07-29T22:29)
That's because in New Outlook (which is what Cox has probably rolled out) the sharing controls moved. Right-click on the calendar icon doesn't show them anymore. Here's how to find them in the current Outlook builds:

## Try these in order

### Method 1 — Right-click the calendar name (not the icon)

1. Click the **Calendar icon** on the left toolbar first to open the calendar view
2. In the left pane you'll see "My Calendars" with your calendar listed under it (probably "Calendar" or your name)
3. **Right-click the calendar name itself** (not the icon on the toolbar)
4. Look for **Sharing and permissions** or **Share**

### Method 2 — From the top ribbon

1. Open the calendar view
2. On the top ribbon, look for a **Share Calendar** button or a **Share** icon
3. Click it — this opens the same permissions dialog

### Method 3 — Settings

1. Click the **⚙️ gear icon** (top-right of Outlook)
2. Search for "**shared calendars**" or navigate to Calendar → Shared calendars
3. You'll see who your calendar is shared with

### Method 4 — Outlook Web (most reliable)

Since Cox uses Exchange/M365, you can always check via the web:

1. Go to **outlook.office.com** and sign in
2. Click the **Calendar icon** (bottom-left)
3. In the left pane, hover over your calendar name → click the **three dots** (⋯)
4. Select **Sharing and permissions**
5. You'll see the full list of who has access and their permission level

The web version is usually the most consistent for finding these settings.

## The easier answer, honestly

Given that:

- You've marked the meeting private
- No one has delegate access
- Jady is a manager, not a delegate

I'd be about 95% confident private items are hidden from him regardless of his access level. The permission that lets someone see private items is *specifically* "Delegate with private-item visibility enabled" — everything else hides private items by default, even for Reviewer or Editor level.

If checking is turning into a rabbit hole, here's the practical test that answers the question in 30 seconds:

**Ask a trusted peer** (not Jady, not anyone connected to this) to pull up your calendar for Thursday July 30 and tell you what they see for the 4-5 PM block. If they see "Private Appointment" or "Busy" with no details, you're set. If they see the actual subject or attendees, you know you have a visibility problem to fix.

That's real-world validation without hunting through settings.

## My honest recommendation

Given the low-actual-risk profile and that you're now spending time on this instead of prepping for the call: **stop checking, trust the private marking, and move on.** The exposure if you're wrong is "Jady sees a meeting with Lloyd's name" — which is defensible ("we're vendors, we talk"), and Jady is unlikely to be specifically watching your calendar for that time slot anyway.

The prep for tomorrow's call matters more than the last 5% of certainty on calendar permissions. Trust the private marking, mentally check "does the private label render as generic" if you happen to have Outlook Web open anyway, and put this down.

Want to move on to any last prep, or are you good to wrap for tonight?

### SCOTT (2026-07-29T22:30)
found it.  here is Jady and Naila who is his ea
[File uploaded: 1785364190681_image.png]

### CLAUDE (2026-07-29T22:30)
Perfect — this gives you a definitive answer.

## What Jady and Naila can see

**Jady West: "Can view titles and locations"**
**Naila Martinez (his EA): "Can view all details"**

Now, the critical question: **do these levels expose private items?**

The answer is *almost certainly no* — but with one important nuance about Naila's access I want to flag.

### For Jady (Can view titles and locations)

At this permission level, private items are **hidden by default**. Jady sees:
- The time block exists (busy from 4-5 PM)
- The label reads "Private Appointment" (not the actual subject)
- No location, no attendees, no meeting body, no Teams link

He *cannot* see that it's with Lloyd or that it's a Cloudstaff meeting. You're good.

### For Naila (Can view all details) — worth thinking about

"Can view all details" gives her more visibility than Jady. On this permission level, private items are still hidden by default — but "all details" access is one step below Delegate, and some Cox configurations may render private items differently to full-details viewers. Almost certainly she still sees "Private Appointment" and no content, but I can't guarantee it 100% without testing.

**The practical question about Naila:** does she actually look at your calendar? EAs often do — scheduling on behalf of Jady, checking your availability for meetings he wants to set. If she does look at your Thursday, she'd see a private block from 4-5 PM. She probably wouldn't ask about it (EAs are used to seeing exec calendars with private blocks), but she'd notice one exists.

## The other two names worth noting

- **Bayat, Par (CCI-Blueprint RF) — "Can view all details"** — same level as Naila. Presumably your peer or someone from your team.
- **Mencos, Johanna (CEI-Atlanta-CON)** and the other CEI-Atlanta names — "titles and locations" access. Consultants or contractors probably.

None of these should see private items either, on the same reasoning.

## The one-question test that gives you certainty

If you want to *know* rather than *reason* about it, do this right now — it takes 60 seconds:

1. Create a fake private test event on your calendar for some random time (like Friday 11 PM)
2. Give it a distinctive subject like "TEST — Confidential Sensitive Meeting"
3. Mark it private
4. Save it
5. Ask Naila (or Par, or anyone with all-details access) in Teams: "Quick sanity check — can you pull up my calendar for Friday 11 PM and tell me what you see?"
6. If they say "Private Appointment" or "Busy" — you're 100% confirmed
7. If they say "TEST — Confidential Sensitive Meeting" — you have a real problem

Delete the test event afterward. Done in 2 minutes.

That's the only way to be *certain*. Otherwise you're relying on Microsoft's default behavior, which is very likely correct but not guaranteed at Cox's specific configuration.

## My honest read

If I had to bet: **you're safe.** Jady sees nothing meaningful, Naila sees at most "Private Appointment," neither of them is going to interrogate a senior director's private calendar block from 4-5 PM on a Thursday. Even in the worst case where Naila somehow sees the subject line, the story is easily defensible — Cloudstaff is a current vendor you spend $60K/month with, of course you have meetings with their CEO.

The exposure is genuinely small. The prep for tomorrow matters more.

## Wrap for tonight?

You've done real work today. The doc is built, the invite is set, Jady's 1:1 is moved, the private marking is in place, and you now understand exactly what different people can see on your calendar. That's a good day of prep.

Suggest closing the laptop, having dinner, and coming back to it tomorrow morning fresh if you want to do a final read-through of the prep doc. Or just let it ride and trust the work — either is fine.

Want to do anything else before you wrap for the night?

### SCOTT (2026-07-29T22:32)
par works for me.  Naila, see all details when scheduling calls on Jady's behalf; she needs to see details so she can know what can be moved, re-prioritized, etc.

### CLAUDE (2026-07-29T22:32)
That makes sense — and reinforces that your permission setup is intentional, not accidental.

Naila needing "all details" for scheduling logistics is exactly right for an EA. She needs to see what's rearrangeable and what isn't when Jady wants a meeting. The private-marking system exists precisely for the situations where an EA has legitimate all-details access but the content itself is sensitive — you get to keep her functional access while hiding the specific content when needed.

For Thursday 4-5 PM: she'll see the block, know you're not moveable, and that's all she needs. Perfectly clean.

Par is fine — direct report, you'd expect him to have that visibility.

You're in good shape on the calendar side. Nothing more to do there.

## Where you actually are

- Prep doc built and printable
- Invite marked private
- Jady moved to Friday
- Calendar permissions reviewed and understood
- No conflicts, no exposure concerns
- ~46 hours of runway until the call

That's a genuinely well-prepared position. Better than most people manage for a call of this importance.

## What I'd suggest for the rest of your night

Close the laptop. Have dinner. Do something that isn't this. The best thing you can do for tomorrow's call now is *not think about it for a while*. Your prep is done. Marinating on it more tonight won't add much and might actually make you tighter than you want to be.

Tomorrow (Wednesday):
- Morning: light re-read of the doc, maybe 15-20 minutes, mostly to refresh the shape
- Then be fully present at the all-hands recognition event — that's your team's day
- After the event: eat something, decompress
- Thursday afternoon before the call: final skim, then walk in

Thursday at 4 PM Atlanta: you're going to do great. You've done the work. You know the material. Lloyd already respects you. The relationship is real. You're not walking in cold.

Come find me after the call. I want to hear how it went.

### SCOTT (2026-07-29T22:33)
corrdct the date and times on the doc and recreate so i can print out.

### CLAUDE (2026-07-29T22:33)

```
This block i