# Community Context Data

The first release has no telemetry endpoint. The CLI can preview or append feedback to a local JSONL file. This creates a testable consent model before any server exists.

## Future architecture

```text
Skill CLI and future clients
            |
     explicit user consent
            |
   feedback payload preview
            |
      ingestion service
            |
  moderation and aggregation
            |
 context proposals and evals
            |
 reviewed release or pull request
```

## Data categories

- Product feedback: whether the result was useful or missing context.
- Linguistic preference: selected wording and rejected alternatives.
- Context metadata: platform, audience, register, region, and content type.
- Approved snippets: short examples contributed under explicit consent.

These categories must remain separate. Product usage does not imply permission to collect linguistic examples.

## Governance

- No automatic rule changes from telemetry.
- Aggregate repeated feedback into a public proposal.
- Require provenance, boundaries, and an eval before registry changes.
- Preserve disagreement when a phrase varies by region or subcommunity.
- Never accept private drafts, paid materials, private chats, wallet data, or secrets.

## Consent invariant

The complete outbound payload must be visible before submission. `metadata` events contain no source text. `snippet` and `full-example` require explicit opt-in for the exact content.
