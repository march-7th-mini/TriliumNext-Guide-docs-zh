# 笔记列表
<figure class="image"><img style="aspect-ratio:990/590;" src="Note List_image.png" width="990" height="590"></figure>

当一条笔记有一个或多个子笔记时，它们会列在笔记末尾，以便于导航。

## 配置

*   若要隐藏特定笔记的笔记列表，只需应用 `hideChildrenOverview` [标签](../../Advanced%20Usage/Attributes.md)。
*   对于某些视图类型，如网格视图，出于性能考虑，只会显示部分笔记，并可通过分页浏览全部笔记。若要调整每页笔记数量，请将 `pageSize` 设置为所需数值。

## 视图类型

视图类型决定了子笔记的呈现方式。默认情况下，笔记将以网格形式显示，但还有其他一些视图类型可供选择。

通常，视图类型只能在 <a class="reference-link" href="../../Collections.md">集合</a> 笔记中通过 <a class="reference-link" href="../UI%20Elements/Ribbon.md">功能区</a> 更改，但也可以在任何类型的笔记上使用 `#viewType` 属性手动更改。