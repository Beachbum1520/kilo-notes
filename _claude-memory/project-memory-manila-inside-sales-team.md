# Claude project memory: Manila Inside Sales Team

**Purpose & context**

Scott is working within a Claude.ai project focused on a Manila-based inside sales context. He has a strong orientation toward structured knowledge management — extracting, categorizing, and preserving information from conversation history in a rigorous, well-formatted way. His goals emphasize clean provenance (distinguishing what he explicitly decided vs. what was proposed to him), precision in labeling uncertainty, and producing outputs as downloadable artifacts rather than inline chat responses.

**Current state**

The project is in early stages — as of the most recent conversation, no prior conversation history existed beyond a reference dossier. A key unresolved issue: the existing dossier conflates Scott's confirmed decisions with pending items and recommendations made *to* him, making it difficult to extract knowledge cleanly under his provenance rules without risking mislabeling. Two options were presented: (1) wait until real conversation history accumulates, or (2) mine the dossier with explicit per-item confidence tagging. Scott's choice between these was not yet captured.

**Key learnings & principles**

- Provenance discipline matters to Scott: only attribute decisions or facts to him when he explicitly stated or decided them — proposals and recommendations should not be labeled as his settled positions.
- Uncertainty should be surfaced with explicit tagging (e.g., `[UNCERTAIN]`) rather than omitted or glossed over.
- When project history is absent, all retrieval methods return null — the correct interpretation is no history exists, not inaccessible data.
- Mixed-provenance documents (like a dossier blending decisions and recommendations) require explicit handling strategy before extraction can begin cleanly.

**Approach & patterns**

- Scott works with highly specific formatting and structural requirements: named fields, exact file naming conventions, defined output destinations, and clear category schemas.
- Prefers continuous, uninterrupted execution (working through multi-step tasks without pausing for permission at each stage).
- Outputs should go to downloadable markdown files rather than appearing inline in chat.
- Decision extraction follows a five-category framework: decisions and rejections, facts and constraints, preferences and working style, open threads, and corrections and reversals.