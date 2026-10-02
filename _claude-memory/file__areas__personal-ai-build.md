---
name: personal-ai-build
description: Scott's self-hosted personal AI assistant build — architecture decisions, stack, and constraints
sources: [chat]
aliases: [personal AI, the assistant build, unified memory system]
---

- [stated] Building a private single-user AI assistant to replace consumer-tier tooling limits; wants one unified memory across all domains, phone-accessible, with project/sub-project structure as tags rather than walled containers
- [stated] Reference point: an Australian contact ("Wayne") who runs a self-hosted AI at home named "Jake," interfaced via WhatsApp
- [stated] Indifferent between Telegram and WhatsApp as the interface
- [stated] Wants Google Drive as the system of record for files; GitHub for markdown notes
- [stated] Already has GitHub (paid plan), Supabase (currently free tier), and Vercel
- [stated] Plans to outsource the build rather than write it himself
- [stated] Wants chat details captured, retained, and reused in future conversations — not just documents

## Decisions
- [stated] business-ops and job-search must be kept SEPARATE
- [stated] Raw message/transcript retention: keep a long time but not indefinitely
- [stated] Voice notes deferred past v1
- [stated] No other users at all — no spouse, no shared access
- [stated] Not cutting scope; wants the full spec settled before hiring

- [stated] Agreed to a $300/month hard API spend cap with a $150 alert threshold
- [stated] Considered hiring the build out through Upwork (used before) or OnlineJobs.ph, driven largely by how much access a contractor would need; Sept 2026: settled — not outsourcing any of it, building it himself
- [stated] No time crunch on this build — the primary motivation is learning by doing, the same reason he started the WattsWay fitness app; he wants to get better at using AI in his business, and secondarily thinks existing AI coaching/assistant products are poor
- [stated] Decided to build a thin slice himself first rather than outsource the whole thing
- [stated] Aug 5, 2026: completed the full A–E harvest on the Business Ops project — 39 conversations spanning June 12 to Aug 5, 2026, yielding 222 note files. Use Aug 5, 2026 as the baseline date for the Business Ops delta harvest later.