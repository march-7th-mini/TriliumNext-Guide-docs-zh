# 笔记上下文菜单
<figure class="image image-style-align-right image_resized" style="width:44.65%;"><img style="aspect-ratio:514/291;" src="Note contextual menu_image.png" width="514" height="291"></figure>

右键点击某些笔记类型（如<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>或<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>）的内容时，会显示一个上下文菜单。

## 功能

*   在<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面端安装</a>中，右键点击拼写错误的单词时会显示<a class="reference-link" href="../../Note%20Types/Text/Spell%20Check.md">拼写检查</a>建议。
*   选中的文本可以通过搜索引擎（在<a class="reference-link" href="Options.md">选项</a>中配置）或[在 Trilium 内部](../Navigation/Search.md)进行搜索。
*   基本的剪贴板功能（剪切、复制、粘贴）。
*   将选中的文本复制为<a class="reference-link" href="../Import%20%26%20Export/Markdown.md">Markdown</a>。
*   使用<a class="reference-link" href="../../Note%20Types/Text/In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>执行快捷操作。

## 桌面端与 Web 端的区别

由于 Web 浏览器的限制，[Web 版本](../../Installation%20%26%20Setup/Server%20Installation.md)的行为略有不同：

*   当未选中文本或右键点击某个单词时，会显示浏览器的默认上下文菜单。
    *   这是有意为之，因为它保留了<a class="reference-link" href="../../Note%20Types/Text/Spell%20Check.md">拼写检查</a>功能。
*   当选中文本时，会显示一个精简菜单，仅包含 Web 版本中可用的功能
    *   _粘贴_不可用，因为浏览器未暴露该功能，请改用 <kbd>Ctrl</kbd>+<kbd>V</kbd>。
    *   仍然可以通过按 <kbd>Shift</kbd> + <kbd>右键点击</kbd> 来触发浏览器菜单。