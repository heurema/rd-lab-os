#!/usr/bin/env python3
"""Create a new research run folder."""
from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from pathlib import Path


LAB_RELATIVE = Path(".heurema") / "rdlab"
PROFILES = {
    "legacy": Path("templates") / "run",
    "project_lab": Path("templates") / "run_project_lab",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9а-яё]+", "-", text, flags=re.I)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80] or "research-run"


def fill_topic(spec: Path, topic: str) -> None:
    spec_text = spec.read_text(encoding="utf-8")
    spec_text = spec_text.replace("## Topic\n\n", f"## Topic\n\n{topic}\n\n", 1)
    spec.write_text(spec_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD date prefix")
    parser.add_argument("--project-root", help="Create the run under <project-root>/.heurema/rdlab/runs")
    parser.add_argument("--profile", choices=sorted(PROFILES), help="Run template profile")
    parser.add_argument("--force", action="store_true", help="Overwrite existing run folder")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    profile = args.profile or ("project_lab" if args.project_root else "legacy")
    templates = root / PROFILES[profile]
    if not templates.exists():
        raise SystemExit(f"Missing run templates for profile {profile!r}: {templates}")

    project_root = Path(args.project_root).expanduser().resolve() if args.project_root else None
    if project_root:
        lab = project_root / LAB_RELATIVE
        if not lab.exists():
            raise SystemExit(
                f"Project lab does not exist: {lab}\n"
                f"Run first: python3 {root / 'scripts' / 'init_project.py'} {project_root}"
            )
        runs = lab / "runs"
    else:
        runs = root / "runs"
    runs.mkdir(parents=True, exist_ok=True)
    run_dir = runs / f"{args.date}-{slugify(args.topic)}"

    if run_dir.exists():
        if not args.force:
            raise SystemExit(f"Run already exists: {run_dir}")
        shutil.rmtree(run_dir)

    shutil.copytree(templates, run_dir)
    fill_topic(run_dir / "00_spec.md", args.topic)

    if project_root:
        print(run_dir)
    else:
        print(run_dir.relative_to(root))


if __name__ == "__main__":
    main()
