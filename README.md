# R&D Lab OS

R&D Lab OS is a portable research operating layer for projects.

This repo is **not** a model-training project. It provides a repeatable,
evidence-first research workflow with project-local configuration, run
templates, evidence ledgers, critic checklists, source snapshots, and durable
memory artifacts.

The core toolkit can run in two modes:

- repo-local mode inside this repository, using `runs/`;
- project-local mode inside another repository or project, using
  `.heurema/rdlab/`.

Do not create `.rdlab/`. Heurema project tooling belongs under the single
`.heurema/` namespace.

## Core workflow

```text
Research Spec
→ Question Graph
→ Source Map
→ Evidence Ledger
→ Contradiction Review
→ Synthesis
→ Critic Review
→ Final Memo
→ Decision Log / Memory Update
```

## Repo-local mode

```bash
python3 scripts/new_run.py "deep research agents reference atlas"
```

Then fill the artifacts in the created folder under `runs/`.

## Project-local mode

Initialize a lab in another project:

```bash
python3 /path/to/rd-lab-os/scripts/init_project.py /path/to/project
```

Create a project-local run:

```bash
python3 /path/to/rd-lab-os/scripts/new_run.py "topic" --project-root /path/to/project
```

Validate the project lab:

```bash
python3 /path/to/rd-lab-os/scripts/validate_project.py /path/to/project
```

Snapshot configured sources:

```bash
python3 /path/to/rd-lab-os/scripts/snapshot_sources.py /path/to/project
```

Project-local runs live under:

```text
<project>/.heurema/rdlab/runs/
```

## Important rule

The final memo is not the source of truth. The evidence ledger is.
