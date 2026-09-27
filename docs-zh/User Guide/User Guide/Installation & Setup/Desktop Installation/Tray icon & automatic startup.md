# 托盘图标与自动启动
> [!NOTE]
> 自动启动以及与系统托盘更好的集成是在 v0.104.0 中引入的。此前的版本只有系统托盘选项，可在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _其他_ 中找到。

## 托盘图标

<figure class="image image-style-align-right"><img style="aspect-ratio:332/71;" src="Tray icon &amp; automatic startup_image.png" width="332" height="71"></figure>

桌面应用程序在所有操作系统上都与系统托盘进行了原生集成。

托盘图标默认启用，但可以在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _桌面_ 中切换。

托盘图标具有以下功能：

*   单击时，最后一个窗口会被隐藏（最小化到托盘图标）。再次单击将重新显示该窗口。
*   右键单击会显示以下选项：
    *   每个窗口都可以单独显示或隐藏，通过其活动笔记进行标识。
    *   可以打开新窗口。
    *   可以直接创建新笔记，新笔记将创建在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a> 中（如果没有可用的收件箱，则创建在 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a> 中）。
    *   可以打开今天的日记笔记。
    *   书签和最近的笔记会显示在子菜单中，单击它们会导航到该笔记。
    *   退出应用程序。

### 关闭到系统托盘

这是一个默认未启用的选项，它允许一种特定行为：当最后一个窗口关闭时，不是退出应用程序，而是隐藏最后一个窗口，同时托盘图标仍然可用。

此选项要求启用托盘图标，否则它没有任何效果。

## 自动启动

在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _启动_ 中有两个选项控制自动启动功能：

*   当启用 _启动时运行_ 时，应用程序将在当前用户登录时自动启动。
    *   请注意，在 Linux 上支持情况取决于桌面环境。欢迎 [报告](../../Troubleshooting/Reporting%20issues.md) 任何问题。
*   如果同时启用了 _启动时最小化到托盘_，应用程序将在后台启动，并可以从托盘图标中显示。
    *   这仅在启用 _启动时运行_ 时适用，手动启动不受此选项影响。

### Linux：为打包者提供的自定义启动命令

在 Linux 上，_启动时运行_ 会将一个 `trilium.desktop` 条目写入用户的自启动目录（`$XDG_CONFIG_HOME/autostart`，通常为 `~/.config/autostart`）。其 `Exec` 行在从 AppImage 运行时指向 AppImage，否则指向正在运行的可执行文件。

在系统级 Electron 上运行 Trilium 的发行版软件包（例如 `electron /usr/lib/trilium/app.asar`）不能依赖正在运行的可执行文件，因为它只是裸的 Electron 二进制文件，启动时不会加载 Trilium。此类软件包可以设置 `TRILIUM_LAUNCH_EXEC` 环境变量（通常在其包装脚本中），将其设置为启动 Trilium 的完整命令：

```
export TRILIUM_LAUNCH_EXEC='electron "/usr/lib/trilium/app.asar"'
```

该值会按原样写入 `Exec` 行，因此任何包含空格的路径必须已经加引号。当启用 _启动时最小化到托盘_ 时，会向其追加 `--start-hidden`。`TRILIUM_LAUNCH_EXEC` 优先于 AppImage 路径和正在运行的可执行文件。