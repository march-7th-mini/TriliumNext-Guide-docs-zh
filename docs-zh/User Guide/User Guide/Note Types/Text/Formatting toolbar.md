# 格式化工具栏
Trilium 根据你的偏好，为文本笔记提供两种不同的编辑体验。

可以通过前往 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>，然后查找 <a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a> 部分来更改格式化工具栏的类型。在其中，查找 _格式化工具栏_ 类别。

## 浮动式

浮动栏是一种更简约的选项，其中格式化功能隐藏在两种不同的弹出窗口中。

### 块级弹出窗口

第一个弹出窗口是块级弹出窗口。它会以一系列圆点的形式出现在你当前正在编辑的段落左侧：
![](Formatting%20toolbar_image.jpg)

点击此弹出窗口将显示特定于整个段落的格式化选项，例如设置标题、列表、表格等。

这些圆点同时也是拖动手柄：拖动它们可以将段落、所有选中的段落，或选中的元素（如图片、表格或包含的笔记）移动到笔记中的其他位置。右键单击它们会复制该段落或所选段落的引用，参见 <a class="reference-link" href="Block%20references.md">块引用</a>。

<figure class="image"><img style="aspect-ratio:1404/156;" src="2_Formatting toolbar_image.png" width="1404" height="156"></figure>

### 行内弹出窗口

行内弹出窗口会在选中文本时自动出现：

<figure class="image"><img style="aspect-ratio:1008/154;" src="1_Formatting toolbar_image.png" width="1008" height="154"></figure>

此处的所有选项仅适用于选中的文本部分，例如更改字体大小或将文本加粗。

## 固定式

固定式格式化提供了一种更传统的编辑范式，通常在需要大量格式化时很有用。

所有选项都组合到一个工具栏中，该工具栏会显示在笔记上方。使用 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Split%20View.md">分屏视图</a> 时，为了节省空间将只提供一个工具栏，它作用于当前活动的笔记。

当前段落左侧的圆点序列仍然会显示，但仅作为拖动手柄：拖动它可以将段落、所有选中的段落，或选中的元素（如图片、表格或包含的笔记）移动到笔记中的其他位置。点击它不会打开弹出窗口，右键单击它会复制该块的引用，参见 <a class="reference-link" href="Block%20references.md">块引用</a>。拖动手柄在移动端布局中不显示。

<figure class="image"><img style="aspect-ratio:1440/60;" src="Formatting toolbar_image.png" width="1440" height="60"></figure>

默认情况下，如果工具栏无法在屏幕上完整显示，其余选项将被归组到末尾的单个选项中。通过在 _格式化工具栏_ 部分勾选相应的选项，可以将项目显示在多行上。