# 其他功能
## 缩进

<figure class="image image-style-align-right"><img style="aspect-ratio:201/124;" src="1_Other features_image.png" width="201" height="124"></figure>

可以使用<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中的以下按钮对段落进行缩进：

*   按 <span class="tn-icon cke cke-indent"></span> 将当前段落缩进增加一级。如有需要可多次按下。
*   按 <span class="tn-icon cke cke-outdent"></span> 将当前段落缩进减少一级。如果已处于最小缩进级别，该按钮将被禁用。
*   为方便起见，还提供了键盘快捷键。按 <kbd>Tab</kbd> 进行缩进，或按 <kbd>Shift</kbd>+<kbd>Tab</kbd> 减少缩进。即使光标不在段落或列表的开头，这些快捷键也能正常工作。
*   除段落外，缩进按钮在<a class="reference-link" href="Lists.md">列表</a>（用于嵌套）和<a class="reference-link" href="Tables.md">表格</a>中也可用。

当缩进的段落或标题以纯文本形式复制并粘贴时（例如粘贴到<a class="reference-link" href="../Code.md">代码</a>笔记或其他应用程序中），每个缩进级别都会变成行首的一个制表符。若复制内容保持在单个段落内，则仅包含其文本，不包含缩进。

反向操作同样有效：当纯文本粘贴到文本笔记中时，如果某个段落的所有行都以制表符开头，则该段落每有一个制表符就缩进一级。粘贴到代码块中时，制表符保持原样。

## Markdown 导入

如果剪贴板中包含 Markdown 文本，可以轻松将其导入到文本笔记中。只需复制 Markdown 格式的文本，然后按 <span class="tn-icon cke cke-trilium-markdown-mark"></span> 即可插入其可视化表示。

请注意，这仅适用于原始 Markdown（例如用 `# Heading 1` 生成标题），而不适用于 Markdown 的可视化表示（例如应用程序预览窗格中的形式）。在这种情况下，只需使用粘贴功能即可，它已经支持 HTML 格式的内容。

这主要适用于文本片段，对于整个 Markdown 文档，请使用专用的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a> 导入/导出功能。

如果通过 Web 浏览器访问 Trilium，Markdown 导入操作会要求在一个专用界面中输入要插入的内容，因为它无法访问剪贴板。

## 剪切为子笔记

<span class="tn-icon cke cke-trilium-scissors"></span> 按钮将使用选中的文本创建一个子笔记。更多信息，请参见<a class="reference-link" href="Cut%20to%20subnote.md">剪切为子笔记</a>。

## 查找和替换

<figure class="image image-style-align-right"><img style="aspect-ratio:394/203;" src="Other features_image.png" width="394" height="203"></figure>

<span class="tn-icon cke cke-find-replace"></span> 按钮将打开编辑器专用的搜索和替换功能。

或者，可以按 <kbd>Ctrl</kbd>+<kbd>F</kbd> 组合键来显示该对话框。