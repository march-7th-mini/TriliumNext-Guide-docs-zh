# 附件
Trilium 中的[笔记](../Notes.md)可以_拥有_一个或多个附件，这些附件可以是图片或文件。这些附件可以在拥有它们的笔记中显示或链接。

这对于包含[脚本](../../Scripting.md)的依赖项特别有用。<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a>展示了如何使用附加到脚本笔记的 [chartjs](https://chartjs.org/)。

每个笔记独占其附件，这意味着附件不能从一个笔记共享或链接到另一个笔记。如果将附件链接复制到不同的笔记，附件本身会被复制，副本此后将独立管理。

附件（尤其是图片文件）是在笔记中嵌入视觉内容的推荐方法。重要的是要在拥有该附件的笔记文本中链接图片附件；否则，如果未被引用，它们将在可配置的超时时间后被自动删除。

## 附件类型

有两种不同类型的附件：

*   _用户内容_，表示上传的文件或图片，是笔记内容的一部分。
*   _系统附件_，由 Trilium 内部使用，可以有多种类型，包括：
    *   <a class="reference-link" href="../../Collections.md">集合</a>，用于存储视图信息，例如<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>的列信息。
    *   <a class="reference-link" href="../../Note%20Types/Text/Link%20Previews.md">链接预览</a>的图标和封面图片。
    *   某些导入器的调试信息，例如<a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>（仅当导入时启用了调试标志）。
    *   <a class="reference-link" href="../../Meeting%20transcription.md">会议转录</a>的转录文本，也会显示在笔记内容上方。
    *   <a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>笔记的 SVG 图片（`canvas-export.svg`），以及文本笔记中每个绘图画布的 SVG 图片（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的_绘图画布_），用于预览和共享页面。

系统附件显示在附件列表的末尾，位于专门的区域（_由 Trilium 生成_）。

## 上传附件

<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中的<span class="tn-icon bx bx-paperclip"></span>_附件_项会打开笔记的附件列表。

*   要将文件作为附件上传，请按列表顶部的_上传附件_并选择一个或多个文件。
*   或者，从文件资源管理器中拖动一个或多个文件，并将它们放到列表上的任意位置。如果在<a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _媒体_中启用了_自动图片压缩_，图片将被压缩。

## 从文本笔记附加文件

要将文件附加到<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记并将其嵌入到其内容中，请按<a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a>中的<span class="tn-icon cke cke-paper-clip"></span>_附加文件_按钮，选择_附加并嵌入文件_并选择一个或多个文件（参见下面的_嵌入附件_）。同一菜单还提供_图片_，用于插入图片（参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>），以及_将文件附加为链接_，用于链接文件。这两个文件操作也可在<a class="reference-link" href="../../Note%20Types/Text/Slash%20Commands.md">斜杠命令</a>中作为_将文件附加为链接_和_附加并嵌入文件_使用。在手机上，菜单还提供_相机_（参见<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动前端</a>）。

当文件作为链接附加时：

*   每个文件成为笔记的附件，并在光标处插入指向它的链接。多个文件会产生多个链接，以空格分隔。
*   在文件上传期间，其链接显示文件名，并显示进度提示。
*   图片显示为链接而非图片，并且完全按原样附加，不会被压缩。要在文本中显示图片，请改用同一菜单中的_图片_（参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>）。

从文件资源管理器将非图片文件拖动到文本上也会附加它并插入指向它的链接。

## 操作附件链接

右键单击指向附件的链接会显示打开它的方式，随后是对附件的操作：在外部打开、下载、上传新版本、重命名或删除它，以及将其转换为笔记。在正在编辑的文本笔记中，相同的条目位于链接弹出窗口的<span class="tn-icon cke cke-three-vertical-dots"></span>_更多操作_菜单中，右键单击链接会打开该弹出窗口。弹出窗口还有一个<span class="tn-icon cke cke-trilium-download"></span>_下载_按钮。

链接会跟随其附件的变化：重命名它会更新它们显示的标题，删除它会从当时打开进行编辑的文本笔记中移除它们。将其转换为笔记会将其链接变为指向新笔记的链接。

## 嵌入附件

附件可以在文本中显示而不是链接，就像<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>显示笔记的方式：图片被显示，PDF、视频或文档被预览，代码或文本文件以语法高亮显示，而 Markdown 文件（如 `.md` 文件）以渲染形式显示。嵌入的代码文件也可以就地编辑（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的_就地编辑包含内容_），嵌入的 Markdown 文件会显示其源代码、渲染结果或两者，就像包含的 Markdown 笔记一样（参见其中的_包含的 Markdown_）。

*   要附加文件并直接嵌入它们，请按<span class="tn-icon cke cke-paper-clip"></span>_附加文件_按钮并选择_附加并嵌入文件_。每个文件都有自己的嵌入，在文件上传时显示文件名。
*   要嵌入已经链接的附件，请在正在编辑的文本笔记中右键单击指向它的链接，然后选择_将链接转换为嵌入_，位于菜单末尾附近。
*   绘图画布通过<span class="tn-icon cke cke-plus"></span>_插入_菜单中的<span class="tn-icon bx bx-pen"></span>_绘图画布_插入，是 `Canvas.excalidraw` 附件的嵌入，可以就地绘制。附加的 Excalidraw 文件（`.excalidraw`）也会作为绘图画布嵌入（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的_绘图画布_）。
*   嵌入会获得适合附件的框大小，就像新的包含笔记一样（参见其中的_框大小_）。要更改其大小，请选择嵌入并使用其工具栏中的框大小菜单，或其<span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_菜单的_大小_子菜单。_小_、_中_或_可展开_的嵌入也可以通过拖动其手柄来调整大小（参见其中的_调整大小_），并从其菜单的_位置_子菜单中放置在笔记的左侧或右侧，文本可以或不可以伴随其旁边（参见其中的_定位_）。
*   嵌入可以像包含笔记一样有标题（参见其中的_标题_）。
*   要仅显示附件，请关闭嵌入的<span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_菜单中的_显示标题_，就像包含笔记一样（参见其中的_标题_）。
*   要在新标签页中打开附件，请按嵌入标题末尾的<span class="tn-icon bx bx-link-external"></span>（_在新标签页中打开_）按钮。
*   _极小_大小的嵌入仅显示附件的标题及其大小，在一行中。其按钮为<span class="tn-icon bx bx-file-find"></span>_在外部打开_和<span class="tn-icon bx bx-download"></span>_下载_。
*   要在整个屏幕上显示_中_或_完整_大小的嵌入，请按其标题末尾的<span class="tn-icon bx bx-fullscreen"></span>（_全屏_）按钮。要返回，请按右上角的<span class="tn-icon bx bx-exit"></span>（_退出全屏_），或按 <kbd>Esc</kbd>。
*   要将嵌入转换回链接，请右键单击嵌入的标题行或按其<span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_按钮打开的菜单中的_转换为链接_。它位于最后一组，在<span class="tn-icon bx bx-trash"></span>_删除_（从笔记中移除嵌入）和<span class="tn-icon bx bx-trash"></span>_删除附件..._（删除附件本身）之后。<span class="tn-icon bx bx-note"></span>_将附件转换为笔记..._紧随其后。

嵌入会像链接一样跟随其附件。将附件转换为笔记会将嵌入变为包含笔记。在[共享笔记](../../Advanced%20Usage/Sharing.md)中，嵌入的图片会显示其标题，绘图画布显示为绘图的图片，而任何其他附件，或_极小_嵌入中的图片，都会显示为下载链接。

## 将笔记转换为附件

<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记可以轻松转换为父笔记的附件。

为此：

*   对于单个笔记，请按<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中的上下文菜单，然后选择_转换为附件_。
*   对于多个笔记，请在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中选择给定的笔记，右键单击 → 高级 → _转换为附件…_。

## 附件预览

附件与<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记类型共享相同的图片、视频、PDF 等内容预览。Markdown 附件以渲染形式预览，就像<a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a>笔记一样。