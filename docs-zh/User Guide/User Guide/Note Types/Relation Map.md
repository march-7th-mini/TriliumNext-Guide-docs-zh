# 关系图

关系图是一种笔记类型，用于可视化笔记及其[关系](../Advanced%20Usage/Attributes.md)。

## 交互

*   要创建新笔记并将其添加到图中，请按图底部的 <span class="tn-icon bx bx-note"></span> _添加笔记_ 按钮，然后在图上任意位置点击以将其放置在那里。
    *   当图等待点击时，一个半透明的框会跟随鼠标，显示笔记将被放置的位置。要取消，请再次按下按钮（此时标签为 _取消_）或按 <kbd>Esc</kbd>。
    *   该笔记将作为图的子笔记创建，使用新笔记的默认标题。它会在笔记面板中打开（见下文），标题处于选中状态，因此你可以直接输入名称。
*   现有笔记也可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中拖入。它将被放置在拖放的位置。
    *   也可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>拖入多个笔记。这些笔记将被放置在拖放位置附近，且不会重叠。
    *   被拖入的笔记可以是图的子笔记，也可以位于任意位置。
*   笔记也可以粘贴到图上。在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中复制或剪切它们，然后点击图并按 <kbd>Ctrl</kbd>+<kbd>V</kbd>，或右键点击图的空白部分并选择 _粘贴笔记_。
    *   使用 <kbd>Ctrl</kbd>+<kbd>V</kbd> 时，笔记会被放置在鼠标下方；如果鼠标不在图上，则放置在图的中央。通过右键菜单，它们会被放置在菜单打开的位置。
    *   复制的笔记在笔记树中保持原位。剪切的笔记会被移动到图下，就像它们在笔记树中被粘贴到图中一样。
    *   指向笔记的链接，例如从文本笔记中复制的<a class="reference-link" href="Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>，也可以用同样的方式粘贴。如果剪贴板中没有指向笔记的链接，则会粘贴最近在笔记树中复制或剪切的笔记。
    *   图空白部分的右键菜单也有 _添加笔记_，会在菜单打开的位置创建新笔记。
*   要创建关系，请将鼠标按住笔记右侧的圆点，然后：
    *   将其拖到另一条笔记上，创建从第一条笔记指向第二条笔记的关系。
    *   拖到同一条笔记上，创建自引用关系（表示为循环）。
    *   拖动后，关系旁边会弹出一个浮层，要求输入关系名称。输入新名称并按 <kbd>Enter</kbd>，或从建议中选择已在使用的关系名称。要取消，请按 <kbd>Esc</kbd>、关闭浮层或点击图上的其他位置。
*   每条笔记显示为一张带有图标和标题的卡片，颜色使用笔记的颜色，与<a class="reference-link" href="../Collections/Kanban%20Board.md">看板</a>的卡片相同。
*   将鼠标悬停在笔记上会高亮显示其关系，如果笔记有颜色则使用笔记的颜色，其他关系则淡出。
*   要查看或编辑笔记，请在图上点击它。这会打开笔记面板（见下文）。
    *   要在新标签页中打开笔记，请 <kbd>Ctrl</kbd>+点击它，或用鼠标中键点击它。<kbd>Shift</kbd>+点击会在新窗口中打开它。右键菜单提供相同的选项。
*   要编辑笔记的标题、更改其颜色或删除它（从图中移除，或彻底删除），请右键点击该笔记。
*   要重命名或删除关系，请右键点击它并选择相应的选项。
*   在[只读](../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)图上，笔记无法移动，关系无法绘制、重命名或删除。笔记的右键菜单只提供打开选项，关系没有右键菜单。
*   要在图中移动，请拖动图的空白部分，并使用鼠标滚轮或右下角的按钮进行缩放。点击缩放百分比会回到 100%，<span class="tn-icon bx bx-scan"></span> _适应视图_ 会缩放和平移，使所有笔记都可见。
    *   点击图后，方向键或 <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> 可以平移，<kbd>+</kbd> 和 <kbd>-</kbd> 可以缩放。图右上角的 <kbd>?</kbd> 按钮列出了所有键盘快捷键。

## 笔记面板

当点击图上的笔记时，图右侧会打开一个面板，该笔记会被高亮显示。如果面板会遮挡笔记，或笔记部分在屏幕外，图会平移以将其带入视图。面板包含：

*   笔记的标题和图标，均可编辑。
*   一个按钮，可将面板展开覆盖整个图，之后再恢复。
*   用于与笔记交互的按钮：
    *   在当前标签页中打开笔记，或通过 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 菜单在新标签页、分屏、窗口或快速编辑弹窗中打开。
    *   用于更改笔记颜色的颜色选择器。
    *   用于从图中移除笔记的按钮，也可以选择同时删除该笔记。
*   笔记的<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>（如果有）。
*   笔记的内容，可以直接从面板中编辑。

如果图是只读的，则不会显示颜色选择器和移除按钮。

点击图上的另一条笔记会将面板切换到该笔记。同样，点击面板内的<a class="reference-link" href="Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>会将面板切换到该笔记，前提是它在图上。

要关闭面板，请按右上角的 X 按钮、点击图的空白部分，或按 <kbd>Esc</kbd>。

在移动端，笔记会以全屏对话框的形式打开，而不是面板。

## 开发流程演示

这是一个基本示例，展示如何使用关系图创建简单的图表：

<img src="Relation Map_relation-map-dev-process.png" width="934" height="667">

以下是如何创建它：

<img src="Relation Map_relation-map-dev-process-demo.gif" width="812" height="585">

我们完全从零开始，首先创建一个名为“开发流程”的新笔记，并将其类型更改为“关系图”。之后，我们逐个创建新笔记，并通过点击图来放置它们。我们还在笔记之间拖动[关系](../Advanced%20Usage/Attributes.md)并为其命名。就这样！

图上的项目——“规格说明”、“开发”、“测试”和“演示”——实际上是在“开发流程”笔记下创建的笔记——你可以点击它们并写入一些内容。笔记之间的连接称为“[关系](../Advanced%20Usage/Attributes.md)”。

## 家族演示

这是一个更复杂的演示，使用了一些高级概念。生成的图表如下：

<img src="Relation Map_relation-map-family.png" width="941" height="758">

以下是如何实现的：

<img src="Relation Map_relation-map-family-demo.gif" width="812" height="585">

这里有几个步骤：

*   我们从空的关系图和两条现有笔记开始，分别代表菲利普亲王和伊丽莎白二世女王。这两条笔记已经定义了 `isPartnerOf` [关系](../Advanced%20Usage/Attributes.md)。
    *   实际上有两个“反向”关系（一个从菲利普到伊丽莎白，一个从伊丽莎白到菲利普）
*   我们将两条笔记拖到关系图上，并放置在合适的位置。注意现有的 `isPartnerOf` 关系是如何显示的。
*   现在我们创建新笔记——将其命名为“查尔斯王子”，并通过点击所需位置将其放置在关系图上。该笔记默认创建在关系图笔记下（在左侧的笔记树中可见）。
*   我们创建两个新关系 `isChildOf`，分别指向菲利普和伊丽莎白
    *   现在出现了一些意想不到的情况——我们还可以看到显示另一个 `hasChild` 关系的关系。这是因为有一个[关系定义](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)，将 `isChildOf` 作为 `hasChildOf` 的“[反向](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)”关系（反之亦然），因此它会自动创建。
*   我们为戴安娜王妃创建另一条笔记，并从查尔斯创建 `isPartnerOf` 关系。再次注意该关系如何具有双向箭头——这是因为 `isPartnerOf` 定义将其反向关系指定为同样是“isPartnerOf”，因此反向关系会自动创建。
*   最后一步，我们平移和缩放图，以更好地适应窗口尺寸。

上述关系定义来自“人物模板”笔记，该笔记被分配给“我的家谱”关系笔记的任何子笔记。你可以在[演示笔记](../Advanced%20Usage/Database.md)中体验整个内容。

## 详情

你可以在 `displayRelations` 标签中使用逗号分隔的关系名称来指定应显示哪些关系。

或者，你可以在 `hideRelations` 中指定逗号分隔的关系名称列表，这将显示所有关系，但标签中定义的关系除外。

## 另请参阅

*   <a class="reference-link" href="Note%20Map.md">笔记地图</a> 是一个类似的概念。