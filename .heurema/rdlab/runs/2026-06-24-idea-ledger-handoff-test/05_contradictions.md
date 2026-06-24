# 05 Contradictions

## C1: Successful handoff vs unsupported status promotion

- Evidence: H3,H4,H5,H6.
- Tension: Agy successfully continued from the ledger but also over-promoted
  I1. Claude refused to update without evidence, which is safer but less
  action-oriented.
- Resolution: Treat handoff success as a separate observation, not as proof that
  idea status should become `validated`.

## C2: More context helps agents, but the test intentionally removed context

- Evidence: H1,H2.
- Tension: The provider could have made better decisions with full run context,
  but the point was to test the ledger alone.
- Resolution: Add update policy to the ledger rather than requiring chat or memo
  context.

## C3: Strict status vocabulary is now necessary

- Evidence: H4,H6.
- Tension: `validated`, `candidate`, and `candidate_validated_once` can mean
  different things unless defined.
- Resolution: Next schema test should include allowed statuses and update rules.
