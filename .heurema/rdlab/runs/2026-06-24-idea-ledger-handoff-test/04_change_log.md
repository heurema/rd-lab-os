# 04 Change Log

## New run artifacts

- `handoff_input_idea_ledger.csv`
- `agy_handoff_output.csv`
- `claude_handoff_output.csv`
- `handoff_normalized_idea_ledger.csv`

## Provider behavior changes

| Provider | Result |
|---|---|
| Agy | Returned valid CSV but promoted I1 to `validated`. |
| Claude Haiku | Returned the ledger unchanged and explicitly refused unsupported updates. |

## Normalization decision

Do not accept `validated` as final status for I1. Use
`candidate_validated_once` to reflect that the ledger passed one handoff test
but should not be globally promoted yet.
