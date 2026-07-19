# lark-openapi-spec

[English](README.md) | 中文

飞书 / Lark 开放平台的 **OpenAPI 3.0 YAML 接口文档**，从官方命令行工具
[lark-cli](https://github.com/larksuite/cli) 内置的 API 注册表自动提取生成，
**每日自动更新**。

## 为什么做这个

飞书官方各语言 SDK 覆盖不全、更新滞后，遇到缺失的 API 只能手写 HTTP 调用。
而 lark-cli 内部维护着一份结构相当完整的 API 元数据（参数、请求体、响应体、
权限 scopes、风险等级、枚举值及中文描述、官方文档链接……）。本项目把这份元数据
转换成标准 OpenAPI 3.0 文档，让任何人都可以：

- 用 [openapi-generator](https://github.com/OpenAPITools/openapi-generator) 生成
  **任意语言** 的客户端 SDK，不再受制于官方 SDK 的覆盖范围；
- 导入 Swagger UI / Redoc / Apifox / Postman 获得可交互的接口文档；
- 在代码评审、契约测试、Mock 服务中作为机器可读的接口契约。

## 覆盖范围（务必阅读）

本仓库的数据与 lark-cli 的「API 命令层」一致，是其**精选集而非全量**：

| 产物 | 内容 | 规模 |
|---|---|---|
| `openapi/*.yaml` | typed API（含完整参数/请求体/响应体 schema） | 15 个服务、239 个接口 |
| `shortcuts/*.yaml` | lark-cli `+` 快捷命令参考（从 CLI help 提取） | 18 个域、412 条命令 |

注意：

- 飞书开放平台全量约 2500+ 接口，**未进入 lark-cli typed 元数据的接口不在本仓库中**
  （例如「发送消息」`POST /open-apis/im/v1/messages` 只以 `+messages-send` 快捷
  命令形式存在，见其参考文档）。
- 快捷命令可能一次调用多个接口，其 YAML 仅描述命令行契约，不是 HTTP 接口定义。

## 仓库结构

```
├── openapi/            # 主产物：每个服务一个自包含 OpenAPI 3.0 文档
├── shortcuts/          # 补充产物：lark-cli 快捷命令参考（每域一个 YAML）
├── raw/registry.json   # 上游注册表原始快照（diff 与审计用）
├── manifest.yaml       # 版本、统计、服务索引
├── CHANGELOG.md        # 每次注册表更新的接口级 diff
└── tools/              # 提取 / 转换 / 更新脚本（Python，零第三方依赖除 PyYAML）
```

## 快速使用

生成一个 Python 客户端：

```bash
openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/dayongxie/lark-openapi-spec/main/openapi/im.yaml \
  -g python -o ./lark-im-client
```

或直接把 `openapi/im.yaml` 拖进 [Swagger Editor](https://editor.swagger.io/) /
Apifox 查看交互式文档。

## `x-lark-*` 扩展字段

OpenAPI 无法表达的信息以扩展字段保留：

| 字段 | 含义 |
|---|---|
| `x-lark-scopes` | 接口可用的权限 scopes 列表 |
| `x-lark-required-scopes` | 必需权限 scopes |
| `x-lark-access-tokens` | 支持的调用身份（`user` / `tenant`） |
| `x-lark-risk` | 风险等级（`read` / `write` / `high-risk-write`） |
| `x-lark-danger` | 高危操作标记 |
| `x-lark-method-id` | 注册表中的原始方法 ID |
| `x-enum-descriptions` | 枚举值 → 中文说明 |

## 自动更新机制

上游注册表接口支持按 `data_version` 增量检查（版本未变时返回空）。
GitHub Actions 每天检查一次：

1. 注册表版本变化 → 重新生成 `openapi/`、`manifest.yaml`，向 `CHANGELOG.md`
   前置接口级 diff，提交并打 `registry-v*` tag + Release；
2. lark-cli 发布新版本 → 重新提取 `shortcuts/` 参考并提交。

此外，推送 `tools/` 或 workflow 本身的改动也会触发重新生成。

## 本地重新生成

```bash
pip install -r tools/requirements.txt
make update                        # 拉取注册表 + 生成 OpenAPI
make shortcuts CLI=/path/to/lark-cli   # 提取快捷命令参考（需要 lark-cli 二进制）
```

## 免责声明

本项目为社区维护的**非官方**项目。数据来源于 lark-cli 项目（MIT 协议）及飞书
开放平台公开端点，权威文档以 [飞书开放平台](https://open.feishu.cn/document) /
[Lark Open Platform](https://open.larksuite.com/document) 为准。「飞书」「Lark」
商标归其各自所有者所有，本项目与其无任何隶属或背书关系。

## License

MIT（代码与生成的 YAML 文档同）。详见 [LICENSE](LICENSE)。
