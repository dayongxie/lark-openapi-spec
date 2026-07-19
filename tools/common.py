"""Shared constants and helpers for lark-openapi-spec tools."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REGISTRY_URL_FEISHU = "https://open.feishu.cn/api/tools/open/api_definition"
REGISTRY_URL_LARK = "https://open.larksuite.com/api/tools/open/api_definition"

RAW_REGISTRY_PATH = PROJECT_ROOT / "raw" / "registry.json"
OPENAPI_DIR = PROJECT_ROOT / "openapi-curated"
SHORTCUTS_DIR = PROJECT_ROOT / "shortcuts"
MANIFEST_PATH = PROJECT_ROOT / "manifest.yaml"
CHANGELOG_PATH = PROJECT_ROOT / "CHANGELOG.md"

USER_AGENT = "lark-openapi-spec registry fetcher"

SERVERS = [
    {"url": "https://open.feishu.cn", "description": "飞书（中国大陆）"},
    {"url": "https://open.larksuite.com", "description": "Lark（国际版）"},
]


def fetch_registry(data_version: str | None = None, brand: str = "feishu",
                   client_version: str = "1.0.0", timeout: int = 30) -> dict:
    """Fetch the API registry from the same endpoint lark-cli uses.

    Returns the decoded envelope ``{"code", "msg", "data"}``. When
    ``data_version`` matches the server-side latest version, ``data`` has no
    ``services`` key (i.e. "not modified").
    """
    base = REGISTRY_URL_FEISHU if brand == "feishu" else REGISTRY_URL_LARK
    query = f"protocol=meta&client_version={client_version}"
    if data_version:
        query += f"&data_version={data_version}"
    req = urllib.request.Request(
        f"{base}?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    if payload.get("msg") != "succeeded":
        raise RuntimeError(f"registry endpoint returned: {payload.get('msg')!r}")
    return payload


def load_local_registry(path: Path = RAW_REGISTRY_PATH) -> dict:
    """Load the cached registry snapshot (the ``data`` section)."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_local_registry(data: dict, path: Path = RAW_REGISTRY_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


_MD_EQ = re.compile(r"==(.+?)==")


def clean_description(text: str | None) -> str:
    """Convert Feishu doc-markup into portable Markdown.

    The upstream metadata uses ``;`` / ``;;`` as line separators and
    ``==code==`` as inline-code markers.
    """
    if not text:
        return ""
    text = _MD_EQ.sub(r"`\1`", text)
    text = text.replace(";;", "\n\n").replace(";", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def summary_of(description: str, limit: int = 60) -> str:
    """First sentence / clause of a description, for use as operation summary."""
    first = re.split(r"[。；;\n]", description, maxsplit=1)[0].strip()
    if len(first) > limit:
        first = first[: limit - 1] + "…"
    return first or description[:limit]


def iter_methods(registry: dict):
    """Yield ``(service, resource_name, method_name, method)`` for every method,
    flattening nested resources. ``resource_name`` uses the dotted form exactly
    as it appears in the registry (e.g. ``chat.members``)."""
    for svc in registry.get("services") or []:
        yield from _walk_resources(svc, svc.get("resources") or {})


def _walk_resources(svc: dict, resources: dict):
    for rname, res in resources.items():
        for mname, method in (res.get("methods") or {}).items():
            yield svc, rname, mname, method
        yield from _walk_resources(svc, res.get("resources") or {})


def full_path(svc: dict, method: dict) -> str:
    return svc["servicePath"].rstrip("/") + "/" + method["path"].lstrip("/")
