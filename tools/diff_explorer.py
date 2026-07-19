#!/usr/bin/env python3
"""Diff two Explorer index snapshots (raw/explorer/index.json) -> Markdown entry.

Usage:
    python tools/diff_explorer.py OLD.json NEW.json [--prepend CHANGELOG.md]
"""
from __future__ import annotations

import argparse
import datetime
import re
import json
import sys


def build_entry(old: dict, new: dict) -> str:
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(k for k in set(old) & set(new)
                     if old[k].get("sha256") != new[k].get("sha256"))

    today = datetime.date.today().isoformat()
    lines = [f"## explorer 全量轨道（{today}）", ""]
    lines.append(f"新增 {len(added)} · 移除 {len(removed)} · 定义变更 {len(changed)}"
                 f"（全量共 {len(new)} 个接口）")
    lines.append("")

    def fmt(key: str, src: dict) -> str:
        e = src[key]
        title = f"「{e['title']}」" if e.get("title") else ""
        path = re.sub(r":([A-Za-z_][\w]*)", r"{\1}", e.get("apiPath") or "?")
        return f"- `{e.get('httpMethod','?')} {path}`{title}（{key}）"

    for label, keys, src in (("新增接口", added, new),
                             ("移除接口", removed, old),
                             ("定义变更", changed, new)):
        if not keys:
            continue
        lines.append(f"### {label}")
        # keep the changelog readable: cap long lists
        for key in keys[:200]:
            lines.append(fmt(key, src))
        if len(keys) > 200:
            lines.append(f"- …… 其余 {len(keys) - 200} 条见 git diff")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--prepend", default=None)
    args = parser.parse_args()

    with open(args.old, encoding="utf-8") as f:
        old = json.load(f)
    with open(args.new, encoding="utf-8") as f:
        new = json.load(f)

    entry = build_entry(old, new)
    if args.prepend:
        try:
            with open(args.prepend, encoding="utf-8") as f:
                existing = f.read()
        except FileNotFoundError:
            existing = "# CHANGELOG\n\n"
        head, _, rest = existing.partition("\n\n")
        with open(args.prepend, "w", encoding="utf-8") as f:
            f.write(head + "\n\n" + entry + ("\n" + rest if rest else ""))
        print(f"changelog updated: {args.prepend}", file=sys.stderr)
    else:
        print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
