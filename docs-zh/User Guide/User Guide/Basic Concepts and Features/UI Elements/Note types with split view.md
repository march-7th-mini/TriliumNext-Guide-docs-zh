# 支持分屏视图的笔记类型
分屏视图是 <a class="reference-link" href="../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a> 和 <a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a> 笔记的一项功能，它在一侧显示源代码，在另一侧显示内容预览。

<a class="reference-link" href="../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a> 还允许在水平或垂直分屏之间切换，以适应各种尺寸的图表。

## 显示模式与交互

分屏附带三种不同的显示模式，可从 <a class="reference-link" href="Note%20buttons.md">笔记按钮</a> 区域进行切换：

*   <span class="tn-icon bx bxs-dock-left"></span> _（分屏视图）_，其中一侧可编辑源代码，另一侧显示预览。
    *   在此模式下，可以通过拖动源代码窗格与预览窗格之间的小边框来调整任一窗格的大小。
*   <span class="tn-icon bx bx-code"></span> _（源代码视图）_，在整个屏幕上显示源代码，提供更专注的编辑体验。
*   <span class="tn-icon bx bx-show"></span> _（预览）_，仅全屏显示图表或文本的渲染结果，尤其适用于只读笔记。

显示模式存储在笔记级别。

## 与只读笔记的关系

如果笔记被标记为[只读](../Notes/Read-Only%20Notes.md)，源代码视图将不可编辑。在预览模式下，将笔记标记为只读没有效果，因为预览本身不可编辑。