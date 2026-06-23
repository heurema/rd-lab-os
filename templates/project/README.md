# Project R&D Lab

This directory is the project-local R&D Lab OS layer.

Canonical path:

```text
.heurema/rdlab/
```

Use it for project research configuration, topic tracking, source snapshots,
research runs, decisions, ideas, experiments, and promoted memory.

Do not create `.rdlab/`. Heurema project tooling should stay under the single
`.heurema/` namespace.

## Typical commands

```bash
python3 /path/to/rd-lab-os/scripts/validate_project.py /path/to/project
python3 /path/to/rd-lab-os/scripts/new_run.py "topic" --project-root /path/to/project
python3 /path/to/rd-lab-os/scripts/snapshot_sources.py /path/to/project
```
