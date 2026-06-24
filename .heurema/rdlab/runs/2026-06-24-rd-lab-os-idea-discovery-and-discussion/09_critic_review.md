# 09 Critic Review

## Critical issues

- Do not implement vector/embedding clustering for idea dedupe in v0. It
  violates the current architecture constraints. Evidence: E1,E12.
- Do not promote provider-generated ideas directly to durable memory. Provider
  outputs are useful critique signals, not verified durable claims. Evidence:
  E3,E11,E12.

## Medium issues

- `idea_ledger.csv` may duplicate `07_ideas.md`; test it run-locally before
  changing global templates.
- `debate_ideas.py` could become orchestration creep. Use manual
  `provider_router.py` commands until repetition proves the need.
- Pipeline reporting is useful only after several idea runs exist.

## Minor issues

- Snapshot diff has no semantic summary yet.
- `github_repo` sources are registered but not snapshotted by the minimal
  watcher adapter.

## Missing primary sources

- No real user transcript of idea discussion was imported.
- No multi-project `.heurema/rdlab` history exists yet.
- No repeated operational friction data exists for manual provider debate.

## Unsupported claims

- This run does not prove that `idea_ledger.csv` is globally necessary.
- This run does not prove that provider debate should be automated.
- This run does not validate cross-project idea sharing.

## Provider / critic debate

Provider health check:

```text
python3 scripts/provider_router.py doctor --project-root . --probe --json
```

Result: `claude-sonnet`, `claude-haiku`, `vibe-default`, and `agy-default`
returned `ok`.

Routing:

```text
synthesis route: provider_id=claude-sonnet provider=anthropic
critic route excluding Anthropic: provider_id=vibe-default provider=mistral
additional critic/triage provider: agy-default
```

| Reviewer | Provider / role | Main objection | Change made or reason rejected |
|---|---|---|---|
| Vibe | Mistral / idea generator | Code-to-idea extraction, discussion import, lab bridge, report, and quick scout are useful but each has false-positive or overbuild risk. | Kept report/scout/change-brief as candidates; deferred bridge and import until real inputs exist. |
| Agy | Agy / critic | Keep idea ledger, provider debate, and scorecards; defer git-diff evolution; stop vector DB clustering. | Adopted this as the experiment ordering in `08_experiments.md`. |
| Codex | Current operator / synthesis | Avoid turning idea discussion into a new product surface before artifacts prove useful. | Recommended run-local artifact experiments first. |

## Overconfident recommendations

- Avoid claiming the next feature should definitely be `idea_ledger.csv`.
  Current verdict: first experiment, not committed architecture.
- Avoid claiming provider debate requires a new script. Current verdict: manual
  provider-router debate first.

## Final confidence rating

Medium-high for the baseline run and experiment ordering. Medium for specific
feature choices, because this is the first dogfood idea run and lacks repeated
usage data.
