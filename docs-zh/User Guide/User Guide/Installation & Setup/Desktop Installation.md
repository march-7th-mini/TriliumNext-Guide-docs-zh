# 桌面安装
要在桌面上安装 Trilium，请按照以下步骤操作：

1.  **下载最新版本**：从 GitHub 上的[最新版本页面](https://github.com/TriliumNext/Trilium/releases/latest)获取适用于您操作系统的相应二进制版本。
2.  **解压软件包**：将下载的软件包解压到您选择的位置。
3.  **运行应用程序**：通过执行解压文件夹中的 `trilium` 可执行文件来启动 Trilium。

## 启动脚本

Trilium 提供各种启动脚本以自定义您的体验：

*   `trilium-no-cert-check`：启动 Trilium 时不验证 [TLS 证书](Server%20Installation/HTTPS%20\(TLS\).md)，这在连接到使用自签名证书的服务器时很有用。
    *   或者，在启动 Trilium 前设置 `NODE_TLS_REJECT_UNAUTHORIZED=0` 环境变量。
*   `trilium-portable`：以便携模式启动 Trilium，[数据目录](Data%20directory.md) 将在应用程序目录内创建，从而可以轻松移动整个设置。Electron 的内部数据（缓存、字典等）也存储在数据目录中，因此不会向系统的漫游配置文件写入任何文件。
*   `trilium-safe-mode`：以“安全模式”启动 Trilium，禁用任何可能导致应用程序崩溃的启动脚本。

## 同步

对于希望将数据与服务器实例同步的 Trilium 桌面用户，请参阅 <a class="reference-link" href="Synchronization.md">同步</a> 指南以获取详细说明。