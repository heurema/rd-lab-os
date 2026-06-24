# 00 Spec

## Topic

Idea ledger handoff test.

## Project context

This run tests whether another agent can continue idea work from only
`idea_ledger.csv`, without relying on chat history, prior memos, or prose
sections.

## Decision context

The prior run kept `idea_ledger.csv` as a run-local experiment and said the next
test should use the ledger as the only idea handoff artifact.

## Intended audience

- Future agents continuing idea work in `rd-lab-os`.
- Maintainer deciding whether `idea_ledger.csv` needs an explicit update policy.

## Output type

Project-local handoff validation run with provider outputs and normalized
result CSVs.

## Scope

- Use only the previous run's `idea_ledger.csv` as provider input.
- Ask independent providers to update `status`, `critic_verdict`, and
  `next_test`.
- Compare whether providers preserve evidence discipline.
- Decide the next schema change.

## Non-scope

- No template promotion.
- No script implementation.
- No UI/backend/vector DB.
- No provider output accepted without normalization.

## Topic registry link

- `idea-discovery`
- `provider-debate`

## Source preferences

Primary source is the previous run's `idea_ledger.csv`. Provider outputs are
evidence about handoff behavior, not authoritative roadmap decisions.

## External source requirement

Internal-only by design. This run tests project-local artifact handoff, not
external market or docs claims. The reason is recorded here, in synthesis, and
in critic review.

## Freshness requirements

Use project lab state on 2026-06-24.

## Critic / debate requirement

Use at least two subscription providers:

- `agy-default` as handoff updater;
- `claude-haiku` as independent handoff updater/checker.

## Success criteria

- Providers can parse the ledger without additional context.
- At least one provider returns a usable updated ledger or a justified refusal.
- Run records divergence between providers.
- Normalized result does not promote statuses without evidence.

## Constraints

- Keep CSV stdlib-readable.
- Keep the input prompt limited to `idea_ledger.csv`.
- Do not pretend provider agreement if outputs diverge.

## Assumptions

- A safe handoff artifact should allow continuation and also prevent unsupported
  status upgrades.

## Open questions

- Should `idea_ledger.csv` include `update_policy`?
- Should `status` and `critic_verdict` use stricter enumerations?
- Should refusal to update without new evidence count as success?
