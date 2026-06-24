#!/usr/bin/env python3
"""Validate the repo scaffold from inside the generated repo."""
from __future__ import annotations

from pathlib import Path
import sys

REQUIRED = [
    "README.md",
    "AGENTS.md",
    ".agents/skills/deep-research-os/SKILL.md",
    "protocols/research-spec.md",
    "protocols/question-graph.md",
    "protocols/evidence-ledger.md",
    "docs/06-portable-project-layer.md",
    "docs/07-idea-ledger.md",
    "templates/run/00_spec.md",
    "templates/run/03_evidence_ledger.csv",
    "templates/idea_ledger/idea_ledger_v2.csv",
    "templates/project/rdlab.toml",
    "templates/project/sources.toml",
    "templates/project/topics.toml",
    "templates/project/providers.toml",
    "templates/run_project_lab/00_spec.md",
    "templates/run_project_lab/03_evidence_ledger.csv",
    "scripts/init_project.py",
    "scripts/new_run.py",
    "scripts/provider_router.py",
    "scripts/validate_idea_ledger.py",
    "scripts/validate_project.py",
    "scripts/validate_run.py",
    "scripts/snapshot_sources.py",
    "scripts/smoke_test.py",
    "memory/references/references.yaml",
]

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
missing = [p for p in REQUIRED if not (root / p).exists()]
if missing:
    print("Missing files:")
    for p in missing:
        print(f"  - {p}")
    raise SystemExit(1)
print(f"Scaffold OK: {root}")
