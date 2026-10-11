# 笔记地图（链接图、树状图）
笔记地图是笔记之间连接的可视化呈现。这提供了对笔记结构（“网络”）的洞察。

笔记地图有两种类型：

*   链接图，显示笔记之间的关系。
*   笔记地图，显示层级树状结构。

## 访问笔记地图

笔记地图有多种形式：

*   笔记地图可在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中的<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>的_笔记地图_部分中找到。
    *   也可以通过前往<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a> → _笔记地图_来访问，这会将侧边栏聚焦到右侧部分。
*   要显示全屏笔记地图，有一个同名的[专用笔记类型](../Note%20Types/Note%20Map.md)。
*   要查看全局笔记地图（知识库中所有笔记的），在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中有一个专用的_笔记地图_按钮。

## 术语和结构

*   每个笔记在图中表示为一个_节点_，标题显示在下方。
    *   当地图缩小时，仍可通过悬停在节点上查看标题。
    *   笔记的[图标和颜色](../Basic%20Concepts%20and%20Features/Notes/Note%20Icons%20%26%20Colors.md)会被保留。
*   根节点是显示关系和层级结构的参考点。
    *   当通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>访问笔记地图时，根节点是当前笔记。
    *   当使用专用的<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记地图</a>笔记时，根笔记可以是父笔记、当前[提升](../Basic%20Concepts%20and%20Features/Navigation/Note%20Hoisting.md)的笔记或特定笔记。有关更多信息，请参阅笔记类型文档。

## 交互

*   节点可以拖动，但释放后会回到原始位置。
    *   要让笔记保持在拖动后的位置，请按_固定节点_按钮。笔记的位置不会被保存，因此当您导航到另一个笔记或重启应用程序后，它会恢复正常。
*   当悬停在节点上时，相邻的关系和节点会高亮显示。
*   节点之间的距离可以通过左下角的滑块调整。同样，此值不会被保存。
*   要缩放，请使用鼠标滚轮、在触摸屏上捏合，或按右下角的 <span class="tn-icon bx bx-plus-circle"></span> 和 <span class="tn-icon bx bx-minus-circle"></span> 按钮。
    *   要将整个地图重新纳入视图，请按它们旁边的 <span class="tn-icon bx bx-scan"></span> _适应视图_按钮。
    *   缩放按钮不会在移动端显示，在移动端通过捏合来缩放。_适应视图_按钮始终显示。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Archived%20Notes.md">存档笔记</a>通常会被笔记地图忽略以减少杂乱。有一个例外：如果根笔记也是已归档的，那么所有已归档的笔记也会显示。

## 链接图

<img src="Note Map (Link map, Tree map)_image.png" width="1425" height="1093">

链接图是特定笔记的传入和传出链接及<a class="reference-link" href="Attributes/Relations.md">关系</a>的可视化。

该图表示以下类型的关系：

*   笔记之间的<a class="reference-link" href="../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
*   <a class="reference-link" href="Attributes/Relations.md">关系</a>

链接图还会将属于层级结构一部分的未链接笔记显示为一团未连接的圆点。在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中故意省略了这一点以节省空间，但当地图最大化时它们会显示出来。

## 树状图

显示笔记的层级地图：

<figure class="image"><img style="aspect-ratio:1420/1490;" src="1_Note Map (Link map, Tree map)_image.png" width="1420" height="1490"></figure>

## 另请参阅

*   除了可以从任何笔记访问的笔记地图功能外，还可以创建一个专用笔记来全屏显示关系。有关更多信息，请参阅<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记地图</a>。
*   <a class="reference-link" href="../Note%20Types/Relation%20Map.md">关系图</a>是一个类似的概念，但有一些区别：
    *   笔记地图是自动生成的，而关系图必须手动创建
    *   关系图是一种笔记类型，而链接图只是虚拟可视化