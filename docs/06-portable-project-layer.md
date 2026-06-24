# Portable Project Layer

R&D Lab OS has three layers:

```text
rd-lab-os core
  -> project-local .heurema/rdlab layer
  -> optional future cross-project registry
```

The core repo owns protocols, templates, scripts, validators, and skills. A
project-local lab stores the research state for one project. A future
cross-project registry may summarize signals across many project-local labs,
but that is out of scope for v0.

## Canonical Path

The project-local lab path is:

```text
<project>/.heurema/rdlab/
```

Do not use `.rdlab/`.

All Heurema project tooling should live under one `.heurema/` namespace. This
prevents each tool from scattering its own top-level hidden directory across
many repositories.

## Project Structure

```text
<project>/
  .heurema/
    rdlab/
      rdlab.toml
      sources.toml
      topics.toml
      providers.toml
      runs/
      memory/
      watch/
      decisions/
      ideas/
      experiments/
```

`rdlab.toml` defines project-level lab settings. `sources.toml` lists sources
that can be used or watched. `topics.toml` is the project research topic
registry. `providers.toml` defines subscription-backed CLI providers for
research, synthesis, critic, and implementation passes.

## Repo Core vs Project Lab

Repo-local mode in `rd-lab-os` uses:

```text
runs/
templates/run/
```

Project-local mode uses:

```text
<project>/.heurema/rdlab/runs/
templates/run_project_lab/
```

The legacy run template remains supported. The project-lab template extends it
with change tracking, ideas, experiments, and explicit memory update artifacts.

## Initialize A Project

```bash
python3 /path/to/rd-lab-os/scripts/init_project.py /path/to/project
```

This creates `.heurema/rdlab/`, copies project config templates, fills the
project name in `rdlab.toml`, and creates the standard lab directories.

Use `--force` only when replacing existing config files is intentional:

```bash
python3 /path/to/rd-lab-os/scripts/init_project.py /path/to/project --force
```

## Create A Run

Repo-local legacy run:

```bash
python3 scripts/new_run.py "topic"
```

Project-local run:

```bash
python3 /path/to/rd-lab-os/scripts/new_run.py "topic" --project-root /path/to/project
```

Project-local mode defaults to the `project_lab` profile and writes under:

```text
<project>/.heurema/rdlab/runs/YYYY-MM-DD-topic/
```

Before synthesis, project-local runs should complete an external source pass
unless the run is deliberately internal-only. The reason for an internal-only
run must be written in `02_source_map.md`, `06_synthesis.md`, and
`09_critic_review.md`.

The critic review should record independent critique. Prefer a separate
provider or agent when available. If the same agent performs all passes, record
that limitation explicitly instead of presenting it as provider debate.

## Subscription Provider Router

Project labs can use a simple subscription-only provider router:

```bash
python3 /path/to/rd-lab-os/scripts/provider_router.py list --project-root /path/to/project
python3 /path/to/rd-lab-os/scripts/provider_router.py doctor --project-root /path/to/project
python3 /path/to/rd-lab-os/scripts/provider_router.py doctor --project-root /path/to/project --probe
```

The router reads `.heurema/rdlab/providers.toml`. It does not store secrets and
does not use API-key provider flows. It shells out to configured local CLI tools
such as Claude Code, Vibe, Agy, Codex, or Gemini when those tools are explicitly
enabled in `providers.toml`.

Use routing commands to separate synthesis and critic providers:

```bash
python3 /path/to/rd-lab-os/scripts/provider_router.py route --project-root /path/to/project --task synthesis
python3 /path/to/rd-lab-os/scripts/provider_router.py route --project-root /path/to/project --task critic --exclude-provider anthropic
```

Provider availability is machine- and account-specific. A configured provider
is not considered healthy until `doctor --probe` succeeds. If a provider is
blocked by login, region, token refresh, or account eligibility, record that in
`09_critic_review.md` instead of claiming a multi-provider debate happened.

## Validate

Validate a project-local lab:

```bash
python3 /path/to/rd-lab-os/scripts/validate_project.py /path/to/project
```

Validate a run:

```bash
python3 /path/to/rd-lab-os/scripts/validate_run.py /path/to/project/.heurema/rdlab/runs/<run>
```

Strict run validation additionally requires evidence rows and avoids counting
template-only Markdown files as completed content.

## Source Snapshots

```bash
python3 /path/to/rd-lab-os/scripts/snapshot_sources.py /path/to/project
```

The snapshot script reads `.heurema/rdlab/sources.toml`, checks entries where
`watch = true`, supports `local_file` and `url` sources, computes SHA256 hashes,
writes timestamped JSON snapshots, and writes a simple diff summary. It skips
entries with `watch = false`. It is not a crawler and does not perform semantic
diffing.

## Ideas, Experiments, And Memory

Project-lab runs include:

- `07_ideas.md` for candidate ideas and rejected ideas;
- `08_experiments.md` for hypothesis and experiment planning;
- `12_memory_update.md` for explicit memory promotion decisions.

For idea-heavy runs, optionally copy:

```text
templates/idea_ledger/idea_ledger_v2.csv
```

See `docs/07-idea-ledger.md` for status vocabulary and update rules.

Run-local idea ledgers can be validated with:

```bash
python3 /path/to/rd-lab-os/scripts/validate_idea_ledger.py /path/to/project/.heurema/rdlab/runs/<run>/idea_ledger_v2_normalized.csv --strict
```

This validator is separate from `validate_ledger.py`. The evidence ledger
validates claims and source support; the idea ledger validator checks idea
status rules such as `status`, `allowed_statuses`, `update_policy`, and
`status_update_reason`.

Memory promotion should remain conservative. Promote verified, reusable claims,
references, patterns, decisions, and benchmarks. Do not promote weak evidence as
durable memory.

## Research Modes

One-off research run:

- create a run;
- fill the artifact chain;
- validate the run;
- stop after the decision or memo.

Watched project research:

- configure sources in `sources.toml`;
- snapshot sources over time;
- use changes as inputs for new runs.

Cross-project intelligence:

- aggregate durable patterns across project-local labs;
- compare topics and decisions across projects;
- defer registry design until several project labs exist.

## Out Of Scope

- Backend or API server
- UI or dashboard
- Model training or fine-tuning
- Vector database
- GraphRAG deployment
- Scheduler
- Heavy multi-agent orchestration framework
- Paid-product UI automation
