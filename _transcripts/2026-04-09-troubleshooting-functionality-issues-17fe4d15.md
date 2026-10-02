# Troubleshooting functionality issues
Date: 2026-04-09
Conversation: 17fe4d15-d89f-4281-b741-fb0950f80673
Domain: skip

## Summary
**Conversation Overview**

The person asked two questions in a brief, exploratory conversation. First, they asked why Claude doesn't work, which Claude interpreted as a general troubleshooting inquiry and responded by confirming it was functioning and offering to help with any specific issues. Second, the person asked whether Claude's Cowork feature supports Outlook in addition to Gmail.

Claude provided a detailed response about Microsoft 365 integration, explaining that Anthropic has added a Microsoft 365 connector available across all plan tiers (Free, Pro, Max, Team, and Enterprise), covering Outlook, OneDrive, and SharePoint. Claude noted the key limitation that this requires a professional Microsoft 365 account linked to a Microsoft Entra tenant, and that personal accounts such as Outlook.com, Hotmail, or Live are not supported. Claude also mentioned that initial activation within a company tenant requires consent from a global Entra administrator. Additionally, Claude described community-built MCP (Model Context Protocol) connector workarounds as an alternative for reading inboxes and placing drafted emails into Outlook drafts folders.

The conversation was brief and informational, with no tasks completed or decisions reached beyond Claude sharing product capability details. No personal details, preferences, or work context were shared by the person.

### SCOTT (2026-04-09T07:54)
Your cowork works with Gmail but does it work with outlook

### SCOTT (2026-04-09T08:11)
Hello

### SCOTT (2026-04-09T09:58)
Why don’t you work?

### CLAUDE (2026-04-09T09:58)
 I'm working just fine! Is there something specific that's not working as expected? I'm happy to help troubleshoot or assist with whatever you need.

### SCOTT (2026-04-09T09:59)
Your cowork works with Gmail but does it also work with outlook

### CLAUDE (2026-04-09T09:59)

Yes, and it's actually gotten a lot better on this front recently! Here's the picture:

**Microsoft 365 Connector (the big news):** Anthropic recently added a Microsoft 365 connector, now available on all Claude plans — Free, Pro, Max, Team, and Enterprise. This lets you connect Outlook, OneDrive, and SharePoint to bring your emails, documents, and files directly into the conversation.

**One important caveat:** This requires a *professional* Microsoft 365 account linked to a Microsoft Entra tenant — personal accounts like Outlook.com, Hotmail, or Live are not compatible. For initial activation within a company tenant, a global Entra administrator also needs to grant consent.

**Cowork + Outlook directly:** Cowork doesn't natively integrate with Outlook's internal API, but it can work with exported emails and through MCP (Model Context Protocol) connectors — community-built Outlook MCP servers allow Claude to read your inbox directly and place drafted emails into your Outlook drafts folder.

So in short: if you have a work Microsoft 365 account, the new connector gives you solid Outlook integration. Personal Outlook accounts aren't supported yet through the official connector, but workarounds via MCP or email exports are available.
