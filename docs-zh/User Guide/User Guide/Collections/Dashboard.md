# 仪表板
<figure class="image"><img style="aspect-ratio:1406/1030;" src="Dashboard_image.png" width="1406" height="1030"></figure>

> [!NOTE]
> 仪表板目前被视为测试版。这意味着在稳定之前，其行为可能会发生一些变化。

仪表板是 Trilium v0.104.0 中引入的一种集合。它类似于 <a class="reference-link" href="Grid%20View.md">网格视图</a> 集合，但有一些关键区别：

*   网格布局不是固定的，允许不同宽度和高度的磁贴。网格有 12 列和无限行数。
*   每个小组件代表集合的一个子笔记，可以重新排序或调整大小。
*   网格会均匀分配列以填满整个屏幕。
    *   如果可用空间太小（例如在分屏或移动端），列会被折叠，使所有小组件一个接一个地显示。
    *   当列被折叠时，小组件无法重新排序或调整大小。
*   与 <a class="reference-link" href="Grid%20View.md">网格视图</a> 不同，小组件不可点击，这使得它们可以交互。

## 小组件类型

仪表板使用与 <a class="reference-link" href="Grid%20View.md">网格视图</a> 或 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a> 相同的渲染机制，这意味着每个笔记都可以被渲染，例如：

*   静态内容，通过 <a class="reference-link" href="../Note%20Types/Text.md">文本</a> 或 <a class="reference-link" href="../Note%20Types/Code.md">代码</a>。
*   图片，通过 <a class="reference-link" href="../Note%20Types/File.md">文件</a>、<a class="reference-link" href="../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>、<a class="reference-link" href="../Note%20Types/Mind%20Map.md">思维导图</a>。
*   交互式小组件，通过 <a class="reference-link" href="../Note%20Types/Render%20Note.md">渲染笔记</a>。
*   网页可以通过 <a class="reference-link" href="../Note%20Types/Web%20View.md">网页视图</a> 显示，并通过上下文菜单刷新。
*   <a class="reference-link" href="../Collections.md">集合</a> 在仪表板内以交互方式渲染

> [!TIP]
> 通过使用 <a class="reference-link" href="../Note%20Types/Render%20Note.md">渲染笔记</a> 实现交互式小组件是仪表板的突出用例。使用 <a class="reference-link" href="../AI.md">AI</a> 对话，这些小组件可以轻松创建，因为 AI 被指示了如何编写它们。

## 添加新小组件

有两种方式可以向仪表板添加小组件：

*   创建任意类型的子笔记，仪表板会自动拾取它并将其添加到网格上。
*   从 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中，将现有笔记拖到仪表板上，它将被放置在那里。这会将笔记[克隆](../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)到集合中。

## 只读仪表板

在[只读](../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)仪表板上，小组件无法移动或调整大小，从 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 拖来的笔记不会被添加，小组件的菜单也不再提供移除选项。