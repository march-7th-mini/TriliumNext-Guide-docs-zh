# 笔记出现在“最近更改”中，但在树中缺失

## 症状

一个确实已创建的笔记没有出现在树中。“最近更改”列出了它，但显示为**已删除**，悬停或尝试恢复它会失败，并显示：

```
NotFoundError: Deleted note 'X' was not found.
```

该行数据在数据库中是存在的。重启应用程序后，笔记会正常显示。

这看起来像是 Becca 或 Froca 的损坏问题。但通常并非如此。

## 原因：两个进程共用一个数据目录

实体变更传播**仅在进程内进行**。进程 A 创建的笔记会进入 A 的 Becca 和共享的 SQLite 文件——但进程 B 的 Becca 永远不会得知此事，因为通知永远不会离开进程 A。

两个视图因此产生分歧，并恰好导致上述症状：

*   **“最近更改”直接读取数据库。** `routes/api/recent_changes.ts` 通过原始 SQL 查询 `notes` 表，因此它能看到新行。
*   **树和 `tree/load` 读取 Becca**，在进程 B 中，Becca 没有这个笔记。客户端会将任何无法通过 Froca 解析的条目渲染为已删除笔记的链接。
*   **悬停该链接会调用 `/api/deleted-notes/:noteId/metadata`**，该接口执行 `... WHERE noteId = ? AND isDeleted = 1` 查询，当找不到结果时抛出 `NotFoundError`——而找不到结果恰恰是因为该笔记是_存活的_。

重启第二个实例会从磁盘重新加载 Becca，这就是笔记随后出现的原因。

## 如何确认

检查是否有多个 Trilium 进程绑定到同一数据目录。在 Windows 上：

```powershell
Get-NetTCPConnection -LocalPort 37840,37841 -State Listen | Select-Object LocalPort, OwningProcess
```

然后将拥有的 PID 与正在运行的可执行文件进行匹配。安装版和本地构建的桌面应用都默认使用 `%APPDATA%\trilium-data`，因此两者共享 `document.db` 而没有任何一方发出警告。它们也共享每日日志文件，且日志行不携带 PID——因此一个进程的输出与另一个进程的无法区分，在阅读日志寻找线索之前需要了解这一点。

这同样适用于任何指向正在运行实例的自动化工具：REST 或 MCP 客户端与占用该端口的进程通信，其写入操作会进入该进程的 Becca——而不是正在被监视的窗口中。

## 如何避免

每当同时运行两个实例时，为每个实例指定独立的数据目录（`TRILIUM_DATA_DIR`）。开发服务器默认已如此（`apps/server/data`）；而安装版应用和本地构建的桌面应用则不会。