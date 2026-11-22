# 旁注块
旁注块将内容与笔记正文区分开来，放在一个正文可以环绕的框中。它可以容纳任何类型的内容，例如格式化文本、列表、表格或图片，但不能包含另一个旁注块。

## 插入旁注块

*   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中，转到 _插入_ → <span class="tn-icon cke cke-trilium-aside"></span> _旁注_。
*   或者，输入 `/aside` 并按 <kbd>Enter</kbd>，如<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中所述。

如果在插入旁注之前选中了内容，该内容将被移入新创建的块中。

## 颜色

新建的旁注块具有灰色背景，即调色板中的 _暗灰色_。要更改它，请将光标放在块内，然后单击块上方出现的工具栏中的 <span class="tn-icon bx bx-color-fill"></span> _背景颜色_ 按钮。它提供调色板和文本背景颜色的颜色选择器（<span class="tn-icon cke cke-color-palette"></span>），如<a class="reference-link" href="General%20formatting.md">常规格式</a>中所述。_移除颜色_ 会使块变为透明。

与文本颜色一样，背景颜色会适应[主题](../../Basic%20Concepts%20and%20Features/Themes.md)：Trilium 会以较浅或较深的色调显示它，因此文本在浅色和深色主题下都保持可读。

_背景颜色_ 按钮在移动端布局中不可用。

## 定位

新建的旁注块位于右侧，正文环绕在其周围。要将其放置在其他位置，请将光标放在块内，并使用块上方出现的工具栏中的 _框位置_ 按钮。该菜单有两组：

*   _环绕文本_ 将块保持在笔记的侧面，文本在其旁边流动：<span class="tn-icon cke cke-object-inline-left"></span> _左对齐_ 或 <span class="tn-icon cke cke-object-inline-right"></span> _右对齐_。
*   _分隔文本_ 为块提供独立的行，因此文本仅在其上方和下方继续。除了 <span class="tn-icon cke cke-object-left"></span> _左对齐_ 和 <span class="tn-icon cke cke-object-right"></span> _右对齐_ 之外，该组还可以将块居中（<span class="tn-icon cke cke-object-center"></span> _居中对齐_）。

在移动端布局中，旁注块占据笔记的整个宽度，因此文本不会环绕它，块也无法调整大小。

## 调整大小

要更改旁注块的宽度，请将光标放在块内并拖动其底角的控制柄。高度会自动调整。

## 移除旁注块

要删除旁注及其中的所有内容，请单击其左上角的控制柄并按 <kbd>Delete</kbd>。

## Markdown

当笔记导出为 Markdown 并重新导入时，旁注块会被保留。有关手动编写它们的信息，请参阅<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>中的旁注部分。