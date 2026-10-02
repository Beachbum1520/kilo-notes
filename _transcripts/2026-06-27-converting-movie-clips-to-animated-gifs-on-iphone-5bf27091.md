# Converting movie clips to animated GIFs on iPhone
Date: 2026-06-27
Conversation: 5bf27091-b6bb-4f0e-ab27-e3d94a64e1bc
Domain: skip

## Summary
**Conversation Overview**

The person sought help converting a video clip into an animated GIF on an iPhone 17. The conversation involved an extended troubleshooting process across multiple approaches. Claude initially recommended using a "Convert Video to GIF" action in the Shortcuts app, which the person correctly identified as non-existent — the actual action is called "Make GIF." Claude then walked through building a custom shortcut using Make GIF, but the person reported it produced no output, which was diagnosed as a missing Save/Quick Look action at the end of the shortcut chain. After adding that step, the output was a static image rather than an animated GIF, which Claude attributed to possible Live Photo confusion or incorrect media type selection. The person confirmed they were selecting an actual video, prompting Claude to use web search to investigate further.

Research revealed that the Make GIF action is designed for photos and Live Photos rather than true video files, and that the Shortcuts Gallery contains a dedicated "Video to GIF" shortcut better suited to the task. The person tried that Gallery shortcut but encountered a "The input was not a video that can be edited" error at the Trim step, followed by a "No Items" error in Quick Look — both symptomatic of the same upstream failure where the Trim action could not process the source clip. Claude suggested re-encoding the clip via Photos Edit → trim handles → Save Video as New Clip to produce a clean, editable file, but the person's follow-up screenshot indicated the problem persisted.

By the end of the conversation, Claude had not successfully resolved the issue through Shortcuts and presented two clear paths forward: fixing the source clip to pass the Trim step, or abandoning Shortcuts entirely in favor of a third-party app such as GIPHY, which Claude noted would be the more practical choice given the repeated failures. The person corrected Claude's initial action name error and pushed back on several incorrect diagnoses throughout, indicating they want accurate, verified guidance rather than iterative guesses. Claude acknowledged missteps explicitly and used web search when uncertain, though search results were not fully conclusive. Future interactions should note that this person is working on iPhone 17 with the current iOS version, and that the Shortcuts video-to-GIF pipeline has proven unreliable for their specific video source — a third-party app is the recommended path if the topic arises again.

### SCOTT (2026-06-27T20:22)
How to make a movie clip into an animated gif iPhone 17

### CLAUDE (2026-06-27T20:22)
There are a few ways to do this on your iPhone 17, depending on what you have installed.

**Using the Shortcuts app (built-in, free)**
1. Open the Shortcuts app and tap the **+** to create a new shortcut.
2. Add the action **Convert Video to GIF** (search for it in the action list).
3. Add a **Get Photos** or **Select Photos** action before it so you can pick your clip.
4. Run the shortcut, choose your video clip, and it'll save the GIF to your Photos.

There are also pre-made "Video to GIF" shortcuts in the Shortcuts Gallery if you'd rather not build one.

**Trim the clip first (recommended)**
GIFs balloon in size fast, so trim your video to just the few seconds you want before converting. Open the clip in Photos, tap **Edit**, drag the timeline handles, and save.

**Using a third-party app**
Apps like GIPHY, ImgPlay, or GIF Maker give you more control over frame rate, looping, speed, and cropping. Good if you want finer tuning than the Shortcuts route offers.

**Quick tip:** Keep it under ~5–6 seconds and consider lowering resolution if you're sharing it somewhere with file-size limits — GIFs are far heavier than the original video.

Want me to walk you through building the Shortcut step by step, or are you leaning toward an app?

### SCOTT (2026-06-27T20:27)
There is no convert video to gif in shortcuts. Only a convert image to gif

### CLAUDE (2026-06-27T20:27)
The user is pointing out that iOS Shortcuts doesn't have a "Convert Video to GIF" action—it's actually called "Make GIF," which accepts video as input and converts it to an animated GIF.You're right — I gave you the wrong action name. The action you want is **Make GIF** (not "Convert Video to GIF"). It accepts a video clip as input and turns it into a GIF.

Here's the corrected build:
1. New shortcut → **+**
2. Add **Select Photos** (or **Get Latest Videos**) so you can pick the clip
3. Add **Make GIF** — it takes the video from the step above
4. Add **Save to Photo Album** to save the result

Tap **Make GIF** in the action to expand its options — you can set the **seconds per photo / frame rate** and toggle whether it auto-sizes. Run it, pick your clip, and the GIF lands in Photos.

The simplest path, though: search the **Shortcuts Gallery** (bottom tab) for "GIF" — there's a ready-made *Convert Video to GIF* shortcut you can add with one tap and skip the building entirely.

One catch with **Make GIF**: it can choke on long clips, so trim to a few seconds first if it errors out or the file comes out huge.

### SCOTT (2026-06-27T20:36)
Not doing anything.
[File uploaded: 22443e1e0bd3a1a4faf5f2838bd85701c911d0e0.png]

### CLAUDE (2026-06-27T20:36)
Looking at the shortcut setup, I can see the issue: "Select Multiple" is turned off in the Select Photos action, which means it's only picking a single photo, but the Make GIF action needs multiple images to create an animation. That's why nothing's happening—the GIF maker has no sequence to work with. The real issue is that the shortcut creates the GIF but never saves or displays it — there's no final action to do anything with the output. Adding either a Quick Look action to preview it or a Save to Photo Album action to store it would fix the problem.Your shortcut is missing the last step — it makes the GIF but never saves or shows it, so it looks like nothing happened.

Add one more action after **Make GIF**:
- **Quick Look** — instantly previews the GIF so you can see it worked, or
- **Save to Photo Album** — drops the finished GIF into your Photos

Search "Quick Look" or "Save to Photo Album" in the Search Actions bar at the bottom and tap to add it. It'll attach below Make GIF automatically.

Two other things in your setup worth a glance:
- **Seconds Per Photo is 0.2** — when feeding a video, this controls playback speed of the extracted frames. 0.2 is fine to start, but if the GIF looks choppy or too slow, lower it (try 0.05–0.1).
- Make sure you're actually picking a **video** when it prompts, not a still photo — a single photo produces a one-frame GIF with nothing to animate.

Run it again with Quick Look added and you'll see the result pop up immediately.

### SCOTT (2026-06-27T20:38)
It’s just saving an image. Not a gif.

### CLAUDE (2026-06-27T20:38)
The user has a Shortcuts workflow that selects photos and converts them to GIF, but when they pick a video, it's saving a still image instead of an animated GIF. The issue seems to be with how the "Make GIF" action is handling the video input—it should be extracting frames from the video and animating them, but something's going wrong in that process. The "All" filter does include videos, so that's not the issue. GIFs saved to the Photo Album might appear static in the grid view on older iOS versions since they don't autoplay there—you'd need to open them to see the animation. But the real culprit is probably that the user is selecting a single still photo instead of a video; feeding one photo to "Make GIF" produces a static single-frame GIF that looks like a regular image. Live Photos could also be the problem if they're being mistaken for videos.

I should clarify the diagnostic steps: confirm they're selecting an actual video file (not a Live Photo, which is the most common mistake), use the "Include" filter set to Videos only to prevent accidentally grabbing a still, and explain where the GIF gets saved and how to view it properly since grid thumbnails don't always show animation. The issue is almost certainly that they're selecting a Live Photo or still image instead of an actual video—with "Select Multiple" off, they're picking just one item, and if it's not a video, the GIF comes out as a single static frame. I should lead with that as the most likely culprit and keep this tight since they've been patient through several attempts.A static result from **Make GIF** almost always means the item you're picking isn't a true video. The usual culprit: it's a **Live Photo**, not a video. Live Photos look like videos in your library but Make GIF only grabs the single still frame from them — so you get a one-frame "GIF" that's effectively an image.

How to fix / confirm:

**Force the picker to videos only.** Tap **All** next to "Include" in your Select Photos action and change it to **Videos**. Now you can't accidentally grab a Live Photo or still — only actual video clips will show.

**Or convert a Live Photo properly.** If what you want to animate *is* a Live Photo:
- Open it in Photos → tap the **Live** badge (top-left) → choose **Loop** or **Bounce**. That creates an animated version right in Photos, no shortcut needed.

**Check what you're actually saving.** A real animated GIF lands in the **GIFs** album (Albums tab → Media Types → GIFs) and animates when you open it. Note that GIFs often show as a *still thumbnail* in the main library grid and only animate when tapped — so if you're judging by the thumbnail, it may actually be working.

My bet is the Include filter — set it to **Videos**, pick an actual clip, and it should animate. If you're still getting a single frame after that, tell me whether the source is a regular video or a Live Photo and we'll go from there.

### SCOTT (2026-06-27T20:39)
Nope. It’s definitely a video.

### CLAUDE (2026-06-27T20:40)
The user's Shortcut is selecting photos and then using "Make GIF from Photos," but it's producing a static image instead of an animated GIF. This is a known behavior issue with how the action handles the input from the photo selection step.

I should verify the current, accurate fix rather than guessing — whether it's about properly encoding the media, extracting frames first, or something else specific to the current iOS version the user is running.Let me look this up rather than keep guessing — I've already steered you wrong twice and this is specific current-software behavior worth getting right.

The search results aren't giving me the specific bug details, so I'm working from what the screenshot shows. The "Make GIF" action is receiving "Photos" as input from the select photos step, with 0.2 seconds per photo—which suggests it's treating the input as individual photos rather than a video, which is likely why it's producing a static image instead of an animated GIF. The saved file might actually be animated but just appears static, so I should verify with Quick Look first. Rather than keep troubleshooting the broken shortcut, the most practical solution is either using the Gallery's pre-built GIF shortcut or testing whether the issue is specific to iOS 26 on the iPhone 17.The older guides don't nail your exact symptom. Let me check whether this is a known issue on the current iOS version your iPhone 17 is running.

I'm seeing the distinction now. The Setapp documentation shows two separate shortcuts: "Make GIF" handles Live Photos and photo sequences with a "Seconds Per Photo" setting to control the frame rate, while "Video to GIF" is specifically for converting video files into GIF format.

The user's shortcut is using the wrong action—they're trying to use "Make GIF" on a video, which only captures a single frame instead of extracting multiple frames. The solution is straightforward: switch to the Gallery's dedicated "Video to GIF" shortcut, which is purpose-built for this exact task.Found the actual cause. The **Make GIF** action you built around is really designed for photos and Live Photos — that's why it has a "Seconds Per Photo" setting. There are two different tools: "Make GIF" and "Video to GIF" — one is for creating GIFs from live photos, and the other is for making GIFs from videos. When you hand a plain video to **Make GIF**, it can grab a single representative frame instead of extracting the motion, which is exactly your "it just saves an image" symptom.

Stop fighting your hand-built shortcut. Use the purpose-built one instead:

1. Open **Shortcuts** → **Gallery** tab (bottom right)
2. Search **"Video to GIF"**
3. Tap it → **Add Shortcut**
4. Run it from **My Shortcuts**, pick your clip, and if the video is too long you'll be prompted to trim it by dragging the chevrons on either end, then tap Save

That shortcut is built to pull frames out of a video, so it'll actually animate. You can then tap the Share button below the preview to save the image or share it.

One thing to know: a working GIF often shows as a **still thumbnail** in your Photos grid and only animates when you tap into it — so check it full-screen (or in the GIFs album) before assuming it failed.

If you'd rather not deal with Shortcuts at all, GIPHY (free) does video-to-GIF with a simpler interface and gives you trim/speed control.

### SCOTT (2026-06-27T20:43)
Close but no cigar
[File uploaded: 26794bc8ba9aaabd1824383363d68aa7689fb205.png]

### CLAUDE (2026-06-27T20:43)
So the actual error is that the Trim action can't process the video — it's not in an editable format. This matches the issue from that Apple Community thread where cropped videos specifically break the Trim step. The problem is either that the video was cropped in Photos, which makes it non-editable, or there's something else about the clip's format that prevents editing.

The solution is to re-export the video cleanly: open it in Photos, make a tiny trim edit, and save it as a new clip. This creates a fresh, standard video file that the shortcut can actually work with. If it's an iCloud-optimized file, I should also make sure the full resolution version is downloaded locally first.That error is the key — and it's failing at the **Trim** step, not the GIF conversion. "The input was not a video that can be edited" means Trim can't touch your source clip. This is a known iOS issue, and it has specific triggers.

The most common cause: the video was cropped in Photos. The original works fine, and even trimming and saving as a new clip works fine, but cropping makes it stop working. Cropping (changing the frame dimensions) makes the clip non-editable for Trim, while trimming (cutting length) doesn't.

Other likely culprits:
- **iCloud "Optimize Storage"** — the full-res video isn't downloaded to your phone, so the shortcut only gets a low-res placeholder it can't edit. Open the clip in Photos and let it fully download first.
- **Screen recording, slo-mo, or time-lapse** — non-standard formats Trim sometimes rejects.

**The fix that flattens almost any problem clip:**
1. Open the video in **Photos** → **Edit**
2. Drag the **trim handles** in just slightly (cut a fraction off either end — do *not* use the crop tool)
3. Tap **Done** → **Save Video as New Clip**
4. Run **Video to GIF** again and pick that new clip

That re-encodes it into a clean, standard, editable video and should clear the error.

If you specifically need the cropped framing, you'll have to crop *after* — but get it converting first with an uncropped clip so we know the pipeline works. Want to try the "Save as New Clip" step and report back?

### SCOTT (2026-06-27T20:46)

[File uploaded: 723f0f95b6e39b5f5a5934a58e26ff79e1f49d6a.png]

### CLAUDE (2026-06-27T20:46)
The root issue is that the Trim step in the Video to GIF Gallery shortcut is failing on the source video, which causes the entire pipeline to break down before Quick Look even receives anything to preview. This is the same underlying problem as the earlier "input was not a video that can be edited" error — the shortcut can't process the video at that stage, so nothing makes it through to the next steps.

At this point, they've tried multiple times and keep hitting the same wall. I should be direct: either fix the source video so Trim can handle it (likely using "Save as New Clip"), or abandon the Shortcuts approach entirely and use a dedicated video-to-GIF app instead. The repeated failures suggest it's time to stop fighting the Shortcuts pipeline and pick the most reliable path forward.Same underlying failure — this "No Items" error is just the tail end of it. The Trim step choked on your video (the previous error), you tapped OK, and the shortcut kept running with nothing in hand, so Quick Look at the end had nothing to show. The GIF was never made.

You've put real effort into the Shortcuts route and it keeps fighting you. Two honest paths:

**Path A — Fix the clip, then retry (if you want Shortcuts to work)**
The Trim step needs a clean, standard, fully-downloaded video. Do this first:
1. Photos → open the clip → **Edit**
2. Nudge the **trim handles** in slightly (don't crop) → **Done** → **Save Video as New Clip**
3. Make sure it's not still downloading from iCloud (no spinner/cloud icon)
4. Run **Video to GIF** on that *new* clip

If your original was cropped, slo-mo, a screen recording, or iCloud-optimized, this re-encode is what clears the error.

**Path B — Skip Shortcuts entirely (faster, more reliable)**
Download **GIPHY** from the App Store → tap **Create** → pick your video → trim → export to Photos. No Trim-action bug, no Quick Look failures, plus you get speed and crop control. Given how many rounds this has taken, this is what I'd actually do.

Want to clean up those four "New Shortcut" attempts cluttering your Library too, or leave them for now?
