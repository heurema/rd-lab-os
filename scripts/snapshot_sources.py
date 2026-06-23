#!/usr/bin/env python3
"""Create minimal source snapshots for a project-local R&D Lab OS layer."""
from __future__ import annotations

import argparse
import hashlib
import json
import tomllib
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LAB_RELATIVE = Path(".heurema") / "rdlab"
TIMEOUT_SECONDS = 10


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_location(source: dict[str, Any]) -> str:
    source_type = source.get("type", "")
    if source_type == "local_file":
        return str(source.get("path", ""))
    if source_type == "url":
        return str(source.get("url", ""))
    return str(source.get("url") or source.get("path") or source.get("query") or "")


def check_local_file(project_root: Path, source: dict[str, Any]) -> dict[str, Any]:
    location = source_location(source)
    path = (project_root / location).resolve()
    if not path.exists():
        return {"hash": "", "status": "missing", "error": f"local file not found: {location}"}
    if not path.is_file():
        return {"hash": "", "status": "error", "error": f"local path is not a file: {location}"}
    try:
        return {"hash": sha256_bytes(path.read_bytes()), "status": "ok", "error": ""}
    except OSError as exc:
        return {"hash": "", "status": "error", "error": str(exc)}


def check_url(source: dict[str, Any]) -> dict[str, Any]:
    url = source_location(source)
    if not url:
        return {"hash": "", "status": "error", "error": "missing url"}
    request = urllib.request.Request(url, headers={"User-Agent": "rd-lab-os-snapshot/0"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read()
        return {"hash": sha256_bytes(body), "status": "ok", "error": ""}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"hash": "", "status": "error", "error": str(exc)}


def latest_previous_snapshot(snapshot_dir: Path) -> dict[str, Any] | None:
    files = sorted(snapshot_dir.glob("*.json"))
    if not files:
        return None
    try:
        return json.loads(files[-1].read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def compare_snapshots(previous: dict[str, Any] | None, current_sources: list[dict[str, Any]]) -> dict[str, list[str]]:
    current_by_id = {item["id"]: item for item in current_sources}
    previous_by_id = {}
    if previous:
        previous_by_id = {item["id"]: item for item in previous.get("sources", [])}

    added = sorted(set(current_by_id) - set(previous_by_id))
    removed = sorted(set(previous_by_id) - set(current_by_id))
    changed: list[str] = []
    unchanged: list[str] = []
    failed: list[str] = []

    for source_id, item in current_by_id.items():
        if item.get("status") != "ok":
            failed.append(source_id)
        if source_id not in previous_by_id:
            continue
        previous_item = previous_by_id[source_id]
        if item.get("hash") and item.get("hash") == previous_item.get("hash"):
            unchanged.append(source_id)
        elif item.get("hash") != previous_item.get("hash"):
            changed.append(source_id)

    return {
        "added": added,
        "removed": removed,
        "changed": sorted(changed),
        "unchanged": sorted(unchanged),
        "failed": sorted(failed),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Project directory with .heurema/rdlab")
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    lab = project_root / LAB_RELATIVE
    sources_path = lab / "sources.toml"
    if not sources_path.exists():
        raise SystemExit(f"Missing sources config: {sources_path}")

    with sources_path.open("rb") as f:
        config = tomllib.load(f)
    sources = config.get("sources", [])
    if not isinstance(sources, list):
        raise SystemExit("sources.toml must contain [[sources]] entries")

    snapshot_dir = lab / "watch" / "snapshots"
    diff_dir = lab / "watch" / "diffs"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    diff_dir.mkdir(parents=True, exist_ok=True)

    previous = latest_previous_snapshot(snapshot_dir)
    timestamp = utc_timestamp()
    checked: list[dict[str, Any]] = []

    for index, source in enumerate(sources, start=1):
        if not isinstance(source, dict):
            continue
        source_id = str(source.get("id") or f"source-{index}")
        source_type = str(source.get("type") or "unknown")
        location = source_location(source)
        if source_type == "local_file":
            result = check_local_file(project_root, source)
        elif source_type == "url":
            result = check_url(source)
        else:
            result = {"hash": "", "status": "unsupported", "error": f"unsupported source type: {source_type}"}
        checked.append({
            "id": source_id,
            "source_type": source_type,
            "source_location": location,
            "hash": result["hash"],
            "status": result["status"],
            "error": result["error"],
        })

    snapshot = {
        "timestamp": timestamp,
        "project": project_root.name,
        "sources_checked": len(checked),
        "sources": checked,
    }
    diff = {"timestamp": timestamp, **compare_snapshots(previous, checked)}

    snapshot_path = snapshot_dir / f"{timestamp}.json"
    diff_path = diff_dir / f"{timestamp}.json"
    snapshot_path.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    diff_path.write_text(json.dumps(diff, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(snapshot_path)
    print(diff_path)


if __name__ == "__main__":
    main()
