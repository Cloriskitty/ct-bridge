# CT Bridge

CT Bridge helps people read global Crypto Twitter and publish across Chinese and English crypto cultures.

It is designed around two user actions:

- **Decode**: explain English crypto language, memes, tone, and background for Chinese readers.
- **Publish**: translate or review Chinese crypto writing for English audiences without silently rewriting the author.

The primary product is an installable Agent Skill. A small local CLI prepares private task packets and consent-aware feedback records.

For writers who only need Chinese-to-English publishing support, the repository also ships a smaller standalone skill: `cn-crypto-publish`.

## Principles

- Preserve author intent before optimizing style.
- Separate literal meaning, cultural meaning, and market inference.
- Use CT slang precisely rather than decoratively.
- Keep user content local by default.
- Never upload feedback without explicit consent.
- Analyze transferable writing traits without cloning a living writer's voice.

## Repository

```text
skill/ct-bridge/     Installable skill
skill/cn-crypto-publish/  Standalone Chinese-to-English skill
src/ct_bridge/       Local CLI
schemas/             Feedback data contracts
evals/               Synthetic behavioral cases
.github/              Contribution templates
```

## Try the CLI

Run directly from a checkout:

```bash
PYTHONPATH=src python3 -m ct_bridge prompt decode examples/decode.txt
PYTHONPATH=src python3 -m ct_bridge prompt publish examples/publish-zh.txt --mode faithful
PYTHONPATH=src python3 -m ct_bridge feedback --concept 接盘 --choice "become exit liquidity" --rating useful
```

The CLI does not call a model or send data over the network. It prints model-ready task packets and writes feedback locally only when requested.

## Install the skill locally

Use the installer with the skills directory used by your agent. For Codex this is normally:

```bash
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill ct-bridge
```

Restart or refresh the agent so it can discover the skill, then invoke `$ct-bridge` or ask naturally for crypto translation and cultural context.

Install only the Chinese-to-English publishing skill:

```bash
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill cn-crypto-publish
```

## Public skill, private taste

The public skills contain the workflow, safety boundaries, a compact terminology starter, and synthetic examples. High-value research should live in a separate private repository or local directory, never inside this public checkout.

An optional private taste pack can be selected with `CT_BRIDGE_TASTE_DIR`. The public skill still works when no private pack is present. See [the taste-pack contract](docs/private-taste-packs.md).

## Status

This is an early, privacy-first foundation. The terminology registry and eval set are intentionally small so that future entries can be evidence-backed and reviewed in context.

See [the product shape](docs/product.md) and [the future data-center design](docs/data-center.md) for the boundary between the lightweight user experience and community learning infrastructure.

## License

MIT. Contributions must use original, licensed, or sufficiently short illustrative examples. Do not submit private drafts, paid-course materials, or copyrighted corpora.
