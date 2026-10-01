# Mermaid 图表
> [!TIP]
> 如需快速了解 Mermaid 语法，请参阅 <a class="reference-link" href="Mermaid%20Diagrams/Syntax%20reference.dat">语法参考</a>（官方文档）。

<figure class="image"><img style="aspect-ratio:1464/915;" src="Mermaid Diagrams_image.png" width="1464" height="915"></figure>

Trilium 支持 Mermaid，它增加了对各种图表的支持，例如流程图、序列图、类图、状态图、饼图等，所有这些都使用图表的文本描述，而不是手动绘制图表。

此笔记类型是分屏视图，这意味着源代码和文档预览会并排显示。有关更多信息，请参阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20types%20with%20split%20view.md">具有分屏视图的笔记类型</a>。

## 示例图表

从 v0.103.0 开始，Mermaid 图表不再以示例流程图开头，而是在底部显示一个窗格，展示所有支持的图表及其示例代码：

*   只需点击任意示例即可应用它。
*   一旦在代码编辑器中输入内容或选择了示例，该窗格就会消失。要使其再次出现，只需删除笔记的内容即可。

## 布局

根据正在编辑的图表和用户偏好，Mermaid 笔记类型支持两种布局：

*   水平布局，源代码（可编辑部分）位于屏幕左侧，预览位于右侧。
*   垂直布局，源代码位于屏幕底部，预览位于顶部。

可以随时通过按下<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域中的 <span class="tn-icon bx bxs-dock-left"></span> 图标在两种布局之间切换。

## 交互

*   图表的源代码（Mermaid 格式）显示在笔记的左侧或底部（取决于布局）。
    *   更改图表代码将自动刷新图表。
*   图表的预览显示在笔记的右侧或顶部（取决于布局）：
    *   预览的右下角有专用按钮，用于控制放大、缩小或适应图表。
    *   可以通过按住鼠标左键并拖动来移动预览。
    *   也可以使用滚轮进行缩放。
    *   随着图表的变化，预览的缩放和位置将保持不变，以便更轻松地处理大型图表。
    *   双击预览可重置缩放/位置。
    *   也可以通过点击预览来使其获得焦点，此时可以使用键盘快捷键：
        *   <kbd>+</kbd> 或 <kbd>E</kbd> 放大，<kbd>-</kbd> 或 <kbd>Q</kbd> 缩小。
        *   <kbd>/</kbd> 重置缩放/位置。
        *   方向键或 <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> 平移。按住 <kbd>Shift</kbd> 可加快平移速度。
*   可以通过将鼠标悬停在源代码/预览窗格之间的边界上并用鼠标拖动来调整它们的大小。
*   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域中：
    *   可以通过 _将编辑窗格移至左侧/底部_ 选项将源代码/预览布局为左右或下上。
    *   按 _锁定编辑_ 可自动将笔记标记为只读。在此模式下，代码窗格被隐藏，图表以全尺寸显示。同样，按 _解锁编辑_ 可将只读笔记标记为可编辑。
    *   按 _复制图片引用到剪贴板_ 可将图表的图像表示插入到文本笔记中。有关更多信息，请参阅<a class="reference-link" href="Text/Images/Image%20references.md">图片引用</a>。
    *   按 _将图表导出为 SVG_ 可下载图表的可缩放/矢量渲染。可用于在缩放时不降低质量地展示图表。
    *   按 _将图表导出为 PNG_ 可下载图表的普通图像（1x 比例，光栅）。可用于通过电子邮件等更传统的渠道发送图表。

## 图表中的错误

如果源代码中存在错误，错误将显示在信息窗格中。

在错误状态下，图表将不再渲染，之前正常工作的图表将保留在预览部分。