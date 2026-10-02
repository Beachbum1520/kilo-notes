# Grand Hyatt Vail — Cosmos proactive monitoring failure (July 2026)

Uplink/switch flapping at Grand Hyatt Vail caused a large recurring group event to repeatedly lose Internet; no proactive alert or response from BPRF.
The hotel owner credited $10K back to the group and faced a board meeting to try to recover the group; hotel sought reimbursement from BPRF, credits for tech dispatches, and payment for infrastructure repairs.
Scott's position: lack of contracted proactive monitoring and alerting is the root cause of the escalation; BPRF failed the MSA proactive monitoring requirement for Hyatt, even if the flapping was hotel infrastructure.
CallTek (Alison Perales) RCA: Cosmos default rule requires 5-minute polling cycles and 3 consecutive cycles (15 minutes) to trigger a ticket; the flapping switch never stayed down long enough; ticket generation also failed for two AP drops. Staff reported issues on 7/15; NOC found missing configs, CRC errors, and fiber/SFP issues.
OAB tool handles SF–Cosmos sync, ticketing toggle, and Cosmos agent deployment; TDE handles Cosmos deployments during projects, PNOC/NOC on server replacements; deployment failures escalate to BPRF Dev team (Cosmos group).

**Approx date:** July 2026

**Source:** Cosmos escalation thread (attached to "Hyatt Grand Vail conversation"), 2026-07-22
