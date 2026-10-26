# 待办列表
## 扩展任务状态

<figure class="image image-style-align-left"><img style="aspect-ratio:303/264;" src="To-do Lists_image.png" width="303" height="264"></figure>

在 Trilium 中，待办事项并不局限于简单的“已完成”或“未完成”。任务还可以标记为_进行中_（“doing”）、_考虑中_（“maybe”）或_已取消_（“won't do”），从而更准确地反映事情的实际进展。

右键单击复选框并选择所需的状态。或者，按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter </kbd> 循环切换任务状态。点击或左键单击复选框将始终在“无”和“已完成”之间切换。在<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a>上，这些状态是 _列表 ›_ 按钮所在行中的按钮，当光标位于列表中时该行会显示。

在<a class="reference-link" href="../Text.md">文本</a>和<a class="reference-link" href="../Markdown.md">Markdown</a>笔记之间双向转换时，任务状态会被完整保留。

### 自定义扩展任务状态

任务状态是可自定义的：你可以重新排序、创建具有不同颜色和符号的新状态，或删除不需要的状态。详情请参阅<a class="reference-link" href="../../Advanced%20Usage/Customizing%20to-do%20task%20states.md">自定义待办任务状态</a>。

## 键盘快捷键

当位于空段落开头时，输入以下内容以插入待办列表：

*   `[ ]` 表示未勾选的项目
*   `[x]` 表示已勾选的项目

也支持扩展任务状态，使用其对应的 _Markdown 符号_。以下是默认值，但如有需要可以更改（请参阅<a class="reference-link" href="../../Advanced%20Usage/Customizing%20to-do%20task%20states.md">自定义待办任务状态</a>）：

*   `[/]` 表示“进行中”。
*   `[?]` 表示“考虑中”。
*   `[-]` 表示“已取消”。

要重新排序光标下的项目，请按 <kbd>Alt</kbd>+<kbd>Up</kbd> 或 <kbd>Alt</kbd>+<kbd>Down</kbd>。要重新排序多个项目，请先选中它们。

## 另请参阅

*   待办列表适用于小型任务列表。对于更复杂的日常任务跟踪，请考虑改用<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>集合。