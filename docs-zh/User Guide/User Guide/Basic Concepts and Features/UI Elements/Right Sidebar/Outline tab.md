# 大纲标签页

大纲标签页显示在<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>中，显示当前笔记的标题和突出显示内容。

## 筛选

标签页顶部的字段会同时筛选其所有分区：目录、突出显示、看板的列、AI 对话的突出显示，以及对于 PDF 而言的页面、注释、附件和图层。没有匹配内容的分区会被隐藏。

*   单词可以按任意顺序输入；大小写和重音符号会被忽略。公式不会被搜索。
*   筛选时，目录会变为匹配标题的扁平列表，每个标题都会显示其所属的上级标题。
*   PDF 的页面按其页码进行匹配。
*   已折叠的分区保持折叠状态且不会被搜索。展开后会显示其匹配项，或显示 _无匹配项_。
*   <kbd>Enter</kbd> 跳转到第一个匹配的标题、页面、注释、突出显示或列。<kbd>Esc</kbd> 清空该字段。
*   打开另一篇笔记时，筛选条件会被清除。

## 目录

目录显示当前笔记中的标题/小标题，并允许轻松导航。

支持以下笔记类型：

*   <a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>
*   <a class="reference-link" href="../../../Note%20Types/Markdown.md">Markdown</a>
*   <a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a>，包括只读的 PDF
*   Word（`.docx`）和 OpenDocument Text（`.odt`）文档以及 EPUB 电子书，属于<a class="reference-link" href="../../../Note%20Types/File/Office%20documents.md">办公文档</a>
*   <a class="reference-link" href="../../../AI.md">AI</a> 对话笔记
*   应用内文档的页面

当 PDF、Word、OpenDocument Text 或 EPUB 文件作为[附件](../../Notes/Attachments.md)单独打开时，其目录也会显示。此类文件首次显示时，Trilium 会读取其标题，在此期间目录会显示 _正在构建目录…_。

<figure class="image image-style-align-right image_resized" style="width:47%;"><img style="aspect-ratio:556/205;" src="1_Outline tab_image.png" width="556" height="205"></figure>

### 交互

*   点击标题会将文档滚动到该标题的位置。
*   随着文档滚动，正在阅读的标题会被高亮显示，列表也会滚动以使其保持在视野中。如果该标题隐藏在已折叠的分区中，则会改为高亮显示该折叠的标题。
*   嵌套项可以通过按下相应的 <span class="tn-icon bx bx-chevron-down"></span> 按钮来折叠。
*   对于文本或 Markdown 笔记，右键点击标题会显示 _复制引用_，它会复制一个在该标题处打开笔记的链接（参见<a class="reference-link" href="../../../Note%20Types/Text/Block%20references.md">块引用</a>）。如果笔记已[共享](../../../Advanced%20Usage/Sharing.md)，_复制公开链接_ 会复制指向共享页面上该标题的链接。
*   对于 PDF、Word、OpenDocument Text 或 EPUB 文件，右键点击标题也会显示 _复制引用_，但没有 _复制公开链接_。
*   将鼠标悬停在可链接的标题上时，其末尾会显示一个 <span class="tn-icon bx bx-copy"></span> 按钮，其作用与 _复制引用_ 相同。
*   无法通过任何链接到达的条目（例如 PDF 大纲中不指向任何页面的条目，或 EPUB 目录中无法显示书中该部分的条目）会变暗且无法点击。

## 突出显示

<figure class="image image-style-align-right image_resized" style="width:46.04%;"><img style="aspect-ratio:489/240;" src="Outline tab_image.png" width="489" height="240"></figure>

与目录类似，但此功能列出的不是标题，而是文本笔记中突出显示的文本，并允许轻松导航到它们。

与支持多种笔记类型的目录不同，突出显示仅适用于<a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>笔记。

突出显示的文本定义为：

*   粗体文本。
*   斜体文本。
*   带下划线的文本。
*   设置了前景色的文本。
*   设置了背景色/高亮的文本。

### 交互

*   点击突出显示的文本会将文档滚动到其位置。
*   在文本笔记中，笔记的滚动条会用这些颜色的淡线标记每段设置了前景色或背景色的文本，当一行中有多个时并排显示。点击一条线会滚动到该文本。这些线遵循下面选择的类别，且仅在桌面布局中显示。当<a class="reference-link" href="../../Navigation/Search%20in%20note.md">在笔记中搜索</a>有结果时，滚动条仅标记这些结果，一旦搜索无结果，这些线就会恢复。
    *   要隐藏这些线，请右键点击滚动条并取消勾选 _突出显示_，或关闭<a class="reference-link" href="../Options.md">选项</a> → _文本笔记_ → _功能_ → _在滚动条上显示突出显示的文本_。该设置仅适用于当前设备。

### 配置

*   全局范围内，可以切换每类突出显示文本（如上定义）的显示
    *   按下该分区右上角的齿轮按钮会显示一个菜单，用于在突出显示类别之间切换。
    *   或者，可以通过前往<a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a>设置并查找 _突出显示列表_ 分区来更改它们。

## PDF 专用大纲

当在 Trilium 中打开 <a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a> 时，<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>会增强为 PDF 专用导航，具有以下功能：

*   目录/大纲
    *   PDF 的所有标题和"书签"会在上述目录中以层级方式显示。
    *   正在阅读的标题会被高亮显示。
    *   点击标题会跳转到 PDF 中的相应位置。
*   页面
    *   所有页面的预览，带有小缩略图。
    *   点击页面会自动导航到该页面。
    *   右键点击页面并选择 _复制引用_ 会复制一个在该页面处打开 PDF 的链接。
*   注释
    *   高亮和评论注释会列在此处。
    *   右键点击注释并选择 _复制引用_ 会复制一个在该注释处打开 PDF 的链接。
*   附件
    *   如果 PDF 有自己的附件（不要与 Trilium 的<a class="reference-link" href="../../Notes/Attachments.md">附件</a>混淆），它们会显示在列表中。
    *   会显示一些信息，例如附件的名称和大小。
    *   可以通过点击下载按钮来下载附件。
*   图层
    *   一个不太常见的功能，如果 PDF 有可切换的图层，这些图层会在此处的列表中显示。
    *   可以切换每个单独图层的可见性。