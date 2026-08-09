# 连接标签页
<figure class="image image-style-align-right image_resized" style="width:33.35%;"><img style="aspect-ratio:490/1801;" src="Connections tab_image.png" width="490" height="1801"></figure>

连接标签页将当前笔记及其与其他笔记关联的所有信息集中展示在四个不同的部分中。

> [!NOTE]
> 通常最好只展开需要查看的部分，因为每个部分都需要检索额外的数据，而这些数据在其他情况下可能并不需要。折叠时，这些部分不会检索任何额外数据。

## 笔记图谱

笔记图谱显示一个图形，展示当前笔记与层级结构中其他笔记之间的关系。有两种可视化类型，可从该部分右上角选择：

*   _链接图谱_，显示笔记之间的[关系](../../../Advanced%20Usage/Attributes/Relations.md)。
*   _树状图谱_，显示层级结构。

侧边栏会记住选择的可视化类型，作为全局选项。请注意，笔记图谱也有一个 `#mapType` 属性用于描述使用哪种可视化类型，但侧边栏有意忽略该属性，以在切换笔记时保持一致性。

点击该部分右上角的按钮也可以展开图谱。展开后，图谱会显示在单独的对话框中。或者，可以折叠所有其他部分，这样笔记图谱会变得更高，侧边栏也可以拖动以获得更多横向空间。

侧边栏内的笔记图谱视图有意做得更紧凑以适应空间：链接图谱也会显示层级结构中与当前笔记没有链接的笔记（形成点云），但这仅在图谱展开时显示。同样，链接强度和固定配置按钮也不在此处显示。

另请参阅：

*   <a class="reference-link" href="../../../Note%20Types/Note%20Map.md">笔记图谱</a> 笔记类型
*   <a class="reference-link" href="../../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记图谱（链接图谱、树状图谱）</a> 了解整体概念的更多信息。

## 笔记路径

笔记路径部分显示当前笔记被[克隆](../../Notes/Cloning%20Notes.md)的位置。笔记路径的每一段都可以点击，以便导航到该笔记或克隆。

可以从右上角的按钮创建新的克隆。

## 反链

反链列出引用当前笔记的笔记，以及引用该笔记的内容预览。

更多信息，请参阅 <a class="reference-link" href="../../../Note%20Types/Text/Links/Backlinks.md">反链</a>。

## 相似笔记

显示基于笔记内容及其属性而看起来相似的笔记列表。更多信息，请参阅 <a class="reference-link" href="../../Navigation/Similar%20Notes.md">相似笔记</a>。