# 关系图

关系图是一种笔记类型，用于可视化笔记及其[关系](../Advanced%20Usage/Attributes.md)。

## 交互

*   要创建新笔记并将其添加到面板上，请按<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>中的加号按钮。
    *   之后，点击地图上的任意位置将其放置在那里。
    *   该笔记将作为关系图的子笔记放置。
*   也可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中拖拽现有笔记。它将被放置在拖拽到的位置。
    *   也可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>拖拽多个笔记。这些笔记将被放置在拖拽位置附近，且不会重叠。
    *   被拖拽的笔记可以是关系图的子笔记，也可以位于任意位置。
*   要创建关系，请将鼠标按住笔记右侧的方框，然后：
    *   将其拖拽到另一个笔记上，创建从第一个笔记指向第二个笔记的关系。
    *   拖拽到同一个笔记上，创建自引用关系（以循环表示）。
    *   拖拽完成后，关系旁边会弹出一个浮窗，要求输入关系名称。输入新名称并按 <kbd>Enter</kbd>，或从建议中选择已在使用的关系名称。要取消，请按 <kbd>Esc</kbd>、关闭浮窗或点击地图上的其他位置。
*   要打开笔记，可以点击该笔记（在当前视图中打开），或使用右键菜单在新标签页中打开。
*   要编辑笔记标题或删除笔记（从地图中移除，或彻底删除），请右键点击该笔记。
*   要重命名或删除关系，请右键点击它并选择相应的选项。

## 开发过程演示

这是一个基本示例，展示如何使用关系图创建简单的图表：

<img src="Relation Map_relation-map-dev-process.png" width="934" height="667">

以下是如何创建它的过程：

<img src="Relation Map_relation-map-dev-process-demo.gif" width="812" height="585">

我们完全从零开始，首先创建一个名为“Development process”的新笔记，并将其类型更改为“关系图”。之后，我们逐一创建新笔记，并通过点击地图来放置它们。我们还拖拽笔记之间的[关系](../Advanced%20Usage/Attributes.md)并为其命名。就这么简单！

地图上的项目——“Specification”、“Development”、“Testing”和“Demo”——实际上是在“Development process”笔记下创建的笔记——你可以点击它们并编写一些内容。笔记之间的连接称为“[关系](../Advanced%20Usage/Attributes.md)”。

## 家族演示

这是一个使用了一些高级概念的更复杂的演示。生成的图表如下：

<img src="Relation Map_relation-map-family.png" width="941" height="758">

以下是如何实现它的过程：

<img src="Relation Map_relation-map-family-demo.gif" width="812" height="585">

这里有几个步骤：

*   我们从一个空的关系图和两个现有笔记开始，分别代表菲利普亲王和伊丽莎白二世女王。这两个笔记已经定义了 `isPartnerOf` [关系](../Advanced%20Usage/Attributes.md)。
    *   实际上有两个“反向”关系（一个从菲利普指向伊丽莎白，一个从伊丽莎白指向菲利普）
*   我们将两个笔记拖拽到关系图上，并放置到合适的位置。注意现有的 `isPartnerOf` 关系是如何显示的。
*   现在我们创建新笔记——将其命名为“Prince Charles”，并通过点击所需位置将其放置在关系图上。该笔记默认创建在关系图笔记之下（在左侧的笔记树中可见）。
*   我们创建两个新关系 `isChildOf`，分别指向菲利普和伊丽莎白
    *   现在出现了一些意想不到的情况——我们还可以看到显示另一个 `hasChild` 关系的关系。这是因为有一个[关系定义](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)，将 `isChildOf` 设为 `hasChildOf` 的“[反向](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)”关系（反之亦然），因此它是自动创建的。
*   我们为戴安娜王妃创建另一个笔记，并从查尔斯创建 `isPartnerOf` 关系。再次注意该关系如何具有双向箭头——这是因为 `isPartnerOf` 定义将其反向关系也指定为“isPartnerOf”，因此反向关系是自动创建的。
*   最后一步，我们平移和缩放地图，使其更好地适应窗口尺寸。

上述关系定义来自“Person template”笔记，该笔记被分配给“My Family Tree”关系笔记的任意子笔记。你可以在[演示笔记](../Advanced%20Usage/Database.md)中体验整个功能。

## 详情

你可以在 `displayRelations` 标签中用逗号分隔的关系名称来指定应显示哪些关系。

或者，你可以在 `hideRelations` 中指定逗号分隔的关系名称列表，这将显示所有关系，但标签中定义的关系除外。

## 另请参阅

*   <a class="reference-link" href="Note%20Map.md">笔记地图</a>是一个类似的概念。