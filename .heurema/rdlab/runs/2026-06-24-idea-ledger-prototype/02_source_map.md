# 02 Source Map

## Project config sources

| Source ID | Source | Mode | Trust | Watch | Status |
|---|---|---|---|---|---|
| previous-run-ideas | `.heurema/rdlab/runs/2026-06-24-rd-lab-os-idea-discovery-and-discussion/07_ideas.md` | internal_doc | A | false | checked |
| previous-run-experiments | `.heurema/rdlab/runs/2026-06-24-rd-lab-os-idea-discovery-and-discussion/08_experiments.md` | internal_doc | A | false | checked |
| previous-run-critic | `.heurema/rdlab/runs/2026-06-24-rd-lab-os-idea-discovery-and-discussion/09_critic_review.md` | internal_doc | A | false | checked |
| provider-router | `scripts/provider_router.py` | code_repo | A | true | checked |

## Primary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | Previous run `07_ideas.md` | internal_doc | Source list of I1-I6. | checked |
| 2 | Previous run `08_experiments.md` | internal_doc | Defines X1 success criteria. | checked |
| 3 | Provider health probe | unknown | Confirms subscription providers available. | checked |
| 4 | Agy critic output | unknown | Independent strict critique and scorecard. | checked |
| 5 | Claude extraction output | unknown | Tests extraction of idea rows into CSV shape. | checked |

## Secondary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | Vibe schema critique attempt | unknown | Tests provider debate reliability. | attempted, not usable |

## External source pass

This run is scoped as an internal artifact experiment. External source baseline
was already established by the previous run snapshot:

```text
.heurema/rdlab/watch/snapshots/20260624T051742518067Z.json
```

## Sources to avoid or treat carefully

| Source | Reason |
|---|---|
| Provider generated CSV | Useful extraction draft, but evidence IDs need normalization against this run ledger. |
| Provider scorecard | Useful critique, not a product requirement by itself. |
