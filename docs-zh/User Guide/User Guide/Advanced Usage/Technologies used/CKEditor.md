# CKEditor
## 编辑器核心

CKEditor 是支持 [文本](../../Note%20Types/Text.md) 笔记的所见即所得（WYSIWYG，即“你所见即你所得到”）编辑器。

其官方网站为 [ckeditor.com](https://ckeditor.com/)。

CKEditor 本身是一个商业产品，但其核心是开源的。正如其 [文档](https://ckeditor.com/docs/ckeditor5/latest/features/index.html) 所述，该编辑器支持相当多的功能。请注意，并非所有功能都在 Trilium 中启用。

## 高级功能

CKEditor 功能集中的某些功能被标记为高级功能。这意味着，没有许可证则无法使用这些功能。

Trilium 无法使用任何这些高级功能，因为它们需要商业许可证。不过，我们正在与 CKEditor 团队进行讨论，以期允许我们使用其中一部分高级功能，例如 [斜杠命令](https://ckeditor.com/docs/ckeditor5/latest/features/slash-commands.html)。

## 插件

CKEditor 生态系统具有很高的可扩展性，这意味着可以编写自定义插件来扩展编辑器的功能，使其超越原有范围。

Trilium 利用了此类功能：

*   数学公式功能是通过 [isaul32/ckeditor5-math: Math feature for CKEditor 5.](https://github.com/isaul32/ckeditor5-math) 的一个版本添加的，我们对其进行了修改以适应我们的需求。
*   我们还使用了修改后的上游插件，例如 [ckeditor/ckeditor5-mermaid](https://github.com/ckeditor/ckeditor5-mermaid)，以支持内联的 Mermaid 代码。
*   [mlewand/ckeditor5-keyboard-marker: Plugin adds support for the keyboard input element (`<kbd>`) to CKEditor 5.](https://github.com/mlewand/ckeditor5-keyboard-marker)
*   [ThomasAitken/ckeditor5-footnotes: Footnotes plugin for CKEditor5](https://github.com/ThomasAitken/ckeditor5-footnotes) 的一个修改版本，用于支持脚注。

除此之外，Trilium 还有自己的一套特定插件，例如：

*   <a class="reference-link" href="../../Note%20Types/Text/Cut%20to%20subnote.md">剪切到子笔记</a>
*   <a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>
*   提及（Mentions），用于链接页面。
*   <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a>
*   [引用链接](../../Note%20Types/Text/Links.md)
*   [警示框](../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md)，我们最终创建了自己的插件，但 [aarkue/ckeditor5-admonition](https://github.com/aarkue/ckeditor5-admonition) 提供了很好的灵感（包括工具栏图标）。