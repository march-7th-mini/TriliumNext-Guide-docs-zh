# 笔记收件箱
收件箱是快速捕获笔记的默认目的地。当创建笔记时未先选择位置，它就会落入收件箱。这使得快速捕获笔记并在之后整理变得容易。

## 收件箱的使用场景

*   <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中的_新建笔记_按钮。
*   全局_创建笔记到收件箱_快捷键（默认 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>）。
*   [托盘图标菜单](../../Installation%20%26%20Setup/Desktop%20Installation/Tray%20icon%20%26%20automatic%20startup.md)中的_新建笔记_操作。
*   <a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏</a>扩展。
*   当搜索未找到匹配项时提供的_创建笔记_选项，位于<a class="reference-link" href="../Navigation/Jump%20to%20%26%20command%20palette.md">跳转与命令面板</a>、空标签页以及文本笔记的 `@` 补全中。

## 设置笔记收件箱

要创建笔记收件箱，请为其应用 `#inbox` [标签](../../Advanced%20Usage/Attributes/Labels.md)。

只有一个笔记应带有此标签。如果有多个笔记，应用程序只会使用其中一个。

> [!NOTE]
> 如果没有收件箱笔记，Trilium 将回退到今天的[日记笔记](../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md)，并根据需要创建它及其日历祖先。如果日记已被完全移除，则笔记会创建在顶层，而不是为其构建新的日记。

## 工作区收件箱

每个[工作区](../Navigation/Workspaces.md)都可以有自己的收件箱，通过 `#workspaceInbox` 标签设置。

当在工作区中聚焦时创建新笔记，位置按以下顺序确定：

*   该工作区中带有 `#workspaceInbox` 标签的笔记。
*   该工作区中带有 `#inbox` 的笔记。
*   今天的[日记笔记](../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md)，如果该工作区有 `#workspaceCalendarRoot`。
*   工作区根笔记本身。