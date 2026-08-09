# 属性标签页

<figure class="image image-style-align-right image_resized" style="width:34.71%;"><img style="aspect-ratio:596/1688;" src="Attributes tab_image.png" width="596" height="1688"></figure>

属性标签页提供了一种更图形化的方式来查看和编辑[属性](../../../Advanced%20Usage/Attributes.md)。

## 分区

以下信息按分区显示：

*   _自有属性_，包含属于此笔记的属性列表。
*   _继承属性_ 是适用于当前笔记但通过<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>获得的属性。
*   _定义_ 描述了属性的类型，并用于<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>和<a class="reference-link" href="../../../Collections/Table.md">表格</a>集合。

## 自有属性

每个项目结构如下：

*   每个项目的图标指示它是[标签](../../../Advanced%20Usage/Attributes/Labels.md)还是[关系](../../../Advanced%20Usage/Attributes/Relations.md)（指向另一个笔记的链接）。
*   第一个文本是标签的名称。
*   属性的值显示在名称之后（如果存在）。
    *   该值以图形方式显示：关系的值是可点击的笔记链接；颜色标签显示颜色色块。

系统属性（在 Trilium 中具有特殊含义）在图标附近显示一个小齿轮，并与用户定义的属性分开分组。

交互：

*   点击项目（值和链接除外）会显示一个专用弹窗，可以在其中定义名称、值和<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>。
*   属性的值可以就地编辑：
    *   输入框遵循相应标签定义中定义的类型（日期、颜色、下拉列表、数字），以及具有特定类型（例如 `color`）的系统属性。
    *   对于标签，点击值即可就地编辑。
        *   按 <kbd>Enter</kbd> 确认或点击输入框外部，或按 <kbd>Esc</kbd> 取消。
        *   对于多行文本，<kbd>Ctrl</kbd>+<kbd>Enter</kbd> 确认，而 <kbd>Enter</kbd> 创建换行。
    *   对于布尔值，点击复选框将切换其状态。
    *   对于没有值的标签，可以通过点击鼠标悬停在项目上时出现的 _无值_ 文本来添加值。
    *   对于关系，则有一个专用的铅笔按钮。
*   可以通过按右侧的 X 按钮删除属性，该按钮仅在悬停时出现。首先会显示确认屏幕，以确保属性不会被意外删除。

可以通过两种方式添加属性：

*   可以从分区标题附近的 + 按钮添加新的标签、关系或属性定义。这会显示完整的详细信息弹窗。
*   要从侧边栏快速添加标签或关系，请点击列表末尾的 _添加属性_ 项目。
    *   名称字段将首先获得焦点。默认情况下，将创建标签，但可以通过输入 <kbd>~</kbd> 或按图标将其切换为关系（类似地，输入 `#` 将切换回标签而不是关系）。
    *   名称填写完毕后，按 <kbd>Enter</kbd> 继续输入值。如果需要，输入值，然后再次按 <kbd>Enter</kbd> 创建属性。
    *   点击编辑器外部也会创建属性，但仅在指定了名称的情况下。

## 继承属性

继承的标签或关系以与_自有属性_相同的方式显示。

唯一区别是：

*   在继承属性的右侧，有一个指向属性来源笔记的链接，以及一个指示其可继承的图标。
*   点击继承的属性将显示与自有属性相同的弹窗，但不可编辑。要编辑它，请首先导航到定义该属性的笔记。

## 定义

对于属性定义（参见<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>）：

*   图标指示属性的类型（文本、数字）。
    *   如果属性被提升，则其上会覆盖一个小型 V 形图标。
*   名称指示其定义的属性名称（不带 `label:` 或 `relation:` 前缀）。
*   在名称右侧显示一个简短摘要，指示显示名称（别名）、是否具有多个值或反向关系。
*   点击定义会显示一个弹窗，可以在其中配置名称、类型、显示名称和其他方面。
*   可以从分区标题附近的 + 按钮添加新的标签或关系定义。
*   对于继承的定义，有一个指向定义来源笔记的链接，以及一个指示其继承的图标。

## 移动端

属性也可以在移动端进行可视化编辑，但不能作为侧边栏的一部分。转到<a class="reference-link" href="../Note%20buttons.md">笔记按钮</a>并选择 _笔记属性_。