# 笔记树
本页介绍如何在 TriliumNext 中操作笔记树，重点讲解移动笔记。

![](Note%20Tree_image.png)

## 拖放

![拖放示例](Note%20Tree_drag-and-drop.gif)

您可以通过拖放笔记轻松重新排列笔记树，如上例所示。

## 键盘操作

![使用键盘按键移动笔记的示例](Note%20Tree_move-note-with-keyboard.gif)Trilium 提供高效的基于键盘的操作方式，使用以下[快捷键](../Keyboard%20Shortcuts.md)：

*   <kbd>Ctrl</kbd> + <kbd><span>↑</span></kbd> 和 <kbd>Ctrl</kbd> +<kbd><span>↓</span></kbd>：按顺序向上或向下移动笔记。
*   <kbd>Ctrl</kbd>+<kbd><span>←</span></kbd>：将笔记的父级更改为其祖父级，从而在层级中向上移动笔记。
*   <kbd>Ctrl</kbd>+<kbd><span>→</span></kbd>：将笔记的父级设置为当前位于其上方的笔记，从而在层级中向下移动笔记（此操作最好通过演示或实际操作来理解）。
*   <kbd><span>←</span></kbd> 和 <kbd><span>→</span></kbd>：展开和折叠子树。

## 上下文菜单

您也可以使用上下文菜单中常见的剪切和粘贴功能，或使用相应的键盘[快捷键](../Keyboard%20Shortcuts.md)来移动笔记：`CTRL-C`（[复制](../Notes/Cloning%20Notes.md)）、<kbd>Ctrl</kbd> + <kbd>X</kbd>（剪切）和 <kbd>Ctrl</kbd> + <kbd>V</kbd>（粘贴）。

更多信息请参阅<a class="reference-link" href="Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。

## 树设置

单击树工具栏中的树图标以打开树设置弹出窗口。它包含以下选项：

*   **隐藏已归档笔记**：启用后，树中不显示已归档的笔记。
*   **自动折叠笔记**：启用后，笔记在一段时间不活动后会自动折叠，以保持树整洁。
*   **跟随活动笔记**：启用后（默认），树会自动滚动并展开父节点，以保持当前活动笔记可见。禁用后，树与导航完全分离——仅更新活动笔记的背景高亮，但树视口及其展开/折叠状态不会因导航而改变。可随时使用十字准线按钮手动跳转到活动笔记。

## 键盘快捷键

笔记树附带多个键盘快捷键以加快编辑速度，请参阅专门的<a class="reference-link" href="Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a>部分。