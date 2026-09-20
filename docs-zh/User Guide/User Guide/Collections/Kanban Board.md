# 看板

<figure class="image"><img style="aspect-ratio:918/248;" src="2_Kanban Board_image.png" width="918" height="248"></figure>

看板视图以列的形式展示子笔记，提供类似看板的体验。每一列代表状态标签的一个可能值，该值可以调整。

## 创建看板

在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击一个已有笔记，选择_插入子笔记_，然后找到_看板_。

## 工作原理

首次创建_看板_类型的集合时，会创建若干子笔记，每个子笔记都设置了 `#status` 标签。看板随后根据状态属性的值对每个笔记进行分组。

笔记是递归显示的，因此即使是子笔记的子笔记也会显示。然而，与<a class="reference-link" href="Table.md">表格</a>不同，笔记不会以层级结构显示。

## 交互

### 操作列

*   通过点击最后一列附近的_添加列_来创建新列。
    *   点击后会显示一个文本框，用于设置列的名称。按 Enter 确认，或按 Escape 取消。
*   要重新排列列的顺序，只需将鼠标悬停在标题上并将其拖动到所需位置。
*   要删除列，右键点击其标题并选择_删除列_。
*   要重命名列，点击笔记标题。
    *   按 Enter 确认。
    *   重命名列后，其所有笔记对应的状态属性将被批量更改。
*   如果列很多，使用鼠标滚轮滚动。

### 操作笔记

*   通过点击_新建条目_在任意列中创建新笔记。
    *   输入笔记名称并按 Enter 或点击其他位置。要取消创建新笔记，只需按 Escape 或将名称留空。
    *   创建后，新笔记将有一个属性（默认为 `status` 标签）设置为列的名称。
*   要打开笔记，只需点击它。
*   要直接从看板更改笔记标题，将鼠标悬停在其卡片上，然后点击右侧的编辑按钮。
*   要更改笔记的状态，只需将笔记从一列拖动到另一列即可更改其状态。
*   每列中笔记的顺序对应它们在树中的位置。
    *   可以通过在同一列内将笔记拖动到所需位置来重新排序。
    *   也可以将笔记跨列拖动到所需位置。
*   如需更多选项，右键点击笔记以显示包含以下选项的上下文菜单：
    *   在新标签页/分屏/窗口中打开笔记或快速编辑。
    *   将笔记移动到任意列。
    *   在当前笔记上方/下方插入新笔记。
    *   归档/取消归档当前笔记。
    *   删除当前笔记。
*   如果列中有很多笔记，将鼠标移到列上并使用鼠标滚轮滚动。

### 操作笔记树

也可以使用<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>在看板上添加条目。

1.  在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中选择所需的笔记。
2.  将鼠标按住该笔记并将其拖动到所需的列。

这适用于：

*   不是看板子笔记的笔记，此时将创建一个[克隆](../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)。
*   是看板子笔记但尚未在看板上分配的笔记。
*   是看板子笔记的笔记，此时它们将被移动到新列。

### 键盘交互

看板视图对基于键盘的导航有适度支持：

*   使用 Tab 和 Shift+Tab 按顺序在列标题、笔记和每列的“新建条目”按钮之间导航。
*   要重命名列或笔记，在聚焦时按 F2。
*   要打开特定笔记或创建新条目，在聚焦时按 Enter。
*   要取消笔记或列的重命名，按 Escape。

## 配置

### 显示自定义属性

<figure class="image image-style-align-center"><img style="aspect-ratio:531/485;" src="Kanban Board_image.png" width="531" height="485"></figure>

自 v0.100.0 起，笔记属性可以显示在看板上，以增强自定义信息，例如为任务添加_截止日期_。

此功能仅通过属性定义（<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>）工作。添加这些的最简单方法是：

1.  转到看板笔记。
2.  在功能区中选择_自有属性_ → 加号按钮 → _添加新标签/关系定义_。
3.  根据需要配置属性。
4.  勾选_可继承_使其自动适用于子笔记。

创建属性后，点击一个笔记并填写提升属性，这些属性随后应反映在看板中。

注意事项：

*   同时支持提升和非提升属性定义。唯一的区别是非提升属性没有用于分配自定义名称的“别名”。
*   同时支持“单值”和“多值”属性。对于多值，属性的每个实例都会显示一个徽章。
*   支持所有标签类型，包括日期、布尔值和 URL。
*   也支持关系属性，显示带有目标笔记标题和图标的链接。

### 按其他标签分组

默认情况下，用于分组笔记的标签是 `#status`。如果需要，可以通过定义一个名为 `#board:groupBy` 的标签来使用不同的标签，其值为要使用的属性（带或不带 `#` 属性前缀）。

### 按关系分组

<figure class="image image-style-align-right"><img style="aspect-ratio:535/245;" src="1_Kanban Board_image.png" width="535" height="245"></figure>

更高级的用例是按[关系](../Advanced%20Usage/Attributes/Relations.md)分组。

在此模式下：

*   列代表关系的_目标笔记_。
*   创建新列时，选择的是笔记而不是列名称。
*   列图标将与目标笔记匹配。
*   在列之间移动笔记将更改其关系。
*   重命名现有列将更改该列中所有笔记的目标笔记。

使用关系而不是标签有一些好处：

*   笔记的状态/分组在看板之外也可见，例如在<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记地图</a>上。
*   列可以有图标。
*   重命名列的工作量更小，因为它只涉及更改目标笔记的笔记标题，而不必进行批量重命名。

为此：

1.  首先，从头创建看板而不是使用模板：
2.  分配 `#viewType=board #hidePromotedAttributes` 以模拟默认模板。
3.  将 `#board:groupBy` 设置为要分组的关系名称，**包括** `~` **前缀**（例如 `~status`）。
4.  可选地，使用<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>以便在笔记中轻松更改状态：
    
    ```
    #relation:status(inheritable)="promoted,alias=Status,single"
    ```