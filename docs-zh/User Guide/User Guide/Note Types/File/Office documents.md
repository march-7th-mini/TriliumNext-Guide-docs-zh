# Office 文档

自 v0.105.0 版本起，存储在 Trilium 中的 Office 文档会显示其内容的内联预览，无需下载或在外部应用程序中打开。

## 支持的格式

*   Microsoft Office 格式：Word (`.docx`)、Excel (`.xlsx`) 和 PowerPoint (`.pptx`)。
*   上述格式的 OpenDocument 替代格式（文本、电子表格、演示文稿），由 LibreOffice 和 OpenOffice 等编辑器创建。
*   [富文本格式 (RTF)](https://en.wikipedia.org/wiki/Rich_Text_Format)。
*   [EPUB](https://en.wikipedia.org/wiki/EPUB) 电子书。

> [!NOTE]
> 不支持较旧的 Microsoft Office 格式（`.doc`、`.xls`、`.ppt`）。

## 工作原理

文档在服务器端被转换为简化的表示形式，并渲染为只读内容，类似于<a class="reference-link" href="../Text.md">文本</a>笔记。

预览通常保留：

*   标题、段落和文本对齐方式。
*   文本格式：粗体、斜体、下划线、删除线、下标/上标、文本和突出显示颜色、字体和字号。
*   项目符号列表和编号列表。
*   表格，包括合并单元格和单元格背景颜色。
*   嵌入的图片。
*   链接和脚注。

为了确保链接在不同主题下均可读，文字处理软件自动应用的默认超链接颜色会被忽略；作者特意赋予自定义颜色的链接则保留其颜色。

## 限制

*   预览是只读的。要编辑文档，请下载它或在外部应用程序中打开；笔记的内容不受预览影响。或者将其复制并粘贴到文本笔记中。
*   预览是简化渲染：复杂布局（分栏、文本框、页眉和页脚）、图表以及表格边框的精确样式不会被重现。
*   超过 20 MB 的文档不会预览，以保持服务器响应速度。常规的下载和打开操作仍然可用。
*   如果文档无法转换，则会显示一条提示信息，文件仍然可以下载或在外部打开。

## 与其他功能的关系

*   当 Office 文档显示在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>中，或通过<a class="reference-link" href="../Text/Include%20Note.md">包含笔记</a>嵌入到文本笔记中时，会使用相同的预览；存储为<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>的 Office 文档也是如此。
*   与预览无关，Office 文档的文本内容也会在后台被提取，以便可以通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取 (OCR)</a> 使用<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>功能找到。
*   `.csv` 和 `.xlsx` 文件可以通过[导入](../../Basic%20Concepts%20and%20Features/Import%20%26%20Export.md)功能转换为<a class="reference-link" href="../Spreadsheets.md">电子表格</a>。