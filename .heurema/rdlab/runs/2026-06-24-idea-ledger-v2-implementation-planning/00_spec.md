# 00 Spec

## Topic

Implementation planning from `idea_ledger_v2_normalized.csv`.

## Project context

The previous run produced `idea_ledger_v2_normalized.csv`, which preserved idea
statuses under explicit update policy. This run tests whether that ledger alone
can drive the smallest next implementation decision.

## Decision context

The desired outcome is not template promotion. The expected safe next step is a
validator or docs before templates.

## Intended audience

- Future coding agent implementing the next small change.
- Maintainer reviewing whether idea-ledger work is ready to enter core scripts.

## Output type

Project-local implementation-planning run with provider plans and normalized
implementation recommendation.

## Scope

- Give only `idea_ledger_v2_normalized.csv` to providers.
- Compare their smallest implementation recommendation.
- Normalize provider naming mistakes against current repo files.
- Decide the next implementation step.

## Non-scope

- Do not implement code in this run.
- Do not promote templates.
- Do not create UI/backend/vector DB.
- Do not create debate automation.

## Topic registry link

- `idea-discovery`
- `provider-debate`

## Source preferences

Primary source is the normalized v2 ledger. Secondary sources are provider
implementation plans and current repo script inventory.

## External source requirement

Internal-only by design. This run asks what implementation follows from a local
artifact; external sources cannot determine the next repo-specific file.

## Freshness requirements

Use repo state on 2026-06-24.

## Critic / debate requirement

Use at least two providers on the same input:

- Claude Sonnet;
- Agy.

## Success criteria

- Providers choose validator/docs before template promotion.
- Normalized plan avoids clobbering existing evidence-ledger validator.
- Run validates in strict mode.

## Constraints

- Keep next implementation stdlib-only.
- Keep evidence ledger and idea ledger validators separate.
- No global memory update.

## Assumptions

- A validator is safer than template promotion because repeated agent edits need
  guardrails.

## Open questions

- Should validator live only in core scripts or also be referenced in project
  README/docs?
- Should `status_update_reason` be required only in strict mode?
