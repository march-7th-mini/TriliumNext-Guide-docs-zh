# 笔记列表
<figure class="image"><img style="aspect-ratio:990/590;" src="Note List_image.png" width="990" height="590"></figure>

当一个笔记拥有一个或多个子笔记时，它们会列在笔记末尾，以便于导航。

## 配置

*   要隐藏特定笔记的笔记列表，只需应用 `hideChildrenOverview` [标签](../../Advanced%20Usage/Attributes.md)。
*   对于某些视图类型（如网格视图），出于性能考虑，只会显示部分笔记，并可使用分页来浏览全部笔记。要调整每页的笔记数量，请将 `pageSize` 设置为所需的数量。

## 视图类型

视图类型决定了子笔记的呈现方式。默认情况下，笔记将以网格形式显示，但也有一些其他视图类型可用。

通常，视图类型只能从<a class="reference-link" href="../../Collections/Collection%20Properties.md">集合属性</a>中更改，但也可以使用 `#viewType` [标签](../../Advanced%20Usage/Attributes/Labels.md)在任何类型的笔记上手动更改。

保存的搜索默认使用*搜索预览*：它将每个结果绘制为一张片段卡片，其中包含匹配的文本和属性。它仅限于搜索笔记，并在<a class="reference-link" href="../Navigation/Search.md">搜索</a>中描述。