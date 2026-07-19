#!/usr/bin/env python3
"""Fetch / check the lark-cli API registry.

Modes:
  (default)     Full fetch — always downloads the latest registry snapshot
                and writes it to raw/registry.json.
  --check       Incremental check — sends the locally recorded data_version;
                the server returns an empty payload when nothing changed.
                Prints ``changed=true|false`` and ``version=<v>`` (also to
                $GITHUB_OUTPUT when set). Exit code is always 0 unless the
                endpoint itself failed.
"""
from __future__ import annotations

import argparse
import os
import sys

from common import RAW_REGISTRY_PATH, fetch_registry, load_local_registry, save_local_registry


def _emit(changed: bool, version: str) -> None:
    print(f"changed={'true' if changed else 'false'}")
    print(f"version={version}")
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")
            f.write(f"version={version}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="incremental check against the local data_version")
    parser.add_argument("--out", default=str(RAW_REGISTRY_PATH),
                        help="output path for the registry snapshot")
    parser.add_argument("--brand", default="feishu", choices=["feishu", "lark"],
                        help="which platform endpoint to query")
    args = parser.parse_args()

    local_version = None
    if args.check:
        try:
            local_version = load_local_registry().get("version")
        except FileNotFoundError:
            local_version = None  # first run -> full fetch

    try:
        payload = fetch_registry(data_version=local_version, brand=args.brand)
    except Exception as exc:  # endpoint failure must fail the CI step loudly
        print(f"error: registry fetch failed: {exc}", file=sys.stderr)
        return 1

    data = payload.get("data") or {}
    services = data.get("services")
    version = data.get("version") or local_version or "unknown"

    if args.check and local_version and services is None:
        _emit(changed=False, version=version)
        print("registry is up to date", file=sys.stderr)
        return 0

    if not services:
        # Defensive: server returned a version but no services on a full fetch.
        print("error: endpoint returned no services", file=sys.stderr)
        return 1

    save_local_registry(data)
    _emit(changed=True, version=version)
    n = sum(1 for svc in services for _ in [svc])
    print(f"saved registry v{version} ({n} services) -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
