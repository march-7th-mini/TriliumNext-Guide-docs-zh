# entity_changes
| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `id` | 整数 | 非空 |  | 实体变更的顺序数字索引。 |
| `entityName` | 文本 | 非空 |  | 被变更实体的类型（`attributes`、`branches`、`note_reordering` 等） |
| `entityId` | 文本 | 非空 |  | 被变更实体的 ID。 |
| `hash` | 文本 | 可空 (\*) |  | 待办：描述哈希是如何计算的 |
| `isErased` | 整数（1 或 0） | 可空 (\*) |  | 待办：这是做什么的？ |
| `changeId` | 文本 | 可空 (\*) |  | 待办：这是做什么的？ |
| `componentId` | 文本 | 可空 (\*) |  | 导致此变更的 UI 组件的 ID。  <br>  <br>示例：`date-note`、`F-PoZMI0vc`、`NA`（捕获所有） |
| `instanceId` | 文本 | 可空 (\*) |  | 创建此变更的[实例](#root/pOsGYCXsbNQG/tC7s2alapj8V/Gzjqa934BdH4/c5xB8m4g2IY6)的 ID。 |
| `isSynced` | 整数（1 或 0） | 非空 |  | 待办：这是做什么的？ |
| `utcDateChanged` | 文本 | 非空 |  | 实体变更的 UTC 格式日期（例如 `2023-11-08 16:43:44.204Z`） |

可空 (\*) 表示所有新值均为非空，旧行可能包含空值。