# 笔记树
本页面介绍如何在 TriliumNext 中操作笔记树，重点介绍移动笔记。

![](Note%20Tree_image.png)

## 拖放

![拖放示例](Note%20Tree_drag-and-drop.gif)

如上面的示例所示，你可以通过拖放笔记轻松地重新排列笔记树。

### 导入文件

只需将文件或压缩包拖入笔记树中，即可轻松将其导入 Trilium。

请注意，拖放导入始终会启用*安全导入*，这意味着脚本等某些功能在即将导入的笔记中会被禁用。要绕过此限制，请使用专用的[导入](../Import%20%26%20Export.md)功能（右键单击 → *导入到笔记*）。

与导入对话框不同，拖放还具备一些基本的导入自动检测功能。例如，拖放一个包含 `.obsidian` 文件夹的 .zip 文件将自动触发专用的 <a class="reference-link" href="../Import%20%26%20Export/Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a> 导入。

## 键盘操作

![使用键盘按键移动笔记的示例](Note%20Tree_move-note-with-keyboard.gif)Trilium 使用以下[快捷键](../Keyboard%20Shortcuts.md)提供高效的键盘操作：

*   <kbd>Ctrl</kbd> + <kbd>↑</kbd> 和 <kbd>Ctrl</kbd> +<kbd>↓</kbd>：按顺序向上或向下移动笔记。
*   <kbd>Ctrl</kbd>+<kbd>←</kbd>：通过将笔记的父级更改为其祖父级，在层级中向上移动笔记。
*   <kbd>Ctrl</kbd>+<kbd>→</kbd>：通过将笔记的父级设置为其上方的笔记，在层级中向下移动笔记（此操作最好通过演示或实际操作来理解）。
*   <kbd>←</kbd> 和 <kbd>→</kbd>：展开和折叠子树。

## 上下文菜单

你还可以使用上下文菜单中熟悉的剪切和粘贴功能，或使用相关的键盘[快捷键](../Keyboard%20Shortcuts.md)来移动笔记：`CTRL-C`（[复制](../Notes/Cloning%20Notes.md)）、<kbd>Ctrl</kbd> + <kbd>X</kbd>（剪切）和 <kbd>Ctrl</kbd> + <kbd>V</kbd>（粘贴）。

有关更多信息，请参阅 <a class="reference-link" href="Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。

## 树设置

单击树工具栏中的树图标以打开树设置弹出窗口。它包含以下选项：

*   **隐藏已归档的笔记**：启用后，已归档的笔记不会显示在树中。
*   **自动折叠笔记**：启用后，笔记会在一段时间不活动后折叠，以保持树整洁。
*   **跟随活动笔记**：启用后（默认），树会自动滚动并展开父节点，以保持当前活动笔记可见。禁用后，树与导航完全分离——仅更新活动笔记的背景高亮，但树的视口及其展开/折叠状态永远不会因导航而改变。随时使用十字准星按钮手动将树跳转到活动笔记。

## 键盘快捷键

笔记树附带多个键盘快捷键以加快编辑速度，请参阅专用的 <a class="reference-link" href="Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a>部分。