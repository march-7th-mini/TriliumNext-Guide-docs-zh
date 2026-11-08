# 外部链接
外部链接是指向例如网站的标准网页链接。例如，[https://en.wikipedia.org/wiki/South\_China\_Sea](https://en.wikipedia.org/wiki/South_China_Sea) 是一个指向维基百科页面的外部链接。

要创建不带自定义文本的链接：

*   在<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>中按 <span class="tn-icon cke cke-link"></span>，或按 <kbd>Ctrl</kbd>+<kbd>K</kbd>：
    *   自 v0.107.0 起，_添加链接_ 对话框会在 _网页_ 上打开，在桌面端以光标旁的弹出窗口形式显示。输入或粘贴地址，以及可选的 _链接标题_；如果没有标题，链接将显示其地址。地址字段末尾的 <span class="tn-icon bx bx-paste"></span> _粘贴_ 按钮会用剪贴板上的文本替换其文本。此按钮仅在 Trilium 可以读取剪贴板时显示：在桌面应用中，以及在通过 HTTPS 访问的浏览器中（除非剪贴板访问被阻止）。
    *   当您离开地址字段，或使用 _粘贴_ 按钮粘贴时，空的 _链接标题_ 会填入网页的标题；加载时其末尾会显示一个旋转指示器。您输入的标题会被保留。要关闭此功能，请转到<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_，并在 _功能_ 部分关闭 _自动获取文本链接的标题_。
    *   _显示为_ 会将地址插入为 _文本_，或作为<a class="reference-link" href="../Link%20Previews.md">链接预览</a>之一：_图标和文本_、_卡片_，或者对于 YouTube 视频或音频/视频文件的地址，则为 _嵌入_。
    *   按 <kbd>Enter</kbd> 或 _插入链接_ 确认。
*   或者，使用<a class="reference-link" href="../Slash%20Commands.md">斜杠命令</a>并选择 _链接到网页_，它会打开相同的对话框。_链接到网页（带图标）_ 和 _链接到网页（作为卡片）_ 会以已选好的显示方式打开它。
*   更简单的方法是粘贴原始链接并按空格，将其自动转换为链接。
*   <a class="reference-link" href="Internal%20(reference)%20links.md">内部（引用）链接</a>的 <span class="tn-icon cke cke-trilium"></span> 按钮和 <kbd>Ctrl</kbd>+<kbd>L</kbd> 会在 _笔记_ 上打开相同的对话框。在对话框顶部选择 _网页_ 即可从那里创建外部链接。

没有协议的地址（如 `example.com`）会加上 `https://`。对话框不会插入不是有效 URL 的地址，也不会插入 `javascript:`、`vbscript:` 或 `data:` 链接，因为这些链接可以运行代码，并会在地址字段下方显示原因。粘贴到 _笔记_ 字段中或从其搜索中选择的 URL 会将对话框切换到 _网页_。当所选文本是 URL 时，对话框也会在 _网页_ 上打开。

要创建带自定义文本的链接：

*   首先，输入并选择将要转换为链接的文本。
*   如上所述打开 _添加链接_ 对话框（通过格式工具栏，或 <kbd>Ctrl</kbd>+<kbd>K</kbd>）。所选文本会成为链接的文本，因此对话框不会提供 _显示为_。
*   或者，直接在所选文本上粘贴（<kbd>Ctrl</kbd>+<kbd>V</kbd>）将其转换为链接。

插入链接后：

*   如有需要，可以更改链接内的文本，但链接本身会保留。
*   要修改链接，请单击链接以显示弹出窗口，然后按 <span class="tn-icon cke cke-pencil"></span> _编辑链接_ 按钮。它会打开 _编辑链接_ 对话框，其中填入链接的地址和文本；将光标置于链接内并按 <kbd>Ctrl</kbd>+<kbd>K</kbd>、<kbd>Ctrl</kbd>+<kbd>L</kbd> 或其中一个链接按钮也会如此。_保存链接_ 会更改整个链接，包括其文本，对话框还可以将其转换为指向笔记的链接。
*   要移除链接，请单击它，打开弹出窗口末尾的 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单，然后选择 <span class="tn-icon cke cke-unlink"></span> _取消链接_。文本会保留，但链接被移除。
*   同一菜单中有 _打开链接_、_编辑链接_ 和 _复制地址（URL）_，以及 _显示为_，它会将链接转换为<a class="reference-link" href="../Link%20Previews.md">链接预览</a>之一，弹出窗口的 _显示_ 菜单也是如此。
*   右键单击链接会打开相同的菜单。

要在正在编辑的笔记中访问外部链接，请 <kbd>Ctrl</kbd>+单击或双击它，这会在新标签页或窗口中打开它，或者右键单击它并选择 _打开链接_。在触摸设备上，触摸并按住链接，然后选择 _打开链接_。[包含的笔记](../Include%20Note.md)中不可 _编辑_ 的链接会在单击时打开，就像在只读笔记中一样。