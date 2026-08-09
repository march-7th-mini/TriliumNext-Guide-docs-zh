# 笔记
| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `noteId` | 文本 | 非空 |  | 笔记的唯一 ID（例如 `2LJrKqIhr0Pe`）。 |
| `title` | 文本 | 非空 | `"note"` | 笔记的标题，由用户定义。 |
| `isProtected` | 整数 | 非空 | 0 | 如果实体是[受保护的](../../../Concepts/Protected%20entities.md)，则为 `1`，否则为 `0`。 |
| `type` | 文本 | 非空 | `"text"` | 笔记的类型（即 `text`、`file`、`code`、`relationMap`、`mermaid`、`canvas`）。 |
| `mime` | 文本 | 非空 | `"text/html"` | 笔记的 MIME 类型（例如 `text/html`）。请注意，在某些情况下它可以是空字符串，但不能为 null。 |
| `blobId` | 文本 | 可空 | `null` | 来自 <a class="reference-link" href="blobs.md">blobs</a> 的对应 ID。虽然理论上可以是 `NULL`，但尚未发现任何此类笔记。 |
| `isDeleted` | 整数 | 可空 | 0 | 如果实体是[已删除的](../../../Concepts/Deleted%20notes.md)，则为 `1`，否则为 `0`。 |
| `deleteId` | 文本 | 非空 | `null` |  |
| `dateCreated` | 文本 | 非空 |  | 本地化的创建日期（例如 `2023-11-08 18:43:44.204+0200`） |
| `dateModified` | 文本 | 非空 |  | 本地化的修改日期（例如 `2023-11-08 18:43:44.204+0200`） |
| `utcDateCreated` | 文本 | 非空 |  | UTC 格式的创建日期（例如 `2023-11-08 16:43:44.204Z`） |
| `utcDateModified` | 文本 | 非空 |  | UTC 格式的修改日期（例如 `2023-11-08 16:43:44.204Z`） |