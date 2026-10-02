# Harvest Playbook — building Kilo's corpus from Claude.ai history

**What this is:** the repeatable procedure for extracting durable knowledge out of a Claude.ai Project and into the notes repo that Kilo will index. Run once per project. Preserved here because the procedure and its guardrails were worked out in conversation and existed nowhere else.

**Origin:** the "Personal AI Assistant" conversation (in this project, Aug 2026).

---

## 1. Why the corpus is built this way

The point of the five-category split is that it separates **what Scott decided** from **what Claude proposed**. A corpus that blurs the two will, on retrieval, hand back Claude's own old suggestions as though they were standing decisions — the exact failure the whole build exists to avoid. Hence the hard rule in the prompt: *only record things I said or decided; anything you proposed, recommended, drafted, or suggested is NOT mine unless I explicitly adopted it.*

Splitting output into many small files rather than one document is deliberate: retrieval works better on focused chunks, so a query about one topic doesn't drag in unrelated contract terms.

---

## 2. The harvest prompt

Start a **new chat inside the project being harvested** and paste everything below the line. Replace the filename on the second-to-last paragraph with `<project-slug>-all.md`.

---

Search this entire project's history — every conversation, oldest to newest — and extract everything worth preserving, in five categories.

Critical distinction throughout: only record things I said or decided. Anything you proposed, recommended, drafted, or suggested is NOT mine unless I explicitly adopted it. If unsure, mark it [UNCERTAIN] rather than omitting it — I'll judge.

Use exactly these formats, keeping all markdown symbols:

**Category 1 — Decisions and rejections**

```
FILE: slug-here.md

# Title

**Decided:** what I decided.

**Why:** my reasoning.

**Rejected alternatives:** what was set aside, and why.

**Would revisit if:** the condition that would reopen it.

**Approx date:** month and year, or "unknown".
```

**Category 2 — Facts, figures, constraints**

```
FILE: slug-here.md

# Title

Fact, stated plainly.
Another related fact.

**Approx date:** month and year, or "unknown".
```

Only facts I supplied. Exclude anything you researched, calculated, or estimated.

**Category 3 — Preferences and working style**

```
FILE: preferences-slug.md

# Title

The preference, stated as an instruction.
```

Only things I actually said. Do not infer from behavior patterns.

**Category 4 — Open threads**

```
FILE: open-slug.md

# Thread name

**Status:** where it stands.

**Open questions:** what's undecided.

**Blocked on:** what it's waiting for.

**Last activity:** approximate date.
```

Mark abandoned threads `[DORMANT]` in the title.

**Category 5 — Corrections and reversals**

```
FILE: correction-slug.md

# Title

**What was wrong:** the incorrect version.

**Correct version:** what's actually true.

**Approx date:** month and year, or "unknown".
```

Include stylistic corrections, not just factual ones.

Rules: one item per block, never merge. Include small items — err heavily toward too much. Include decisions later reversed, as separate items. No editorializing or advice.

Write the results directly into a downloadable markdown file named `<project-slug>-all.md`, appending to it as you go, rather than printing them in chat. Only tell me in chat when you've hit a limit or finished.

Do not stop between categories or ask permission to continue. Work through all five continuously until you hit your output limit. If you run out of room, stop and I'll say "continue" — resume exactly where you stopped, no repeating and no re-summarizing what you already covered.

---

## 3. Splitting the output

Download the produced `-all.md`, drop it in `_raw\`, then:

```
cd /d C:\Users\scott\Dev\notes
python split_harvest.py "_raw\<project-slug>-all.md" <project-slug>
```

The splitter reads the `FILE:` markers and writes one markdown file per block into `<project-slug>\`.

---

## 4. Corpus status

Repo: `C:\Users\scott\Dev\notes`

Harvested directories present: `business-ops`, `farm-concrete`, `fitness-training`, `home-pool`, `manila-sales`, `watts-way-farms`, `wattsway-app`. Plus `kilo` (this project's own docs) and `_raw`.

Known detail: the Business Ops harvest covered 39 conversations spanning 12 June – 5 August 2026 and produced 222 note files. **Use 5 August 2026 as the baseline date for a Business Ops delta harvest** — anything after that has not been captured.

Everything harvested before mid-September 2026 predates the three systems audits and `spec-addendum-v1.md`; those live in this project's knowledge files, not in the corpus.

---

## 5. Two guardrails that survive into the build

### 5.1 The employer data boundary

**Personal, farm, and pre-formation venture material goes on Scott's own stack. Day-job data stays in sanctioned tooling.**

The reasoning, from the origin conversation: a Cox employee during a Charter merger who ingests Blueprint RF operational data, brand contracts, Cloudstaff cost detail, or anything merger-adjacent into personal infrastructure has created an unmanaged repository of employer data outside retention policy and outside any legal hold. That is a materially different category of risk from the tooling limits the build is meant to solve. Connecting the two is a conversation with Cox IT/security, not a weekend project.

This constraint is also the reason `business-ops` and `job-search` are specified as physically separate stores (spec §4.4), and why the job-search store is out of scope for any third party entirely.

### 5.2 Corrections are preserved, not cleaned up

Category 5 exists because reversals are load-bearing. A corrected fact and the correction that produced it are both worth indexing — the correction is what stops the old version being retrieved as current later. The same instinct appears in the addendum as `superseded_by` and write-time reconciliation (`spec-addendum-v1.md` §D.1). Don't let a future tidy-up pass collapse them.

### 5.3 A marker worth keeping

Pending items get recorded as pending, not resolved. From the Manila harvest: a reporting-structure decision was held as `PENDING` because it genuinely hadn't been made, and a commission-earnings observation was kept framed as a hypothesis rather than a finding — *"it's the highest-value open item precisely because it isn't answered yet."* When the decision later landed, the harvest files were updated and the now-obsolete constraint was removed. That update cycle is part of the procedure, not an afterthought.
