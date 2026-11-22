# 故障排除
## Trilium 只显示空白窗口

Trilium 使用基于 Chromium（Google Chrome 的开源替代品）的 Electron；为了提高性能，它利用了_GPU 加速_。在某些情况下，GPU 不兼容（尤其是在较旧型号的集成显卡上）可能导致完全无法渲染，从而出现空白窗口。

要绕过此问题，请尝试使用以下命令行参数运行 Trilium：

```
trilium --disable-gpu
```

如果这不起作用，也请尝试以下命令：

*   `trilium --disable-gpu-compositing`
*   `ELECTRON_OZONE_PLATFORM_HINT=x11 trilium`（此命令在 Wayland 上强制使用 X11 渲染）

如果此后 Trilium 渲染正常，Trilium 提供了内置选项来禁用 GPU 加速：转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _外观_，找到_性能_部分，然后取消勾选_硬件加速（GPU）_。

## Trilium 启动时因沙箱错误崩溃（Linux）

Trilium 在 Chromium 的沙箱中运行其窗口。Chromium 从非特权用户命名空间构建该沙箱，当系统不允许时，会回退到一个辅助程序 `chrome-sandbox`。Ubuntu 23.10 及更高版本通过 AppArmor 限制非特权用户命名空间，因此在这些系统上运行的是回退方案。该辅助程序只有在由 `root` 拥有并具有 setuid 位（模式 `4755`）时才能工作。

`.deb` 包以这种方式安装 `chrome-sandbox`，而 Flathub 版本使用 Flatpak 沙箱，因此两者都能正常启动。`.zip` 归档则不能：解压后辅助程序归你的用户所有，Trilium 在启动后立即停止并显示：

```
FATAL:setuid_sandbox_host.cc The SUID sandbox helper binary was found, but is not configured correctly. Rather than run without sandboxing I'm aborting now. You need to make sure that …/chrome-sandbox is owned by root and has mode 4755.
```

要解决此问题，请按优先顺序使用以下方法之一：

*   安装 `.deb` 包或 Flathub 版本（参见 <a class="reference-link" href="../Desktop%20Installation.md">桌面安装</a>），而不是 `.zip` 归档。
*   保留 `.zip` 归档并自行设置辅助程序：
    
    1.  重命名解压后的文件夹，使其完整路径不包含空格。归档解压为 `Trilium Notes-linux-x64`，而 setuid 辅助程序无法从包含空格的路径启动 Trilium（`LaunchProcess: failed to execvp`，然后是 `Zygote process exited prematurely`）。
        
        ```sh
        mv "Trilium Notes-linux-x64" trilium-linux-x64
        ```
    2.  使 `chrome-sandbox` 归 `root` 所有并设置 setuid：
        
        ```sh
        cd trilium-linux-x64
        sudo chown root:root chrome-sandbox
        sudo chmod 4755 chrome-sandbox
        ```
    3.  使用 `./trilium` 启动 Trilium。
    
    解压较新版本后请重复这些步骤。
*   使用 `./trilium --no-sandbox` 启动 Trilium。

> [!WARNING]
> `--no-sandbox` 会为整个应用程序关闭 Chromium 的沙箱，包括 Trilium 显示的网页内容、剪藏页面和导入的 HTML。仅将其用于让 Trilium 运行，不要作为永久设置。

### 错误提到 `credentials.cc`

在某些 Ubuntu 系统上，Trilium（包括 `.deb` 包）会改为以下列内容停止：

```
FATAL:credentials.cc Check failed: . : Permission denied (13)
```

当 AppArmor 限制用户命名空间但未加载其 `unprivileged_userns` 配置文件时会发生这种情况，例如在 Ubuntu 实时会话中。Chromium 随后永远不会到达 `chrome-sandbox` 回退方案。要解决此问题，请为 Trilium 提供一个允许用户命名空间的 AppArmor 配置文件：

```sh
sudo tee /etc/apparmor.d/trilium > /dev/null << 'EOF'
abi <abi/4.0>,
include <tunables/global>

profile trilium /usr/lib/trilium/trilium flags=(unconfined) {
  userns,
  include if exists <local/trilium>
}
EOF
sudo apparmor_parser -r /etc/apparmor.d/trilium
```

路径 `/usr/lib/trilium/trilium` 是 `.deb` 包安装 Trilium 的位置。对于 `.zip` 归档，请将其替换为解压文件夹中 `trilium` 可执行文件的完整路径。

要查看适用两种情况中的哪一种，请运行 `journalctl -k | grep userns_create`：`failed to find unprivileged_userns profile` 表示需要上述配置文件，而 `transitioning profile` 表示需要执行 `chrome-sandbox` 相关步骤。