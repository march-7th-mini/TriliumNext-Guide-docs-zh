# 附件
Trilium 中的[笔记](../Notes.md)可以_拥有_一个或多个附件，附件可以是图片或文件。这些附件可以在拥有它们的笔记中显示或链接。

这对于包含[脚本](../../Scripting.md)的依赖项特别有用。<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a>展示了如何使用 [chartjs](https://chartjs.org/)，它被附加到脚本笔记中。

每个笔记独占其附件，这意味着附件不能从一个笔记共享或链接到另一个笔记。如果附件链接被复制到不同的笔记，附件本身会被复制，副本之后将独立管理。

附件，尤其是图片文件，是在笔记中嵌入视觉内容的推荐方法。重要的是要在拥有该附件的笔记正文中链接图片附件；否则，如果未被引用，它们将在可配置的超时时间后被自动删除。

## 附件的类型

有两种不同类型的附件：

*   _用户内容_，表示上传的文件或图片，是笔记内容的一部分。
*   _系统附件_，由 Trilium 内部使用，可以有多种类型，包括：
    *   <a class="reference-link" href="../../Collections.md">集合</a>用于存储视图相关信息，例如<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>的列信息。
    *   <a class="reference-link" href="../../Note%20Types/Text/Link%20Previews.md">链接预览</a>的图标和封面图片。
    *   某些导入器的调试信息，例如 <a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>（仅在导入时启用了调试标志的情况下）。

系统附件显示在附件列表的末尾，位于一个专门的区域（_由 Trilium 生成_）。

## 从文本笔记附加文件

要将文件附加到<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记并在其内容中链接它们，请按<a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a>中的 <span class="tn-icon cke cke-paper-clip"></span> _附加文件_ 按钮，它位于 <span class="tn-icon cke cke-image-upload"></span> 图片上传按钮旁边，然后选择一个或多个文件。按钮旁边的箭头列出了相同的操作，即 _以链接形式附加文件_，后面是 _附加并嵌入文件_，后者会改为嵌入文件（见下文）。这两个操作也可以在<a class="reference-link" href="../../Note%20Types/Text/Slash%20Commands.md">斜杠命令</a>中以 _以链接形式附加文件_ 和 _附加并嵌入文件_ 的形式使用。

*   每个文件都会成为笔记的附件，并且会在光标处插入指向它的链接。多个文件会产生多个链接，以空格分隔。
*   在文件上传期间，其链接会显示文件名，并有一个提示显示进度。
*   图片会以链接而非图片的形式出现，并且会按原样附加，不会被压缩。要在文本中显示图片，请改用图片上传按钮（参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>）。

从文件资源管理器中拖动一个非图片文件到文本上，也会将其附加并插入指向它的链接。

## 对附件链接进行操作

右键单击指向附件的链接会显示打开它的方式，随后是针对该附件的操作：在外部打开它、下载它、上传新版本、重命名或删除它，以及将其转换为笔记。

链接会跟随其附件的变化：重命名附件会更新它们显示的标题，删除附件会将它们从当时打开以供编辑的文本笔记中移除。将附件转换为笔记会将其链接变为指向新笔记的链接。

## 嵌入附件

附件可以在文本中显示而不是被链接，就像<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>显示笔记的方式一样：图片会被显示，PDF、视频或文档会被预览。

*   要附加文件并立即嵌入它们，请从 <span class="tn-icon cke cke-paper-clip"></span> _附加文件_ 按钮旁边的箭头中选择 _附加并嵌入文件_。每个文件都会有自己的嵌入，在文件上传期间会显示文件名。
*   要嵌入一个已经链接的附件，请在正在编辑的文本笔记中右键单击指向它的链接，然后选择菜单末尾的 _将链接转换为嵌入_。
*   通过 <span class="tn-icon cke cke-plus"></span> _插入_ 菜单中的 <span class="tn-icon bx bx-pen"></span> _绘图画布_ 插入的绘图画布，是一个 `Canvas.excalidraw` 附件的嵌入，可以直接在其上绘图（参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>中的 _绘图画布_）。
*   嵌入会获得适合该附件的框大小，就像新建的包含笔记一样（参见那里的 _框大小_）。要更改其大小，请选择该嵌入并使用其工具栏中的框大小菜单，或使用其 <span class="tn-icon bx bx-dots-vertical-rounded"></span> _更多操作_ 菜单中的 _大小_ 子菜单。_小_、_中_ 或 _可展开_ 的嵌入也可以通过拖动其手柄来调整大小（参见那里的 _调整大小_）。
*   嵌入可以像包含笔记一样拥有标题（参见那里的 _标题_）。
*   要仅显示附件，请选择该嵌入并按工具栏中的 <span class="tn-icon bx bx-window-alt"></span> _显示标题_ 按钮，就像包含笔记一样（参见那里的 _标题_）。
*   要在新标签页中打开附件，请按嵌入标题末尾的 <span class="tn-icon bx bx-link-external"></span> _在新标签页中打开_ 按钮。
*   _极小_ 大小的嵌入只会在单行中显示附件的标题及其大小。其按钮为 <span class="tn-icon bx bx-file-find"></span> _在外部打开_ 和 <span class="tn-icon bx bx-download"></span> _下载_。
*   要在整个屏幕上显示 _中_ 或 _全_ 大小的嵌入，请按其标题末尾的 <span class="tn-icon bx bx-fullscreen"></span> _全屏_ 按钮。要返回，请按右上角的 <span class="tn-icon bx bx-exit"></span> _退出全屏_，或按 <kbd>Esc</kbd>。
*   要将嵌入重新变回链接，请选择它并按工具栏中的 <span class="tn-icon cke cke-link"></span> _转换为链接_ 按钮。_转换为链接_ 也会结束通过右键单击嵌入的标题行或按其 <span class="tn-icon bx bx-dots-vertical-rounded"></span> _更多操作_ 按钮所打开的菜单。

嵌入会像链接一样跟随其附件。将附件转换为笔记会将嵌入变为包含笔记。在[共享笔记](../../Advanced%20Usage/Sharing.md)中，嵌入的图片会与其标题一起显示，而任何其他附件，或 _极小_ 嵌入中的图片，都会显示为可下载它的链接。

## 将笔记转换为附件

<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记可以轻松转换为父笔记的附件。

为此：

*   对于单个笔记，请从<a class="reference-link" href="../UI%20Elements/Note%20buttons.md">笔记按钮</a>中按上下文菜单，然后选择 _转换为附件_。
*   对于多个笔记，请在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中选择给定的笔记，右键单击 → 高级 → 转换为附件。

## 附件预览

附件与<a class="reference-link" href="../../Note%20Types/File.md">文件</a>笔记类型共享相同的图片、视频、PDF 等内容预览。