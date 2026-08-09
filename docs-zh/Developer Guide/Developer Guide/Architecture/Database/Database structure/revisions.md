# 修订版本

| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `revisionId` | 文本 | 非空 |  | 修订版本的唯一 ID（例如 `0GjgUqnEudI8`）。 |
| `noteId` | 文本 | 非空 |  | 此修订版本所属[笔记](notes.md)的 ID。 |
| `type` | 文本 | 非空 | `""` | 笔记的类型（即 `text`、`file`、`code`、`relationMap`、`mermaid`、`canvas`）。 |
| `mime` | 文本 | 非空 | `""` | 笔记的 MIME 类型（例如 `text/html`）。 |
| `title` | 文本 | 非空 |  | 用户定义的笔记标题。 |
| `isProtected` | 整数 | 非空 | 0 | 如果实体是[受保护的](../../../Concepts/Protected%20entities.md)，则为 `1`，否则为 `0`。 |
| `blobId` | 文本 | 可空 | `null` | 来自 <a class="reference-link" href="blobs.md">blobs</a> 的对应 ID。虽然理论上可以是 `NULL`，但尚未发现任何此类笔记。 |
| `utcDateLastEdited` | 文本 | 非空 |  | **不确定它与修改日期有何不同。** |
| `utcDateCreated` | 文本 | 非空 |  | UTC 格式的创建日期（例如 `2023-11-08 16:43:44.204Z`） |
| `utcDateModified` | 文本 | 非空 |  | UTC 格式的修改日期（例如 `2023-11-08 16:43:44.204Z`） |
| `dateLastEdited` | 文本 | 非空 |  | **不确定它与修改日期有何不同。** |
| `dateCreated` | 文本 | 非空 |  | 本地化的创建日期（例如 `2023-08-12 15:10:04.045+0300`） |