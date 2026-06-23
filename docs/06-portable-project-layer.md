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
      runs/
      memory/
      watch/
      decisions/
      ideas/
      experiments/
```

`rdlab.toml` defines project-level lab settings. `sources.toml` lists sources
that can be used or watched. `topics.toml` is the project research topic
registry.

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
