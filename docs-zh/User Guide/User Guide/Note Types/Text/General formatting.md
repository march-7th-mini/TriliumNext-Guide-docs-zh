# 常规格式设置
## 标题

<figure class="image image-style-align-right"><img style="aspect-ratio:255/284;" src="3_General formatting_image.png" width="255" height="284"></figure>

Trilium 提供了标题功能，用于定义文本中的各个部分。标题的级别从 2 到 6。

列表中缺少一级标题的原因是，一级标题被保留用于笔记的标题。

若要将标题恢复为普通文本，请从列表中选择 _段落_。

除了使用界面外，还可以使用类似 Markdown 的快捷方式快速插入标题：

*   `##` 用于二级标题
*   `###` 用于三级标题
*   `####` 用于四级标题
*   `#####` 用于五级标题
*   `######` 用于六级标题

## 字体大小

<figure class="image image-style-align-right"><img style="aspect-ratio:363/249;" src="General formatting_image.png" width="363" height="249"></figure>

突出显示部分文本的一种方法是增大字体大小。

为此，请选择一些文本，然后从 _字体大小_ 选择器中选择一个选项（如右图所示）。

与 Microsoft Word 等其他文本编辑器不同，这里的字体大小是相对的（例如，“极小”、“小”，而不是像 12 这样的数字）。

请避免仅仅为了将所有文本变大而使用此功能。在这种情况下，通常最好在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> 中调整所有笔记的字体大小，或者通过缩放来实现。

## 加粗、斜体、下划线、删除线

<figure class="image image-style-align-right"><img style="aspect-ratio:215/71;" src="4_General formatting_image.png" width="215" height="71"></figure>

文本可以通过格式工具栏中的专用按钮设置为 **加粗**、_斜体_、下划线 或 ~~删除线~~。

使用 _清除格式_ 项目可以轻松移除这些格式。

这里可以使用以下键盘快捷键：

*   <kbd>Ctrl</kbd>+<kbd>B</kbd> 用于加粗
*   <kbd>Ctrl</kbd>+<kbd>I</kbd> 用于斜体
*   <kbd>Ctrl</kbd>+<kbd>U</kbd> 用于下划线

或者，也可以使用类似 Markdown 的格式：

*   **加粗**：输入 `**text**` 或 `__text__`
*   _斜体_：输入 `*text*` 或 `_text_`
*   ~~删除线~~：输入 `~~text~~`

## 上标、下标

这允许编写上标或下标文本。

这对于度量单位（例如，立方厘米的 cm3）和化学符号（例如，NaHCO3）最为有用。

对于数学公式，请优先使用 <a class="reference-link" href="Math%20Equations.md">数学公式</a> 功能。

## 字体颜色和背景颜色

<figure class="image image-style-align-right"><img style="aspect-ratio:167/204;" src="2_General formatting_image.png" width="167" height="204"></figure>

选中的文本可以使用调色板中的预定义颜色之一进行着色，也可以使用颜色选择器选择任意颜色。

一旦文档中定义了至少一种颜色，它就会出现在列表中，方便重复使用。

在选择前景色或背景色时，请考虑在深色主题和浅色 [主题](../../Basic%20Concepts%20and%20Features/Themes.md) 之间切换时的对比度。

要移除文本的背景色或前景色，请选择相应的格式按钮并按下 _清除颜色_，或使用 _清除格式_ 工具栏项目。

## 清除格式

<img src="1_General formatting_image.png" width="17" height="16"> _清除格式_ 按钮是快速消除特定文本常规格式样式的方法。

只需选择文本并按下该按钮即可移除格式（加粗、斜体、颜色、大小等）。如果文本没有任何可移除的格式，该按钮将显示为禁用状态。

请注意，标题样式不会被考虑在内，必须根据 _标题_ 部分手动将其更改回段落。

当粘贴带有不需要的格式的内容时，除了粘贴后清除格式外，还可以通过 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> 以纯文本形式粘贴。

## 格式刷

<a class="reference-link" href="Format%20Painter.md">格式刷</a> 允许用户复制文本的格式（如加粗、斜体、删除线等），并将其应用于文档的其他部分。它有助于保持格式一致，并加速富内容的创建。

## Markdown 支持

当导出为 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a> 时，大部分常规格式（如标题、加粗、斜体、下划线等）都会得到保留。