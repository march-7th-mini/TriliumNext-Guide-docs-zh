# 图标包

<figure class="image image-style-align-right image_resized" style="width:45.14%;"><img style="aspect-ratio:854/649;" src="Icon Packs_image.png" width="854" height="649"></figure>

默认情况下，Trilium 附带一组名为 Boxicons v2 的图标。自 v0.102.0 起，自定义图标包允许为笔记提供更广泛的图标选择。

图标包是 Trilium 特有的，因此它们必须从头开始创建（见下文）或从第三方开发者的 ZIP 文件中导入。

## 示例图标包

Trilium 团队维护了一些未随 Trilium 一起发布的图标包。这些图标包可以在官方网站的[资源页面](https://triliumnotes.org/resources)上找到。

## 导入现有图标包

> [!注意]
> **图标包是第三方内容**
> 
> 除了[示例图标包](https://triliumnotes.org/resources)之外，Trilium 维护者不负责保持图标包的最新状态。如果您对某个特定图标包有问题，则必须向负责该图标包的第三方开发者报告问题，而不是向 Trilium 团队报告。

要导入图标包：

1. 最好在您的笔记树中创建一个专门的位置来放置图标包。
2. 右键单击要放置的位置的笔记，然后选择_导入到笔记中_。
3. 取消选中_安全导入_。
4. 选择_导入_。
5. [刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)。

> [!警告]
> 由于_安全导入_被禁用，请确保您信任来源，因为它可能包含危险的第三方脚本。检查图标包是否安全的一个好方法是手动解压缩 .zip 文件并检查文件内容。图标包应仅包含一个字体文件和一个 JSON 文件。其他文件（尤其是脚本）应被视为有害文件。

## 创建图标包

创建图标包需要一些 Trilium 之外的脚本知识，以便生成图标列表。有关信息，请参阅<a class="reference-link" href="../../Theme%20development/Creating%20an%20icon%20pack.md">创建图标包</a>。

## 使用图标包中的图标

[刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)后，图标包应默认启用。要测试这一点，只需选择一个现有笔记或创建一个新笔记，然后尝试更改笔记图标。

图标列表中的搜索栏右侧应该有一个_筛选_按钮。单击它可以按图标包进行筛选，新导入的图标包应显示在那里。

> [!注意]
> 如果该列表中缺少图标包，则很可能存在问题。
> 
> *   尝试检查<a class="reference-link" href="../../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>以获取线索，并确保图标包具有带有分配值（前缀）的 `#iconPack` [标签](../../Advanced%20Usage/Attributes/Labels.md)。
> *   已[保护](../Notes/Protected%20Notes.md)的图标包将被忽略。

## 与分享和导出功能的集成

自定义图标包也受<a class="reference-link" href="../../Advanced%20Usage/Sharing.md">分享</a>功能支持，它们将显示在笔记树中。但是，为了使图标包对分享功能可见，图标包笔记也必须被分享。

如果您使用自定义分享主题，请确保它支持 `iconPackCss`，否则图标将不会显示。请参考原始分享模板源代码。

自定义图标包在<a class="reference-link" href="../../Advanced%20Usage/Sharing/Exporting%20static%20HTML%20for%20web%20publishing.md">导出静态 HTML 以用于网络发布</a>时也将被保留。在这种情况下，无需使图标包被分享。

## 如果我移除图标包会发生什么

如果图标包被移除或禁用（通过移除或更改其 `#iconPack` 标签），所有使用该图标包的笔记将在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中显示为无图标。除了看起来奇怪之外，这不会引起任何问题。

解决方案是用其他图标替换，尝试使用支持批量操作的<a class="reference-link" href="../Navigation/Search.md">搜索</a>，通过查找前缀来识别使用已删除图标包的笔记，并更改或移除它们的 `iconClass`。