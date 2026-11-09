# 数学公式
<figure class="image image-style-align-right"><img style="aspect-ratio:350/193;" src="Math Equations_image.png" width="350" height="193"></figure>

在文本笔记中，可以使用<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>（通常位于<a class="reference-link" href="Insert%20buttons.md">插入按钮</a>下）中的 <span class="tn-icon cke cke-trilium-math"></span> 按钮来输入数学公式。

默认情况下，数学公式对话框包含一个 MathLive 可视化编辑器和 TeX 字段。在选项 → 文本笔记 → 功能下禁用 _MathLive 可视化编辑器_，即可仅使用 TeX 字段和预览。

要放大字段，请拖动对话框的右下角：MathLive 编辑器和 TeX 字段会随之增大。

启用 _显示模式_ 会使公式渲染得稍大一些（尤其是在使用求和等大型运算符或分数时），并将其居中。显示模式公式将作为块（即类似段落或表格）运作，例如可以插入到列表中。非显示模式公式则可以作为文本的一部分。

## 键盘快捷键

如果频繁插入公式，使用 <kbd>Ctrl</kbd>+<kbd>M</kbd> 键盘快捷键可能更为舒适。或者，直接输入 `$$` 或 `\[` 来触发弹出窗口。

目前还没有快捷方式可以将已经输入的公式转换，例如用 `$` 将其包围或按下 <kbd>Ctrl</kbd>+<kbd>M</kbd>。

## 支持的数学功能

技术上我们使用的是 KaTeX 库，它支持 TeX 格式的一个子集。要查看支持功能的完整列表，请查阅官方文档中的[支持的函数](https://katex.org/docs/supported)和[支持表](https://katex.org/docs/support_table)。

## Markdown 支持

在导出到 Markdown 或从 Markdown 导入时，数学公式将被保留，行内数学表达式用 `$` 字符包围，显示模式用 `$$` 包围。

如果您发现公式的 Markdown 导入/导出存在任何问题，欢迎[报告](../../Troubleshooting/Reporting%20issues.md)，同时请提供导致问题的公式。

## 格式化公式

可以像任何其他文本一样，自定义行内公式和显示模式公式的字体大小和前景色。对于行内公式，还可以调整背景色/高亮。