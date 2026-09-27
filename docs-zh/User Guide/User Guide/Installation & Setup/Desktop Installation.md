# 桌面安装
要在桌面上安装 Trilium，请按照以下步骤操作：

1.  **下载最新版本**：从 GitHub 上的[最新版本页面](https://github.com/TriliumNext/Trilium/releases/latest)获取适用于您操作系统的二进制版本。
2.  **解压软件包**：将下载的软件包解压到您选择的位置。
3.  **运行应用程序**：通过执行解压文件夹中的 `trilium` 可执行文件来启动 Trilium。

## 从 Flathub 安装

在 Linux 上，Trilium 也可通过 [Flathub](https://flathub.org/en/apps/org.triliumnotes.Trilium) 获取，支持 x86\_64 和 ARM (aarch64)。您可以从软件中心（例如 GNOME Software 或 KDE Discover）安装，也可以从终端安装：

```sh
flatpak install flathub org.triliumnotes.Trilium
```

更新会像其他 Flatpak 应用一样通过软件中心或 `flatpak update` 推送。

Flathub 版本在沙箱中运行，其[数据目录](Data%20directory.md)位于 `~/.var/app/org.triliumnotes.Trilium/data/trilium-data`。它无法访问 `.deb`、`.rpm`、AppImage 或 `.zip` 安装方式的数据目录（`~/.local/share/trilium-data`），因此会以空数据库启动。要迁移现有笔记：

1.  关闭旧安装和 Flatpak 中的 Trilium。
2.  将旧数据目录复制到沙箱中：
    
    ```sh
    mkdir -p ~/.var/app/org.triliumnotes.Trilium/data
    cp -a ~/.local/share/trilium-data ~/.var/app/org.triliumnotes.Trilium/data/
    ```
3.  启动 Flatpak 版本。

如果 `~/.var/app/org.triliumnotes.Trilium/data/trilium-data` 已经存在（因为之前启动过 Flatpak 版本），请先将其删除或重命名。

## 启动脚本

Trilium 提供了多种启动脚本来自定义您的使用体验：

*   `trilium-no-cert-check`：启动 Trilium 时不验证 [TLS 证书](Server%20Installation/HTTPS%20\(TLS\).md)，适用于连接到使用自签名证书的服务器。
    *   或者，在启动 Trilium 之前设置 `NODE_TLS_REJECT_UNAUTHORIZED=0` 环境变量。
*   `trilium-portable`：以便携模式启动 Trilium，[数据目录](Data%20directory.md)会在应用程序目录内创建，便于整体迁移。Electron 的内部数据（缓存、词典等）也存储在数据目录中，因此不会向系统的漫游配置文件中写入任何文件。
*   `trilium-safe-mode`：以“安全模式”启动 Trilium，禁用任何可能导致应用程序崩溃的启动脚本。

## 同步

对于希望将数据与服务器实例同步的 Trilium 桌面用户，请参阅 <a class="reference-link" href="Synchronization.md">同步</a> 指南以获取详细说明。