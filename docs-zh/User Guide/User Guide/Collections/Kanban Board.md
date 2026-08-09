# 看板视图

<figure class="image"><img style="aspect-ratio:918/248;" src="2_Kanban Board_image.png" width="918" height="248"></figure>

看板视图将子笔记按列展示，提供类似看板的体验。每一列代表状态标签的一个可能值，该值可以调整。

## 创建看板

在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击现有笔记，选择 _插入子笔记_，然后查找 _看板_。

## 工作原理

首次创建 _看板_ 类型的集合时，会创建几个子笔记，每个子笔记都设置了 `#status` 标签。看板随后根据状态属性的值对每个笔记进行分组。

笔记以递归方式显示，因此即使是子笔记的子笔记也会被显示。但是，与<a class="reference-link" href="Table.md">表格</a>不同，笔记不会以层级结构显示。

## 交互操作

### 处理列

*   通过点击最后一列附近的 _添加列_ 来创建新列。
    *   点击后，将显示一个文本框以设置列的名称。按 <kbd>Enter</kbd> 确认，或按 <kbd>Escape</kbd> 取消。
*   要重新排序列，只需将鼠标悬停在标题上并将其拖拽到所需位置。
*   要删除列，请右键点击其标题并选择 _删除列_。
*   要重命名列，请点击笔记标题。
    *   按 Enter 确认。
    *   重命名列时，其所有笔记对应的状态属性将被批量更改。
*   如果列很多，可以使用鼠标滚轮滚动。

### 处理笔记

*   通过点击 _新建项目_ 在任何列中创建新笔记。
    *   输入笔记名称并按 <kbd>Enter</kbd> 或点击其他区域。要取消创建新笔记，只需按 <kbd>Escape</kbd> 或留空名称。
    *   创建后，新笔记将具有一个属性（默认为 `status` 标签），其值设置为列的名称。
*   要打开笔记，只需点击它。
*   要直接从看板更改笔记标题，请将鼠标悬停在其卡片上，然后按右侧的编辑按钮。
*   要更改笔记的状态，只需将笔记从一列拖到另一列即可更改其状态。
*   每列中笔记的顺序对应它们在树中的位置。
    *   可以通过在同一列内将笔记拖拽到所需位置来重新排序。
    *   也可以将笔记跨列拖拽到所需位置。
*   如需更多选项，请右键点击笔记以显示上下文菜单，其中包含以下选项：
    *   在新标签页/分屏/窗口中打开笔记，或快速编辑。
    *   将笔记移动到任何列。
    *   在当前笔记上方/下方插入新笔记。
    *   归档/取消归档当前笔记。
    *   删除当前笔记。
*   如果列内笔记很多，请将鼠标移到列上并使用鼠标滚轮滚动。

### 使用笔记树操作

也可以使用<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>向看板添加项目。

1.  在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中选择所需的笔记。
2.  按住鼠标左键并拖拽笔记到所需的列。

这适用于：

*   不是看板子笔记的笔记，这种情况下将创建一个[克隆](../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)。
*   是看板子笔记但尚未在看板上分配的笔记。
*   是看板子笔记的笔记，这种情况下它们将被移动到新列。

### 键盘交互

看板视图对基于键盘的导航提供适度支持：

*   使用 <kbd>Tab</kbd> 和 <kbd>Shift</kbd>+<kbd>Tab</kbd> 按顺序在列标题、笔记和每个列的“新建项目”按钮之间导航。
*   要重命名列或笔记，请在聚焦时按 <kbd>F2</kbd>。
*   要打开特定笔记或创建新项目，请在聚焦时按 <kbd>Enter</kbd>。
*   要取消重命名笔记或列，请按 <kbd>Escape</kbd>。

## 配置

### 显示自定义属性

<figure class="image image-style-align-center"><img style="aspect-ratio:531/485;" src="Kanban Board_image.png" width="531" height="485"></figure>

自 v0.100.0 起，可以在看板上显示笔记属性，以通过自定义信息（例如为任务添加 _截止日期_）增强看板功能。

此功能仅通过属性定义（<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>）工作。添加这些属性的最简单方法是：

1.  转到看板笔记。
2.  在功能区中选择 _自有属性_ → 加号按钮 → _添加新的标签/关系定义_。
3.  根据需要配置属性。
4.  勾选 _可继承_ 以使其自动适用于子笔记。

创建属性后，点击一个笔记并填写提升属性，这些属性应反映在看板内部。

注意：

*   支持提升和非提升的属性定义。唯一的区别是非提升属性没有用于分配自定义名称的“别名”。
*   支持“单值”和“多值”属性。对于多值属性，属性的每个实例都会显示一个徽章。
*   支持所有标签类型，包括日期、布尔值和 URL。
*   也支持关系属性，显示带有目标笔记标题和图标的链接。
*   目前，无法调整显示哪些提升属性，因为所有提升属性都会被显示（除了 `board:groupBy` 属性）。有计划改进此功能，以便能够单独隐藏提升属性。

### 按其他标签分组

默认情况下，用于对笔记进行分组的标签是 `#status`。如果需要，可以通过定义一个名为 `#board:groupBy` 的标签来使用不同的标签，其值为要使用的属性（带或不带 `#` 属性前缀均可）。

### 按关系分组

<figure class="image image-style-align-right"><img style="aspect-ratio:535/245;" src="1_Kanban Board_image.png" width="535" height="245"></figure>

一个更高级的用例是按[关系](../Advanced%20Usage/Attributes/Relations.md)分组。

在此模式下：

*   列代表关系的_目标笔记_。
*   创建新列时，选择的是一个笔记而不是列名称。
*   列图标将与目标笔记匹配。
*   在列之间移动笔记将更改其关系。
*   重命名现有列将更改该列中所有笔记的目标笔记。

使用关系而不是标签有一些好处：

*   笔记的状态/分组在看板外部可见，例如在<a class="reference-link" href="../Note%20Types/Note%20Map.md">笔记地图</a>上。
*   列可以有图标。
*   重命名列的工作量较小，因为它只涉及更改目标笔记的笔记标题，而不必进行批量重命名。

操作步骤：

1.  首先，从头创建一个看板，而不是使用模板：
2.  分配 `#viewType=board #hidePromotedAttributes` 以模拟默认模板。
3.  将 `#board:groupBy` 设置为要按其分组的关系名称，**包括** `~` **前缀**（例如 `~status`）。
4.  （可选）使用<a class="reference-link" href="../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>以便在笔记内轻松更改状态：
    
    ```
    #relation:status(inheritable)="promoted,alias=Status,single"
    ```