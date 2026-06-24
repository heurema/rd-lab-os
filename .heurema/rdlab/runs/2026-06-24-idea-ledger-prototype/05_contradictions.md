# 05 Contradictions

## C1: Separate scorecard vs ledger columns

- Evidence: L5,L7.
- Tension: The previous run proposed a separate scorecard, but Agy argues that
  scoring belongs inside `idea_ledger.csv` first.
- Resolution: Keep `idea_scorecard.csv` as a run-local experiment only. Do not
  promote it.

## C2: Debate script is useful but not yet justified

- Evidence: L1,L5.
- Tension: Agy marked I2 KEEP, but the baseline said to add it only after manual
  debate repeats.
- Resolution: Keep I2 as `deferred_until_repeated_manual_debate`.

## C3: Provider health is not provider usefulness

- Evidence: L3,L6.
- Tension: Vibe passed `doctor --probe`, but failed to produce a useful critique
  for this task.
- Resolution: Track both health and task usefulness in critic review.

## C4: Discussion import helps continuity but risks brittle parsing

- Evidence: L2,L5.
- Tension: Importing discussion could reduce manual work, but parsing arbitrary
  transcripts can overbuild and weaken evidence discipline.
- Resolution: STOP I6 for now; manual ledger extraction is enough.
