# 桌面安装
要在桌面安装 Trilium，请按以下步骤操作：

1.  **下载最新版本**：从 GitHub 上的[最新版本页面](https://github.com/TriliumNext/Trilium/releases/latest)获取适用于您操作系统的二进制版本。
2.  **解压软件包**：将下载的软件包解压到您选择的位置。
3.  **运行应用程序**：通过执行解压文件夹中的 `trilium` 可执行文件来启动 Trilium。

在 Ubuntu 23.10 及更高版本上，Linux `.zip` 归档在启动前需要额外的设置步骤；请参阅<a class="reference-link" href="Desktop%20Installation/Troubleshooting.md">故障排除</a>。`.deb` 软件包和 Flathub 版本无需此步骤即可使用。

## 从 Flathub 安装

在 Linux 上，Trilium 也可在 [Flathub](https://flathub.org/en/apps/org.triliumnotes.Trilium) 上获取，支持 x86\_64 和 ARM（aarch64）。可从软件中心（如 GNOME Software 或 KDE Discover）安装，或在终端中安装：

```sh
flatpak install flathub org.triliumnotes.Trilium
```

更新通过软件中心或 `flatpak update` 获取，与其他 Flatpak 应用一样。

Flathub 版本在沙盒中运行，其[数据目录](Data%20directory.md)位于 `~/.var/app/org.triliumnotes.Trilium/data/trilium-data`。它无法看到 `.deb`、`.rpm`、AppImage 或 `.zip` 安装的数据目录（`~/.local/share/trilium-data`），因此会以空数据库启动。要迁移现有笔记：

1.  关闭 Trilium，包括旧安装和 Flatpak 版本。
2.  将旧数据目录复制到沙盒中：
    
    ```sh
    mkdir -p ~/.var/app/org.triliumnotes.Trilium/data
    cp -a ~/.local/share/trilium-data ~/.var/app/org.triliumnotes.Trilium/data/
    ```
3.  启动 Flatpak 版本。

如果 `~/.var/app/org.triliumnotes.Trilium/data/trilium-data` 已存在（因为之前启动过 Flatpak 版本），请先删除或重命名它。

沙盒还会隐藏[基于订阅的 AI 提供商](../AI/Providers/Subscription-based%20providers.md)所运行的命令行工具（Claude Code、GitHub Copilot、OpenAI Codex、Google Antigravity）；该页面描述了允许 Flatpak 启动这些工具的权限。

## 启动脚本

Trilium 提供多种启动脚本以自定义您的体验：

*   `trilium-no-cert-check`：启动 Trilium 时不验证 [TLS 证书](Server%20Installation/HTTPS%20\(TLS\).md)，适用于连接使用自签名证书的服务器。
    *   或者，在启动 Trilium 前设置 `NODE_TLS_REJECT_UNAUTHORIZED=0` 环境变量。
*   `trilium-portable`：以便携模式启动 Trilium，[数据目录](Data%20directory.md)创建在应用程序目录内，便于移动整个设置。Electron 的内部数据（缓存、词典等）也存储在数据目录内，因此不会向系统的漫游配置文件写入任何文件。
*   `trilium-safe-mode`：以“安全模式”启动 Trilium，禁用任何可能导致应用程序崩溃的启动脚本。

## 同步

对于希望将数据与服务器实例同步的 Trilium 桌面用户，请参阅<a class="reference-link" href="Synchronization.md">同步</a>指南获取详细说明。