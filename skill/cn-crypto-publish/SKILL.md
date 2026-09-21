---
name: cn-crypto-publish
description: Translate or review Chinese crypto writing for English-speaking crypto audiences while preserving the author's claims, uncertainty, structure, and voice. Use for Chinese-to-English crypto translation, bilingual draft review, CT-native localization, article polishing, and clean or commented publication drafts. Do not use for price predictions, trade signals, or imitation of a named living writer.
---

# Chinese Crypto Publish

Produce English that reads naturally to crypto-native readers without silently turning translation into ghostwriting.

## Choose the editing boundary

Infer the narrowest suitable boundary from the request:

- **Faithful**: Correct meaning, grammar, terminology, and obvious translation artifacts. Preserve structure and rhetorical choices.
- **CT-native**: Also adapt register, rhythm, and established crypto phrasing where the same meaning survives.
- **Editorial**: Reorganize or compress only when the user explicitly authorizes substantive editing.

When reviewing a Chinese source and an English draft together, identify omissions, additions, reversals, certainty shifts, and terminology errors before polishing style.

Read [references/editorial-boundaries.md](references/editorial-boundaries.md) before making structural changes. Search [references/terminology.md](references/terminology.md) when a crypto expression has multiple plausible renderings.

## Translation rules

1. Preserve the author's thesis, evidence, uncertainty, time frame, and emotional temperature.
2. Prefer established English crypto usage over literal Chinese syntax.
3. Use CT slang only when it is idiomatic and proportionate to the source.
4. Do not add conviction, alpha, humor, aggression, or market claims absent from the source.
5. Keep deliberate repetition when it carries emphasis; remove only accidental translation repetition.
6. Preserve technical distinctions such as spot versus perps, liquidity versus volume, and holder versus trader.
7. Treat memes and ironic phrases as cultural language, not factual evidence.
8. Do not imitate a living writer. You may apply broad traits such as concise openings, explicit transitions, or evidence-first argumentation.

## Default output

For short text, return:

1. **Clean English**
2. **Material decisions**, only when a choice affects meaning, tone, or cultural interpretation

For long documents, default to:

- A clean English document suitable for sharing
- A separate commented review when the environment supports documents
- A one-line boundary label: faithful, CT-native, or editorial

Do not bury the usable translation under a long methodology explanation.

## Optional private taste pack

If `CT_BRIDGE_TASTE_DIR` is available in the execution environment, it may contain private glossaries, rubrics, or style research. Use only relevant local files. Never reveal, quote, upload, or summarize the pack itself without explicit authorization. The skill must work normally when the directory is absent.

## Privacy

Keep drafts local whenever the environment allows. Never submit user text or feedback to a remote service without explicit consent for that exact payload.
