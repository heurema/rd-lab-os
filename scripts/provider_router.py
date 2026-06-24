#!/usr/bin/env python3
"""Route project research work across subscription-backed provider CLIs."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LAB_RELATIVE = Path(".heurema") / "rdlab"
DEFAULT_TIMEOUT_SECONDS = 90
TASKS = ["research", "synthesis", "critic", "implementation", "fast"]


@dataclass(frozen=True)
class Provider:
    id: str
    provider: str
    adapter: str
    command: str
    model: str
    enabled: bool
    subscription_only: bool
    roles: tuple[str, ...]
    notes: str


def toolkit_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_config_path() -> Path:
    return toolkit_root() / "templates" / "project" / "providers.toml"


def resolve_project_lab(project_root: str | None) -> Path | None:
    if not project_root:
        return None
    root = Path(project_root).expanduser().resolve()
    lab = root / LAB_RELATIVE
    if not lab.exists():
        raise SystemExit(
            f"Project lab missing: {lab}\n"
            f"Run scripts/init_project.py {root} before using project-local provider routing."
        )
    return lab


def resolve_config(config_arg: str | None, project_root: str | None) -> tuple[Path, bool]:
    if config_arg:
        return Path(config_arg).expanduser().resolve(), False

    lab = resolve_project_lab(project_root)
    if lab:
        project_config = lab / "providers.toml"
        if project_config.exists():
            return project_config, False
        return default_config_path(), True

    return default_config_path(), False


def load_router_config(config_arg: str | None, project_root: str | None) -> tuple[dict[str, Any], Path, bool]:
    path, used_fallback = resolve_config(config_arg, project_root)
    if not path.exists():
        raise SystemExit(f"Provider config missing: {path}")
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)
    except tomllib.TOMLDecodeError as exc:
        raise SystemExit(f"Invalid TOML in {path}: {exc}") from exc
    return data, path, used_fallback


def require_string(value: Any, field: str, provider_id: str) -> str:
    if not isinstance(value, str):
        raise SystemExit(f"Provider {provider_id} must define string field: {field}")
    return value


def parse_providers(data: dict[str, Any]) -> list[Provider]:
    raw = data.get("providers", [])
    if not isinstance(raw, list):
        raise SystemExit("providers.toml must contain [[providers]] entries")

    providers: list[Provider] = []
    seen: set[str] = set()
    for item in raw:
        if not isinstance(item, dict):
            raise SystemExit("Each provider entry must be a TOML table")
        provider_id = require_string(item.get("id"), "id", "<unknown>")
        if provider_id in seen:
            raise SystemExit(f"Duplicate provider id: {provider_id}")
        seen.add(provider_id)
        roles = item.get("roles", [])
        if not isinstance(roles, list) or not all(isinstance(role, str) for role in roles):
            raise SystemExit(f"Provider {provider_id} must define roles as a string list")
        providers.append(
            Provider(
                id=provider_id,
                provider=require_string(item.get("provider"), "provider", provider_id),
                adapter=require_string(item.get("adapter"), "adapter", provider_id),
                command=require_string(item.get("command"), "command", provider_id),
                model=str(item.get("model", "")),
                enabled=bool(item.get("enabled", False)),
                subscription_only=bool(item.get("subscription_only", False)),
                roles=tuple(roles),
                notes=str(item.get("notes", "")),
            )
        )
    return providers


def command_available(provider: Provider) -> bool:
    return shutil.which(provider.command) is not None


def provider_status(provider: Provider, require_subscription_only: bool = True) -> str:
    if not provider.enabled:
        return "disabled"
    if require_subscription_only and not provider.subscription_only:
        return "non_subscription"
    if not command_available(provider):
        return "command_missing"
    return "ready"


def routing_order(data: dict[str, Any], task: str, providers: list[Provider]) -> list[Provider]:
    by_id = {provider.id: provider for provider in providers}
    routing = data.get("routing", {})
    ordered_ids: list[str] = []
    if isinstance(routing, dict):
        values = routing.get(task, [])
        if isinstance(values, list):
            ordered_ids = [value for value in values if isinstance(value, str)]

    ordered = [by_id[provider_id] for provider_id in ordered_ids if provider_id in by_id]
    ordered_seen = {provider.id for provider in ordered}
    ordered.extend(provider for provider in providers if provider.id not in ordered_seen)
    return ordered


def select_provider(
    data: dict[str, Any],
    providers: list[Provider],
    task: str,
    exclude_ids: set[str],
    exclude_providers: set[str],
    require_available: bool,
) -> Provider:
    if task not in TASKS:
        raise SystemExit(f"Unknown task: {task}. Expected one of: {', '.join(TASKS)}")

    candidates = routing_order(data, task, providers)
    for provider in candidates:
        if provider.id in exclude_ids or provider.provider in exclude_providers:
            continue
        if not provider.enabled or not provider.subscription_only:
            continue
        if task not in provider.roles:
            continue
        if require_available and not command_available(provider):
            continue
        return provider

    raise SystemExit(
        f"No subscription provider available for task={task}. "
        "Check providers.toml or run provider_router.py doctor --probe."
    )


def build_prompt_command(provider: Provider, prompt: str, cwd: Path, output_file: Path | None = None) -> list[str]:
    if provider.adapter == "claude":
        cmd = [
            "env",
            "-u",
            "ANTHROPIC_API_KEY",
            "-u",
            "CLAUDECODE",
            provider.command,
            "-p",
            "--output-format",
            "text",
        ]
        if provider.model:
            cmd.extend(["--model", provider.model])
        cmd.append(prompt)
        return cmd

    if provider.adapter == "gemini":
        model = provider.model or "auto-gemini-3"
        return [provider.command, "-m", model, "-p", prompt, "--output-format", "text"]

    if provider.adapter == "vibe":
        return [
            provider.command,
            "--trust",
            "--workdir",
            str(cwd),
            "-p",
            prompt,
            "--max-turns",
            "1",
            "--max-tokens",
            "800",
            "--max-price",
            "0.10",
            "--output",
            "text",
        ]

    if provider.adapter == "agy":
        cmd = [provider.command, "-p", prompt, "--print-timeout", f"{DEFAULT_TIMEOUT_SECONDS}s"]
        if provider.model:
            cmd.extend(["--model", provider.model])
        return cmd

    if provider.adapter == "codex":
        if output_file is None:
            raise SystemExit("Codex adapter requires an output file")
        cmd = [
            provider.command,
            "--ask-for-approval",
            "never",
            "exec",
            "--skip-git-repo-check",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--output-last-message",
            str(output_file),
        ]
        if provider.model:
            cmd.extend(["--model", provider.model])
        cmd.append(prompt)
        return cmd

    raise SystemExit(f"Unsupported provider adapter: {provider.adapter}")


def run_provider(provider: Provider, prompt: str, cwd: Path, timeout: int) -> tuple[int, str, str]:
    env = os.environ.copy()
    with tempfile.TemporaryDirectory(prefix="rdlab-provider-") as tmp:
        output_file = Path(tmp) / "codex-last-message.txt" if provider.adapter == "codex" else None
        cmd = build_prompt_command(provider, prompt, cwd, output_file)
        proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout, env=env)
        stdout = proc.stdout.strip()
        if output_file and output_file.exists():
            stdout = output_file.read_text(encoding="utf-8").strip() or stdout
        return proc.returncode, stdout, proc.stderr.strip()


def probe_token(provider_id: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", provider_id).strip("_").upper()
    return f"{normalized}_OK"


def doctor_provider(provider: Provider, probe: bool, timeout: int, cwd: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": provider.id,
        "provider": provider.provider,
        "adapter": provider.adapter,
        "model": provider.model,
        "enabled": provider.enabled,
        "subscription_only": provider.subscription_only,
        "command": provider.command,
    }
    status = provider_status(provider)
    result["status"] = status
    if status != "ready" or not probe:
        return result

    expected = probe_token(provider.id)
    prompt = f"Reply with exactly: {expected}"
    try:
        returncode, stdout, stderr = run_provider(provider, prompt, cwd, timeout)
    except subprocess.TimeoutExpired:
        result.update({"status": "timeout", "returncode": "timeout"})
        return result

    result.update(
        {
            "returncode": returncode,
            "stdout_tail": stdout[-500:],
            "stderr_tail": stderr[-500:],
        }
    )
    if returncode == 0 and expected in stdout:
        result["status"] = "ok"
    else:
        result["status"] = "failed"
    return result


def print_fallback_warning(used_fallback: bool, project_root: str | None) -> None:
    if used_fallback and project_root:
        print(
            "warning: project lab has no providers.toml; using toolkit defaults",
            file=sys.stderr,
        )


def cmd_list(args: argparse.Namespace) -> None:
    data, path, used_fallback = load_router_config(args.config, args.project_root)
    print_fallback_warning(used_fallback, args.project_root)
    providers = parse_providers(data)
    print(f"config={path}")
    for provider in providers:
        roles = ",".join(provider.roles)
        print(
            f"provider_id={provider.id} provider={provider.provider} adapter={provider.adapter} "
            f"model={provider.model or '-'} enabled={str(provider.enabled).lower()} "
            f"subscription_only={str(provider.subscription_only).lower()} "
            f"status={provider_status(provider)} roles={roles}"
        )


def cmd_route(args: argparse.Namespace) -> None:
    data, path, used_fallback = load_router_config(args.config, args.project_root)
    print_fallback_warning(used_fallback, args.project_root)
    provider = select_provider(
        data=data,
        providers=parse_providers(data),
        task=args.task,
        exclude_ids=set(args.exclude_id),
        exclude_providers=set(args.exclude_provider),
        require_available=not args.allow_missing_command,
    )
    print(
        f"provider_id={provider.id} provider={provider.provider} adapter={provider.adapter} "
        f"model={provider.model or '-'} command={provider.command} task={args.task} config={path}"
    )


def cmd_doctor(args: argparse.Namespace) -> None:
    data, _path, used_fallback = load_router_config(args.config, args.project_root)
    print_fallback_warning(used_fallback, args.project_root)
    providers = parse_providers(data)
    if not args.include_disabled:
        providers = [provider for provider in providers if provider.enabled]
    cwd = Path(args.workdir).expanduser().resolve() if args.workdir else Path.cwd()
    results = [doctor_provider(provider, args.probe, args.timeout, cwd) for provider in providers]
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    for result in results:
        print(
            f"provider_id={result['id']} provider={result['provider']} adapter={result['adapter']} "
            f"model={result['model'] or '-'} status={result['status']}"
        )
        if result.get("stderr_tail"):
            print(f"  stderr_tail={result['stderr_tail']}")


def cmd_run(args: argparse.Namespace) -> None:
    data, _path, used_fallback = load_router_config(args.config, args.project_root)
    print_fallback_warning(used_fallback, args.project_root)
    providers = parse_providers(data)
    if args.provider_id:
        matches = [provider for provider in providers if provider.id == args.provider_id]
        if not matches:
            raise SystemExit(f"Unknown provider id: {args.provider_id}")
        provider = matches[0]
        if not provider.enabled:
            raise SystemExit(f"Provider is disabled in providers.toml: {provider.id}")
    else:
        provider = select_provider(
            data=data,
            providers=providers,
            task=args.task,
            exclude_ids=set(args.exclude_id),
            exclude_providers=set(args.exclude_provider),
            require_available=True,
        )
    cwd = Path(args.workdir).expanduser().resolve() if args.workdir else Path.cwd()
    try:
        returncode, stdout, stderr = run_provider(provider, args.prompt, cwd, args.timeout)
    except subprocess.TimeoutExpired:
        raise SystemExit(f"Provider timed out after {args.timeout}s: {provider.id}") from None
    if stdout:
        print(stdout)
    if returncode != 0:
        if stderr:
            print(stderr, file=sys.stderr)
        raise SystemExit(returncode)


def add_config_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project-root", help="Project root containing .heurema/rdlab/")
    parser.add_argument("--config", help="Explicit providers.toml path")


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List configured subscription providers")
    add_config_args(list_parser)
    list_parser.set_defaults(func=cmd_list)

    route_parser = subparsers.add_parser("route", help="Select a provider for a task")
    add_config_args(route_parser)
    route_parser.add_argument("--task", choices=TASKS, default="synthesis")
    route_parser.add_argument("--exclude-id", action="append", default=[], help="Provider id to skip")
    route_parser.add_argument("--exclude-provider", action="append", default=[], help="Provider family to skip")
    route_parser.add_argument("--allow-missing-command", action="store_true", help="Route even if CLI command is missing")
    route_parser.set_defaults(func=cmd_route)

    doctor_parser = subparsers.add_parser("doctor", help="Check provider CLI availability")
    add_config_args(doctor_parser)
    doctor_parser.add_argument("--probe", action="store_true", help="Send a short prompt to each enabled provider")
    doctor_parser.add_argument("--include-disabled", action="store_true", help="Include disabled providers")
    doctor_parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    doctor_parser.add_argument("--workdir", help="Working directory for provider prompt probes")
    doctor_parser.add_argument("--json", action="store_true", help="Print JSON results")
    doctor_parser.set_defaults(func=cmd_doctor)

    run_parser = subparsers.add_parser("run", help="Route and run one prompt")
    add_config_args(run_parser)
    run_parser.add_argument("--task", choices=TASKS, default="synthesis")
    run_parser.add_argument("--provider-id", help="Use a specific provider id")
    run_parser.add_argument("--exclude-id", action="append", default=[], help="Provider id to skip")
    run_parser.add_argument("--exclude-provider", action="append", default=[], help="Provider family to skip")
    run_parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    run_parser.add_argument("--workdir", help="Working directory for the provider invocation")
    run_parser.add_argument("--prompt", required=True)
    run_parser.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
