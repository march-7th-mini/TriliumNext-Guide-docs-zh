# 代码块

![](1_Code%20blocks_image.png)

代码块功能允许在文本笔记中输入代码片段。

请注意，此功能适用于一般较小的代码片段。对于较大的文件（如整个日志），请改用 <a class="reference-link" href="../../Code.md">代码</a> 笔记类型。

## 插入代码块

*   通过 <a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>，查找 ![](Code%20blocks_image.png) 按钮。
    *   直接点击图标将插入一个使用最近所选语言的代码块。如果这是第一次插入代码块，语言默认为“自动检测”。
    *   点击图标旁边的箭头，将显示一个包含可用语言的下拉菜单。
*   输入 ` ``` ` （如同 Markdown）。
    *   注意无法指定语言，因为它将默认为上次选择的语言。

## 退出代码块

*   要退出代码块并进入普通段落，请将光标移动到代码块末尾并按 <kbd>Enter</kbd> 两次。
*   同样，要在代码块上方插入一个段落，请将光标移动到代码块开头并按 <kbd>Enter</kbd> 两次。

> [!NOTE]
> 如果您粘贴的代码块具有更复杂的 HTML 结构，通过多次按 <kbd>Enter</kbd> 退出代码块可能无效。在这种情况下，最佳方法是完全删除代码块，并使用 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>（粘贴为纯文本）。

## 语法高亮与配色方案

自 TriliumNext v0.90.12 起，Trilium 将尝试为代码块提供语法高亮。请注意，由于涉及的技术不同，此语法高亮机制与 <a class="reference-link" href="../../Code.md">代码</a> 笔记中的机制略有不同。

交互方式：

*   当语言设置为 _自动检测_（默认）时，Trilium 将尝试识别与给定文本片段对应的编程语言（或类似语言）并对其进行高亮。如果存在问题，请考虑手动更改代码块的语言。
*   当语言设置为 _纯文本_ 时，将不会进行语法高亮。

请注意，在编辑文本笔记时，如果代码块太大（大约 500 行左右），语法高亮会自动禁用。此值目前不可配置。对于 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a>，此限制不适用。

为了配置此新功能，在“选项”→“外观”中添加了一个部分来控制语法高亮。可以在其中选择配色方案，从 Highlight.js 的内置主题中进行选择。

*   可以在“配色方案”选项中选择“无语法高亮”来禁用所有笔记的语法高亮。
*   默认情况下禁用自动换行，但可以在同一部分进行配置。
*   也可以从“选项”中调整制表符宽度。

> [!NOTE]
> **关于语法高亮的背景信息**
> 
> 为了实现语法高亮，我们使用了 Highlight.js 库。请注意，代码块中的语法高亮支持并非我们使用的文本编辑器（CKEditor）的受支持功能，而是一种利用高亮 API（例如用于高亮搜索结果）的技巧。尽管如此，我们在开发此功能期间没有发现任何重大问题，但如果您遇到任何问题，请随时报告。
> 
> 实现语法高亮的大部分工作已由 [antoniotejada](https://github.com/antoniotejada) 在 [https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget) 中完成。我们在此基础上添加了自定义功能以及额外的功能。

### 从现有的语法高亮插件迁移

如果您已经在使用我们基于其开发的语法高亮插件（如 [Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget)），则在升级前禁用该插件非常重要，以免与我们的实现冲突。

如果在迁移后遇到任何问题，请尝试在安全模式下运行 Trilium。

## 更改代码块的语言

只需点击代码块内的任意位置，然后再次按下 <a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a> 中的代码块按钮：  
![](2_Code%20blocks_image.png)

## 调整语言列表

代码块功能与 <a class="reference-link" href="../../Code.md">代码</a> 笔记类型共享语言列表。

可以通过转到 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>，然后选择 _代码笔记_ 并查找 _下拉菜单中的可用 MIME 类型_ 部分来调整支持的语言。只需勾选任何项目即可将其添加到列表中，或取消勾选以将其从列表中移除。

请注意，语言列表不会立即刷新，您需要手动 [刷新应用程序](../../../Troubleshooting/Refreshing%20the%20application.md)。