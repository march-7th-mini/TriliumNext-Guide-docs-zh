# 笔记
笔记是 Trilium 中的核心实体。笔记的主要属性是[标题](Notes/Title.md)和内容。

### 笔记类型

主要的笔记类型是一种称为<a class="reference-link" href="../Note%20Types/Text.md">文本</a>的富文本笔记类型。对于图表和绘图，有<a class="reference-link" href="../Note%20Types/Canvas.md">画布</a>和<a class="reference-link" href="../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>。

还有更复杂的笔记类型，如<a class="reference-link" href="../Note%20Types/Saved%20Search.md">保存的搜索</a>、<a class="reference-link" href="../Note%20Types/Render%20Note.md">渲染笔记</a>，它们通常与<a class="reference-link" href="../Scripting.md">脚本</a>配合使用。

在 Trilium 中没有特定的“文件夹”笔记类型。任何笔记都可以有子笔记，因此都可以作为文件夹。要创建一个只显示其子笔记的笔记（类似于其他应用程序中的文件夹），请使用<a class="reference-link" href="../Collections/Grid%20View.md">网格视图</a>或<a class="reference-link" href="../Collections/List%20View.md">列表视图</a>集合。另请参阅<a class="reference-link" href="../FAQ.md">常见问题</a>。

### 根笔记

有一个特殊的笔记称为“根笔记”，它是笔记树的根。所有其他笔记都放置在它下面的结构中。

### 树结构

重要的是，笔记本身不携带其在笔记树中位置的信息。详情请参阅<a class="reference-link" href="Notes/Cloning%20Notes.md">克隆笔记</a>。

笔记的树结构可以类似于文件系统——但与此相比，Trilium 中的笔记可以同时充当文件和目录——这意味着笔记既可以有自己的内容，也可以有子笔记。“叶子笔记”是没有任何子笔记的笔记。

### 删除/恢复笔记

当你在 Trilium 中删除一个笔记时，实际上只是将其标记为删除（软删除）——实际的内容、标题、属性等并未被删除，只是被隐藏了。

在（默认）7 天内，可以恢复这些软删除的笔记——打开<a class="reference-link" href="UI%20Elements/Recent%20Changes.md">最近更改</a>对话框，你将看到所有已修改笔记的列表，包括已删除的笔记。可恢复的笔记有一个链接可供操作。这类似于 Windows 等系统中已知的“回收站”功能。

点击恢复将恢复笔记、其内容和属性——笔记应该与删除前完全一样。此操作还将恢复在同一次操作中被删除的子笔记。

要能够恢复一个笔记，已删除笔记的父笔记必须未被删除（否则就没有地方可以恢复它）。当你连续删除多个笔记时，这可能会成为问题——解决方法是按照删除的相反顺序进行恢复。

在 7 天（可配置）之后，笔记将被“擦除”——其标题、内容、修订版本和属性将被擦除，并且将无法再恢复它们（除非你恢复<a class="reference-link" href="../Installation%20%26%20Setup/Backup.md">备份</a>）。

## 另请参阅

*   <a class="reference-link" href="Notes/Read-Only%20Notes.md">只读笔记</a>