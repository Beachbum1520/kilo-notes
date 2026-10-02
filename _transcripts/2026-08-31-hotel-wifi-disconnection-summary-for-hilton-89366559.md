# Hotel wifi disconnection summary for Hilton
Date: 2026-08-31
Conversation: 89366559-0db2-4db8-abb9-d91a7da00db3
Domain: business-ops

## Summary
**Conversation Overview**

The person works at BluePrint RF (also referenced as BPRF Holdings, LLC) and was preparing an urgent communication for Hilton corporate regarding a dispute with MBM Legacy Inc., a hotel owner operating two Hilton-brand properties in Fayetteville, North Carolina: Embassy Suites Fayetteville Fort Bragg (inn code FAYFB) and Hilton Garden Inn Fayetteville Fort Bragg (inn code FAYNH). The person's name appears to be Scott, based on the email sign-off used throughout. The conversation was time-sensitive, taking place after 3pm the day before a planned service disconnection at FAYFB.

The core task was to extract and reframe content from an uploaded demand letter (Final_Demand_Letter_BluePrint_RF_to_MBM_Legacy_July_31__2026.docx) into an emailable summary for Hilton corporate, stripping out all references to a third property (a Marriott-brand property, FAYFP) that was also named in the letter but irrelevant to Hilton. Claude read the document using pandoc, drafted the email, and iterated through several revisions based on legal edits and clarifications from the person. Key issues covered in the final email included: an outstanding balance at FAYFB for installation services completed in July 2025, a withdrawn settlement offer, a rejected counter-proposal from MBM, planned service disconnection at FAYFB, and unauthorized post-execution alterations to Work Orders at both FAYFB and FAYNH purporting to reduce monthly support rates. The person clarified midway that no demand letter was actually being sent to MBM, so all "final demand," "10-day deadline," and "date of the letter" framing had to be removed and replaced with language reflecting ongoing unresolved conversations. The person also confirmed that FAYNH had been paying the correct contracted rate of $414/month, so the FAYNH section was framed solely as a contract document integrity issue with no stated dollar balance due.

The person provided legal edits directly (replacing "initialed" with "never agreed to"), corrected Claude's initial misreading of FAYNH as having no financial issue at all, and made at least one edit themselves (removing a hedging sentence about unconfirmed billing rates at FAYNH). The person types with significant typos and abbreviated phrasing but communicates intent clearly; Claude should parse through spelling errors without flagging them. The person prefers direct, professional email language for external communications to corporate partners, with numbered sections and clean formatting. Claude should not over-explain caveats or open questions in the email itself — those belong in the working conversation, not the deliverable.

**Tool Knowledge**

Claude used a bash tool with pandoc to read the uploaded .docx file, converting it to plain text and markdown for review. The command `pandoc -t plain "[filename]"` piped through `grep -n -i` with property codes (e.g., "FAYNH\|Garden Inn") was effective for targeted lookups within the document. When needing to review specific sections, `sed -n '[start],[end]p'` was used to page through the output in chunks. The message_compose_v1 tool was used with `kind: email` to render polished, sendable email drafts with subject lines and body content across multiple iterations.

### SCOTT (2026-08-31T14:41)
read this attahced letter.  This hotel owner has gootten hilton corpaote invliced.  we intend to disconet the hotels wifi sevice on tomoorw.  hilton corporate has aksed for a summary.  i need to take out anythong that is related to marritt and provide and emailable summary to hiltoin.  can you help
[File uploaded: Final_Demand_Letter_BluePrint_RF_to_MBM_Legacy July 31, 2026.docx]

### CLAUDE (2026-08-31T14:42)

One flag before you send this: the letter's demand total ($37,888.22) and settlement figures ($18,944.11 credit, $15–18K counter-proposal cost) are combined across both FAYFB (Hilton) and FAYFP (Marriott). I pulled out the FAYFB-only balance ($30,564.44) for the top-line number to Hilton, but kept the settlement-offer/counter-proposal narrative as stated since the letter doesn't break those out by property — worth double-checking whether that $18,944.11 credit figure was itself a blended number before you send it as Hilton-only.

Also worth deciding deliberately: whether to mention the Marriott-side balance exists at all (even without naming Marriott) — as written, the email is silent on it, which is clean, but if Hilton ever cross-references invoice totals with the demand letter (if it's ever produced in a dispute) the numbers won't reconcile without that context.

### SCOTT (2026-08-31T14:43)
no the summary is for both hiltions.  not jsu tthe one.

### CLAUDE (2026-08-31T14:44)

Covers both FAYFB and FAYNH now. Note: the letter itself doesn't list a separate outstanding balance for FAYNH — it only shows up in the contract-alteration section (V.B), with a monthly support-charge schedule ($414/month) but no delinquency table entry. So I've framed FAYNH as a document-integrity issue only, not a payment issue — if there's a balance owed there too that just wasn't in this letter, let me know and I'll fold it in.

### SCOTT (2026-08-31T19:05)
hwere's a few edits form our lwegal.  And i just leanred we never sent the dmeand letter.  so lets reprhasr thes.  hower the owner is very aware of this and there have been many mant conversatiosns with our teams to try and reoslve this.

Subject: Summary — Outstanding Balance & Contract Document Issue, MBM Legacy Inc. (Embassy Suites & Hilton Garden Inn, Fayetteville Fort Bragg)
 
Hilton team,
 
As requested, here is a summary of the current status with MBM Legacy Inc. (MBM) across both Hilton-brand properties it operates.
 
1. Embassy Suites Fayetteville Fort Bragg (FAYFB)
 
Outstanding Balance: MBM has an outstanding balance of $30,564.44 for guest-facing technology installation services completed at the property in July 2025. Despite repeated demands, this balance remains unpaid.
 
Final Demand Issued: Blueprint RF has issued a final written demand to MBM requiring payment in full within 10 days of the letter date. Blueprint RF previously offered a 50% settlement credit; that offer was refused by MBM and has now been withdrawn. A subsequent counter-proposal from MBM (a reduction of monthly service fees to $2.00/month for 7 years across multiple properties) was also rejected as commercially unreasonable.
 
Service Disconnection: Service disconnection at this property is planned for tomorrow due to nonpayment.
 
2. Hilton Garden Inn Fayetteville Fort Bragg (FAYNH)
 
No payment delinquency is at issue at this property. The concern here is a contract document integrity issue described below.
 
3. Contract Document Concern (Both Properties)
 
Blueprint RF has identified unauthorized alterations to the executed Work Orders for both FAYFB and FAYNH. Handwritten notations purporting to reduce monthly support costs were inserted into both documents after execution, without Blueprint RF's knowledge, review, or consent, and were never agreed to ~~initialed ~~by any Blueprint RF representative. Blueprint RF considers these alterations void and unenforceable and does not recognize them for either property.
 
4. Contractual Basis
 
MBM Legacy Inc. is the Participating Entity under the Hilton Guest Facing Technology Participation Agreement with BPRF Holdings, LLC (dated February 20, 2024), under which MBM is solely responsible for its payment obligations. Hilton has no liability in connection with the Participation Agreement.
 
5. Next Steps
 
If MBM does not pay the FAYFB balance in full by the deadline stated in the demand letter, Blueprint RF intends to commence legal proceedings to recover the outstanding balance, accrued interest, and collection costs. Blueprint RF also reserves all rights with respect to the unauthorized Work Order alterations at both properties.
 
Happy to provide additional detail on any of the above.
 
Best,
Scott

### CLAUDE (2026-08-31T19:05)

Changed "has issued"/"is planned" language to present tense ("is issuing," "is being withdrawn") since the letter hasn't gone out yet — worth double-checking against whatever date it actually goes out, since "within 10 days" language should track the real send date once you have it. Also swapped "initialed" for "agreed to" per legal's edit, and added the awareness/prior-conversations context to the FAYFB balance section.

### SCOTT (2026-08-31T19:10)
i think you need to read the demand letter again beifre you say nothing is due for faybh
[File uploaded: Final_Demand_Letter_BluePrint_RF_to_MBM_Legacy July 31, 2026.docx]

### CLAUDE (2026-08-31T19:11)

I went back through the letter carefully, including the payment/wire-reference section and the settlement paragraphs.

The letter's "Amounts Owed" table (Section I) only lists two properties:

| Property | Balance |
|---|---|
| FAYFB – Embassy Suites (Hilton) | $30,564.44 |
| FAYFP – Four Points by Sheraton (Marriott) | $7,323.78 |

The wire-transfer reference line even confirms this: "Reference: MBM Legacy / FAYFB / FAYFP" — no FAYNH.

FAYNH (Hilton Garden Inn) appears only in Section V, and only in connection with the altered Work Order — there's no dollar balance stated for it anywhere in this document, just the original $414.00/month support-charge schedule.

So based on this letter alone, there's nothing due for FAYNH — the letter doesn't carry a balance for it. If there's an amount owed at FAYNH, it's coming from somewhere outside this document (AR aging, a separate invoice, etc.). Can you give me that figure, or point me to where it lives? I don't want to put a number in front of Hilton corporate that isn't backed by something in front of me.

### SCOTT (2026-08-31T19:12)
i was talkign about thsi section.  but you need to do a better job explaoing this.  and quit saying 10 day demand.  there is not demand letter being sent.
[File uploaded: 1788203547120_image.png]

### CLAUDE (2026-08-31T19:13)
That section is the FAYNH monthly-rate math, not a balance-due table — that's the distinction I was missing.

Here's what it actually shows: the **executed, signed** FAYNH Work Order fixes the monthly support charge at **$414.00**. Separately (per Section V.C, which we discussed earlier), someone inserted a handwritten notation into that same document *after* signing, dropping the rate to **$310.00/month** — never agreed to by BluePrint RF, no initials next to it. BluePrint RF's position is that $414 is the only valid, enforceable rate; the $310 notation is void.

So the "amount due" issue at FAYNH isn't a stated arrears balance like FAYFB has — it's a **rate dispute**. If FAYNH has actually been invoiced/paid at the altered $310 rate since the work order took effect, there's a shortfall accruing every month ($104/month × however many months), separate from any lump-sum balance. The letter doesn't calculate that shortfall for FAYNH — it only flags the alteration as void and reserves rights to it.

Two things I need from you before I touch the Hilton email again:

1. **Has FAYNH actually been billed at $310 instead of $414?** If yes, I can calculate the accrued shortfall once I know the billing start date. If it's been billed correctly at $414 all along, then there's no dollar amount currently due at FAYNH — just the standing legal position that the $310 notation is unenforceable.
2. **No demand letter is going out** — got it, I'll drop all "10-day," "final demand," and "date of the letter" language from the Hilton summary and reframe it around the ongoing/unresolved conversations with MBM instead.

Want me to hold the revised draft until you confirm the FAYNH billing question, or send it now with FAYNH framed purely as the unresolved rate dispute (no dollar figure)?

### SCOTT (2026-08-31T19:14)
its after 3pm on the day beofre the cutoff,  I need to get an update to hoilton corp;

### CLAUDE (2026-08-31T19:15)

This is ready to send. All "10-day"/"date of the letter"/"final demand" language is gone — it now reads as an ongoing dispute BluePrint RF is pursuing, not a letter Hilton might ask to see. FAYNH is framed as an open rate-dispute item rather than a stated balance, since I still don't have confirmation on whether it was actually billed at $310 or $414.

### SCOTT (2026-08-31T19:17)
"We are still confirming what rate has actually been billed/collected at this property and will follow up with any dollar impact once that's verified"  nope, he has beenign payign the corrdct rate, I am pretty sure.  I jsut removed that sentece

### CLAUDE (2026-08-31T19:17)
Got it — updated FAYNH section, sentence removed:

**2. Hilton Garden Inn Fayetteville Fort Bragg (FAYNH)**

No service disconnection is planned at this property. The issue here is a contract document dispute, not a payment delinquency: the executed Work Order fixes the monthly support charge at $414.00, but BluePrint RF has identified a handwritten notation inserted into that document after execution, purporting to reduce the rate to $310.00/month. BluePrint RF never agreed to or authorized this change and considers it void and unenforceable.

Rest of the email is unchanged from the last draft. Good to send as-is.
