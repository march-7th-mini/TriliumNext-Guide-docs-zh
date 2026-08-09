# 附件

Trilium 中的[笔记](../Notes.md)可以_拥有_一个或多个附件，这些附件可以是图片或文件。这些附件可以在拥有它们的笔记中显示或链接。

这对于包含[脚本](../../Scripting.md)的依赖项特别有用。<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Weight%20Tracker.md">Weight Tracker</a> 展示了如何使用附加到脚本笔记上的 [chartjs](https://chartjs.org/)。

每个笔记独占其附件，这意味着附件不能从一个笔记共享或链接到另一个笔记。如果附件链接被复制到不同的笔记，附件本身会被复制，并且副本此后独立管理。

附件，尤其是图片文件，是在笔记中嵌入视觉内容的推荐方法。重要的是，在拥有附件的笔记文本中链接图片附件；否则，如果在一定时间后未被引用，它们将被自动删除（该超时时间可配置）。

## 附件类型

有两种不同类型的附件：

*   _用户内容_，表示上传的、作为笔记内容一部分的文件或图片。
*   _系统附件_，由 Trilium 内部使用，可以有多种类型，包括：
    *   <a class="reference-link" href="../../Collections.md">集合</a> 用于存储视图信息，例如 <a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a> 的列信息。
    *   <a class="reference-link" href="../../Note%20Types/Text/Link%20Previews.md">链接预览</a> 的图标和封面图片。
    *   某些导入器（如 <a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>）的调试信息（仅在导入时启用了调试标志的情况下）。

系统附件显示在附件列表的末尾，位于一个专门的区域（_由 Trilium 生成_）。

## 将笔记转换为附件

<a class="reference-link" href="../../Note%20Types/File.md">文件</a> 笔记可以轻松转换为父笔记的附件。

操作方法如下：

*   对于单个笔记，从 <a class="reference-link" href="../UI%20Elements/Note%20buttons.md">笔记按钮</a> 打开上下文菜单，然后选择 _转换为附件_。
*   对于多个笔记，在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中选择相应的笔记，右键单击 → 高级 → 转换为附件。

## 附件预览

附件与 <a class="reference-link" href="../../Note%20Types/File.md">文件</a> 笔记类型共享相同的图片、视频、PDF 等内容预览。