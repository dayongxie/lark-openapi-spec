#!/usr/bin/env python3
"""Fetch the official Feishu API Explorer catalog + per-API definitions.

Endpoints (public, no auth — the same ones open.feishu.cn/api-explorer uses):

    GET /api_explorer/v1/api_catalog
    GET /api_explorer/v1/api_definition?project=P&version=V&resource=R&apiName=A

Outputs:

    raw/explorer/catalog.json        full catalog tree (committed)
    raw/explorer/index.json          apiKey -> {identity, httpMethod, apiPath,
                                     title, category, sha256} (committed; the
                                     hash drives change detection)
    raw/explorer/defs/*.json         raw definitions (NOT committed — they are
                                     re-fetchable; .gitignore excludes them)

Definitions have no version field, so change detection is content-hash based:
every run re-fetches all definitions (polite concurrency), updates hashes, and
reports added / removed / changed APIs. A run keeps going past individual
fetch failures (the stale cache is kept) and only fails hard when the catalog
itself is unreachable or too many definitions fail.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://open.feishu.cn/api_explorer/v1"
USER_AGENT = "lark-openapi-spec explorer fetcher (github.com/dayongxie/lark-openapi-spec)"

CATALOG_PATH = Path("raw/explorer/catalog.json")
INDEX_PATH = Path("raw/explorer/index.json")
DEFS_DIR = Path("raw/explorer/defs")

MAX_FAILURE_RATIO = 0.05  # tolerate up to 5% definition fetch failures


def http_get(url: str, timeout: int = 30, retries: int = 3) -> dict:
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed after {retries} attempts: {last}")


def api_key(ident: dict) -> str:
    return f"{ident['project']}/{ident['version']}/{ident['resource']}/{ident['apiName']}"


def def_filename(ident: dict) -> str:
    return api_key(ident).replace("/", "__") + ".json"


# --------------------------------------------------------------------------
# Catalog
# --------------------------------------------------------------------------

def walk_catalog(items: list, trail=()):
    """Yield (identity_dict, summary, category_trail, node_name) for API leaves."""
    for node in items or []:
        name = node.get("name") or ""
        summary = node.get("apiSummary") or {}
        ident = summary.get("apiIdentity")
        if ident:
            yield ident, summary, trail, name
        yield from walk_catalog(node.get("children"), trail + (name,))


def fetch_catalog() -> tuple[list, dict]:
    payload = http_get(f"{BASE}/api_catalog")
    if payload.get("code") != 0:
        raise RuntimeError(f"api_catalog returned code={payload.get('code')}")
    items = (payload.get("data") or {}).get("items") or []
    index = {}
    for ident, summary, trail, node_name in walk_catalog(items):
        key = api_key(ident)
        index[key] = {
            "project": ident["project"],
            "version": ident["version"],
            "resource": ident["resource"],
            "apiName": ident["apiName"],
            "httpMethod": summary.get("httpMethod"),
            "apiPath": summary.get("apiPath"),
            "title": node_name or None,
            "category": " / ".join(t for t in trail if t),
            "docPath": summary.get("fullPath"),
            "sha256": None,  # filled from definition fetch
        }
    return items, index


# --------------------------------------------------------------------------
# Definitions
# --------------------------------------------------------------------------

def fetch_one(key: str, ident: dict) -> tuple[str, dict | None, str | None]:
    """Fetch one definition; returns (key, data, error)."""
    url = (f"{BASE}/api_definition?project={ident['project']}"
           f"&version={ident['version']}&resource={ident['resource']}"
           f"&apiName={ident['apiName']}")
    try:
        payload = http_get(url, timeout=30, retries=3)
        if payload.get("code") != 0:
            return key, None, f"code={payload.get('code')}"
        return key, payload.get("data"), None
    except Exception as exc:  # noqa: BLE001 — per-API failures are tolerable
        return key, None, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog-only", action="store_true",
                        help="only refresh catalog.json + index skeleton")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--out-dir", type=Path, default=Path("raw/explorer"))
    parser.add_argument("--limit", type=int, default=0,
                        help="only fetch the first N definitions (testing)")
    args = parser.parse_args()

    catalog_path = args.out_dir / "catalog.json"
    index_path = args.out_dir / "index.json"
    defs_dir = args.out_dir / "defs"
    defs_dir.mkdir(parents=True, exist_ok=True)

    # --- catalog -----------------------------------------------------------
    print("fetching catalog...", file=sys.stderr)
    items, index = fetch_catalog()
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"catalog: {len(index)} APIs across "
          f"{len({v['project'] for v in index.values()})} projects", file=sys.stderr)

    old_index = {}
    if index_path.exists():
        with open(index_path, encoding="utf-8") as f:
            old_index = json.load(f)

    if args.catalog_only:
        _write_index(index_path, index, old_index)
        return 0

    # --- definitions -------------------------------------------------------
    keys = sorted(index.keys())
    if args.limit:
        keys = keys[: args.limit]
    total = len(keys)
    print(f"fetching {total} definitions with {args.workers} workers...",
          file=sys.stderr)

    failures: list[tuple[str, str]] = []
    done = 0
    started = time.time()
    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(fetch_one, k, index[k]): k for k in keys}
        for fut in futures.as_completed(futs):
            key = futs[fut]
            key, data, error = fut.result()
            done += 1
            if error is not None or data is None:
                failures.append((key, error or "empty data"))
            else:
                out = defs_dir / def_filename(index[key])
                tmp = out.with_suffix(".tmp")
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, sort_keys=True)
                    f.write("\n")
                tmp.replace(out)
                raw = tmp.read_bytes() if tmp.exists() else out.read_bytes()
                index[key]["sha256"] = hashlib.sha256(raw).hexdigest()
            if done % 100 == 0:
                rate = done / max(time.time() - started, 0.01)
                print(f"  {done}/{total} ({rate:.1f}/s, {len(failures)} failed)",
                      file=sys.stderr)

    # carry over hashes for failed fetches so the diff stays quiet
    for key, _err in failures:
        if key in old_index and old_index[key].get("sha256"):
            index[key]["sha256"] = old_index[key]["sha256"]
            index[key]["title"] = old_index[key].get("title")

    ratio = len(failures) / max(total, 1)
    if failures:
        print(f"{len(failures)} failures ({ratio:.1%}):", file=sys.stderr)
        for key, err in failures[:20]:
            print(f"  {key}: {err}", file=sys.stderr)
    if ratio > MAX_FAILURE_RATIO and total > 20:
        print("error: too many definition fetch failures, keeping old index",
              file=sys.stderr)
        return 1

    _write_index(index_path, index, old_index)

    added = sorted(set(index) - set(old_index))
    removed = sorted(set(old_index) - set(index))
    changed = sorted(k for k in set(index) & set(old_index)
                     if index[k].get("sha256") != old_index[k].get("sha256"))
    summary = {"total": total, "added": len(added), "removed": len(removed),
               "changed": len(changed), "failures": len(failures)}
    print(f"done: {json.dumps(summary)}", file=sys.stderr)
    # machine-readable summary on stdout for CI
    print(json.dumps({"added": added, "removed": removed, "changed": changed,
                      **{k: summary[k] for k in ('total', 'failures')}}))
    return 0


def _write_index(index_path: Path, index: dict, old_index: dict) -> None:
    # preserve hashes/titles from the old index for entries not refreshed
    for key, entry in index.items():
        if entry.get("sha256") is None and key in old_index:
            entry["sha256"] = old_index[key].get("sha256")
            entry["title"] = old_index[key].get("title")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"index -> {index_path} ({len(index)} entries)", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
