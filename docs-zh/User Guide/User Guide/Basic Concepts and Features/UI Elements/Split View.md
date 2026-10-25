# 分屏视图
在 Trilium 中，可以并排处理两个或多个笔记。

<figure class="image image-style-align-center"><img style="aspect-ratio:1398/1015;" src="Split View_2_Split View_image.png" width="1398" height="1015"></figure>

## 交互

*   按笔记标题右侧的 <span class="tn-icon bx bx-dock-right"></span> 按钮，在其右侧打开一个新的分屏。
    *   可以根据需要打开任意数量的分屏，只需再次按下该按钮即可。
    *   仅支持水平分屏，不支持垂直分屏或拖放操作。
*   当至少打开一个分屏时，按下其旁边的 <span class="tn-icon bx bx-x"></span> 按钮即可关闭它。
*   使用 <span class="tn-icon bx bx-chevron-right"></span> 或 <span class="tn-icon bx bx-chevron-left"></span> 按钮在分屏之间移动。
*   创建、关闭和移动分屏也可以通过[键盘快捷键](../Keyboard%20Shortcuts.md)（_Create New Split_、_Close Active Split_、_Move Split Left_ 和 _Move Split Right_，默认均未分配）或通过[命令面板](../Navigation/Jump%20to%20%26%20command%20palette.md)触发。
*   可以使用 _Focus Split to the Left_ 和 _Focus Split to the Right_ 操作将焦点从一个分屏移动到相邻的分屏，这些操作会在标签页的任一端停止，而不会继续进入下一个标签页。它们默认也未分配快捷键。
*   每个[标签页](Tabs.md)都有各自的分屏视图配置（例如，一个标签页可以在分屏视图中显示两个笔记，而其他标签页则是单笔记视图）。
    *   标签页的标题将按分屏从左到右的顺序显示所有笔记标题，并以圆点符号分隔。
    *   标签页的图标将显示最后活动分屏的图标，点击该标签页时会自动聚焦到该分屏。

## 分屏与笔记树及提升

点击某个分屏的内容将聚焦该分屏。聚焦时，<a class="reference-link" href="Note%20Tree.md">笔记树</a>也会指示当前正在编辑的笔记。

每个分屏都可以拥有自己的<a class="reference-link" href="../Navigation/Note%20Hoisting.md">笔记提升</a>。

创建新分屏时，它将与之前的分屏共享相同的笔记提升。一个简单的解决方案是在创建分屏后再提升笔记。

这通常对于从一个位置到另一个位置重新组织笔记非常有用，方法是在第一个分屏中提升旧位置，在第二个分屏中提升新位置。这样可以轻松剪切和粘贴，而不会因为切换笔记导致树跳动。

## 移动端支持

从 v0.100.0 起，移动端视图也支持分屏视图，与桌面版分屏有以下区别：

*   在智能手机上，分屏视图是垂直排列的（一个在上，一个在下），而不是像桌面版那样水平排列。
*   每个标签页只能打开一个分屏。
*   无法调整两个分屏窗格的大小。
*   当键盘打开时，活动笔记将被“最大化”，从而即使在分屏打开时也能获得更多空间。当键盘关闭时，分屏恢复为等大。

交互：

*   要创建新分屏，点击笔记标题右侧的三点按钮，然后在顶部图标行中点击 <span class="tn-icon bx bx-dock-right"></span> _New split_。
    *   仅当当前标签页尚未打开分屏时，此选项才可用。
*   要关闭分屏，点击笔记标题右侧的三点按钮，然后选择 _Close this pane_。
    *   请注意，此选项仅在分屏中的第二个笔记上可用（智能手机上位于底部的那个，平板电脑上位于右侧的那个）。
*   长按链接时，将显示上下文菜单，其中包含 _Open note in a new split_ 选项。
    *   如果已经存在分屏，该选项将替换现有分屏。