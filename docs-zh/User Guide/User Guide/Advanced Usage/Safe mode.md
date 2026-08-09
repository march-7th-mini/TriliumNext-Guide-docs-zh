# 安全模式

安全模式通过将 `TRILIUM_SAFE_MODE` 环境变量设置为真值（通常为 `1`）来触发。

每个构件中都包含一个 `trilium-safe-mode.sh`（或 `.bat`）脚本用于启用该模式。

其作用如下：

*   在 `app/widgets/containers/launcher.js` 中禁用 `customWidget` 启动器类型。
*   禁用 `mobileStartup` 或 `frontendStartup` 脚本的运行。
*   显示根笔记而不是之前保存的会话。
*   禁用 `backendStartup`、`hourly`、`daily` 脚本的运行，并检查隐藏子树。