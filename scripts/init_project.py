#!/usr/bin/env python3
"""Initialize a project-local R&D Lab OS layer under .heurema/rdlab."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


LAB_RELATIVE = Path(".heurema") / "rdlab"
PROJECT_TEMPLATE_FILES = ["rdlab.toml", "sources.toml", "topics.toml", "providers.toml", "README.md"]
DIRECTORIES = [
    "runs",
    "memory",
    "memory/references",
    "memory/entities",
    "memory/claims",
    "memory/patterns",
    "memory/benchmarks",
    "memory/decisions",
    "watch",
    "watch/snapshots",
    "watch/diffs",
    "decisions",
    "ideas",
    "experiments",
]


def render_project_name(text: str, project_name: str) -> str:
    return text.replace('name = ""', f'name = "{project_name}"', 1)


def init_project(project_root: Path, force: bool) -> Path:
    root = project_root.expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Project root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    toolkit_root = Path(__file__).resolve().parents[1]
    template_root = toolkit_root / "templates" / "project"
    if not template_root.exists():
        raise SystemExit(f"Missing project templates: {template_root}")

    lab = root / LAB_RELATIVE
    lab.mkdir(parents=True, exist_ok=True)

    conflicts = [name for name in PROJECT_TEMPLATE_FILES if (lab / name).exists() and not force]
    if conflicts:
        joined = ", ".join(conflicts)
        raise SystemExit(f"Project lab already has config files: {joined}. Use --force to overwrite.")

    for relative in DIRECTORIES:
        (lab / relative).mkdir(parents=True, exist_ok=True)

    project_name = root.name
    for name in PROJECT_TEMPLATE_FILES:
        src = template_root / name
        dst = lab / name
        if name == "rdlab.toml":
            text = render_project_name(src.read_text(encoding="utf-8"), project_name)
            dst.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(src, dst)

    return lab


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Project directory to initialize")
    parser.add_argument("--force", action="store_true", help="Overwrite existing project config files")
    args = parser.parse_args()

    lab = init_project(Path(args.project_root), args.force)
    print(lab)


if __name__ == "__main__":
    main()
