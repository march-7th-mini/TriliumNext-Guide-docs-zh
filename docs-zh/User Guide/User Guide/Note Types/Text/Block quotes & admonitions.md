# 块引用与警示框
## 块引用

顾名思义，块引用可用于引用一个或多个段落。

要创建块引用，请按 <a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a> 中的 <span class="tn-icon cke cke-quote"></span>。也可以输入 <kbd>&gt;</kbd>，后跟一个空格来创建（但仅当光标位于行首时）。

在引用块内部，可以插入其他块级项目，例如表格、图片，甚至其他块引用或警示框。

## 警示框

警示框是一种向读者突出显示信息的方式。它的其他名称包括 _call-outs_ 和 _info/warning/alert boxes_。

<figure class="image image-style-align-center"><img style="aspect-ratio:959/547;" src="Block quotes &amp; admonitions_image.png" width="959" height="547"></figure>

从功能角度来看，警示框的行为与块引用非常相似，只是样式不同。这包括在其中插入其他元素的能力，例如标题、表格、图片等。

### 插入新警示框

在 <a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a> 中，点击 <span class="tn-icon cke cke-trilium-admonition"></span> _警示框_ 按钮以插入上次选择的类型，或打开其旁边的箭头以选择类型：_Note_、_Tip_、_Important_、_Caution_ 或 _Warning_。

也可以直接输入以下内容来插入警示框：

*   `!!! note`
*   `!!! tip`
*   `!!! important`
*   `!!! caution`
*   `!!! warning`

除此之外，还可以输入 `!!!` 后跟任意文本，此时将出现默认的警示框类型（note），其中包含输入的文本。

### 交互

从设计上，警示框的行为与块引用非常相似。

*   选中文本并按下警示框按钮，会将文本转换为警示框。
*   如果选中多个警示框，按下警示框按钮会自动将它们合并为一个。

在警示框内部：

*   当警示框为空时按下 <kbd>Backspace</kbd> 会将其移除。
*   按下 <kbd>Enter</kbd> 会开始新段落。按两次会退出警示框。
*   可以在警示框内插入标题和其他块级内容，包括表格。

### 警示框的类型

目前有五种类型的警示框：_Note_、_Tip_、_Important_、_Caution_、_Warning_。

这些类型受 GitHub 对该功能支持的启发，目前没有调整它们或允许用户自定义的计划。

### Markdown 支持

参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>。