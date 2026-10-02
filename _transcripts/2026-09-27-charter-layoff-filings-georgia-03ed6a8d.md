# Charter layoff filings Georgia
Date: 2026-09-27
Conversation: 03ed6a8d-edf6-4d68-8612-31ccdce01d0d
Domain: business-ops

## Summary
**Conversation Overview**

The person is researching WARN Act filings related to the Charter Communications acquisition of Cox Communications, with a specific focus on Georgia. They asked Claude to find the Georgia WARN notice portal, then to search for any filings tied to Charter, Spectrum, or Cox entities. Claude identified the official Georgia portal as WorkSourceGeorgia.com/WARN (administered by the Technical College System of Georgia's Office of Workforce Development since 2023) and clarified that Georgia follows the federal 60-day notice rule, not a 90-day state requirement. No current Georgia WARN filings were found for Charter, Spectrum, Cox Communications, or Cox Automotive, though the official state portal returned a 404 during Claude's fetch attempts.

The person then requested a daily automated monitoring task for all related entities. Claude set up a cloud-based scheduled agent named "Daily WARN watch – Charter/Cox" running at 7:50 AM Eastern every day. The agent checks Charter Communications, Charter Communications Operating LLC, Spectrum, Cox Communications, CoxCom LLC, Cox Enterprises, Cox Automotive and its subsidiaries (Manheim, Autotrader, Kelley Blue Book), Cox Media, and Blueprint RF. Sources include WARNTracker, Layoff Lookout's Georgia page, the official WorkSourceGeorgia list, and recent news searches. Alerts fire only when new notices are found; silent days produce no notification. Known baseline notices from 2026 and earlier were documented so the agent does not re-alert on them.

**Tool Knowledge**

WebFetch on WorkSourceGeorgia.com/WARN consistently returned a 404; WARNTracker and Layoff Lookout proved more reliable for fetching Georgia WARN data. WARNTracker entity pages follow the pattern `warntracker.com/company/[entity-slug]` (e.g., `/company/cox-communications`, `/company/charter-communications`, `/company/cox-automotive`) and successfully returned structured notice data. The scheduled trigger was created using `mcp__claude-code-remote__create_trigger` with `cron_expression: CRON_TZ=America/New_York 50 7 * * *`, `initiation: human_request`, and `notifications: {push: True, email: True}`. The trigger was submitted twice due to an apparent parameter issue on the first attempt.

### SCOTT (2026-09-27T15:06)
There’s a website where big company have to file public notice 90 days in advance of layoffs. Can you find the website address for ga?

### CLAUDE (2026-09-27T15:07)

Georgia's WARN filings live at **www.WorkSourceGeorgia.com/WARN**. Since January 1, 2023, the state's Rapid Response services, which include WARN, have been run by the Technical College System of Georgia's Office of Workforce Development. The old GDOL listing still turns up in search results, but that page is no longer updated and only covers layoffs through June 2013.

One correction: Georgia doesn't require 90 days' notice. It has no state mini-WARN law, so only the federal 60-day rule applies. New York is the state known for 90 days. If you'd rather search Georgia notices than use the state portal, layoffdata.com has searchable Georgia WARN data back to January 2023.

Sources:
- [Rapid Response | Georgia Department of Labor](https://dol.georgia.gov/blog/rapid-response)
- [GDOL WARN Notices (legacy)](https://www.dol.state.ga.us/Access/Service/WarnIDListingInput)
- [WARNTracker – Georgia](https://www.warntracker.com/?state=GA)
- [Georgia WARN Act Layoff Notices | WARN Database](https://layoffdata.com/georgia/)

### SCOTT (2026-09-27T15:08)
Are you able to access that site and check for any filings related to Charter, spectrum?

### CLAUDE (2026-09-27T15:09)

I found no Georgia WARN filings for Charter or Spectrum. I couldn't read the state portal itself because the WorkSourceGeorgia WARN page returned a 404 to my fetch tool. So this answer comes from WARNTracker, which compiles the public state records.

**Charter's WARN history:** 51 notices from 2004 through September 2026 across 20 states. None are in Georgia. The three most recent in 2026:

| Filed | State | City | Workers | Layoff date |
|---|---|---|---|---|
| Jul 8 | MO | Town & Country | 107 | Sep 8 |
| Mar 18 | WI | Appleton | 313 | Jun 21 |
| Mar 5 | SC | West Columbia | 62 | May 7 |

The Missouri notice shuts down a network operations center. The layoffs are mostly network engineers and upper management, and Spectrum says no customer-facing roles are affected.

There are two gaps in this check:
- **Aggregator lag.** A notice filed in the last few weeks may not show up yet.
- **Filing entity.** After the merger, Georgia cuts could be filed under a Cox entity rather than "Charter." Cox's Atlanta HQ makes that the more likely name to watch. I only searched Charter and Spectrum.

I can search Cox entity filings next, or open the Georgia portal in your browser to check it directly.

Sources:
- [WARNTracker – Charter Communications](https://www.warntracker.com/company/charter-communications)
- [FOX 2 – Charter Town and Country layoffs](https://fox2now.com/news/missouri/charter-to-close-town-and-country-office-107-layoffs-planned/)

### SCOTT (2026-09-27T15:10)
Yes

### CLAUDE (2026-09-27T15:10)

No Georgia WARN filings turned up for any Cox entity tied to the merger. The most recent Cox Communications WARN notice anywhere was filed in February 2015.

| Entity | Georgia filings | Most recent notice (any state) |
|---|---|---|
| Cox Communications | 2 (Macon 2010, 71 workers; Atlanta 2012, 133) | Feb 2015, Rhode Island |
| Charter / Spectrum | None | Jul 2026, Missouri (107) |
| Cox Automotive (a Cox Enterprises company, not part of the Charter deal) | 5, all Atlanta-area COVID cuts in May 2020 | Apr 2026, Bel Air, MD (70) |

So nothing public signals a Georgia mass layoff from the integration yet. That's weaker evidence than it looks, for three reasons:

- **Reporting lag.** WARNTracker (and a second aggregator, Layoff Lookout) can run weeks behind the state. Some Georgia aggregators hold notices for up to 6 months unless you pay.
- **Thresholds.** WARN only applies to 50+ workers at a single site. Integration cuts spread across teams, remote staff, or several sites often never trigger a filing.
- **Filing entity.** A notice could be filed under a legal entity name like "CoxCom, LLC" or "Charter Communications Operating, LLC." Aggregators sometimes don't roll those up under the parent company.

I still haven't checked the official Georgia list. My fetch tool got a 404 from the state portal, and opening it in a browser needs the Claude desktop app running on your computer. The fastest route is to open www.WorkSourceGeorgia.com/WARN yourself and search "Cox" and "Charter." I can walk through it with you from the desktop app if you'd rather.

Sources:
- [WARNTracker – Cox Communications](https://www.warntracker.com/company/cox-communications)
- [WARNTracker – Cox Automotive](https://www.warntracker.com/company/cox-automotive)
- [WARNTracker – Charter Communications](https://www.warntracker.com/company/charter-communications)
- [Layoff Lookout – Georgia](https://www.layofflookout.com/warn-notices/georgia)

### SCOTT (2026-09-27T15:11)
From the desktop app are you able to set up an agent where you check this everyday for all related entities and then alert me if anything comes up?

### CLAUDE (2026-09-27T15:11)
Yes, and it doesn't need the desktop app. I can set up a daily scheduled task from here. Each run would check every related entity (Charter, Spectrum, Cox Communications, CoxCom, Cox Enterprises, Cox Automotive, Cox Media) and send you a push or email alert only when a new notice appears.

The one real decision is where it runs:

- **Cloud (recommended):** runs every day no matter what, but checks the aggregators (WARNTracker, Layoff Lookout, news) rather than the official Georgia list. The risk is a lag of days to weeks behind the state.
- **Your computer:** opens the official WorkSourceGeorgia list in the browser, so it's closest to the source. It only runs when your computer is on, awake, and has the Claude app open, and a missed day just gets skipped.

A cheap backstop either way is WARNTracker's free email alerts, which you can set for Charter and Cox yourself.

Which one do you want, and what time should the daily check run? I'd suggest around 7:50 AM Eastern.

### SCOTT (2026-09-27T15:13)
Let’s go with your recommendation and time

### CLAUDE (2026-09-27T15:13)

I've set up a scheduled task called "Daily WARN watch – Charter/Cox." It runs every day at 7:50 AM Eastern in the cloud, and the first run is tomorrow morning.

**What each run does:**
- **Checks:** Charter, Spectrum, Cox Communications/CoxCom, Cox Enterprises, Cox Automotive, Cox Media and Blueprint RF.
- **Sources:** WARNTracker, Layoff Lookout's Georgia page, the official WorkSourceGeorgia list, and recent news.
- **What it skips:** the notices we already found today, so you're only alerted on new ones.
- **What counts as an alert:** a notice filed in the last 7 days, with Georgia listed first. It also flags credible Georgia layoff news even when no WARN notice has been filed, labeled as news-only.
- **Notifications:** you'll get push and email only when something new turns up. Quiet days send nothing.

The task wasn't set to approve actions automatically, so a run will stop if any step needs your approval. You can switch it to "Automatically approve" in the task's settings if your organization allows it.

Its biggest weakness is still aggregator lag. If a run can't reach the official Georgia list, it will say so in the alert.
