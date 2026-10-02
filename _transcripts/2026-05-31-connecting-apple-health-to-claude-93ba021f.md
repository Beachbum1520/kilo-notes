# Connecting Apple Health to Claude
Date: 2026-05-31
Conversation: 93ba021f-8d92-4b80-a017-77dfe2fc3b22
Domain: skip

## Summary
**Conversation Overview**

The person asked how to connect Apple Health to Claude. Claude searched Anthropic's support documentation and retrieved the official help article on using Claude with iOS apps to provide accurate, current information.

Claude explained that the Apple Health integration is not a settings toggle but is triggered contextually: the person asks a health-related question in the Claude iOS app, and Claude prompts for iOS Health permissions at that moment. Claude outlined the prerequisites (latest iOS app version, Pro or Max subscription, US account region, beta feature access) and the step-by-step flow, including how to manage or revoke permissions later via iPhone Settings. Claude also noted that the integration is read-only, covers broad data categories relevant to fitness tracking (activity, workouts, vitals, sleep, nutrition), and flagged that health data pulled in a conversation is unlikely to persist into project memory structures due to how the memory feature handles such data.

### SCOTT (2026-05-31T03:05)
How do I connect Apple health to Claude.

### CLAUDE (2026-05-31T03:05)
 The user is asking about Apple Health integration with Claude, which is a product feature question. I need to search Anthropic's documentation to get accurate information rather than speculating based on my tool capabilities.

I'll check support.claude.com and docs.claude.com for details on how to connect Apple Health.Let me check Anthropic's current documentation for this, since app features change.

 I'm looking up the official support documentation to provide accurate step-by-step instructions.Let me pull the exact steps from Anthropic's help article.

 Now I understand how this actually works — it's not a traditional connector setup. When Scott asks a health question, Claude will prompt for permission right there in the conversation rather than requiring him to dig through settings. He'll need a Pro or Max subscription, be in the US, have the beta feature enabled, and keep his iOS app current. Given his focus on endurance training and HRV metrics, this integration could be really useful for his marathon preparation, so I'll walk him through the straightforward steps.The Apple Health connection isn't a connector you flip on in a menu — it's triggered contextually. You just ask Claude a health question in the iOS app, and it requests permission on the spot.

The actual steps:

1. Make sure you're on the latest version of the Claude iOS app, and signed in on a **Pro or Max plan** (required), with your account region set to the **US**. The health feature is in beta on Pro and Max only and currently limited to US users.
2. Ask a health question — e.g. "How have my runs been trending this month?" or "Show me my HRV over the past three months."
3. Claude will throw up the standard iOS Health permission screen. You choose exactly which data types to share, then approve.
4. From then on Claude can read that data and chart it inline.

To manage or revoke later: **Settings > Health > Data Access & Devices > Claude** on your iPhone.

A couple of things worth flagging given how you'd actually use this:

It's **read-only**. Claude can read health data but cannot write or modify entries in Apple Health. So it won't replace your TrainingPeaks/Athletica workflow for logging — it's for analysis, not entry.

The data categories it can pull are broad and relevant to your training: activity metrics, workouts (type, duration, distance, heart rate, calories), vitals including resting heart rate and HRV, body measurements, sleep stages and efficiency, and nutrition.

One caveat on your memory setup: the memory feature is designed to prevent Claude from using sensitive health information in future conversations — meaning health data pulled in one chat won't necessarily persist or carry across into your project structure the way your other context does. If you're expecting it to feed your Fitness & Training project memory, it likely won't.

If you're not seeing the permission prompt, the usual culprit is an outdated app version or a non-US/non-Pro account.
