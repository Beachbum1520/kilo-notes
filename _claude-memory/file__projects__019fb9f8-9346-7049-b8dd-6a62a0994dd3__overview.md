---
name: overview
description: Purpose, current state, and working conventions for Scott's Manila-based inside sales knowledge-extraction project
sources: [backfill]
aliases: []
---

## Purpose & context

- [stated] The project centers on a Manila-based inside sales context.
- [stated] Scott's aim is structured knowledge management — extracting, categorizing, and preserving information from conversation history in a rigorous, well-formatted way.
- [stated] Clean provenance is a core goal: distinguishing what Scott explicitly decided from what was merely proposed to him.
- [stated] Precision in labeling uncertainty is a stated goal.
- [stated] Outputs should be produced as downloadable artifacts rather than inline chat responses.

## Current state

- [stated] The project is in early stages — as of the most recent conversation, no prior conversation history existed beyond a reference dossier.
- [stated] Open issue: the existing dossier conflates Scott's confirmed decisions with pending items and recommendations made *to* him, making clean extraction under his provenance rules risky (mislabeling).
- [stated] Two options were presented for handling this: (1) wait until real conversation history accumulates, or (2) mine the dossier with explicit per-item confidence tagging.
- [stated] Scott's choice between those two options was not yet captured — this remains an open question.

## Key learnings & principles

- [stated] Provenance discipline: only attribute decisions or facts to Scott when he explicitly stated or decided them; proposals and recommendations must not be labeled as his settled positions.
- [stated] Surface uncertainty with explicit tagging (e.g. `[UNCERTAIN]`) rather than omitting or glossing over it.
- [stated] When project history is absent, all retrieval methods return null — the correct interpretation is that no history exists, not that data is inaccessible.
- [stated] Mixed-provenance documents (a dossier blending decisions and recommendations) require an explicit handling strategy before extraction can begin cleanly.

## Approach & patterns

- [stated] Scott works with highly specific formatting and structural requirements: named fields, exact file naming conventions, defined output destinations, and clear category schemas.
- [stated] Prefers continuous, uninterrupted execution — working through multi-step tasks without pausing for permission at each stage.
- [stated] Outputs go to downloadable markdown files rather than appearing inline in chat.
- [stated] Decision extraction follows a five-category framework: decisions and rejections; facts and constraints; preferences and working style; open threads; corrections and reversals.