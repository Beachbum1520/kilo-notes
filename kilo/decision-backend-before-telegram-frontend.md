# Build retrieval before the Telegram front end

**Decided:** Scott accepted building the back end first (ingest, hybrid search, answer assembly, then eval) and not the Telegram front end first ("Ok. Fair.").

**Why:** The argument Scott accepted: a front end with no retrieval behind it is just Telegram wired to stock Claude. Ingest is hands-on chunking work, not a background data copy. Retrieval quality has to be inspected directly, not through a chat interface.

**Rejected alternatives:** Scott's suggestion of building the front end first, so he could start using it to some degree while data from the other projects was being copied over.

**Would revisit if:** Not stated.

**Approx date:** September 2026

**Source:** Backend-first development approach, 2026-09-13
