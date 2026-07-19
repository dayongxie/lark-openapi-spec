#!/usr/bin/env python3
"""Extract HTTP API definitions from lark-cli's Go source code.

lark-cli shortcut commands (``lark-cli im +chat-list`` ...) are implemented as
``common.Shortcut`` struct literals under ``shortcuts/``. Each carries rich
metadata (description, risk, scopes, auth types, flags, tips) and calls one
(or more) ``/open-apis/...`` endpoints. Roughly a hundred of these endpoints
are NOT documented in the official API Explorer (Base v3, docs_ai, slides_ai,
sheet_ai, spark, ...), so this track complements the Explorer full track.

The extractor is regex/heuristic based — Go is not parsed with a real AST —
so the output is an approximation and is marked ``x-lark-source: lark-cli-go``:

- path params come from the path template (``:id`` / ``{id}`` / ``<id>`` /
  ``%s`` styles);
- for GET/DELETE, flags become query parameters; for POST/PUT/PATCH they
  become request-body properties (CLI-side flags like --json/--format are
  excluded);
- responses use the generic Feishu envelope (code/msg/data) since the Go
  code does not declare response schemas.

Usage:

    python tools/extract_go_apis.py --src /path/to/lark-cli --out-dir openapi-go
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

GENERATOR = "lark-openapi-spec tools/extract_go_apis.py"

SERVERS = [
    {"url": "https://open.feishu.cn", "description": "飞书（中国大陆）"},
    {"url": "https://open.larksuite.com", "description": "Lark（国际版）"},
]

# flags that control the CLI itself, not the HTTP request
CLI_ONLY_FLAGS = {
    "json", "format", "as", "output", "dry-run", "yes", "force",
    "page-limit", "limit-pages", "max-pages", "compact", "verbose",
}

# HTTP method builder calls: POST("/open-apis/...") / GET(...)
# (also with an fmt.Sprintf wrapper around the literal)
RE_BUILDER = re.compile(
    r'\b(GET|POST|PUT|PATCH|DELETE)\(\s*(?:fmt\.Sprintf\(\s*)?'
    r'"(/open-apis/[^"]+)"')
# builder calls over an identifier: POST(somePathConst) / GET(path)
RE_BUILDER_IDENT = re.compile(
    r'\b(GET|POST|PUT|PATCH|DELETE)\(\s*([A-Za-z_]\w*)\s*\)')
# DoAPIJSON*(http.MethodPost, "/open-apis/...", ...)
RE_DOAPI = re.compile(
    r'DoAPIJSON\w*\(\s*http\.Method(Get|Post|Put|Patch|Delete)\s*,\s*'
    r'(?:fmt\.Sprintf\(\s*)?((?:"/open-apis/[^"]+")|(?:[A-Za-z_]\w*))')
# CallAPITyped("POST", somePath, ...)
RE_CALLAPI = re.compile(
    r'CallAPI\w*\(\s*"(GET|POST|PUT|PATCH|DELETE)"\s*,\s*'
    r'(?:fmt\.Sprintf\(\s*)?((?:"/open-apis/[^"]+")|(?:[A-Za-z_]\w*))')
# generic string literal that looks like an API path
RE_PATH_STR = re.compile(r'"(/open-apis/[^"]+)"')
# const / package-var path declarations: const x = "/open-apis/..." (or expr)
RE_PATH_CONST = re.compile(
    r'(?:const|var)\s+([A-Za-z_]\w*)\s*=\s*([^\n]*"/open-apis/[^\n]*)')

RE_SHORTCUT_VAR = re.compile(r'var\s+(\w+)\s*=\s*common\.Shortcut\{')
RE_FUNC_DEF = re.compile(
    r'func\s+(\w+)\s*\([^)]*\)\s*(?:\*?common\.\w+\s*)?\{')
RE_FLAG_HELPER = re.compile(
    r'func\s+(\w+)\s*\(([^)]*)\)\s*common\.Flag\s*\{\s*'
    r'return\s+common\.Flag\{', re.S)
RE_STRINGS_HELPER = re.compile(
    r'func\s+(\w+)\s*\(\s*\)\s*\[\]string\s*\{\s*'
    r'return\s*\[\]string\{([^}]*)\}', re.S)

FIELD_RE = {
    "Name": re.compile(r'\bName:\s*"([^"]*)"'),
    "Type": re.compile(r'\bType:\s*"([^"]*)"'),
    "Default": re.compile(r'\bDefault:\s*"([^"]*)"'),
    "Desc": re.compile(r'\bDesc:\s*((?:`[^`]*`|"(?:[^"\\]|\\.)*"))'),
    "Required": re.compile(r'\bRequired:\s*(\w+)'),
    "Hidden": re.compile(r'\bHidden:\s*(true|false)'),
    "Enum": re.compile(r'\bEnum:\s*\[\]string\{([^}]*)\}', re.S),
}

GO_TYPE_MAP = {
    "": "string",
    "string": "string",
    "int": "integer",
    "int64": "integer",
    "float": "number",
    "bool": "boolean",
    "string_slice": "array",
    "string_array": "array",
    "json": "object",
}


# ---------------------------------------------------------------------------
# small Go-literal parsing helpers
# ---------------------------------------------------------------------------

def find_matching_brace(text: str, open_idx: int) -> int:
    """Return the index just past the brace matching text[open_idx]."""
    depth = 0
    i = open_idx
    in_str = None  # '"', '`'
    while i < len(text):
        ch = text[i]
        if in_str:
            if in_str == '"' and ch == "\\":
                i += 2
                continue
            if ch == in_str:
                in_str = None
        else:
            if ch in ('"', '`'):
                in_str = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    return len(text)


def split_top_level(text: str, sep: str = ",") -> list[str]:
    """Split on sep at brace/bracket depth 0, ignoring strings."""
    parts, depth, in_str, start, i = [], 0, None, 0, 0
    while i < len(text):
        ch = text[i]
        if in_str:
            if in_str == '"' and ch == "\\":
                i += 2
                continue
            if ch == in_str:
                in_str = None
        else:
            if ch in ('"', '`'):
                in_str = ch
            elif ch in "{[":
                depth += 1
            elif ch in "}]":
                depth -= 1
            elif ch == sep and depth == 0:
                parts.append(text[start:i])
                start = i + 1
        i += 1
    tail = text[start:].strip()
    if tail:
        parts.append(text[start:])
    return parts


def unquote(lit: str) -> str:
    lit = lit.strip()
    if lit.startswith("`") and lit.endswith("`"):
        return lit[1:-1]
    if lit.startswith('"') and lit.endswith('"'):
        try:
            return json.loads(lit)
        except json.JSONDecodeError:
            return lit[1:-1]
    return lit


def parse_string_list(body: str) -> list[str]:
    return [unquote(p) for p in split_top_level(body) if p.strip()]


# ---------------------------------------------------------------------------
# flag helpers: `func xFlag(required bool) common.Flag { return common.Flag{`
# ---------------------------------------------------------------------------

def collect_string_consts(pkg_sources: dict[str, str]) -> dict[str, str]:
    """Package-level string constants, incl. const ( ... ) blocks."""
    consts: dict[str, str] = {}
    single = re.compile(r'(?:const|var)\s+(\w+)\s*(?:string\s*)?=\s*"([^"]*)"')
    blocked = re.compile(r'^\s*(\w+)\s*(?:string\s*)?=\s*"([^"]*)"')
    for src in pkg_sources.values():
        for m in single.finditer(src):
            consts.setdefault(m.group(1), m.group(2))
        in_block = False
        for line in src.splitlines():
            if re.match(r'^(const|var)\s*\($', line.strip()[:7].rstrip()):
                in_block = True
                continue
            if in_block:
                if line.strip() == ")":
                    in_block = False
                    continue
                m = blocked.match(line)
                if m:
                    consts.setdefault(m.group(1), m.group(2))
    return consts


def parse_flag_literal(text: str, bool_args: dict[str, bool] | None = None,
                       str_consts: dict[str, str] | None = None) -> dict:
    """Parse the fields of a common.Flag{...} literal body."""
    bool_args = bool_args or {}
    str_consts = str_consts or {}
    flag: dict = {}
    for field, rx in FIELD_RE.items():
        m = rx.search(text)
        if not m:
            # Name/Type/Default may reference a string constant
            if field in ("Name", "Type", "Default"):
                m2 = re.search(rf'\b{field}:\s*([A-Za-z_]\w*)', text)
                if m2 and m2.group(1) in str_consts:
                    flag[field.lower()] = str_consts[m2.group(1)]
            continue
        raw = m.group(1)
        if field == "Enum":
            flag["enum"] = parse_string_list(raw)
        elif field in ("Required", "Hidden"):
            if raw in bool_args:
                flag[field.lower()] = bool_args[raw]
            elif raw in ("true", "false"):
                flag[field.lower()] = raw == "true"
        elif field == "Desc":
            flag["desc"] = unquote(raw)
        else:
            flag[field.lower()] = raw
    return flag


RE_ANY_FLAG_HELPER = re.compile(
    r'func\s+(\w+)\s*\(([^)]*)\)\s*common\.Flag\s*\{')
RE_DELEGATE = re.compile(r'\bflag\s*:=\s*(\w+)\(([^)]*)\)')
RE_OVERRIDE = re.compile(
    r'\bflag\.(Name|Type|Default|Desc|Required|Hidden)\s*=\s*'
    r'((?:`[^`]*`|"(?:[^"\\]|\\.)*")|true|false)')


def collect_flag_helpers(sources: dict[str, str]) -> dict[str, dict]:
    """Map helper-func name -> parsed helper (direct literal or delegate)."""
    helpers = {}
    for src in sources.values():
        for m in RE_ANY_FLAG_HELPER.finditer(src):
            name, args = m.group(1), m.group(2)
            open_brace = m.end() - 1
            body = src[open_brace + 1: find_matching_brace(src, open_brace) - 1]
            arg_names = [a.split()[0] for a in args.split(",") if a.strip()]
            ret = re.search(r'return\s+common\.Flag\{', body)
            if ret:
                ob = body.index("{", ret.end() - 1)
                helpers[name] = {
                    "kind": "literal", "args": arg_names,
                    "body": body[ob + 1: find_matching_brace(body, ob) - 1]}
                continue
            deleg = RE_DELEGATE.search(body)
            if deleg:
                overrides = {}
                for om in RE_OVERRIDE.finditer(body):
                    val = om.group(2)
                    if val in ("true", "false"):
                        overrides[om.group(1).lower()] = val == "true"
                    else:
                        overrides[om.group(1).lower()] = unquote(val)
                helpers[name] = {
                    "kind": "delegate", "args": arg_names,
                    "delegate": deleg.group(1), "delegate_args": deleg.group(2),
                    "overrides": overrides}
    return helpers


def resolve_flag_helper(helpers: dict, call: str,
                        str_consts: dict[str, str] | None = None,
                        _depth: int = 0) -> dict | None:
    """Resolve a call like baseTokenFlag(true) to a flag dict."""
    if _depth > 4:
        return None
    m = re.match(r"(\w+)\(([^)]*)\)", call.strip())
    if not m:
        return None
    name, argstr = m.group(1), m.group(2)
    helper = helpers.get(name)
    if not helper:
        return None
    bool_args = {}
    for arg_name, arg_val in zip(helper["args"], split_top_level(argstr)):
        v = arg_val.strip()
        if v in ("true", "false"):
            bool_args[arg_name] = v == "true"
    if helper["kind"] == "literal":
        return parse_flag_literal(helper["body"], bool_args, str_consts)
    base = resolve_flag_helper(
        helpers, f"{helper['delegate']}({helper['delegate_args']})",
        str_consts, _depth + 1)
    if base is None:
        return None
    for k, v in helper["overrides"].items():
        base["desc" if k == "desc" else k] = v
    return base


# ---------------------------------------------------------------------------
# shortcut struct parsing
# ---------------------------------------------------------------------------

def parse_shortcut(body: str, helpers: dict, str_helpers: dict,
                   str_consts: dict | None = None) -> dict:
    """Parse the body of a common.Shortcut{...} literal."""
    sc: dict = {"flags": [], "tips": []}
    for field in ("Service", "Command", "Description", "Risk"):
        m = re.search(rf'\b{field}:\s*((?:`[^`]*`|"(?:[^"\\]|\\.)*"))', body)
        if m:
            sc[field.lower()] = unquote(m.group(1))
    m = re.search(r'\bScopes:\s*\[\]string\{([^}]*)\}', body, re.S)
    if m:
        sc["scopes"] = parse_string_list(m.group(1))
    m = re.search(r'\bAuthTypes:\s*(?:\[\]string\{([^}]*)\}|(\w+)\(\))', body, re.S)
    if m:
        if m.group(1) is not None:
            sc["auth_types"] = parse_string_list(m.group(1))
        elif m.group(2) in str_helpers:
            sc["auth_types"] = str_helpers[m.group(2)]

    m = re.search(r'\bFlags:\s*\[\]common\.Flag\{', body)
    if m:
        open_idx = body.index("[", m.start()) + 1  # after []common.Flag
        open_brace = body.index("{", m.end() - 1)
        flags_body = body[open_brace + 1: find_matching_brace(body, open_brace) - 1]
        for item in split_top_level(flags_body):
            item = item.strip()
            if not item:
                continue
            if item.startswith("{"):
                sc["flags"].append(parse_flag_literal(item, str_consts=str_consts))
            else:
                resolved = resolve_flag_helper(helpers, item, str_consts)
                if resolved:
                    sc["flags"].append(resolved)

    m = re.search(r'\bTips:\s*\[\]string\{', body)
    if m:
        open_brace = body.index("{", m.end() - 1)
        tips_body = body[open_brace + 1: find_matching_brace(body, open_brace) - 1]
        sc["tips"] = [unquote(p) for p in split_top_level(tips_body) if p.strip()]

    for field in ("DryRun", "Execute"):
        m = re.search(rf'\b{field}:\s*(\w+),', body)
        if m:
            sc[field.lower()] = m.group(1)
    return sc


# ---------------------------------------------------------------------------
# HTTP method + path resolution
# ---------------------------------------------------------------------------

def normalize_path(raw: str) -> tuple[str, dict[str, str]]:
    """Normalize :id / {id} / <id> / %s styles to {id}; split baked-in query.

    Returns (path, fixed_query_params).
    """
    path, _, query = raw.partition("?")
    path = path.rstrip("/")
    # <param> (sometimes with prose) and fmt verbs become named params
    path = re.sub(r"<([^>]+)>", lambda m: "{" + re.sub(r"\W+", "_", m.group(1)).strip("_") + "}", path)
    # %s / %v -> name derived from the preceding path segment
    def fmt_sub(match):
        prev = match.group(1)
        base = re.sub(r"s$", "", prev) if prev else "param"
        return f"{prev}/{{{base}_id}}"
    path = re.sub(r"/(\w[\w-]*)/%[sv]", lambda m: fmt_sub(m), path)
    path = re.sub(r":([A-Za-z_]\w*)", r"{\1}", path)
    fixed = {}
    if query:
        for kv in query.split("&"):
            if "=" in kv:
                k, v = kv.split("=", 1)
                fixed[k] = v
    return path, fixed


def collect_path_consts(pkg_sources: dict[str, str]) -> dict[str, str]:
    """Resolve package-level path constants, including simple concatenation.

    const slashCommandBasePath = "/open-apis/application/v7/app_slash_commands"
    const recordsPath = basePath + "/records"
    """
    raw: dict[str, str] = {}
    for src in pkg_sources.values():
        for m in RE_PATH_CONST.finditer(src):
            raw.setdefault(m.group(1), m.group(2).strip())
    resolved: dict[str, str] = {}

    def try_resolve(expr: str) -> str | None:
        parts = [p.strip() for p in expr.split("+")]
        out = []
        for p in parts:
            if p.startswith('"'):
                m = re.match(r'"([^"]*)"', p)
                if m is None:
                    return None
                out.append(m.group(1))
            elif p in resolved:
                out.append(resolved[p])
            else:
                return None
        joined = "".join(out)
        return joined if joined.startswith("/open-apis/") else None

    for _ in range(4):  # a few rounds for chained constants
        progressed = False
        for name, expr in raw.items():
            if name in resolved:
                continue
            val = try_resolve(expr)
            if val is not None:
                resolved[name] = val
                progressed = True
        if not progressed:
            break
    return resolved


def _resolve_ident_path(ident: str, text: str,
                        consts: dict[str, str]) -> str | None:
    if ident in consts:
        return consts[ident]
    # local variable: path := "/open-apis/..." (maybe + params.Encode())
    m = re.search(rf'\b{re.escape(ident)}\s*:?=\s*"(/open-apis/[^"]*)"', text)
    if m:
        return m.group(1).rstrip("?")
    return None


def find_apis_in(text: str, consts: dict[str, str] | None = None
                 ) -> list[tuple[str, str]]:
    """All (method, raw_path) call sites in source order."""
    consts = consts or {}
    found = []
    for m in RE_BUILDER.finditer(text):
        found.append((m.start(), m.group(1), m.group(2)))
    for rx in (RE_DOAPI, RE_CALLAPI):
        for m in rx.finditer(text):
            arg = m.group(2)
            if arg.startswith('"'):
                path = arg.strip('"')
            else:
                path = _resolve_ident_path(arg, text, consts)
            if path:
                found.append((m.start(), m.group(1).upper(), path))
    for m in RE_BUILDER_IDENT.finditer(text):
        path = _resolve_ident_path(m.group(2), text, consts)
        if path:
            found.append((m.start(), m.group(1), path))
    found.sort()
    seen, out = set(), []
    for _, method, path in found:
        if (method, path) not in seen:
            seen.add((method, path))
            out.append((method, path))
    return out


def resolve_api(struct_body: str, sc: dict, file_src: str,
                pkg_sources: dict[str, str],
                consts: dict[str, str]) -> tuple[str, str] | None:
    """Pick the primary (method, path) for a shortcut."""
    # 1. calls inside the struct literal itself (anonymous DryRun/Execute)
    calls = find_apis_in(struct_body, consts)
    if calls:
        return calls[0]
    # 2. the named DryRun / Execute function body (one helper hop allowed)
    for fname in (sc.get("dryrun"), sc.get("execute")):
        if not fname:
            continue
        for src in pkg_sources.values():
            m = re.search(rf'func\s+{re.escape(fname)}\s*\(', src)
            if not m:
                continue
            open_brace = src.index("{", m.end() - 1)
            body = src[open_brace: find_matching_brace(src, open_brace)]
            calls = find_apis_in(body, consts)
            if calls:
                return calls[0]
            # body delegates to another local func (e.g. dryRunViewGetCard
            # -> dryRunViewGetProperty): follow one hop, package-wide
            for callee in set(re.findall(r'\b([a-z]\w+)\(', body)):
                if callee in ("if", "for", "return", "fmt", "runtime"):
                    continue
                for src2 in pkg_sources.values():
                    m2 = re.search(rf'func\s+{re.escape(callee)}\s*\(', src2)
                    if not m2:
                        continue
                    ob2 = src2.index("{", m2.end() - 1)
                    body2 = src2[ob2: find_matching_brace(src2, ob2)]
                    calls = find_apis_in(body2, consts)
                    if calls:
                        return calls[0]
    # 3. any call in the same file
    calls = find_apis_in(file_src, consts)
    if calls:
        return calls[0]
    return None


# ---------------------------------------------------------------------------
# OpenAPI operation construction
# ---------------------------------------------------------------------------

def flag_to_schema(flag: dict) -> dict:
    schema: dict = {"type": GO_TYPE_MAP.get(flag.get("type", ""), "string")}
    if schema["type"] == "array":
        schema["items"] = {"type": "string"}
    if flag.get("enum"):
        schema["enum"] = flag["enum"]
    if flag.get("default") not in (None, ""):
        d = flag["default"]
        if schema["type"] == "integer":
            try:
                d = int(d)
            except ValueError:
                pass
        elif schema["type"] == "boolean":
            d = d.lower() == "true"
        # upstream sometimes mixes CLI-style defaults with Go-style enum
        # values ('remote-wins' vs driveSyncOnConflictRemoteWins)
        if schema.get("enum") and d not in schema["enum"]:
            pass
        else:
            schema["default"] = d
    if flag.get("desc"):
        schema["description"] = flag["desc"]
    return schema


def build_operation(sc: dict, method: str, path: str,
                    fixed_query: dict) -> dict:
    desc_parts = [sc.get("description", "")]
    if sc.get("tips"):
        desc_parts.append("\n\n**Tips（来自 lark-cli 源码）**\n")
        desc_parts.extend(f"- {t}" for t in sc["tips"])
    op: dict = {
        "operationId": re.sub(
            r"\W+", "_",
            f"{sc.get('service', 'x')}_{sc.get('command', 'x').lstrip('+')}"),
        "summary": sc.get("description", ""),
        "description": "\n".join(desc_parts).strip(),
        "tags": [sc.get("service", "")],
        "x-lark-cli-command": f"lark-cli {sc.get('service', '')} "
                              f"{sc.get('command', '')}".strip(),
        "x-lark-source": "lark-cli-go",
    }
    if sc.get("risk"):
        op["x-lark-risk"] = sc["risk"]
    if sc.get("scopes"):
        op["x-lark-scopes"] = sc["scopes"]
    if sc.get("auth_types"):
        op["x-lark-access-tokens"] = [
            "user_access_token" if a == "user" else "tenant_access_token"
            for a in sc["auth_types"]]

    path_params = re.findall(r"\{([^}]+)\}", path)
    flags = [f for f in sc["flags"]
             if f.get("name") and not f.get("hidden")
             and f["name"] not in CLI_ONLY_FLAGS]

    params = []
    body_props: dict[str, dict] = {}
    required_body: list[str] = []
    used_flags: set[str] = set()

    def snake(name: str) -> str:
        return name.replace("-", "_")

    # path params: match a flag when possible (for its description)
    for pp in path_params:
        flag = next((f for f in flags if snake(f["name"]) == pp), None)
        if flag:
            used_flags.add(flag["name"])
        schema = flag_to_schema(flag) if flag else {"type": "string"}
        schema.pop("default", None)
        schema.pop("enum", None) if not flag else None
        params.append({
            "name": pp, "in": "path", "required": True,
            "schema": schema if flag else {"type": "string"},
            **({"description": flag["desc"]} if flag and flag.get("desc") else {}),
        })
    # baked-in fixed query params
    for k, v in fixed_query.items():
        params.append({"name": k, "in": "query", "required": True,
                       "schema": {"type": "string", "enum": [v], "default": v},
                       "description": "固定值（lark-cli 源码中硬编码）"})
    # remaining flags -> query (GET/DELETE) or body (others)
    for flag in flags:
        if flag["name"] in used_flags:
            continue
        if method in ("GET", "DELETE"):
            p = {"name": snake(flag["name"]), "in": "query",
                 "required": bool(flag.get("required")),
                 "schema": flag_to_schema(flag)}
            params.append(p)
        else:
            body_props[snake(flag["name"])] = flag_to_schema(flag)
            if flag.get("required"):
                required_body.append(snake(flag["name"]))
    if params:
        seen_param: set[tuple] = set()
        unique_params = []
        for p in params:
            k = (p["name"], p["in"])
            if k not in seen_param:
                seen_param.add(k)
                unique_params.append(p)
        op["parameters"] = unique_params
    if body_props:
        op["requestBody"] = {
            "required": bool(required_body),
            "content": {"application/json": {"schema": {
                "type": "object", "properties": body_props,
                **({"required": required_body} if required_body else {})}}},
        }
    op["responses"] = {"200": {
        "description": "飞书标准响应信封（data 结构未在 lark-cli 源码中声明）",
        "content": {"application/json": {"schema": {
            "type": "object",
            "properties": {
                "code": {"type": "integer"},
                "msg": {"type": "string"},
                "data": {"type": "object"},
            }}}},
    }}
    return op


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=Path, required=True,
                        help="lark-cli source tree root")
    parser.add_argument("--out-dir", type=Path, default=Path("openapi-go"))
    parser.add_argument("--cli-version", default="unknown")
    parser.add_argument("--manifest", type=Path, default=Path("manifest.yaml"))
    args = parser.parse_args()

    shortcuts_dir = args.src / "shortcuts"
    if not shortcuts_dir.is_dir():
        print(f"error: {shortcuts_dir} not found", file=sys.stderr)
        return 1

    # load all non-test sources, grouped by package directory
    pkg_files: dict[str, dict[str, str]] = {}
    for f in sorted(shortcuts_dir.rglob("*.go")):
        if f.name.endswith("_test.go") or f.name.startswith("register"):
            continue
        pkg_files.setdefault(str(f.parent.relative_to(args.src)), {})[f.name] = \
            f.read_text(encoding="utf-8")

    services: dict[str, list] = {}
    n_skip = 0
    for pkg, sources in sorted(pkg_files.items()):
        helpers = collect_flag_helpers(sources)
        consts = collect_path_consts(sources)
        str_consts = collect_string_consts(sources)
        str_helpers = {}
        for src in sources.values():
            for m in RE_STRINGS_HELPER.finditer(src):
                str_helpers[m.group(1)] = parse_string_list(m.group(2))

        for fname, src in sources.items():
            for m in RE_SHORTCUT_VAR.finditer(src):
                open_brace = src.index("{", m.end() - 1)
                body = src[open_brace + 1: find_matching_brace(src, open_brace) - 1]
                sc = parse_shortcut(body, helpers, str_helpers, str_consts)
                if not sc.get("service") or not sc.get("command"):
                    continue
                resolved = resolve_api(body, sc, src, sources, consts)
                if not resolved:
                    n_skip += 1
                    continue
                method, raw_path = resolved
                path, fixed_query = normalize_path(raw_path)
                # skip bare prefixes like /open-apis/spark/v1
                if len([s for s in path.split("/") if s]) < 4:
                    n_skip += 1
                    continue
                op = build_operation(sc, method, path, fixed_query)
                key = (sc["service"], path, method.lower())
                services.setdefault(sc["service"], {})[key] = (
                    path, method.lower(), op)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    for service, ops in sorted(services.items()):
        doc = {
            "openapi": "3.0.3",
            "info": {
                "title": f"飞书开放平台 · {service} API（lark-cli Go 源码）",
                "description": (
                    f"从 lark-cli Go 源码 `shortcuts/{service}/` 提取的 HTTP 接口定义，"
                    "含官方 API Explorer 未收录的接口。\n\n---\n\n"
                    "本文档由 [lark-openapi-spec](https://github.com/dayongxie/lark-openapi-spec) "
                    "项目自动提取（启发式，非官方发布物），字段为近似推断，"
                    "权威说明以[飞书开放平台](https://open.feishu.cn/document)为准。"),
                "version": args.cli_version,
                "x-lark-service": service,
                "x-lark-track": "go (lark-cli source)",
                "x-generator": GENERATOR,
            },
            "servers": SERVERS,
            "tags": [{"name": service}],
            "paths": {},
        }
        for (_svc, path, m), (p, meth, op) in sorted(ops.items()):
            doc["paths"].setdefault(p, {})[meth] = op
            total += 1
        out = args.out_dir / f"{service}.yaml"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Generated by lark-openapi-spec — DO NOT EDIT BY HAND.\n"
                    "# Source: lark-cli Go source (shortcuts/), "
                    f"version {args.cli_version}\n")
            yaml.dump(doc, f, Dumper=_Dumper, allow_unicode=True,
                      sort_keys=False, width=120)
        print(f"  {service:15s} -> {out.name:18s} ({len(ops)} operations)")

    print(f"\n{len(services)} services, {total} operations, "
          f"{n_skip} shortcuts skipped (no resolvable API call).")

    # merge go-track stats into the manifest (preserving its header comments)
    manifest = {}
    header = ""
    if args.manifest.exists():
        with open(args.manifest, encoding="utf-8") as f:
            text = f.read()
        header = "".join(line for line in text.splitlines(keepends=True)
                         if line.startswith("#"))
        manifest = yaml.safe_load(text) or {}
    manifest["go_track"] = {
        "source": "lark-cli Go source (shortcuts/ dir, heuristic extraction)",
        "cli_version": args.cli_version,
        "stats": {"services": len(services), "operations": total},
        "directory": "openapi-go/",
    }
    with open(args.manifest, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.dump(manifest, f, Dumper=_Dumper, allow_unicode=True,
                  sort_keys=False, width=120)
    return 0


class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_representer)


if __name__ == "__main__":
    sys.exit(main())
