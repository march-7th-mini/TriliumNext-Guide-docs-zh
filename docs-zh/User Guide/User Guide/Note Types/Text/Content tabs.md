# 内容标签页
内容标签页将多个带标题的内容面板组合成一个区块，一次只显示一个面板。它们适用于有多种变体的内容（例如针对每个操作系统的安装步骤，或同一代码片段在多种编程语言中的写法）。

一个标签页区块由以下部分组成：

*   **一行标签页标题。** 正在显示的面板的标题会高亮显示。
*   **活动标签页的面板**，位于标题下方。面板可以容纳任何类型的内容（包括嵌套的标签页区块）。

## 插入标签页区块

*   在格式栏中，转到 _插入_ → _标签页_。
*   或者，输入 `/tabs` 并按 <kbd>Enter</kbd>，如 <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a> 中所述。

新区块包含两个标签页，分别名为“Tab 1”和“Tab 2”。第一个标签页的标题处于选中状态，因此输入内容会将其替换。

## 编辑标签页

*   要显示某个标签页，请点击其标题或将光标移入其中。
*   要从标题移动到其面板，请按 <kbd>Enter</kbd>。
*   标签页的标签可以像普通文本一样进行格式化，包括支持 <a class="reference-link" href="Insert%20buttons/Icons.md">图标</a>。

当光标位于标签页区块内时，其上方会出现一个工具栏，包含以下按钮：

*   <span class="tn-icon cke cke-plus"></span> _(添加标签页)_ 在当前标签页之后插入一个标签页并选中其标题。
*   <span class="tn-icon cke cke-remove"></span> _(移除标签页)_ 移除当前标签页。移除最后一个标签页会移除整个区块。
*   <span class="tn-icon cke cke-chevron-right bx-flip-horizontal"></span> _(左移标签页)_ 和 <span class="tn-icon cke cke-chevron-right"></span> _(右移标签页)_ 改变标签页的顺序。
*   <span class="tn-icon cke cke-link"></span> _(复制标签页链接)_ 复制指向当前标签页的链接，如下所述。

正在显示的标签页不会随笔记一起保存：每个标签页区块打开时都显示其第一个标签页。

## 阅读标签页

在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a> 和 <a class="reference-link" href="../../Advanced%20Usage/Sharing.md">分享</a> 中，标签页区块同样以标签页的形式工作：

*   要显示某个标签页，请点击其标题，或将其聚焦后按 <kbd>Enter</kbd> 或 <kbd>Space</kbd>。
*   要在区块的各个标题之间移动，请使用方向键、<kbd>Home</kbd> 和 <kbd>End</kbd>。

没有标题的标签页会显示“Tab title”来代替标题。

## 链接到标签页

链接可以指向单个标签页，就像指向区块的链接一样（参见 <a class="reference-link" href="Block%20references.md">区块引用</a>）：

1.  将光标放在标签页中，无论是在其标题还是其面板中。
2.  在标签页区块的工具栏中按 _复制标签页链接_。或者，右键点击文本并选择 _复制_ → _复制此标签页的链接_。该标签页会短暂闪烁。
3.  转到要插入链接的笔记，然后按 <kbd>Ctrl</kbd>+<kbd>V</kbd>。

该链接会显示笔记的标题，后跟标签页的标题。点击它会打开笔记、显示该标签页并使其闪烁。与任何区块引用一样，该链接可以转换为仅显示该标签页的 <a class="reference-link" href="Include%20Note.md">包含笔记</a>。

指向标签页的链接只能从正在编辑的笔记中复制。在[共享页面](../../Advanced%20Usage/Sharing.md)上，此类链接会打开整个笔记。

## 隐藏标签页中的内容

未显示的标签页中的内容仍然可以访问（无论是在编辑时还是阅读时）。以下情况会显示包含该内容的标签页：

*   使用 <kbd>Ctrl</kbd>+<kbd>F</kbd> 搜索笔记时高亮显示了其中的匹配项；
*   有链接指向其中的锚点或区块（参见 <a class="reference-link" href="Anchors.md">锚点</a> 和 <a class="reference-link" href="Block%20references.md">区块引用</a>）；
*   <a class="reference-link" href="Table%20of%20contents.md">目录</a> 或 <a class="reference-link" href="Highlights%20list.md">高亮列表</a> 中的某个条目指向其中；
*   在共享页面上，页面地址指向其中的某个标题或锚点。

标签页标题不是标题，因此不会出现在目录中；面板内的标题则会。

## 打印和导出

*   在打印或[导出为 PDF](../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md) 时，每个标签页都会依次打印，每个标签页的标题位于其面板上方。
*   Markdown 导出和导入使用 Material for MkDocs 的内容标签页语法来写入标签页区块，详见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>。<a class="reference-link" href="../Markdown.md">Markdown</a> 笔记使用相同的语法，在其预览中将区块显示为标签页，并通过 `/tabs` 插入它们。
*   在任何标签页无法作为标签页工作的地方（例如在其他地方打开的 HTML 导出），标签页区块会作为一系列带标题的章节来阅读。