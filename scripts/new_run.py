#!/usr/bin/env python3
"""Create a new research run folder from templates/run."""
from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from pathlib import Path


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9а-яё]+", "-", text, flags=re.I)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80] or "research-run"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD date prefix")
    parser.add_argument("--force", action="store_true", help="Overwrite existing run folder")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    templates = root / "templates" / "run"
    runs = root / "runs"
    run_dir = runs / f"{args.date}-{slugify(args.topic)}"

    if run_dir.exists():
        if not args.force:
            raise SystemExit(f"Run already exists: {run_dir}")
        shutil.rmtree(run_dir)

    shutil.copytree(templates, run_dir)

    spec = run_dir / "00_spec.md"
    spec_text = spec.read_text(encoding="utf-8")
    spec_text = spec_text.replace("## Topic\n\n", f"## Topic\n\n{args.topic}\n\n")
    spec.write_text(spec_text, encoding="utf-8")

    print(run_dir.relative_to(root))


if __name__ == "__main__":
    main()
