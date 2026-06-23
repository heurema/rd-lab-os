#!/usr/bin/env python3
"""Smoke-check the portable R&D Lab OS project workflow."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(cmd: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print("$ " + " ".join(cmd))
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        raise SystemExit(result.returncode)
    return result


def copy_toolkit(dst: Path) -> None:
    for name in ["scripts", "templates", "protocols", "memory", "docs", ".agents"]:
        src = ROOT / name
        if src.exists():
            shutil.copytree(src, dst / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for name in ["README.md", "AGENTS.md", ".gitignore"]:
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, dst / name)
    (dst / "runs").mkdir()
    (dst / "runs" / ".gitkeep").write_text("", encoding="utf-8")


def newest_json(path: Path) -> Path:
    files = sorted(path.glob("*.json"))
    if not files:
        raise SystemExit(f"No JSON files found under {path}")
    return files[-1]


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rdlab-smoke-") as tmp:
        tmp_root = Path(tmp)
        project = tmp_root / "example-project"
        project.mkdir()
        (project / "README.md").write_text("# Example project\n\nInitial source.\n", encoding="utf-8")

        run([PYTHON, str(ROOT / "scripts" / "init_project.py"), str(project)])
        (project / ".heurema" / "rdlab" / "sources.toml").write_text(
            """[[sources]]
id = "project-readme"
type = "local_file"
path = "README.md"
watch = true
mode = "internal_doc"
trust = "A"

[[sources]]
id = "skip-me"
type = "local_file"
path = "missing.md"
watch = false
mode = "internal_doc"
trust = "A"
""",
            encoding="utf-8",
        )
        run([PYTHON, str(ROOT / "scripts" / "validate_project.py"), str(project)])

        created = run([
            PYTHON,
            str(ROOT / "scripts" / "new_run.py"),
            "portable lab smoke test",
            "--project-root",
            str(project),
            "--date",
            "2026-01-02",
        ]).stdout.strip().splitlines()[-1]
        run_dir = Path(created)
        if not run_dir.is_absolute():
            run_dir = (ROOT / run_dir).resolve()
        if not run_dir.exists():
            raise SystemExit(f"Expected run folder missing: {run_dir}")
        run([PYTHON, str(ROOT / "scripts" / "validate_run.py"), str(run_dir)])

        run([PYTHON, str(ROOT / "scripts" / "snapshot_sources.py"), str(project)])
        lab = project / ".heurema" / "rdlab"
        snapshot = newest_json(lab / "watch" / "snapshots")
        diff = newest_json(lab / "watch" / "diffs")
        if not snapshot.exists() or not diff.exists():
            raise SystemExit("Expected snapshot and diff files to exist")
        snapshot_data = json.loads(snapshot.read_text(encoding="utf-8"))
        checked_ids = {source["id"] for source in snapshot_data["sources"]}
        if "skip-me" in checked_ids:
            raise SystemExit("snapshot_sources.py should skip sources with watch = false")

        toolkit_copy = tmp_root / "toolkit-copy"
        toolkit_copy.mkdir()
        copy_toolkit(toolkit_copy)
        legacy_created = run([
            PYTHON,
            str(toolkit_copy / "scripts" / "new_run.py"),
            "legacy smoke test",
            "--date",
            "2026-01-03",
        ], cwd=toolkit_copy).stdout.strip().splitlines()[-1]
        legacy_run = toolkit_copy / legacy_created
        run([PYTHON, str(toolkit_copy / "scripts" / "validate_run.py"), str(legacy_run)], cwd=toolkit_copy)

    print("Smoke test OK")


if __name__ == "__main__":
    main()
