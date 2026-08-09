# branches
| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `branchId` | 文本 | 非空 |  | 分支的ID，格式为`a_b`，其中`a`是`parentNoteId`，`b`是`noteId`。 |
| `noteId` | 文本 | 非空 |  | [笔记](notes.md)的ID。 |
| `parentNoteId` | 文本 | 非空 |  | 笔记所属父级[笔记](notes.md)的ID。 |
| `notePosition` | 整数 | 非空 |  | 分支在同一层级中的位置，该值通常是10的倍数。 |
| `prefix` | 文本 | 可空 |  | [分支前缀](../../../Concepts/Branch%20prefixes.md)（如果有），否则为`NULL`。 |
| `isExpanded` | 整数 | 非空 | 0 | 分支是否应向用户显示为展开状态（显示其子项）。 |
| `isDeleted` | 整数 | 非空 | 0 | 如果实体已被[删除](../../../Concepts/Deleted%20notes.md)，则为`1`，否则为`0`。 |
| `deleteId` | 文本 | 可空 | `null` |  |
| `utcDateModified` | 文本 | 非空 |  | UTC格式的修改日期（例如`2023-11-08 16:43:44.204Z`） |