# 将桌面应用用作服务器

有时，搭建[专用服务器安装](../Server%20Installation.md)并不可行。桌面应用默认自带一个功能完整的服务器实例。

出于安全原因，此功能**默认未启用**。要启用它，请在<a class="reference-link" href="../../Scripting/Security.md">安全</a>中启用_网络访问_。

启用网络访问并重启应用后，您可以通过访问 [http://localhost:37840/login](http://localhost:37840/login) 在本地访问此 Web 界面。

> [!NOTE]
> 桌面应用中嵌入的服务器仅在桌面应用本身运行时才会运行。因此，关闭应用也会关闭服务器。要解决此问题，您可以尝试将应用隐藏到系统托盘中。

## 移动端界面

默认情况下，即使在移动设备上，也会显示桌面用户界面。要切换到移动版本，只需进入<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>并选择“切换到移动版本”。

## 在 Windows 上使用 Windows Defender 防火墙允许外部访问端口

首先，在本地终端中运行 `ipconfig` 找出桌面服务器的 IP。然后尝试在另一台设备上访问 `http://<ip>:37840/login`。如果无法访问，很可能是端口被操作系统的防火墙阻止了。

如果您使用 Windows Defender 防火墙：

1.  转到 Windows 开始菜单，搜索“高级安全 Windows Defender 防火墙”。
2.  在左侧树中转到“入站规则”，然后在右侧的“操作”侧边栏中选择“新建规则”。
3.  选择“端口”，然后点击“下一步”。
4.  在“特定本地端口”部分输入 `37840`，然后点击“下一步”。
5.  保持选中“允许连接”，然后点击“下一步”。
6.  配置要应用的网络（如果不确定，请全部勾选），然后点击“下一步”。
7.  为规则添加适当的名称（例如“Trilium Notes”），然后点击“完成”。

> [!WARNING]
> 自 v0.104.0 起，Trilium 使用的端口仅可在 `localhost` 上访问。要允许在本地网络中访问，请参阅<a class="reference-link" href="Network%20Access.md">网络访问</a>。