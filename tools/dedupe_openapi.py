#!/usr/bin/env python3
"""Deduplicate repeated schemas in generated OpenAPI documents.

Per-API definitions arrive as self-contained trees, so shared structures
(e.g. docx Blocks) are repeated hundreds of times per file. This tool extracts
structurally identical subtrees into ``components/schemas`` and replaces
occurrences with ``$ref`` (descriptions are preserved via an ``allOf`` wrapper,
since OpenAPI 3.0 forbids siblings next to ``$ref``).

Algorithm: repeat passes until fixpoint — each pass hashes every object schema
(excluding descriptive-only keys), groups exact duplicates, extracts the
largest groups first, and replaces occurrences. Child extraction changes
parent structure, so nested repeats collapse over a few passes.

Only schemas worth the indirection are extracted (see MIN_WEIGHT / MIN_COUNT).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

# extraction thresholds
MIN_WEIGHT = 30   # subtree node count below this is not worth a component
MIN_COUNT = 2     # occurrences below this cannot be deduplicated
MAX_PASSES = 8

_IGNORED_KEYS = frozenset({"description", "example"})


# --------------------------------------------------------------------------
# structural hashing / weights
# --------------------------------------------------------------------------

def canonical(node):
    if isinstance(node, dict):
        return {k: canonical(v) for k, v in sorted(node.items())
                if k not in _IGNORED_KEYS}
    if isinstance(node, list):
        return [canonical(v) for v in node]
    return node


def struct_hash(node) -> str:
    return hashlib.sha256(
        json.dumps(canonical(node), sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


def weight(node) -> int:
    if isinstance(node, dict):
        return 1 + sum(weight(v) for v in node.values())
    if isinstance(node, list):
        return 1 + sum(weight(v) for v in node)
    return 1


# --------------------------------------------------------------------------
# occurrence collection (with replacement handles)
# --------------------------------------------------------------------------

class Occ:
    __slots__ = ("container", "key", "node", "hint")

    def __init__(self, container, key, node, hint):
        self.container = container   # parent dict or list
        self.key = key               # key in dict / index in list
        self.node = node
        self.hint = hint             # nearest property name (for naming)


def collect_occurrences(root) -> dict:
    """hash -> list[Occ] for every object schema under root."""
    groups: dict[str, list[Occ]] = {}

    def walk(node, hint=""):
        if isinstance(node, dict):
            if "$ref" in node:
                return  # already a reference — nothing to dedupe inside
            if node.get("type") == "object" and node.get("properties"):
                h = struct_hash(node)
                groups.setdefault(h, []).append(
                    Occ(_current_parent[0], _current_parent[1], node, hint))
            for k, v in node.items():
                _current_parent[:] = (node, k)
                walk(v, k)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                _current_parent[:] = (node, i)
                walk(v, hint)  # array items inherit the array's name hint

    _current_parent = [None, None]
    walk(root)
    return groups


# --------------------------------------------------------------------------
# naming
# --------------------------------------------------------------------------

def pascal(name: str) -> str:
    parts = re.split(r"[^A-Za-z0-9]+", name)
    out = "".join(p[:1].upper() + p[1:] for p in parts if p)
    return out or "SharedSchema"


def singular(name: str) -> str:
    if name.endswith("ies"):
        return name[:-3] + "y"
    if name.endswith("ses"):
        return name[:-2]
    if name.endswith("s") and not name.endswith("ss"):
        return name[:-1]
    return name


def pick_name(occurrences: list[Occ]) -> str:
    hints = [o.hint for o in occurrences if o.hint and o.hint != "items"]
    if not hints:
        hints = [o.hint for o in occurrences if o.hint]
    if not hints:
        return "SharedSchema"
    # most frequent hint wins; ties broken by shortest name, then
    # alphabetically — a total order keeps the pick deterministic
    # (max() over a bare set depends on hash randomization)
    best = min(set(hints), key=lambda h: (-hints.count(h), len(h), h))
    return pascal(singular(best))


# --------------------------------------------------------------------------
# replacement
# --------------------------------------------------------------------------

def make_ref(name: str, original: dict) -> dict:
    ref = {"$ref": f"#/components/schemas/{name}"}
    desc = original.get("description")
    example = original.get("example")
    if desc is None and example is None:
        return ref
    wrapped = {"allOf": [ref]}
    if desc is not None:
        wrapped["description"] = desc
    if example is not None:
        wrapped["example"] = example
    return wrapped


def dedupe_document(doc: dict, stats: dict | None = None) -> dict:
    components = doc.setdefault("components", {}).setdefault("schemas", {})
    paths = doc.get("paths") or {}
    extracted_total = 0

    for _pass in range(MAX_PASSES):
        groups = collect_occurrences(paths)
        candidates = [
            (h, occ) for h, occ in groups.items()
            if len(occ) >= MIN_COUNT and weight(occ[0].node) >= MIN_WEIGHT
        ]
        if not candidates:
            break
        # largest first for maximal early compression
        candidates.sort(key=lambda kv: weight(kv[1][0].node) * len(kv[1]),
                        reverse=True)
        for _h, occ in candidates:
            base = pick_name(occ)
            name, i = base, 2
            while name in components:
                name, i = f"{base}{i}", i + 1
            components[name] = occ[0].node
            for o in occ:
                o.container[o.key] = make_ref(name, o.node)
            extracted_total += 1
            if stats is not None:
                stats[name] = len(occ)

    return doc, extracted_total


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

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
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    for path in args.files:
        with open(path, encoding="utf-8") as f:
            # keep the 2-line generator header comments
            head = "".join(f.readline() for _ in range(2))
            doc = yaml.safe_load(head + f.read())
        before = path.stat().st_size
        doc, n = dedupe_document(doc)
        with open(path, "w", encoding="utf-8") as f:
            f.write(head)
            yaml.dump(doc, f, Dumper=_Dumper, allow_unicode=True,
                      sort_keys=False, width=120)
        after = path.stat().st_size
        print(f"{path.name}: {n} components extracted, "
              f"{before/1e6:.1f}MB -> {after/1e6:.1f}MB "
              f"({(1-after/before)*100:.0f}% smaller)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
