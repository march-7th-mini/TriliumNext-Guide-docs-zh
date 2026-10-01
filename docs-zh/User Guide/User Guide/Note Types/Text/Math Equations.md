# 数学公式
<figure class="image image-style-align-right"><img style="aspect-ratio:350/193;" src="Math Equations_image.png" width="350" height="193"></figure>

在文本笔记中，可以使用<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>（通常位于<a class="reference-link" href="Insert%20buttons.md">插入按钮</a>下）中的 <span class="tn-icon cke cke-trilium-math"></span> 按钮来输入数学公式。

数学表达式必须使用 TeX 格式书写。数学公式没有可视化编辑器，只有预览。

启用*显示模式*后，公式会渲染得稍大一些（尤其是在使用求和、分数等大型运算符时）并居中显示。显示模式公式会作为块级元素（即像段落或表格一样），例如可以插入到列表中。非显示模式公式可以作为文本的一部分。

## 键盘快捷键

如果经常插入公式，使用 <kbd>Ctrl</kbd>+<kbd>M</kbd> 键盘快捷键会更方便。或者，直接输入 `$$` 或 `\[` 来触发弹出窗口。

目前还没有快捷方式将已输入的公式转换为公式，例如用 `$` 将其包围或按 <kbd>Ctrl</kbd>+<kbd>M</kbd>。

## 支持的数学功能

技术上我们使用的是 KaTeX 库，它支持 TeX 格式的一个子集。要查看支持功能的完整列表，请查阅官方文档中的[支持的函数](https://katex.org/docs/supported)和[支持表](https://katex.org/docs/support_table)。

## Markdown 支持

数学公式在导出为 Markdown 或从 Markdown 导入时会被保留，行内数学表达式用 `$` 字符包围，显示模式用 `$$` 包围。

如果您发现公式的 Markdown 导入/导出有任何问题，欢迎[报告](../../Troubleshooting/Reporting%20issues.md)，同时请提供导致问题的公式。

## 设置公式格式

可以像其他文本一样，为行内公式和显示模式公式自定义字体大小和前景色。对于行内公式，还可以调整背景色/高亮。