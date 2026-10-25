# 插入按钮
在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中按下 <span class="tn-icon cke cke-plus"></span> 按钮，即可显示可插入的特殊项目和块，例如符号、数学表达式和分隔符。

## 书签

请参阅专门的<a class="reference-link" href="Anchors.md">锚点</a>章节。

## 表情符号

<figure class="image image-style-align-right image_resized" style="width:42.4%;"><img style="aspect-ratio:366/410;" src="Insert buttons_plus.png" width="366" height="410"></figure>

此功能允许插入 Unicode 表情符号字符。只需选择一个类别和所需的表情符号即可插入。

表情符号也可以通过其英文名称进行搜索，并且可以通过右侧的组合框选择肤色。

还可以通过输入 `:` 后跟表情符号名称来直接插入表情符号，这会触发表情符号列表的显示。只需使用方向键选择一个，然后按 <kbd>Enter</kbd> 或 <kbd>Tab</kbd> 即可插入。

<img src="1_Insert buttons_plus.png" width="272" height="187">

## 符号

<figure class="image image-style-align-right"><img style="aspect-ratio:346/322;" src="Insert buttons_image.png" width="346" height="322"></figure>

按下 <span class="tn-icon cke cke-special-characters"></span> 按钮将显示一个弹出窗口，其中列出了通常较难直接从键盘插入的字符，例如部分表情符号、引号字符等。

交互方式：

*   点击某个字符即可将其插入到当前光标位置。
*   可以通过标题所在的顶栏拖动窗口，以避免遮挡文本。
*   点击 _类别_ 选择器可筛选字符。

## 多栏布局

请参阅专门的<a class="reference-link" href="Multicolumn%20layout.md">多栏布局</a>页面。

## 数学公式

请参阅专门的<a class="reference-link" href="Math%20Equations.md">数学公式</a>页面。

## 绘图画布

选择 <span class="tn-icon bx bx-pen"></span> _绘图画布_ 可在文本内的 Excalidraw 画布上绘图。请参阅<a class="reference-link" href="Include%20Note.md">包含笔记</a>中的 _绘图画布_。

## Mermaid 图表

按下 <span class="tn-icon cke cke-trilium-mermaid-insert"></span> 按钮可创建内联 Mermaid 图表。其旁边的箭头列出了每种图表的模板。该图表也可在<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中作为 _Mermaid 图表_ 使用。

此功能与<a class="reference-link" href="../Mermaid%20Diagrams.md">Mermaid 图表</a>笔记类型非常相似，旨在作为简单图表的替代方案。对于更复杂的图表，请使用<a class="reference-link" href="Include%20Note.md">包含笔记</a>功能来创建专门的 Mermaid 笔记。

<figure class="image"><img style="aspect-ratio:1174/358;" src="2_Insert buttons_image.png" width="1174" height="358"></figure>

图表显示在一个类似于包含笔记的框中，因此可以调整其大小、从其 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单中设置其他框大小（_小_、_中_ 或 _全宽_），或全屏显示，如<a class="reference-link" href="Include%20Note.md">包含笔记</a>中所述。

*   图表工具栏开头的 <span class="tn-icon bx bx-edit-alt"></span> _可编辑_ 按钮决定其源是否可以更改。关闭时，源仍然显示，但为只读。
*   其旁边的按钮选择图表显示的内容，与 Mermaid 笔记类似：<span class="tn-icon bx bx-code"></span> _源码视图_ 仅显示 Mermaid 源码，<span class="tn-icon bx bxs-dock-left"></span> _分屏视图_ 显示源码及旁边的图表，<span class="tn-icon bx bx-show"></span> _预览_ 仅显示图表。其 _更多操作_ 菜单提供相同的选择。
*   其 _更多操作_ 菜单中的 _自动换行_ 和 _行号_ 子菜单可更改源的显示方式，每个都有 _自动_、_开_ 和 _关_ 选项，与包含的代码笔记相同（请参阅<a class="reference-link" href="Include%20Note.md">包含笔记</a>中的 _就地编辑包含内容_）。
*   新图表以可编辑状态启动，处于 _分屏视图_。图表在您停止输入后片刻更新。如果源有错误，错误将显示在最后一次成功生成的图表上方，该图表保持变暗，与 Mermaid 笔记相同。在桌面端，拖动源码和图表之间的分隔条可调整它们的大小。
*   未选择视图的图表在可编辑时显示源码及旁边的图表，否则仅显示图表。在只读笔记中，源永远无法更改。只读笔记和 AI 对话在相同的框中显示图表，使用保存时的视图，并且缩放按钮显示在图表上方而非工具栏中。_中_ 或 _全宽_ 图表在那里也有一个 <span class="tn-icon bx bx-fullscreen"></span> _全屏_ 按钮，或在 _源码_ 视图中显示在源码上方。
*   要缩放，请使用图表工具栏的 <span class="tn-icon bx bx-zoom-out"></span> 和 <span class="tn-icon bx bx-zoom-in"></span> 按钮；它们之间的缩放级别可重置缩放。在全屏模式下，工具栏隐藏，相同的按钮显示在图表上方。拖动图表可移动它，双击可重置视图。鼠标滚轮会滚动笔记，直到您点击图表，然后进行缩放。
*   当源码显示时，工具栏末尾的 <span class="tn-icon bx bx-help-circle"></span> _Mermaid 语法帮助_ 按钮会在<a class="reference-link" href="../Mermaid%20Diagrams.md">Mermaid 图表</a>上打开帮助，其中链接到 Mermaid 语法。
*   对图表源所做的更改是文本笔记撤销历史的一部分，按所做的顺序排列。<kbd>Ctrl</kbd>+<kbd>Z</kbd> 和 <kbd>Ctrl</kbd>+<kbd>Y</kbd> 可从源码以及文本中撤销和重做它们，如<a class="reference-link" href="Include%20Note.md">包含笔记</a>中的 _就地编辑包含内容_ 所述。

图表的源作为 Mermaid 代码块保留在笔记中，因此图表会作为 `mermaid` 代码块导出到 Markdown，其他应用程序可以显示。

在早期版本中创建的图表保留其保存时的视图，并以可编辑状态打开。

## 水平分隔线

此功能将显示一条水平线，通常用于分隔文本的不同部分。为此，请在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中按下 <span class="tn-icon cke cke-horizontal-line"></span> 按钮。

<img src="1_Insert buttons_image.png" width="502" height="95">

或者，也可以通过输入 `---` 来插入水平分隔线。

## 分页符

<figure class="image image-style-align-right"><img style="aspect-ratio:371/79;" src="3_Insert buttons_image.png" width="371" height="79"></figure>

分页符提供了一种在打印时（无论是打印到真实打印机还是[导出为 PDF 时](../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md)）强制下一段落或块（表格、图片等）显示在下一页的方法。

分页符在编辑器中以 _分页符_ 字样标记，但打印时不会实际显示。

*   要插入分页符，请在格式工具栏中按下 <span class="tn-icon cke cke-page-break"></span>。
*   要一次插入多个分页符，请先插入一个分页符，点击它并按 <kbd>Ctrl</kbd>+<kbd>C</kbd>。然后使用 <kbd>Ctrl</kbd>+<kbd>V</kbd> 粘贴所需次数。

## 日期和时间

<span class="tn-icon cke cke-trilium-date-time"></span> 按钮在光标处插入当前日期和时间，如果有选中的文本则替换它。插入的文本采用周围文本的格式，因此在粗体文本中插入的日期也是粗体。

*   要以默认格式插入日期，请按下按钮本身或按 <kbd>Alt</kbd>+<kbd>T</kbd>。
*   要以其他格式插入，请按下按钮旁边的箭头并从列表中选择一种格式。每个条目都以该格式显示当前日期和时间：默认格式、仅日期或仅时间、书面日期以及 ISO 8601。
*   <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>也提供相同的格式：输入 `/date`、`/time`、`/now` 或 `/today`。_插入日期/时间_ 条目使用默认格式，并在下方显示其插入的内容；其他条目在标题中显示其输出。

默认格式可以在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ → _编辑器_ → _日期/时间格式_ 中更改，使用 [Day.js 格式标记](https://day.js.org/docs/en/display/format)（例如 `DD.MM.YYYY HH:mm`）。

## 图标

就像[笔记图标](../../Basic%20Concepts%20and%20Features/Notes/Note%20Icons%20%26%20Colors.md)的图标一样，图标也可以插入到文本中。更多信息请参阅<a class="reference-link" href="Insert%20buttons/Icons.md">图标</a>。