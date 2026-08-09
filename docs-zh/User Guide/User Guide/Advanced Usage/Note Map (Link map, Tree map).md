# 笔记图谱（链接图谱、树状图谱）

笔记图谱是笔记之间连接的可视化呈现。这有助于洞察笔记的结构（“网络”）。

笔记图谱有两种类型：

*   链接图谱，展示笔记之间的关系。
*   笔记图谱，展示层级树状结构。

## 访问笔记图谱

笔记图谱有多种访问方式：

*   访问当前笔记的笔记图谱：
    *   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>中，笔记图谱位于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Connections%20tab.md">连接选项卡</a>内的<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中。
    *   在旧布局中，笔记图谱是<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>中的一个选项卡。
*   要显示全屏笔记图谱，有一个同名的[专用笔记类型](../Note%20Types/Note%20Map.md)。
*   要查看全局笔记图谱（知识库中所有笔记的图谱），在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中有一个专用的 _笔记图谱_ 按钮。

## 术语和结构

*   每个笔记在图中表示为一个 _节点_，标题显示在下方。
    *   当地图缩小时，仍可通过将鼠标悬停在节点上来查看标题。
    *   笔记的[图标和颜色](../Basic%20Concepts%20and%20Features/Notes/Note%20Icons%20%26%20Colors.md)会被保留。
*   根节点是显示关系和层级结构的参考点。
    *   通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>或<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>（新布局）访问笔记图谱时，根节点是当前笔记。
    *   使用专用的<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记图谱</a>笔记时，根笔记可以是父笔记、当前[提升](../Basic%20Concepts%20and%20Features/Navigation/Note%20Hoisting.md)的笔记或特定笔记。有关更多信息，请参阅笔记类型文档。

## 交互

*   节点可以拖动，但释放后会回到原始位置。
    *   要使笔记保持在拖动后的位置，请按 _固定节点_ 按钮。笔记的位置不会被保存，因此一旦导航到另一个笔记或重新启动应用程序，它将恢复正常。
*   将鼠标悬停在节点上时，相邻的关系和节点会高亮显示。
*   节点之间的距离可以通过左下角的滑块进行调整。同样，此值不会被保存。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Archived%20Notes.md">已归档笔记</a>通常会被笔记图谱忽略，以减少杂乱。有一个例外：如果根笔记也已归档，则所有已归档的笔记也会显示。

## 链接图谱

<img src="Note Map (Link map, Tree map)_image.png" width="1425" height="1093">

链接图谱是特定笔记的传入和传出链接及<a class="reference-link" href="Attributes/Relations.md">关系</a>的可视化呈现。

该图谱指示以下类型的关系：

*   笔记之间的<a class="reference-link" href="../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
*   <a class="reference-link" href="Attributes/Relations.md">关系</a>

链接图谱还会将层级结构中未链接的笔记显示为一团未连接的圆点。在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>中，侧边栏为了节省空间会刻意省略这些内容，但当地图最大化时它们会显示出来。

## 树状图谱

显示笔记的层级图谱：

<figure class="image"><img style="aspect-ratio:1420/1490;" src="1_Note Map (Link map, Tree map)_image.png" width="1420" height="1490"></figure>

## 另请参阅

*   除了可以从任何笔记访问的笔记图谱功能外，还可以创建一个专用笔记来全屏显示关系。有关更多信息，请参阅<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记图谱</a>。
*   <a class="reference-link" href="../Note%20Types/Relation%20Map.md">关系图谱</a>是一个类似的概念，但有一些区别：
    *   笔记图谱是自动生成的，而关系图谱必须手动创建
    *   关系图谱是一种笔记类型，而链接图谱只是虚拟的可视化