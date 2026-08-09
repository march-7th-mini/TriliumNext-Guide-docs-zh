# 格式刷
<figure class="image image-style-align-right"><img style="aspect-ratio:220/76;" src="Format Painter_image.png" width="220" height="76"></figure>

格式刷是文本笔记中的一项功能，允许用户复制文本的格式（如**粗体**、_斜体_、~~删除线~~等），并将其应用于文档的其他部分。它有助于保持格式一致，并加速富内容的创建。

## 使用说明

单击要复制格式的文本，然后使用格式刷工具栏按钮（<img class="image_resized" style="aspect-ratio:150/150;width:2.7%;" src="Format Painter_746436a2e1.svg" alt="Format painter" width="150" height="150">）来复制样式。然后用鼠标选中目标文本以应用该格式。

*   **复制格式**：将光标置于带有某种格式的文本中，单击格式刷工具栏按钮。鼠标光标会发生变化，表示格式刷已就绪。
*   **使用复制的格式进行涂抹**：用鼠标选中目标文本。松开鼠标按钮时，格式即被应用，同时格式刷解除就绪状态——光标恢复正常。
*   **取消而不应用格式**：再次单击工具栏按钮或按 <kbd>Escape</kbd> 键。

## 局限性

1.  尚不支持对块级格式（如标题或图片样式）进行涂抹。这是因为在 <a class="reference-link" href="../../Advanced%20Usage/Technologies%20used/CKEditor.md">CKEditor</a> 中，它们被视为内容的一部分，而非文本格式。
2.  格式刷作用于选区，而非单词：单击单个单词不会对其应用格式。单击仅定位光标，因此您在那里输入的文本会采用复制的格式。
3.  格式刷是一次性的；每次涂抹都需要重新复制格式。