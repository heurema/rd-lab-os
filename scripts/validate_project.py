#!/usr/bin/env python3
"""Validate a project-local R&D Lab OS layer under .heurema/rdlab."""
from __future__ import annotations

import argparse
import tomllib
from pathlib import Path


LAB_RELATIVE = Path(".heurema") / "rdlab"
CONFIG_FILES = ["rdlab.toml", "sources.toml", "topics.toml"]
OPTIONAL_CONFIG_FILES = ["providers.toml"]
REQUIRED_DIRS = ["runs", "memory", "watch", "ideas", "experiments", "decisions"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Project directory to validate")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    lab = root / LAB_RELATIVE
    errors: list[str] = []

    if not root.exists():
        errors.append(f"project root missing: {root}")
    if (root / ".rdlab").exists():
        errors.append("top-level .rdlab/ exists; canonical lab path is .heurema/rdlab/")
    if not lab.exists():
        errors.append(f"missing lab directory: {lab}")
    elif not lab.is_dir():
        errors.append(f"lab path is not a directory: {lab}")

    for name in CONFIG_FILES:
        path = lab / name
        if not path.exists():
            errors.append(f"missing config: {name}")
            continue
        try:
            with path.open("rb") as f:
                tomllib.load(f)
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid TOML in {name}: {exc}")

    for name in OPTIONAL_CONFIG_FILES:
        path = lab / name
        if not path.exists():
            continue
        try:
            with path.open("rb") as f:
                tomllib.load(f)
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid TOML in {name}: {exc}")

    for name in REQUIRED_DIRS:
        path = lab / name
        if not path.exists():
            errors.append(f"missing directory: {name}")
        elif not path.is_dir():
            errors.append(f"not a directory: {name}")

    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(f"Project lab OK: {lab}")


if __name__ == "__main__":
    main()
