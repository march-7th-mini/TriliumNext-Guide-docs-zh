# 实体变更墓碑

当一个实体被删除时，其在 `entity_changes` 表中的行**不会**被删除——而是被标记。`erase#setEntityChangesAsErased` 设置 `isErased = true`，刷新 `utcDateChanged`，并通过 `putEntityChangeWithForcedChange` 重新推送该行。墓碑的作用是告知每个对等节点“此实体已不存在”；如果没有它，仍然持有该实体的对等节点会简单地将其推送回来。

## 墓碑永远不会被清理

系统对墓碑没有任何垃圾回收机制。没有集群范围的已确认 ID 水位线，没有 TTL，也没有压缩过程。因此，`entity_changes` 表会随着**整个生命周期的删除活动**单调增长，而不是随着用户当前拥有的数据量增长。

有两个因素放大了这一点：

*   **删除是级联的。** 删除一个笔记也会为其分支、属性和修订版本创建墓碑（`erase#eraseNotes`），因此计数跟踪的是编辑和删除的量，而不是笔记数量。
*   **完全初始同步会重放整个历史记录。** 新客户端会拉取每一行，包括墓碑。没有任何快照或引导路径可以让它从当前状态开始。

2026 年观察到的一个真实数据库持有约 165 000 条实体变更，而活跃实体仅约 12 000 个（1 954 个笔记，7 200 个属性，644 个附件）——大约 **85% 是墓碑**。

## 为什么不能简单地删除它们

`content_hash#getEntityHashes` 将该标志合并到每个扇区的哈希中：

```
entityHashMap[sector] = (entityHashMap[sector] || "") + hash + isErased;
```

因此，被删除的行是对等节点进行比较的哈希的一部分。在一个实例上删除墓碑会使其扇区哈希与任何仍持有这些墓碑的对等节点产生分歧，`checkContentHashes` 随后几乎会在每个扇区上失败，而 `addEntityChangesForSector` 会重新推送这些扇区的**所有**行——包括已删除的行，因为 `putEntityChange` 会保留 `isErased`。墓碑会再次出现。

手动执行 `DELETE FROM entity_changes WHERE isErased = 1` 只有在所有实例同时执行，或者服务器是唯一幸存的来源且所有客户端都被清空或是全新的（新设备没有可推送回来的墓碑）时才会生效。请先备份，并且只在所有客户端都同步完成的情况下执行。它是 ID 安全的：`entity_changes` 使用 `AUTOINCREMENT` 高水位标记，因此 ID 永远不会被重用。

## 内置选项无济于事

*   **`fillEntityChanges`** 执行 `DELETE FROM entity_changes WHERE isErased = 0` 并重建活跃行。墓碑不受影响，并且重建的行会获得新的 ID，这会导致对等节点重新拉取它们。
*   **`forceFullSync`** 将 `lastSyncedPull`/`lastSyncedPush` 重置为 0 并重新拉取所有内容，包括墓碑。这会使问题变得更糟。

## Blob 是唯一的例外

对于 Blob，系统已经遇到了同样的问题，并在 `erase#eraseUnusedBlobs` 中进行了特殊处理，该函数直接清除其变更行，而不是为其创建墓碑：

```
// blobs are not marked as erased in entity_changes, they are just purged completely
// this is because technically every keystroke can create a new blob and there would be just too many
sql.executeMany(`DELETE FROM entity_changes WHERE entityName = 'blobs' AND entityId IN (???)`, unusedBlobIds);
```

这个例外从未被推广，因此所有其他实体类型仍然在持续累积。

## 真正的问题所在

这种代价在原生客户端上是不可见的——better-sqlite3 处理几十万行毫无压力。只有在 WASM 目标（浏览器中的独立版本，以及基于其构建的 Capacitor 移动应用）上才是致命的，因为在这些环境中 SQLite 是同步运行的，长时间的事务会阻塞线程。这是新目标暴露出来的潜在债务，而不是它们创造的。

任何真正的修复都必须解决上述哈希耦合问题。可能的方向包括：引入每个实例的已确认 ID 水位线以允许协调收集，提供快照/引导路径以便新客户端不必重放历史记录，或者将 Blob 清理机制推广到其他高变更率的实体类型。