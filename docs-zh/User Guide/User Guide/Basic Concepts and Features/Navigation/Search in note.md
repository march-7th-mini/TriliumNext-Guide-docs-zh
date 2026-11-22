# 在笔记中搜索
<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:898/93;" src="Search in note_image.png" width="898" height="93"></figure>

本地搜索允许你在当前显示的笔记内进行搜索。

## 替代方式

*   在浏览器中按下 <kbd>Ctrl</kbd>+<kbd>F</kbd>，且焦点不在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>或<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记中时，将触发浏览器原生搜索。这也会查找属于 Trilium 界面一部分的文本。
*   在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记中按下 <kbd>Ctrl</kbd>+<kbd>F</kbd> 将显示 <a class="reference-link" href="../../Advanced%20Usage/Technologies%20used/CKEditor.md">CKEditor</a> 的搜索功能。

## 访问搜索

*   在桌面上，按下 <kbd>Ctrl</kbd> + <kbd>F</kbd>。
*   从<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中，在顶部图标行中选择 _查找_。
*   在<a class="reference-link" href="Quick%20edit.md">快速编辑</a>中，两者都会在弹出窗口底部打开一个搜索栏，用于搜索弹出窗口中的笔记。

## 交互

*   查找：
    *   在 _在文本中查找…_ 中填入要搜索的文本。
    *   搜索将在后台自动执行。
    *   使用文本框的上下箭头在结果之间导航。
*   替换：
    *   在 _在文本中查找…_ 字段中填入要替换的文本。
    *   在 _替换为…_ 字段中填入用于替换的文本。
    *   按下 _替换_ 仅替换当前结果。
    *   按下 _全部替换_ 一次性替换所有结果。
*   选项：
    *   _区分大小写_ – 搜索将区分大写和小写字符（例如搜索 Hello 将不会匹配 `hello`）。
    *   _匹配单词_ - 搜索将仅查找完全匹配的单词（例如搜索 `Java` 将不会匹配 `JavaScript`）。

## 滚动条上的结果

在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记中，只要搜索有结果，滚动条就会用线条标记每个结果的位置，即使笔记短到无需滚动也是如此。当前结果的线条更粗。这些线条仅在桌面布局中显示。

*   点击某条线会跳转到该结果并将其设为当前结果。当结果过期时（例如在编辑笔记之后），点击只会跳转到该结果，下一次按 <kbd>Enter</kbd> 会重新搜索。
*   滚动条的滑块显示屏幕上可见的笔记部分，因此屏幕上结果的线条位于其下方。<kbd>Shift</kbd>+点击滚动条会将笔记的该部分带入视图。

## 包含的笔记

在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记中，搜索还会查找通过<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>所包含的笔记文本，顺序与它们在笔记中出现的顺序一致。

*   会搜索被包含的文本笔记和代码笔记的文本、嵌入的代码文件（例如 `.js` 或 `.txt` 附件）的文本，以及绘图画布的文本。包含项的标题和其他笔记的内容（例如集合或包含的<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>笔记）不会被搜索。
*   绘图画布中的结果会在绘图上高亮显示。画布仅在结果位于其视图之外时移动以显示该结果，并在搜索继续后移回，除非在此期间被移动过。在正在编辑的笔记中，对此类结果关闭搜索会将画布留在原处，并且在画布可编辑时，选中该结果的文本。
*   上下箭头会像遍历笔记其余部分一样遍历包含项的结果。
*   折叠的 _可展开_ 包含项中的结果在该结果为当前结果时会展开该包含项，并在搜索继续后再次折叠。
*   _替换_ 和 _全部替换_ 仅在其 _可编辑_ 按钮开启时才会更改被包含的笔记。当当前结果位于不可编辑的包含项中时，_替换_ 被禁用，_全部替换_ 会保持此类结果不变。绘图画布的文本永远不会被替换。