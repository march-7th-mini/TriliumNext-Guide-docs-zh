# 跳转与命令面板
<figure class="image image-style-align-center"><img style="aspect-ratio:991/403;" src="1_Jump to &amp; command palette_image.png" width="991" height="403"></figure>

## 跳转到笔记

_跳转到笔记_ 功能允许通过搜索笔记标题在笔记之间轻松导航。除此之外，它还可以触发完整搜索或创建笔记。

要进入“跳转到”对话框：

*   在 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a> 中，按 <span class="tn-icon bx bx-send"></span> 按钮。
*   使用键盘，按 <kbd>Ctrl</kbd> + <kbd>J</kbd>。

除了搜索笔记外，还可以搜索命令。有关更多信息，请参阅下面的专门章节。

### 交互

*   默认情况下，当没有输入文本时，它会显示最近的笔记。
*   使用键盘，使用向上或向下箭头键在项目之间导航。按 <kbd>Enter</kbd> 打开所需的笔记。
*   如果笔记不存在，可以通过输入所需的笔记标题并选择以下两个选项之一来创建它：
    *   _创建笔记_ 将其放置在 <a class="reference-link" href="../Notes/Note%20Inbox.md">笔记收件箱</a> 中：标记为 `#inbox` 的笔记，如果没有则为今天的 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>，如果也没有日记则为顶层。当提升到 <a class="reference-link" href="Workspaces.md">工作区</a> 中时，使用工作区自己的收件箱，如果工作区有 `#workspaceCalendarRoot`，则使用今天的日记笔记，否则使用工作区根目录本身。该选项会指明目标位置，因此在创建笔记之前始终可见。
    *   _创建子笔记_ 将其放置在当前打开的笔记下。
*   当标题搜索未找到笔记时，结果下方的栏提供两种进一步搜索的方式。它保持在列表下方，无论结果滚动多远。当字段为空或列出命令时，两者都会隐藏。
    *   _包含笔记内容_ 开关会搜索笔记的内容及其标题，并在当前位置列出找到的内容以替代当前结果，而不会离开对话框。它在查询更改时保持开启，直到被关闭。按 <kbd>Shift</kbd>+<kbd>Enter</kbd> 从键盘切换它。
    *   _在完整搜索中显示_ 会在新标签页中打开完整 <a class="reference-link" href="Search.md">搜索</a> 中的查询，在那里可以通过其选项进一步细化。按 <kbd>Ctrl</kbd>+<kbd>Enter</kbd> 从键盘运行它。
*   要查看结果响应的按键，请单击结果下方的 <kbd>?</kbd> 按钮，或在搜索字段获得焦点时按 <kbd>Alt</kbd>+<kbd>F1</kbd>。
*   在足够宽的桌面窗口中，结果中高亮的笔记会在其右侧预览：其路径、标题、属性以及内容的开头。预览会随着高亮在结果中移动而跟随，命令面板则不会显示预览。
*   创建笔记的选项列在笔记之后。当没有笔记匹配时，列表会在它们上方说明。 <kbd>Enter</kbd> 打开最匹配的笔记，或在没有匹配时创建笔记。否则，从第一个笔记按 <kbd>↑</kbd> 可到达创建笔记的选项。

## 最近的笔记

跳转到笔记还能够显示最近查看/编辑的笔记列表并快速跳转到其中。

要访问此功能，请单击顶部的 `跳转到` 按钮。默认情况下（当没有在自动完成中输入任何内容时），此对话框将显示最近的笔记列表。

最近的笔记按最后访问时间分组：_今天_、_昨天_、_过去 7 天_、_过去 30 天_ 和 _更早_。相同的列表及相同的分组会在任何获得焦点且为空的笔记字段中打开。

## 命令面板

<figure class="image image-style-align-center"><img style="aspect-ratio:982/524;" src="Jump to &amp; command palette_image.png" width="982" height="524"></figure>

命令面板是一项功能，允许轻松执行应用程序中各处可找到的各种命令，例如来自菜单或键盘快捷键的命令。此功能直接集成到“跳转到”对话框中。

### 交互

要触发命令面板：

*   按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd> 直接显示命令面板。
*   如果在“跳转到”对话框中，在搜索中输入 `>` 以切换到命令面板。

交互：

*   输入几个词以在命令之间过滤。
*   使用键盘上的向上和向下箭头或鼠标选择命令。
*   按 <kbd>Enter</kbd> 执行命令。

要退出命令面板：

*   移除搜索中的 `>` 以返回笔记搜索。
*   按 <kbd>Esc</kbd> 完全关闭对话框。

### 可用选项

目前显示以下选项：

*   大多数 <a class="reference-link" href="../Keyboard%20Shortcuts.md">键盘快捷键</a> 都有一个条目，但那些过于特定而无法从对话框运行的除外。
*   一些额外的选项，尚未作为键盘快捷键提供，但可以从各种菜单访问，例如：导出笔记、显示附件、搜索笔记或配置 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>。

### 限制

目前无法定义显示在命令面板中的自定义操作。将来可能会通过将选项集成到启动栏中来改变这一点，启动栏可以根据需要进行自定义。