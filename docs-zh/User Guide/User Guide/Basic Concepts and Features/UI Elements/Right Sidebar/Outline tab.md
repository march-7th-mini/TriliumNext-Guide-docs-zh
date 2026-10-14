# 大纲标签页
大纲标签页显示在<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>中，显示当前笔记的标题和突出显示内容。

## 目录

目录显示当前笔记中的标题/标题，并允许轻松导航。

支持以下笔记类型：

*   <a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>
*   <a class="reference-link" href="../../../Note%20Types/Markdown.md">Markdown</a>
*   <a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a>
*   <a class="reference-link" href="../../../AI.md">AI</a> 对话笔记
*   应用内文档的页面

<figure class="image image-style-align-right image_resized" style="width:47%;"><img style="aspect-ratio:556/205;" src="1_Outline tab_image.png" width="556" height="205"></figure>

### 交互

*   点击标题会将文档滚动到该标题的位置。
*   当文档滚动时，正在阅读的标题会高亮显示，列表会滚动以使其保持在视野中。如果该标题隐藏在折叠的部分中，则会高亮显示折叠的标题。
*   嵌套项可以通过按相应的 <span class="tn-icon bx bx-chevron-down"></span> 按钮来折叠。

## 突出显示

<figure class="image image-style-align-right image_resized" style="width:46.04%;"><img style="aspect-ratio:489/240;" src="Outline tab_image.png" width="489" height="240"></figure>

与目录类似，但此功能不是列出标题，而是列出文本笔记中突出显示的文本，并允许轻松导航到它们。

与支持多种笔记类型的目录不同，突出显示特定于<a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>笔记。

突出显示的文本定义为：

*   粗体文本。
*   斜体文本。
*   带下划线的文本。
*   设置了前景色的文本。
*   设置了背景色/高亮的文本。

### 交互

*   点击突出显示的文本会将文档滚动到其位置。

### 配置

*   全局范围内，可以切换每个突出显示文本类别（如上定义）的显示
    *   按该部分右上角的齿轮按钮将显示一个菜单，用于在突出显示类别之间切换。
    *   或者，可以通过转到<a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a>设置并查找 _突出显示列表_ 部分来更改它们。

## PDF 专用大纲

当在 Trilium 中打开<a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a>时，<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>会增加 PDF 专用导航，具有以下功能：

*   目录/大纲
    *   所有标题和“书签”将以层级方式显示。
    *   当前页面上的标题也会高亮显示（请注意，根据同一页面上有多少标题，它可能会略有偏移）。
    *   点击标题将跳转到 PDF 中的相应位置。
*   页面
    *   所有页面的预览，带有小缩略图。
    *   点击页面将自动导航到该页面。
    *   右键单击页面并选择 _复制引用_ 会复制一个在该页面打开 PDF 的链接。
*   注释
    *   高亮和评论注释列在此处。
    *   右键单击注释并选择 _复制引用_ 会复制一个在该注释处打开 PDF 的链接。
*   附件
    *   如果 PDF 有自己的附件（不要与 Trilium 的<a class="reference-link" href="../../Notes/Attachments.md">附件</a>混淆），它们将显示在列表中。
    *   显示一些信息，例如附件的名称和大小。
    *   可以通过点击下载按钮来下载附件。
*   图层
    *   一个不太常见的功能，如果 PDF 有可切换的图层，这些图层将在此处的列表中显示。
    *   可以切换每个单独图层的可见性。