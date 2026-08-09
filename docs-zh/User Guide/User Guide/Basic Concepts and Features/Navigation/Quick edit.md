# 快速编辑
<figure class="image image-style-align-right image_resized" style="width:53.13%;"><img style="aspect-ratio:895/694;" src="Quick edit_image.png" width="895" height="694"></figure>

_快速编辑_ 提供了标准标签页导航和编辑之外的另一种选择。

无需点击笔记来切换<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>至新选中的笔记，也无需在两个不同的<a class="reference-link" href="../UI%20Elements/Tabs.md">标签页</a>之间导航，_快速编辑_ 功能会以弹出窗口的形式打开，并且可以轻松关闭。

此功能还与<a class="reference-link" href="../../Collections.md">集合</a>（如日历视图）良好集成，使得编辑条目时无需在子笔记和日历之间来回切换。

## 功能亮点

*   支持所有笔记类型，包括<a class="reference-link" href="../../Collections.md">集合</a>。
*   请注意，除<a class="reference-link" href="../../Collections.md">集合</a>类型的笔记外，<a class="reference-link" href="../Notes/Note%20List.md">笔记列表</a>将不会显示。
*   对于<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记，根据用户偏好，支持浮动编辑器和经典编辑器。请参阅<a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a>。
*   标题、笔记和图标均可编辑，与普通标签页相同。
*   同时显示<a class="reference-link" href="../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>。
    *   这与<a class="reference-link" href="../../Collections.md">集合</a>（其中预定义了如 _开始日期_ 和 _结束日期_ 等属性）集成良好，便于编辑。

## 访问快速编辑

*   从<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>：
    *   右键点击笔记并选择 _快速编辑_。
    *   或者，在笔记上按 <kbd>Ctrl</kbd>+<kbd>右键点击</kbd>。
*   在<a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>上：
    *   右键点击并选择 _快速编辑_。
    *   或者，在链接上按 <kbd>Ctrl</kbd>+<kbd>右键点击</kbd>。
*   在<a class="reference-link" href="../UI%20Elements/Note%20Tooltip.md">笔记工具提示</a>上，点击快速编辑图标。
*   在<a class="reference-link" href="../../Collections.md">集合</a>中：
    *   对于<a class="reference-link" href="../../Collections/Calendar.md">日历</a>：
        *   点击事件将打开该事件以进行快速编辑。
        *   如果日历是针对<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">每日笔记</a>根节点的，点击日期数字将打开该日笔记的弹出窗口。
    *   对于<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>：
        *   点击标记将打开该标记，但仅当地图处于只读模式时。

## 只读笔记的处理

快速编辑功能对<a class="reference-link" href="../Notes/Read-Only%20Notes.md">只读笔记</a>有特殊行为：

*   如果笔记因性能原因（自动只读）而处于只读状态，则该笔记将变为可编辑以进行快速编辑。
*   如果笔记被手动设置为只读，则该笔记保持只读以防止意外更改。
    *   在这种情况下，仍可通过屏幕上的指示进行编辑。