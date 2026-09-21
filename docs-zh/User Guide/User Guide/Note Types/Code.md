# 代码
Trilium 支持创建"代码"笔记，即包含某种形式化代码的笔记——无论是编程语言（C++、JavaScript）、结构化数据（JSON、XML）还是其他类型的代码（CSS 等）。

这在以下几个方面很有用：

*   程序员可以将代码片段存储为带语法高亮的笔记
*   JavaScript 代码笔记可以在 Trilium 内部执行，以实现一些额外功能
    *   我们将此类 JavaScript 代码笔记称为"脚本"——参见 <a class="reference-link" href="../Scripting.md">脚本</a>
*   JSON、XML 等可用作结构化数据的存储（通常与脚本配合使用）

对于可嵌入 [Text](Text.md) 笔记的较短代码片段，请参见[代码块](Text/Developer-specific%20formatting/Code%20blocks.md)。

![](Code_image.png)

## 调整代码笔记的语言

在[功能区](../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md)中，找到*笔记类型*选择器并点击它，以显示可能的笔记类型。在其中会有一个名为*代码*的部分，选择任意一种语言。

![](1_Code_image.png)

## 调整语言列表

Trilium 支持多种语言的语法高亮，但默认只显示其中一部分。可以通过前往[选项](../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md)，然后选择*代码笔记*，找到*下拉菜单中可用的 MIME 类型*部分来调整支持的语言。只需勾选任意项目即可将其添加到列表中，或取消勾选以将其从列表中移除。

请注意，语言列表不会立即刷新，你需要手动[刷新应用程序](../Troubleshooting/Refreshing%20the%20application.md)。

语言列表也与 [Text](Text.md) 笔记的[代码块](Text/Developer-specific%20formatting/Code%20blocks.md)功能共享。

## 自动换行

长行可以显示为多行：

*   全局应用于所有代码笔记，从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → *代码笔记*。
*   针对特定笔记，前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>中的菜单，选择*自动换行*并选择适当的选项：
    *   *自动*，遵循代码笔记的全局自动换行设置。
    *   *开启*或*关闭*，无论全局选项如何，都更改此笔记的自动换行状态。

> [!NOTE]
> 自动换行也可以通过 `#wrapLines` [标签](../Advanced%20Usage/Attributes/Labels.md)在笔记级别进行调整，该标签也可以被继承。

## 使用状态栏调整选项

> [!NOTE]
> 此功能仅适用于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>。对于旧布局，可以使用 `#tabWidth` 属性在笔记级别调整制表符宽度，但不提供重新缩进功能。

编辑器底部的状态栏显示当前的缩进设置和语言。点击缩进指示器会打开一个包含三个部分的菜单：

1.  **缩进方式** — 在空格和制表符之间切换（`#indentWithTabs`）。如果启用了针对笔记的覆盖设置，会出现"重置为默认值"选项。
2.  **显示宽度** — 从预设宽度（1、2、3、4、6、8）中选择。更改会保存为针对笔记的 `#tabWidth` 标签。
3.  **将内容重新缩进为** — 将现有缩进转换为不同的样式。例如，将文件从 4 个空格重新缩进为 2 个空格，或从空格转换为制表符。这会重写每一行的前导空白，同时保留对齐余数。

点击语言指示器可以更改笔记的 MIME 类型。

### 重新缩进

当你重新缩进内容时，编辑器会：

*   使用当前样式测量每一行前导空白的视觉列宽
*   计算缩进级别和任何对齐余数
*   以目标样式重建前导空白
*   保留非前导空白、空行以及没有缩进的内容

## 配色方案

从 Trilium 0.94.0 开始，可以通过前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → 代码笔记，找到*外观*部分来自定义代码笔记的颜色。

> [!NOTE]
> **为什么主题很少，而文本笔记的代码块主题却很多？**  
> 原因是代码笔记使用的技术与文本笔记中使用的技术不同，因此可选主题更为有限。如果你找到了想要使用的 CodeMirror 6（不是 5）主题，请告诉我们，我们可能会考虑将其添加到默认主题集中。目前无法添加新主题（至少目前如此），因为主题是在 JavaScript 中定义的，而非 CSS 级别。

## 编程连字

如果你在代码笔记中看到 `!=` 显示为 `≠` 或 `->` 显示为 `→`，那些是*字体连字*：默认等宽字体将某些字符对绘制为单个符号。底层文本并未被 Trilium 更改（不同于文本笔记具有<a class="reference-link" href="Text/Automatic%20replacements.md">自动替换</a>功能），将其复制出来会得到 `!=` 和 `->`。

可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>*→ 外观 → 字体 → 编程连字*来关闭此功能。

## 虚拟键盘行为

使用虚拟键盘时，键盘建议和更正的控制方式如下：

*   对于 <a class="reference-link" href="Markdown.md">Markdown</a> 和纯文本代码笔记，自动更正为**开启**状态，自动大写也是如此。
*   对于所有其他代码笔记，自动更正为关闭状态，以避免输入代码时出现问题。

> [!NOTE]
> 并非所有浏览器和平台都遵循此设置，因此键盘建议可能会出现但不进行自动更正，或者浏览器可能忽略此设置并仍然进行自动更正。