# Setting up new BPO contractor accounts
Date: 2026-09-10
Conversation: d0e878f0-c0c8-4e46-8d39-3e1ac5d50ae8
Domain: business-ops

## Summary
**Conversation Overview**

The person is managing 100+ agents at Blueprint RF and is navigating a transition away from a legacy identity management system called MyID to a newer system (likely a Charter platform, given the Cox/Charter context). They shared a specific list of five unresolved issues with the new contractor account setup process: gaps in required form fields (including a mobile number field that doesn't fit their agent population), the inability to set agent email addresses to the @blueprintrf.com domain, uncertainty about whether the new system has account expiration and renewal mechanisms equivalent to MyID's, the need for a delegated admin model allowing select agents to create and renew accounts with the person's approval, and a lower-priority need for a quarterly access attestation workflow to meet SOC 2 and ISO 27001 compliance obligations.

Claude searched prior conversations for relevant context using multiple queries but found no previous discussion matching this topic. The closest prior chat flagged was one about a personal AI assistant project (July 29/Aug 5, 2026, chat ID cbc7561a-7ede-4d02-8ef3-d64eda8b1a80), which the person confirmed was not relevant. Claude offered to work through the issues in the current conversation if the person could identify the new system by name, but the conversation ended before proceeding further.

**Tool Knowledge**

Claude performed four conversation searches using the following queries: "setting up new BPO contractor accounts," "Cloudstaff contractor account setup process," "new hire onboarding credentials Manila team accounts," and "new contractor VPN email access provisioning." None returned a match. A fifth search on "MyID legacy identity management contractor account expiration" also returned no results. The pattern suggests that searches using platform-specific names (Cloudstaff, MyID) and operational terms (provisioning, onboarding, VPN) did not surface this conversation topic, indicating it had not previously been discussed with Claude.

### SCOTT (2026-09-10T17:14)
wheres the chat abut setting up new BPO contractor accounts

### CLAUDE (2026-09-10T17:14)

None of these match. Let me search with different terms.

The closest match is the **"Personal AI Assistant"** chat (July 29/Aug 5, 2026) — it has a whole section (§11) on "Contractor engagement" covering environment separation, synthetic data, credential handoff, and account/access provisioning for the contractor building your self-hosted AI assistant. That's likely what you're thinking of: https://claude.ai/chat/cbc7561a-7ede-4d02-8ef3-d64eda8b1a80

If you meant something different — like setting up Cloudstaff/BPO staff accounts for actual work systems (not the AI assistant contractor) — I didn't find a chat matching that. Can you narrow it down: is this about the AI assistant contractor, or about onboarding actual Cloudstaff hospitality-ops staff into work systems?

### SCOTT (2026-09-10T17:14)
no.  this list:

1. Setup form gaps — Required fields are blank on my one migrated reference account, so I can't tell what should go in them. One required field is mobile number, which most of my Philippines-based agents don't have (no company phones).
 
2. Email domain — These agents represent Blueprint RF, not Cox or Spectrum, to our customers. Their primary email must be @blueprintrf.com. I can't find where the form lets me set that.
 
3. Account expiration — Under legacy MyID, contractor accounts expired after a year and, if not renewed in time, were deleted entirely (email, SharePoint, system access). I need to know if this new system has an equivalent expiration/renewal mechanism, and if so, how it's managed.
 
4. Delegated admin — Under MyID, I could designate select contractors as supervisors to create and renew accounts themselves, routing to me for approval. Given I manage 100+ agents, I need to know if a similar delegation model exists here.
 
There's a fifth item, lower urgency: under our SOC 2 / ISO 27001 obligations, I run a quarterly access attestation confirming all agent/team accounts are legitimate and should retain access. MyID had a workflow for this. I need to know if this system supports something equivalent

### CLAUDE (2026-09-10T17:14)

I don't have a past chat about this specific replacement identity-management system (post-MyID) or this exact list of setup-form gaps. This looks like it hasn't come up before — want to just work through it now? If you can tell me the name of the new system (Charter's platform, presumably, given the Cox/Charter merger), I can help you draft the questions/escalation to whoever owns it, or think through workarounds for each gap.
