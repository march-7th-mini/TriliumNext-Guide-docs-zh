# 文本提取（OCR）

光学字符识别是从图像或PDF中提取文本的过程。

## 内置支持

自 v0.103.0 版本起，Trilium 内置了 OCR 支持。提取的文本可以：

*   与<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>集成，以便根据文本片段快速找到图像或文件。
*   与<a class="reference-link" href="../AI.md">AI</a>功能集成，允许智能体访问非文本笔记的内容。
*   手动访问以用于其他目的（例如，复制到笔记中或发送到其他地方）。

## 支持的格式

Trilium 中的 OCR 支持以下格式：

### 图像

*   支持[单个图像笔记](../Note%20Types/File.md)和[文本文件中的附件](../Note%20Types/Text/Images.md)。
*   支持的格式：
    *   JPEG
    *   PNG
    *   GIF（仅限非动画）
    *   BMP
    *   WebP
*   请注意，此功能最适合计算机渲染的文本，而非手写内容。
*   底层技术是 Tesseract.js。

### PDF

目前仅支持文本提取，不支持 OCR。

*   这意味着 PDF 需要包含正确的文本信息（即文本可以在 PDF 查看器中选择），而扫描文档尚不支持。
*   有计划为 PDF 集成与图像相同的基于 OCR 的识别功能，但尚未实现。

### Office 文档

将从以下文件格式中提取文本：

*   Microsoft Word 文档
*   Microsoft Excel 文档
    *   仅提取原始文本信息，不保留单元格结构。
    *   值是原始提取的，因此搜索日期将不起作用。OpenDocument 替代格式将实际提取格式正确的值。
*   Microsoft PowerPoint 文档
*   前述格式的 OpenDocument 替代格式（文本、电子表格、演示文稿），由 LibreOffice 和 OpenOffice 等编辑器创建。
*   [富文本格式 (RTF)](https://en.wikipedia.org/wiki/Rich_Text_Format)，自 v0.104.0 起。
*   [EPUB](https://en.wikipedia.org/wiki/EPUB)，自 v0.104.1 起。

## 配置和触发 OCR

可以通过转到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → <a class="reference-link" href="#root/_hidden/_options/_optionsMedia">媒体</a> 并查找 _文本提取 (OCR)_ 部分来配置 OCR。

有三种方式可以触发 OCR：

*   启用 _自动处理新文件_，这将仅处理启用该选项后创建的笔记或附件，现有文件将保持未处理状态。
*   按下 _开始批量处理_，这将处理所有现有笔记。
*   手动请求提取图像或文件的文本，无论自动处理是否启用。

### 最低置信度

从图像中提取文本时，存在一定程度的置信度，用于指示提取的文本是否看起来相关。

当最低置信度设置为较低百分比时，文本提取可能会错误地解释符号和图形，导致乱码文本。

如果笔记或附件的提取文本质量低于最低置信度，则忽略 OCR 结果。

## 语言管理

OCR 需要了解内容的语言才能正常工作。原因是每种语言都有自己的数据需要下载，并且默认语言不支持重音符号或其他符号。

要配置 OCR 支持的语言，只需转到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → <a class="reference-link" href="#root/_hidden/_options/_optionsLocalization">语言与区域</a> 并调整 _内容语言_。

当未定义内容语言时，将使用用户界面 _语言_。

进行此更改后，自动处理或手动重新处理将考虑新的语言。

要为给定笔记强制使用特定语言进行检测，请使用 `language` [属性](Attributes.md)，类似于[文本内容语言](../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md)。对于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>，无法手动调整语言。

> [!NOTE]
> 每种语言的训练数据不随 Trilium 打包，因为那将需要大量可能不需要的空间。因此，训练数据将通过 [Tesseract.js](https://github.com/naptha/tesseract.js/) 自动下载。
> 
> 下载的训练数据位于<a class="reference-link" href="../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>中的 `ocr-cache` 目录中。

## 查看单个笔记的提取内容

要访问笔记的提取内容：

*   对于<a class="reference-link" href="../Note%20Types/File.md">文件</a>笔记，转到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a> → _高级_ → _查看 OCR 文本_。
*   对于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>（例如<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记中的<a class="reference-link" href="../Note%20Types/Text/Images.md">图像</a>），双击附件查看详细信息，按左侧的 \[…\] 按钮并选择 _查看提取的文本 (OCR)_。

此部分允许：

*   查看提取的文本，如有需要可以复制到其他地方，或仅用于检查提取质量。
*   如果笔记尚未提取，按 _处理 OCR_ 将在后台处理。如果提取置信度低于最低置信度，将会有通知。
*   类似地，如果在设置中更改了最低置信度，可以再次按 _处理 OCR_ 按钮以重新提取文本。