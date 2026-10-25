# 笔记树
本页介绍如何在 TriliumNext 中操作笔记树，重点介绍移动笔记。

![](Note%20Tree_image.jpg)

## 拖放

![拖放示例](Note%20Tree_drag-and-drop.gif)

如上方示例所示，你可以通过拖放笔记轻松地重新排列笔记树。

### 导入文件

只需将文件或压缩包拖入笔记树中，即可轻松将其导入 Trilium。

请注意，拖放始终会启用*安全导入*，这意味着即将导入的笔记中的某些功能（例如脚本）会被禁用。若要绕过此限制，请使用专用的[导入](../Import%20%26%20Export.md)功能（右键单击 → *导入到笔记*）。

与导入对话框不同，拖放还会对导入内容进行一些基本的自动检测。例如，拖入一个包含 `.obsidian` 文件夹的 .zip 文件会自动触发专用的 <a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a> 导入。

## 键盘操作

![使用键盘按键移动笔记的示例](Note%20Tree_move-note-with-keyboard.gif)Trilium 通过以下[快捷键](../Keyboard%20Shortcuts.md)提供高效的键盘操作：

*   <kbd>Ctrl</kbd> + <kbd>↑</kbd> 和 <kbd>Ctrl</kbd> +<kbd>↓</kbd>：按顺序将笔记上移或下移。
*   <kbd>Ctrl</kbd>+<kbd>←</kbd>：将笔记的父级改为其祖父级，从而在层级中上移该笔记。
*   <kbd>Ctrl</kbd>+<kbd>→</kbd>：将笔记的父级设置为其当前上方的笔记，从而在层级中下移该笔记（此操作最好通过演示或实际操作来理解）。
*   <kbd>←</kbd> 和 <kbd>→</kbd>：展开和折叠子树。

## 上下文菜单

你还可以使用上下文菜单中熟悉的剪切和粘贴功能，或使用相关的键盘[快捷键](../Keyboard%20Shortcuts.md)来移动笔记：`CTRL-C`（[复制](../Notes/Cloning%20Notes.md)）、<kbd>Ctrl</kbd> + <kbd>X</kbd>（剪切）和 <kbd>Ctrl</kbd> + <kbd>V</kbd>（粘贴）。

更多信息请参阅 <a class="reference-link" href="Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。

## 树设置

单击树工具栏中的树图标以打开树设置弹出窗口。每个选项都是一个开关，切换后立即生效：

*   *隐藏已归档的笔记*：启用后，已归档的笔记不会显示在树中。
*   *自动折叠笔记*：启用后，笔记在一段时间无操作后会被折叠，以保持树整洁。
*   *跟随活动笔记*：启用后（默认），树会自动滚动并展开父节点，以保持当前活动笔记可见。禁用后，树与导航完全分离——只会更新活动笔记的背景高亮，但导航永远不会改变树的视口及其展开/折叠状态。可随时使用十字准星按钮手动将树跳转到活动笔记。

## 隐藏和窥视树

要隐藏或显示笔记树，在水平布局中按第一个标签页左侧的 <span class="tn-icon bx bx-sidebar"></span> 按钮，或在垂直布局中按 <a class="reference-link" href="Launch%20Bar.md">启动栏</a> 底部的 <span class="tn-icon bx bx-chevrons-left"></span> 按钮。*切换左侧窗格*[键盘快捷键](../Keyboard%20Shortcuts.md)（默认未分配）也可实现相同效果。请参阅 <a class="reference-link" href="Vertical%20and%20horizontal%20layout.md">垂直和水平布局</a>。

在水平布局中，应用左边缘有一条带箭头图标的小条。在垂直布局中，它位于 <a class="reference-link" href="Launch%20Bar.md">启动栏</a> 的右侧，并且仅在树隐藏时显示。

*   当树隐藏时，按该条会*窥视*树。
    *   在此模式下，树会临时显示在内容上方，而不会移动笔记内容。
    *   单击树外部、按 <kbd>Esc</kbd> 或再次按该条将隐藏树。
    *   按显示树的按钮会将其停靠。
*   在水平布局中，当树已停靠时按该条会将其隐藏。

*窥视树窗格*[键盘快捷键](../Keyboard%20Shortcuts.md)（默认为 <kbd>Alt</kbd>+<kbd>[</kbd>）与按该条的效果相同。一次只能窥视一个面板：窥视树会隐藏已窥视的 <a class="reference-link" href="Right%20Sidebar.md">右侧边栏</a>，反之亦然。

## 键盘快捷键

笔记树附带多个键盘快捷键以加快编辑速度，请参阅专用的 <a class="reference-link" href="Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a> 部分。