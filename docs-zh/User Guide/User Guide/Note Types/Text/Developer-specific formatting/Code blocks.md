# 代码块
![](1_Code%20blocks_image.png)

代码块功能允许在文本笔记中输入代码片段。

请注意，此功能适用于通常较小的代码片段。对于更大的文件（例如整个日志），请改用 <a class="reference-link" href="../../Code.md">代码</a> 笔记类型。

## 插入代码块

*   通过 <a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>，找到 ![](Code%20blocks_image.png) 按钮。
    *   直接点击图标将插入一个代码块，使用最近选择过的语言。如果这是第一次插入代码块，语言将默认为“自动检测”。
    *   点击图标旁边的箭头，将显示一个包含可用语言的弹出窗口。
*   输入 ` ``` `（如同 Markdown 中那样）。
    *   注意，无法指定语言，它将默认为上次选择的语言。

## 退出代码块

*   要退出代码块并进入普通段落，请将光标移到代码块末尾并按两次 Enter。
*   类似地，要在笔记块上方插入段落，请将光标移到代码块开头并按两次 Enter。

> [!NOTE]
> 如果您粘贴了一个 HTML 结构较复杂的代码块，通过多次按 Enter 退出代码块可能不起作用。在这种情况下，最好的方法是完全删除该代码块，并使用 Ctrl+Shift+V（粘贴为纯文本）。

## 语法高亮与配色方案

自 TriliumNext v0.90.12 起，Trilium 将尝试为代码块提供语法高亮。请注意，语法高亮机制与 <a class="reference-link" href="../../Code.md">代码</a> 笔记中的略有不同，因为涉及不同的技术。

交互方式：

*   当语言设置为 _自动检测_（默认）时，Trilium 将尝试识别与给定文本片段对应的编程语言（或类似语言）并对其进行高亮。如果出现问题，请考虑手动更改代码块的语言。
*   当语言设置为 _纯文本_ 时，将不会有语法高亮。

请注意，在编辑文本笔记时，如果代码块太大（大约 500 行左右），语法高亮会自动禁用。此值目前不可配置。对于 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a>，此限制不适用。

为了配置此新功能，在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _外观_ 中添加了一个部分来控制语法高亮。在那里可以从 Highlight.js 的内置主题选择配色方案。

*   可以通过在“配色方案”选项中选择“无语法高亮”来为所有笔记禁用语法高亮。
*   自动换行默认禁用，但可以从同一部分进行配置。
*   制表符宽度也可以从选项中进行调整。

> [!NOTE]
> **关于语法高亮的背景信息**
> 
> 为了实现语法高亮，使用了 Highlight.js 库。请注意，代码块中的语法高亮支持并非我们使用的文本编辑器（CKEditor）所支持的功能，而是一种利用 highlights API（例如用于高亮搜索结果）的变通方法。尽管如此，我们在功能开发过程中没有发现任何重大问题，但欢迎随时报告您可能遇到的任何问题。
> 
> 实现语法高亮的大部分工作已由 [antoniotejada](https://github.com/antoniotejada) 在 [https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget) 中完成。在我们这边，我们添加了自定义功能以及额外的功能。

### 从现有的语法高亮插件迁移

如果您已经在使用我们所基于的语法高亮插件（如 [Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget)），请在升级前禁用该插件，以免与我们的实现发生冲突。

如果在迁移后遇到任何问题，请尝试以安全模式运行 Trilium。

## 更改代码块的语言

只需点击代码块内的任意位置，然后再次点击 <a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a> 中的代码块按钮：  
![](2_Code%20blocks_image.png)

## 调整语言列表

代码块功能与 <a class="reference-link" href="../../Code.md">代码</a> 笔记类型共享语言列表。

可以通过转到 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>，然后选择 _代码笔记_，找到 _下拉菜单中可用的 MIME 类型_ 部分来调整支持的语言。只需勾选任意项目即可将其添加到列表中，或取消勾选以将其从列表中移除。

请注意，语言列表不会立即刷新，您需要手动[刷新应用程序](../../../Troubleshooting/Refreshing%20the%20application.md)。

## 文本替换与连字

<a class="reference-link" href="../Automatic%20replacements.md">自动替换</a> 是文本笔记的一项功能，它将某些字符序列转换为另一种形式，其中一些会干扰编程文本，例如引号的转换。在代码块中，自动替换**不会生效**。自动替换唯一可能产生干扰的情况是文本在放入代码块之前被输入/粘贴。

另一个功能是 _编程连字_，它只是一种显示效果，将 `!=` 变为 `≠` 或将 `->` 变为 `→`。这些来自[字体](../../../Basic%20Concepts%20and%20Features/Themes/Personalizing%20the%20font.md)。底层文本实际上并未改变，复制出来仍然是 `!=` 和 `->`。

连字可以在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>_→ 外观 → 字体 → 编程连字_ 中禁用。