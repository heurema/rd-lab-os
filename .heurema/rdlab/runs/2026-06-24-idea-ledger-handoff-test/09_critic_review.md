# 09 Critic Review

## Critical issues

- Do not mark I1 as fully `validated` from this run alone.
- Do not promote the ledger schema without update policy.

## Medium issues

- Agy was action-oriented but over-promoted status.
- Claude was evidence-disciplined but did not advance the ledger.
- The prompt said providers may update status, but did not define when they
  should update it.

## Minor issues

- `candidate_validated_once` is descriptive but not yet part of a defined status
  vocabulary.

## Missing primary sources

- No real fourth agent or human operator used the normalized ledger yet.
- No script consumes the normalized ledger.

## Unsupported claims

- "The ledger is template-ready" is not supported.
- "All providers can safely update ledger status" is not supported.

## Provider / critic debate

| Reviewer | Provider / role | Main objection | Change made or reason rejected |
|---|---|---|---|
| Agy | handoff updater | Treated handoff completion as validation and changed I1 to `validated`. | Rejected full validation; normalized to `candidate_validated_once`. |
| Claude Haiku | handoff updater/checker | Refused to update because no new evidence was supplied. | Accepted as evidence-discipline signal. |
| Codex | synthesis owner | Provider divergence shows schema needs update policy. | Added X1c/X1d experiments. |

## Overconfident recommendations

- Avoid "ship template now".
- Avoid "Agy validated the ledger"; it only showed the ledger is actionable.

## Final confidence rating

Medium-high that the ledger works as handoff input. Medium that the current
schema is safe without update policy.
