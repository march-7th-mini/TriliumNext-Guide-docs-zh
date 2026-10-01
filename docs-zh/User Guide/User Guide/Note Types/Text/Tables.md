# 表格

表格是<a class="reference-link" href="../Text.md">文本</a>笔记的一项强大功能，因为编辑表格通常很容易。

<figure class="image image-style-align-right"><img style="aspect-ratio:176/204;" src="2_Tables_image.png" width="176" height="204"></figure>

要创建表格，只需按下表格按钮，然后用鼠标选择所需的列数和行数，如旁边的图所示。

## 格式工具栏

当选中表格时，会出现一个特殊的格式工具栏：

<img src="3_Tables_image.png" width="384" height="100">

## 在表格中导航

*   使用鼠标：
    *   点击某个单元格以将其聚焦。
    *   点击表格顶部或底部的 <span class="tn-icon cke cke-return-arrow"></span> 按钮，可在其附近插入一个空段落。
    *   点击表格左上角的 <span style="color:hsl(0,0%,60%);"><span class="tn-icon cke cke-drag-handle"></span></span> 按钮可将其整体选中（便于复制粘贴或剪切），或拖放它以移动表格。
*   使用键盘：
    *   使用键盘上的方向键可轻松地在单元格之间导航。
    *   也可以使用 <kbd>Tab</kbd> 键前往下一个单元格，使用 Shift+Tab 前往上一个单元格。
    *   与方向键不同，在表格末尾（最后一行、最后一列）按下 <kbd>Tab</kbd> 键会自动创建新的一行。
    *   要选择多个单元格，请在使用方向键时按住 <kbd>Shift</kbd> 键。

## 调整单元格大小

*   可以通过将鼠标悬停在两个相邻单元格的边界上并拖动来调整列的大小。
*   默认情况下，行高无法使用鼠标调整，但可以从单元格设置中进行配置（见下文）。
*   要精确调整单元格的宽度（以像素或百分比为单位），请选择 <span class="tn-icon cke cke-table-cell-properties"></span> 按钮。

## 插入新行和新列

*   要插入新列，请点击所需位置，然后按下格式工具栏中的 <span class="tn-icon cke cke-table-column"></span> 按钮，并选择 _向左或向右插入列_。
*   要插入新行，请点击所需位置，然后按下 <span class="tn-icon cke cke-table-row"></span> 按钮，并选择 _在上方或下方插入行_。
    *   在表格末尾创建新行的一种更快捷的方法是按下 <kbd>Tab</kbd> 键。

## 合并单元格

要将两个或多个单元格合并在一起，只需通过拖放选中它们，然后按下格式工具栏中的 <span class="tn-icon cke cke-table-merge-cell"></span> 按钮。

按下其旁边的箭头可获得更多选项：

*   点击单个单元格并选择向上/向下/向右/向左合并单元格，以与相邻单元格合并。
*   选择 _垂直拆分单元格_ 或 _水平拆分单元格_，以将一个单元格拆分为多个单元格（也可用于撤销合并）。

## 表格属性

<figure class="image image-style-align-right"><img style="aspect-ratio:312/311;" src="Tables_image.png" width="312" height="311"></figure>

表格属性可通过 <span class="tn-icon cke cke-table-properties"></span> 按钮访问，并允许进行以下调整：

*   边框（不是单元格的边框，而是表格的外边缘），包括样式（单线、双线）、颜色和宽度。
*   背景颜色，默认未设置。
*   表格的宽度和高度，以百分比（必须以 `%` 结尾）或像素（必须以 `px` 结尾）为单位。
*   表格的对齐方式。
    *   左对齐或右对齐，在这种情况下文本将环绕在其旁边。
    *   居中对齐，在这种情况下文本将避开表格，无论表格宽度如何。

表格将立即更新以反映更改，但必须按下 _保存_ 按钮才能使更改持久生效。

## 单元格属性

<figure class="image image-style-align-right"><img style="aspect-ratio:320/386;" src="1_Tables_image.png" width="320" height="386"></figure>

与表格属性类似，<span class="tn-icon cke cke-table-cell-properties"></span> 按钮会打开一个弹出窗口，用于调整一个或多个单元格的样式（基于用户的选择）。

可以调整以下选项：

*   边框样式、颜色和宽度（与表格属性相同），但仅应用于当前单元格。
*   背景颜色，默认未设置。
*   单元格的宽度和高度，以百分比（必须以 `%` 结尾）或像素（必须以 `px` 结尾）为单位。
*   内边距（文本与单元格边框之间的距离）。
*   文本的对齐方式，包括水平方向（左对齐、居中、右对齐、两端对齐）和垂直方向（顶部、居中或底部）。

单元格将立即更新以反映更改，但必须按下 _保存_ 按钮才能使更改持久生效。

## 题注

按下 <span class="tn-icon cke cke-caption"></span> 按钮可插入表格的题注或文字描述，它将显示在表格上方。

## 表格边框

默认情况下，表格会带有预定义的灰色边框。

要调整边框，请按照以下步骤操作：

1.  选中表格。
2.  在浮动面板中，选择 _表格属性_ 选项（<span class="tn-icon cke cke-table-properties"></span>）。
    1.  在新打开的面板顶部找到 _边框_ 部分。
    2.  这将控制表格的外部边框。
    3.  为边框选择一种样式。通常 _单线_ 是理想的选择。
    4.  为边框选择一种颜色。
    5.  为边框选择一种宽度，以像素为单位。
3.  选中表格的所有单元格，然后按下 _单元格属性_ 选项（<span class="tn-icon cke cke-table-cell-properties"></span>）。
    1.  这将在单元格级别控制表格的内部边框。
    2.  请注意，可以通过选择一个或多个单元格来单独更改边框，在这种情况下，它只会更改与这些单元格相交的边框。
    3.  重复与步骤 (2) 相同的步骤。

### 具有不可见边框的表格

可以将表格设置为具有不可见边框，以便对文本或[图片](Images.md)进行基本布局（列、网格），而不会受到边框的干扰：

1.  首先插入一个具有所需列数和行数的表格。
2.  选中整个表格。
3.  在 _表格属性_ 中，设置：
    1.  _样式_ 为 _单线_
    2.  _颜色_ 为 `transparent`
    3.  宽度为 `1px`。
4.  在单元格属性中，设置与上一步相同的内容。

## 表格缩进

自 v0.104.1 起，表格可以作为一个块进行缩进（整个表格移动，而不仅仅是单元格的内容）。

1.  点击 <span style="color:hsl(0,0%,60%);"><span class="tn-icon cke cke-drag-handle"></span></span> 按钮以选中整个表格。否则，缩进仅应用于当前单元格的内容。
2.  按下 <kbd>Tab</kbd> 键增加缩进，或按下 <kbd>Shift</kbd>+<kbd>Tab</kbd> 键减少缩进。或者，使用格式工具栏中的缩进按钮。

Markdown 不支持缩进的表格，因此转换为 Markdown 时缩进会丢失。

## Markdown 导入/导出

简单表格会以 GitHub 风格的 Markdown 格式导出（例如一系列 `|` 项）。如果发现表格较为复杂（包含 HTML 元素、具有自定义尺寸或图片），则表格会改为转换为 HTML 表格。

通常，由于会回退到 HTML 格式，导出为 Markdown 时格式丢失应该是最小的。