# 后端（服务器）日志
## 通过后端日志访问

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中，前往_高级_ → _后端日志_。这将显示当前的后端日志（即今天的日志），历史信息仅保存在磁盘上（见下文）。

日志经过着色以便于阅读：按类别着色的请求状态码、慢 SQL 查询以及红色显示的错误。慢 SQL 查询的语句会像在<a class="reference-link" href="../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a>中一样高亮显示，使用代码笔记的配色方案（参见<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>中的_配色方案_）。

应用在后台运行的搜索（例如用于筛选集合）或脚本运行的搜索，其后会跟随一行 `Search:`，包含其查询语句及其返回的笔记数量。该查询会像在<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>中一样高亮显示。快速搜索和保存的搜索不会添加此行。

自 v0.104.0 起的交互：

*   可以使用<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a>区域中的 <span class="tn-icon bx bx-download"></span> 按钮将该文件下载为文本文件。
*   该文件也可以像普通<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记一样被搜索。

## 磁盘上的位置

后端日志存储在文件系统中。要找到它们，请打开<a class="reference-link" href="../../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>，进入 `log` 子目录并找到最新的日志文件，例如 `trilium-2022-12-14.log`。

## 在终端中

服务器还会将每条日志条目打印到其标准输出，即 `docker logs` 或 `journalctl` 所显示的内容。当该输出为终端时，每条条目以其时间开头，并像应用中的后端日志一样着色：按类别着色的请求状态码、慢 SQL 查询以及红色显示的错误。慢 SQL 查询的语句和搜索的查询在此处不显示语法高亮。带有 Trilium 徽标和版本信息的启动横幅也会着色。输出到文件、管道或容器日志时保持纯文本且不带时间，因为这些工具会添加自己的时间。

要在终端中关闭颜色，请设置 `NO_COLOR` 环境变量；要在其他地方强制开启颜色，请设置 `FORCE_COLOR=1`。

## 报告后端缺陷

你可以将整个文件附加到缺陷报告中（推荐），或者打开它并仅复制粘贴最后几行/你认为相关的行。

## 自定义日志保留

后端日志完全由 Trilium 服务器管理。默认情况下，保留最近 90 天的日志；更早的日志会被删除以减少空间占用。

可以通过 `.ini` 文件修改<a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>来更改保留期限：

```
[Logging]
retentionDays=7
```

或通过环境变量 `TRILIUM_LOGGING_RETENTION_DAYS`。

特殊情况：

*   正值表示要保留的日志天数
*   值为 0 时使用默认值（90 天）
*   负值（例如 `-1`）表示保留所有日志，无论其多么古老和数量众多（以及

> [!NOTE]
> 如果将保留天数设置为较小的数字，你可能会注意到并非所有日志文件都被删除。这是因为始终会维持一个最低数量的日志（撰写本文时为 7 个）。