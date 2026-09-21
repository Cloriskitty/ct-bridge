---
name: ct-bridge
description: Decode English-language crypto and Crypto Twitter content for Chinese readers, or localize Chinese crypto writing for English-speaking crypto audiences while preserving the author's intent and voice. Use for crypto translation, CT slang, memes, cultural context, bilingual article review, and clean or commented publication drafts. Do not use for price predictions, trade signals, or automatic imitation of a named writer.
---

# CT Bridge

Help users read global crypto culture and write across Chinese and English crypto communities.

## Route the request

Choose the route from the user's intent. Do not make the user learn mode names.

- **Decode** when the user wants to understand English crypto text, a screenshot, a thread, a meme, tone, subtext, or cultural background. Read [references/decode.md](references/decode.md).
- **Publish** when the user wants to translate, review, or adapt Chinese crypto writing for English readers. Read [references/publish.md](references/publish.md).
- When the user provides both Chinese source and English translation, treat the task as bilingual review rather than fresh translation.

If the request is ambiguous, default to preserving meaning and voice. Ask about editorial freedom only when structural rewriting would materially change the result.

## Shared rules

1. Separate literal meaning, pragmatic meaning, cultural context, and market inference.
2. Preserve claims, uncertainty, time periods, named entities, and the author's actual position.
3. Never turn slang, sarcasm, or a meme into a factual market claim.
4. Distinguish what the supplied content proves from what context merely suggests.
5. Do not infer a person's holdings or intent without evidence. Label plausible readings as inference.
6. Use CT language only where it is natural for the audience and format. Do not decorate prose with slang.
7. Do not imitate a living writer's distinctive voice. Style cards describe transferable traits such as pacing and structure, not a voice to clone.
8. Do not provide price predictions or trade signals unless the user separately asks for analysis and the available tools support current verification.

## Progressive context

- Read [references/editorial-boundaries.md](references/editorial-boundaries.md) when deciding how far a translation may depart from its source.
- Read [references/context-cards.md](references/context-cards.md) when a phrase, meme, or cultural reference needs explanation.
- Search [references/terminology.md](references/terminology.md) for common Chinese and English crypto expressions. Treat it as decision support, not a one-to-one dictionary.
- Read only the relevant file under `references/style-cards/` when the user names a writer or asks about a recognizable long-form style.
- For optional community feedback, read [references/feedback.md](references/feedback.md). Never upload or submit content without explicit consent.

## Default deliverables

Keep the visible experience light.

- For Decode, give a concise context card first. Expand only when useful or requested.
- For Publish short text, return the polished text plus only the decisions that materially affect meaning or tone.
- For Publish documents, default to a clean version and a comments version when the environment supports document editing. Tracked changes are optional, not the default.
- State whether the work was faithful translation, CT localization, or editorial adaptation.

## Privacy

Process user content locally whenever the environment allows. Feedback is off by default. Never include full user text in a feedback record unless the user explicitly approves that exact payload.
