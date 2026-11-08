# 内部（引用）链接
内部链接是指向 Trilium 内其他笔记的链接。

你可以通过点击内部链接来打开它。也可以将鼠标悬停在内部链接上，查看其内容的只读预览。

自 v0.107.0 起，在编辑文本笔记时点击内部链接会改为显示其弹出菜单，与点击外部链接的行为一致：

*   _打开笔记_ 会打开所链接的笔记；若链接指向附件，则显示为 _打开附件_。指向同一笔记内的链接会改为显示 _跳转到标题_、_跳转到块_ 或 _跳转到锚点_，并在不离开当前笔记的情况下滚动到对应位置。
*   <span class="tn-icon cke cke-trilium-download"></span> _下载_，对于指向附件的链接，会下载该附件。
*   <span class="tn-icon cke cke-pencil"></span> _编辑链接_ 会修改该链接，详见下文。
*   <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单，首先是 <span class="tn-icon bx bx-right-arrow-circle"></span> _打开笔记_，其作用与第一个按钮相同，然后是 <span class="tn-icon bx bx-link-external"></span> _在新标签页中打开笔记_、<span class="tn-icon bx bx-dock-right"></span> _在新分屏中打开笔记_、<span class="tn-icon bx bx-window-open"></span> _在新窗口中打开笔记_ 和 <span class="tn-icon bx bx-edit"></span> _快速编辑_，接着是 _编辑链接_ 和 <span class="tn-icon cke cke-unlink"></span> _取消链接_，后者会将链接转换为纯文本。显示笔记标题的链接末尾会有 _将链接转换为包含的笔记_，详见 <a class="reference-link" href="../Include%20Note.md">包含笔记</a>。指向附件的链接会在 _编辑链接_ 和 _取消链接_ 之间列出针对该附件的操作，但 <span class="tn-icon bx bx-trash"></span> _删除附件..._ 除外，它位于 _取消链接_ 之后，并以将附件转换为笔记的操作结尾。指向同一笔记内块的链接会省略在其他位置打开笔记的方式。

在正在编辑的笔记中，右键点击链接也会打开此菜单。

若要在不显示弹出菜单的情况下跟随链接，请按住 <kbd>Ctrl</kbd> 并点击，或双击该链接，其作用与弹出菜单的第一个按钮相同。在触摸设备上，长按链接，然后选择其菜单的第一项，例如 _打开笔记_ 或 _跳转到标题_。若要在新标签页中打开笔记，请使用鼠标中键点击它。弹出菜单打开时不会显示预览。

在 [包含的笔记](../Include%20Note.md) 中，若链接所在笔记不可 _编辑_，点击链接会直接打开，与在只读笔记中的行为一致。

## 插入内部链接

可以通过以下方式在文本笔记的当前位置创建内部链接：

1.  按下 <kbd>Ctrl</kbd> + <kbd>L</kbd>，或点击 <a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a> 中 <span class="tn-icon cke cke-plus"></span> 菜单下方的 <span class="tn-icon cke cke-trilium"></span> 按钮，或在 <a class="reference-link" href="../Slash%20Commands.md">斜杠命令</a> 中选择 _链接到笔记（内部链接）_。在桌面端，_添加链接_ 对话框会在光标旁的弹出窗口中打开。
2.  搜索所需链接笔记的标题。也可以在此对话框中输入不存在的笔记标题并选择 _创建笔记_ 来创建新笔记，该笔记会被放入 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>（即今天的日记笔记；若未设置收件箱，则放在顶层），或选择 _创建子笔记_，将其放在正在编辑的笔记之下。

根据对话框中的 _链接标题_ 字段，有两种链接类型：

1.  未设置链接标题时，链接将显示笔记的标题。若笔记标题发生更改，链接会自动重命名为新名称。
    1.  这有时也被称为“引用链接”。
    2.  同时还会显示所链接笔记的图标。
    3.  若所链接的笔记被删除，链接会保留其最后显示的标题，以红色显示，并用 <span class="tn-icon bx bx-x"></span> 图标代替笔记图标。在编辑时点击它会打开 _修复链接_ 对话框，该对话框会搜索该标题；选择一个笔记或创建新笔记，即可将链接替换为指向该笔记的链接。
2.  输入了链接标题时，链接将显示该文本。
    1.  这会创建一个传统的超链接，其中链接文本可以与笔记标题不同。

自 v0.107.0 起，若要更改链接，请点击它并在其弹出菜单中按下 <span class="tn-icon cke cke-pencil"></span> _编辑链接_ 按钮。对于带有自身标题的链接，将光标置于其中并按 <kbd>Ctrl</kbd> + <kbd>L</kbd> 或点击 <span class="tn-icon cke cke-trilium"></span> 按钮同样可行。_编辑链接_ 对话框会在所链接的笔记上打开，其中包含其锚点，对于带有自身标题的链接，还包含链接的文本；_保存链接_ 会更改整个链接。在此处清空 _链接标题_ 会将链接变为显示笔记标题的链接，而输入标题则会使其拥有自己的标题。对于指向附件的链接，对话框仅显示 _链接标题_，清空它会使链接显示附件的标题。

## 就地链接

你也可以使用 `@` 符号“就地”插入内部链接：

1.  在文本笔记中输入 `@`，会打开笔记搜索菜单。
2.  输入几个字符以搜索所需笔记的标题。使用 <kbd>Up</kbd> 和 <kbd>Down</kbd> 选择正确的笔记，然后按 <kbd>Enter</kbd> 或 <kbd>Tab</kbd> 创建链接。也可以使用此方法创建新笔记，方法是输入不存在的笔记标题并选择 _创建笔记_（如上所述）或 _创建子笔记_。_创建子笔记_ 会在正在编辑的笔记下创建笔记而不询问其类型，插入链接并在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Navigation/Quick%20edit.md">快速编辑</a> 中打开新笔记，该界面会在笔记仍为空时提供可将其转换成的笔记类型。

若要在命名之前创建一个空的子笔记并链接到它，请使用 <a class="reference-link" href="../Insert%20buttons.md">插入按钮</a> 中所述的 _新建子笔记_。

## 粘贴内部链接

你也可以通过从笔记树中复制笔记来插入内部链接。

1.  在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中，选择一个笔记并按 <kbd>Ctrl</kbd> + <kbd>C</kbd>。
2.  在文本笔记中，按 <kbd>Ctrl</kbd> + <kbd>V</kbd> 粘贴链接。