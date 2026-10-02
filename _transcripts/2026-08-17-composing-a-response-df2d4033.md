# Composing a response
Date: 2026-08-17
Conversation: df2d4033-f14b-4d2d-9307-ad76218c71d8
Domain: business-ops

## Summary
**Conversation Overview**

Scott is a senior decision-maker (likely VP or Director level) at Blueprint RF, a hospitality technology LSP (Licensed Service Provider) managing gateway infrastructure for major hotel brands including Marriott and Hyatt. He was asked by a colleague named Kathy to approve a property-facing letter announcing end-of-life (EOL) for the DG1 gateway platform at Marriott properties, before it goes to Woju, their Marriott corporate contact. The broader campaign was initiated by Jady, who appears to be a senior leader above both Scott and Kathy. Par is a colleague managing the Marriott relationship day-to-day. Dan appears to handle the technical/hardware support side.

Scott asked Claude to review three uploaded files — the draft Marriott EOL letter (a .docx), a December 1, 2025 EOL notice sent to Marriott GPNS (embedded in an .eml), and the Hyatt EOL communication package (three .docx files: email version, formal mailed letter, and FAQ) — then draft a reply email identifying issues before approval. Through several rounds of revision, Scott provided key factual context: Marriott had requested the EOL date be extended from 12/31/26 to 6/30/27 (likely documented in writing); the December notice went to the Marriott GPNS distribution list, not to individual properties; and Marriott has indicated intent to standardize on an AirAngel/11OS gateway solution following their EMEA precedent, which Scott believes may be the same initiative as the MikroTik single-gateway evaluation referenced by Par. Scott's strategic read is that the commercial window is selling DG2 replacements before a competing brand mandate lands, but he explicitly decided that reasoning should stay out of the written email and be handled verbally with Jady.

The final email draft raises six editorial items for Kathy and Par: naming the 6/30/27 date as a Marriott-requested extension to the original notice; verifying rather than demanding the written extension request; resolving the silent incentive term (10% discount from the December notice that disappeared from the letter); removing unsupported Marriott Brand Standards assertions given no citable standard exists and the brand's emerging direction points elsewhere; correcting "Dominion Gateway" naming throughout the Hyatt documents per Legal guidance to use DG1/DG2 only; and completing the full four-piece campaign package before approving the letter in isolation. Item 7 was deliberately narrowed to a factual confirmation ask to Par about gateway decision status, stripping all strategic rationale. A separate note flags the Hyatt/Marriott EOL date asymmetry (12/31/26 vs. 6/30/27 for identical hardware) as a matter for Jady to address before it surfaces externally. Scott's approval is conditioned on items 1–4 being resolved and the full document set being ready together.

Scott communicates in direct, structured email with numbered items and clear conditional sign-off language. He distinguishes carefully between what belongs in writing versus what should be handled verbally, and between claims the company can substantiate versus those it cannot. He corrected Claude twice during drafting: to clarify that the December notice reached the GPNS distribution (not individual properties), and to soften the extension documentation request from a demand to a verification. He also made a deliberate editorial judgment to remove the AirAngel/gateway-timing rationale from the email entirely, keeping it for a direct verbal conversation with Jady.

**Tool Knowledge**

Claude extracted content from uploaded files using Python with the `python-docx` library for .docx files and the standard `email` library for the .eml file. For the .eml, the PDF attachment was extracted using `part.get_payload(decode=True)` and read with `pdftotext -layout`, which preserved tabular formatting. The .docx extraction iterated both `document.paragraphs` and `document.tables` to capture all content including structured data. This two-pass approach (paragraphs then tables) is necessary for Blueprint RF documents as key terms and dates often appear in table cells rather than paragraph text.

### SCOTT (2026-08-17T19:29)
help with reply
[File uploaded: FW_ Hyatt EOL Communications and replace for Marriott .pdf]
[File uploaded: Product Lifecycle Notice_ Dominion V1 End-of-Life Announcement.eml]
[File uploaded: Formal Mailed Letter Version - Marriott DG1 EOL - Final.docx]

### CLAUDE (2026-08-17T19:31)

Read all three. The letter itself is clean on naming (DG1/DG2 only), but there are two material problems before you sign off:

**Date conflict.** The letter commits to support through 6/30/27 with a 3/30/27 signature deadline. Par's 12/1/25 notice to Marriott GPNS — which you were copied on — states final maintenance 12/31/26, and Jady's 7/1/26 Hyatt email uses 12/31/26 EOL with a 9/30/26 property deadline. So we'd be putting a second, later date in writing to the same customer without acknowledging the first, and running two EOL dates for the same hardware across two brands. Also worth confirming Dan's side can actually carry DG1 six more months.

**Brand standard assertion.** The two Hyatt Brand Standards references were swapped for "current Marriott Brand Standards require the use of a non-EOL Gateway platform." Hyatt's was concrete — Nomadix is their approved gateway. Marriott's equivalent doesn't obviously exist, and Par's own note says the Global Network team is evaluating MikroTik as a single-gateway solution. Asking ownership to fund an upgrade on a brand requirement we can't cite is exposure, especially in a letter Woju is being asked to bless in writing.

Secondary: the 10% incentive from the December notice vanished entirely from this letter, and the two attachments Par plans to send Woju use "Dominion" throughout including the subject line and PDF title.

One judgment call to flag: item 2 is the one that could read as blocking Jady's directive, since he told Kathy to get this rolling. If you'd rather not put the brand-standard challenge in writing on a thread Kathy controls, it strips cleanly — send 1, 3, 4, 5 and handle the brand-standard question with Par directly.

### SCOTT (2026-08-17T19:33)
heres the attachment to the 12/1 2025 email.  were you abel to read it.  and i htink Marriott pushed back on that as aksed for us to ectend to the june 2027 date
[File uploaded: Dominion V1 End Of Life Product Lifecycle Notification.pdf]

### CLAUDE (2026-08-17T19:34)
Yes — I pulled it out of the .eml attachment before drafting, so the 12/31/26 final maintenance date and the 10% window were already factored in.

The extension being Marriott-requested changes the framing but doesn't remove the issue. Three things follow from it:

**The letter should say it's an extension.** As written, 6/30/27 just appears as the date. Every owner on the 12/1/25 distribution saw 12/31/26. If we don't name the change, it reads as a deadline that moved once and can move again — which is exactly what kills the 3/30/27 signature push. Naming it as a concession granted at Marriott's request does the opposite: it's a one-time accommodation with a hard back end.

**Confirm the extension is documented.** If Woju asked verbally, we're about to put a six-month support commitment in writing to ownership on the strength of a phone call. Get it in an email from him before the letter goes out — which is convenient, since he's reviewing it anyway.

**Hyatt asymmetry is now live.** Jady's 7/1/26 letter has Hyatt at 12/31/26 on the same hardware. Marriott at 6/30/27 is a six-month gap on an identical platform, and the Hyatt properties are being pushed to Nomadix on the shorter clock. Someone should decide whether that's defensible as brand-specific compliance timing before Hyatt asks, and that's Jady's call, not something to settle on this thread.

The incentive question also sharpens: 10% expiring 12/31/26 against a 3/30/27 signature deadline is either deliberate — early-action carrot inside an extended window, which is a reasonable design — or an oversight. Either way the letter currently says nothing, and that's the gap.

Revised draft:

The Hyatt paragraph is the one to decide on deliberately. It's factual and belongs on the record eventually, but putting it on a thread Kathy owns means it reaches Jady through her rather than from you. If you'd rather raise it with him directly, cut that paragraph and the draft still stands on its own.

### SCOTT (2026-08-17T19:34)
here's what went to hyatt.  make sure it foots to what tyou are saying
[File uploaded: Frequently Asked Questions.docx]
[File uploaded: Hyatt EOL Email Version.docx]
[File uploaded: Hyatt EOL Formal Mailed Letter Version.docx]

### CLAUDE (2026-08-17T19:35)

Checked all three against what I sent you. Most of it foots; two things need correcting and one needs adding.

**Foots:** Hyatt EOL is 12/31/26 in all three documents, deadline 9/30/26, and the brand-standard reference is concrete and sourced — the FAQ states flatly that Hyatt requires the Nomadix Gateway as the approved platform, and both letters say the Dominion is no longer approved under Hyatt Brand Standards. That's a real mandate stated as fact. The Marriott letter's "current Marriott Brand Standards require the use of a non-EOL Gateway platform" is generic by comparison and points to no document. The contrast is sharper than I put it.

**Correction — drop the deposit item.** Both Hyatt versions require signed proposal plus deposit. It's established precedent, not a new term.

**Correction — the naming problem is bigger.** All three Hyatt documents say "Dominion Gateway" throughout, including the FAQ. That's property-facing material, sent to Hyatt corporate on 7/1 and headed to owners. So this isn't just about which attachments Par forwards to Woju — the Hyatt set itself needs remediation before further distribution. That's presumably what prompted Par's question in the first place.

**Addition — the package is incomplete.** Jady's plan specified four artifacts: property email, formal mailed letter, one-page FAQ, proposal. Only the formal letter was Marriott-ized. The FAQ is the one carrying the heaviest Hyatt/Nomadix language ("Hyatt now requires the use of the Nomadix Gateway"), and it's the piece non-technical owners actually read. Approving the letter alone doesn't approve the campaign.

One observation not worth an email line: the Marriott letter is markedly softer than the Hyatt version — "we strongly recommend" against Hyatt's "may result in loss of guest Wi-Fi service." That's correct, because we can't compel Marriott owners the way Hyatt's mandate compels theirs. Which is itself an argument against manufacturing the brand-standard line — the letter already works as a supportability argument.

Item 5 is now the one with reach beyond this thread — if the Hyatt materials have already gone to properties with "Dominion" in them, that's a remediation question rather than an edit, and Legal may want to know. Worth finding out from Amy what's actually been distributed before the email goes out, so you're not raising it as a hypothetical.

### SCOTT (2026-08-17T19:39)
1.clarify that the dec email wnet to all of hte peoel on thsi distro.
 2. we have that in wroiting I am preety sure.  so change that to say verify.
[File uploaded: 1786995477927_image.png]

### CLAUDE (2026-08-17T19:40)
Both corrections make sense, and the first one changes the argument in a useful way — the December notice went to the Marriott GPNS group address, not to properties. So owners never saw 12/31/26; Marriott corporate did, including the team reviewing this letter. That makes the date discrepancy a reviewer-facing issue rather than an owner-facing one, which is a stronger reason to name it up front rather than a weaker one.

If Par confirms the extension request in writing before you send, item 2 collapses to one line about Dan and DG1 hardware coverage — worth checking with him first so you're not asking for something already in the thread.

### SCOTT (2026-08-17T19:44)
on #7 - Marriott has already said they want to go with an AirAngel/11OS gateway just lie they did in emea

### CLAUDE (2026-08-17T19:45)
That changes the shape of the campaign, not just item 7.

If Marriott is heading to AirAngel/11OS the way EMEA did, the letter is asking owners to fund a DG2 in Q1 2027 that the brand may redirect within a year. The owner eats stranded capital and we own the conversation as the LSP. That's a different risk than "a decision might be coming."

It also makes item 4 considerably worse. Asserting that Marriott Brand Standards require a non-EOL gateway platform — in a letter that then sells our gateway — while Marriott's actual emerging standard points to somebody else's, is a claim that could be read as using the brand's name against its own direction to move our hardware. That's the piece I'd most want out of the letter now, regardless of what happens to the rest.

The clean separation: DG1 support ending 6/30/27 is true no matter which gateway Marriott lands on, and owners need that notice. Whether the replacement is DG2 or AirAngel is Marriott's call. A letter that gives the EOL notice and says we'll work with the property on a replacement path consistent with Marriott's direction is defensible in any outcome. A letter that demands a signed DG2 proposal and deposit by 3/30/27 is only defensible if DG2 is where Marriott lands.

One factual question worth resolving before you assert anything: Par's note said Global Network is considering MikroTik as the single-gateway solution, and you're saying AirAngel/11OS. Those may well be the same initiative — AirAngel deploys on MikroTik hardware in some designs — but if they're two separate tracks, that matters. Worth asking rather than assuming.

Revised 4 and 7:

Item 7 as written effectively recommends stripping the DG2 sale out of a campaign Jady initiated, on a thread Kathy controls. That's a bigger call than editing a letter, and it lands better coming from you to Jady directly than arriving at him secondhand.

If you want to keep the email in editorial territory, send 1–6 and hold 7 for a verbal with Jady — the AirAngel point is exactly the kind of thing that reads differently in writing than it does in a two-minute conversation.

### SCOTT (2026-08-17T19:46)
i tink maybe our hops is that they buy our new gateway beifre the new signle gateway mandate comes out

### CLAUDE (2026-08-17T19:46)
That's probably right, and it's worth separating the two things inside it, because one is fine and one isn't.

Selling DG2 into properties before a competing standard lands is ordinary commercial timing. Every vendor does it. The EOL is real, the no-RMA position is real, and a property that buys DG2 in Q1 2027 gets a supported gateway for however long it runs. Nobody has to apologize for that.

What doesn't survive contact is the brand-standard sentence. Telling ownership that Marriott Brand Standards require this upgrade, while we understand Marriott is heading to AirAngel, converts a timing play into a claim about the brand's position that the brand hasn't made — and we're asking Marriott corporate to sign off on it. If the mandate lands in 2027 and owners who just spent capital go back to Marriott asking why, the thread that gets pulled is the letter Woju approved. Par is the one holding that relationship.

The practical math also isn't obviously favorable. Signatures are due 3/30/27 and the mandate timing is unknown. If it lands before then, the campaign stalls and we've spent goodwill for nothing. If it lands after, we've placed gateways that get displaced inside a year or two, and we're the LSP fielding those calls — right as we'd want to be positioned as the integrator for whatever Marriott standardizes on. That's the bigger prize and it's the one that gets harder to win if owners feel they were sold into a dead standard.

So: keep the urgency, source it from facts we own. Support ends 6/30/27. No RMA path on the hardware. The 10% expires. Those are all true and none of them require us to speak for Marriott. The letter is actually strong on supportability already — it doesn't need the brand line to work.

That version also lets you approve it without your name sitting on the brand-standard claim, which matters given Kathy asked you specifically to approve.

Want me to cut item 7 down to just the confirmation ask to Woju and leave the campaign strategy out of writing entirely? That keeps the email editorial and puts the timing question where it belongs, with Jady, verbally.

### SCOTT (2026-08-17T19:49)
yes

### CLAUDE (2026-08-17T19:49)

AirAngel is out of the email entirely — item 7 is now just a factual ask to Par, and item 4 rests only on the absence of a citable Marriott standard, which is defensible on its own without reference to where the brand is heading.

Two things left for the verbal with Jady: the timing bet itself, and the Hyatt date asymmetry if you'd rather he hear that from you than off Kathy's thread.
