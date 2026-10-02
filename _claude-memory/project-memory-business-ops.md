# Claude project memory: Business Ops

**Purpose & context**

Scott Watts is Senior Director of Hospitality Operations at Blueprint RF (BPRF), a managed Wi-Fi and hospitality technology LAN Service Provider (LSP) serving 2,600+ hotels across major brands including Marriott, Hilton, Hyatt, Choice, Omni, and Wyndham. BPRF operates as a separately branded subsidiary within the Charter/Spectrum ecosystem following the Cox/Charter merger close. Scott oversees NOC, PNOC, TDE (Technical Deployment Engineers), and Philippines-based offshore teams (~40 headcount through two BPOs), plus vendor relationships, brand certifications, and cross-functional operations.

**Key people:**
- **Jady West** (he/him) — Scott's manager; Senior Director post-merger with verbal VP promise; conflict-averse; political escalations and SLA credit approvals route through him
- **Kathy Hatala** — peer Senior Director of Sales; same title and manager as Scott; can be territorial; keep her off sponsor/stakeholder lines on documents Scott controls
- **Kyle Davis** — Manager, Customer Support / NOC; direct report; senior Philippines presence
- **Marie Henson** — TDE Supervisor; direct report; Philippines-based
- **Julian Cayetano** — Manager, Sales Engineering / Brand Support; direct report
- **Dan Apa** — Manager, Software Development; direct report; building the network monitoring platform replacement
- **Par Bayat** — Marriott brand manager; reports to Scott; long-standing relationship
- **Mary Rose** (also "MR" — shorthand strictly between Scott and Claude only, never external) — Office Administrator, Cloudstaff Cebu; oversees SLA report completeness/accuracy with escalation authority to Scott
- **Melvin Palma** — Cloudstaff account manager
- **Josh** (CallTek CGO) — adversarial; prone to bypassing Scott and escalating to Jady
- **Jady's boss chain** — Mark Kornegay is above Jady; Brian Miller and Chris Fulton are SVP-level Spectrum contacts
- **Eric Nowak** — Sr. Director, Managed Services, Spectrum; Scott's peer-level operational counterpart
- **Bob Schroeder** — GVP, Business Technical Sales, Spectrum; calibrate tone as Sr. Director writing to GVP

**BPO structure:**
- **CallTek (CTC)** — primary call center and NOC/Tier 3/PNOC provider; contentious relationship; exit strategy in development
- **Cloudstaff (CS)** — network engineers, TDE, brand/sales roles; preferred vendor; Lloyd (CEO), Melvin (account rep), Jamar (leadership)
- **PEBL** — third vendor for Kyle Davis, Marie Henson (independent of other BPOs), and one Guatemala-based TDE (Bayron)

**Active brand/platform constraints:**
- Per Legal (July 2026): gateway product must be called **"DG2" only** — "Dominion Gateway," "Dominion Platform," and all prior naming conventions are superseded for trademark reasons; DG3 must never appear in external or forwardable material
- **Cosmos** and **CAS** must never be named in external-facing materials (decks, collateral, RFPs) — use generic functional labels (e.g., "network monitoring platform"); Dan's team is actively building a replacement
- "BPRF," "Spectrum," and "Charter" have specific usage contexts — not interchangeable; "Cox" is legacy pre-merger
- **ORCA** — Marriott's RFP/approved vendor platform; pronounced "OR-KAH"; covers GPNS tiers (Basic, Full, EBIO), GRE&T, and conference services

---

**Current state**

**CallTek exit strategy:** Scott and Jady concluded the relationship warrants building an exit. Scott's posture with Josh is cordial and non-committal ("grin-fuck") to avoid tipping the plan. Discussions with Cloudstaff (Melvin, Jamar) ongoing for moving ~40 NOC/PNOC headcount. Cloudstaff currently lacks a managed services model for Tier 1/Tier 2 guest Wi-Fi support — a separate BPO (e.g., Connectys) may be needed for that piece. CallTek disputes documented: MSA 5.2.1 Key Personnel violation (Alison), contractual basis review of Josh's demands (all three demands unsupported), recording policy violation (Read AI), QA monitoring deficiencies.

**Spectrum integration:** 58 Spectrum sellers activated across two major hospitality brands; growth continuing. Scott posted additional TDE roles at Cloudstaff. Salesforce source-of-truth dispute with Erik Nowak: BPRF Salesforce is authoritative for opportunity counts, not Spectrum's instance.

**Vendor / BPO operations:**
- Mary Rose established as Office Administrator, Cloudstaff Cebu; dotted-line to Kyle Davis and Marie Henson (both can task her directly); performance management stays with Scott; sits below Kyle and Marie in scope/seniority; Mariane (Project Administrator) sits below Mary Rose
- RJ/Jenna (former PNOC Lead): withdrew Cloudstaff offer due to CallTek non-compete — CTC-employee contract matter, not BPRF/Spectrum issue
- Sharmie (Cebu CS, brand manager): ongoing site-admin matter now under Mary Rose's purview; Julian is functional manager despite Atlanta location

**Active client matters:**
- **MBM Legacy / Hilton Fayetteville** (FAYFB, FAYNH): service disconnection dispute and unauthorized Work Order alterations; demand letter process ongoing
- **Grand Hyatt Vail**: 68-day monitoring suppression failure documented; fleet-wide Nomadix audit commitment extracted from CallTek's own RCA; formal demands issued in writing
- **Bluegreen**: fiber break/network outage; reimbursement request declined via scope-framing; Monday call deferral approach
- **Hyatt Place SF (SFOZS)**: $60K installation billing dispute; 2.4 GHz at 40 MHz config error confirmed as legitimate miss; invoice dispute kept factually separate from config remediation

**Merger/org context:** Scott and Jady hold same Senior Director title post-merger; VP roles expected in a January reorg. Scott positioning carefully — controls capacity model and narrative. Jady's boss is Mark Kornegay; Jady's boss's boss chain reaches Chris Winfrey.

**Contractor/IT access:** Cox MyID system failure caused contractor account expirations; INC13726266 open; blueprintrf.com domain migration to Charter/Spectrum tenant in progress — end state is @blueprintrf.com as primary, @spectrum.com/@charter.com as aliases. Marriott/Hilton/Hyatt brand certifications are tied to the blueprintrf.com domain — customer-facing infrastructure, not internal tooling.

**Hilton compliance:** Two General Warnings received; formal response submitted; JP (Cloudstaff, Cebu) removed from account under Section 7 of Cloudstaff MSA for unauthorized access provisioning (Warren Medellin re-added after Hilton revoked his access). MFA audit commitment (Section 4.1) needed verification by Marie with Corey before submission.

---

**On the horizon**

- CallTek full exit execution: resolving Tier 1/Tier 2 guest Wi-Fi BPO gap before transition
- Marriott GRE&T RFP: clarification phase complete (17 questions submitted); full proposal response is open work item; Scott holds 10% SLA credit cap (Option 1) with Jady as approval gate for any movement to 50%
- Choice Hotels HSIA RFP: corporate-level brand-standard designation would resolve property-by-property ETF issue from the top down
- Hyatt dashboard rollout: paused pending Julian's return; end of September was always a target, not a hard commitment
- January reorg: VP role positioning; Scott controls capacity model and is deliberate about what Jady sees and when
- Omni Hotels: no-cost IRE POC proposed at New Orleans property (active Wi-Fi install); Gustaaf (Omni CIO) expressed interest; follow-up pending
- Philippines trip: twice-yearly cadence established; BPOs cover flight costs; pending approval cadence with Jady post-merger

---

**Key learnings & principles**

- **Written record discipline:** Keep politically sensitive assessments, exit intent, motive characterizations, and attribution of underperformance verbal. Written communications should be professional, factual, and forwardable. Scott creates paper trail through what he puts on record — not through what he says aloud.
- **Jady as approval gate:** Route SLA credits, CEO-level escalations, formal breach declarations, comp decisions, and politically sensitive moves through Jady before acting. Brief Jady before CTC or other vendors shape their version of events.
- **Avoid creating openings:** Don't volunteer information that invites scrutiny, don't pre-commit to economics before leadership alignment, don't over-explain settled points on live threads, don't reference Cosmos/CAS or DG3 externally.
- **Contractual grounding:** Cite specific MSA/SOW sections in vendor communications. Non-solicitation clause MSA 13.19 runs one direction (CallTek cannot poach BPRF employees). Josh's three demands have no contractual basis. CallTek's QA obligations (Section 2.6) have been in breach since April 2025.
- **Scope framing over hard refusals:** When declining reimbursement or credits on multi-stakeholder threads, frame around scope boundaries rather than putting a flat refusal in writing.
- **Don't throw the team under the bus:** External communications should protect the team's narrative; never expose internal process failures to outside parties.
- **Kathy dynamics:** Frame communications as informing not asking; never give her a veto; keep her off sponsor lines on Scott's documents; don't engage on rules-of-engagement debates.
- **LSP accountability principle:** As the LSP, BPRF is accountable for everything running on the network. "We don't get to define the market, we just decide if we want to participate."
- **New build vs. upgrade design:** New build design is lighter than upgrade work because the LV vendor handles cabling and rack work.

---

**Approach & patterns**

- **Communication register:** Direct and informal when working with Claude; professional and audience-calibrated for external output. Writes differently for Jady, Kathy, GVPs, clients, and BPO partners. Adjusts formality based on whether content is likely to be forwarded.
- **Email construction:** Single polished drafts preferred over multiple variants. Bottom-line-up-front structure. Numbered items for traceability on complex issues. Named individuals and specific contract citations on the record when building accountability. Never recap context the recipient already knows.
- **Typo tolerance:** Scott types quickly with significant typos and expects Claude to interpret and clean up without flagging each error.
- **Terse correction style:** Corrections are phrase-by-phrase and direct; no re-litigation. Claude should accept and apply corrections without extended acknowledgment.
- **Strategic information sequencing:** What goes in writing vs. stays verbal is a deliberate decision. AirAngel/gateway-timing rationale, exit intent, political reads on colleagues — all verbal only. Forwardability is always a test applied to outgoing drafts.
- **Capacity and modeling:** Scott controls the capacity model and the narrative it produces; does not share the model preemptively ahead of the reorg.
- **Search patterns:** Combining specific proper nouns (vendor names, people, deal names) with task type (audit, reconciliation, RFP) produces better conversation search results than broad topic terms. Parallel multi-query searches surface more than single broad queries.

---

**Tools & resources**

- **Platforms in use (no external live access):** Salesforce (BPRF instance is authoritative), Zendesk (ticketing only), Field Nation, Workday, Microsoft Teams (primary async comms with Philippines teams), Outlook (dual mailbox: scott.watts@blueprintrf.com primary + scott.watts1@spectrum.com)
- **File tools used in this project:** openpyxl (Excel), python-docx / docx Node.js library (Word), PptxGenJS (PowerPoint), pandoc/pdftotext (document extraction), markitdown (PPTX text extraction), extract-msg (Outlook .msg files), xlrd+pandas (legacy .xls files), bash/Python for quantitative analysis
- **OOO routing structure (established template):** Kyle Davis — Call Center Ops/NOC/PNOC/Dispatch; Dan Apa — Software Development; Julian Cayetano — Hotel Brand Support/Sales Engineering; Marie Henson — Technical Deployment Engineers. Email format: firstname.lastname@blueprintrf.com