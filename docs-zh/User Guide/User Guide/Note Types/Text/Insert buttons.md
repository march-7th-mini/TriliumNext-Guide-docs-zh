# 插入按钮
按 <a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a> 中的 <span class="tn-icon cke cke-plus"></span> 按钮，即可显示可插入的特殊项目和块，例如符号、数学表达式和分隔符。

## 书签

请参阅专门的 <a class="reference-link" href="Anchors.md">锚点</a> 章节。

## 表情符号

<figure class="image image-style-align-right image_resized" style="width:42.4%;"><img style="aspect-ratio:366/410;" src="Insert buttons_plus.png" width="366" height="410"></figure>

此功能允许插入 Unicode 表情符号字符。只需选择一个类别和所需的表情符号即可插入。

表情符号也可以通过其英文名称进行搜索，并且可以通过右侧的组合框选择肤色。

还可以通过输入 `:` 后跟表情符号的名称来直接插入表情符号，这会触发表情符号列表的显示。只需使用方向键选择一个，然后按 <kbd>Enter</kbd> 或 <kbd>Tab</kbd> 即可插入。

<img src="1_Insert buttons_plus.png" width="272" height="187">

## 符号

<figure class="image image-style-align-right"><img style="aspect-ratio:346/322;" src="Insert buttons_image.png" width="346" height="322"></figure>

按 <span class="tn-icon cke cke-special-characters"></span> 按钮将显示一个弹出窗口，其中列出了通常较难直接从键盘插入的字符，例如部分表情符号、引号字符等。

交互方式：

*   点击某个字符即可将其插入到当前光标位置。
*   可以通过标题所在的顶部栏拖动窗口，以免遮挡文本。
*   点击 _类别_ 选择器可筛选字符。

## 多栏布局

请参阅专门的 <a class="reference-link" href="Multicolumn%20layout.md">多栏布局</a> 页面。

## 数学公式

请参阅专门的 <a class="reference-link" href="Math%20Equations.md">数学公式</a> 页面。

## 绘图画布

选择 <span class="tn-icon bx bx-pen"></span> _绘图画布_，即可在文本内的 Excalidraw 画布上绘图。请参阅 <a class="reference-link" href="Include%20Note.md">包含笔记</a> 中的 _绘图画布_。

## Mermaid 图表

按 <span class="tn-icon cke cke-trilium-mermaid-insert"></span> 按钮可创建内联 Mermaid 图表。

此功能与 <a class="reference-link" href="../Mermaid%20Diagrams.md">Mermaid 图表</a> 笔记类型非常相似，旨在作为简单图表的替代方案。对于更复杂的图表，请使用 <a class="reference-link" href="Include%20Note.md">包含笔记</a> 功能来创建专门的 Mermaid 笔记。

<figure class="image"><img style="aspect-ratio:1174/358;" src="2_Insert buttons_image.png" width="1174" height="358"></figure>

## 水平分隔线

此功能将显示一条水平线，通常用于分隔文本的不同部分。为此，请按 <a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a> 中的 <span class="tn-icon cke cke-horizontal-line"></span> 按钮。

<img src="1_Insert buttons_image.png" width="502" height="95">

或者，也可以通过输入 `---` 来插入水平分隔线。

## 分页符

<figure class="image image-style-align-right"><img style="aspect-ratio:371/79;" src="3_Insert buttons_image.png" width="371" height="79"></figure>

分页符提供了一种方式，可以在打印时（无论是打印到真实打印机，还是[导出为 PDF 时](../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md)）强制将下一个段落或块（表格、图片等）显示在下一页。

分页符在编辑器中以 _分页符_ 字样标记，但在实际打印时不会显示。

*   要插入分页符，请按格式工具栏中的 <span class="tn-icon cke cke-page-break"></span>。
*   要一次插入多个分页符，请先插入一个分页符，点击它并按 <kbd>Ctrl</kbd>+<kbd>C</kbd>。然后使用 <kbd>Ctrl</kbd>+<kbd>V</kbd>，根据需要粘贴任意多次。

## 日期和时间

<span class="tn-icon cke cke-trilium-date-time"></span> 按钮会在光标处插入当前日期和时间，如果有选中的文本则会替换它。插入的文本会采用其周围文本的格式，因此在粗体文本中插入的日期也会是粗体。

*   要以默认格式插入日期，请按该按钮本身或按 <kbd>Alt</kbd>+<kbd>T</kbd>。
*   要以其他格式插入，请按按钮旁边的箭头，然后从列表中选择一种格式。每个条目都会以该格式显示当前日期和时间：默认格式、仅日期或仅时间、完整写出的日期，以及 ISO 8601。
*   <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a> 也提供相同的格式：输入 `/date`、`/time`、`/now` 或 `/today`。_插入日期/时间_ 条目使用默认格式，并在下方显示其插入的内容；其他条目则在标题中显示其输出。

默认格式可以在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ → _编辑器_ → _日期/时间格式_ 中更改，使用 [Day.js 格式标记](https://day.js.org/docs/en/display/format)（例如 `DD.MM.YYYY HH:mm`）。

## 图标

就像[笔记图标](../../Basic%20Concepts%20and%20Features/Notes/Note%20Icons%20%26%20Colors.md)所用的图标一样，图标也可以插入到文本中。有关更多信息，请参阅 <a class="reference-link" href="Insert%20buttons/Icons.md">图标</a>。