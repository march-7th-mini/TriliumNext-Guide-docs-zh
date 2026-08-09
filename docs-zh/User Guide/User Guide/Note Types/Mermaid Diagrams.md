# Mermaid 图表

> [!TIP]
> 如需快速了解 Mermaid 语法，请参阅 <a class="reference-link" href="Mermaid%20Diagrams/Syntax%20reference.dat">语法参考</a>（官方文档）。

<figure class="image image-style-align-center"><img style="aspect-ratio:886/663;" src="2_Mermaid Diagrams_image.png" width="886" height="663"></figure>

Trilium 支持 Mermaid，这为流程图、时序图、类图、状态图、饼图等各种图表提供了支持，所有这些都使用图表的文本描述，而不是手动绘制图表。

此笔记类型为分屏视图，即源代码和文档预览并排显示。有关更多信息，请参阅 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20types%20with%20split%20view.md">分屏视图的笔记类型</a>。

## 示例图表

从 v0.103.0 开始，Mermaid 图表不再以示例流程图开头，而是在底部显示一个窗格，其中包含所有支持的图表及每个图表的示例代码：

*   只需点击任意示例即可应用。
*   一旦在代码编辑器中输入内容或选择了示例，该窗格将消失。若要使其再次出现，只需清除笔记的内容即可。

## 布局

根据所编辑的图表和用户偏好，Mermaid 笔记类型支持两种布局：

*   水平布局，源代码（可编辑部分）位于屏幕左侧，预览位于右侧。
*   垂直布局，源代码位于屏幕底部，预览位于顶部。

可以随时通过按下 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a> 区域中的 ![](Mermaid%20Diagrams_image.png) 图标来切换两种布局。

## 交互

*   图表的源代码（Mermaid 格式）显示在笔记的左侧或底部（取决于布局）。
    *   更改图表代码将自动刷新图表。
*   图表的预览显示在笔记的右侧或顶部（取决于布局）：
    *   预览右下角有专用按钮，用于控制图表的放大、缩小或重新居中：![](1_Mermaid%20Diagrams_image.png)
    *   可以通过按住鼠标左键并拖动来移动预览。
    *   也可以使用滚轮进行缩放。
    *   预览的缩放和位置将随着图表的变化而保持固定，以便更轻松地处理大型图表。
*   源代码/预览窗格的大小可以通过将鼠标悬停在它们之间的边界上并拖动来调整。
*   在 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a> 区域：
    *   可以通过 _将编辑窗格移至左侧/底部_ 选项将源代码/预览设置为左右或上下布局。
    *   按下 _锁定编辑_ 可自动将笔记标记为只读。在此模式下，代码窗格被隐藏，图表以全尺寸显示。同样，按下 _解锁编辑_ 可将只读笔记标记为可编辑。
    *   按下 _将图片引用复制到剪贴板_ 可将图表的图片表示插入到文本笔记中。有关更多信息，请参阅 <a class="reference-link" href="Text/Images/Image%20references.md">图片引用</a>。
    *   按下 _将图表导出为 SVG_ 可下载图表的可缩放/矢量渲染。可用于在缩放时不会失真的方式呈现图表。
    *   按下 _将图表导出为 PNG_ 可下载图表的普通图像（1 倍缩放，光栅）。可用于通过更传统的渠道（如电子邮件）发送图表。

## 图表中的错误

如果源代码中存在错误，错误将显示在信息窗格中。

在错误状态下，图表将不再渲染，之前正常工作的图表将保留在预览部分。