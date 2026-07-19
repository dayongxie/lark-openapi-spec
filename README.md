# lark-openapi-spec

English | [中文](README.zh.md)

**OpenAPI 3.0 YAML specifications for the Feishu / Lark Open Platform**,
generated from two data tracks and **updated daily by CI**:

- **Full track (`openapi-full/`)** — from the official API Explorer data
  endpoints: **55 projects, 1627 operations**;
- **Curated track (`openapi/`)** — from the API registry embedded in the
  official [lark-cli](https://github.com/larksuite/cli) tool: 15 services,
  239 curated operations (with exclusive risk-level metadata).

## Why

The official Lark SDKs lag behind the platform and miss endpoints; falling back
to hand-written HTTP calls is tedious. This project converts the platform's own
structured API metadata into standard OpenAPI 3.0 documents so you can:

- generate a client SDK in **any language** with
  [openapi-generator](https://github.com/OpenAPITools/openapi-generator) —
  no longer limited by official SDK coverage;
- import into Swagger UI / Redoc / Apifox / Postman for interactive docs;
- use the specs as machine-readable contracts for reviews, contract tests
  and mock servers.

## Coverage

| Artifact | Source | Content | Size |
|---|---|---|---|
| `openapi-full/*.yaml` | Official API Explorer (`/api_explorer/v1`) | Every documented server API: params / bodies / responses, plus error-code tables, rate-limit tiers, pagination flags | 55 projects, 1627 operations |
| `openapi/*.yaml` | lark-cli API registry (`/api/tools/open/api_definition`) | Curated typed APIs with risk levels, danger flags, usage tips | 15 services, 239 operations |
| `shortcuts/*.yaml` | lark-cli `+` shortcut commands (from CLI help) | CLI contract reference (not HTTP interfaces) | 18 domains, 412 commands |

Repeated shared structures (e.g. docx Blocks) are automatically extracted into each file's `components/schemas` and referenced via `$ref`, shrinking the documents by ~76%.

The tracks complement each other: the full track answers "does it exist", while
the curated track's risk levels (`read` / `write` / `high-risk-write`) and tips
are unique to it. Where they disagree, prefer the full track (official source).

## Layout

```
├── openapi-full/       # full track: one OpenAPI 3.0 doc per project (55)
├── openapi/            # curated track: one OpenAPI 3.0 doc per service (15)
├── shortcuts/          # lark-cli shortcut reference (one YAML per domain)
├── raw/
│   ├── registry.json       # lark-cli registry snapshot
│   └── explorer/           # Explorer catalog tree + API index (content hashes)
├── manifest.yaml       # version, stats, service index
├── CHANGELOG.md        # method-level diff for every update
└── tools/              # fetch / convert / diff scripts (Python, PyYAML only)
```

## Quick start

Generate a Python client:

```bash
openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/dayongxie/lark-openapi-spec/main/openapi-full/im.yaml \
  -g python -o ./lark-im-client
```

Or drop `openapi-full/im.yaml` into [Swagger Editor](https://editor.swagger.io/)
for interactive documentation.

## `x-lark-*` extension fields

Everything OpenAPI cannot express is preserved as extensions:

| Field | Meaning | Track |
|---|---|---|
| `x-lark-scopes` | Permission scopes | both |
| `x-lark-access-tokens` | Supported identities (`user` / `tenant`) | both |
| `x-lark-error-mappings` | Business error-code table | full |
| `x-lark-rate-limit` | Rate-limit tier | full |
| `x-lark-pagination` | Paginated-endpoint flag | full |
| `x-lark-id-types` | ID type mapping (e.g. chat_id → chat) | full |
| `x-lark-risk` | Risk level (`read` / `write` / `high-risk-write`) | curated |
| `x-lark-danger` | Dangerous-operation flag | curated |
| `x-lark-tips` | Usage tips | curated |
| `x-enum-descriptions` | Enum value → human description | both |

## How it stays fresh

A GitHub Actions workflow runs daily:

1. **Curated track** — the registry endpoint supports incremental checks via
   `data_version` (empty reply = no change); specs rebuild only on bumps.
2. **Full track** — the upstream has no version field, so the whole catalog +
   all 1627 definitions are re-fetched daily and compared by content hash;
   commits happen only on real changes (added/removed/changed go to
   CHANGELOG.md). The fetcher sorts the upstream's randomly-ordered
   field-scope list before hashing, and the output is fully deterministic:
   `info.version` is a content hash (`1.0.0+<hash>`) with no build
   timestamps, so rebuilding an unchanged document is byte-identical.
3. **Shortcuts** — re-extracted whenever lark-cli publishes a new release.

Pushing changes to `tools/` or the workflow itself also triggers a rebuild.

## Regenerate locally

```bash
pip install -r tools/requirements.txt
make update                        # lark-cli registry track
make explorer                      # official Explorer full track (~10 min)
make shortcuts CLI=/path/to/lark-cli     # shortcut reference (needs lark-cli)
```

## Disclaimer

Unofficial, community-maintained project. Data originates from the lark-cli
project (MIT License) and public Feishu/Lark Open Platform endpoints. The
authoritative documentation is at [open.feishu.cn](https://open.feishu.cn/document)
and [open.larksuite.com](https://open.larksuite.com/document). "Feishu" and
"Lark" are trademarks of their respective owners; this project is not
affiliated with or endorsed by them.

## License

MIT (code and generated YAML alike). See [LICENSE](LICENSE).
