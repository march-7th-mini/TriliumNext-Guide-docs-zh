# 快速编辑
<figure class="image image-style-align-right image_resized" style="width:53.13%;"><img style="aspect-ratio:895/694;" src="Quick edit_image.png" width="895" height="694"></figure>

_快速编辑_ 提供了基于标签页的标准导航和编辑之外的另一种方式。

无需点击笔记将 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 切换到新选中的笔记，也无需在两个不同的 <a class="reference-link" href="../UI%20Elements/Tabs.md">标签页</a> 之间导航，_快速编辑_ 功能会以弹出窗口的形式打开，可以轻松关闭。

此功能还与 <a class="reference-link" href="../../Collections.md">集合</a>（如日历视图）良好集成，使得编辑条目变得容易，无需在子笔记和日历之间来回切换。

## 功能亮点

*   支持所有笔记类型，包括 <a class="reference-link" href="../../Collections.md">集合</a>。
*   请注意，<a class="reference-link" href="../Notes/Note%20List.md">笔记列表</a> 将不会显示，但 <a class="reference-link" href="../../Collections.md">集合</a> 类型的笔记除外。
*   对于 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a> 笔记，根据用户偏好，支持浮动编辑器和经典编辑器。参见 <a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a>。
*   标题、笔记和图标均可编辑，就像普通标签页一样。
*   笔记的操作及其菜单显示在弹出窗口的头部，如同标签页的标题行。
    *   当其他笔记链接到该笔记时，带有链接图标的按钮会列出 <a class="reference-link" href="../../Note%20Types/Text/Links/Backlinks.md">反链</a>。按下其中一个即可在弹出窗口中打开该笔记。
    *   仅在标签页中有效的菜单项不会显示：_笔记地图_、_全宽_ 和 _转换为附件_。
    *   菜单中的 _查找_，或桌面应用程序中的 <kbd>Ctrl</kbd>+<kbd>F</kbd>，会在弹出窗口底部打开 <a class="reference-link" href="Search%20in%20note.md">在笔记中搜索</a> 栏。它搜索的是弹出窗口中的笔记，而不是其后方标签页中的笔记。
    *   从弹出窗口打开的帮助页面（例如通过笔记类型的帮助按钮）会在其上方打开第二个弹出窗口。关闭该弹出窗口会返回到正在编辑的笔记。
*   <a class="reference-link" href="../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a> 也会显示。
    *   这与 <a class="reference-link" href="../../Collections.md">集合</a> 良好集成，其中存在预定义的属性，如 _开始日期_ 和 _结束日期_，便于编辑。

## 访问快速编辑

*   从 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>：
    *   右键点击笔记并选择 _快速编辑_。
    *   或者，在笔记上按下 <kbd>Ctrl</kbd>+<kbd>右键点击</kbd>。
*   在 <a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a> 上：
    *   右键点击并选择 _快速编辑_。
    *   或者，在链接上按下 <kbd>Ctrl</kbd>+<kbd>右键点击</kbd>。
*   在 <a class="reference-link" href="../UI%20Elements/Note%20Tooltip.md">笔记工具提示</a> 上，按下快速编辑图标。
*   在 <a class="reference-link" href="../../Collections.md">集合</a> 中：
    *   对于 <a class="reference-link" href="../../Collections/Calendar.md">日历</a>：
        *   点击事件将打开该事件进行快速编辑。
        *   如果日历用于 <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a> 根节点，点击日期数字将打开该日记笔记的弹出窗口。
    *   对于 <a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>：
        *   点击标记将打开该标记，但仅当地图处于只读模式时。

## 只读笔记的处理

快速编辑功能对 <a class="reference-link" href="../Notes/Read-Only%20Notes.md">只读笔记</a> 有独特的行为：

*   如果笔记因性能原因而只读（自动只读），则该笔记会变为可编辑以进行快速编辑。
*   如果笔记已被手动设置为只读，则该笔记保持只读以防止意外更改。
    *   在这种情况下，仍可通过屏幕上的说明编辑笔记。

## 移动端支持

在手机上，弹出窗口使用屏幕的整个宽度，笔记内容保持与 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a> 笔记相同的侧边距。文本笔记的 <a class="reference-link" href="../../Note%20Types/Text/Formatting%20toolbar.md">格式工具栏</a> 位于对话框底部、笔记下方；其下拉菜单向上打开，以免被键盘遮挡。