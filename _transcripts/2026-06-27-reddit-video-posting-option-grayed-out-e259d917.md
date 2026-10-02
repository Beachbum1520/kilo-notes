# Reddit video posting option grayed out
Date: 2026-06-27
Conversation: e259d917-0161-4a70-9e7d-7673be034596
Domain: skip

## Summary
**Conversation Overview**

The person asked why the video posting option was grayed out on Reddit. Claude explained that this is most commonly caused by subreddit-level settings, as individual communities can disable specific post types (video, images, links, etc.), which causes those options to appear grayed out rather than throwing an error. Claude walked through several other possible causes in order of likelihood: subreddit restrictions on video posts, account age or karma requirements set by certain communities, platform differences between the mobile app and desktop versions of Reddit, file size or length limitations, and account standing issues. Claude concluded by asking a diagnostic follow-up question — which subreddit the person was trying to post to, and whether they were using the app or website — to help narrow down whether the issue was account-side or community-specific. The conversation was brief and the troubleshooting exchange was not completed, as the person had not yet responded with additional details.

### SCOTT (2026-06-27T13:45)
How come Reddit won’t let me post videos. The option is grayed out for me.

### CLAUDE (2026-06-27T13:46)
The user is asking why they can't post videos on Reddit — the posting option is grayed out. This is a question about current Reddit functionality that could have changed, so I'm considering whether to search for the latest information. There are several established reasons why video posting might be disabled, though I should verify what Reddit's current policies are to give them accurate help.

I'll try a different search approach with adjusted keywords.

The search results aren't helping much, so I'll draw on what I know about this—the underlying causes tend to be consistent. The most likely culprit by far is that video posts are disabled in that subreddit's community settings.Most likely it's the subreddit itself, not your account. Reddit lets each community decide which post types are allowed, and a lot of subs turn off video (and sometimes images) entirely. When a sub disables a post type, that tab/option shows up grayed out — so it'll look broken even though it's working as intended.

A few things to check, roughly in order of likelihood:

1. **The subreddit blocks video.** Try posting the same video to a sub you know allows it (like r/test). If it works there, the original sub just doesn't permit video. This is the most common cause by far.

2. **Account age/karma gates.** Some subs require a minimum account age or karma before you can post video/links. Newer or low-karma accounts hit this a lot.

3. **Where you're posting from.** The mobile app, old.reddit, and new desktop reddit don't all expose the same upload options. If it's grayed out on the website, try the official app, or vice versa.

4. **File limits.** Reddit caps video length (around 15 min) and file size (~1GB). An oversized or unsupported file can disable the option rather than throw a clear error.

5. **Account standing.** If your account is shadowbanned or under a restriction, certain post types get limited.

Quick diagnostic: which sub are you trying to post to, and are you on the app or the website? That'll narrow it down fast — if it's grayed out everywhere across multiple subs, it's account-side; if it's just one sub, it's that community's rules.
