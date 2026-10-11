# 在笔记中搜索
<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:898/93;" src="Search in note_image.png" width="898" height="93"></figure>

本地搜索允许你在当前显示的笔记中进行搜索。

## 替代方案

*   在浏览器中按下 <kbd>Ctrl</kbd>+<kbd>F</kbd>，且焦点不在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>或<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记中时，会触发浏览器原生搜索。这也会找到属于 Trilium UI 的文本。
*   在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记中按下 <kbd>Ctrl</kbd>+<kbd>F</kbd> 会显示 <a class="reference-link" href="../../Advanced%20Usage/Technologies%20used/CKEditor.md">CKEditor</a> 的搜索功能。

## 访问搜索

*   在桌面上，按下 <kbd>Ctrl</kbd> + <kbd>F</kbd>。
*   从<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中，找到上下文菜单并选择 _在笔记中搜索_。

## 交互

*   查找：
    *   在 _在文本中查找…_ 中填入要搜索的文本。
    *   搜索将在后台自动执行。
    *   使用文本框的上下箭头在结果之间导航。
*   替换：
    *   在 _在文本中查找…_ 字段中填入要替换的文本。
    *   在 _替换为…_ 字段中填入替换后的文本。
    *   按下 _替换_ 仅替换当前结果。
    *   按下 _全部替换_ 一次性替换所有结果。
*   选项：
    *   _区分大小写_ – 搜索将区分大写字符和小写字符（例如搜索 Hello 不会匹配 `hello`）。
    *   _匹配单词_ - 搜索将仅查找完全匹配的单词（例如搜索 `Java` 不会匹配 `JavaScript`）。