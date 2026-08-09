# 关系图谱

关系图谱是一种[笔记](../Advanced%20Usage/Attributes.md)类型，用于可视化笔记及其[关系](../Advanced%20Usage/Attributes.md)。

## 交互操作

*   要创建新笔记并将其添加到画布上，请按下<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>中的加号按钮。
    *   然后，点击图谱上的任意位置即可将其放置在那里。
    *   该笔记将作为图谱的子笔记被放置。
*   也可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中拖拽现有笔记。它将放置在拖拽到的位置。
    *   也可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>拖拽多个笔记。这些笔记将放置在拖拽位置附近，且不会重叠。
    *   被拖拽的笔记可以是图谱的子笔记，也可以位于任意位置。
*   要创建关系，请按住笔记右侧的方框，然后：
    *   将其拖拽到另一个笔记上，以创建从第一个笔记指向第二个笔记的关系。
    *   拖拽到同一个笔记上，以创建自引用关系（显示为循环）。
    *   拖拽完成后，输入要创建的关系名称。要取消，只需关闭对话框或按 <kbd>Esc</kbd> 键。
*   要打开笔记，可以点击该笔记（在当前视图中打开），或使用右键菜单在新标签页中打开。
*   要编辑笔记标题或删除笔记（无论是从图谱中删除，还是完全删除），请右键点击该笔记。
*   要删除关系，请右键点击它并选择相应选项。

## 开发流程演示

以下是一个基本示例，展示如何使用关系图谱创建简单图表：

<img src="Relation Map_relation-map-dev-process.png" width="934" height="667">

以下是创建它的方法：

<img src="Relation Map_relation-map-dev-process-demo.gif" width="812" height="585">

我们完全从零开始，首先创建一个名为“开发流程”的新笔记，并将其类型更改为“关系图谱”。之后，我们逐个创建新笔记，并通过点击图谱来放置它们。我们还在笔记之间拖拽[关系](../Advanced%20Usage/Attributes.md)并为其命名。就这样！

图谱上的项目——“规格说明”、“开发”、“测试”和“演示”——实际上是在“开发流程”笔记下创建的笔记——您可以点击它们并编写一些内容。笔记之间的连接称为“[关系](../Advanced%20Usage/Attributes.md)”。

## 家庭演示

这是一个使用一些高级概念的更复杂的演示。生成的图表如下：

<img src="Relation Map_relation-map-family.png" width="941" height="758">

以下是创建它的方法：

<img src="Relation Map_relation-map-family-demo.gif" width="812" height="585">

这里有几个步骤：

*   我们从空的关系图谱和两个代表菲利普亲王和伊丽莎白二世女王的现有笔记开始。这两个笔记已经定义了 `isPartnerOf` [关系](../Advanced%20Usage/Attributes.md)。
    *   实际上有两个“反向”关系（一个从菲利普到伊丽莎白，另一个从伊丽莎白到菲利普）。
*   我们将两个笔记拖拽到关系图谱上，并放置在合适的位置。注意现有的 `isPartnerOf` 关系是如何显示的。
*   现在我们创建新笔记——我们将其命名为“查尔斯王子”，并通过点击所需位置将其放置在关系图谱上。该笔记默认在关系图谱笔记下创建（在左侧的笔记树中可见）。
*   我们创建两个新的 `isChildOf` 关系，分别指向菲利普和伊丽莎白。
    *   现在有一些意想不到的事情——我们还可以看到显示另一个 `hasChild` 关系。这是因为有一个[关系定义](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)将 `isChildOf` 设置为 `hasChildOf` 的“[反向](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)”关系（反之亦然），因此它会自动创建。
*   我们为戴安娜王妃创建另一个笔记，并从查尔斯创建 `isPartnerOf` 关系。再次注意关系如何具有双向箭头——这是因为 `isPartnerOf` 定义将其反向关系指定为同样是“isPartnerOf”，因此相反的关系会自动创建。
*   作为最后一步，我们平移和缩放图谱以更好地适应窗口尺寸。

上述关系定义来自“人物模板”笔记，该笔记分配给“我的家谱”关系笔记的任何子笔记。您可以在[演示笔记](../Advanced%20Usage/Database.md)中体验整个功能。

## 详细信息

您可以在 `displayRelations` 标签中指定应显示哪些关系，使用逗号分隔的关系名称。

或者，您可以在 `hideRelations` 中指定逗号分隔的关系名称列表，这将显示所有关系，但标签中定义的关系除外。

## 另请参阅

*   <a class="reference-link" href="Note%20Map.md">笔记地图</a>是一个类似的概念。