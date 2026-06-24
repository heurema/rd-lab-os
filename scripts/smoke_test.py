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


def run_fail(cmd: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.returncode == 0:
        print("$ " + " ".join(cmd))
        if result.stdout:
            print(result.stdout)
        raise SystemExit("Expected command to fail")
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
        providers_config = project / ".heurema" / "rdlab" / "providers.toml"
        if not providers_config.exists():
            raise SystemExit("init_project.py should create providers.toml")
        provider_list = run([
            PYTHON,
            str(ROOT / "scripts" / "provider_router.py"),
            "list",
            "--project-root",
            str(project),
        ]).stdout
        if "claude-sonnet" not in provider_list or "vibe-default" not in provider_list:
            raise SystemExit("provider_router.py list should include default subscription providers")
        synthesis_route = run([
            PYTHON,
            str(ROOT / "scripts" / "provider_router.py"),
            "route",
            "--project-root",
            str(project),
            "--task",
            "synthesis",
        ]).stdout
        if "provider_id=claude-sonnet" not in synthesis_route:
            raise SystemExit("synthesis route should prefer claude-sonnet by default")
        critic_route = run([
            PYTHON,
            str(ROOT / "scripts" / "provider_router.py"),
            "route",
            "--project-root",
            str(project),
            "--task",
            "critic",
            "--exclude-provider",
            "anthropic",
        ]).stdout
        if "provider_id=vibe-default" not in critic_route:
            raise SystemExit("critic route should prefer a non-Anthropic provider when Anthropic is excluded")

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
        source_map_template = (run_dir / "02_source_map.md").read_text(encoding="utf-8")
        critic_template = (run_dir / "09_critic_review.md").read_text(encoding="utf-8")
        if "External source pass" not in source_map_template:
            raise SystemExit("project_lab source map must require an external source pass")
        if "Provider / critic debate" not in critic_template:
            raise SystemExit("project_lab critic review must require provider / critic debate")
        run([PYTHON, str(ROOT / "scripts" / "validate_run.py"), str(run_dir)])

        valid_idea_ledger = tmp_root / "valid_idea_ledger.csv"
        valid_idea_ledger.write_text(
            """idea_id,status,allowed_statuses,update_policy,status_update_reason
I1,candidate,candidate|deferred,Keep candidate unless new evidence supports a change.,No new evidence.
I2,deferred,candidate|deferred,Keep deferred until prerequisite evidence exists.,Prerequisite missing.
""",
            encoding="utf-8",
        )
        invalid_status_ledger = tmp_root / "invalid_status_ledger.csv"
        invalid_status_ledger.write_text(
            """idea_id,status,allowed_statuses,update_policy,status_update_reason
I1,promoted,candidate|deferred,Keep candidate unless new evidence supports a change.,No new evidence.
""",
            encoding="utf-8",
        )
        missing_policy_ledger = tmp_root / "missing_policy_ledger.csv"
        missing_policy_ledger.write_text(
            """idea_id,status,allowed_statuses,update_policy,status_update_reason
I1,candidate,candidate|deferred,,No new evidence.
""",
            encoding="utf-8",
        )
        duplicate_id_ledger = tmp_root / "duplicate_id_ledger.csv"
        duplicate_id_ledger.write_text(
            """idea_id,status,allowed_statuses,update_policy,status_update_reason
I1,candidate,candidate|deferred,Keep candidate unless new evidence supports a change.,No new evidence.
I1,deferred,candidate|deferred,Keep deferred until prerequisite evidence exists.,Prerequisite missing.
""",
            encoding="utf-8",
        )
        run([PYTHON, str(ROOT / "scripts" / "validate_idea_ledger.py"), str(valid_idea_ledger), "--strict"])
        run_fail([PYTHON, str(ROOT / "scripts" / "validate_idea_ledger.py"), str(invalid_status_ledger)])
        run_fail([PYTHON, str(ROOT / "scripts" / "validate_idea_ledger.py"), str(missing_policy_ledger)])
        run_fail([PYTHON, str(ROOT / "scripts" / "validate_idea_ledger.py"), str(duplicate_id_ledger)])
        idea_ledger_template = ROOT / "templates" / "idea_ledger" / "idea_ledger_v2.csv"
        if not idea_ledger_template.exists():
            raise SystemExit(f"Missing idea ledger template: {idea_ledger_template}")
        run([PYTHON, str(ROOT / "scripts" / "validate_idea_ledger.py"), str(idea_ledger_template), "--strict"])

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
