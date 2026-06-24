# 09 Critic Review

## Critical issues

- Do not promote `idea_ledger.csv` to global templates yet.
- Do not implement discussion import now.
- Do not treat `doctor --probe` as proof a provider will produce useful output
  for every critique prompt.

## Medium issues

- Evidence rows from provider-generated CSV required normalization.
- A separate scorecard may duplicate ledger fields.
- Vibe was healthy but not useful for this task.

## Minor issues

- `idea_ledger.csv` uses semicolon-separated evidence row lists inside a CSV
  cell; this is acceptable but should be documented if promoted.

## Missing primary sources

- No second human/operator continued the run from the ledger yet.
- No downstream script consumes `idea_ledger.csv`.

## Unsupported claims

- This run does not prove `idea_ledger.csv` should be part of every
  `project_lab` run.
- This run does not prove `debate_ideas.py` is needed.

## Provider / critic debate

Provider health:

```text
claude-sonnet: ok
claude-haiku: ok
vibe-default: ok
agy-default: ok
```

Actual task usefulness:

| Reviewer | Provider / role | Main objection | Change made or reason rejected |
|---|---|---|---|
| Claude Sonnet | extraction | Drafted CSV rows but evidence IDs needed normalization. | Used only as draft input. |
| Agy | strict critic | Keep I1/I2, modify I3, defer I4/I5, stop I6. | Adopted in `idea_ledger.csv` and `idea_scorecard.csv`. |
| Vibe | schema critic | Did not return usable schema critique; first attempt hit turn limit, retry emitted tool-read text. | Recorded as provider limitation. |

## Overconfident recommendations

- "Add idea ledger to templates now" is premature.
- "Add debate script now" is premature.

## Final confidence rating

Medium. The ledger is useful enough for another run-local test, but not enough
for template promotion.
