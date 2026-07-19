# lark-openapi-spec

[English](README.md) | 中文

飞书 / Lark 开放平台的 **OpenAPI 3.0 YAML 接口文档**，由两条数据轨道自动生成、
**每日自动更新**：

- **全量轨道（`openapi-full/`）**：来自飞书官方 API Explorer 数据源，
  覆盖 **55 个项目、1627 个接口**；
- **精选轨道（`openapi/`）**：来自官方命令行工具
  [lark-cli](https://github.com/larksuite/cli) 内置的 API 注册表，
  覆盖 15 个服务、239 个精选接口（含风险分级等独有信息）。

## 为什么做这个

飞书官方各语言 SDK 覆盖不全、更新滞后，遇到缺失的 API 只能手写 HTTP 调用。
本项目把开放平台内部维护的结构化 API 元数据转换成标准 OpenAPI 3.0 文档，
让任何人都可以：

- 用 [openapi-generator](https://github.com/OpenAPITools/openapi-generator) 生成
  **任意语言** 的客户端 SDK，不再受制于官方 SDK 的覆盖范围；
- 导入 Swagger UI / Redoc / Apifox / Postman 获得可交互的接口文档；
- 在代码评审、契约测试、Mock 服务中作为机器可读的接口契约。

## 覆盖范围

| 产物 | 数据源 | 内容 | 规模 |
|---|---|---|---|
| `openapi-full/*.yaml` | 官方 API Explorer（`/api_explorer/v1`） | 全量服务端 API：参数/请求体/响应体（含错误码表、限流档位、分页标记） | 55 个项目、1627 个接口 |
| `openapi/*.yaml` | lark-cli API 注册表（`/api/tools/open/api_definition`） | 精选 typed API（含风险分级、高危标记、操作提示） | 15 个服务、239 个接口 |
| `shortcuts/*.yaml` | lark-cli `+` 快捷命令（从 CLI help 提取） | 命令行契约参考（非 HTTP 接口定义） | 18 个域、412 条命令 |

重复出现的公共结构（如 docx 的 Block）已自动提取到各文件的 `components/schemas` 并以 `$ref` 引用，文档体积因此减少约 76%。

两个轨道互为补充：全量轨道解决「有没有」，精选轨道的风险分级（read /
write / high-risk-write）和操作提示是其独有信息。同一接口在两个轨道中的
描述可能略有差异，以全量轨道（官方数据源）为准。

## 仓库结构

```
├── openapi-full/       # 全量轨道：每个项目一个 OpenAPI 3.0 文档（55 个）
├── openapi/            # 精选轨道：每个服务一个 OpenAPI 3.0 文档（15 个）
├── shortcuts/          # lark-cli 快捷命令参考（每域一个 YAML）
├── raw/
│   ├── registry.json       # lark-cli 注册表快照
│   └── explorer/           # Explorer 目录树 + 接口索引（含内容 hash）
├── manifest.yaml       # 版本、统计、服务索引
├── CHANGELOG.md        # 每次更新的接口级 diff
└── tools/              # 提取 / 转换 / 更新脚本（Python，仅依赖 PyYAML）
```

## 快速使用

生成一个 Python 客户端：

```bash
openapi-generator-cli generate \
  -i https://raw.githubusercontent.com/dayongxie/lark-openapi-spec/main/openapi-full/im.yaml \
  -g python -o ./lark-im-client
```

或直接把 `openapi-full/im.yaml` 拖进 [Swagger Editor](https://editor.swagger.io/) /
Apifox 查看交互式文档。

## `x-lark-*` 扩展字段

OpenAPI 无法表达的信息以扩展字段保留：

| 字段 | 含义 | 轨道 |
|---|---|---|
| `x-lark-scopes` | 权限 scopes 列表 | 两者 |
| `x-lark-access-tokens` | 支持的调用身份（`user` / `tenant`） | 两者 |
| `x-lark-error-mappings` | 业务错误码表 | 全量 |
| `x-lark-rate-limit` | 限流档位 | 全量 |
| `x-lark-pagination` | 分页接口标记 | 全量 |
| `x-lark-id-types` | ID 类型映射（如 chat_id → chat） | 全量 |
| `x-lark-risk` | 风险等级（`read` / `write` / `high-risk-write`） | 精选 |
| `x-lark-danger` | 高危操作标记 | 精选 |
| `x-lark-tips` | 操作提示 | 精选 |
| `x-enum-descriptions` | 枚举值 → 中文说明 | 两者 |

## 自动更新机制

GitHub Actions 每日运行：

1. **精选轨道**：注册表接口支持 `data_version` 增量检查（无变化返回空），
   有更新才重新生成；
2. **全量轨道**：上游无版本号，每日全量抓取目录 + 1627 个定义，
   以内容 hash 比对，有变化才提交（新增/移除/变更写入 CHANGELOG）；
3. **快捷命令**：lark-cli 发布新版本时重新提取。

推送 `tools/` 或 workflow 本身的改动也会触发重新生成。

## 本地重新生成

```bash
pip install -r tools/requirements.txt
make update                        # lark-cli 注册表轨道
make explorer                      # 官方 Explorer 全量轨道（约 10 分钟）
make shortcuts CLI=/path/to/lark-cli   # 快捷命令参考（需要 lark-cli 二进制）
```

## 免责声明

本项目为社区维护的**非官方**项目。数据来源于 lark-cli 项目（MIT 协议）及飞书
开放平台公开端点，权威文档以 [飞书开放平台](https://open.feishu.cn/document) /
[Lark Open Platform](https://open.larksuite.com/document) 为准。「飞书」「Lark」
商标归其各自所有者所有，本项目与其无任何隶属或背书关系。

## License

MIT（代码与生成的 YAML 文档同）。详见 [LICENSE](LICENSE)。
