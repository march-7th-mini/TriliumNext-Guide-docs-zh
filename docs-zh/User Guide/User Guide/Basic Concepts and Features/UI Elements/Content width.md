# 内容宽度

某些笔记类型，例如<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>、<a class="reference-link" href="../../Note%20Types/Relation%20Map.md">关系图</a>和已保存的搜索，会刻意限制内容的宽度。

乍一看这可能令人意外，但其目的是让文本在更宽的屏幕上也能良好适配，而不会显得扭曲。如果文档包含<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>、表格或其他依赖宽度的元素，这一点尤其重要。

## 配置内容宽度和对齐方式

内容宽度以像素为单位表示，可以通过<a class="reference-link" href="Options.md">选项</a> → _外观_ → _内容宽度_ 并调整 _最大内容宽度_ 部分来更改。

要有效禁用内容宽度限制，只需将宽度设置为大于屏幕尺寸的值（例如 9999）。

默认情况下，内容左对齐，但可以通过在同一部分（内容宽度所在部分）勾选 _保持内容居中_ 来使其水平居中。

## 在笔记级别调整

对于包含<a class="reference-link" href="../../Note%20Types/Text/Tables.md">表格</a>等大型元素的笔记，有时在不影响其他笔记的情况下避免内容宽度限制是有意义的。操作方法如下：

*   自 v0.104.0 起，仅在<a class="reference-link" href="New%20Layout.md">新布局</a>中，转到<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>并切换 _全宽_。
*   或者手动将 `fullContentWidth` [标签](../../Advanced%20Usage/Attributes/Labels.md) 应用到笔记上。

> [!NOTE]
> 某些[笔记类型](../../Note%20Types.md)默认就是全宽的，例如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>。在这种情况下，_全宽_ 切换按钮将不会显示，该标签也不会生效。