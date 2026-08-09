# 托盘图标与自动启动
> [!NOTE]
> 自动启动及与系统托盘的更好集成功能在 v0.104.0 版本中引入。此前的版本仅有系统托盘选项，可在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _其他_ 中找到。

## 托盘图标

<figure class="image image-style-align-right"><img style="aspect-ratio:332/71;" src="Tray icon &amp; automatic startup_image.png" width="332" height="71"></figure>

桌面应用在所有操作系统上均原生集成了系统托盘功能。

托盘图标默认启用，但可在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _桌面_ 中进行切换。

托盘图标具有以下功能：

*   单击时，最后一个窗口将被隐藏（最小化到托盘图标）。再次单击将重新显示该窗口。
*   右键单击显示以下选项：
    *   每个窗口都可以单独显示或隐藏，以其当前活动的笔记进行标识。
    *   可以打开新窗口。
    *   可以直接创建新笔记，该笔记将创建在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>（或 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">每日笔记</a>，如果收件箱不可用）。
    *   可以打开今天的每日笔记。
    *   书签和最近笔记显示在子菜单中，点击它们将导航到该笔记。
    *   退出应用程序。

### 关闭到系统托盘

这是一个默认未启用的选项，它允许一种特定行为：当最后一个窗口被关闭时，不是退出应用程序，而是隐藏最后一个窗口，同时托盘图标保持可用。

此选项要求启用托盘图标，否则无效。

## 自动启动

<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _启动_ 中有两个选项控制自动启动功能：

*   当启用 _登录时启动_ 时，应用程序将在登录当前用户时自动启动。
    *   请注意，在 Linux 上，支持程度取决于桌面环境。如有任何问题，请随时[报告](../../Troubleshooting/Reporting%20issues.md)。
*   如果同时启用了 _启动时最小化到托盘_，应用程序将在后台启动，并可通过托盘图标显示。
    *   这仅适用于启用了 _登录时启动_ 的情况，手动启动不受此选项影响。