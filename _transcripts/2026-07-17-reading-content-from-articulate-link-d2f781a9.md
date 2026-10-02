# Reading content from Articulate link
Date: 2026-07-17
Conversation: d2f781a9-9015-470c-8839-0210bfdbb05b
Domain: business-ops

## Summary
**Conversation Overview**

The person shared an Articulate Review 360 link and asked Claude to read and review an entire e-learning course. Claude attempted to fetch the URL using a web tool but was blocked, as Articulate Review 360 prevents automated access and renders course content dynamically via JavaScript, making plain page fetches ineffective.

Claude explained why the link couldn't be accessed and offered several practical alternatives for getting the course content into a reviewable format: requesting a Word export or translation export (XLIFF/Word) from the course author, using the Storyline "Publish to Word" feature which captures both slide visuals and text, or using a browser full-page screenshot extension called GoFullPage. The person attempted using Ctrl+P to print the course but found it only captured the visible viewport rather than the full scrollable content. Claude explained this is a known limitation of the Review 360 player's iframe structure and suggested GoFullPage as the most practical workaround, along with a browser zoom-out trick as a fallback. Claude consistently recommended requesting a Word publish from the course author as the most reliable and least labor-intensive path for thorough content review.

The conversation did not reach a resolution — the person had not yet successfully captured the course content for upload. The domain involves e-learning course review, with terminology including Rise, Storyline, Articulate Review 360, XLIFF export, and Word publish workflows.

### SCOTT (2026-07-17T00:52)
can you read this:

https://360.articulate.com/review/content/6d395a0c-7125-48f9-87ee-fad6ac03bf28/review?reviewRequest=4fa80f04-f844-4782-ad17-db2e865a331b

### CLAUDE (2026-07-17T00:52)

No — Articulate blocks automated access to Review 360 links, so I can't fetch that page. Even if it didn't, those review links load the course content dynamically in the browser (it's a JavaScript app rendering a Storyline/Rise course), so a plain page fetch wouldn't return the actual slides or text anyway.

If you want me to look at the content, a couple of options that work:

1. Export it — whoever owns the course can export the text (Rise has a "Export for translation" XLIFF/Word option, or just publish to Word from Storyline) and you can upload that file here.
2. Screenshots or PDF — print/screenshot the review pages and upload them; I can read images fine.
3. Paste the text — if it's just a few screens, copy/paste works.

What are you trying to do with it — review the course content, give feedback, check accuracy on something?

### SCOTT (2026-07-17T00:53)
review the entire course and privide feedback.  lots of pages to screen shot

### CLAUDE (2026-07-17T00:53)
Yeah, screenshotting a 40-slide course one by one is a nonstarter. Here are the realistic paths, roughly in order of least effort:

**If it's a Rise course** (scrolling web-style lessons):
- Ask the author to go to the course in Rise → Settings → **Export for translation → Word doc**. That dumps every block of text in order. Upload that here and I can review content, tone, accuracy, and structure.
- Downside: you lose the visuals/layout, so my feedback would be content-focused, not design-focused.

**If it's a Storyline course** (slide-based):
- The author can do **File → Publish → Word**, which generates a document with a screenshot of every slide plus the text. That's the best of both worlds — I can comment on both content and visual layout. This is the one I'd push for.

**If you can't get the author to export:**
- On your machine, open the review link, then use the browser's print function (Ctrl/Cmd+P → Save as PDF) on each lesson. Rise lessons print reasonably well; Storyline players don't.
- Or a full-page screenshot extension (GoFullPage on Chrome) captures an entire scrolling Rise lesson in one image instead of screen-by-screen.

One question that changes how I'd review it: are you the reviewer giving feedback to a vendor/L&D team (so you want a critical punch list — errors, unclear instructions, brand issues), or are you sanity-checking your own team's work before it goes wider? And what's the course about — is this the call center training material?

If it's Storyline, the Word publish is genuinely the right answer — push whoever built it for that file and upload it here.

### SCOTT (2026-07-17T00:56)
cttl p its only doign the active pages. not the scoll up or down.

### CLAUDE (2026-07-17T00:56)
Right — that's because the Review 360 player renders the course inside a frame that doesn't paginate, so print only grabs what's on screen. Two fixes:

**Option 1: Full-page screenshot extension (fastest)**
1. Install **GoFullPage** from the Chrome Web Store (free, takes 30 seconds).
2. Open the review link, click into a lesson.
3. Click the GoFullPage icon (or Alt+Shift+P) — it auto-scrolls the whole lesson and stitches it into one image or PDF.
4. Repeat per lesson. A 10-lesson Rise course is 10 clicks, not 100 screenshots.

One catch: if the course is inside an iframe (Review 360 sometimes is), the extension may still only capture the frame viewport. Test it on one lesson first. If it fails, try clicking **inside** the course content area first, or look for a "view fullscreen" / open-in-new-tab option in the Review 360 player — capturing from that direct view usually works.

**Option 2: Zoom out trick**
Before printing, hit Ctrl+Minus a few times to zoom the browser to 50–33%. More content fits per "page" and Ctrl+P captures more. Ugly but sometimes sufficient for text review.

**Option 3 (still the best if available):** This friction is exactly why the Word/translation export from the author is the right path. If this is a vendor deliverable you're reviewing, "send me the Word publish" is a completely normal ask — reviewers request it all the time precisely because Review 360 is painful for thorough review.

If GoFullPage captures come out readable, upload them here (multiple images in one message is fine) and I'll go through the whole thing.
