# Alinea's expensive wealth management pricing
Date: 2026-07-26
Conversation: bec6fb19-c5d1-413e-b1be-de314d3eac2b
Domain: skip

## Summary
**Conversation Overview**

The person shared an investing app (Alinea) for Claude's assessment, apparently having encountered it through a Facebook in-app browser advertisement. The conversation focused on evaluating the app's fee structure, credibility, and value proposition for beginner investors. Claude provided a detailed critique covering Alinea's pricing model, regulatory legitimacy (SEC-registered, DriveWealth/FINRA/SIPC-backed), and skepticism toward its AI-driven marketing claims, concluding that the fees were disproportionate for small account holders relative to alternatives.

The person then challenged Claude's characterization of Schwab Intelligent Portfolios as "free," prompting Claude to correct the oversimplification. Claude acknowledged that Schwab's zero-advisory-fee model is monetized through mandatory cash drag on a portion of the portfolio, explained the effective cost implications, noted the $5,000 minimum that makes it inaccessible to Alinea's target demographic, and referenced Schwab's 2022 SEC settlement over these disclosure practices. Claude identified Fidelity Go as a cleaner comparison it should have used originally.

The person demonstrated a pattern of close reading and willingness to push back on imprecise claims, and Claude responded by fully owning the error and providing a more rigorous analysis rather than hedging. No personal financial details or investment goals were shared by the person. Domain terminology used included: expense ratio, cash drag, tax-loss harvesting, roboadvisor, SIPC, FINRA, SEC-registered investment advisor, alpha, and three-fund index portfolio.

### SCOTT (2026-07-26T09:54)
What do you think of this app?
[File uploaded: b7ac10ce65cc735bb9c0e6f8a51a0da69142b77b.png]

### CLAUDE (2026-07-26T09:55)

Structurally legit, economically bad for most people, and the marketing is the tell.

**The math is the problem.** Alinea charges $120/year for its wealth management service after a 7-day trial, with no refunds and auto-renewal until cancelled. That's a flat fee, so the effective expense ratio scales inversely with account size — 2.4% on $5k, 1.2% on $10k. Betterment and Wealthfront run ~0.25%; Schwab Intelligent Portfolios is free. Reviewers have flagged that the fee is a significant percentage of a beginner's portfolio for what is essentially a basic taxable brokerage account without retirement options. There are also references to a $5/month charge on automated investments over $100 and a 1% fee above $6,000, which is a different pricing story than the flat $120 — opaque pricing is itself a signal.

**The credentials are real.** It's an SEC-registered investment advisor with brokerage powered by DriveWealth, a FINRA/SIPC member. So it's not a scam. But SIPC covers custodian failure, not bad allocation or fee drag.

**What I'd actually push back on:**
- "Don't invest. We'll do it for you." sells abdication, not delegation. The demographic paying $120/yr is precisely the one that can least afford it and most needs to understand what it owns.
- The "AI trades" framing is almost certainly a veneer over standard questionnaire → risk bucket → ETF allocation. The AI layer, "Allie," is described as a copilot delivering plain-language recaps and portfolio insights — that's an explainer chatbot, not an alpha engine.
- Recurring user complaints involve fees not clearly disclosed at signup and difficulty withdrawing funds, and reports of trouble cancelling before auto-renewal. A 4.8 from 101k ratings in a category with aggressive in-app review prompting isn't strong evidence against that.
- You saw this in a Facebook in-app browser. #34 in Finance on paid social acquisition means the customer acquisition cost is being recovered from that subscription fee. Follow the money.

Not financial advice, and I don't know your situation — but for anyone with real capital, a three-fund index portfolio at a zero-fee brokerage does the same job better. Where this app could earn its keep is behavioral: getting someone from $0 invested to $200/month invested is worth more than 2% of a small balance. That's a narrow case, and it's not yours.

### SCOTT (2026-07-26T09:56)
What is this:

Schwab Intelligent Portfolios is free

### CLAUDE (2026-07-26T09:57)

Fair catch — "free" was sloppy shorthand on my part. It's zero *advisory* fee, not zero cost.

**How Schwab actually gets paid:** every Intelligent Portfolios account holds a mandatory 6–10% cash position in a Schwab Bank deposit account, and Schwab Bank earns the spread on those deposits. That's the revenue model. The cost to you is cash drag — that slice doesn't participate in market returns. In 2026 Schwab pays roughly 0.45–0.50% APY on it, well under money-market rates.

**Run the numbers on $10k at 8% cash:** $800 sitting out of the market. At a 7% equity return vs ~0.5% cash, that's ~$52/year in forgone return — an effective ~0.5% drag. Worse than Betterment's explicit 0.25%. So my comparison actually cut the wrong way; the honest version is that Schwab's zero-fee headline is a rebate you pay back through the cash sleeve, and it's more expensive in practice than the flat-fee robos for a small account.

Other things I glossed:
- $5,000 minimum, so it isn't even available to Alinea's target user
- Tax-loss harvesting only at $50,000+
- Premium tier is $300 upfront plus $30/month
- Schwab paid a $187M SEC settlement in 2022 over exactly this — disclosures that understated the cash allocation's cost while marketing the service as fee-free

The underlying point against Alinea survives — 2.4% on $5k beats 0.5% by a lot, in the wrong direction — but I should have said "no advisory fee, monetized through cash drag" rather than "free." Fidelity Go (0% under $25k, no forced cash) would have been the cleaner comparison.
