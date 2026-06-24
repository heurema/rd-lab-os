# 00 Spec

## Topic

Run-local `idea_ledger.csv` prototype.

## Project context

This run continues the baseline idea-discovery run:

```text
.heurema/rdlab/runs/2026-06-24-rd-lab-os-idea-discovery-and-discussion/
```

The baseline accepted X1 as the first experiment: test whether a minimal idea
ledger improves continuity over prose-only `07_ideas.md`.

## Decision context

The user wants agents to search and discuss ideas without relying on manual
chat steering. The next practical step is to see whether a flat CSV artifact
helps agents extract, critique, and update ideas consistently.

## Intended audience

- Future `rd-lab-os` agents.
- Repository maintainer deciding whether `idea_ledger.csv` should become a
  template artifact.

## Output type

Project-local experimental run with:

- normal `project_lab` artifacts;
- extra run-local `idea_ledger.csv`;
- extra run-local `idea_scorecard.csv`;
- provider critique notes.

## Scope

- Convert prior run ideas into a CSV ledger.
- Ask subscription providers to critique or score the ledger.
- Decide whether to keep the ledger run-local, promote it to a template, or
  reject/defer it.

## Non-scope

- No backend.
- No UI.
- No vector DB.
- No global template change in this run.
- No `debate_ideas.py` implementation yet.

## Topic registry link

- `idea-discovery`
- `provider-debate`
- `portable-lab-product`

## Source preferences

Primary source is the previous run's `07_ideas.md`, `08_experiments.md`, and
`09_critic_review.md`. Provider outputs are critique signals only.

## External source requirement

This run is intentionally mostly internal because it tests a local artifact
shape. External source baseline was already checked in the previous run via
snapshot `20260624T051742518067Z.json`.

## Freshness requirements

Use repository and lab state as of 2026-06-24.

## Critic / debate requirement

Use at least two subscription provider passes when possible:

- Claude Sonnet for ledger extraction;
- Agy for strict scorecard critique;
- Vibe attempted for schema critique, but record failure if output is not
  usable.

## Success criteria

- `idea_ledger.csv` has rows for I1-I6.
- Each row references evidence rows.
- A critic pass changes at least one status/verdict.
- Run validates in strict mode.
- Final memo gives a keep/modify/defer decision.

## Constraints

- Do not modify global templates yet.
- Keep CSV stdlib-readable.
- Do not treat provider output as authoritative evidence.
- Do not hide failed provider attempts.

## Assumptions

- A useful run-local ledger should reduce the need to read prior chat.
- If scorecard fields are useful, they may belong in the ledger rather than a
  separate artifact.

## Open questions

- Should score fields live inside `idea_ledger.csv`?
- What status vocabulary is sufficient?
- Is `discussion import` still worth keeping after strict critique?
