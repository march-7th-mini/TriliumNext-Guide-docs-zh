# 属性选项卡
<figure class="image image-style-align-right image_resized" style="width:34.71%;"><img style="aspect-ratio:596/1688;" src="Attributes tab_image.png" width="596" height="1688"></figure>

属性选项卡提供了一种更图形化的方式来查看和编辑[属性](../../../Advanced%20Usage/Attributes.md)。

## 分区

属性被分组到可折叠的分区中，每个分区在其名称旁显示所包含的属性数量：

*   _自有_ 包含属于此笔记的属性列表。
*   _继承_ 包含适用于当前笔记但通过<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>而来的属性。此分区仅在笔记继承了属性时显示。
*   _定义_ 描述属性的类型，用于<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>和<a class="reference-link" href="../../../Collections/Table.md">表格</a>集合。此分区仅在笔记拥有或继承了定义时显示。

点击分区名称可折叠或展开该分区，折叠状态会被记住。

## 工具栏

分区上方有一个工具栏，包含：

*   一个 _全选_ 复选框，用于选择所有属性（参见[选择属性](#selecting-attributes)）。
*   一个 <span class="tn-icon bx bx-paste"></span> 按钮，仅在属性被复制后出现。它列出已复制的属性，并提供将其粘贴到当前笔记或清除的选项。
*   一个 <span class="tn-icon bx bx-plus"></span> _添加新属性_ 按钮，提供添加标签、关系、标签定义或关系定义的选项。这会显示完整的详情弹窗。

在不可编辑的笔记上（例如应用内帮助的页面），粘贴和添加按钮会被替换为 <span class="tn-icon bx bx-lock-alt"></span> _只读_ 指示器。仍然可以从这样的笔记中选择和复制属性。

## 自有属性

每个条目的结构如下：

*   每个条目的图标指示它是[标签](../../../Advanced%20Usage/Attributes/Labels.md)（<span class="tn-icon bx bx-hash"></span>）还是[关系](../../../Advanced%20Usage/Attributes/Relations.md)（<span class="tn-icon bx bx-transfer"></span>，链接到另一个笔记）。
*   第一段文本是标签的名称。
*   属性的值（如果存在）显示在名称之后。
    *   值以图形方式显示：关系的值是可点击的笔记链接；颜色标签显示颜色色块。

系统属性（在 Trilium 中有特殊含义的）在图标附近显示一个小 <span class="tn-icon bx bx-cog"></span> 齿轮图标，并与用户定义的属性分开分组。

交互：

*   点击条目（值和链接除外）会显示一个专用弹窗，可在其中定义名称、值和<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>。
*   属性的值可以就地编辑：
    *   输入框遵循相应标签定义中定义的类型（日期、颜色、下拉列表、数字），以及具有特定类型的系统属性（例如 `color`）。
    *   对于标签，点击值可就地编辑。
        *   按 <kbd>Enter</kbd> 确认或点击输入框外部，或按 <kbd>Esc</kbd> 取消。
        *   对于多行文本，<kbd>Ctrl</kbd>+<kbd>Enter</kbd> 确认，而 <kbd>Enter</kbd> 创建新行。
    *   对于复选框属性，点击复选框将切换其状态。
    *   对于没有值的标签，可以通过点击鼠标悬停在条目上时出现的 _无值_ 文本来添加值。
    *   对于关系，则有一个专用的 <span class="tn-icon bx bx-pencil"></span> 按钮。
*   可以通过按右侧的 <span class="tn-icon bx bx-trash"></span> 按钮删除属性，该按钮仅在悬停时出现。首先会显示确认屏幕以确保属性不会被意外删除。

可以通过两种方式添加属性：

*   可以从[工具栏](#toolbar)中的 <span class="tn-icon bx bx-plus"></span> 按钮添加新的标签、关系或属性定义。这会显示完整的详情弹窗。
*   要直接从侧边栏快速添加标签或关系，请点击列表末尾的 _添加属性_（<span class="tn-icon bx bx-plus"></span>）条目。
    *   名称字段会首先获得焦点。默认情况下会创建标签，但可以通过输入 <kbd>~</kbd> 或按 <span class="tn-icon bx bx-hash"></span> 图标切换为关系（类似地，输入 `#` 将切换回标签而非关系）。
    *   填写名称后，按 <kbd>Enter</kbd> 继续到值。如果需要，输入值，然后再次按 <kbd>Enter</kbd> 创建属性。
    *   点击编辑器外部也会创建属性，但仅在指定了名称的情况下。

## 继承属性

继承的标签或关系以与自有属性相同的方式显示。

唯一的区别是：

*   继承属性的右侧有一个指向属性来源笔记的链接，以及一个 <span class="tn-icon bx bx-sitemap"></span> 图标表示它是可继承的。
*   点击继承属性会显示与自有属性相同的弹窗，但不可编辑。要编辑它，请先导航到定义该属性的笔记。

## 定义

对于属性定义（参见<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>）：

*   图标指示属性的类型（文本、数字）。
    *   如果属性被提升，其上方会叠加一个小 <span class="tn-icon bx bx-chevron-up"></span> 尖括号图标。
*   名称指示它所定义的属性名称（不含 `label:` 或 `relation:` 前缀）。
*   名称右侧显示简短摘要，指示显示名称（别名）、是否具有多个值或反向关系。
*   点击定义会显示一个弹窗，可在其中配置名称、类型、显示名称和其他方面。
*   要添加标签定义，请点击列表末尾的 _添加定义_（<span class="tn-icon bx bx-plus"></span>）条目；其类型可以从弹窗中更改为关系。两种定义也可以从[工具栏](#toolbar)中的 <span class="tn-icon bx bx-plus"></span> 按钮添加。
*   对于继承的定义，有一个指向定义来源笔记的链接，以及一个 <span class="tn-icon bx bx-sitemap"></span> 图标表示它是继承的。

## 选择属性

可以选择多个属性以便一起复制或删除：

*   将鼠标悬停在属性上会在其图标位置显示一个复选框。点击它以选择该属性。
*   或者，在点击属性时按住 <kbd>Ctrl</kbd>（macOS 上为 <kbd>Cmd</kbd>）以选择它，或按住 <kbd>Shift</kbd> 选择一系列属性。范围可以跨越多个分区。
*   一旦至少选择了一个属性，每个属性都会显示其复选框，点击属性的任何位置将选择或取消选择它，而不是打开详情弹窗。
*   工具栏中的 _全选_ 复选框选择所有属性；当有属性被选中时，它显示已选数量。再次点击它清除选择，按 <kbd>Esc</kbd> 也是如此。

当有属性被选中时，工具栏显示：

*   一个 <span class="tn-icon bx bx-copy"></span> 按钮，用于复制选中的属性。
*   一个 <span class="tn-icon bx bx-trash"></span> 按钮，在确认后删除选中的属性。它仅在所有选中的属性都属于当前笔记时出现，因为继承属性只能从其来源笔记中删除。

右键点击属性会显示一个包含相同操作以及粘贴的菜单。如果该属性不属于选择范围，菜单仅适用于该属性。

## 复制和粘贴属性

属性可以从一个笔记复制并粘贴到另一个笔记：

*   要复制，选择属性并按 <kbd>Ctrl</kbd>+<kbd>C</kbd>，或使用工具栏中的 <span class="tn-icon bx bx-copy"></span> 按钮或上下文菜单。
*   要粘贴，导航到目标笔记，在属性选项卡中任意位置点击后按 <kbd>Ctrl</kbd>+<kbd>V</kbd>，或使用工具栏中的 <span class="tn-icon bx bx-paste"></span> 按钮。右键点击属性或分区的空白区域也会提供粘贴选项。

属性以文本形式复制，格式与属性编辑器相同（例如 `#author=John ~template=#root/abc123 #tag(inheritable)`）。因此：

*   复制的属性可以粘贴到属性编辑器或笔记中，属性编辑器的文本也可以粘贴到属性选项卡中。
*   属性可以在任何其他应用程序中手写，然后粘贴到 Trilium 中。

粘贴时，属性成为当前笔记的自有属性，即使它们在源笔记中是继承的：

*   如果笔记已有同名属性，其值将被粘贴的值替换。
*   如果定义将属性标记为具有多个值（参见<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>），则粘贴的值会与现有值一起添加，除非相同的值已存在。

> [!NOTE]
> <kbd>Ctrl</kbd>+<kbd>V</kbd> 粘贴系统剪贴板中的内容，而 <span class="tn-icon bx bx-paste"></span> 按钮和上下文菜单粘贴的是 Trilium 中最后复制的属性。如果在此期间复制了其他内容，两者会有所不同。

## 移动端

属性也可以在移动端以可视化方式编辑，但不是作为侧边栏的一部分。转到<a class="reference-link" href="../Note%20menu.md">笔记菜单</a>并选择 _属性_，位于 _反链_ 和 _笔记路径_ 下方，这会在屏幕底部的面板中打开属性。

在移动端，每个分区显示为单独的卡片：

*   属性从工具栏中的 <span class="tn-icon bx bx-plus"></span> 按钮添加，或从 _定义_ 卡片标题中的 <span class="tn-icon bx bx-plus"></span> 按钮添加。
*   要选择属性，请长按它。一旦选择了某个属性，点击其他属性也会选择它们。
*   复制、粘贴和删除的工作方式与桌面端相同，通过工具栏操作。