#!/usr/bin/env python3
"""Diff two registry snapshots and produce a Markdown changelog entry.

Usage:
    python tools/diff_registry.py OLD.json NEW.json [--version X] [--prepend CHANGELOG.md]

The entry lists added / removed / changed methods. A method is "changed" when
any of its semantic attributes differ (path, http method, fields, scopes,
risk, doc url...). Field-level details are included for changed methods.
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys


def method_map(registry: dict) -> dict:
    """key: (service, resource, method) -> method dict (+ inherited path)."""
    out = {}

    def walk(svc, resources):
        for rname, res in (resources or {}).items():
            for mname, m in (res.get("methods") or {}).items():
                m = dict(m)
                m["_full_path"] = svc["servicePath"].rstrip("/") + "/" + m["path"].lstrip("/")
                out[(svc["name"], rname, mname)] = m
            walk(svc, res.get("resources"))

    for svc in registry.get("services") or []:
        walk(svc, svc.get("resources"))
    return out


def field_diff(old: dict, new: dict) -> list[str]:
    """Human-readable per-field changes between two method dicts."""
    notes = []
    for section, label in (("parameters", "参数"), ("requestBody", "请求体"),
                           ("responseBody", "响应体")):
        o, n = old.get(section) or {}, new.get(section) or {}
        for name in sorted(set(n) - set(o)):
            notes.append(f"{label}新增字段 `{name}`")
        for name in sorted(set(o) - set(n)):
            notes.append(f"{label}移除字段 `{name}`")
        for name in sorted(set(o) & set(n)):
            if json.dumps(o[name], sort_keys=True, ensure_ascii=False) != \
               json.dumps(n[name], sort_keys=True, ensure_ascii=False):
                notes.append(f"{label}字段 `{name}` 定义变更")
    if (old.get("scopes") or []) != (new.get("scopes") or []):
        notes.append("权限 scopes 变更")
    if old.get("risk") != new.get("risk"):
        notes.append(f"风险等级 {old.get('risk')} → {new.get('risk')}")
    if old.get("_full_path") != new.get("_full_path"):
        notes.append(f"路径 {old.get('_full_path')} → {new.get('_full_path')}")
    if old.get("httpMethod") != new.get("httpMethod"):
        notes.append(f"HTTP 方法 {old.get('httpMethod')} → {new.get('httpMethod')}")
    if old.get("description") != new.get("description") and not notes:
        notes.append("描述更新")
    return notes


def build_entry(old: dict, new: dict, version: str | None) -> str:
    old_m, new_m = method_map(old), method_map(new)
    added = sorted(set(new_m) - set(old_m))
    removed = sorted(set(old_m) - set(new_m))
    changed = []
    for key in sorted(set(old_m) & set(new_m)):
        o, n = old_m[key], new_m[key]
        if json.dumps(o, sort_keys=True, ensure_ascii=False) != \
           json.dumps(n, sort_keys=True, ensure_ascii=False):
            changed.append((key, field_diff(o, n)))

    today = datetime.date.today().isoformat()
    version = version or new.get("version") or "unknown"
    lines = [f"## registry v{version}（{today}）", ""]
    lines.append(f"新增 {len(added)} · 移除 {len(removed)} · 变更 {len(changed)}")
    lines.append("")
    if added:
        lines.append("### 新增接口")
        for svc, res, m in added:
            lines.append(f"- `{new_m[(svc,res,m)]['httpMethod']} {new_m[(svc,res,m)]['_full_path']}`"
                         f"（{svc} / {res}.{m}）")
        lines.append("")
    if removed:
        lines.append("### 移除接口")
        for svc, res, m in removed:
            lines.append(f"- `{old_m[(svc,res,m)]['httpMethod']} {old_m[(svc,res,m)]['_full_path']}`"
                         f"（{svc} / {res}.{m}）")
        lines.append("")
    if changed:
        lines.append("### 变更接口")
        for (svc, res, m), notes in changed:
            lines.append(f"- `{new_m[(svc,res,m)]['httpMethod']} {new_m[(svc,res,m)]['_full_path']}`"
                         f"（{svc} / {res}.{m}）：{'；'.join(notes)}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--version", default=None)
    parser.add_argument("--prepend", default=None,
                        help="prepend the entry to this changelog file")
    args = parser.parse_args()

    with open(args.old, encoding="utf-8") as f:
        old = json.load(f)
    with open(args.new, encoding="utf-8") as f:
        new = json.load(f)

    entry = build_entry(old, new, args.version)
    if args.prepend:
        try:
            with open(args.prepend, encoding="utf-8") as f:
                existing = f.read()
        except FileNotFoundError:
            existing = "# CHANGELOG\n\n"
        head, sep, rest = existing.partition("\n\n")
        with open(args.prepend, "w", encoding="utf-8") as f:
            f.write(head + "\n\n" + entry + ("\n" + rest if rest else ""))
        print(f"changelog updated: {args.prepend}", file=sys.stderr)
    else:
        print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
