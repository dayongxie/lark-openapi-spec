#!/usr/bin/env python3
"""Extract lark-cli shortcut (+) command references into YAML.

The shortcuts are hand-written Go commands, so their public contract is the
CLI help output itself. This tool parses:

  lark-cli --help                      -> the list of domains
  lark-cli <domain> --help             -> the domain's shortcut list
  lark-cli <domain> +<name> --help     -> description, usage, flags, risk

Output: one YAML per domain in shortcuts/.

The parsing is deliberately tolerant: unrecognised lines are skipped, never
fatal, so a help-format change degrades output quality instead of breaking
the pipeline.
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

import yaml

from common import SHORTCUTS_DIR, _MD_EQ


def clean_text(text: str | None) -> str:
    """Tidy help-output text: convert ``==code==`` markers, keep punctuation.

    Unlike the registry metadata, CLI help text uses ``;`` as ordinary
    punctuation, so no line-separator conversion is applied here.
    """
    if not text:
        return ""
    return _MD_EQ.sub(r"`\1`", text).strip()

DOMAIN_LINE = re.compile(r"^  ([a-z][\w-]*)\s{2,}(.+)$")
SHORTCUT_LINE = re.compile(r"^  (\+\S+)\s{2,}(.+)$")
FLAG_LINE = re.compile(r"^\s+(?:-([a-zA-Z]),\s+)?--([\w-]+)(?:\s+(\w+))?\s{2,}(.*)$")
DEFAULT_RE = re.compile(r'\s*\(default ("[^"]*"|[^)]+)\)\s*$')


def run_help(cli: str, *args: str) -> str:
    result = subprocess.run([cli, *args, "--help"], capture_output=True,
                            text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(f"{cli} {' '.join(args)} --help failed: {result.stderr[:200]}")
    return result.stdout


def parse_domains(help_text: str) -> list[dict]:
    domains, in_section = [], False
    for line in help_text.splitlines():
        if line.startswith("Lark domains:"):
            in_section = True
            continue
        if in_section:
            if not line.strip():
                break
            m = DOMAIN_LINE.match(line)
            if m:
                domains.append({"name": m.group(1), "description": m.group(2).strip()})
    return domains


def parse_shortcut_list(help_text: str) -> list[dict]:
    shortcuts, in_section = [], False
    for line in help_text.splitlines():
        if line.startswith("Available Commands:"):
            in_section = True
            continue
        if in_section:
            if not line.strip():
                break
            m = SHORTCUT_LINE.match(line)
            if m:
                shortcuts.append({"name": m.group(1), "summary": m.group(2).strip()})
    return shortcuts


def parse_shortcut_help(help_text: str) -> dict:
    lines = help_text.splitlines()
    desc_lines, usage, risk = [], None, None
    flags, section = [], "desc"
    current_flag = None

    for line in lines:
        if line.startswith("Usage:"):
            section = "usage"
            continue
        if line.startswith("Flags:"):
            section = "flags"
            continue
        if line.startswith("Risk:"):
            risk = line.split(":", 1)[1].strip()
            section = "done"
            continue
        if section == "desc":
            if line.strip():
                desc_lines.append(line.strip())
        elif section == "usage":
            stripped = line.strip()
            if stripped and usage is None:
                usage = stripped
            elif not stripped and usage is not None:
                section = "pre-flags"
        elif section == "flags":
            m = FLAG_LINE.match(line)
            if m:
                default = None
                text = m.group(4).strip()
                dm = DEFAULT_RE.search(text)
                if dm:
                    default = dm.group(1).strip('"')
                    text = DEFAULT_RE.sub("", text).strip()
                current_flag = {
                    "name": "--" + m.group(2),
                    "shorthand": ("-" + m.group(1)) if m.group(1) else None,
                    "type": m.group(3) or "bool",
                    "description": clean_text(text),
                }
                if default is not None:
                    current_flag["default"] = default
                flags.append(current_flag)
            elif current_flag is not None and line.startswith(" " * 12) and line.strip():
                # continuation of the previous flag's description
                current_flag["description"] += " " + line.strip()
    return {
        "description": clean_text(" ".join(desc_lines)),
        "usage": usage,
        "risk": risk,
        "flags": flags,
    }


class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_representer)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", default="lark-cli", help="path to the lark-cli binary")
    parser.add_argument("--out-dir", type=Path, default=SHORTCUTS_DIR)
    parser.add_argument("--cli-version", default="unknown")
    args = parser.parse_args()

    extracted_at = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")

    domains = parse_domains(run_help(args.cli))
    print(f"{len(domains)} domains found", file=sys.stderr)

    total = 0
    for domain in domains:
        name = domain["name"]
        try:
            shortcuts = parse_shortcut_list(run_help(args.cli, name))
        except Exception as exc:
            print(f"  {name}: skipped ({exc})", file=sys.stderr)
            continue
        if not shortcuts:
            continue
        entries = []
        for sc in shortcuts:
            try:
                detail = parse_shortcut_help(run_help(args.cli, name, sc["name"]))
            except Exception as exc:
                print(f"  {name} {sc['name']}: detail skipped ({exc})", file=sys.stderr)
                detail = {"description": "", "usage": None, "risk": None, "flags": []}
            entry = {"name": sc["name"], "summary": sc["summary"]}
            entry.update(detail)
            entries.append(entry)
        doc = {
            "domain": name,
            "description": domain["description"],
            "cli_version": args.cli_version,
            "extracted_at": extracted_at,
            "note": "从 lark-cli --help 输出自动提取，仅供参考；字段语义以上游 CLI 为准。",
            "shortcuts": entries,
        }
        out = args.out_dir / f"{name}.yaml"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Generated from lark-cli help output — DO NOT EDIT BY HAND.\n")
            yaml.dump(doc, f, Dumper=_Dumper, allow_unicode=True,
                      sort_keys=False, width=120)
        total += len(entries)
        print(f"  {name:12s} -> {len(entries)} shortcuts", file=sys.stderr)

    print(f"{total} shortcuts extracted", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
