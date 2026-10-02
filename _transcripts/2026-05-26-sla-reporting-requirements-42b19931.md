# SLA reporting requirements
Date: 2026-05-26
Conversation: 42b19931-c161-40e3-9cc5-985bdbba87de
Domain: business-ops

## Summary
**Conversation Overview**

The person uploaded a contract document — the "BPRF-Marriott NEW LAN Service Provider Framework" dated June 24, 2025 (draft) — and asked Claude to summarize what it says about SLA reporting. No personal details, role, or organizational context were shared beyond the document itself.

Claude extracted the full document text and searched it for SLA, service level, and reporting references, then synthesized findings across multiple sections of the agreement. The conversation was a single-turn research and summarization task with no follow-up questions or corrections from the person.

The document covers a framework agreement between Marriott (via its GPNS program) and a vendor (Blueprint RF), and Claude identified that SLA reporting obligations live primarily in Schedule 7 (Service Level Agreements / Performance Credits). Key findings included: a mandatory monthly report to the Operator detailing service delivery with enough granularity to assess compliance; escalated obligations when benchmarks are missed (root cause analysis, corrective action reports, status updates, and SME availability); integration of SLA performance into a monthly Partner Scorecard; and Performance Credits and potential decertification risk tied to sustained underperformance. Claude also flagged a structurally important limitation: the actual SLA metrics and benchmarks are not in the contract itself but are housed in an external Marriott GPNS SharePoint site requiring active Marriott credentials to access. Claude offered to pull verbatim Schedule 7 text or trace the scorecard/decertification exposure path if useful, but the person did not respond further.

### SCOTT (2026-05-26T17:03)
what does the attached say about SLA reporting
[File uploaded: BPRF-Marriott_NEW LAN Service Provider Framework_24Jun2025 draft (rfw) 9233098 1.docx]

### CLAUDE (2026-05-26T17:04)
I'll review the document to find what it says about SLA reporting.

Now let me extract the text from the document to find the SLA reporting content.

This is a large agreement. Let me search the full text specifically for SLA and reporting references rather than reading the whole thing linearly.

Let me look at the key passages in full detail, particularly the Service Level Failure Process (the most specific reporting obligation) and the surrounding context.

Let me also check the SLA Performance metrics line in the management/monitoring section and the operational summaries context around line 1202 and 1266.

I now have a complete picture of how SLA reporting is treated across the framework agreement and its SOW schedules.

The agreement handles SLA reporting at two levels — the framework level (Marriott corporate) and the property/SOW level — and the most concrete obligations live in the Statement of Work schedules, not the main body.

The core operational requirement is in **Schedule 7 (Service Level Agreements / Performance Credits)**, under the "Service Level Failure Process." Vendor (Blueprint RF) must give the Operator a detailed monthly report on its delivery of Services, with enough detail for the Operator to assess compliance against the Service Levels — including things like first notification of a service issue or complaint, time to resolution, and ticket number. If a Service Level benchmark is missed in a given month for items under Vendor's control, the report obligations escalate: Vendor must flag the miss to the property's GPNS Operator in that monthly report, promptly investigate root cause and prepare a report on causes plus corrective/preventive methods, take commercially reasonable corrective action, keep the Operator advised on remediation status, and — if the Operator requests due to the nature or recurrence of the problem — make its subject-matter experts available for meetings.

Note one important detail: the actual SLA metrics and benchmarks themselves are **not in this document.** Schedule 7 just says the LSP must comply with the SLAs posted at a Marriott GPNS SharePoint URL (the "GPNS Americas SLA Descriptions"), which Marriott can update from time to time and which require an active Marriott EID to access. Similarly, the framework's defined term "Service Levels" points to a posted SharePoint location for the "then current minimum service levels." So the obligations are committed to documents that live outside the contract and can change.

A few supporting provisions reinforce the reporting picture:

In the SOW's NOC/management scope (Schedule 6 area), Vendor commits to "Service Level Management" — providing SLA performance metrics and reporting on the applicable SLAs in Schedule 7 — plus centralized logging and reporting of the property network, and creating accounts so Operator-designated personnel can monitor the system, check ticket status, and run connectivity/billing reports themselves.

At the framework level, Section on "Reporting; Annual Performance Reviews, ARB and GPNS" ties reporting to the GPNS Standards generally and to periodic Performance Reviews with the Continent iT VP. If Marriott requests it, Vendor must submit a Continuous Quality Improvement Plan with a schedule to improve performance against the Service Levels.

SLA reporting also feeds Marriott's scorecard machinery. The "Partner Scorecard" is calculated monthly against KPIs — explicitly including the Certified Provider's SLA performance — drawing on "Certified Provider reports required by GPNS Standards." And under Section 13.2, sustained underperformance (a Red Zone Two classification beyond 30 days) can trigger Performance Credits to properties or, ultimately, withdrawal of Certified Provider status, with credits capped at 50% of total Helpdesk and NOC service fees.

If it would help, I can pull the exact verbatim text of the Schedule 7 failure-process bullets, or trace how the monthly report flows into the scorecard/decertification mechanics so you can see the full exposure path.
