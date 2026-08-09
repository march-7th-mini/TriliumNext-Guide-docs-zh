# 数学公式
<figure class="image image-style-align-right"><img style="aspect-ratio:350/193;" src="Math Equations_image.png" width="350" height="193"></figure>

在文本笔记中，可以使用<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>（通常位于<a class="reference-link" href="Insert%20buttons.md">插入按钮</a>下方）中的<img src="1_Math Equations_image.png" width="20" height="15">按钮来输入数学公式。

数学表达式必须以 TeX 格式编写。数学公式没有可视化编辑器，只有预览功能。

启用_显示模式_会使公式渲染得稍大一些（尤其是使用求和、分数等大型运算符时）并将其居中。显示模式下的公式将作为块级元素（即类似于段落或表格），可以插入到列表等位置。非显示模式的公式可以作为文本的一部分。

## 键盘快捷键

如果频繁插入公式，使用 <kbd>Ctrl</kbd>+<kbd>M</kbd> 键盘快捷键可能更方便。或者，直接输入 `$$` 或 `\[` 来触发弹出窗口。

目前还没有快速方法将已输入的公式（例如用 `$` 包围或按 <kbd>Ctrl</kbd>+<kbd>M</kbd>）进行转换。

## 支持的数学功能

从技术上讲，我们使用的是 KaTeX 库，它支持 TeX 格式的一个子集。要查看支持功能的完整列表，请参阅官方文档中的[支持的功能](https://katex.org/docs/supported)和[支持表](https://katex.org/docs/support_table)。

## Markdown 支持

在导出到 Markdown 或从 Markdown 导入时，数学公式将被保留，行内数学表达式用 `$` 字符包围，显示模式用 `$$` 包围。

如果您发现公式的 Markdown 导入/导出有任何问题，请随时[报告](../../Troubleshooting/Reporting%20issues.md)，并提供导致问题的公式。

## 格式化公式

可以像自定义任何其他文本一样，自定义行内和显示模式公式的字体大小和前景色。对于行内公式，还可以调整背景色/高亮。