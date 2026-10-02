# Mass deleting Amazon saved for later items
Date: 2026-08-01
Conversation: ed73ddbb-34aa-4dd0-8b9d-88b01a8cb969
Domain: skip

## Summary
**Conversation Overview**

The person asked for help bulk-deleting items from Amazon's Saved for Later list. Claude explained that Amazon has no native bulk-delete feature and walked through a browser console-based JavaScript solution. The conversation involved iterative troubleshooting across several steps: identifying the correct DOM selector, handling Chrome's self-XSS paste warning, dealing with lazy-loading, and refining scripts based on what was actually rendered on the page.

The key technical breakthrough came when the person shared a screenshot revealing Amazon's actual data attributes: `data-action="delete-saved"` for Saved for Later items and `data-action="delete-active"` for active cart items. This made the selector both precise and safe. From there, Claude provided three separate scripts used in sequence: a scroll-to-bottom auto-loader that polls until the item count stabilizes across five passes, a count check (`document.querySelectorAll('input[data-action="delete-saved"]').length`), and the delete loop that clicks items one at a time with a 1200ms delay to accommodate page re-rendering. The person confirmed 436 items loaded and proceeded with deletion. The conversation also covered how to open Chrome DevTools (Ctrl+Shift+J on Windows) and how the `allow pasting` guard works — it only activates in response to a paste attempt, not preemptively.

The person's communication style was casual and direct, comfortable with trial and error, and preferred receiving scripts cleanly re-pasted on request rather than being pointed back to prior messages. They declined the suggestion to save a record of items before deleting.

### SCOTT (2026-08-01T12:55)
is the a way to mass delte saved for later list in amazon

### CLAUDE (2026-08-01T12:55)
The user is asking about bulk deleting items from Amazon's Saved for Later list. Amazon doesn't have a built-in bulk delete feature, so the typical workarounds involve using browser console scripts, extensions, or manually deleting each item one by one. I should search to see if this functionality has been added recently or if there are any new methods available.

There's no native bulk delete option, so I'll suggest the browser console script approach since it automates the deletion process directly in their own browser. The move-to-list workaround doesn't actually help since moving items one-by-one is just as tedious, and while you can delete an entire list at once, you'd still need to manually move each item first.

I'm writing a script that finds and clicks the delete controls for saved items, adding delays between clicks since Amazon re-renders the page after each removal. The selectors can be fragile since Amazon changes their markup, so I'll include a note to test it carefully first and mention the caveats around rate limiting and needing to run it repeatedly for large lists.Short answer: no. Amazon has never shipped a bulk-delete or multi-select for Saved for Later — you have to delete each item individually, and that's still true.

Three workarounds, in order of how much I'd trust them:

**1. Browser console script (fastest, ~5 min for hundreds of items)**

Open the cart page on desktop, scroll to the bottom of the Saved for Later section repeatedly until everything is loaded (it lazy-loads), then open DevTools (Ctrl+Shift+J / Cmd+Opt+J) and paste:

```js
(async () => {
  const q = () => Array.from(document.querySelectorAll(
    '#sc-saved-cart input[data-action="delete"], #sc-saved-cart [aria-label^="Delete"]'
  ));
  let n = 0;
  while (q().length) {
    q()[0].click();
    n++;
    await new Promise(r => setTimeout(r, 1200));
  }
  console.log('Clicked delete on', n, 'items');
})();
```

The 1200ms delay matters — the cart re-renders after each removal, and firing clicks in a tight loop either misses elements or gets you throttled. Expect to re-run it a few times; it only sees what's rendered.

**2. Verify the selector first.** Amazon changes cart DOM regularly, and the version above may not match what you're seeing. Before running the loop, run just `document.querySelectorAll('#sc-saved-cart input[data-action="delete"]').length` — if it returns 0, right-click an actual Delete link → Inspect, and swap in whatever attribute it's actually using.

**3. Manual, on mobile.** If the list is under ~50 items, the app is genuinely faster than fighting selectors. Tap Delete, the list collapses upward, tap the same spot again.

Two things worth flagging: this is automation against Amazon's site, which their ToS technically prohibits — practically nobody gets actioned for clearing their own cart, but it's your account. And there's no undo. If some of those saved items are things you actually wanted to track, move them to a wish list first (also one at a time, unfortunately) or scrape the titles before deleting:

```js
console.log(Array.from(document.querySelectorAll('#sc-saved-cart .sc-product-title'))
  .map(e => e.innerText.trim()).join('\n'));
```

### SCOTT (2026-08-01T12:59)
loosk like blocked
[File uploaded: 1785589137541_image.png]

### CLAUDE (2026-08-01T12:59)
I'm seeing Chrome's self-XSS protection warning here—the user needs to type "allow pasting" to proceed. The blocked script errors are just from sandboxed ad iframes and aren't the issue. I should acknowledge the warning exists for good reason since they're pasting code I provided, and give them a quick explanation of what the script does so they can verify it's safe.That's not your script being blocked — it's Chrome's self-XSS guard, which fires on *any* first paste into the console on a page.

The two red "Blocked script execution" errors are unrelated noise from Amazon's own ad iframes. Ignore them.

**Fix:** click into the console prompt, type `allow pasting` (literally, by hand — pasting it won't work), press Enter. Then paste the script.

Before you do: that warning is there for a real reason, and the correct response to it is to actually read the code, not just click past it. Mine does three things — finds elements in the `#sc-saved-cart` container whose delete attribute matches, clicks the first one, waits 1.2 seconds, repeats until none are left. No network calls, no reading of page data, nothing sent anywhere. If any line doesn't look like that to you, don't run it. Same standard applies to any console snippet anyone hands you.

Also worth doing first, before the loop: run the count check by itself.

```js
document.querySelectorAll('#sc-saved-cart input[data-action="delete"]').length
```

If that returns `0`, the loop will spin uselessly and you'll want the selector fix from before.

### SCOTT (2026-08-01T13:00)
yes. retunred zero.  now give me the script again

### CLAUDE (2026-08-01T13:00)
The selector approach isn't working reliably since Amazon's page structure keeps changing. Instead of guessing at specific IDs, I should write a discovery script that scans the entire page for delete controls by looking for elements with "Delete" in their text, aria-label, or value attributes, then reports what it finds and adapts from there.

Once I have visibility into what's actually on the page, I can locate the "Saved for later" heading, find its nearest container, and scope the deletion loop to just that section.

Writing diagnostic script...Two steps — I'm not going to guess a third selector blind.

**Step 1: find out what the delete controls actually are.**

```js
const cands = Array.from(document.querySelectorAll('input,button,a,span,[role="button"]'))
  .filter(e => /^delete$/i.test((e.value || e.getAttribute('aria-label') || e.innerText || '').trim()));
console.log('found:', cands.length);
cands.slice(0, 2).forEach(e => console.log(e.outerHTML.slice(0, 300)));
```

If `found:` is still 0, tell me — it likely means Amazon served you the newer cart layout where saved items live in a different component, and I'll need to see the markup. If it's a sensible number (roughly your item count, possibly plus a few from the active cart), continue.

**Step 2: scoped loop with a dry run.**

```js
const DRY_RUN = true;   // flip to false when the preview looks right

(async () => {
  const heading = Array.from(document.querySelectorAll('*'))
    .find(e => e.children.length === 0 && /saved for later/i.test(e.textContent));
  if (!heading) return console.log('could not locate the Saved for Later heading');

  const find = () => Array.from(document.querySelectorAll('input,button,a,span,[role="button"]'))
    .filter(e => /^delete$/i.test((e.value || e.getAttribute('aria-label') || e.innerText || '').trim()))
    .filter(e => heading.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING);

  if (DRY_RUN) return console.log('would delete', find().length, 'items (nothing clicked)');

  let n = 0;
  while (find().length && n < 500) {
    find()[0].click();
    n++;
    await new Promise(r => setTimeout(r, 1200));
  }
  console.log('clicked delete on', n, 'items');
})();
```

The `compareDocumentPosition` filter is what keeps it off your active cart — it only touches controls that appear *after* the "Saved for later" heading in the document. That's the part worth verifying: if the dry run reports a count noticeably higher than your saved item count, stop, because it's catching cart items too.

Scroll to the bottom several times first to force the lazy-load, and expect to re-run after each pass.

### SCOTT (2026-08-01T13:03)

[File uploaded: 1785589382927_image.png]

### CLAUDE (2026-08-01T13:03)
I see the actual data attributes now — `data-action="delete-active"` for cart items and `data-action="delete-saved"` for saved-for-later items, which is a much cleaner way to distinguish between them than relying on heading positions. I also notice the submit button follows the pattern `name="submit.delete-saved.<uuid>"` for saved items. Let me write a corrected script with a dry run first to filter for only the saved-for-later deletions.That's the answer — Amazon distinguishes them at the attribute level. `data-action="delete-active"` is a cart item; `data-action="delete-saved"` is a Saved for Later item. That's far more reliable than the document-position trick, so throw that version out.

Count first:

```js
document.querySelectorAll('input[data-action="delete-saved"]').length
```

That number should be your saved-item count. Then:

```js
(async () => {
  const find = () => Array.from(document.querySelectorAll('input[data-action="delete-saved"]'));
  let n = 0;
  while (find().length && n < 1000) {
    find()[0].click();
    n++;
    await new Promise(r => setTimeout(r, 1200));
  }
  console.log('clicked delete on', n, 'items');
})();
```

Nothing in that selector can match a cart item — `delete-active` and `delete-saved` are distinct strings, and there's no prefix matching happening. Your cart is safe.

Two practical notes. Each click submits a form and the cart re-renders, so the page will visibly churn; don't touch anything while it runs. And it only sees what's loaded, so after it reports done, scroll to the bottom a few times and re-run until the count check returns 0.

If you want the titles first, that `aria-label` is where they live:

```js
console.log(Array.from(document.querySelectorAll('input[data-action="delete-saved"]'))
  .map(e => e.getAttribute('aria-label').replace(/^Delete\s*/, '')).join('\n'));
```

### SCOTT (2026-08-01T13:08)
it soden ans now liast is zero

### CLAUDE (2026-08-01T13:08)
Nice — that's the whole list gone.

Worth confirming it stuck rather than just re-rendering empty: hard refresh the cart page (Ctrl+Shift+R) and check the Saved for Later section is still empty. Amazon's cart state is server-side, so it should be, but a refresh is the only real proof.

Also glance at your active cart while you're there. The script couldn't have touched it, but a quick look costs nothing.

If it ever fills up again, the useful piece to keep is the selector: `input[data-action="delete-saved"]`. That's the part that took the digging — the loop around it is trivial to rewrite.

### SCOTT (2026-08-01T13:09)
opps spoke too soon.  i think i had not scrolled al the way down beofre starting...

### CLAUDE (2026-08-01T13:09)
Expected — that's the lazy-load, exactly the caveat from earlier. Nothing broke; the script just cleared what was rendered at the time, and Amazon then loaded the next batch in.

Loop it:

1. Scroll to the very bottom, wait for it to stop loading, repeat until scrolling stops adding items.
2. Run the count check.
3. Run the delete loop.
4. Refresh the page and go back to step 1.

Each pass should clear a few hundred. Keep going until a fresh page load shows zero.

If the manual scrolling is tedious, this does both — auto-scrolls until the count stops growing, then deletes:

```js
(async () => {
  const find = () => Array.from(document.querySelectorAll('input[data-action="delete-saved"]'));
  let last = -1, stable = 0;
  while (stable < 3) {
    window.scrollTo(0, document.body.scrollHeight);
    await new Promise(r => setTimeout(r, 1500));
    const c = find().length;
    stable = (c === last) ? stable + 1 : 0;
    last = c;
    console.log('loaded:', c);
  }
  console.log('deleting', last);
  let n = 0;
  while (find().length && n < 1000) {
    find()[0].click();
    n++;
    await new Promise(r => setTimeout(r, 1200));
  }
  console.log('deleted', n, '— refresh and re-run');
})();
```

It waits for the count to hold steady across three scroll attempts before it starts deleting, which is the part your first run skipped. Still re-run after a refresh until it reports zero — a single pass genuinely may not get everything if the list is deep.

### SCOTT (2026-08-01T13:10)
whats the kys to open the dev comnsole

### CLAUDE (2026-08-01T13:10)
Chrome on Windows: **Ctrl+Shift+J** opens straight to the Console. F12 or Ctrl+Shift+I opens DevTools to whatever panel you last used.

Mac: **Cmd+Option+J** for Console, Cmd+Option+I for DevTools.

Firefox is the same combos. Safari needs Develop enabled in Settings → Advanced first, then Cmd+Option+C.

### SCOTT (2026-08-01T13:11)
and the script for the coount again please

### CLAUDE (2026-08-01T13:11)
```js
document.querySelectorAll('input[data-action="delete-saved"]').length
```

That's the count of Saved for Later items currently loaded in the page — not your total, if the list hasn't fully lazy-loaded yet.

### SCOTT (2026-08-01T13:12)
is there a scroll down script i can run.  there is years worth of shit here

### CLAUDE (2026-08-01T13:13)
Yes — this is the scroll half of the earlier script, standalone. Run it, walk away, come back to a fully loaded list:

```js
(async () => {
  const count = () => document.querySelectorAll('input[data-action="delete-saved"]').length;
  let last = -1, stable = 0, passes = 0;
  while (stable < 5 && passes < 400) {
    window.scrollTo(0, document.body.scrollHeight);
    await new Promise(r => setTimeout(r, 1500));
    const c = count();
    stable = (c === last) ? stable + 1 : 0;
    last = c;
    passes++;
    if (passes % 5 === 0) console.log('loaded:', c);
  }
  console.log('DONE loading —', last, 'items');
})();
```

It stops when the count holds steady across five scroll attempts, so a slow-loading batch won't fool it into quitting early. The 400-pass ceiling is a safety stop; if it hits that, just run it again.

Two things about "years worth." At 1.2s per delete, a thousand items is about twenty minutes of the delete loop grinding away — that's fine, just don't close the tab. And with a list that deep, run the title-dump before you delete:

```js
console.log(Array.from(document.querySelectorAll('input[data-action="delete-saved"]'))
  .map(e => e.getAttribute('aria-label').replace(/^Delete\s*/, '')).join('\n'));
```

Right-click the console output → Save as, and you've got a text file of everything. Costs you ten seconds and it's the only thing standing between you and permanently losing a list you can't reconstruct. Years of saves usually has a handful of things in it you'd actually want back.

### SCOTT (2026-08-01T13:13)
i need to do thew allow pasting again  is that the correct command

### CLAUDE (2026-08-01T13:13)
Yes — type `allow pasting` by hand and press Enter. Exactly that, lowercase, no quotes.

You'll hit it again on each new tab or after a refresh; Chrome doesn't remember it per-session. Same drill each time.

### SCOTT (2026-08-01T13:13)
hmm
[File uploaded: 1785590035514_image.png]

### CLAUDE (2026-08-01T13:14)
That SyntaxError is actually good news — it means the guard isn't active. Chrome only intercepts `allow pasting` as a magic phrase *while* the warning is showing. Once it's already unlocked, the console just tries to evaluate it as JavaScript, and `allow pasting` isn't valid JS. Hence the error.

So: skip it and paste your script directly. It should work.

If it doesn't — if the yellow warning reappears — the sequence has to be: paste attempt first (which triggers the prompt), *then* type the phrase. Typing it preemptively does nothing.

### SCOTT (2026-08-01T13:14)
give me the scroll down script again

### CLAUDE (2026-08-01T13:14)
```js
(async () => {
  const count = () => document.querySelectorAll('input[data-action="delete-saved"]').length;
  let last = -1, stable = 0, passes = 0;
  while (stable < 5 && passes < 400) {
    window.scrollTo(0, document.body.scrollHeight);
    await new Promise(r => setTimeout(r, 1500));
    const c = count();
    stable = (c === last) ? stable + 1 : 0;
    last = c;
    passes++;
    if (passes % 5 === 0) console.log('loaded:', c);
  }
  console.log('DONE loading —', last, 'items');
})();
```

It prints a running count every fifth pass, so you'll know it's alive. Wait for the `DONE loading` line before running the delete loop.

### SCOTT (2026-08-01T13:15)
done.  436 items.,  jeesh  my wife loves adding shit to the save it for later lsit.  give me the delete sctript again

### CLAUDE (2026-08-01T13:15)
436 at 1.2s each is about nine minutes. Leave the tab alone while it runs.

```js
(async () => {
  const find = () => Array.from(document.querySelectorAll('input[data-action="delete-saved"]'));
  let n = 0;
  while (find().length && n < 1000) {
    find()[0].click();
    n++;
    if (n % 25 === 0) console.log(n, 'deleted,', find().length, 'left');
    await new Promise(r => setTimeout(r, 1200));
  }
  console.log('clicked delete on', n, 'items');
})();
```

One thing before you pull the trigger, given whose list this partly is: 436 items of your wife's saved stuff is about to be unrecoverable. Ten seconds of insurance —

```js
console.log(Array.from(document.querySelectorAll('input[data-action="delete-saved"]'))
  .map(e => e.getAttribute('aria-label').replace(/^Delete\s*/, '')).join('\n'));
```

Right-click the output → Save as. Then if she asks where that one thing went, you have an answer that isn't "I ran a script."

### SCOTT (2026-08-01T13:16)
na.  fuck thaty.  she doent need it.  she buys too much shot already

### CLAUDE (2026-08-01T13:16)
Your call — it's a shared cart, you know the dynamic.

Script's above, ready to paste. Expect roughly nine minutes of churn, then re-run the scroll script and check the count. It may take a second pass.
