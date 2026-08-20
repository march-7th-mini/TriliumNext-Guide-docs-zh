# 键盘快捷键

这应该是一个完整的键盘快捷键列表。请注意，其中一些可能仅在特定上下文中有效（例如在树形面板或笔记编辑器中）。

## 配置键盘快捷键

大多数键盘快捷键也可以在 <a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_ 中进行配置。

在 <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 中，还可以通过点击按键组合旁边的地球图标来使快捷键全局生效，这样即使 Trilium 不在焦点状态下，快捷键也能正常工作。

## 快捷键参考

> [!NOTE]
> 以下所有快捷键均为默认按键绑定，可在 <a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_ 中单独修改。

### 树

参见相应章节：<a class="reference-link" href="UI%20Elements/Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a>

### 笔记导航

*   <kbd>Alt</kbd>+<kbd>←</kbd>, <kbd>Alt</kbd>+<kbd>→</kbd> – 在历史记录中后退/前进
*   <kbd>Ctrl</kbd>+<kbd>J</kbd> – 显示[“跳转到”对话框](Navigation/Note%20Navigation.md)
*   <kbd>Ctrl</kbd>+<kbd>.</kbd> – 滚动到当前笔记（当你滚动离开笔记或焦点在编辑器中时很有用）
*   <kbd>Backspace</kbd> – 跳转到父笔记
*   <kbd>Alt</kbd>+<kbd>C</kbd> – 折叠整个笔记树
*   <kbd>Alt</kbd>+<kbd>-</kbd> （Alt 加减号） – 折叠子树（如果某个子树在树形面板上占用太多空间，可以将其折叠）
*   你可以定义一个 [标签](../Advanced%20Usage/Attributes.md) `#keyboardShortcut`，例如值为 `Ctrl + I`。按下此组合键将跳转到定义了该标签的笔记。请注意，必须重新加载/重启 Trilium（<kbd>Ctrl</kbd>+<kbd>R</kbd>）才能使更改生效。

在[笔记导航](Navigation/Note%20Navigation.md)中查看其中一些功能的演示。

### 标签页

*   <kbd>Ctrl</kbd> + <kbd>🖱 左键单击</kbd> – （或鼠标中键单击）在笔记链接上可在新标签页中打开笔记

仅限桌面版（Electron 构建）：

*   <kbd>Ctrl</kbd>+<kbd>T</kbd> – 打开空白标签页
*   <kbd>Ctrl</kbd>+<kbd>W</kbd> – 关闭当前标签页
*   <kbd>Ctrl</kbd>+<kbd>Tab</kbd> – 激活下一个标签页
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Tab</kbd> – 激活上一个标签页

### 分屏

<a class="reference-link" href="UI%20Elements/Split%20View.md">分屏视图</a> 也可以通过键盘操作来控制，例如：

*   创建新的分屏
*   关闭当前分屏
*   向左/向右移动分屏
*   将焦点移到左侧/右侧的分屏。

这些键盘快捷键都没有默认设置，请前往 <a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_ 并查找 _分屏视图_ 类别。

### 创建笔记

*   <kbd>Ctrl</kbd>+<kbd>O</kbd> – 在当前笔记之后创建新笔记
*   <kbd>Ctrl</kbd>+<kbd>P</kbd> – 在当前笔记中创建新的子笔记
*   <kbd>F2</kbd> – 编辑当前笔记克隆的 <a class="reference-link" href="Notes/Cloning%20Notes/Branch%20prefix.md">分支前缀</a>

### 编辑笔记

> [!NOTE]
> 有关 <a class="reference-link" href="../Note%20Types/Text.md">文本</a> 笔记特有的键盘快捷键，请参阅 <a class="reference-link" href="../Note%20Types/Text/Keyboard%20shortcuts.md">键盘快捷键</a> 和 <a class="reference-link" href="../Note%20Types/Text/Markdown-like%20formatting.md">类 Markdown 格式</a>。

*   在树形面板中按回车键可从树形面板切换到笔记标题。在笔记标题中按回车键可将焦点切换到文本编辑器。<kbd>Ctrl</kbd>+<kbd>.</kbd> 可从编辑器切换回树形面板。
*   <kbd>Ctrl</kbd>+<kbd>.</kbd> – 从编辑器跳转到树形面板并滚动到当前笔记

### 运行时快捷键

这些快捷键在 Electron 中已挂钩，以模拟原生浏览器键盘快捷键。

*   <kbd>F5</kbd>, <kbd>Ctrl</kbd>+<kbd>R</kbd> – 重新加载 Trilium 前端
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> – 显示开发者工具
*   <kbd>Ctrl</kbd>+<kbd>F</kbd> – 显示搜索对话框
*   <kbd>Ctrl</kbd>+<kbd>-</kbd> – 缩小
*   <kbd>Ctrl</kbd>+<kbd>=</kbd> – 放大

### 其他

*   <kbd>Alt</kbd>+<kbd>O</kbd> – 显示 SQL 控制台（仅在你明确知道自己在做什么时使用）
*   <kbd>Alt</kbd>+<kbd>M</kbd> – 免打扰模式 - 仅显示笔记编辑器，隐藏其他所有内容
*   <kbd>F11 </kbd> – 切换全屏
*   <kbd>Ctrl</kbd>+<kbd>S</kbd> – 在树形面板中切换[搜索](Navigation/Search.md)表单
*   <kbd>Alt</kbd>+<kbd>A</kbd> – 显示笔记[属性](../Advanced%20Usage/Attributes.md)对话框