# CT Bridge

中文 | [English](#english)

CT Bridge 是一个连接中文加密社区与英文 Crypto Twitter（CT）语境的开源 Agent Skill。

它不只是逐字翻译，而是帮助用户处理两类真正困难的问题：

- **Decode / 读懂**：向中文读者解释英文加密内容中的术语、meme、语气、潜台词与文化背景。
- **Publish / 表达**：把中文加密内容翻译或校订为英语，同时保留作者本人的观点、语气与写作边界。

主要产品是可以安装到 AI Agent 中的 Skill。仓库还包含一个轻量本地 CLI，用于生成任务包和记录经过用户同意的反馈；它本身不会调用模型或上传数据。

## 为什么做这个项目

中文和英文加密社区之间的信息差不只来自语言，也来自社区记忆、市场周期、meme、玩梗方式和默认常识。

直译经常丢掉语境；过度“润色”又可能擅自改变作者的判断。CT Bridge 希望在两者之间建立一套透明、可测试、可贡献的方法。

## 核心原则

- 先保留作者原意，再优化英文表达。
- 区分字面含义、文化含义与市场推断。
- CT slang 只在自然且准确时使用，不把黑话当装饰。
- 不擅自增加确定性、攻击性、幽默或市场观点。
- 默认在本地处理用户内容，未经明确同意不上传反馈。
- 可以分析可迁移的写作特征，但不模仿在世作者的独特文风。

## 三个可安装 Skill

### `ct-bridge`

完整版本，同时支持 Decode 和 Publish。

### `cn-crypto-publish`

独立的中译英版本，适合只需要翻译、双语校订或 CT-native 本地化的作者。它提供三种编辑边界：

- **Faithful**：忠实翻译，只修正准确性、术语、语法和明显的翻译腔。
- **CT-native**：在不改变原意的前提下，调整为英文加密读者熟悉的表达。
- **Editorial**：仅在用户明确授权时重组、压缩或改写文章。

### `en-crypto-decode`

独立的英译中版本。除了翻译文字，也会按需解释 CT slang、meme、语气、潜台词与必要背景，并明确区分事实和推断。

## 安装

```bash
git clone https://github.com/Cloriskitty/ct-bridge.git
cd ct-bridge

# 安装完整 Skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill ct-bridge

# 或者只安装中译英 Skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill cn-crypto-publish

# 或者只安装英译中 + 语境解码 Skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill en-crypto-decode
```

安装后刷新或重启 Agent，然后调用 `$ct-bridge`、`$cn-crypto-publish`、`$en-crypto-decode`，或直接用自然语言描述任务。

也可以把两个单向 Skill 分别打包：

```bash
python3 scripts/package_skills.py
```

## CLI 示例

```bash
PYTHONPATH=src python3 -m ct_bridge prompt decode examples/decode.txt
PYTHONPATH=src python3 -m ct_bridge prompt publish examples/publish-zh.txt --mode faithful
PYTHONPATH=src python3 -m ct_bridge feedback --concept 接盘 --choice "become exit liquidity" --rating useful
```

CLI 不调用模型，也不会通过网络发送数据。只有在用户主动指定时，它才会把反馈写入本地文件。

## 公开能力与私有 Taste

公开仓库包含工作流、编辑边界、基础术语、合成测试案例和扩展接口。高价值研究，例如真实文章标注、完整人物风格分析、gold eval、付费资料和用户偏好，不应进入公开仓库。

私有增强资料可以保存在独立仓库或本地目录，并通过 `CT_BRIDGE_TASTE_DIR` 连接。公开 Skill 在没有私有资料时仍可独立运行。详见 [Private taste packs](docs/private-taste-packs.md)。

## 项目结构

```text
skill/ct-bridge/          完整 Decode + Publish Skill
skill/cn-crypto-publish/ 独立中译英 Skill
skill/en-crypto-decode/  独立英译中 + 语境解码 Skill
src/ct_bridge/           本地 CLI
schemas/                 反馈数据协议
evals/                   合成行为测试
.github/                 Issue 与 PR 模板
```

## 测试

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 evals/check_cases.py
```

项目目前处于早期阶段。术语库与评测集刻意保持精简，后续条目应有明确语境、可验证案例和人工审核。

## 贡献与许可

欢迎提交术语、语境卡、测试案例和方法改进。请只使用原创、已获授权或足够短的说明性示例，不要提交私人稿件、付费课程内容或受版权保护的语料库。

本项目采用 MIT License。

---

<a id="english"></a>

## English

CT Bridge is an open-source Agent Skill for navigating the cultural and linguistic gap between Chinese crypto communities and English-language Crypto Twitter (CT).

It supports two core workflows:

- **Decode**: explain English crypto terminology, memes, tone, subtext, and cultural background for Chinese readers.
- **Publish**: translate or review Chinese crypto writing for English-speaking audiences without silently rewriting the author's position or voice.

The main product is an installable Agent Skill. The repository also includes a small local CLI for preparing task packets and recording consent-aware feedback. The CLI does not call a model or upload data.

## Why this exists

The gap between Chinese and English crypto communities is not merely linguistic. It also includes shared memory, market-cycle references, memes, irony, and unstated cultural assumptions.

Literal translation often loses that context, while aggressive polishing can overwrite the author's actual judgment. CT Bridge provides a transparent, testable, and community-improvable method between those extremes.

## Principles

- Preserve author intent before optimizing the English.
- Separate literal meaning, cultural meaning, and market inference.
- Use CT slang precisely, not decoratively.
- Do not add conviction, aggression, humor, or market claims absent from the source.
- Keep user content local by default and never upload feedback without explicit consent.
- Analyze transferable writing traits without cloning a living writer's distinctive voice.

## Three installable skills

### `ct-bridge`

The complete skill, covering both Decode and Publish workflows.

### `cn-crypto-publish`

A standalone Chinese-to-English skill for translation, bilingual review, and CT-native localization. It supports three editing boundaries:

- **Faithful**: correct accuracy, terminology, grammar, and translation artifacts while preserving structure and voice.
- **CT-native**: adapt established crypto phrasing and rhythm without changing the underlying meaning.
- **Editorial**: reorganize, compress, or rewrite only with explicit authorization.

### `en-crypto-decode`

A standalone English-to-Chinese skill. Beyond translation, it explains CT slang, memes, tone, subtext, and necessary background while keeping facts separate from inference.

## Installation

```bash
git clone https://github.com/Cloriskitty/ct-bridge.git
cd ct-bridge

# Install the complete skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill ct-bridge

# Or install only the Chinese-to-English skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill cn-crypto-publish

# Or install only the English-to-Chinese decoding skill
python3 scripts/install_skill.py --skills-dir "$CODEX_HOME/skills" --skill en-crypto-decode
```

Refresh or restart the agent after installation, then invoke `$ct-bridge`, `$cn-crypto-publish`, `$en-crypto-decode`, or describe the task naturally.

Package the two directional skills as separate ZIP files:

```bash
python3 scripts/package_skills.py
```

## CLI examples

```bash
PYTHONPATH=src python3 -m ct_bridge prompt decode examples/decode.txt
PYTHONPATH=src python3 -m ct_bridge prompt publish examples/publish-zh.txt --mode faithful
PYTHONPATH=src python3 -m ct_bridge feedback --concept 接盘 --choice "become exit liquidity" --rating useful
```

The CLI does not call a model or transmit data over the network. It writes feedback locally only when explicitly requested.

## Public capability, private taste

The public repository contains the workflow, editorial boundaries, starter terminology, synthetic tests, and extension contract. High-value research such as annotated real-world drafts, complete writer studies, gold evaluations, paid material, and user preference profiles should remain outside the public repository.

Private enhancements can live in a separate repository or local directory and be selected with `CT_BRIDGE_TASTE_DIR`. The public skills remain fully usable without a private pack. See [Private taste packs](docs/private-taste-packs.md).

## Repository layout

```text
skill/ct-bridge/          Complete Decode + Publish skill
skill/cn-crypto-publish/ Standalone Chinese-to-English skill
skill/en-crypto-decode/  Standalone English-to-Chinese decoding skill
src/ct_bridge/           Local CLI
schemas/                 Feedback data contracts
evals/                   Synthetic behavioral cases
.github/                 Issue and pull-request templates
```

## Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 evals/check_cases.py
```

This is an early-stage, privacy-first foundation. The terminology registry and evaluation set are intentionally compact so future additions can be contextual, evidence-backed, and reviewed.

## Contributing and license

Contributions to terminology, context cards, evaluations, and methodology are welcome. Use only original, licensed, or sufficiently short illustrative examples. Do not submit private drafts, paid-course material, or copyrighted corpora.

Released under the MIT License.
