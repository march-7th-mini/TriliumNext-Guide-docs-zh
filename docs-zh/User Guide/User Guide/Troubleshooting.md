# 故障排除

尽管 Trilium 会积极维护且保持稳定，但遇到错误仍有可能发生。

## 常规快速修复

故障排除的第一步通常是重启。

如果您遇到界面问题，前端可能已进入不一致状态。按 <kbd>Ctrl</kbd> + <kbd>R</kbd> 重新加载应用程序。这将重新加载前端。

如果问题仍然存在或似乎是后端问题，请重启整个应用程序。对于桌面（Electron）版本，只需关闭并重新打开窗口。如果您使用的是 Docker 版本，请重启容器。

## 损坏的笔记导致 Trilium 崩溃

某些问题，例如渲染带有错误脚本的笔记，可能会导致 Trilium 崩溃。如果 Trilium 在重启时尝试重新加载有问题的笔记，它将持续崩溃。

要解决此问题，请使用 `TRILIUM_START_NOTE_ID` 环境变量将打开的标签页重置为单个指定的笔记 ID（例如 `root`）。在 Linux 中，您可以按如下方式设置：

```
TRILIUM_START_NOTE_ID=root ./trilium
```

## 损坏的脚本阻止应用程序启动

如果自定义脚本导致 Trilium 崩溃，并且该脚本被设置为启动脚本或位于活动的[自定义小组件](Scripting/Frontend%20Basics/Custom%20Widgets.md)中，请以“安全模式”启动 Trilium 以防止任何自定义脚本执行：

```
TRILIUM_SAFE_MODE=true ./trilium
```

根据您的 Trilium 发行版，您可能有预制的脚本可用：`trilium-safe-mode.bat` 和 `trilium-safe-mode.sh`。

Trilium 启动后，找到并修复或删除有问题的笔记。

## 同步与一致性检查

Trilium 会定期验证数据库的逻辑一致性（例如，确保每个笔记都有父笔记）。如果检测到不一致，您将通过界面收到通知。

在这种情况下，请提交错误报告，并在必要时附上[匿名化数据库](Troubleshooting/Anonymized%20Database.md)。

## 恢复备份

Trilium 会定期进行自动备份。如果问题变得严重，您可以[从备份中恢复](Installation%20%26%20Setup/Backup.md)。

## 忘记密码

请参阅 <a class="reference-link" href="Installation%20%26%20Setup/Server%20Installation/Authentication/Resetting%20your%20password.md">重置密码</a>。

## 报告错误

报告错误非常有价值。以下是一些提示：

*   使用 GitHub issues 进行报告：[https://github.com/TriliumNext/Trilium/issues](https://github.com/TriliumNext/Trilium/issues)
*   请参阅[错误日志](Troubleshooting/Error%20logs.md)页面，了解提供必要详细信息的相关信息。