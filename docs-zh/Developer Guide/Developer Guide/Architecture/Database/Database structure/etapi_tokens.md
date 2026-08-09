# etapi_tokens
| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `etapiTokenId` | 文本 | 非空 |  | 令牌的唯一 ID（例如 `aHmLr5BywvfJ`）。 |
| `name` | 文本 | 非空 |  | 令牌的名称，由用户设置。 |
| `tokenHash` | 文本 | 非空 |  | 令牌本身。 |
| `utcDateCreated` | 文本 | 非空 |  | 创建日期，UTC 格式（例如 `2023-11-08 16:43:44.204Z`） |
| `utcDateModified` | 文本 | 非空 |  | 修改日期，UTC 格式（例如 `2023-11-08 16:43:44.204Z`） |
| `isDeleted` | 整数 | 非空 | 0 | 如果实体已[归档](../../../Concepts/Deleted%20notes.md)，则为 `1`，否则为 `0`。 |