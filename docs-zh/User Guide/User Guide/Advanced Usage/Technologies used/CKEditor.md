# CKEditor
## 编辑器核心

CKEditor 是 [Text](../../Note%20Types/Text.md) 笔记背后的所见即所得（WYSIWYG，即 What You See Is What You Get）编辑器。

其网站是 [ckeditor.com](https://ckeditor.com/)。

CKEditor 本身是一款商业产品，但其核心是开源的。正如[其文档](https://ckeditor.com/docs/ckeditor5/latest/features/index.html)所述，该编辑器支持相当多的功能。请注意，并非所有功能都在 Trilium 中启用。

## 高级功能

CKEditor 将一些插件作为高级功能提供（斜杠命令、模板、AI 集成）。最初 Trilium（自 v0.96.0 起）随附了其中一些功能，例如斜杠命令，这是 CKEditor 授予 Trilium Notes 开发者许可的一部分。

在 v0.105.0 中，我们决定用我们自己的开源实现替换这些高级插件。这也意味着我们可以更好地将这些插件定制为适合 Trilium 应用。

## 插件

CKEditor 生态系统具有相当强的可扩展性，也就是说可以编写自定义插件，将编辑器的功能扩展到其原始范围之外。

Trilium 利用了这些特性：

*   数学功能由 [isaul32/ckeditor5-math: Math feature for CKEditor 5.](https://github.com/isaul32/ckeditor5-math) 的一个版本添加，我们对其进行了修改以满足我们的需求。
*   我们还利用了修改过的上游插件，例如 [ckeditor/ckeditor5-mermaid](https://github.com/ckeditor/ckeditor5-mermaid)，以允许内联 Mermaid 代码。
*   [mlewand/ckeditor5-keyboard-marker: Plugin adds support for the keyboard input element (`<kbd>`) to CKEditor 5.](https://github.com/mlewand/ckeditor5-keyboard-marker)
*   [ThomasAitken/ckeditor5-footnotes: Footnotes plugin for CKEditor5](https://github.com/ThomasAitken/ckeditor5-footnotes) 的一个修改版本，以支持脚注。

除此之外，Trilium 还有自己的一套特定插件，例如：

*   <a class="reference-link" href="../../Note%20Types/Text/Cut%20to%20subnote.md">剪切为子笔记</a>
*   <a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>
*   提及（Mentions），用于链接页面。
*   <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a>
*   [引用链接](../../Note%20Types/Text/Links.md)
*   [警示框](../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md)，我们最终创建了自己的插件，但 [aarkue/ckeditor5-admonition](https://github.com/aarkue/ckeditor5-admonition) 是一个很好的灵感来源（包括工具栏图标）。