# 大纲标签页

大纲标签页出现在<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>中，显示当前笔记的标题和高亮内容。

## 目录

目录显示当前笔记中的标题/标题，并支持轻松导航。

支持以下笔记类型：

*   <a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>
*   <a class="reference-link" href="../../../Note%20Types/Markdown.md">Markdown</a>
*   <a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a>
*   <a class="reference-link" href="../../../AI.md">AI</a> 对话笔记
*   应用内文档的页面

<figure class="image image-style-align-right image_resized" style="width:47%;"><img style="aspect-ratio:556/205;" src="1_Outline tab_image.png" width="556" height="205"></figure>

### 交互

*   点击标题会将文档滚动到该标题的位置。
*   按下关闭按钮将关闭目录，但可以从<a class="reference-link" href="../Floating%20buttons.md">浮动按钮</a>部分重新显示。

### 配置

> [!NOTE]
> 本节仅适用于旧布局，<a class="reference-link" href="../New%20Layout.md">新布局</a>无论标题数量多少都会显示目录。

*   要全局更改此选项，请前往<a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a>选项，找到 _目录_ 部分，并配置当前笔记中需要存在的最小标题数量，以便显示目录：
    *   要始终隐藏，请将该值设置为一个非常大的数字（例如 10000）。
    *   要始终显示（只要至少有一个标题），请将该值设置为 1。
*   使用<a class="reference-link" href="../../../Advanced%20Usage/Attributes.md">属性</a>为特定笔记配置目录：
    *   `#toc=show` 将显示该笔记的目录，无论全局设置如何。
    *   同样，`#toc=hide` 将始终隐藏该笔记的目录。

## 高亮

<figure class="image image-style-align-right image_resized" style="width:46.04%;"><img style="aspect-ratio:489/240;" src="Outline tab_image.png" width="489" height="240"></figure>

与目录类似，但此功能不是列出标题，而是列出文本笔记中的高亮文本，并支持轻松导航到这些文本。

与支持多种笔记类型的目录不同，高亮功能特定于<a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>笔记。

高亮文本定义为：

*   粗体文本。
*   斜体文本。
*   带下划线的文本。
*   设置了前景色的文本。
*   设置了背景色/高亮的文本。

### 交互

*   点击高亮文本会将文档滚动到其位置。
*   仅限旧布局：按下关闭按钮将关闭高亮列表，但可以从<a class="reference-link" href="../Floating%20buttons.md">浮动按钮</a>部分重新显示。

### 配置

*   在全局范围内，可以切换显示每个类别的高亮文本（如上定义）
    *   对于新布局，按下该部分右上角的齿轮按钮将显示一个菜单，用于切换高亮类别。
    *   或者，可以通过前往<a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a>设置并查找 _高亮列表_ 部分来更改它们。
*   仅限旧布局：要抑制特定笔记的高亮文本显示，请使用<a class="reference-link" href="../../../Advanced%20Usage/Attributes.md">属性</a>添加 `#hideHighlightWidget` 标签。

## PDF 特定大纲

当在 Trilium 中打开<a class="reference-link" href="../../../Note%20Types/File/PDFs.md">PDF</a>时，<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>会增强 PDF 特定的导航功能，具有以下特性：

*   目录/大纲
    *   所有标题和“书签”将按层级显示。
    *   当前页面上的标题也会被高亮显示（请注意，根据同一页面上标题的数量，可能会有轻微偏移）。
    *   点击标题将跳转到 PDF 中的相应位置。
*   页面
    *   所有页面的预览，带有小缩略图。
    *   点击页面将自动导航到该页面。
*   注释
    *   高亮和评论注释在此列出。
    *   对于旧布局，此功能不直接可用，但 PDF 工具栏中直接有一个评论列表。
*   附件
    *   如果 PDF 有自己的附件（不要与 Trilium 的<a class="reference-link" href="../../Notes/Attachments.md">附件</a>混淆），它们将显示在列表中。
    *   会显示一些信息，例如附件的名称和大小。
    *   可以通过点击下载按钮下载附件。
*   图层
    *   一个不太常见的功能，如果 PDF 具有可切换的图层，这些图层将在此处的列表中显示。
    *   可以切换每个单独图层的可见性。