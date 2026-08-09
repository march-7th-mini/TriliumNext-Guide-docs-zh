# 笔记收件箱

收件箱是快速捕获笔记的默认位置。当创建笔记时未先选择位置，它就会放入收件箱。这样可以轻松快速捕获笔记，并在之后进行分类整理。

## 收件箱的使用位置

*   <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中的_新建笔记_按钮。
*   全局_创建笔记到收件箱_快捷键（默认为 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>）。
*   [托盘图标菜单](../../Installation%20%26%20Setup/Desktop%20Installation/Tray%20icon%20%26%20automatic%20startup.md)中的_新建笔记_操作。
*   <a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">Web Clipper</a> 扩展。

## 设置笔记收件箱

要创建笔记收件箱，请为其应用 `#inbox` [标签](../../Advanced%20Usage/Attributes/Labels.md)。

只有一个笔记应带有此标签。如果有多个笔记，应用程序将只使用其中一个。

> [!NOTE]
> 如果没有收件箱笔记，Trilium 将回退使用今天的[日记笔记](../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md)。

## 工作区收件箱

每个[工作区](../Navigation/Workspaces.md)都可以有自己的收件箱，通过 `#workspaceInbox` 标签设置。

当在工作区中提升（hoisted）状态下创建新笔记时，位置按以下顺序确定：

*   该工作区中带有 `#workspaceInbox` 标签的笔记。
*   该工作区中带有 `#inbox` 标签的笔记。
*   工作区根笔记本身。