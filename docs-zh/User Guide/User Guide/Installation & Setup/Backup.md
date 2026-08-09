# 备份

Trilium 支持简单的备份方案，它会在以下事件发生时保存一份 <a class="reference-link" href="../Advanced%20Usage/Database.md">数据库</a> 的副本：

*   每天一次
*   每周一次
*   每月一次
*   在数据库迁移到新版本之前

因此，您总共最多会有 4 个来自不同时间点的备份，这应该能保护您免受各种问题的影响。这些备份默认存储在 [数据目录](Data%20directory.md) 中的 `backup` 目录下。

这只是一个非常基础的备份解决方案，我们建议您添加一些更好的备份方案——例如，将 <a class="reference-link" href="../Advanced%20Usage/Database.md">数据库</a> 备份到云端或其他计算机等。

请注意，<a class="reference-link" href="Synchronization.md">同步</a> 本身通过将数据分发到其他计算机的特性，也提供了一些备份能力。

## 下载备份

您可以通过进入 设置 > 备份 > 现有备份 > 下载 来下载现有备份。

## 恢复备份

假设您想要恢复每周备份，操作步骤如下：

*   找到 Trilium 使用的 [数据目录](Data%20directory.md) —— 简单的方法是点击左上角“菜单”中的“关于 Trilium Notes”，然后查看“数据目录”
    *   从现在起，我将把 `~/trilium-data` 称为数据目录
*   找到 `~/trilium-data/backup/backup-weekly.db` —— 这是 <a class="reference-link" href="../Advanced%20Usage/Database.md">数据库</a> 的备份
*   此时停止/结束 Trilium 进程
*   删除 `~/trilium-data/document.db`、`~/trilium-data/document.db-wal` 和 `~/trilium-data/document.db-shm`（后两个文件是自动生成的）
*   将此 `~/trilium-data/backup/backup-weekly.db` 复制并重命名为 `~/trilium-data/document.db`
*   确保该文件可写，例如使用 `chmod 600 document.db` 命令
*   重新启动 Trilium

如果您已配置同步，则需要对同步集群中的所有成员执行此操作，否则会检测到旧版本（恢复的备份）的文档并将其同步到新版本。

## 禁用备份

虽然不建议这样做，但可以在 [数据目录](Data%20directory.md) 的 `config.ini` 中禁用备份：

```
[General]
... 其他配置
# 设置为 true 以禁用备份（例如，因为服务器空间有限）
noBackup=true
```

您也可以查看 [配置](../Advanced%20Usage/Configuration%20\(config.ini%20or%20environment%20variables\).md) 文件，以了解如何将所有 `config.ini` 值作为环境变量提供。

参见 [示例配置](https://github.com/TriliumNext/Trilium/blob/master/config-sample.ini)。