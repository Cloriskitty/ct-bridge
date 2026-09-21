# Private taste packs

CT Bridge deliberately separates the public workflow from private editorial research.

## Keep private

- Full style analyses of named writers
- Real client drafts and annotated revisions
- Paid-course material or licensed corpora
- Gold evaluation answers and scoring heuristics
- Contributor preference profiles and non-public feedback
- Time-sensitive phrase judgments built from private research

Keep these assets in a separate private repository. Do not place them in this repository and rely only on `.gitignore`.

## Optional directory contract

Set `CT_BRIDGE_TASTE_DIR` to a local checkout of a private pack:

```text
taste-private/
├── README.md
├── glossary/
│   └── crypto-en.yaml
├── style-cards/
├── rubrics/
└── evals/
```

The public skill must remain useful without this directory. A compatible agent may consult the directory only when it exists and only for the current local task. It must not quote, upload, or expose private pack contents unless the user explicitly requests and authorizes that exact disclosure.

## Publishing rule

Before every public release, verify the staged file list with:

```bash
git status --short
git diff --cached --name-only
```

If a file contains real user text, private research, or paid material, unstage it and move it to the private repository.
