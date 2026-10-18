# 内容标签页

内容标签页将多个带标题的内容面板组合成一个区块，一次只显示一个面板。它们适用于有多种变体的内容（例如各操作系统的安装步骤，或同一代码片段在多种编程语言中的版本）。

一个标签页区块由以下部分组成：

*   **一行标签页标题**，位于面板上方；当标签页对齐到底部时，则位于面板下方。当前显示的面板的标题会高亮显示。
*   **活动标签页的面板。** 面板可以容纳任何类型的内容（包括嵌套的标签页区块）。

## 插入标签页区块

*   在格式栏中，转到 _插入_ → _标签页_。
*   或者，输入 `/tabs` 并按 <kbd>Enter</kbd>，如<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中所述。

新区块包含两个标签页，分别名为“Tab 1”和“Tab 2”。插入标签页之前选中的任何内容都会被移入第一个标签页。第一个标签页的标题处于选中状态，因此输入即可替换它。

## 滚动浏览标题

当区块的标题无法在一行内显示时，其两端会出现 <span class="tn-icon bx bx-chevron-left"></span> 按钮和 <span class="tn-icon bx bx-chevron-right"></span> 按钮：

*   要滚动标题，请点击其中一个按钮。按住按钮会持续滚动标题，直到松开为止。
*   在触摸屏上，也可以横向滑动标题。

每当显示另一个标签页时（例如点击其标题、将光标移入其中或通过链接跳转到它），该行会滚动，使其完整标题可见。这在编辑时、只读笔记中以及共享页面上都同样有效。

## 编辑标签页

*   要显示某个标签页，请点击其标题或将光标移入其中。
*   要从标题移动到其面板，请按 <kbd>Enter</kbd>。
*   标签页的标签可以像普通文本一样设置格式，包括支持<a class="reference-link" href="Insert%20buttons/Icons.md">图标</a>。

当光标位于标签页区块内时，其上方会出现一个工具栏，包含以下按钮：

*   <span class="tn-icon cke cke-plus"></span> _（添加标签页）_ 在当前标签页之后插入一个标签页，并选中其标题。
*   <span class="tn-icon cke cke-remove"></span> _（移除标签页）_ 移除当前标签页。移除最后一个标签页会移除整个区块。
*   <span class="tn-icon cke cke-chevron-right bx-flip-horizontal"></span> _（左移标签页）_ 和 <span class="tn-icon cke cke-chevron-right"></span> _（右移标签页）_ 更改标签页的顺序。
*   <span class="tn-icon cke cke-link"></span> _（复制标签页链接）_ 复制指向当前标签页的链接，如下所述。
*   <span class="tn-icon cke cke-trilium-tabs"></span> _（标签页对齐）_ 将标签页标题放在面板上方（_标签页顶部对齐_，默认值）或下方（_标签页底部对齐_）。

当前显示的标签页不会随笔记保存：每个标签页区块打开时都显示其第一个标签页。

### 添加标签页

当光标位于某个标签页中（无论是在其标题还是面板中）时，可以使用以下组合键：

*   <kbd>Ctrl</kbd> + <kbd>Enter</kbd>：在当前标签页之后添加一个标签页。
*   <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>：在当前标签页之前添加一个标签页。

新标签页会显示出来，其标题处于选中状态，因此输入即可替换它。

<kbd>Ctrl</kbd> + <kbd>Enter</kbd> 在链接、待办事项和可折叠区块的标题中保留其通常功能，<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> 在待办事项中也是如此。

### 重新排序标签页

当光标位于某个标签页中（无论是在其标题还是面板中）时，可以使用以下组合键：

*   <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Right</kbd>：将标签页向右移动。
*   <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Left</kbd>：将标签页向左移动。
*   <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Home</kbd>：使其成为第一个标签页。
*   <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>End</kbd>：使其成为最后一个标签页。

## 在标签页之间移动内容

要将内容移动到另一个标签页，请在面板中选中它，然后使用以下组合键：

*   <kbd>Ctrl</kbd> + <kbd>Right</kbd>：移动到右侧的标签页。
*   <kbd>Ctrl</kbd> + <kbd>Left</kbd>：移动到左侧的标签页。
*   <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>End</kbd>：移动到最后一个标签页。
*   <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Home</kbd>：移动到第一个标签页。

接收内容的标签页会显示出来，内容仍处于选中状态，因此再次按键会将其移动到下一个标签页。段落、列表项、表格和其他区块会整体移动，即使只选中了其中一部分。移动到左侧标签页的内容会放到该标签页的末尾，而移动到右侧标签页的内容会放到其开头，因此它在阅读顺序中保持其位置。

在没有选中内容，或选中内容位于标签页标题中时，这些键保留其通常功能：按词移动光标，或选中到标签页的开头或结尾。

当标签页区块和<a class="reference-link" href="Multicolumn%20layout.md">多栏布局</a>相互嵌套时，组合键作用于最靠近光标的那个。

## 阅读标签页

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a>和<a class="reference-link" href="../../Advanced%20Usage/Sharing.md">共享</a>中，标签页区块也作为标签页工作：

*   要显示某个标签页，请点击其标题，或聚焦它并按 <kbd>Enter</kbd> 或 <kbd>Space</kbd>。
*   要在区块的标题之间移动，请使用方向键、<kbd>Home</kbd> 和 <kbd>End</kbd>。

没有标题的标签页会显示“Tab title”作为替代。

在只读笔记中，标题过长而无法在其标签页中显示时，会在被截断处淡出。要阅读其余部分，请横向滑动它或用鼠标拖动它。

## 链接到标签页

链接可以指向单个标签页，就像指向区块的链接一样（参见<a class="reference-link" href="Block%20references.md">区块引用</a>）：

1.  将光标放在标签页中，无论是在其标题还是面板中。
2.  在标签页区块的工具栏中按 _复制标签页链接_（<span class="tn-icon cke cke-link"></span>）。或者，右键点击文本并选择 _复制_ → _复制此标签页的链接_。标签页会短暂闪烁。
3.  转到要插入链接的笔记，然后按 <kbd>Ctrl</kbd>+<kbd>V</kbd>。

链接会显示笔记的标题，后跟标签页的标题。点击它会打开笔记、显示该标签页并使其闪烁。与任何区块引用一样，该链接可以转换为只显示该标签页的<a class="reference-link" href="Include%20Note.md">包含笔记</a>。

只能从正在编辑的笔记中复制指向标签页的链接。在[共享页面](../../Advanced%20Usage/Sharing.md)上，此类链接会打开整个笔记。

## 隐藏标签页中的内容

未显示的标签页中的内容仍然可以访问（无论是在编辑时还是阅读时）。当以下情况发生时，包含该内容的标签页会显示出来：

*   使用 <kbd>Ctrl</kbd>+<kbd>F</kbd> 搜索笔记时，高亮显示了其中的匹配项；
*   链接指向其中的锚点或区块（参见<a class="reference-link" href="Anchors.md">锚点</a>和<a class="reference-link" href="Block%20references.md">区块引用</a>）；
*   <a class="reference-link" href="Table%20of%20contents.md">目录</a>或<a class="reference-link" href="Highlights%20list.md">高亮列表</a>中的条目指向其中；
*   在共享页面上，页面地址指向其中的标题或锚点。

标签页标题不是标题，因此不会出现在目录中；面板内的标题则会。

## 打印和导出

*   在打印或[导出为 PDF](../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md)时，每个标签页都会依次打印，每个标签页的标题位于其面板上方，无论标签页对齐方式如何。
*   Markdown 导出和导入会以 Material for MkDocs 的内容标签页语法写入标签页区块，如<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>中所述。<a class="reference-link" href="../Markdown.md">Markdown</a> 笔记使用相同的语法，在其预览中将区块显示为标签页，并使用 `/tabs` 插入它们。该语法没有标签页对齐，因此底部对齐的标签页会导出为常规标签页。
*   在任何标签页无法作为标签页工作的地方（例如在其他地方打开的 HTML 导出中），标签页区块会显示为一系列带标题的章节。