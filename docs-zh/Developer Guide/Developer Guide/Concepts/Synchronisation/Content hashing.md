# 内容哈希

实体哈希在 `content_hash#getEntityHashes` 中完成。

*   其工作原理是查看 `entity_changes` 表并遍历每个实体名称/类型：
    *   `blobs`
    *   `attributes`
    *   `revisions`
    *   `attachments`
    *   `notes`
    *   `branches`
    *   `etapi_tokens`
    *   `options`
*   出于某种原因，`note_reordering` 实体被特别忽略。
*   然后，`entity_changes` 中的所有行根据其 `entityId` 按字母顺序排序。
*   每个实体行随后按 `entityName` 分组，再按扇区分组。扇区定义为 `id` 的第一个字符。
*   哈希值会被修改以同时添加 `isErased` 值，因为已删除条目的哈希值不会更新。
*   对于每个扇区，使用 `utils.hash` 计算哈希值，使用 Base64 编码的 SHA1。