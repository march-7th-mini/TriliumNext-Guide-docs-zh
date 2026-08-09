# 列表视图
<figure class="image"><img style="aspect-ratio:1387/758;" src="List View_image.png" width="1387" height="758"></figure>

列表视图与<a class="reference-link" href="Grid%20View.md">网格视图</a>类似，但在列表视图模式下，每个笔记以单行显示，默认情况下仅显示笔记的标题和图标。通过点击展开按钮，可以查看笔记的内容以及笔记的子笔记（递归展开）。

在上面的示例中，左侧面板中的“Node.js”笔记包含多个子笔记。右侧面板将这些子笔记的内容显示为单个连续文档。

### 创建新表格

在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击现有笔记，选择 _插入子笔记_，然后查找 _列表视图_。

## 交互

*   每个笔记可以通过点击标题左侧的箭头来展开或折叠。
*   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>的 _集合_ 选项卡中，有选项可以轻松展开和折叠所有笔记。

## 打印和导出为 PDF

自 v0.100.0 起，列表集合可以[打印或导出为 PDF](../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md)。

打印列表集合将按正确顺序打印集合中的所有笔记，并保留完整的层级结构。

如果在桌面应用程序中导出为 PDF，则还有额外功能：

*   PDF 的目录将反映笔记的结构。
*   同一层级内指向其他笔记的引用和内联链接将可用（将跳转到相应页面）。如果链接指向不在打印层级中的笔记，则该链接将变为非链接。

## 同时展开和折叠多个笔记

除了单独展开或折叠笔记外，还可以一次性全部展开或折叠。为此，请前往<a class="reference-link" href="Collection%20Properties.md">集合属性</a>并查找相应的按钮。

默认情况下，_展开_ 按钮只会展开集合的直接子笔记（第一层级）。从 v0.100.0 开始，可以使用按钮旁边的箭头按钮展开多个层级的笔记。

如果应用程序/标签页关闭后再次访问该集合，手动展开的笔记将重置。使用功能区配置自动展开的笔记将保持不变。

> [!TIP]
> 按照设计，UI 仅提供有限的层级深度用于展开笔记（直接子笔记、2-5 层、所有层级）。也可以通过手动设置[相应的标签](../Advanced%20Usage/Attributes/Labels.md)来指定任意所需深度。例如：`#expanded=100` 表示展开到 100 层深度。

> [!NOTE]
> 从性能角度来看，列表集合是高效的，因为它不会加载子笔记，除非笔记实际被展开。对于非常大的层级结构，展开列表可能会导致速度变慢。