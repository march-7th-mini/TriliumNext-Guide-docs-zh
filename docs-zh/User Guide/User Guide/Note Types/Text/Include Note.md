# 包含笔记

文本笔记可以“包含”另一条笔记，作为只读小组件或交互式小组件，具体取决于笔记的类型。

这可用于例如包含动态生成的图表（来自脚本和“渲染 HTML”笔记）或其他更高级的用例。

## 包含笔记

在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中，查找 <span class="tn-icon cke cke-trilium-note"></span> 按钮。也为它定义了键盘快捷键，但默认未分配。

_包含笔记_ 对话框打开后有两行：_笔记_，用于搜索要包含的笔记；以及 _框尺寸_（见下方 _框尺寸_），一行按钮，每个按钮带有一个尺寸的小图示，下方有一句描述所选尺寸的说明。选定笔记后，按 _包含笔记_ 或 <kbd>Enter</kbd> 将其包含。输入不存在的笔记标题会提示创建它。

在对话框中选择的图像笔记、<a class="reference-link" href="../Canvas.md">Canvas</a> 或 <a class="reference-link" href="../Mermaid%20Diagrams.md">Mermaid 图表</a>笔记会作为图像插入而非被包含，因此 _框尺寸_ 行会说明这一点，而不是显示尺寸按钮。在文本笔记中，图像进入文本后可以调整大小，对话框会提醒你这一点，同时也会提醒你包含的尺寸之后可以更改。

要包含一条已被链接的笔记，在正在编辑的文本笔记中右键单击指向它的引用链接，然后选择菜单末尾的 _将链接转换为包含的笔记_。包含会获得适合该笔记的框尺寸，与通过按钮添加的包含一样。

[附件](../../Basic%20Concepts%20and%20Features/Notes/Attachments.md)也可以用同样的方式包含，从指向它的链接的上下文菜单中操作（参见那里的 _嵌入附件_）。

指向文本笔记块的链接也以同样的方式转换，使用 _将链接转换为笔记摘录_，然后包含只显示那些块。参见<a class="reference-link" href="Block%20references.md">块引用</a>。

## 框尺寸

框尺寸设置显示多少被包含的笔记内容。

*   _极小_ 显示单行而非内容：笔记的图标、其标题以及上方指向该笔记的路径，以及用于操作该笔记的按钮。被包含的笔记从不渲染，因此在编辑器之外显示该笔记的任何地方，例如打印时、工具提示中或共享页面上，_极小_ 包含会显示为指向被包含笔记的链接。
*   _小_ 和 _中_ 在有限高度的框中显示内容。文本在框内滚动，而图片、图表或视频会缩小以适应框。
*   _完整_ 显示全部内容。
*   _可展开_ 仅显示标题，直到按下其 <span class="tn-icon bx bx-chevron-right"></span> 箭头。在只读笔记中，单击标题行上除按钮和链接以外的任何位置也会展开或折叠它。

新的包含会获得适合其所显示内容的尺寸：

*   对于没有预览的笔记或附件（例如关系图或归档），为 _极小_。
*   对于音频，为 _小_。
*   对于代码笔记或代码文件（例如 `.js`、`.py` 或 `.txt` 附件），以及文本笔记块的摘录，为 _完整_。
*   对于其他任何内容，为 _中_。

_包含笔记_ 对话框在选定笔记后会在其 _框尺寸_ 按钮中选择该尺寸，你也可以在那里选择另一个。要稍后更改尺寸，选择该包含并使用其工具栏中的 _框尺寸_ 菜单，或其 _更多操作_ 菜单的 _尺寸_ 子菜单。对于被包含的代码或 Markdown 笔记以及嵌入的代码或 Markdown 文件，_框尺寸_ 菜单是 <span class="tn-icon bx bx-move-vertical"></span> 按钮，其工具提示会显示当前尺寸。

## 调整大小

_小_、_中_ 或 _可展开_ 的包含可以调整为任意宽度和高度。_极小_ 或 _完整_ 的包含始终适应其内容。

*   要调整包含的大小，选择它并拖动其右下角的手柄。要仅更改宽度或仅更改高度，改为拖动其右边缘或底边缘的中间位置，触摸屏在那里也会显示手柄。在从右到左的文本中，手柄位于左下角，宽度从左侧边缘更改。
*   调整大小可使用鼠标、触控笔或手指。
*   当高度变化时，将手柄移到笔记顶部或底部附近会滚动笔记。
*   比笔记窄的包含会居中，因此更改其宽度会移动其两侧。使其与笔记一样宽会恢复为完整宽度。
*   要取消调整大小，在释放手柄前按 <kbd>Esc</kbd>。
*   要重置尺寸，双击角手柄，或在触摸屏上双击它。双击右边缘或底边缘仅重置宽度或高度。
*   选择框尺寸会重置高度。选择 _极小_ 或 _完整_ 也会重置宽度。
*   当 _可展开_ 包含处于折叠状态时，只能更改其宽度。

## 题注

包含可以带有题注，居中显示在其框的底部。题注是文本笔记的一部分，因此可以像其余文本一样格式化，例如加粗或带有链接。

*   要添加题注，选择该包含，按其工具栏中的 <span class="tn-icon cke cke-caption"></span> _开启题注_ 按钮并输入题注。
*   要移除题注，再次按同一按钮。再按一次会恢复其原有文本，只要笔记保持打开。
*   _极小_ 包含没有题注。将包含切换为 _极小_ 会移除其题注，将其切换回较大尺寸会恢复题注，只要笔记保持打开。
*   _可展开_ 包含在内容折叠时于标题下方显示题注，展开后在内容下方显示。

## 标题

包含的标题行链接到被包含的笔记并容纳其按钮。要仅显示内容，选择该包含并按工具栏中的 <span class="tn-icon bx bx-window-alt"></span> _显示标题_ 按钮。再次按下会显示标题。

*   当标题隐藏时，包含工具栏中的 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 按钮会打开被包含笔记的菜单。
*   _极小_ 或 _可展开_ 包含始终显示其标题，其工具栏没有 _显示标题_ 按钮。

## 打开被包含的笔记

要在新标签页中打开被包含的笔记，按其标题末尾的 <span class="tn-icon bx bx-link-external"></span> _在新标签页中打开_ 按钮。嵌入的附件也有相同的按钮。

标题行末尾的 <span class="tn-icon bx bx-dots-vertical-rounded"></span> _更多操作_ 按钮会打开与右键单击标题行任意位置相同的菜单：打开该笔记的其他位置，以及对于嵌入的附件，对附件的操作。

在正在编辑的笔记中，该菜单还包含包含工具栏的命令：_尺寸_ 子菜单、_显示标题_ 和 _显示题注_（生效时各自带有勾选标记），以及末尾的 _转换为链接_。绘图画布、Mermaid 图表、被包含的文本、代码或 Markdown 笔记以及嵌入的代码或 Markdown 文件在 _尺寸_ 上方还有 _可编辑_。被包含的代码或 Markdown 笔记、嵌入的代码或 Markdown 文件以及 Mermaid 图表在 _可编辑_ 之后还有 _自动换行_ 和 _行号_ 子菜单（参见下方 _就地编辑包含_）。Mermaid 图表、被包含的 Markdown 笔记和嵌入的 Markdown 文件在这些子菜单之后还有 _源码视图_、_分屏视图_ 和 _预览_。对于嵌入的附件，它们跟随其第一组操作；对于被包含的笔记，它们结束菜单。

要在整个屏幕上显示 _中_ 或 _完整_ 尺寸的包含，按其标题末尾的 <span class="tn-icon bx bx-fullscreen"></span> _全屏_ 按钮。笔记块的摘录在那里有一个 <span class="tn-icon bx bx-pencil"></span> _编辑摘录_ 按钮；参见<a class="reference-link" href="Block%20references.md">块引用</a>。要返回，按右上角的 <span class="tn-icon bx bx-exit"></span> _退出全屏_，或按 <kbd>Esc</kbd>。

_极小_ 包含改为具有这些按钮，随后是相同的 _更多操作_ 按钮：

*   对于笔记，<span class="tn-icon bx bx-edit"></span> _快速编辑_ 在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Quick%20edit.md">快速编辑</a>中打开该笔记，<span class="tn-icon bx bx-link-external"></span> _在新标签页中打开_ 在新标签页中打开它。
*   对于嵌入的附件，<span class="tn-icon bx bx-file-find"></span> _在外部打开_ 在另一个应用程序中打开该文件，<span class="tn-icon bx bx-download"></span> _下载_ 下载它。文件的大小显示在其标题下方。

## 将包含转换为链接

要用指向被包含笔记的链接替换包含，选择它并按工具栏中的 <span class="tn-icon cke cke-link"></span> _转换为链接_ 按钮，或在其 _更多操作_ 菜单末尾选择 _转换为链接_。嵌入的附件以同样的方式变为指向该附件的链接。

## 共享功能中的被包含笔记

如果[共享笔记](../../Advanced%20Usage/Sharing.md)包含一个或多个被包含的笔记，它们将显示在笔记内容中，就像它们是笔记本身的一部分。包含的题注显示在被包含内容的下方。_极小_ 包含改为显示为指向被包含笔记的链接，对于会显示其周围已显示的笔记的包含也是如此，例如包含自身的笔记。打印或导出的笔记也是如此。

为此，被包含的笔记也必须被共享，否则它们将不会显示。但是，被包含的笔记仍可通过 `#shareHiddenFromTree` 从笔记树中隐藏。

## 交互式笔记

自 v0.104.0 起，被包含的笔记可能根据其笔记类型变为交互式：

*   <a class="reference-link" href="../../Collections.md">集合</a>（例如<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>）将完全交互式渲染，包括创建新笔记。
*   <a class="reference-link" href="../Saved%20Search.md">保存的搜索</a>也会显示结果。
*   <a class="reference-link" href="../Web%20View.md">网页视图</a>提供网站的交互式预览。

## 被包含的图像

被包含的图像，无论是图像笔记还是图像附件，都显示在图像查看器中，可缩放和平移：

*   要缩放，按图像右下角的 <span class="tn-icon bx bx-plus-circle"></span> _放大_ 和 <span class="tn-icon bx bx-minus-circle"></span> _缩小_ 按钮，或在触摸屏上捏合。它们之间的百分比可重置缩放。
*   要用鼠标滚轮缩放，先单击图像。在此之前，鼠标滚轮会滚动笔记。
*   要平移已放大的图像，拖动它。在其适应尺寸下，在触摸屏上拖动图像会滚动笔记。
*   要返回适应尺寸，双击图像。

在 _小_ 或 _中_ 框中，图像会缩小以适应框的高度。在全屏中，它适应屏幕。

## 就地编辑包含

被包含的文本笔记、被包含的代码笔记以及嵌入的代码文件（例如 `.js`、`.py` 或 `.txt` 附件）可以在不离开包含它们的笔记的情况下编辑。在此之前，代码笔记或文件在代码编辑器中以只读方式显示，其中可以选择和复制其代码，并可通过其装订线中的箭头折叠和展开其块。被包含的 Markdown 也可以编辑，参见下方 _被包含的 Markdown_。

*   要编辑，选择该包含并打开其工具栏开头的 <span class="tn-icon bx bx-edit-alt"></span> _可编辑_ 按钮，或在其 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单中勾选 _可编辑_。关闭 _可编辑_ 以停止编辑。
*   当 _可编辑_ 开启时，方向键会将光标移入包含并移出，如同穿过其余文本一样。从上方或左侧进入会将光标置于包含的开头，从下方或右侧进入会将其置于末尾。折叠的 _可展开_ 包含会被跳过。
*   当被包含的文本笔记获得焦点时，格式工具栏应用于它。它依次包含的笔记保持只读。
*   代码在与<a class="reference-link" href="../Code.md">代码</a>笔记相同的代码编辑器中编辑，使用其主题、缩进和自动换行设置。
*   在代码中输入 `/` 会列出其语言的<a class="reference-link" href="../../Advanced%20Usage/Snippets/Code%20Snippets.md">代码片段</a>，与在代码笔记中一样。
*   被包含的代码笔记或嵌入的代码文件的工具栏在 _可编辑_ 和 <span class="tn-icon bx bx-move-vertical"></span> _框尺寸_ 菜单之间还有<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>的语言和缩进菜单：_更改语言模式_（显示当前语言）和 _更改制表符宽度_（显示当前缩进）。_将内容重新缩进为_ 会转换代码本身的缩进并将其保存到被包含的笔记或文件，无论 _可编辑_ 是否开启。
    *   对于被包含的笔记，这些菜单会更改该笔记，与在其自己的标签页中一样。
    *   对于嵌入的代码文件，语言和缩进设置仅更改此包含显示该文件的方式，并与包含它的笔记一起保存。语言会替换文件名所给出的语言，_使用默认值_ 条目会返回<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ 中设置的缩进。这些设置不会更改文件本身，它的其他包含会保留自己的设置。
*   被包含的代码或 Markdown 笔记、嵌入的代码或 Markdown 文件以及 [Mermaid 图表](Insert%20buttons.md)的 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单在 _可编辑_ 之后还有两个子菜单，每个都有 _自动_、_开_ 和 _关_。它们更改代码编辑器显示源码的方式。
    *   _自动换行_ 会换行长行而非滚动它们。_自动_ 遵循<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ 中的设置。对于被包含的笔记，它会设置笔记的 `#wrapLines` 标签，正如其<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a>的 _自动换行_ 子菜单对代码笔记所做的那样。对于嵌入的文件或 Mermaid 图表，它仅更改此包含。
    *   _行号_ 显示或隐藏每行开头的编号。_自动_ 遵循<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ 中的设置。它仅更改此包含，对于被包含的笔记也是如此。
*   更改会在你输入时保存到被包含的笔记或附件，与在其自己的标签页中一样。
*   在包含的代码编辑器中所做的更改是包含它的笔记的撤销历史的一部分，与其文本的更改一起，按所做的顺序排列。这包括被包含的 Markdown 和 [Mermaid 图表](Insert%20buttons.md)的源码，以及对绘图画布的更改（见下文）。
    *   <kbd>Ctrl</kbd>+<kbd>Z</kbd> 撤销笔记的最后一次更改，<kbd>Ctrl</kbd>+<kbd>Y</kbd> 或 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> 重做它，无论光标在文本中还是在包含中，且在 _可编辑_ 关闭时也是如此。格式工具栏的 <span class="tn-icon cke cke-undo"></span> _撤销_ 和 <span class="tn-icon cke cke-redo"></span> _重做_ 按钮也是如此。使用 Vim 键位绑定时，包含中的 `u` 和 <kbd>Ctrl</kbd>+<kbd>R</kbd> 也是如此。
    *   焦点会移到被撤销或重做的更改处：移入包含的代码编辑器或绘图画布，或回到文本。
    *   撤销被包含笔记的更改会再次保存被包含的笔记。一旦被包含的笔记在其他地方（例如在另一个标签页中）被更改，其较早的更改就无法再从这里撤销，撤销会跳过它们。
    *   被包含的文本笔记保留自己的撤销历史。
*   <a class="reference-link" href="Block%20references.md">块引用</a>的包含仅编辑被引用的块。
*   在[只读笔记](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)中、对于标记为 `#readOnly` 的被包含笔记、或对于另一条笔记的附件，无法编辑。
*   <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Search%20in%20note.md">在笔记中搜索</a>会在其周围笔记的结果中找到被包含的文本和代码笔记的文本，并在 _可编辑_ 开启时替换它。

## 被包含的 Markdown

被包含的<a class="reference-link" href="../Markdown.md">Markdown</a>笔记和嵌入的 Markdown 文件（例如 `.md` 附件）会以与 Markdown 笔记在其自己的标签页中相同的三种视图显示（参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20types%20with%20split%20view.md">带分屏视图的笔记类型</a>）：<span class="tn-icon bx bx-code"></span> _源码视图_、<span class="tn-icon bx bxs-dock-left"></span> _分屏视图_ 和 <span class="tn-icon bx bx-show"></span> _预览_。

*   要切换视图，按包含标题行中的三个按钮之一。在正在编辑的笔记中，包含的工具栏在 _可编辑_ 之后有相同的按钮，其 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单将它们作为 _源码视图_、_分屏视图_ 和 _预览_。
*   在选择视图之前，包含显示 _预览_，当 _可编辑_ 开启时显示 _分屏视图_。
*   要编辑 Markdown，开启 _可编辑_（参见上方 _就地编辑包含_）。源码在 Markdown 笔记的代码编辑器中编辑，预览会随你输入而跟随更改。当 _可编辑_ 关闭时，源码可以阅读和复制但不能更改。
*   源码具有<a class="reference-link" href="../Markdown.md">Markdown</a>笔记的斜杠命令以及 `@` 和 `[[` 笔记链接。从 `@` 或 `[[` 列表创建的笔记会放在被包含的笔记下，对于嵌入的文件则放在包含它的笔记下，`/image` 会将图像上传到同一笔记。
*   _更多操作_ 菜单的 _自动换行_ 和 _行号_ 子菜单会更改源码的显示方式，与代码一样（参见上方 _就地编辑包含_）。
*   与在 Markdown 笔记中一样，预览会随源码一起滚动并高亮光标所在的块，<kbd>Ctrl</kbd>+<kbd>B</kbd>、<kbd>Ctrl</kbd>+<kbd>I</kbd>、<kbd>Ctrl</kbd>+<kbd>M</kbd> 和 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd> 会格式化所选内容。
*   在正在编辑的笔记中，视图与包含一起保存，因此同一笔记的两个包含可以显示不同的视图。在[只读笔记](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)中，视图也可以更改，直到笔记再次打开。
*   当源码显示时，包含具有其框尺寸的高度，或调整到的高度。_完整_ 包含改为适应其内容。
*   <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Search%20in%20note.md">在笔记中搜索</a>在源码显示时搜索源码，否则搜索预览。

## 绘图画布

绘图画布是 Excalidraw 画布，类似于<a class="reference-link" href="../Canvas.md">Canvas</a>笔记的画布，直接在文本笔记中绘制。它不是自己的笔记：绘图保存在文本笔记的 `Canvas.excalidraw` [附件](../../Basic%20Concepts%20and%20Features/Notes/Attachments.md)中，并与文本一起保存。

*   要插入绘图画布，打开<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>的 <span class="tn-icon cke cke-plus"></span> _插入_ 菜单并选择 <span class="tn-icon bx bx-pen"></span> _绘图画布_，位于 _Mermaid 图表_ 上方。它也可在<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中作为 _绘图画布_ 使用。画布以空白且可编辑的方式添加，位于隐藏标题的 _中_ 框中，并获得焦点，准备好绘制。
*   要在图像上绘制或书写，选择该图像并按工具栏中的 <span class="tn-icon bx bxs-pen"></span> _将图像转换为绘图画布_ 按钮。图像被替换为 _中_ 框中的可编辑绘图画布，其标题隐藏且焦点在其中。图像以其原始尺寸位于画布中央，缩放以显示全部，并被锁定，以免意外选中或移动。当它被锁定时，画布可以在图像上放大，但不能缩小超过它或滚动超出其边缘。要移动或调整图像大小，右键单击它并选择 _解锁_。图像的题注会保留，但其对齐方式或链接不会保留。只有单独占一行的图像可以转换，段落内的图像不行。撤销会恢复图像。
*   通过 _附加并嵌入文件_（位于 <span class="tn-icon cke cke-paper-clip"></span>_附加文件_ 按钮下）附加的 Excalidraw 文件（`.excalidraw`）也会变为绘图画布，位于以文件名命名的 _中_ 框中。它开始时 _可编辑_ 关闭，因此绘图会显示但在 _可编辑_ 开启之前无法更改（见下文）。
*   要在没有焦点的画布上绘制，先单击它。在此之前，触摸手势会滚动笔记。然后画布具有 Canvas 笔记的工具、菜单和键盘快捷键。工具栏、菜单和所选形状的属性仅在画布具有焦点时显示，因此在其他地方绘图读起来就像文本中的图片。
*   鼠标滚轮和触控板在画布上也会滚动笔记，与在文本上一样。要缩放，使用画布工具栏的缩放按钮；要在绘图中移动，使用 <span class="tn-icon bx bxs-hand"></span> _手形_ 工具。在全屏中，鼠标滚轮改为移动和缩放绘图。
*   画布工具栏取代 Excalidraw 菜单：_导出图像_、_在画布上查找_、_库_ 和 _帮助_ 位于其 <span class="tn-icon bx bx-category"></span> _更多工具_ 菜单的末尾。在全屏中，Excalidraw 菜单会再次显示。
*   对绘图的更改是文本笔记撤销历史的一部分（参见上方 _就地编辑包含_）。<kbd>Ctrl</kbd>+<kbd>Z</kbd>、<kbd>Ctrl</kbd>+<kbd>Y</kbd> 以及画布工具栏的 <span class="tn-icon bx bx-undo"></span> _撤销_ 和 <span class="tn-icon bx bx-redo"></span> _重做_ 按钮会撤销和重做笔记的最后一次更改，无论是在绘图中还是在文本中。
*   新绘图具有笔记的背景色。从 Excalidraw 菜单选择的背景会替换它。
*   要保护已完成的绘图免受意外更改，选择它并关闭其工具栏开头的 <span class="tn-icon bx bx-edit-alt"></span> _可编辑_ 按钮，或在其 <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_ 菜单中取消勾选 _可编辑_。然后绘图会以静止图片显示，保持其原有的缩放和位置，并且无法再更改、缩放或移动。要再次绘制，重新开启 _可编辑_。
*   框尺寸、调整大小、题注和标题的工作方式与被包含的笔记相同，但绘图工具栏将框尺寸、_显示标题_ 和 _转换为链接_ 留给其 _更多操作_ 菜单。
*   在桌面布局中，无论框多小，Excalidraw 都保持其桌面界面。在移动布局中，窄或短的框会将其切换为紧凑界面。要获得更多空间，选择 _完整_，或显示标题并按 <span class="tn-icon bx bx-fullscreen"></span> _全屏_。
*   添加到绘图中的图片存储在同一附件中。转换的图像改为作为笔记的图像附件保留，以生成的代码命名。
*   在[只读笔记](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)中，绘图也显示为静止图片。
*   在[共享页面](../../Advanced%20Usage/Sharing.md)上，绘图以其自身尺寸显示为图片，无论其框的尺寸如何，以浅色或深色以匹配页面。对绘图的每次更改都会将此图片保存为笔记的 SVG 图像附件，同样以生成的代码命名。

### 限制

*   Excalidraw 形状库不会为绘图画布保存。
*   在编辑器之外，例如在工具提示中、打印时或附件列表中，绘图显示为图片。
*   绘图在第一次更改之前没有用于共享页面的图片，从图像转换而来的除外。在此之前，例如对于附加的 `.excalidraw` 文件，共享页面改为显示下载绘图的链接。
*   在 Safari 中，共享页面上绘图的图片遵循系统的浅色或深色外观，而非页面上选择的主题。
*   粘贴到同一笔记中的绘图画布副本会与原始绘图共享绘图，因此对其中一个的更改只有在笔记再次打开后才会在另一个中显示。粘贴到另一条笔记中的副本会获得自己的绘图。