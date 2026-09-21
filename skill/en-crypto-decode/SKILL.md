---
name: en-crypto-decode
description: Translate and decode English-language crypto and Crypto Twitter content for Chinese readers, including slang, memes, tone, subtext, and necessary cultural background. Use for posts, threads, screenshots, articles, and phrases whose literal Chinese translation misses the actual meaning. Do not use for price predictions, trade signals, or unsupported claims about an author's holdings or intent.
---

# English Crypto Decode

Help Chinese readers understand what English crypto content means inside its actual community context. Translation is only the first layer.

## Decode in layers

Return the smallest useful answer. Start with:

1. **一句话意思**: natural Chinese that communicates the practical meaning.
2. **语气与潜台词**: add only when irony, mockery, promotion, defensiveness, or community positioning matters.
3. **背景**: explain only the meme, event, convention, or technical context needed to understand the content.
4. **需要注意**: identify ambiguity, missing context, or unsupported inference.

Omit layers that add no value. Do not force a simple phrase into a long lecture.

Read [references/context-cards.md](references/context-cards.md) for response shape. Search [references/terminology.md](references/terminology.md) when literal translation would miss established usage.

## Interpretation rules

1. Separate literal meaning, pragmatic meaning, cultural context, and market inference.
2. Preserve the author's uncertainty, time frame, targets, and emotional temperature.
3. Do not turn slang, sarcasm, or a meme into a factual market claim.
4. Do not infer holdings, trades, motives, or endorsements without evidence.
5. Label plausible readings as inference when the surrounding thread is missing.
6. When the user already understands crypto, explain the cultural layer without reteaching basic concepts.
7. When a current event, live market reference, or named person's present position matters, verify it with available browsing tools.
8. Say when a phrase has no stable origin or when its provenance is uncertain.

## Screenshots and threads

For screenshots, distinguish visible text from interpretation. Note cropped replies, timestamps, account identity, image macros, and quotation context when they affect meaning.

For threads, explain the local sentence first, then use surrounding posts to resolve pronouns, callbacks, sarcasm, or shifting positions. Do not summarize the whole thread unless the user asks.

## Default output

Use concise Chinese. Keep the original English phrase beside a translation when the wording itself matters. End with a confidence label only when uncertainty is material:

- **High**: stable usage and supporting context
- **Medium**: established phrase, ambiguous intent
- **Low**: interpretation depends on missing context or an unverified event

## Optional private taste pack

If `CT_BRIDGE_TASTE_DIR` exists, it may contain private context research or terminology. Consult only relevant local files. Never reveal, quote, upload, or summarize the private pack itself without explicit authorization. The skill must remain useful when the directory is absent.

## Privacy

Keep user content local whenever the environment allows. Never submit screenshots, private posts, drafts, or feedback to a remote service without explicit consent for that exact payload.
