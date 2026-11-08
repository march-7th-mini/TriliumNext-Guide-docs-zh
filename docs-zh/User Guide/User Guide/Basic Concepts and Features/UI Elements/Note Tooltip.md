# 笔记工具提示
<figure class="image image-style-align-right"><img style="aspect-ratio:505/261;" src="Note Tooltip_image.png" width="505" height="261"></figure>

笔记工具提示是一项便捷功能，当鼠标悬停在指向另一条笔记的[内部链接](../../Note%20Types/Text/Links/Internal%20\(reference\)%20links.md)上时，会显示一个弹出窗口。

显示的信息如下：

*   笔记路径，位于弹出窗口顶部。
*   笔记的标题。
    *   点击标题将在当前标签页中打开该笔记。
    *   按住 <kbd>Ctrl</kbd> 的同时点击标题，将在新标签页中打开，而非当前标签页。
*   还会显示一段内容片段。
*   一个用于在弹出窗口中[快速编辑](../Navigation/Quick%20edit.md)该笔记的按钮。
    *   对于指向该链接所在笔记中块的链接，<span class="tn-icon bx bx-up-arrow"></span> _跳转到块_ 按钮会取代其位置；对于标题则为 _跳转到标题_，并滚动到相应位置而不离开该笔记。

对于指向[附件](../Notes/Attachments.md)的链接，工具提示会改为显示该附件：其标题显示在拥有该附件的笔记路径之后，一行显示其大小（例如 _附件 • 20.59 MiB_），在可用时显示其内容预览，以及打开该附件的快速编辑按钮。

工具提示可在多个位置出现，包括：

*   在 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a> 笔记中，当鼠标悬停在 <a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a> 上时。
*   <a class="reference-link" href="../../Collections.md">集合</a>：
    *   <a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图视图</a>，当鼠标悬停在标记上时。
    *   <a class="reference-link" href="../../Collections/Calendar.md">日历视图</a>，当鼠标悬停在事件上时。
    *   <a class="reference-link" href="../../Collections/Table.md">表格视图</a>，当鼠标悬停在笔记标题或[关系](../../Advanced%20Usage/Attributes/Relations.md)上时。