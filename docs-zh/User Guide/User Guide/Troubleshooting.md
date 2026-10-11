# 故障排除
虽然 Trilium 处于积极维护状态且运行稳定，但仍有可能遇到 bug。

## 通用快速修复

故障排除的第一步通常是重启。

如果遇到 UI 问题，前端可能已进入不一致状态。按 <kbd>Ctrl</kbd> + <kbd>R</kbd> 重新加载应用程序。这将重新加载前端。

如果问题仍然存在或似乎是后端问题，请重启整个应用程序。对于桌面（Electron）版本，只需关闭并重新打开窗口即可。如果您使用的是 Docker 版本，请重启容器。

## 报告 Bug

报告 Bug 非常有价值。以下是一些提示：

*   使用 GitHub issues 进行报告：[https://github.com/TriliumNext/Trilium/issues](https://github.com/TriliumNext/Trilium/issues)
*   请参阅[错误日志](Troubleshooting/Error%20logs.md)页面，了解如何提供必要的详细信息。

<details open="">
    <summary>损坏的笔记导致 Trilium 崩溃</summary>
    <p>某些问题，例如渲染带有错误脚本的笔记，可能导致 Trilium 崩溃。如果 Trilium 在重启时尝试重新加载有问题的笔记，它将持续崩溃。</p>
    <p>要解决此问题，请使用 <code>TRILIUM_START_NOTE_ID</code> 环境变量将打开的标签页重置为单个指定的笔记 ID（例如 <code>root</code>）。在 Linux 中，您可以按如下方式设置：</p>
    <pre><code class="language-text-x-trilium-auto">TRILIUM_START_NOTE_ID=root ./trilium</code></pre>
</details>

<details open="">
    <summary>损坏的脚本阻止应用程序启动</summary>
    <p>如果自定义脚本导致 Trilium 崩溃，并且它被设置为启动脚本或位于活动的<a href="Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a>中，请以“安全模式”启动 Trilium 以阻止任何自定义脚本执行：</p>
    <pre><code class="language-text-x-trilium-auto">TRILIUM_SAFE_MODE=true ./trilium</code></pre>
    <p>根据您的 Trilium 发行版本，您可能已有现成的脚本可用：<code>trilium-safe-mode.bat</code> 和 <code>trilium-safe-mode.sh</code>。</p>
    <p>Trilium 启动后，找到并修复或删除有问题的笔记。</p>
</details>

<details open="">
    <summary>同步与一致性检查</summary>
    <p>Trilium 会定期验证数据库的逻辑一致性（例如，确保每个笔记都有父笔记）。如果检测到不一致，您将通过 UI 收到通知。</p>
    <p>在这种情况下，请提交 Bug 报告，并在必要时附上<a href="Troubleshooting/Anonymized%20Database.md">匿名化数据库</a>。</p>
</details>

<details open="">
    <summary>恢复备份</summary>
    <p>Trilium 会定期进行自动备份。如果问题变得严重，您可以<a href="Installation%20%26%20Setup/Backup.md">从备份恢复</a>。</p>
</details>

<details open="">
    <summary>忘记密码</summary>
    <p>请参阅&nbsp;<a class="reference-link" href="Installation%20%26%20Setup/Server%20Installation/Authentication/Resetting%20your%20password.md">重置密码</a>。</p>
</details>