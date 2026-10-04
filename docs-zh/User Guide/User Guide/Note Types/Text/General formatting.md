# 通用格式
## 标题

<figure class="image image-style-align-right"><img style="aspect-ratio:255/284;" src="2_General formatting_image.png" width="255" height="284"></figure>

Trilium 提供标题来定义文本中的章节。标题编号从 2 到 6。

列表中缺少标题 1 的原因是它被保留用于笔记的标题。

要将标题变回普通文本，请从列表中选择 _段落_。

除了使用 UI 之外，还可以使用类似 Markdown 的快捷方式快速插入标题：

*   `##` 用于标题 2
*   `###` 用于标题 3
*   `####` 用于标题 4
*   `#####` 用于标题 5
*   `######` 用于标题 6

## 字体大小

<figure class="image image-style-align-right"><img style="aspect-ratio:363/249;" src="General formatting_image.png" width="363" height="249"></figure>

突出显示部分文本的一种方法是增大字体大小。

为此，请选择一些文本，然后从 _字体大小_ 选择器中选择一个选项（如右图所示）。

与 Microsoft Word 等其他文本编辑器不同，字体大小是相对的（即“极小”、“小”，而不是像 12 这样的数字）。

避免仅仅为了让所有文本变大而使用此功能。在这种情况下，通常最好在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> 中调整所有笔记的字体大小，或者通过缩放来实现。

## 粗体、斜体、下划线、删除线

<figure class="image image-style-align-right"><img style="aspect-ratio:215/71;" src="3_General formatting_image.png" width="215" height="71"></figure>

可以通过格式工具栏中的专用按钮将文本格式化为 **粗体、** _斜体、_ 下划线或 ~~删除线~~。

可以使用 _移除格式_ 项轻松移除此格式。

此处可以使用以下键盘快捷键：

*   <kbd>Ctrl</kbd>+<kbd>B</kbd> 用于粗体
*   <kbd>Ctrl</kbd>+<kbd>I</kbd> 用于斜体
*   <kbd>Ctrl</kbd>+<kbd>U</kbd> 用于下划线

或者，可以使用类似 Markdown 的格式：

*   **粗体**：输入 `**text**` 或 `__text__`
*   _斜体_：输入 `*text*` 或 `_text_`
*   ~~删除线~~：输入 `~~text~~`

## 上标、下标

这允许书写上标或下标文本。

这主要用于计量单位（例如 cm3 表示立方厘米）和化学符号（例如 NaHCO3）

对于数学公式，请优先使用 <a class="reference-link" href="Math%20Equations.md">数学公式</a> 功能。

## 字体颜色和背景颜色

<figure class="image image-style-align-right"><img style="aspect-ratio:167/204;" src="1_General formatting_image.png" width="167" height="204"></figure>

可以使用调色板中的预定义颜色之一为选中的文本着色，也可以使用颜色选择器选择任意颜色。

一旦文档中定义了至少一种颜色，它就会出现在列表中以便于重复使用。

颜色会适应[主题](../../Basic%20Concepts%20and%20Features/Themes.md)。Trilium 会以适合当前主题的较浅或较深色调显示每种颜色，因此在浅色和深色主题之间切换后文本仍然可读。色相保持不变：红色文本在两个主题中都是红色，只是更浅或更深。这同样适用于调色板、颜色选择器和文档颜色，也适用于共享笔记。打印的笔记和 PDF 导出始终使用适合白纸的浅色主题色调。笔记本身会保留选取时的颜色，因此导出的笔记会原样显示该颜色。

使用旧版本 Trilium 应用的颜色会完全按照选取时的样子显示，直到笔记下次被编辑。

无法适应颜色的旧版浏览器会完全按照选取时的样子显示颜色。

当你在 Chrome、Edge 或基于 Chromium 的应用（如 Visual Studio Code）中粘贴从网页复制的文本时，Trilium 会移除页面的样式：

*   文本和背景颜色。
*   字体和字体大小。
*   表格边框、背景和间距。

以下格式会被保留：

*   粗体、斜体、下划线和删除线。
*   上标和下标。
*   链接、代码和表格。

从 Word、Google Docs 或其他笔记粘贴时，颜色会被保留。

要移除文本的背景色或前景色，请选择相应的格式按钮并按下 _移除颜色_，或使用 _移除格式_ 工具栏项。

## 移除格式

<span class="tn-icon cke cke-remove-format"></span> _移除格式_ 按钮是消除特定文本通用格式样式的快捷方式。

只需选择文本并按下按钮即可移除格式（粗体、斜体、颜色、大小等）。如果文本没有任何可移除的格式，该按钮将显示为禁用状态。

请注意，标题样式不在考虑范围内，必须根据 _标题_ 部分手动将其改回段落。

当粘贴带有不需要的格式的内容时，除了先粘贴再移除格式之外，另一种方法是通过 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> 以纯文本形式粘贴。

## 格式刷

<a class="reference-link" href="Format%20Painter.md">格式刷</a> 允许用户复制文本的格式（如粗体、斜体、删除线等）并将其应用到文档的其他部分。它有助于保持格式一致并加速富内容的创建。

## 对 Markdown 的支持

导出为 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a> 时，大多数通用格式都会保留，如标题、粗体、斜体、下划线等。