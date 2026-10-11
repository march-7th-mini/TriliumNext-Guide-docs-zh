# 安全模式
安全模式通过将 `TRILIUM_SAFE_MODE` 环境变量设置为真值（通常为 `1`）来触发。

在每个构建产物中都有一个 `trilium-safe-mode.sh`（或 `.bat`）脚本来启用它。

它的作用：

*   禁用 `app/widgets/containers/launcher.js` 中的 `customWidget` 启动器类型。
*   禁用 `mobileStartup` 或 `frontendStartup` 脚本的运行。
*   显示根笔记，而不是之前保存的会话。
*   打开<a class="reference-link" href="../Note%20Types/Saved%20Search.md">保存的搜索</a>时不运行它；按 _立即搜索_ 来运行。
*   禁用 `backendStartup`、`hourly`、`daily` 脚本的运行以及对隐藏子树的检查。