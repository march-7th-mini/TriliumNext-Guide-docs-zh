# 笔记树

本页介绍如何在 TriliumNext 中操作笔记树，重点介绍移动笔记。

<figure class="image image-style-align-right"><img style="aspect-ratio:401/720;" src="Note Tree_demo.webp" width="401" height="720"></figure>

## 拖放

![拖放示例](Note%20Tree_drag-and-drop.gif)

你可以通过拖放笔记轻松地重新排列笔记树，如上例所示。

笔记放置的位置取决于指针所在行的位置：

*   笔记的中间：拖动的笔记成为其最后一个子笔记。
*   两个笔记之间的线：拖动的笔记被放置在这两者之间。在展开的笔记下方，该线会将其放置为第一个子笔记。

### 导入文件

只需将文件或压缩包拖入笔记树中，即可轻松将其导入 Trilium。

请注意，拖放始终会启用*安全导入*，这意味着即将导入的笔记中的某些功能（如脚本）会被禁用。要绕过此限制，请使用专用的[导入](../Import%20%26%20Export.md)功能（右键单击 → *导入到笔记*）。

与导入对话框不同，拖放还具有一些基本的导入自动检测功能。例如，拖动一个包含 `.obsidian` 文件夹的 .zip 文件将自动触发专用的 <a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a> 导入。

## 键盘操作

![使用键盘按键移动笔记的示例](Note%20Tree_move-note-with-keyboard.gif)Trilium 使用以下[快捷键](../Keyboard%20Shortcuts.md)提供高效的键盘操作：

*   <kbd>Ctrl</kbd> + <kbd>↑</kbd> 和 <kbd>Ctrl</kbd> +<kbd>↓</kbd>：按顺序向上或向下移动笔记。
*   <kbd>Ctrl</kbd>+<kbd>←</kbd>：通过将笔记的父笔记更改为其祖父笔记，在层级中向上移动笔记。
*   <kbd>Ctrl</kbd>+<kbd>→</kbd>：通过将笔记的父笔记设置为其当前上方的笔记，在层级中向下移动笔记（此操作最好通过演示或实际操作来理解）。
*   <kbd>←</kbd> 和 <kbd>→</kbd>：展开和折叠子树。

## 上下文菜单

你还可以使用上下文菜单中熟悉的剪切和粘贴功能，或使用相关的键盘[快捷键](../Keyboard%20Shortcuts.md)来移动笔记：`CTRL-C`（[复制](../Notes/Cloning%20Notes.md)）、<kbd>Ctrl</kbd> + <kbd>X</kbd>（剪切）和 <kbd>Ctrl</kbd> + <kbd>V</kbd>（粘贴）。

有关更多信息，请参阅 <a class="reference-link" href="Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。

## 树设置

单击树工具栏中的树图标以打开树设置弹出窗口。每个选项在更改后立即生效：

*   *显示密度*：*宽松*（默认）或*紧凑*。紧凑行更短，因此屏幕上可以容纳更多笔记。此设置不会同步，因此每个设备保留自己的设置。
*   *隐藏已归档的笔记*：启用后，已归档的笔记不会显示在树中。
*   *自动折叠笔记*：启用后，笔记在一段时间不活动后会被折叠，以保持树整洁。
*   *跟随活动笔记*：启用后（默认），树会自动滚动并展开父节点，以保持当前活动笔记可见。你折叠的活动笔记的父笔记将保持折叠状态，直到你导航到另一个笔记或活动笔记被移动。禁用后，树完全与导航分离——仅更新活动笔记的背景高亮，但树视口及其展开/折叠状态永远不会因导航而改变。随时使用十字准线按钮手动将树跳转到活动笔记。

## 隐藏和窥视树

要隐藏或显示笔记树，在水平布局中按第一个标签页左侧的 <span class="tn-icon bx bx-sidebar"></span> 按钮，或在垂直布局中按 <a class="reference-link" href="Launch%20Bar.md">启动栏</a> 底部的 <span class="tn-icon bx bx-chevrons-left"></span> 按钮。*切换左侧窗格*[键盘快捷键](../Keyboard%20Shortcuts.md)（默认未分配）具有相同的效果。请参阅 <a class="reference-link" href="Vertical%20and%20horizontal%20layout.md">垂直和水平布局</a>。

在水平布局中，一条带有箭头图标的小条沿应用程序的左边缘延伸。在垂直布局中，它沿 <a class="reference-link" href="Launch%20Bar.md">启动栏</a> 的右侧延伸，并且仅在树隐藏时显示。

*   当树隐藏时，按下该条将*窥视*树。
    *   在此模式下，树临时显示在内容上方，而不会移动笔记的内容。
    *   单击树外部、按 <kbd>Esc</kbd> 或再次按该条将隐藏树。
    *   按显示树的按钮将其停靠。
*   在水平布局中，当树停靠时按该条将隐藏它。

*窥视树窗格*[键盘快捷键](../Keyboard%20Shortcuts.md)（默认为 <kbd>Alt</kbd>+<kbd>[</kbd>）与按该条的效果相同。一次只能窥视一个面板：窥视树会隐藏已窥视的 <a class="reference-link" href="Right%20Sidebar.md">右侧边栏</a>，反之亦然。

## 键盘快捷键

笔记树附带多个键盘快捷键以加快编辑速度，请参阅专用的 <a class="reference-link" href="Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a> 部分。