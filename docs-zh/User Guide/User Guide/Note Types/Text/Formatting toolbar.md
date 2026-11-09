# 格式化工具栏

Trilium 根据你的偏好，为文本笔记提供两种不同的编辑体验。

可以通过前往 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>，然后查找 <a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a> 部分来更改格式化工具栏的类型。在其中查找 _格式化工具栏_ 类别。

## 浮动

浮动栏是一种更简约的选项，其中格式化功能隐藏在两个不同的弹出窗口中。

### 块级弹出窗口

第一个弹出窗口是块级弹出窗口。它会出现在你当前正在编辑的段落左侧，显示为一串圆点：
![](Formatting%20toolbar_image.jpg)

点击此弹出窗口将显示特定于整个段落的格式化选项，例如设置标题、列表、表格等。

这些圆点同时也是拖动手柄：拖动它们可以将段落、所有选中的段落，或选中的元素（如图片、表格或包含的笔记）移动到笔记中的其他位置。右键单击它们会打开一个菜单，用于复制对该段落或所选段落的引用，参见 <a class="reference-link" href="Block%20references.md">块引用</a>。菜单的标题是其作用的块类型，例如 _段落_、_表格_ 或 _列表项_，当有多个块时则显示块的数量。对于段落以外的单个块，标题末尾的 <span class="tn-icon bx bx-help-circle"></span> 按钮会在笔记旁边的分屏中打开其类型的帮助页面。其第一组项目 _在上方插入_ 和 _在下方插入_ 列出了用于插入内容或将段落转换为其他块的 <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>，并将所选命令添加到段落上方或下方的新段落中。对于列表项，则由 _在上方插入项_、_在下方插入项_ 和 _插入子项_ 取代它们的位置，并添加一个空项。之后，_剪切_ 和 _复制_ 会将整个段落或所选段落放入剪贴板，即使只选中了部分文本也是如此；_剪切_ 还会将其移除。配置 AI 提供商后，_AI 助手_ 紧随其后，其项目与工具栏的 <span class="tn-icon cke cke-trilium-ai"></span> 按钮相同，并且作用于整个段落或所选段落，而不是选中的文本，参见 <a class="reference-link" href="In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>。其最后一项 _删除_ 会立即删除该段落或所选段落，而不要求确认；<kbd>Ctrl</kbd>+<kbd>Z</kbd> 可将它们恢复。

<figure class="image"><img style="aspect-ratio:1404/156;" src="2_Formatting toolbar_image.png" width="1404" height="156"></figure>

### 行内弹出窗口

行内弹出窗口会在选中文本时自动出现：

<figure class="image"><img style="aspect-ratio:1008/154;" src="1_Formatting toolbar_image.png" width="1008" height="154"></figure>

此处的所有选项仅适用于选中的文本部分，例如更改字体大小或将文本加粗。

## 固定

固定格式化提供了一种更传统的编辑范式，通常在需要大量格式化时很有用。

所有选项都组合到一个工具栏中，该工具栏会出现在笔记上方。使用 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Split%20View.md">分屏视图</a> 时，为节省空间将只提供一个工具栏，它作用于活动笔记。

当前段落左侧的圆点序列仍作为拖动手柄显示：拖动它可以将段落、所有选中的段落，或选中的元素（如图片、表格或包含的笔记）移动到笔记中的其他位置。将其释放到第一个段落上方或最后一个段落下方，会将其移动到笔记的开头或末尾。单击或右键单击它会打开一个菜单，用于复制对该块的引用，参见 <a class="reference-link" href="Block%20references.md">块引用</a>。该菜单的最后一项 _删除_ 会删除拖动时会移动的块，而不要求确认；<kbd>Ctrl</kbd>+<kbd>Z</kbd> 可将它们恢复。将鼠标悬停在拖动手柄上会为它移动的块添加底纹，并且在其菜单打开期间这些块会保持底纹状态：在表格内，这是当前单元格中的段落，当选中多个单元格时，则是整个表格。菜单的标题是带底纹块的类型，例如 _段落_、_表格_ 或 _列表项_，当有多个带底纹块时则显示块的数量。对于段落以外的单个块，标题末尾的 <span class="tn-icon bx bx-help-circle"></span> 按钮会在笔记旁边的分屏中打开其类型的帮助页面。其第一组项目 _在上方插入_ 和 _在下方插入_ 列出了用于插入内容或将段落转换为其他块的 <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>，并将所选命令添加到带底纹块上方或下方的新段落中；当其中一项打开时输入可对其进行筛选。它们仅在斜杠命令开启时显示。对于列表项，则由 _在上方插入项_、_在下方插入项_ 和 _插入子项_ 取代它们的位置，并添加一个空项：在该项上方、在其及其嵌套项下方，或作为其第一个嵌套项。在表格单元格中，_在上方插入行_ 和 _在下方插入行_ 紧随其后。之后，_剪切_ 和 _复制_ 会将带底纹块放入剪贴板，_剪切_ 还会将其移除。配置 AI 提供商后，_AI 助手_ 紧随其后，其项目与工具栏的 <span class="tn-icon cke cke-trilium-ai"></span> 按钮相同，并且作用于带底纹块，而不是选中的文本，参见 <a class="reference-link" href="In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>。拖动手柄在移动端布局中不显示。

在空段落旁边，圆点会变成一个 <span class="tn-icon cke cke-plus"></span> 按钮。单击它会以菜单形式打开用于插入内容或将段落转换为其他块的 <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>，其顶部有一个用于筛选的输入框，右键单击它仍会打开该块的菜单。该按钮仅在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ → _功能_ → _斜杠命令_ 开启时显示。

<figure class="image"><img style="aspect-ratio:1440/60;" src="Formatting toolbar_image.png" width="1440" height="60"></figure>

默认情况下，如果工具栏无法在屏幕上完整显示，其余选项将在末尾归组为单个选项。可以通过勾选 _格式化工具栏_ 部分中的相应选项来在多行上显示项目。