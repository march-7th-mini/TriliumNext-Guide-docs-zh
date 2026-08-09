# 笔记图谱
<figure class="image image_resized" style="width:72.68%;"><img style="aspect-ratio:1311/1271;" src="Note Map_image.png" width="1311" height="1271"></figure>

笔记图谱是一种笔记类型，它展示了同名功能的独立版本：<a class="reference-link" href="../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记图谱（链接图谱，树状图谱）</a>。关于笔记图谱的工作原理及其显示内容，请参阅该页面。

创建后，笔记图谱将显示笔记之间的关系。只有属于笔记图谱父笔记（包括其子笔记）的笔记才会被显示。

## 根笔记

根笔记定义了图谱的起始点，关系和层级结构均由此派生。

共有三种可能的根笔记：

*   默认根笔记是笔记图谱的父笔记。
*   若要改用当前[提升的笔记](../Basic%20Concepts%20and%20Features/Navigation/Note%20Hoisting.md)，请将 `mapRootNoteId` 标签设置为 `hoisted`。
*   若要改用特定笔记，请将 `mapRootNoteId` 设置为所需笔记的<a class="reference-link" href="../Advanced%20Usage/Note%20ID.md">笔记 ID</a>。

## 自定义

可以使用以下<a class="reference-link" href="../Advanced%20Usage/Attributes/Labels.md">标签</a>自定义笔记图谱：

| 标签 | 描述 |
| --- | --- |
| `#mapIncludeRelation` | 以逗号分隔的关系名称列表，用于包含在笔记图谱中。 |
| `#mapExcludeRelation` | 以逗号分隔的关系名称列表，用于从笔记图谱中排除。 |
| `#mapRootNoteId` | 图谱根笔记的 ID，或 `hoisted`。有关更多信息，请参阅上面的根笔记部分。 |