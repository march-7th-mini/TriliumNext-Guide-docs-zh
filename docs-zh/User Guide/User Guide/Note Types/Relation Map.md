# 关系图

关系图是一种笔记类型，用于可视化笔记及其[关系](../Advanced%20Usage/Attributes.md)。

## 交互

*   要创建新笔记并将其添加到图中，请按图底部的 <span class="tn-icon bx bx-note"></span> _添加笔记_ 按钮，然后单击图上任意位置将其放置在那里。
    *   当图等待点击时，一个半透明框会跟随鼠标以显示笔记将放置的位置。要取消，请再次按该按钮（此时标签为 _取消_）或按 <kbd>Esc</kbd>。
    *   该笔记作为图的子笔记创建，使用新笔记的默认标题。它会在笔记面板（见下文）中打开，标题处于选中状态，因此你可以直接输入其名称。
*   现有笔记也可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中拖拽。它将被放置在拖拽到的位置。
    *   也可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>拖拽多个笔记。这些笔记将被放置在拖拽位置附近，且不会重叠。
    *   被拖拽的笔记可以是图的子笔记，也可以位于任意位置。
*   笔记也可以粘贴到图上。在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中复制或剪切它们，然后单击图并按 <kbd>Ctrl</kbd>+<kbd>V</kbd>，或右键单击图的空白部分并选择 _粘贴笔记_。
    *   使用 <kbd>Ctrl</kbd>+<kbd>V</kbd> 时，笔记被放置在鼠标下方；如果鼠标不在图上，则放置在图的中央。从右键菜单中，它们被放置在菜单打开的位置。
    *   复制的笔记保留在树中的原位置。剪切的笔记被移动到图下，就像它们在树中被粘贴到图中一样。
    *   指向笔记的链接，例如从文本笔记复制的<a class="reference-link" href="Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>，也可以用同样的方式粘贴。如果剪贴板中没有指向笔记的链接，则粘贴最近在树中复制或剪切的笔记。
    *   图空白部分的右键菜单也有 _添加笔记_，它会在菜单打开的位置创建新笔记。
*   要创建关系，请将鼠标按住笔记右侧的圆点，然后：
    *   将其拖到另一个笔记上，以创建从第一个笔记指向第二个笔记的关系。
    *   拖到同一个笔记上，以创建自引用关系（表示为循环）。
    *   拖拽后，关系旁边会弹出一个浮层询问其名称。输入新名称并按 <kbd>Enter</kbd>，或从建议中选择已在使用的关系名称。要取消，请按 <kbd>Esc</kbd>、关闭浮层或单击图上其他位置。
*   每个笔记显示为带有其图标和标题的卡片，颜色与<a class="reference-link" href="../Collections/Kanban%20Board.md">看板</a>的卡片一样使用笔记的颜色。
*   将鼠标悬停在笔记上会高亮其关系（如果笔记有颜色，则使用笔记的颜色），并淡化其他关系。
*   要查看或编辑笔记，请在图上单击它。这会打开笔记面板（见下文）。
    *   要在新标签页中打开笔记，请 <kbd>Ctrl</kbd>+单击它或用鼠标中键单击它。<kbd>Shift</kbd>+单击会在新窗口中打开它。右键菜单提供相同的选项。
*   要编辑笔记的标题、更改其颜色或删除它（从图中移除，或完全删除），请右键单击该笔记。
*   要重命名或删除关系，请右键单击它并选择相应选项。
*   在[只读](../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)图上，笔记无法移动，关系无法绘制、重命名或删除。笔记的右键菜单仅提供打开选项，关系没有右键菜单。
*   要在图中移动，请拖拽图的空白部分，并使用鼠标滚轮或右下角的 <span class="tn-icon bx bx-minus-circle"></span> 和 <span class="tn-icon bx bx-plus-circle"></span> 按钮进行缩放。单击缩放百分比可回到 100%，<span class="tn-icon bx bx-scan"></span> _适应视图_ 会缩放和平移，使所有笔记都可见。
    *   单击图后，方向键或 <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> 可平移，<kbd>+</kbd> 和 <kbd>-</kbd> 可缩放。图右上角的 <kbd>?</kbd> 按钮列出了所有键盘快捷键。

## 笔记面板

当单击图上的笔记时，图右侧会打开一个面板，并且该笔记被高亮显示。如果面板会覆盖笔记，或笔记部分在屏幕外，图会平移以将其带入视图。面板包含：

*   笔记的标题和图标，两者均可编辑。
*   一个 <span class="tn-icon bx bx-expand-alt"></span> 按钮，用于将面板展开到整个图上，以及之后恢复。
*   与笔记交互的按钮：
    *   <span class="tn-icon bx bx-log-in"></span> 在当前标签页中打开笔记，或通过 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 菜单在新标签页、分屏、窗口或快速编辑弹出框中打开。
    *   一个 <span class="tn-icon bx bx-palette"></span> 颜色选择器，用于更改笔记的颜色。
    *   一个 <span class="tn-icon bx bx-trash"></span> 按钮，用于从图中移除笔记，也可以选择同时删除该笔记。
*   笔记的<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>（如果有）。
*   笔记的内容，可以直接从面板中编辑。

如果图是只读的，则不会显示颜色选择器和移除按钮。

单击图上的另一个笔记会将面板切换到该笔记。同样，单击面板内的<a class="reference-link" href="Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>会将面板切换到该笔记，只要它在图上。

要关闭面板，请按面板右上角的 <span class="tn-icon bx bx-x"></span> 按钮、单击图的空白部分或按 <kbd>Esc</kbd>。

在移动端，笔记会作为覆盖整个屏幕的对话框打开，而不是面板。

## 开发过程演示

这是一个基本示例，展示如何使用关系图创建简单的图表：

<img src="Relation Map_relation-map-dev-process.png" width="934" height="667">

而这是创建它的方法：

<img src="Relation Map_relation-map-dev-process-demo.gif" width="812" height="585">

我们完全从零开始，首先创建一个名为“开发过程”的新笔记，并将其类型更改为“关系图”。之后，我们逐个创建新笔记，并通过单击图来放置它们。我们还拖拽笔记之间的[关系](../Advanced%20Usage/Attributes.md)并为其命名。就这样！

图上的项目——“规格说明”、“开发”、“测试”和“演示”——实际上是在“开发过程”笔记下创建的笔记——你可以单击它们并编写一些内容。笔记之间的连接称为“[关系](../Advanced%20Usage/Attributes.md)”。

## 家族演示

这是一个使用了一些高级概念的更复杂的演示。生成的图表如下：

<img src="Relation Map_relation-map-family.png" width="941" height="758">

而这是达到它的方法：

<img src="Relation Map_relation-map-family-demo.gif" width="812" height="585">

这里有以下几个步骤：

*   我们从一个空的关系图和两个现有笔记开始，分别代表菲利普亲王和伊丽莎白二世女王。这两个笔记已经定义了 `isPartnerOf` [关系](../Advanced%20Usage/Attributes.md)。
    *   实际上有两个“反向”关系（一个从菲利普到伊丽莎白，一个从伊丽莎白到菲利普）
*   我们将两个笔记拖到关系图上并放置到合适的位置。注意现有的 `isPartnerOf` 关系是如何显示的。
*   现在我们创建新笔记——将其命名为“查尔斯王子”，并通过单击所需位置将其放置在关系图上。该笔记默认在关系图笔记下创建（在左侧的笔记树中可见）。
*   我们创建两个新关系 `isChildOf`，分别指向菲利普和伊丽莎白
    *   现在有一些意想不到的事情——我们还可以看到显示另一个 `hasChild` 关系的关系。这是因为有一个[关系定义](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)，它将 `isChildOf` 作为 `hasChildOf` 的“[反向](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)”关系（反之亦然），因此它是自动创建的。
*   我们为戴安娜王妃创建另一个笔记，并从查尔斯创建 `isPartnerOf` 关系。再次注意该关系如何具有双向箭头——这是因为 `isPartnerOf` 定义将其反向关系再次指定为“isPartnerOf”，因此相反的关系是自动创建的。
*   作为最后一步，我们平移和缩放图以更好地适应窗口尺寸。

上面提到的关系定义来自“人物模板”笔记，该笔记被分配给“我的家谱”关系笔记的任何子笔记。你可以在[演示笔记](../Advanced%20Usage/Database.md)中体验整个内容。

## 详情

你可以在 `displayRelations` 标签中使用逗号分隔的关系名称来指定应显示哪些关系。

或者，你可以在 `hideRelations` 中指定逗号分隔的关系名称列表，这将显示所有关系，但标签中定义的关系除外。

## 另请参阅

*   <a class="reference-link" href="Note%20Map.md">笔记地图</a> 是一个类似的概念。