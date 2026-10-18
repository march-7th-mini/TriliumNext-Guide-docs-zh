# 内容宽度
某些笔记类型（例如<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>和保存的搜索）会有意限制内容的宽度。

乍一看这可能令人意外，但其目的是让文本在较宽的屏幕上也能良好呈现，而不会显得变形。当文档包含<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>、表格或其他依赖宽度的元素时尤其如此。

## 配置内容宽度和对齐方式

内容宽度以像素为单位表示，可以在<a class="reference-link" href="Options.md">选项</a> → _外观_ → _内容宽度_ 中调整 _最大内容宽度_ 部分来更改。

要有效禁用内容宽度限制，只需将宽度设置为大于屏幕尺寸的值（例如 9999）。

默认情况下，内容左对齐，但可以通过在同一部分勾选 _保持内容居中_ 来使其水平居中。

## 在笔记级别调整

对于包含大型元素（如<a class="reference-link" href="../../Note%20Types/Text/Tables.md">表格</a>）的笔记，有时在不影响其他笔记的情况下避开内容宽度限制是合理的。为此：

*   转到<a class="reference-link" href="Note%20menu.md">笔记菜单</a>并切换 _全宽_。
*   或者手动将 `fullContentWidth` [标签](../../Advanced%20Usage/Attributes/Labels.md)应用到笔记。

自 v0.107.0 起，单个表格也可以比内容宽度更宽，此时它会横向滚动。参见<a class="reference-link" href="../../Note%20Types/Text/Tables.md">表格</a>。

> [!NOTE]
> 某些[笔记类型](../../Note%20Types.md)默认就是全宽，例如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>。在这种情况下，不会显示 _全宽_ 切换项，标签也不会生效。

## 共享笔记

在[共享页面](../../Advanced%20Usage/Sharing.md)上，文本笔记以固定的阅读宽度显示，无论选项中配置的宽度如何，并且导航树、内容和目录在宽屏幕上保持在同一列中居中。带有 `fullContentWidth` 的笔记，或在应用中为全宽类型的笔记，在那里会使用窗口的整个宽度，导航树和目录位于其边缘。