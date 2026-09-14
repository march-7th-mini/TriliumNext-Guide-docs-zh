# 跳转与命令面板
<figure class="image image-style-align-center"><img style="aspect-ratio:991/403;" src="1_Jump to &amp; command palette_image.png" width="991" height="403"></figure>

## 跳转到笔记

_跳转到笔记_ 功能允许通过搜索笔记标题在笔记之间轻松导航。除此之外，它还可以触发完整搜索或创建笔记。

要进入“跳转到”对话框：

*   在 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a> 中，按 ![](2_Jump%20to%20&%20command%20palette_image.png) 按钮。
*   使用键盘，按 <kbd>Ctrl</kbd> + <kbd>J</kbd>。

除了搜索笔记外，还可以搜索命令。有关更多信息，请参阅下面的专门章节。

### 交互

*   默认情况下，当没有输入文本时，它会显示最近的笔记。
*   使用键盘，使用向上或向下箭头键在项目之间导航。按 <kbd>Enter</kbd> 打开所需的笔记。
*   如果笔记不存在，可以通过输入所需的笔记标题并选择以下两个选项之一来创建它：
    *   _创建笔记_ 将其放置在 <a class="reference-link" href="../Notes/Note%20Inbox.md">笔记收件箱</a> 中：标记为 `#inbox` 的笔记，如果没有则为今天的 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>，如果也没有日记则为顶层。当提升到 <a class="reference-link" href="Workspaces.md">工作区</a> 中时，使用工作区自己的收件箱，回退到工作区根目录本身。该选项会命名目标位置，因此在创建笔记之前它始终可见。
    *   _创建子笔记_ 将其放置在当前打开的笔记下。

## 最近的笔记

跳转到笔记还能够显示最近查看/编辑的笔记列表并快速跳转到其中。

要访问此功能，请点击顶部的 `跳转到` 按钮。默认情况下（当自动完成中没有输入任何内容时），此对话框将显示最近的笔记列表。

或者，您可以点击右侧的“时间”图标。

## 命令面板

<figure class="image image-style-align-center"><img style="aspect-ratio:982/524;" src="Jump to &amp; command palette_image.png" width="982" height="524"></figure>

命令面板是一项功能，允许轻松执行应用程序中随处可见的各种命令，例如来自菜单或键盘快捷键的命令。此功能直接集成到“跳转到”对话框中。

### 交互

要触发命令面板：

*   按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd> 直接显示命令面板。
*   如果在“跳转到”对话框中，在搜索中输入 `>` 以切换到命令面板。

交互：

*   输入几个词以在命令之间进行筛选。
*   使用键盘上的向上和向下箭头或鼠标选择命令。
*   按 <kbd>Enter</kbd> 执行命令。

要退出命令面板：

*   删除搜索中的 `>` 以返回笔记搜索。
*   按 <kbd>Esc</kbd> 完全关闭对话框。

### 可用选项

目前显示以下选项：

*   大多数 <a class="reference-link" href="../Keyboard%20Shortcuts.md">键盘快捷键</a> 都有一个条目，但那些过于具体而无法从对话框运行的除外。
*   一些额外的选项尚未作为键盘快捷键提供，但可以从各种菜单访问，例如：导出笔记、显示附件、搜索笔记或配置 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>。

### 限制

目前无法定义在命令面板中显示的自定义操作。将来可能会通过将选项集成到启动栏中来改变这一点，如果需要，启动栏可以自定义。