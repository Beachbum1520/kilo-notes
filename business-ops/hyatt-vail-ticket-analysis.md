# Grand Hyatt Vail — ticket and infrastructure analysis findings

NOC six-month review: 33 total tickets to date; 11 (33%) and the firewall reboot traced to an ISP interruption from a past-due balance on the property's Lumen account (ZD 1224947, March 30, 2026).
205 of 210 APs had the same uptime as the FortiGate firewall, suggesting a power issue.
Circuit conversion (secondary circuit, ticket 782191) completed.
Fast Roaming and Airtime Decongestion enabled on 2.4GHz and holding.
Both Nomadix servers updated to firmware v9.7.053, BPRF's recommended version.
3 APs remained offline (ZD 823343), worked by PNOC.
False Cosmos alerts fixed by changing Nomadix IPs in Salesforce Installed Equipment from public to private; Cosmos–Salesforce sync takes 24 hours.
Switch reboot after hours to be coordinated (ZD 1410397).
NOC dashboard cannot generate bandwidth utilization for this property due to Nomadix configuration, so 1Gig circuit performance cannot be confirmed remotely; team was working with Nomadix on remote validation.
Kyle Davis asked Scott whether to approve an FOC dispatch to test the circuit.
Sharmie was pulling connection counts to calculate the TvU ratio.
Hotel's POS Wi-Fi network from before the 2024/25 implementation was not carried forward; needed for pool service tablets.

**Approx date:** April 2026

**Source:** Hyatt Vail EGEGH escalation threads (attached to "Hyatt Vail - EGEGH - Escalation"), 2026-04-23
