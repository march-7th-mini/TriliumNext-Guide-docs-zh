# 锚点
> [!NOTE]
> 此功能过去被称为_书签_（因为这是我们使用的编辑器中的官方名称），但为了避免与<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md">书签</a>的概念冲突，我们将其重命名为_锚点_。

锚点允许创建指向笔记特定部分的[链接](Links.md)，例如引用笔记中的特定标题或章节。

此功能在 TriliumNext v0.94.0 中引入，并在 v0.103.0 中增强以支持跨笔记链接。

## 交互

*   创建锚点：
    *   将光标放置在要放置锚点的所需位置。
    *   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中查找 <span class="tn-icon bx bx-plus"></span> 按钮，然后按 <span class="tn-icon cke cke-bookmark"></span> 按钮。
    *   或者，使用<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>并查找 _anchor_。
*   在同一笔记中放置指向锚点的链接：
    *   将光标放置在链接的所需位置，或选择要转换为链接的文本。
    *   按 <kbd>Ctrl</kbd>+<kbd>K</kbd> 或<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中的 <span class="tn-icon cke cke-link"></span> 按钮，然后在[_添加链接_对话框](Links.md)顶部选择_标题 / 锚点_。或者，在<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中选择_链接到标题或锚点_，这将在该页面打开对话框。
    *   在_锚点_下，单击所需的锚点以勾选它。可选地，输入_链接标题_；如果没有，链接将显示锚点的名称。
    *   按 <kbd>Enter</kbd> 或_插入链接_以确认。
*   单击指向同一笔记锚点的链接会滚动到该锚点，并在只读笔记和共享页面中短暂高亮显示包含该锚点的块。在编辑时，单击链接会显示其弹出窗口，其_跳转到锚点_按钮执行相同的操作，<kbd>Ctrl</kbd>+单击和双击也是如此。
*   要更改指向锚点的链接，请将光标放在其中并按 <kbd>Ctrl</kbd>+<kbd>K</kbd>。自 v0.107.0 起，_编辑链接_对话框会在_标题 / 锚点_上打开，并勾选已链接的锚点。

> [!TIP]
> 要链接到同一笔记的标题，不需要锚点：在同一对话框中的_标题_下选择该标题即可。详情请参阅[链接到标题](Block%20references.md)。

## 跨笔记链接

Trilium v0.103.0 引入了跨笔记锚点，这使得可以创建指向该文档中特定锚点的<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。

### 与旧版本文档的兼容性

对于在 Trilium v0.103.0 之前创建的笔记，您可能会注意到锚点可能无法被识别。此限制是有意为之，以避免重新处理所有笔记来查找锚点。

要解决此问题，只需转到该笔记并进行任何更改（例如插入一个空格），这将触发链接的重新计算。

### 通过_添加链接_对话框链接到锚点

1.  使用上述相同流程在目标笔记中创建锚点。
2.  在另一个笔记中，按 <kbd>Ctrl</kbd>+<kbd>L</kbd> 插入内部链接。选择包含锚点的目标笔记。
3.  如果目标笔记包含锚点，则在笔记选择器下方将出现一个部分，其中列出锚点。
4.  正常添加链接。

单击指向锚点的引用链接将自动滚动到所需部分。

### 通过书签工具栏链接到锚点

1.  使用上述相同流程在目标笔记中创建锚点。
2.  单击锚点以显示锚点的浮动工具栏。
3.  单击 <span class="tn-icon cke cke-trilium-copy"></span> _复制锚点引用链接_按钮。
4.  转到要插入链接的笔记并按 <kbd>Ctrl</kbd>+<kbd>V</kbd>。

> [!NOTE]
> 仅使用此方法在两个文档之间插入<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。要链接到同一笔记上的锚点，请改用_添加链接_对话框（<kbd>Ctrl</kbd>+<kbd>K</kbd>）并在其顶部选择_标题 / 锚点_。