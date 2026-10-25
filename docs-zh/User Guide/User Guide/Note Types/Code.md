# 代码

Trilium 支持创建“代码”笔记，即包含某种形式化代码的笔记——无论是编程语言（C++、JavaScript）、结构化数据（JSON、XML）还是其他类型的代码（CSS 等）。

这在以下几个方面很有用：

*   程序员可以将代码片段存储为带有语法高亮的笔记
*   JavaScript 代码笔记可以在 Trilium 内部执行，以实现一些额外功能
    *   我们将此类 JavaScript 代码笔记称为“脚本”——参见 <a class="reference-link" href="../Scripting.md">脚本</a>
*   JSON、XML 等可用作结构化数据的存储（通常与脚本配合使用）

对于可嵌入[文本](Text.md)笔记的较短代码片段，请参见[代码块](Text/Developer-specific%20formatting/Code%20blocks.md)。

![](Code_image.jpg)

## 创建代码笔记

在[笔记树](../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md)中，右键点击一个笔记并选择*插入子笔记*或*插入笔记到之后*，然后：

*   要创建纯文本代码笔记，选择*代码*。
*   要创建指定语言的代码笔记，悬停在*代码*上并选择语言。列表显示在选项中启用的语言（见下文），末尾是*配置代码笔记...*，点击可打开这些选项。

## 调整代码笔记的语言

要更改代码笔记的语言，请在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中查找 <span class="tn-icon bx bx-code"></span> 图标。点击后会显示可用语言列表（可根据下文进行自定义）。该菜单还提供搜索栏以快速筛选，以及用于视觉区分部分编程语言的图标。

在<a class="reference-link" href="../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a>上，同一列表可在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a> → *笔记设置* → *更改语言模式*中找到。

## 调整语言列表

Trilium 支持多种语言的语法高亮，但默认只显示其中一部分。要更改提供的语言，请前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → *代码笔记*，找到*下拉菜单中的可用 MIME 类型*。在此你可以：

*   通过按下 <span class="tn-icon bx bx-plus"></span> *添加其他语言*按钮来添加语言，该按钮还会显示剩余多少种语言，然后选择它。选择时，悬停在某个语言上可查看其语法高亮效果。
*   按下语言旁的 <span class="tn-icon bx bx-x"></span> 按钮，或选中它并按 <kbd>Delete</kbd>，将其从列表中移除。*纯文本*无法移除。
*   查看每种语言的语法高亮位置：*代码块*徽章代表文本笔记中的代码块，*代码笔记*徽章代表代码笔记。

无论你在何处选择语言，语言列表的顺序都相同：<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中的语言菜单、创建笔记时的*代码*子菜单，以及代码块的语言。默认情况下，列表按字母顺序排序，*纯文本*排在首位。要使用自定义顺序：

1.  关闭该区域顶部的*按字母顺序排序*开关。
2.  按住语言旁显示的 **\=** 手柄，然后向上或向下拖动。或者，选中一个语言并按 <kbd>Ctrl</kbd>+<kbd>↑</kbd> 或 <kbd>Ctrl</kbd>+<kbd>↓</kbd>。

重新打开*按字母顺序排序*不会丢弃你的顺序：下次关闭该开关时会再次使用它。

请注意，语言列表不会立即刷新，你需要手动[刷新应用程序](../Troubleshooting/Refreshing%20the%20application.md)。

语言列表也与[文本](Text.md)笔记的[代码块](Text/Developer-specific%20formatting/Code%20blocks.md)功能共享。

## 自动换行

长行可以显示为多行：

*   全局应用于所有代码笔记，从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → *代码笔记*中设置。
*   针对特定笔记，前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a>中的菜单，选择*自动换行*并选择适当的选项：
    *   *自动*，遵循代码笔记的全局自动换行设置。
    *   *开*或*关*，无论全局选项如何，更改此笔记的自动换行状态。

> [!NOTE]
> 自动换行也可以通过 `#wrapLines` [标签](../Advanced%20Usage/Attributes/Labels.md)在笔记级别进行调整，该标签也可以被继承。

## 行号

每行开头的数字可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → *代码笔记* → *编辑器* → *行号*中隐藏。该设置适用于每个代码编辑器，例如 [Markdown](Markdown.md) 笔记的源代码，以及不显示编辑器时展示的代码（参见下文*配色方案*）。

被包含的代码笔记或嵌入的代码文件可以通过其*更多操作*菜单中的*行号*子菜单自行显示或隐藏行号，参见<a class="reference-link" href="Text/Include%20Note.md">包含笔记</a>。其*自动*条目遵循该设置。

## 使用状态栏调整选项

编辑器底部的状态栏显示光标位置、当前缩进设置和语言。

光标位置显示为*行*（行号）和*列*（列号），均从 1 开始计数。一个制表符计为制表符显示宽度的列数，因此列号与光标在屏幕上的位置一致。选中文本时，*已选中*显示选中的字符数，每个换行计为一个字符。

点击缩进指示器会打开一个包含三个部分的菜单：

1.  *缩进使用* — 在空格和制表符之间切换（`#indentWithTabs`）。如果启用了按笔记覆盖，则会出现“重置为默认值”选项。
2.  *显示宽度* — 从预设宽度中选择（1、2、3、4、6、8）。更改会保存为按笔记的 `#tabWidth` 标签。
3.  *重新缩进内容至* — 将现有缩进转换为不同样式。例如，将文件从 4 个空格重新缩进为 2 个空格，或从空格转换为制表符。这会重写每行的前导空白，同时保留对齐余数。

点击语言指示器可更改笔记的 MIME 类型。与*笔记类型*选择器一样，输入可缩小语言列表范围。

同样的两个菜单也出现在代码笔记或文本笔记中包含的代码文件的工具栏中，参见<a class="reference-link" href="Text/Include%20Note.md">包含笔记</a>。

### 重新缩进

当你重新缩进内容时，编辑器会：

*   使用当前样式测量每行前导空白的视觉列宽
*   计算缩进级别和任何对齐余数
*   以目标样式重建前导空白
*   保留非前导空白、空行和无缩进的内容

## 转换文本

要更改选中的行或文本，右键点击选区并打开*转换*。其命令分为三组：

*   *升序排序*、*降序排序*、*随机打乱行*、*反转行顺序*和*去重行*，后者保留每行的第一个副本。
*   *去除前导空白*、*去除尾部空白*和*去除两端空白*删除每行开头、末尾或两端的空白。*删除空行*还会删除仅包含空白的行。
*   *转为大写*、*转为小写*、*转为句首大写*、*转为标题大写*和*移除变音符号*。

前两组的命令会更改选区触及的每一行，即使是部分触及。第三组的命令仅更改选中的文本。每次更改都可以通过 <kbd>Ctrl</kbd>+<kbd>Z</kbd> 一步撤销。

*   排序按值读取数字、日期和时间，与表格排序相同（参见<a class="reference-link" href="Text/Tables.md">表格</a>），并忽略字母大小写和缩进。空行排在最后。
*   *转为句首大写*将文本转为小写，并将每个句子和每行的第一个单词大写。*转为标题大写*将每个单词大写，但“of”和“the”等次要词除外，它们保持小写，除非位于句子开头或结尾。
*   *移除变音符号*将 `é`、`ș` 和 `ł` 等字母转换为 `e`、`s` 和 `l`，并移除希伯来语和阿拉伯语的元音符号。`ß` 和 `æ` 等字母保持不变。
*   排序和大小写更改遵循<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → *语言与地区* → *默认内容语言*中设置的语言。例如，在土耳其语中，大写 `i` 是 `İ`。

## 配色方案

自 Trilium 0.94.0 起，可以通过前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → 代码笔记，找到*外观*部分来自定义代码笔记的颜色。

不显示编辑器的代码笔记或代码文件，例如在<a class="reference-link" href="Text/Include%20Note.md">包含笔记</a>中、<a class="reference-link" href="../Collections.md">集合</a>的卡片上或工具提示中，使用与编辑器相同的颜色和行号。打印输出使用*浅色主题*。[共享页面](../Advanced%20Usage/Sharing.md)使用 VS Code 浅色或深色主题，跟随页面的模式。

> [!NOTE]
> **为什么只有少数几个主题，而文本笔记的代码块主题有很多？**
> 原因是代码笔记使用的技术与文本笔记中使用的技术不同，因此主题选择较为有限。如果你找到想要使用的 CodeMirror 6（不是 5）主题，请告诉我们，我们可能会考虑将其添加到默认主题集中。目前无法添加新主题（至少目前如此），因为主题是在 JavaScript 中定义的，而非 CSS 级别。

## 编程连字

如果你在代码笔记中看到 `!=` 显示为 `≠` 或 `->` 显示为 `→`，那些是*字体连字*：默认等宽字体将某些字符对绘制为单个符号。底层文本不会被 Trilium 更改（与具有<a class="reference-link" href="Text/Automatic%20replacements.md">自动替换</a>的文本笔记不同），复制出来得到的仍是 `!=` 和 `->`。

可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>*→ 外观 → 字体 → 编程连字*关闭此功能。

## 虚拟键盘行为

使用虚拟键盘时，键盘建议和更正的控制方式如下：

*   对于 <a class="reference-link" href="Markdown.md">Markdown</a> 和纯文本代码笔记，自动更正为**开启**，自动大写也为开启。
*   对于所有其他代码笔记，自动更正为关闭，以避免输入代码时出现问题。

> [!NOTE]
> 并非所有浏览器和平台都遵循此值，因此键盘建议可能会出现但不自动更正，或者浏览器可能忽略此设置而仍然自动更正。