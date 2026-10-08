# 键盘快捷键
这应该是一份完整的键盘快捷键列表。请注意，其中一些可能只在特定上下文中有效（例如在笔记树窗格或笔记编辑器中）。

## 配置键盘快捷键

大多数键盘快捷键也可以在<a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_ 中进行配置。

在<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装版</a>中，还可以通过点击按键组合旁边的地球图标将快捷键设为全局快捷键，这样即使 Trilium 未处于焦点状态，快捷键也能生效。

### 键盘布局

快捷键遵循当前键盘布局按键上印制的字符。例如，在法语 AZERTY 键盘上，<kbd>Ctrl</kbd>+<kbd>Z</kbd> 指的是标有 Z 的按键。

在不输入拉丁字母的布局上（例如俄语、希腊语或希伯来语），输入该字母表字母的按键等同于美式 QWERTY 键盘上相同位置的按键。因此 <kbd>Ctrl</kbd>+<kbd>J</kbd> 指的是俄语键盘上输入 `о` 的按键，这样无需先切换布局，快捷键也能继续使用。

输入标点符号的按键仍然遵循其自身的字符。在俄语键盘上，输入 `.` 的按键触发的是 <kbd>Ctrl</kbd>+<kbd>.</kbd>，而不是美式键盘上该位置按键的快捷键。

## 快捷键参考

> [!NOTE]
> 所有这些快捷键表示默认的按键绑定，可以在<a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_ 中单独更改。

### 笔记树

参见相应章节：<a class="reference-link" href="UI%20Elements/Note%20Tree/Keyboard%20shortcuts.md">键盘快捷键</a>

### 笔记导航

*   <kbd>Alt</kbd>+<kbd>←</kbd>、<kbd>Alt</kbd>+<kbd>→</kbd> – 在历史记录中后退 / 前进
*   <kbd>Ctrl</kbd>+<kbd>J</kbd> – 显示[“跳转到”对话框](Navigation/Note%20Navigation.md)
*   <kbd>Ctrl</kbd>+<kbd>.</kbd> – 滚动到当前笔记（当你从笔记处滚动离开或焦点当前在编辑器中时很有用）
*   <kbd>Backspace</kbd> – 跳转到父笔记
*   <kbd>Alt</kbd>+<kbd>C</kbd> – 折叠整个笔记树
*   <kbd>Alt</kbd>+<kbd>-</kbd>（alt 加减号）– 折叠子树（如果某个子树在笔记树窗格中占用太多空间，你可以将其折叠）
*   你可以定义一个[标签](../Advanced%20Usage/Attributes.md) `#keyboardShortcut`，例如值为 `Ctrl + I`。按下此键盘组合后，将带你跳转到定义该标签的笔记。请注意，必须重新加载/重启 Trilium（<kbd>Ctrl</kbd>+<kbd>R</kbd>）才能使更改生效。

在[笔记导航](Navigation/Note%20Navigation.md)中查看其中一些功能的演示。

### 标签页

*   <kbd>Ctrl</kbd> + <kbd>🖱 左键单击</kbd> – （或鼠标中键单击）笔记链接会在新标签页中打开笔记

仅在桌面版（electron 构建）中：

*   <kbd>Ctrl</kbd>+<kbd>T</kbd> – 打开空白标签页
*   <kbd>Ctrl</kbd>+<kbd>W</kbd> – 关闭活动标签页
*   <kbd>Ctrl</kbd>+<kbd>Tab</kbd> – 激活下一个标签页
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Tab</kbd> – 激活上一个标签页

### 分屏

<a class="reference-link" href="UI%20Elements/Split%20View.md">分屏视图</a>也可以通过键盘操作来控制，例如：

*   创建新分屏
*   关闭活动分屏
*   将分屏向左/右移动
*   将焦点切换到左侧/右侧的分屏。

所有这些键盘快捷键都没有默认设置，请前往<a class="reference-link" href="UI%20Elements/Options.md">选项</a> → _快捷键_，查找 _分屏视图_ 类别。

### 上下文菜单

每个上下文菜单都可以通过键盘操作，无论它是如何打开的，例如在文本笔记中使用 <kbd>Menu</kbd> 键来访问拼写建议。这些按键是固定的，无法在选项中更改。

*   <kbd>↑</kbd>、<kbd>↓</kbd> – 移动到上一个 / 下一个项目，跳过已禁用的项目，并在两端循环
*   <kbd>Home</kbd>、<kbd>End</kbd> – 移动到第一个 / 最后一个项目
*   <kbd>→</kbd> – 打开当前项目的子菜单，或在按列布局的子菜单中移动到下一列
*   <kbd>←</kbd> – 移动到上一列，或关闭子菜单并返回其项目
*   <kbd>Enter</kbd> 或 <kbd>Space</kbd> – 运行当前项目，或打开其子菜单
*   <kbd>Esc</kbd> – 关闭最内层的子菜单，然后关闭菜单本身
*   输入项目的前几个字母 – 跳转到标题以这些字母开头的下一个项目

对于从右到左的语言，<kbd>←</kbd> 和 <kbd>→</kbd> 的角色互换。

### 创建笔记

*   <kbd>Ctrl</kbd>+<kbd>O</kbd> – 在当前笔记之后创建新笔记
*   <kbd>Ctrl</kbd>+<kbd>P</kbd> – 在当前笔记中创建新的子笔记
*   <kbd>F2</kbd> – 编辑当前笔记克隆的<a class="reference-link" href="Notes/Cloning%20Notes/Branch%20prefix.md">分支前缀</a>

### 编辑笔记

> [!NOTE]
> 有关<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记特定的键盘快捷键，请参阅<a class="reference-link" href="../Note%20Types/Text/Keyboard%20shortcuts.md">键盘快捷键</a>和<a class="reference-link" href="../Note%20Types/Text/Markdown-like%20formatting.md">类 Markdown 格式</a>。

*   在笔记树窗格中按 Enter 会从笔记树窗格切换到笔记标题。从笔记标题按 Enter 会将焦点切换到文本编辑器。<kbd>Ctrl</kbd>+<kbd>.</kbd> 会从编辑器切换回笔记树窗格。
*   <kbd>Ctrl</kbd>+<kbd>.</kbd> – 从编辑器跳转到笔记树窗格并滚动到当前笔记

### 运行时快捷键

这些在 Electron 中挂钩，以类似于原生浏览器键盘快捷键。

*   <kbd>F5</kbd>、<kbd>Ctrl</kbd>+<kbd>R</kbd> – 重新加载 Trilium 前端
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> – 显示开发者工具
*   <kbd>Ctrl</kbd>+<kbd>F</kbd> – 显示搜索对话框
*   <kbd>Ctrl</kbd>+<kbd>-</kbd> – 缩小
*   <kbd>Ctrl</kbd>+<kbd>=</kbd> – 放大

### 其他

*   <kbd>Alt</kbd>+<kbd>O</kbd> – 显示 SQL 控制台（仅在你清楚自己在做什么时使用）
*   <kbd>Alt</kbd>+<kbd>M</kbd> – 免打扰模式 - 仅显示笔记编辑器，其他一切隐藏
*   <kbd>F11 </kbd> – 切换全屏
*   <kbd>Ctrl</kbd>+<kbd>S</kbd> – 在笔记树窗格中切换[搜索](Navigation/Search.md)表单
*   <kbd>Alt</kbd>+<kbd>A</kbd> – 显示笔记[属性](../Advanced%20Usage/Attributes.md)对话框