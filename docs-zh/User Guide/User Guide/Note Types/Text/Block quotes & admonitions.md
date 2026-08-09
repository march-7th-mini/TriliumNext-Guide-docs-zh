# 块引用与警示框
## 块引用

顾名思义，块引用可用于引用一个或多个段落。

要创建块引用，请从<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中按下 <img src="Block quotes &amp; admonitions_image.png" width="15" height="12">。也可以输入 <kbd>&gt;</kbd> 后跟一个空格来创建（但仅当光标位于行首时）。

在引用块内部，可以插入其他块级元素，如表格、图片，甚至其他块引用或警示框。

## 警示框

警示框是一种向读者突出显示信息的方式。它的其他名称包括_标注框_和_信息/警告/提醒框_。

<figure class="image image-style-align-center"><img style="aspect-ratio:959/547;" src="2_Block quotes &amp; admonitions_image.png" width="959" height="547"></figure>

从功能角度来看，警示框的行为与块引用非常相似，只是样式不同。这包括能够在其中插入其他元素，如标题、表格、图片等。

### 插入新的警示框

在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中：

![](1_Block%20quotes%20&%20admonitions_image.png)

可以通过直接输入以下内容来插入警示框：

*   `!!! note`
*   `!!! tip`
*   `!!! important`
*   `!!! caution`
*   `!!! warning`

除此之外，还可以输入 `!!!` 后跟任意文本，此时将出现默认类型的警示框（note），其中包含输入的文本。

### 交互

按照设计，警示框的行为与块引用非常相似。

*   选中文本并按警示框按钮会将所选文本转换为警示框。
*   如果选中多个警示框，按警示框按钮将自动将它们合并为一个。

在警示框内部：

*   当警示框为空时按 <kbd>Backspace</kbd> 将删除该警示框。
*   按 <kbd>Enter</kbd> 将开始一个新段落。按两次将退出警示框。
*   标题和其他块级内容（包括表格）都可以插入到警示框内部。

### 警示框类型

目前有五种类型的警示框：_Note_、_Tip_、_Important_、_Caution_、_Warning_。

这些类型受 GitHub 对此功能的支持所启发，目前没有计划调整或允许用户自定义它们。

### Markdown 支持

参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>。