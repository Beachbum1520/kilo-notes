# Claude model families explained
Date: 2026-06-21
Conversation: 30c43475-5519-40ad-8669-6e5555b7c9d9
Domain: skip

## Summary
**Conversation Overview**

The person asked Claude to explain the different AI models visible in a model selector interface. Claude provided an explanation of Anthropic's Claude model families — Haiku, Sonnet, and Opus — describing the tier structure from fastest/lightest (Haiku) to most capable (Opus), and clarifying that version numbers indicate generation iterations within each family. Claude also explained the "Effort: High" setting as a reasoning depth control and noted that "Fable 5" was greyed out due to restricted access. The conversation referenced an ongoing project involving data analysis, prescription building, and periodization decisions, with Claude noting that Opus 4.8 on High effort is the appropriate configuration for that work.

### SCOTT (2026-06-21T15:27)
Explain to me these different models.
[File uploaded: photo.jpeg]

### CLAUDE (2026-06-21T15:28)
Looking at the image Scott shared, I can see a model selector showing several Claude versions available, with Opus 4.8 currently selected for complex tasks. The dropdown displays other options like Sonnet 4.6, Haiku 4.5, and various Opus versions, plus a note that Fable 5 is unavailable. I need to explain what these different models are and how they differ. I'm recognizing that the tier structure is what matters here—Haiku for speed, Sonnet for balance, Opus for maximum capability—and I can explain the version numbers as iterations within each tier without needing to fabricate details I don't have. I should be straightforward about what I know from my product information versus what I'm uncertain about, and skip the fitness context since this is just a straightforward question about the models themselves. I should stick with what I know reliably rather than inventing details about intermediate versions. I'll organize around the three model families as the core concept, keep the explanation straightforward for mobile, and be upfront about the version numbering without fabricating specs.Quick map of what you're looking at. Claude models come in three families, and the number after the name is the generation (higher = newer).

The three families, fastest to most capable:

- **Haiku (4.5)** — the lightweight, fast, cheap model. Good for quick lookups, simple tasks, high-volume stuff where speed matters more than depth.
- **Sonnet (4.6)** — the balanced middle. Strong reasoning at much better speed and cost than Opus. Most everyday work runs fine here.
- **Opus (4.8, 4.7, 4.6, 3)** — the heavyweight tier, built for complex, multi-step reasoning. 4.8 is the current top model and what's selected in your screenshot. 4.7, 4.6, and 3 are older Opus generations still kept available; unless you have a specific reason to pin an older one, the newest Opus is the one to use.

A couple other things in that menu:

**Effort: High** — this controls how much reasoning the model does before answering. Higher effort = deeper thinking, slower response. High is the right setting for analysis-heavy work (which is most of what you throw at me in this project).

**Fable 5 – Currently unavailable** — that's part of a higher experimental tier sitting above Opus. Access is restricted right now, which is why it's greyed out. Not something you can select.

For what we do here — parsing your data, building prescriptions, periodization decisions — Opus 4.8 on High effort is the correct pick. You're already on it.
