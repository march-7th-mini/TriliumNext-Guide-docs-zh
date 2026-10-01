# 图标

图标就像[笔记图标](Icons.md)一样，可以插入到笔记内容中，包括来自任何其他[自定义图标包](../../../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md)的图标。

## 功能

*   图标可以通过<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>的<a class="reference-link" href="../General%20formatting.md">通用格式</a>工具进行格式化：
    *   前景色/图标颜色
    *   背景色/高亮
    *   字体大小
*   也支持自定义<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md">图标包</a>。
    *   对于表情符号，优先使用<a class="reference-link" href="../Insert%20buttons.md">插入按钮</a>中的表情符号功能。
*   当点击图标时，会出现一个浮动工具栏，具有以下功能：
    *   <span class="tn-icon bx bx-sticker"></span> 用于更改图标。
    *   <span class="tn-icon bx bx-reflect-horizontal"></span> 用于应用变换：旋转（90 / 180 / 270）和水平/垂直翻转。每个图标只能使用一种变换。

## 用途

*   应用内帮助/用户指南使用这些图标来说明界面中的按钮。
*   <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a> 导入器也将它们用于<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote/Tags.md">标签</a>。

## 插入图标

有两种方式可以插入图标：

*   通过<a class="reference-link" href="../Formatting%20toolbar.md">格式工具栏</a>，找到 <span class="tn-icon bx bx-plus"></span> 图标，然后点击 <span class="tn-icon bx bx-sticker"></span> 图标。
*   通过<a class="reference-link" href="../Slash%20Commands.md">斜杠命令</a>，输入 `/icon`。

将出现一个图标选择器，搜索图标并点击它以将其插入文档中。

## 通过图标查找笔记

图标可以被[搜索](../../../Basic%20Concepts%20and%20Features/Navigation/Search.md)。包含 <span class="tn-icon bx bx-star"></span> 图标的笔记可以通过搜索 `star` 或其 `iconClass`（`bx-star`）来找到。

要查找图标的名称，请在图标选择器中将鼠标悬停在图标上。

## Markdown 渲染

导出为 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md">Markdown</a> 时，该项将渲染为 Trilium 所使用的图标的原始 HTML 表示形式：

```html
<span class="tn-icon bx bx-star"></span>
```