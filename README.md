# lark-openapi-spec

English | [中文](README.zh.md)

**OpenAPI 3.0 YAML specifications for the Feishu / Lark Open Platform**,
automatically extracted from the API registry embedded in the official
[lark-cli](https://github.com/larksuite/cli) tool — **updated daily by CI**.

## Why

The official Lark SDKs lag behind the platform and miss endpoints; falling back
to hand-written HTTP calls is tedious. lark-cli ships a rich internal API
registry (parameters, request/response bodies, permission scopes, risk levels,
enums with descriptions, official doc links...). This project converts that
registry into standard OpenAPI 3.0 documents so you can:

- generate a client SDK in **any language** with
  [openapi-generator](https://github.com/OpenAPITools/openapi-generator) —
  no longer limited by official SDK coverage;
- import into Swagger UI / Redoc / Apifox / Postman for interactive docs;
- use the specs as machine-readable contracts for reviews, contract tests
  and mock servers.

## Coverage (read me)

This repository mirrors lark-cli's "API command" layer — a **curated set, not
the full platform surface**:

| Artifact | Content | Size |
|---|---|---|
| `openapi/*.yaml` | Typed APIs (full parameter/body/response schemas) | 15 services, 239 operations |
| `shortcuts/*.yaml` | lark-cli `+` shortcut command reference (from CLI help) | 18 domains, 412 commands |

Caveats:

- The platform exposes ~2500+ endpoints in total; endpoints **not** present in
  lark-cli's typed registry are not covered here. (E.g. "send message"
  `POST /open-apis/im/v1/messages` exists only as the `+messages-send`
  shortcut — see the shortcut reference.)
- A shortcut may wrap several API calls; its YAML describes the CLI contract,
  not an HTTP interface.

## Layout

```
├── openapi/            # main artifact: one self-contained OpenAPI 3.0 doc per service
├── shortcuts/          # bonus artifact: lark-cli shortcut reference (one YAML per domain)
├── raw/registry.json   # verbatim upstream registry snapshot (for diffing/auditing)
├── manifest.yaml       # version, stats, service index
├── CHANGELOG.md        # method-level diff for every registry update
└── tools/              # fetch / convert / diff scripts (Python, PyYAML only)
```

## Quick start

Generate a Python client:

```bash
openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/dayongxie/lark-openapi-spec/main/openapi/im.yaml \
  -g python -o ./lark-im-client
```

Or drop `openapi/im.yaml` into [Swagger Editor](https://editor.swagger.io/) for
interactive documentation.

## `x-lark-*` extension fields

Everything OpenAPI cannot express is preserved as extensions:

| Field | Meaning |
|---|---|
| `x-lark-scopes` | Permission scopes accepted by the endpoint |
| `x-lark-required-scopes` | Mandatory scopes |
| `x-lark-access-tokens` | Supported identities (`user` / `tenant`) |
| `x-lark-risk` | Risk level (`read` / `write` / `high-risk-write`) |
| `x-lark-danger` | Dangerous-operation flag |
| `x-lark-method-id` | Original method ID in the registry |
| `x-enum-descriptions` | Enum value → human description |

## How it stays fresh

The upstream registry endpoint supports incremental checks via `data_version`
(it returns an empty payload when the version is unchanged). A GitHub Actions
workflow runs daily:

1. Registry version bump → regenerate `openapi/` + `manifest.yaml`, prepend a
   method-level diff to `CHANGELOG.md`, commit, tag `registry-v*` and cut a
   Release.
2. New lark-cli release → re-extract the `shortcuts/` reference and commit.

Pushing changes to `tools/` or the workflow itself also triggers a rebuild.

## Regenerate locally

```bash
pip install -r tools/requirements.txt
make update                              # fetch registry + build OpenAPI specs
make shortcuts CLI=/path/to/lark-cli     # extract shortcut reference (needs lark-cli)
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
