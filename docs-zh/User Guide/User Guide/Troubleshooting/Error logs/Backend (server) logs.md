# 后端（服务器）日志
## 通过后端日志访问

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中，转到 _高级_ → _显示后端日志_。这将显示当前的后端日志（即今天的），历史信息仅保存在磁盘上（见下文）。

自 v0.104.0 起的交互方式：

*   可以使用<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>区域中的专用按钮将文件下载为文本文件（仅限<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>）。
*   该文件也可以像普通的<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记一样进行搜索。

## 磁盘上的位置

后端日志存储在文件系统中。要找到它们，请打开<a class="reference-link" href="../../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>，进入 `log` 子目录并找到最新的日志文件，例如 `trilium-2022-12-14.log`。

## 报告后端错误

您可以将整个文件附加到错误报告中（推荐），或者打开文件并仅复制粘贴最后几行/您认为相关的行。

## 自定义日志保留策略

后端日志完全由 Trilium 服务器管理。默认情况下，会保留最近 90 天的日志；超过该期限的日志将被删除以减少空间占用。

可以通过 `.ini` 文件修改<a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>来更改保留期限：

```
[Logging]
retentionDays=7
```

或者通过环境变量 `TRILIUM_LOGGING_RETENTION_DAYS` 进行设置。

特殊情况：

*   正值表示要保留的日志天数
*   值为 0 时使用默认值（90 天）
*   负值（例如 `-1`）表示保留所有日志，无论其多么古老和数量多少（且

> [!NOTE]
> 如果您将保留天数设置为较小的值，您可能会注意到并非所有日志文件都会被删除。这是因为始终会维持最少数量的日志（撰写本文时为 7 个）。