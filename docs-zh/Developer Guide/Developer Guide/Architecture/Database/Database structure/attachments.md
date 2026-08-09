# 附件

| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `attachmentId` | 文本 | 非空 |  | 唯一 ID（例如 `qhC1vzU4nwSE`） |
| `ownerId` | 文本 | 非空 |  | <a class="reference-link" href="notes.md">笔记</a> 中某行的唯一 ID。 |
| `role` | 文本 | 非空 |  | 附件的作用：`image` 表示附加到笔记的图片，`file` 表示上传的文件。 |
| `mime` | 文本 | 非空 |  | 附件的 MIME 类型（例如 `image/png`） |
| `title` | 文本 | 非空 |  | 附件的标题。 |
| `isProtected` | 整数 | 非空 | 0 | 如果实体是[受保护的](../../../Concepts/Protected%20entities.md)，则为 `1`，否则为 `0`。 |
| `position` | 整数 | 非空 | 0 | 不确定位置在附件中的相关性（曾看到值为 10 和 0）。 |
| `blobId` | 文本 | 可空 | `null` | <a class="reference-link" href="blobs.md">blobs</a> 表中对应的 `blobId`。 |
| `dateModified` | 文本 | 非空 |  | 本地化的修改日期（例如 `2023-11-08 18:43:44.204+0200`） |
| `utcDateModified` | 文本 | 非空 |  | UTC 格式的修改日期（例如 `2023-11-08 16:43:44.204Z`） |
| `utcDateScheduledForErasure` | 文本 | 可空 | `null` |  |
| `isDeleted` | 整数 | 非空 |  | 如果实体是[已删除的](../../../Concepts/Deleted%20notes.md)，则为 `1`，否则为 `0`。 |
| `deleteId` | 文本 | 可空 | `null` |  |