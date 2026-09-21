# Feedback and Consent

Feedback improves the context registry only when users understand what leaves their environment.

## Consent levels

- `off`: record nothing.
- `metadata`: mode, concept label, selected option, rating, and software version. No source text.
- `snippet`: include only a user-approved short source/target pair.
- `full-example`: include a complete example only after explicit approval for that exact content.

Default to `off`. A request to translate or review content is not consent to collect it.

## Useful events

- Accepted or rejected suggestion.
- User-provided alternative.
- Register assessment such as too formal, too degen, or unlike the author.
- Platform and audience fit.
- Report that a phrase is outdated, regional, or missing context.

Before submission, show the complete feedback payload. This initial repository writes feedback locally and provides no network submission path.
