# 02 Source Map

## Project config sources

| Source ID | Source | Mode | Trust | Watch | Status |
|---|---|---|---|---|---|
| project-readme | `README.md` | internal_doc | A | true | snapshotted ok |
| agent-instructions | `AGENTS.md` | internal_doc | A | true | snapshotted ok |
| portable-project-layer-doc | `docs/06-portable-project-layer.md` | internal_doc | A | true | snapshotted ok |
| provider-router-script | `scripts/provider_router.py` | code_repo | A | true | snapshotted ok |
| project-lab-run-template | `templates/run_project_lab/07_ideas.md` | internal_doc | A | true | snapshotted ok |
| project-lab-experiment-template | `templates/run_project_lab/08_experiments.md` | internal_doc | A | true | snapshotted ok |
| github-repo | `https://github.com/heurema/rd-lab-os` | code_repo | A | false | registered, not snapshotted |
| github-repo-readme | raw GitHub README URL | code_repo | A | true | snapshotted ok |
| openai-codex-skills-doc | OpenAI Codex skills docs URL | official_docs | A | true | snapshotted ok |

## Primary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | `README.md` | internal_doc | Defines current public project framing and workflow. | checked |
| 2 | `AGENTS.md` | internal_doc | Defines agent operating rules and quality bar. | checked |
| 3 | `docs/06-portable-project-layer.md` | internal_doc | Defines portable project layer, provider router, ideas/experiments. | checked |
| 4 | `scripts/provider_router.py` | code_repo | Implements the provider routing surface now available for debate. | checked |
| 5 | `.heurema/rdlab/watch/snapshots/20260624T051742518067Z.json` | internal_doc | Confirms local and external source snapshot state. | checked |

## Secondary sources

| Priority | Source | Mode | Why it matters | Status |
|---|---|---|---|---|
| 1 | Vibe provider output | unknown | Independent product-idea generation from a non-Anthropic provider. | checked |
| 2 | Agy provider output | unknown | Independent critic/triage output from a separate provider. | checked |

## External source pass

External source pass completed through `scripts/snapshot_sources.py .`.

| Priority | Source | Mode | What it can support | Status |
|---|---|---|---|---|
| 1 | `https://raw.githubusercontent.com/heurema/rd-lab-os/main/README.md` | code_repo | Public repo state can be fetched and watched. | ok |
| 2 | `https://developers.openai.com/codex/skills` | official_docs | Codex skill model remains relevant external reference. | ok |

## Social / recency signals

| Source | Mode | What it can support | Limitations |
|---|---|---|---|
| none used | social_signal | N/A | This run focuses on repo-local workflow design, not market/social validation. |

## Sources to avoid or treat carefully

| Source | Reason |
|---|---|
| Provider outputs | Useful for critique and idea diversity, but not authoritative evidence about repo constraints. |
| Raw external docs content | Snapshot confirms reachability/hash, but this run does not quote the external docs. |
| Future UI/backend ideas | Explicitly out of scope for v0. |
