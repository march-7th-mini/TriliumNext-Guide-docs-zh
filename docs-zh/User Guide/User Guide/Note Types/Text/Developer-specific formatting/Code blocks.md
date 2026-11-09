# 代码块
![](Code%20blocks_image.jpg)

代码块功能允许在文本笔记中输入代码片段。

请注意，此功能适用于通常较小的代码片段。对于较大的文件（例如完整的日志），请改用 <a class="reference-link" href="../../Code.md">代码</a> 笔记类型。

## 插入代码块

*   通过<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>，找到 <span class="tn-icon cke cke-code-block"></span> 按钮。
    *   直接点击图标将插入一个代码块，使用最近选择的语言。如果这是第一次插入代码块，语言将默认为“自动检测”。
    *   点击图标旁边的箭头，将显示一个包含可用语言的弹出窗口。
*   输入 ` ``` `（如同 Markdown 中那样）。
    *   请注意，无法指定语言，因为它将默认为最后选择的语言。
*   粘贴从 Visual Studio Code 复制的多行代码。
    *   代码块使用 Visual Studio Code 中文件的语言。
    *   如果该语言不在语言列表中，代码块将使用_自动检测_。
    *   Visual Studio Code 主题的颜色会被移除。
    *   单行会变成行内代码而不是代码块。
    *   在 Firefox 中，代码块始终使用_自动检测_。Firefox 无法从 Visual Studio Code 读取语言。

## 退出代码块

*   要退出代码块并输入普通段落，请将光标移到代码块末尾并按两次 Enter。
*   同样，要在笔记块上方插入段落，请将光标移到代码块开头并按两次 Enter。

> [!NOTE]
> 如果您粘贴的代码块具有更复杂的 HTML 结构，通过多次按 Enter 退出代码块可能无法正常工作。在这种情况下，最好的方法是完全删除代码块并使用 Ctrl+Shift+V（粘贴为纯文本）。

## 语法高亮与配色方案

自 TriliumNext v0.90.12 起，Trilium 将尝试为代码块提供语法高亮。请注意，语法高亮机制与<a class="reference-link" href="../../Code.md">代码</a>笔记中的略有不同，因为涉及不同的技术。

交互：

*   当语言设置为_自动检测_（默认）时，Trilium 将尝试识别与给定文本片段对应的编程语言（或类似语言）并对其进行高亮。仅考虑在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ → _下拉菜单中可用的 MIME 类型_ 中启用的语言。如果出现问题，请考虑手动更改代码块的语言。
*   当语言设置为_纯文本_时，将没有语法高亮。

请注意，在编辑文本笔记时，如果代码块太大（大约 500 行左右），语法高亮会自动禁用。在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a>中、打印时以及在[共享页面](../../../Advanced%20Usage/Sharing.md)上，超过 500 行或 50,000 个字符的代码块将不显示语法高亮。这些限制不可配置。

为了配置此新功能，在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _外观_ 中添加了一个部分来控制语法高亮。在那里可以从 Highlight.js 的内置主题选择中选择配色方案。_VS Code（浅色）_ 和 _VS Code（深色）_ 使用与<a class="reference-link" href="../../Code.md">代码</a>笔记默认主题相同的颜色，因此代码块和代码笔记对相同的代码着色一致。

*   可以通过在“配色方案”选项中选择“无语法高亮”来禁用所有笔记的语法高亮。
*   自动换行默认禁用，但可以从同一部分进行配置。
*   制表符宽度也可以从选项中调整。

> [!NOTE]
> **关于语法高亮的背景信息**
> 
> 为了实现语法高亮，使用了 Highlight.js 库。请注意，代码块中的语法高亮支持并不是我们使用的文本编辑器（CKEditor）的受支持功能，而是一种利用 highlights API（例如用于高亮搜索结果）的变通方法。尽管如此，在功能开发过程中我们没有发现任何重大问题，但欢迎报告您可能遇到的任何问题。
> 
> 实现语法高亮本身的大部分工作已由 [antoniotejada](https://github.com/antoniotejada) 在 [https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget) 中完成。在我们这边，我们添加了自定义功能以及其他附加功能。

### 从现有语法高亮插件迁移

如果您已经在使用我们所基于的语法高亮插件（如 [Trilium-SyntaxHighlightWidget](https://github.com/antoniotejada/Trilium-SyntaxHighlightWidget)），请在升级前禁用该插件，以免与我们的实现发生冲突。

如果在迁移后遇到任何问题，请尝试以安全模式运行 Trilium。

## 更改代码块的语言

只需点击代码块内的任意位置，然后再次按<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>中的代码块按钮：  
![](Code%20blocks_image.png)

## 调整语言列表

代码块功能与<a class="reference-link" href="../../Code.md">代码</a>笔记类型共享语言列表。

支持的语言及其列出顺序可以通过前往<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ → _下拉菜单中可用的 MIME 类型_ 进行调整。有关如何添加、删除和重新排序它们的信息，请参阅<a class="reference-link" href="../../Code.md">代码</a>。

请注意，语言列表不会立即刷新，您需要手动[刷新应用程序](../../../Troubleshooting/Refreshing%20the%20application.md)。

## 文本替换与连字

<a class="reference-link" href="../Automatic%20replacements.md">自动替换</a>是文本笔记的一项功能，它将某些字符序列转换为另一种字符序列，其中一些会干扰编程文本，例如引号的转换。在代码块中，自动替换**不会生效**。自动替换唯一可能产生干扰的情况是在文本被放入代码块之前输入/粘贴。

另一个不同的功能是_编程连字_，它只是一种显示效果，将 `!=` 变为 `≠` 或将 `->` 变为 `→`。这些来自[字体](../../../Basic%20Concepts%20and%20Features/Themes/Personalizing%20the%20font.md)。底层文本实际上并未改变，复制出来仍然是 `!=` 和 `->`。

连字可以在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>_→ 外观 → 字体 → 编程连字_ 中禁用。

## 扩展代码块

> [!IMPORTANT]
> 扩展代码块是实验性功能，随着其成熟会发生变化。要使用它们，请在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _高级_ → _实验性选项_ 中开启_扩展代码块_。

扩展代码块是一种在文本内部使用<a class="reference-link" href="../../Code.md">代码</a>笔记的代码编辑器进行编辑的代码块。它具有与代码笔记相同的语法高亮和代码折叠功能，适用于较长的代码片段。

*   要插入一个，请打开<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>的 <span class="tn-icon cke cke-plus"></span> _插入_ 菜单，在_分栏_之后选择 <span class="tn-icon bx bx-code-block"></span> _扩展代码块_。它也可以在<a class="reference-link" href="../Slash%20Commands.md">斜杠命令</a>中作为_扩展代码块_使用。
*   新块是空的且可编辑，位于_完整_框中，并获得焦点。其语言为上次在扩展代码块上设置的语言，或_纯文本_。
*   点击会将光标置于代码中，如同在代码块中一样。在_小_或_中_框上，鼠标滚轮可滚动代码。
*   该块显示在类似于包含的代码笔记的框中，具有代码块的圆角和阴影。当块可编辑时，其语言显示在其顶部角落，如同代码块一样。当它只读时（因为_可编辑_未勾选或笔记是<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md">只读笔记</a>之一），该角落改为显示 <span class="tn-icon bx bx-copy"></span> _复制到剪贴板_ 按钮，如同只读笔记的代码块一样。
*   其工具栏具有嵌入式代码文件的_更改语言模式_和_更改制表符宽度_菜单，在<a class="reference-link" href="../Include%20Note.md">包含笔记</a>的_就地编辑包含内容_中有所描述，以及 <span class="tn-icon cke cke-trilium-copy"></span> _复制到剪贴板_ 按钮，它像代码块一样复制代码。其 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单包含_可编辑_（取消勾选后以只读方式显示代码）、_自动换行_和_行号_子菜单、_大小_子菜单（包含_可调整大小_、_完整_和_默认_）、_位置_子菜单，以及 <span class="tn-icon bx bx-trash"></span> _删除块_，它从笔记中移除该块。
*   _位置_子菜单放置块的方式与放置包含内容相同，在<a class="reference-link" href="../Include%20Note.md">包含笔记</a>的_定位_中有所描述：在其所在行的左侧、居中或右侧，或者在左侧或右侧且文本在其旁边排列。只有_可调整大小_的框可以被定位，并且在调整变窄之前它会占据笔记的整个宽度。在移动布局中，位置不是_居中对齐_的块会占据整个宽度。
*   在块中所做的更改是文本笔记撤销历史的一部分。

代码以其语言的代码块形式保留在笔记中。Markdown 导出、[共享页面](../../../Advanced%20Usage/Sharing.md)和打印会将其显示为代码块，将其复制到另一个应用程序会粘贴为代码块。粘贴到文本笔记中时，它会再次变为扩展代码块，并保留其设置。

再次关闭_扩展代码块_只会将它们从_插入_菜单和斜杠命令中移除：笔记中已有的扩展代码块继续正常工作。没有此功能的 Trilium 版本会将它们显示为代码块，并将它们保存回代码块，不保留其框大小和其他设置。