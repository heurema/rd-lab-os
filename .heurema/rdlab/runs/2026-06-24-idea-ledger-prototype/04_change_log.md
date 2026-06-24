# 04 Change Log

## New artifacts in this run

- `idea_ledger.csv`
- `idea_scorecard.csv`

## Provider attempts

| Provider | Purpose | Result |
|---|---|---|
| claude-sonnet | Convert ideas I1-I6 into CSV-like rows. | Usable draft, normalized before use. |
| agy-default | Strict critic scorecard. | Usable; changed statuses. |
| vibe-default | Schema critique. | Not usable for this prompt; recorded as limitation. |

## Changes to idea status from baseline

- I1 remains top candidate.
- I2 remains useful but gated on manual repetition.
- I3 is modified: scorecard fields should be tested in the ledger first.
- I4 and I5 are deferred.
- I6 is stopped for now because discussion import risks brittle parsing.
