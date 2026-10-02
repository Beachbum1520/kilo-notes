# Kilo — Where Things Live

Orientation file for the **AI Personal Assistant** project. Read this first when picking the build back up after a gap.
Last updated: 14 September 2026.

---

## 1. Project knowledge (this project)

| File | What it is |
|---|---|
| `personal-ai-assistant-spec.md` | The spec, v1.0. Sections referenced elsewhere as §4.1, §6.1, §7, §8, §9.1, §14. |
| `thin-slice-build-guide.md` | Stage-by-stage build guide. "Thin slice" = Stages 0–7. |
| `REJECTED.md` | Alternatives considered and set aside. Check before re-proposing anything. |
| `spec-addendum-v1.md` | Consolidated output of the three systems audits (Sept 2026). **Not yet folded into the spec** — see §3. |
| `audit-findings.md` | The three audit responses in full — the evidence `spec-addendum-v1.md` was drawn from. |
| `harvest-playbook.md` | How the notes corpus is built: the five-category harvest prompt, the splitter command, corpus status, and the employer data boundary. |

## 2. Source conversations

**As of 14 Sep 2026 you should not need any of these to work.** Their substance is in the project files above: the audits in `audit-findings.md`, the design conclusions in `spec-addendum-v1.md`, the corpus procedure in `harvest-playbook.md`. The table is here for provenance, not for retrieval.

The three systems audits were each run **inside the project being audited** — the audited instance needed that project's own context to answer. They are not misfiled.

| Conversation | Lives in | Date |
|---|---|---|
| Personal AI coaching system audit | Fitness & Training project | 13 Sep 2026 |
| Personal AI system architecture audit | Business Ops project | 13 Sep 2026 |
| Personal AI system design audit | Job Opportunities project | 13 Sep 2026 |
| Backend-first development approach | **This project** — where the audits were consolidated and `spec-addendum-v1.md` was produced | 13 Sep 2026 |
| Personal AI Assistant | **This project** (moved in 14 Sep 2026; was standalone). The knowledge-harvest work: extracting past conversations into markdown for the corpus | through 5 Aug 2026 |

## 3. Open decisions

- **Fold `spec-addendum-v1.md` into `personal-ai-assistant-spec.md` as v1.1.** The addendum's own closing line says to do this before resuming Stage 0. Not done yet.
- **Do B.4 (state-objects table) and C.1 (forced session-start injection) land in the thin slice, or get pushed out?** Both are new engineering rather than config on top of the existing stages. Raised at the end of the Backend-first conversation, not resolved.

## 4. Settled: no outsourcing

**Decided 14 Sep 2026 — none of this build is being contracted out. Scott builds all of it himself, with Claude Code.**

Consequences, in case earlier material reads otherwise:

- Any reference to *"the contracted 40%"* (Backend-first conversation, 13 Sep 2026) is dead. There is no contracted portion.
- `hiring-kit.md` — the contracting playbook (job post, screening questions, paid trial task, milestone/payment structure, contractor access matrix and offboarding checklist) — was removed from project knowledge on 14 Sep 2026. It is not archived elsewhere. If a hiring kit is ever needed again it gets rebuilt, not recovered.
- The B.4 / C.1 scope question changes shape: the argument for keeping them in the thin slice was *"these are the load-bearing pieces you want to have built yourself."* With nothing being outsourced, that distinction no longer decides anything — the only remaining question is sequencing, not ownership.

## 5. Where the project's standing instructions actually live

The stack, the "Settled — do not re-open" list, the spend cap, the working-style rules and the DECISIONS.md rule are all in the project **Description**, not the **Instructions** field — Instructions is empty. Verified 14 Sep 2026 that the Description does reach chats in the project: a fresh chat asked for the spend cap answered "$300/month hard cap, $150 alert threshold" with no other context. Leave it where it is; just don't go looking for it under Instructions.

## 6. Corpus / repo

- Notes repo: `C:\Users\scott\Dev\notes`
- Harvested markdown lands in `_raw\`, then is split with `python split_harvest.py "_raw\<name>-all.md" <slug>`
- Harvest completed for: Business Ops (39 conversations, 12 Jun – 5 Aug 2026, 222 note files), Manila Inside Sales, Watts Way Farms
- Decisions made in project conversations get written to `DECISIONS.md` in the repo
