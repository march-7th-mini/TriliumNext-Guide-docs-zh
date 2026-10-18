# 连接标签页
<figure class="image image-style-align-right image_resized" style="width:33.35%;"><img style="aspect-ratio:490/1801;" src="Connections tab_image.png" width="490" height="1801"></figure>

连接标签页将当前笔记的所有信息及其与其他笔记的关系分组为四个不同的部分。

> [!NOTE]
> 通常最好只展开所需的部分，因为每个部分都需要检索可能原本不需要的额外数据。折叠时，这些部分不会检索任何额外数据。

## 笔记地图

笔记地图显示一个图表，展示当前笔记与层级结构中其他笔记之间的关系。有两种可视化类型，可从该部分的右上角进行选择：

*   _链接地图_（<span class="tn-icon bx bx-network-chart"></span>），显示笔记之间的[关系](../../../Advanced%20Usage/Attributes/Relations.md)。
*   _树状地图_（<span class="tn-icon bx bx-sitemap"></span>），显示层级结构。

侧边栏将记住所选的可视化类型，作为全局选项。请注意，笔记地图也有一个 `#mapType` 属性来描述使用哪种可视化类型，但侧边栏有意忽略它，以便在切换笔记时保持一致。

地图还可以通过按该部分右上角的 <span class="tn-icon bx bx-expand-alt"></span> 按钮来展开。展开时，地图会显示在单独的对话框中。或者，可以折叠所有其他部分，这将使笔记地图更高，并且可以拖动侧边栏以获得更多的横向空间。

侧边栏内的笔记地图视图为了适应空间而有意更加紧凑：链接地图还会显示层级结构中没有链接到当前笔记的笔记（形成一片点云），但这仅在展开地图时显示。同样，链接强度和固定配置按钮在此处不显示。

另请参阅：

*   <a class="reference-link" href="../../../Note%20Types/Note%20Map.md">笔记地图</a> 笔记类型
*   <a class="reference-link" href="../../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记地图（链接地图、树状地图）</a> 了解关于该概念的更多信息。

## 笔记路径

笔记路径部分显示当前笔记被[克隆](../../Notes/Cloning%20Notes.md)的位置。笔记路径的每一段都是可点击的，以便导航到该笔记或克隆。根笔记显示为其图标，与<a class="reference-link" href="../Breadcrumb.md">面包屑导航</a>中相同；悬停在其上会显示其标题。

可以通过右上角的 <span class="tn-icon bx bx-duplicate"></span> 按钮创建新的克隆。

## 反链

反链列出引用当前笔记的笔记，以及引用该笔记处的内容预览。

更多信息，请参阅<a class="reference-link" href="../../../Note%20Types/Text/Links/Backlinks.md">反链</a>。

## 相似笔记

显示基于笔记内容及其属性而看起来相似的笔记列表。更多信息，请参阅<a class="reference-link" href="../../Navigation/Similar%20Notes.md">相似笔记</a>。