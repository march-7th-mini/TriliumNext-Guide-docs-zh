# 跳转到笔记与命令面板
<figure class="image image-style-align-center"><img style="aspect-ratio:991/403;" src="1_Jump to &amp; command palette_image.png" width="991" height="403"></figure>

## 跳转到笔记

_跳转到笔记_ 功能允许通过搜索笔记标题在笔记之间轻松导航。除此之外，它还可以触发完整搜索或创建笔记。

要进入“跳转到”对话框：

*   在 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a> 中，按 <span class="tn-icon bx bx-send"></span> 按钮。
*   使用键盘，按 <kbd>Ctrl</kbd> + <kbd>J</kbd>。

除了搜索笔记外，还可以搜索命令。更多信息请参阅下面的专门章节。

### 交互

*   默认情况下，当没有输入文本时，它会显示最近的笔记。
*   使用键盘上的上、下箭头键在项目之间导航。按 <kbd>Enter</kbd> 打开所需的笔记。
*   如果笔记不存在，可以通过输入所需的笔记标题并选择以下两个选项之一来创建它：
    *   _创建笔记_ 将其放入 <a class="reference-link" href="../Notes/Note%20Inbox.md">笔记收件箱</a>：标记为 `#inbox` 的笔记、今天的 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>（如果没有收件箱），或者如果没有日记则为顶层。当在 <a class="reference-link" href="Workspaces.md">工作区</a> 中提升时，使用工作区自己的收件箱，然后如果工作区有 `#workspaceCalendarRoot` 则使用今天的日记笔记，否则使用工作区根节点。该选项会标明目标位置，因此在创建笔记之前始终可见。
    *   _创建子笔记_ 将其放在当前打开的笔记下。
*   当标题搜索未找到笔记时，结果下方的栏提供两种进一步搜索的方式。无论结果滚动多远，它都保持在列表下方。当字段为空或列出命令时，两者都会隐藏。
    *   _包含笔记内容_ 开关会同时搜索笔记的内容及其标题，并在当前位置列出找到的内容，而不会离开对话框。在查询更改期间它会保持开启，直到被关闭。按 <kbd>Shift</kbd>+<kbd>Enter</kbd> 可从键盘切换它。
    *   _在完整搜索中显示_ 会在新标签页中打开完整 <a class="reference-link" href="Search.md">搜索</a> 中的查询，在那里可以通过其选项进一步细化。按 <kbd>Ctrl</kbd>+<kbd>Enter</kbd> 可从键盘运行它。
*   要查看结果对应的按键，请单击结果下方的 <kbd>?</kbd> 按钮，或在搜索字段获得焦点时按 <kbd>Alt</kbd>+<kbd>F1</kbd>。
*   在足够宽的桌面窗口中，结果中高亮的笔记会在其右侧预览：其路径、标题、属性及其内容的开头。预览会随着高亮在结果中移动而跟随，并且在命令面板中会被省略。
*   创建笔记的选项列在笔记之后。当没有笔记匹配时，列表会在它们上方说明。 <kbd>Enter</kbd> 打开最匹配的笔记，或在没有匹配时创建笔记。否则，从第一个笔记按 <kbd>↑</kbd> 可到达创建笔记的选项。

## 最近的笔记

跳转到笔记还具有显示最近查看/编辑的笔记列表并快速跳转到它的能力。

要访问此功能，请单击顶部的 `跳转到` 按钮。默认情况下（当自动完成中没有输入任何内容时），此对话框将显示最近的笔记列表。

最近的笔记按上次访问时间分组：_今天_、_昨天_、_过去 7 天_、_过去 30 天_ 和 _更早_。其他笔记字段（例如 _移动到_ 对话框中的字段）在为空时也会显示相同的列表：按字段末尾的 <span class="tn-icon bx bx-chevron-down"></span> 按钮，或按 <kbd>↓</kbd>。输入至少两个字符则会改为列出匹配的笔记。

## 命令面板

<figure class="image image-style-align-center"><img style="aspect-ratio:982/524;" src="Jump to &amp; command palette_image.png" width="982" height="524"></figure>

命令面板是一项功能，可以轻松执行整个应用程序中可找到的各种命令，例如来自菜单或键盘快捷键的命令。此功能直接集成到“跳转到”对话框中。

### 交互

要触发命令面板：

*   按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd> 直接显示命令面板。
*   如果在“跳转到”对话框中，在搜索中输入 `>` 以切换到命令面板。

交互：

*   输入几个词以在命令之间过滤。
*   使用键盘上的上、下箭头或鼠标选择命令。
*   按 <kbd>Enter</kbd> 执行命令。

要退出命令面板：

*   删除搜索中的 `>` 以返回笔记搜索。
*   按 <kbd>Esc</kbd> 完全关闭对话框。

### 可用选项

目前显示以下选项：

*   大多数 <a class="reference-link" href="../Keyboard%20Shortcuts.md">键盘快捷键</a> 都有对应条目，但那些过于具体而无法从对话框运行的除外。
*   一些额外的选项尚未作为键盘快捷键提供，但可以从各种菜单访问，例如：导出笔记、显示附件、搜索笔记或配置 <a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>。

### 限制

目前无法定义显示在命令面板中的自定义操作。将来可能会通过集成启动栏中的选项来改变这一点，启动栏可以根据需要进行自定义。