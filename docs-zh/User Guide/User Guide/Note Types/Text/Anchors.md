# 锚点
> [!NOTE]
> 此功能以前被称为_书签_（这是我们所使用的编辑器中的官方名称），但为了避免与<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md">书签</a>的概念混淆，我们已将其重命名为_锚点_。

锚点允许创建指向笔记特定部分的[链接](Links.md)，例如引用笔记中的某个特定标题或章节。

此功能在 TriliumNext v0.94.0 中引入，并在 v0.103.0 中增强，以支持跨笔记链接。

## 交互

*   创建锚点：
    *   将光标放置在要放置锚点的所需位置。
    *   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中查找 <img src="Anchors_plus.png" width="15" height="16"> 按钮，然后按下 <img src="1_Anchors_plus.png" width="12" height="15"> 按钮。
    *   或者，使用<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>并查找_锚点_。
*   放置指向锚点的链接：
    *   将光标放置在链接的所需位置。
    *   从[链接](Links.md)面板中，选择_锚点_部分并选择所需的锚点。

## 跨笔记链接

Trilium v0.103.0 引入了跨笔记锚点，这使得创建指向该文档中特定锚点的<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>成为可能。

### 与旧版本文档的兼容性

对于在 Trilium v0.103.0 之前创建的笔记，您可能会注意到锚点可能无法被识别。此限制是故意的，以避免重新处理所有笔记来查找锚点。

要解决此问题，只需转到该笔记并进行任何更改（例如插入一个空格），这将触发链接的重新计算。

### 通过_添加链接_对话框链接到锚点

1.  使用上述相同的过程在目标笔记中创建锚点。
2.  在另一个笔记中，按 <kbd>Ctrl</kbd>+<kbd>L</kbd> 插入内部链接。选择包含锚点的目标笔记。
3.  如果目标笔记包含锚点，笔记选择器下方将出现一个部分，其中包含锚点列表。
4.  正常添加链接。

点击指向锚点的引用链接将自动滚动到所需部分。

### 通过书签工具栏链接到锚点

1.  使用上述相同的过程在目标笔记中创建锚点。
2.  点击锚点以显示锚点的浮动工具栏。
3.  点击_复制锚点引用链接_按钮。
4.  转到要插入链接的笔记，然后按 <kbd>Ctrl</kbd>+<kbd>V</kbd>。

> [!NOTE]
> 仅使用此方法在两个文档之间插入<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。要链接到同一笔记上的锚点，请改用_插入链接_对话框（<kbd>Ctrl</kbd>+<kbd>K</kbd>）并选择_锚点_项。