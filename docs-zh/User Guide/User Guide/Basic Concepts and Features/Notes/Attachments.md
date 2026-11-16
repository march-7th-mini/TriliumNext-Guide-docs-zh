# 附件

Trilium 中的[笔记](../Notes.md)可以 _拥有_ 一个或多个附件，这些附件可以是图片或文件。这些附件可以在拥有它们的笔记中显示或链接。

这对于为你的[脚本](../../Scripting.md)包含依赖项特别有用。<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a>展示了如何使用附加到脚本笔记的 [chartjs](https://chartjs.org/)。

每个笔记独占其附件，这意味着附件不能从一个笔记共享或链接到另一个笔记。如果将附件链接复制到不同的笔记，附件本身会被复制，此后这些副本将独立管理。

附件（尤其是图片文件）是在笔记中嵌入视觉内容的推荐方法。重要的是要在拥有该附件的笔记文本中链接图片附件；否则，如果未被引用，它们将在可配置的超时时间后被自动删除。

## 附件类型

有两种不同类型的附件：

*   _用户内容_，表示上传的文件或图片，是笔记内容的一部分。
*   _系统附件_，由 Trilium 内部使用，可以有多种类型，包括：
    *   <a class="reference-link" href="../../Collections.md">集合</a>，用于存储视图信息，例如<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>的列信息。
    *   <a class="reference-link" href="../../Note%20Types/Text/Link%20Previews.md">链接预览</a>的图标和封面图片。
    *   某些导入器的调试信息，例如<a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>（仅当导入时启用了调试标志）。
    *   <a class="reference-link" href="../../Meeting%20transcription.md">会议转录</a>的转录文本，也会显示在笔记内容的上方。
    *   <a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>笔记的 SVG 图片（`canvas-export.svg`），以及文本笔记中每个绘图画布的 SVG 图片（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的 _绘图画布_），用于预览和共享页面。

系统附件显示在附件列表的末尾，位于一个专门的区域（_由 Trilium 生成_）。

## 上传附件

<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中的 <span class="tn-icon bx bx-paperclip"></span>_附件_ 项会打开笔记的附件列表。

*   要将文件作为附件上传，请按列表顶部的 _上传附件_ 并选择一个或多个文件。
*   或者，从文件资源管理器中拖动一个或多个文件，并将它们放到列表的任意位置。如果在<a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _媒体_ 中启用了 _自动图片压缩_，图片将被压缩。

## 从文本笔记附加文件

要将文件附加到<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记并将其嵌入到内容中，请按<a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a>中的 <span class="tn-icon cke cke-paper-clip"></span>_附加文件_ 按钮，选择 _附加并嵌入文件_ 并选择一个或多个文件（参见下方的 _嵌入附件_）。同一菜单还提供 _图片_，用于插入图片（参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>），以及 _将文件附加为链接_，用于以链接方式附加文件。这两个文件操作也可在<a class="reference-link" href="../../Note%20Types/Text/Slash%20Commands.md">斜杠命令</a>中以 _将文件附加为链接_ 和 _附加并嵌入文件_ 的形式使用。在手机上，该菜单还提供 _相机_（参见<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a>）。

当文件作为链接附加时：

*   每个文件都会成为笔记的一个附件，并在光标处插入指向它的链接。多个文件会产生多个链接，以空格分隔。
*   在文件上传期间，其链接显示文件名，并有一个提示显示进度。
*   图片以链接而非图片的形式出现，并且完全按原样附加，不会被压缩。要在文本中显示图片，请改用同一菜单中的 _图片_（参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>）。

从文件资源管理器将非图片文件拖动到文本上也会附加该文件并插入指向它的链接。

## 对附件链接进行操作

右键单击指向附件的链接会显示打开它的方式，随后是对附件的操作：在外部打开、下载、上传新版本、重命名或删除，以及将其转换为笔记。在正在编辑的文本笔记中，相同的条目位于链接弹出窗口的 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单中，右键单击链接即可打开该弹出窗口。该弹出窗口还有一个 <span class="tn-icon cke cke-trilium-download"></span> _下载_ 按钮。

链接会跟随其附件的变化：重命名附件会更新它们显示的标题，删除附件会将其从当时打开以供编辑的文本笔记中移除。将附件转换为笔记会将其链接变为指向新笔记的链接。

## 嵌入附件

附件可以在文本中显示而不是链接，就像<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>显示笔记的方式一样：图片会被显示，PDF、视频或文档会被预览，代码或文本文件会以语法高亮显示，而诸如 `.md` 文件之类的 Markdown 文件会以渲染形式显示。嵌入的代码文件也可以就地编辑（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的 _就地编辑包含内容_），嵌入的 Markdown 文件会显示其源代码、渲染结果或两者，就像包含的 Markdown 笔记一样（参见其中的 _包含的 Markdown_）。

*   要附加文件并立即嵌入它们，请按 <span class="tn-icon cke cke-paper-clip"></span>_附加文件_ 按钮并选择 _附加并嵌入文件_。每个文件都会获得自己的嵌入，在文件上传期间显示文件名。
*   要嵌入已经链接的附件，请在正在编辑的文本笔记中右键单击指向它的链接，然后选择 _将链接转换为嵌入_，该选项位于菜单末尾附近。
*   绘图画布是通过 <span class="tn-icon cke cke-plus"></span>_插入_ 菜单中的 <span class="tn-icon bx bx-pen"></span>_绘图画布_ 插入的，它是一个 `Canvas.excalidraw` 附件的嵌入，可以在其中就地绘制。附加的 Excalidraw 文件（`.excalidraw`）也会作为绘图画布嵌入（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的 _绘图画布_）。
*   嵌入会获得适合该附件的框尺寸，就像新建的包含笔记一样（参见其中的 _框尺寸_）。要更改其尺寸，请选择嵌入并使用其工具栏中的框尺寸菜单，或使用其 <span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_ 菜单中的 _尺寸_ 子菜单。_可调整大小_ 的嵌入也可以通过拖动其手柄来调整大小，_可展开_ 的嵌入可以在高度上调整（参见其中的 _调整大小_）。_可调整大小_ 的嵌入可以从其菜单的 _位置_ 子菜单中放置在笔记的左侧或右侧，文本可以在其旁边流动或不流动（参见其中的 _定位_）。
*   嵌入可以像包含的笔记一样拥有说明文字（参见其中的 _说明文字_）。
*   要仅显示附件，请关闭嵌入的 <span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_ 菜单中的 _显示标题_，就像包含的笔记一样（参见其中的 _标题_）。
*   要在新标签页中打开附件，请按嵌入标题末尾的 <span class="tn-icon bx bx-link-external"></span>（_在新标签页中打开_）按钮。
*   尺寸为 _紧凑_ 的嵌入仅以单行显示附件的标题及其大小，无论附件是什么：绘图画布或视频在那里不显示其任何内容。其按钮为 <span class="tn-icon bx bx-file-find"></span>_在外部打开_ 和 <span class="tn-icon bx bx-download"></span>_下载_。_紧凑_ 尺寸的音频文件则是一行播放器控件，在打开 _显示标题_ 之前不显示其标题。
*   要在整个屏幕上显示尺寸为 _可调整大小_ 或 _完整_ 的嵌入，请按其标题末尾的 <span class="tn-icon bx bx-fullscreen"></span>（_全屏_）按钮。要返回，请按右上角的 <span class="tn-icon bx bx-exit"></span>（_退出全屏_），或按 <kbd>Esc</kbd>。
*   要将嵌入重新转换为链接，请在右键单击嵌入的标题行或按其 <span class="tn-icon bx bx-dots-vertical-rounded"></span>_更多操作_ 按钮所打开的菜单中选择 _转换为链接_。它位于最后一组，在 <span class="tn-icon bx bx-trash"></span>_删除块_（从笔记中移除嵌入）和 <span class="tn-icon bx bx-trash"></span>_删除附件..._（删除附件本身）之后。紧随其后的是 <span class="tn-icon bx bx-note"></span>_将附件转换为笔记..._。

嵌入会像链接一样跟随其附件。将附件转换为笔记会将嵌入变为包含的笔记。在[共享笔记](../../Advanced%20Usage/Sharing.md)中，嵌入的图片会连同其说明文字一起显示，绘图画布显示为绘图的图片，视频或音频文件在浏览器的播放器中显示，而任何其他附件，或 _紧凑_ 嵌入中的图片，都会显示为可下载的链接。

## 将笔记转换为附件

<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记可以轻松转换为父笔记的附件。

操作方法：

*   对于单个笔记，请从<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中按上下文菜单并选择 _转换为附件_。
*   对于多个笔记，请在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中选择给定的笔记，右键单击 → 高级 → _转换为附件…_。

## 附件预览

附件与<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记类型共享相同的图片、视频、PDF 等内容预览。Markdown 附件会以渲染形式预览，就像<a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a>笔记一样。