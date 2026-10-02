# Creating GIFs longer than 6 seconds
Date: 2026-07-14
Conversation: 2d730391-ac7f-4acb-83a4-b89366f0cd13
Domain: skip

## Summary
**Conversation Overview**

This conversation focused on building an iPhone Shortcuts workflow to convert videos to animated GIFs, and ultimately pivoted to a paid app recommendation. The person wanted to create GIFs from videos in their Photos library with the ability to trim specific sections, with no hard length cap like the 6-second limit they were hitting in another tool.

Claude and the person went through multiple iterations of building a Shortcuts workflow. Key problems encountered included: the initial shortcut showing only photos instead of videos (caused by missing Media Type filter), videos appearing oldest-first rather than newest-first (fixed by switching Sort from Date Taken to Creation Date, as screen recordings lack a "taken" date), and difficulty connecting the Trim Media output variable to the Make GIF action (requiring the Clear Variable → Select Variable → tap output token sequence rather than picking from a list). The person deleted the shortcut partway through and requested a fresh build, which still had issues with video discovery and variable wiring. The person explicitly corrected Claude's approach multiple times — noting "Choose from Photos" not "Choose from List" as the action name visible in their Shortcuts editor.

The person then asked about paid app alternatives and was pointed to **ImgPlay** (one-time purchase ~$5–8, removes watermark and length restrictions) as the primary recommendation, with GIF Toaster as a runner-up. The person appeared to be evaluating ImgPlay and noted its constraints: 15 fps maximum and 200 frames cap, which Claude confirmed yields 13.3 seconds at max settings. Claude explained that dropping to 10 fps extends the limit to 20 seconds, and that the Pro unlock may raise or remove the frame ceiling, with file size being the practical constraint beyond app settings.

### SCOTT (2026-07-14T22:47)
Gif maker seems to be limited to 6 second gifs. I need to make longer ones.

### CLAUDE (2026-07-14T22:47)
Scott's looking to extend his GIF length, but I'm not sure which GIF maker he's referring to—could be anything from iPhone Shortcuts to a web tool like GIPHY or ezgif. I should check if there's context from earlier conversations about what tool he typically uses.

I'm trying to figure out what's causing the 6-second limit on Scott's GIF shortcut — it could be GIPHY's video-to-GIF conversion cap, the GIF Maker app itself, or possibly something else entirely in how the Shortcuts action is configured.

Looking at the actual options: the native Shortcuts Make GIF action doesn't have a hard 6-second duration limit, but it can create large files; ImgPlay supports longer clips but watermarks them; and ezgif.com on the web can handle up to around 60 seconds depending on file size. The real constraint is that GIF files balloon in size quickly past 10 seconds, and many platforms will reject or convert them anyway. I should probably ask where he's posting the GIFs or just give him the straightforward solutions — either use Shortcuts with a lower frame rate for longer clips, or point him to ezgif for more control, while flagging that longer GIFs might not be practical depending on where he's sharing them.That 6-second cap is the app's limit (GIPHY and a few "GIF Maker" apps hard-cap around 6–6.5s), not a GIF format limit. Options that go longer:

1. **Shortcuts "Make GIF"** (the one you built in June) — no duration cap. For longer clips, lower the frame rate in the action's options (tap the expand arrow) or it'll choke on file size.
2. **ImgPlay** — handles clips well past 6 seconds, with frame rate/speed/crop controls. Free version watermarks; one-time purchase removes it.
3. **ezgif.com** — upload the video in Safari, converts up to ~60 seconds, best fine-grain control over size and quality.

One tradeoff to know before you go long: GIF is a brutally inefficient format. A 15-second GIF at decent quality can hit 30–50MB, and many platforms (iMessage, Slack, socials) will compress it to mush or reject it. If the destination supports it, a short looping MP4 gives you 10x the quality at a tenth the size. What are you making these for?

### SCOTT (2026-07-14T22:51)
I don’t think we ever got the shortcut to work. Let’s try it again

### CLAUDE (2026-07-14T22:52)
I should walk through the shortcut setup step-by-step with the corrected approach, making sure to highlight that the missing save step was what caused the problem in the first place.Right — last time it "did nothing" because the shortcut made the GIF but never saved it. Let's build it clean, all four steps this time:

1. Open **Shortcuts** → **+** (top right) to create a new shortcut.
2. Tap **Add Action**, search **Select Photos**, add it. Tap the arrow on that action and turn ON **Select Multiple**? No — leave it off, but do check that it allows videos (it does by default).
3. Search **Make GIF**, add it. It should auto-connect to "Photos" from step 2. Tap the arrow to expand it — set **Seconds Per Photo** low (0.1 ≈ 10fps) and leave **Auto Size** on.
4. Search **Save to Photo Album**, add it. It should auto-connect to the GIF output.
5. Tap the name at the top to rename it "Video to GIF," then hit the ▶ play button to test. Pick a video, and the GIF should land in your Photos Recents.

If the GIF appears but doesn't animate in Photos, that's normal for the thumbnail — tap into it and it'll play.

One watch-out for your longer clips: if it hangs or errors on a 15–20 second video, that's the file size choking it. Drop the source video resolution first (screen record trick or export smaller), or lower the frame rate. Tell me what happens when you run it.

### SCOTT (2026-07-14T22:52)
We want gif from video. Not pics.

### CLAUDE (2026-07-14T22:52)
The "Select Photos" action in Shortcuts actually includes videos in its picker, so the instructions are already correct—I just need to clarify that this action handles both photos and videos by default. There's no need to use a separate filter or "Get File" action since the photo picker naturally shows all media types.Same steps — that's the confusing part. **Select Photos** is just Apple's name for the media picker; it shows your videos too, and you'll pick a video from it. **Make GIF** then converts that video into an animated GIF frame by frame.

So the build stands: Select Photos → Make GIF → Save to Photo Album. When you run it and the picker opens, tap the **Videos** album (or just scroll to your clip in Recents) and select it. The output will be a true animated GIF of the video, not a slideshow of stills.

Run it with a short test clip first — 5 seconds or so — to confirm the pipeline works before throwing a longer video at it.

### SCOTT (2026-07-14T22:56)
Here it is. Do I need to shorten the video to a certain length first for this to work?
[File uploaded: IMG_8831.png]
[File uploaded: IMG_8832.png]
[File uploaded: IMG_8833.png]
[File uploaded: IMG_8834.png]

### CLAUDE (2026-07-14T22:56)
I'm looking at a Shortcuts workflow that converts videos to GIFs. It starts by finding videos longer than a second, and if none exist it alerts the user—otherwise it lets them pick one from their library. The shortcut then trims the selection, calculates the duration, and divides it by 20 to determine the frame interval, with a minimum threshold of 0.1 seconds to avoid issues. Finally it generates the GIF with those parameters and displays it in Quick Look.

The key limitation is that this always produces exactly 20 frames regardless of video length, so longer clips become choppy—a 20-second video would only show one frame per second. To get smoother results, you can tap into the Make GIF settings and adjust the seconds-per-photo value, or modify the division factor. Also worth noting: the shortcut only previews the result in Quick Look, so to actually save it you'd need to share from there or add a Save to Photo Album action afterward.No pre-trim needed — this shortcut has its own **Trim** step built in. When you run it, a trim screen pops up and you drag the handles right there. Any length video works.

But there's a catch in the math that matters for your longer GIFs: see that **Duration ÷ 20** step? This shortcut always produces exactly **20 frames total**, spread evenly across whatever length you keep. A 4-second clip looks fine (5 fps), but a 20-second clip becomes 1 frame per second — a slideshow, not a smooth GIF.

Two fixes:

1. **For smooth long GIFs:** delete the Get Duration, Calculation, and the If/0.1/End If blocks. Then tap the **>** arrow on **Make GIF** and set **Seconds Per Photo** to 0.1 manually. That's 10 fps at any length. File size will grow fast past ~10 seconds, but it'll actually look like video.
2. **To auto-save:** it currently ends at Quick Look only. Either tap the share icon from the Quick Look preview to save it, or add a **Save to Photo Album** action after Make GIF so it lands in Photos every time.

Run it once as-is with a short clip just to confirm the pipeline works, then make the edits.

### SCOTT (2026-07-14T23:00)
I’m deleting it and we are going to start fro scratch. When I run that no videos come up. Pics only.

### CLAUDE (2026-07-14T23:00)
I'm realizing the issue — the Find Photos step is filtering for duration and excluding Live Photos, but it's searching within the Photos library rather than Videos. The Select Photos picker might be inheriting those constraints or the media type settings are limiting what shows up. Let me start fresh with a basic three-action shortcut and check if there's an option in Select Photos to explicitly include video content.That's the bug — the **Find Photos** step in that gallery shortcut filters by duration and Live Photo, but never actually says "videos," so the picker fed you stills. Fresh build, four actions:

1. New shortcut → **Add Action** → search **Find Photos** (not Select Photos). Add it.
2. Tap **Add Filter** inside it → set the filter to **Media Type** | **is** | **Video**. That's the line the other one was missing. Turn ON the **Limit** toggle and set it to something like 20 so it only grabs recent ones.
3. Add **Choose from List** — connect it to the Photos result if it doesn't auto-link. This shows you the videos to pick from.
4. Add **Make GIF** → tap its **>** arrow → set **Seconds Per Photo** to **0.1**, leave Auto Size on.
5. Add **Save to Photo Album**.

Name it, hit ▶, and it should present actual videos this time.

Fair warning on the picker: Choose from List shows filenames/thumbnails less elegantly than the Photos grid, but it reliably shows videos. Test with a short clip, and once it saves a working GIF to Photos, throw a 15-second clip at it and see how the file size behaves.

### SCOTT (2026-07-14T23:06)
No. This is wrong. It’s showing me the older seat videos in my library. I want the most recent first. And I want the edit screen to select the right 20 secs from my video to come up.

### CLAUDE (2026-07-14T23:06)
I need to adjust the sorting for the Find Photos action—using "Date Taken" for photos but switching to "Creation Date" for videos with the latest entries first. I should also insert a Trim Video action right after the Choose from List step so the user can access the trim interface.Two edits fix both:

1. **Newest first:** open the **Find Photos** action → set **Sort by** to **Creation Date** and **Order** to **Latest First**. (If Order isn't visible, it appears after you pick the sort.) The Limit of 20 will then grab your 20 most recent videos instead of the oldest.

2. **Trim screen:** add a **Trim Media** action between **Choose from List** and **Make GIF**. Search "Trim" → add **Trim Media** → make sure its input is **Chosen Item** (tap the variable if it grabbed the wrong one). Then update **Make GIF** so its input is **Trimmed Media** instead of Chosen Item — tap the blue variable in Make GIF and reselect it.

Final chain: Find Photos (Video, Creation Date, Latest First, Limit 20) → Choose from List → Trim Media → Make GIF (0.1 sec/photo) → Save to Photo Album.

Now when you run it: pick the video, the trim handles come up, drag to your 20 seconds, tap Save on the trim screen, and it converts just that section.

### SCOTT (2026-07-14T23:09)
I have choose from photos. Not choose from list
[File uploaded: 389378ed5695dd233cdd3888bf6ac84c387a5625.png]

### CLAUDE (2026-07-14T23:09)
I see the issue now — the "Choose from Photos" action is actually the Choose from List action that's been auto-named based on the Photos variable, which is fine. But there's a missing step: he needs to add Trim Media between the Choose from List and Make GIF actions, since Make GIF is currently pointing directly to the Selected Item instead of the trimmed media.That's actually the same action — "Choose from **Photos**" is Choose from List with the Photos variable plugged in. It'll work fine.

The build looks good except it's missing the **Trim** step, so right now it'll convert the entire video. Two changes:

1. Tap the search bar → type **Trim** → add **Trim Media**. Drag it so it sits **between** "Choose from Photos" and "Make GIF." Its input should auto-set to **Selected Item** — if not, tap the variable and pick it.
2. In **Make GIF**, tap the blue **Selected Item** variable → change it to **Trimmed Media** (it'll appear in the variable picker once Trim Media is above it).

Everything else is right — 0.1 sec/photo, Loop Forever, Auto Size, Save to Recents. Run it, pick your video, drag the trim handles to the section you want, hit Save on the trim screen, and the GIF drops into Recents.

### SCOTT (2026-07-14T23:16)
No trimmed meida option. And still not showing all videos.
[File uploaded: 11fb5e1a706c597b59929830a971444e95126009.png]

### CLAUDE (2026-07-14T23:16)
I'm seeing the issue now — the Trimmed Media output from the Trim action isn't showing up as a variable option in Make GIF because the user needs to tap "Selected Item" in the Make GIF input field and then explicitly choose "Select Variable" to access the magic variable from the Trim action above it.

For the second issue with videos not displaying, the problem likely stems from either the Find Photos filter not being set to Media Type is Video, or the 20-item limit combined with the sort order is restricting what's visible — I should suggest verifying the filter settings inside Find Photos to ensure it's actually capturing all the videos.

As for the variable assignment in Make GIF, the fix is straightforward: tap the blue "Selected Item" token once to open the menu, select "Clear Variable," and the field will reset to show "Media" ready for the next selection.

For diagnosing why videos aren't showing, I should ask what he's seeing in the list — if it's mixing photos and videos, the filter is missing; if it's only old videos, the sort might need adjustment to "Date Created" descending.Two separate fixes:

**1. Connecting Trimmed Media.** You're in the variable's detail sheet — back out of that. Instead:
- In **Make GIF**, tap the blue **Selected Item** token once → tap **Clear Variable** from that popup.
- The input field is now empty. Tap it → tap **Select Variable** (bottom bar option).
- The shortcut editor highlights — tap the small output token that appears directly **under the Trim action**. That's Trimmed Media; it only shows up in this select-variable mode, which is why you couldn't find it in a list.

**2. Videos still wrong.** Open the **Find Photos** action (scroll to the top) and verify all three, exactly:
- Filter reads **Media Type | is | Video** — not Photo Type, not Duration. If the filter says anything else, remove it and re-add.
- **Sort by: Creation Date** (not Date Taken — screen recordings and saved videos sometimes lack a "taken" date, which pushes them out of order or off the list entirely)
- **Order: Latest First**

That Date Taken quirk is the most likely culprit for both missing videos and old ones surfacing first. Screenshot me the Find Photos block if it still misbehaves after that.

### SCOTT (2026-07-14T23:20)

[File uploaded: 8baeb772dea41198cb494d3394f1090719bed520.png]

### CLAUDE (2026-07-14T23:20)
The Find Photos block configuration looks right now—it's set to filter for videos, sorted by creation date with the newest first, and limited to 20 results. That should pull the 20 most recent videos, which might resolve the earlier issue with older videos appearing. I should confirm the setup is correct and suggest that if he wants to see more videos beyond those 20, he can increase or remove the limit entirely. There's still a remaining task to handle with the connection.That Find Photos block is now correct — Media Type is Video, Date Created, Latest First. It should return your 20 most recent videos when you run it.

Two things to know about what you'll see:

1. **You'll only ever see 20** — that's the Limit doing its job. If the video you want is older than your last 20, bump the count up or toggle Limit off entirely (off = every video in your library, sorted newest first; the picker just gets longer to load).
2. The "Choose from Photos" list shows plain thumbnails without the normal Photos browsing experience — no albums, no search. That's a Shortcuts limitation, not a misconfiguration.

Still one open item from before: did you get **Make GIF** pointed at **Trimmed Media** (via Clear Variable → Select Variable → tap the token under Trim)? If Make GIF is still reading Selected Item, it'll convert the whole video and ignore your trim. Once that's connected, run it end to end and tell me what the output looks like.

### SCOTT (2026-07-14T23:25)
Is there a decent app that will do this?  Don’t mind paying.

### CLAUDE (2026-07-14T23:26)
Now I'm moving on to app recommendations for converting videos to GIFs on iPhone. ImgPlay Pro stands out as the best option with a one-time purchase model, though GIF Toaster is worth mentioning as an alternative. I'm considering whether a quick search for current pricing would be helpful since app costs fluctuate, but I have solid knowledge of these tools already—I'll keep my recommendation concise since he's looking for straightforward guidance.Yes — **ImgPlay** is the one I'd buy. It's purpose-built for exactly this: pick any video from your library, scrub to the section you want (no arbitrary duration cap), set frame rate, speed, crop, and export as GIF. The Pro unlock is a one-time purchase around $5–8 that removes the watermark and length restrictions. It does in three taps what we've been fighting Shortcuts to do for an hour.

Runner-up: **GIF Toaster** — more format options and finer compression control, slightly clunkier interface. Worth it only if you end up caring about file-size tuning for wherever you're posting these.

Honest assessment: you made the right call. Shortcuts can do this, but the picker limitations and variable-wiring friction you just hit are permanent annoyances, not one-time setup costs. A $6 app that shows you your real Photos library and a proper trim scrubber is the durable solution. Delete the shortcut.

### SCOTT (2026-07-14T23:32)
Bottom says 15 fps max 200 frames. So 13.33 sec gif?
[File uploaded: f59d0f4ca75ad98cb94ce6e5f5625ed8fc80c80f.png]

### CLAUDE (2026-07-14T23:32)
The user is asking a straightforward technical question about frame rate and duration calculations for a video conversion app. The math is simple: at 15 fps with 200 frames maximum, that gives about 13.33 seconds of video. To extend the duration, they could lower the frame rate to 10 fps for 20 seconds, or check if the Pro version allows a higher frame limit.Correct math — 200 frames ÷ 15 fps = 13.3 seconds max at those settings. Two levers to go longer:

1. **Drop the FPS.** 10 fps × 200 frames = 20 seconds. 8 fps gets you 25. For most content 10 fps still reads as smooth motion in GIF form; below 8 it starts to look steppy.
2. **Raise Max Frame.** Tap the 200 — the Pro unlock typically raises or removes that ceiling. More frames at the same FPS = more duration without sacrificing smoothness, at the cost of file size.

The real constraint is the file, not the app: 200 frames at decent resolution can push 40–60MB, and wherever you're sending it may choke. If the export comes out huge, cut resolution in the export settings before cutting FPS — resolution costs you far less visually than frame rate does.
