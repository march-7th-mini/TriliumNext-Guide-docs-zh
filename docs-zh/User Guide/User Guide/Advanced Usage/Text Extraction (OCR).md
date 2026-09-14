# 文本提取（OCR）
光学字符识别是从图像或 PDF 中提取文本的过程。

## 内置支持

自 v0.103.0 起，Trilium 内置支持 OCR。提取出的文本可以：

*   与<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>集成，以便根据文本片段快速找到图像或文件。
*   与<a class="reference-link" href="../AI.md">AI</a>功能集成，使智能体能够访问非文本笔记的内容。
*   手动访问以用于其他目的（例如复制到笔记中或发送到其他地方）。

## 支持的格式

Trilium 中的 OCR 支持以下格式：

### 图像

*   同时支持[单张图像笔记](../Note%20Types/File.md)和[文本文件中的附件](../Note%20Types/Text/Images.md)。
*   支持的格式：
    *   JPEG
    *   PNG
    *   GIF（仅限非动画）
    *   BMP
    *   WebP
*   请注意，此功能对计算机渲染的文本效果最佳，而非手写文本。
*   底层技术为 Tesseract.js。

### PDF

PDF 提取支持：

*   包含文本信息的 PDF（例如由浏览器或文字处理应用程序创建的 PDF），其中的文本会被提取。
*   扫描版 PDF，以及其他无法选中文本的 PDF（例如文本已被转换为轮廓的文档），其中的文本通过 OCR 过程提取。
*   混合 PDF，同时包含文本和带有文本内容的图像。

请注意，OCR 提取限制为每个 PDF 最多 50 页，包含文本信息（非图像形式）的页面不受此限制。

> [!NOTE]
> 使用 OCR 对扫描版 PDF 进行文本提取的功能于 v0.106.0 引入。如果某个扫描版 PDF 已被早期版本处理过，请通过 _处理 OCR_ 单独重新处理；批量处理仅处理尚未进行 OCR 的文件。

### Office 文档

将从以下文件格式中提取文本：

*   Microsoft Word 文档
*   Microsoft Excel 文档
    *   仅提取原始文本信息，不保留单元格结构。
    *   值以原始形式提取，因此搜索日期将无法正常工作。OpenDocument 替代格式实际上会提取正确格式化的值。
*   Microsoft PowerPoint 文档
*   上述格式的 OpenDocument 替代格式（文本、电子表格、演示文稿），由 LibreOffice 和 OpenOffice 等编辑器创建。
*   [富文本格式（RTF）](https://en.wikipedia.org/wiki/Rich_Text_Format)，自 v0.104.0 起。
*   [EPUB](https://en.wikipedia.org/wiki/EPUB)，自 v0.104.1 起。

## 配置和触发 OCR

可以通过转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → <a class="reference-link" href="#root/_hidden/_options/_optionsMedia">媒体</a>并查找 _文本提取（OCR）_ 部分来配置 OCR。

有三种方式可以触发 OCR：

*   通过启用 _自动处理新文件_，该选项仅处理启用该选项后创建的笔记或附件，现有文件将保持未处理状态。
*   通过按下 _开始批量处理_，将处理所有现有笔记。
*   通过手动请求对图像或文件进行文本提取，无论是否启用了自动处理。

### 最低置信度

从图像中提取文本时，存在一定程度的置信度，用于指示提取的文本是否看起来相关。

当最低置信度设置为较低的百分比时，文本提取可能会错误地解释符号和图形，导致文本乱码。

如果笔记或附件的提取文本质量低于最低置信度，则 OCR 结果将被忽略。

## 语言管理

OCR 需要了解内容的语言才能正常工作。原因是每种语言都有自己的数据需要下载，并且默认语言不支持重音符号或其他符号。

要配置 OCR 支持的语言，只需转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → <a class="reference-link" href="#root/_hidden/_options/_optionsLocalization">语言和地区</a>并调整 _内容语言_。

当未定义内容语言时，将使用用户界面 _语言_ 代替。

进行此更改后，自动处理或手动重新处理将考虑新的语言。

要为特定笔记强制以特定语言进行检测，请使用 `language` [属性](Attributes.md)，类似于[文本内容语言](../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md)。对于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>，无法手动调整语言。

> [!NOTE]
> 每种语言的训练数据并未随 Trilium 打包，因为那将需要大量可能不需要的空间。因此，训练数据将通过 [Tesseract.js](https://github.com/naptha/tesseract.js/) 自动下载。
> 
> 下载的训练数据位于<a class="reference-link" href="../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>中的 `ocr-cache` 目录下。

## 查看单个笔记的提取内容

要访问笔记的提取内容：

*   对于<a class="reference-link" href="../Note%20Types/File.md">文件</a>笔记，转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a> → _高级_ → _查看 OCR 文本_。
*   对于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>（例如<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记中的<a class="reference-link" href="../Note%20Types/Text/Images.md">图像</a>），双击附件查看详情，按左侧的 \[…\] 按钮并选择 _查看提取的文本（OCR）_。

此部分允许：

*   查看提取的文本，如有需要可以复制到其他地方，或仅用于检查提取质量。
*   如果笔记尚未被提取，按下 _处理 OCR_ 将在后台进行处理。如果提取置信度低于最低置信度，将会有通知。
*   同样，如果在设置中更改了最低置信度，可以再次按下 _处理 OCR_ 按钮以重新提取文本。