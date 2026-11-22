# Office 文档
自 v0.105.0 起，存储在 Trilium 中的 Office 文档会显示其内容的行内预览，无需下载它们或在外部应用程序中打开它们。

## 支持的格式

*   Microsoft Office 格式：Word（`.docx`）、Excel（`.xlsx`）和 PowerPoint（`.pptx`）。
*   上述格式的 OpenDocument 替代格式（文本、电子表格、演示文稿），由 LibreOffice 和 OpenOffice 等编辑器创建。
*   [富文本格式（RTF）](https://en.wikipedia.org/wiki/Rich_Text_Format)。
*   [EPUB](https://en.wikipedia.org/wiki/EPUB) 电子书。

> [!NOTE]
> 不支持较旧的 Microsoft Office 格式（`.doc`、`.xls`、`.ppt`）。

## 工作原理

文档在服务器上被转换为简化表示，并渲染为只读内容，类似于<a class="reference-link" href="../Text.md">文本</a>笔记。

预览通常保留：

*   标题、段落和文本对齐方式。
*   文本格式：粗体、斜体、下划线、删除线、下标/上标、文本和高亮颜色、字体和字号。
*   项目符号列表和编号列表。
*   表格，包括合并单元格和单元格背景颜色。
*   嵌入的图像。
*   链接和脚注。

为使链接在任何主题下都清晰可读，字处理器自动应用的默认超链接颜色会被忽略；作者特意指定了自定义颜色的链接则保留该颜色。

### Excel 工作簿

包含 Excel 工作簿（`.xlsx`）的文件笔记会在只读电子表格中打开，其视图与不可编辑的<a class="reference-link" href="../Spreadsheets.md">电子表格</a>笔记相同：工作表列在底部的选项卡中，无论工作簿多大，网格都可向两个方向滚动。与电子表格笔记一样，无论<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Content%20width.md">内容宽度</a>如何，它始终占据窗口的整个宽度。

作为<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>存储的工作簿，在单独打开该附件后也会以相同方式打开。如果该文件无法作为工作簿读取，则改为显示上述简化预览。

## 链接到标题或书签

自 v0.108.0 起，链接可以指向 Word（`.docx`）或 OpenDocument 文本（`.odt`）文档的标题、EPUB 电子书的章节或小节，或 Word 或 OpenDocument 文档的书签。要从文本或 Markdown 笔记创建此类链接：

*   在 _添加链接_ 对话框中，在 _笔记_ 页面选择该文档。其标题列在 _链接标题_ 下方的 _链接到标题_ 下，其书签列在 _链接到锚点_ 下。勾选一项，然后按 <kbd>Enter</kbd> 或 _插入链接_。
*   或者，输入 `@` 并选择该文档：菜单随后会列出相同的标题和书签。

这些标题也会列在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Outline%20tab.md">大纲选项卡</a>的目录中，该目录会高亮显示正在阅读的标题。点击某个标题会将预览滚动到该处，右键点击它并选择 _复制引用_ 会复制指向它的链接。

该链接显示文档标题，后跟标题的标题，并在该标题或书签处打开预览。当找不到它时，例如文件的新版本重命名了该标题，链接会打开文档顶部。如果某个标题的标题在相邻标题中重复出现，则只能在完全相同的文件中找到它，因此一旦上传了文件的新版本，指向它的链接会打开文档顶部。

要链接到作为附件存储的文档的标题，请编辑指向该附件的链接：对话框会列出该附件的标题。

这些标题是预览中的标题。在 Word 文档中，它们是使用 Word 内置标题样式和 _标题_ 样式的段落。某些本地化版本的 Word（例如德语和法语版本）对这些样式的命名不同，它们的标题会显示为普通段落，任何链接都无法指向它们。编辑器自行创建的书签（例如目录的书签）不会被列出。

在 EPUB 电子书中，标题是书籍自身目录的条目，正如电子书阅读器所列出的那样。书籍中无法显示的部分（例如受 DRM 保护的章节）的条目不会被列出。

> [!NOTE]
> Trilium 将每个文档的标题保存在笔记的一个名为 `toc-cache.json` 的附件中，每当文件更改时都会重新读取。笔记的修订版本、导出和副本不会包含它。

## 限制

*   预览是只读的。要编辑文档，请下载它或在外部应用程序中打开它；笔记的内容不受预览影响。或者将其复制并粘贴到文本笔记中。
*   预览是简化渲染：复杂布局（分栏、文本框、页眉和页脚）、图表以及表格边框的精确样式不会被重现。
*   大于 20 MB 的文档不会被预览，以保持服务器响应。会显示一条消息说明文档过大无法预览，通常的下载和打开操作仍然可用。
*   如果文档无法转换，则会改为显示一条提示，该文件仍然可以下载或在外部打开。

## 与其他功能的关系

*   当 Office 文档显示在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>中，或通过<a class="reference-link" href="../Text/Include%20Note.md">包含笔记</a>嵌入到文本笔记中时，以及对于作为<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>存储的 Office 文档，都会使用相同的预览。对于电子表格，笔记列表和附件列表仅显示其第一个工作表的左上角（20 行 × 15 列）；打开笔记或附件即可在只读电子表格中查看全部内容。
*   与预览无关，Office 文档的文本内容也会在后台提取，以便可以通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>使用<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>找到它。
*   `.csv` 和 `.xlsx` 文件可以通过[导入](../../Basic%20Concepts%20and%20Features/Import%20%26%20Export.md)功能转换为<a class="reference-link" href="../Spreadsheets.md">电子表格</a>。