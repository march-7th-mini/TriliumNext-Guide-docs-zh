# 列表视图
<figure class="image"><img style="aspect-ratio:1387/758;" src="List View_image.png" width="1387" height="758"></figure>

列表视图与<a class="reference-link" href="Grid%20View.md">网格视图</a>类似，但在列表视图模式下，每条笔记显示为单独一行，默认仅显示笔记的标题和图标。通过按下展开按钮，可以查看笔记的内容以及笔记的子笔记（递归显示）。

在上面的示例中，左侧面板的“Node.js”笔记包含若干子笔记。右侧面板将这些子笔记的内容显示为一个连续的文档。

### 创建新表格

在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击现有笔记，然后选择 _插入子笔记_ → _集合_ → _列表视图_。

## 交互

*   点击标题左侧的箭头可以展开或折叠每条笔记。
*   在<a class="reference-link" href="Collection%20Properties.md">集合属性</a>中，有按钮可以轻松展开和折叠所有笔记。

## 打印和导出为 PDF

自 v0.100.0 起，列表集合可以[打印或导出为 PDF](../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md)。

打印列表集合时，将按正确顺序打印集合中的所有笔记，并保留完整的层级结构。

如果在桌面应用程序中导出为 PDF，还有额外的功能：

*   PDF 的目录将反映笔记的结构。
*   指向同一层级结构中其他笔记的引用链接和内联链接将可用（将跳转到相应页面）。如果链接指向的笔记不在打印的层级结构中，则该链接将被取消链接。

## 一次性展开和折叠多条笔记

除了单独展开或折叠笔记外，还可以一次性展开或折叠所有笔记。为此，请转到<a class="reference-link" href="Collection%20Properties.md">集合属性</a>并查找相应的按钮。

默认情况下，_展开_按钮仅展开集合的直接子笔记（第一层级）。从 v0.100.0 开始，可以使用按钮旁边的箭头按钮展开多个层级的笔记。

手动展开的笔记在应用程序/标签页关闭后再次访问集合时将重置。但是，通过<a class="reference-link" href="Collection%20Properties.md">集合属性</a>中的按钮自动展开/折叠的笔记将会保留。

> [!TIP]
> 按照设计，UI 仅提供少数几个展开笔记的深度层级（直接子笔记、2-5 层、所有层级）。也可以通过手动设置[相应的标签](../Advanced%20Usage/Attributes/Labels.md)来指定任意所需的深度。例如：`#expanded=100` 可展开最多 100 个层级。

> [!NOTE]
> 从性能角度来看，列表集合是高效的，因为除非笔记实际被展开，否则不会加载子笔记。对于非常庞大的层级结构，展开列表可能会导致速度变慢。