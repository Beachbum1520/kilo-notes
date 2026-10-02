# Review response assistance
Date: 2026-05-20
Conversation: 42d048bd-7e8d-4b4e-829d-ca00436d95a0
Domain: business-ops

## Summary
**Conversation Overview**

The person is working on a contract negotiation involving a Schedule 7 SLA (Service Level Agreement) document between Blueprint RF (BPRF) and Marriott. They uploaded a Word document titled "Proposed SLA Language Schedule 7" and asked Claude to review it and help draft a response to a colleague named Par Bayat, identified as Hospitality Support Manager at Blueprint RF. The core issue was choosing between two credit cap options: Option 1 (10% cap on SLA performance credits relative to total Helpdesk and NOC services fees) and Option 2 (a 50% escalating cap triggered by consecutive same-metric failures, representing a 5x increase in per-property financial exposure).

Claude extracted and analyzed the document, identified a key "Note to Draft" (NTD) flag at the top of the schedule explicitly stating BPRF would not agree to the escalation structure in Option 2, and flagged that Par's framing incorrectly characterized Option 2 as simply a Marriott request rather than a BPRF-proposed structure already marked as a non-starter internally. The person confirmed via follow-up selections that they wanted to hold the 10% cap (Option 1) as the protective position and that a colleague named Jady should be looped in as an explicit approval gate before any movement toward the 50% option. Claude produced a final email draft addressed To Par, CC Jady, directing Par to proceed with Option 1 and establishing that any 50% movement requires Jady's sign-off. The person also asked Claude to clarify the term "NTD," which Claude explained as "Note to Draft" — a working annotation convention used in contract negotiation to flag unresolved issues, intended to be removed before document finalization.

### SCOTT (2026-05-20T22:45)
review attahced and help woth a repsonse
[File uploaded: Proposed SLA Language Schedule 7.docx]
[File uploaded: 1779317110251_image.png]

### CLAUDE (2026-05-20T22:46)
I'll review the attached document before drafting a response. Let me read it first.

Now let me read the actual document content.

I've now reviewed the full document. Let me search for any prior context on this Marriott/Schedule 7 negotiation so the response is consistent with what's already happened.

I have the full picture now. This is the Marriott Schedule 7 SLA negotiation, and the document is the same Performance Credits framework you've been working through. Par Bayat (Hospitality Support Manager at Blueprint RF) is asking which of two credit-cap options to put forward.

Here's the key thing the document makes clear before I draft anything: this isn't really "their" two options — both options are **Blueprint RF / BPRF proposals to Marriott**, and they represent dramatically different risk exposure for your side.

**Option 1 (10% cap)** keeps the standard language: maximum credit never exceeds 10% of the total Helpdesk and NOC services fees, even for consecutive failures. This is the conservative, BPRF-protective position. Note the document already carries an explicit NTD flag at the top: *"BPRF will not agree to the 'Proposal' regarding SLA credits at the end of Schedule 7"* — and the 50% structure **is** that flagged Proposal.

**Option 2 (50% cap)** is the escalation structure where, on a consecutive same-metric failure, the 10% cap is waived and credits ramp to **up to 50% of MRC** by the third consecutive month. That's a 5x increase in maximum financial exposure per property, and it's the version your own document expressly flags BPRF as unwilling to agree to.

So the framing in Par's email is slightly off — Option 2 isn't simply "agreeing to their request," it's adopting a credit structure your team has already internally flagged as a non-starter. That's worth correcting gently rather than just picking a number.

Before I draft, two quick things so I level this correctly:

Looks like the selection didn't come through — no choice registered. No problem, I'll give you a reply you can use right now that holds the protective line without locking anything in prematurely, and you can adjust if you want a different posture.

This draft holds the 10% cap (Option 1), corrects the framing that Option 2 is simply "their request," flags that the 50% structure is the one your own document marks as a non-starter, and stops short of any commitment on the 50% path — consistent with not putting future concessions in writing before you've decided.

That's ready to send or tweak.

A few notes on the choices I made, and where you might want to steer differently:

The draft directs Par to **proceed with Option 1**, holds the 50% path open only as a future "if Marriott pushes" contingency, and deliberately makes no written commitment toward 50% — which keeps you off the hook for anything you haven't decided yet.

It also gently corrects Par's framing. His email described Option 2 as "agrees to their requested 50% credit," but both options are actually BPRF proposals, and the 50% version is the exact structure your schedule's NTD already flags as a non-starter. Worth Par understanding that distinction so he doesn't carry the wrong framing into a Marriott conversation.

I left Jady out of the To/CC line and instead referenced him as a conditional escalation ("if it moves toward 50%, loop in Jady"). Given the exposure on the 50% option, you may want him copied now rather than later — say the word and I'll adjust.

If your actual intent is different from "hold the line" — for example, you're genuinely open to the 50% structure with guardrails, or you want to signal flexibility to Marriott up front — tell me which posture and I'll rewrite. The earlier buttons didn't register a selection, so I went with the most protective default given the NTD flag in your own document.

### SCOTT (2026-05-20T22:46)
Q: Which direction do you actually want to take with Par?
A: Hold the 10% cap (Option 1) — the protective position

Q: Should this reply loop in Jady, given the financial exposure on the 50% option?
A: Yes — Jady should weigh in / approve before any 50% commitment

### CLAUDE (2026-05-20T22:46)
Got it — hold the 10% cap, and loop Jady in as the approval gate before any 50% movement. The earlier draft was close, but with Jady now CC'd I'll adjust the framing so the email reads correctly to two audiences at once: directing Par to proceed, while signaling to Jady that the protective position is being held and that any escalation to 50% would route through him for approval.

Ready to send. Suggested addressing: **To:** Par, **CC:** Jady.

The changes from the prior version: it now opens with a clear directive to proceed with Option 1, and the escalation paragraph explicitly establishes Jady as the approval gate — "any movement toward the 50% band will need Jady's sign-off before it goes into a document — hence the CC." That single line does the work of telling Par the boundary *and* signaling to Jady that you're holding the protective position and routing the high-exposure decision to him, without making it feel like you're asking permission for the default call.

One small judgment point worth flagging: the email tells Par not to move off 10% "in writing." That's deliberate — it lets Par verbally acknowledge Marriott's pushback without creating a paper trail that concedes ground before Jady has weighed in. If you'd rather Par not even discuss the 50% option verbally until Jady's approval, I can tighten that line.

### SCOTT (2026-05-21T00:00)
NTD??

### CLAUDE (2026-05-21T00:00)
NTD = **"Note to Draft."**

It's a drafting/markup convention used in contracts and legal documents. When someone is reviewing or negotiating a draft agreement, they insert an "NTD:" note as a flag to the other reviewers or the counterparty — basically a margin comment baked into the text saying "here's an open issue, a condition, or an instruction about this section that still needs to be resolved."

In your Schedule 7 document, the NTD appears right at the top:

> **NTD: Subject to further BPRF review, expressly provided that BPRF will not agree to the "Proposal" regarding SLA credits at the end of Schedule 7**

So whoever drafted that flag was signaling two things: (1) BPRF hasn't finished reviewing the schedule, and (2) BPRF will not agree to the "Proposal" section at the bottom — which is the 50% escalation structure (Option 2). That's exactly why I flagged Option 2 as already being marked internally as a non-starter; the document itself says so in that note.

These notes are meant to be **resolved and removed before the document is finalized** — they're working annotations, not contract language. So before this schedule goes to Marriott in final form, that NTD line should be cleaned out (and the underlying issue it flags actually decided).

In my draft to Par, I referenced "the NTD at the top of the schedule" — if you'd rather I spell it out as "the note to draft at the top" so there's zero ambiguity for Par, I can swap that. Want me to?
