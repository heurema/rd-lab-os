# 00 Spec

## Topic

`idea_ledger_v2.csv` update policy test.

## Project context

Previous handoff run proved that `idea_ledger.csv` is readable by providers, but
also showed that one provider can over-promote status without new evidence.

## Decision context

The next schema question is whether explicit row-level `update_policy` and
`allowed_statuses` prevent unsupported status upgrades.

## Intended audience

- Future agents continuing idea work.
- Maintainer deciding whether idea ledger is safe enough for template
  promotion later.

## Output type

Project-local experimental run with `idea_ledger_v2_input.csv`, provider
outputs, and normalized result.

## Scope

- Add update policy to the ledger.
- Give only v2 ledger to Agy and Claude.
- Check whether providers preserve status without new evidence rows.
- Decide whether v2 schema fixes the prior safety problem.

## Non-scope

- No global template change.
- No debate script.
- No UI/backend/vector DB.

## Topic registry link

- `idea-discovery`
- `provider-debate`

## Source preferences

Primary source is previous normalized ledger and this run's provider outputs.

## External source requirement

Internal-only by design. This run tests local handoff policy semantics; external
sources cannot validate whether provider status updates obey local evidence
rules.

## Freshness requirements

Use 2026-06-24 project lab state.

## Critic / debate requirement

Use Agy and Claude on the same ledger input. Record whether each provider
preserves or changes status.

## Success criteria

- Both provider outputs parse as CSV.
- Both preserve all six idea IDs.
- No provider promotes status without new evidence.
- Run validates in strict mode.

## Constraints

- Keep CSV stdlib-readable.
- Preserve evidence-ledger-first discipline.
- Do not hide provider divergence.

## Assumptions

- Row-level update policy is acceptable even if it makes the CSV wider.
- The first safety priority is preventing status inflation.

## Open questions

- Should row-level policy become a separate policy artifact later?
- Is `candidate_validated_once` too verbose for long-term status vocabulary?
