# Mermaid 图表
> [!TIP]
> 如需快速了解 Mermaid 语法，请参阅 <a class="reference-link" href="Mermaid%20Diagrams/Syntax%20reference.dat">语法参考</a>（官方文档）。

<figure class="image"><img style="aspect-ratio:1464/915;" src="Mermaid Diagrams_image.png" width="1464" height="915"></figure>

Trilium 支持 Mermaid，它增加了对各种图表的支持，例如流程图、时序图、类图、状态图、饼图等，所有这些都使用图表的文本描述，而不是手动绘制图表。

此笔记类型为分栏视图，即源代码和文档预览会并排显示。更多信息请参阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20types%20with%20split%20view.md">带分栏视图的笔记类型</a>。

## 示例图表

从 v0.103.0 开始，Mermaid 图表不再以示例流程图开头，而是在底部显示一个窗格，其中列出所有支持的图表及各自的示例代码：

*   只需点击任意示例即可应用它。
*   一旦在代码编辑器中输入内容或选择了示例，该窗格就会消失。要使其再次出现，只需删除笔记的内容即可。

## 布局

根据正在编辑的图表和用户偏好，Mermaid 笔记类型支持两种布局：

*   水平布局，源代码（可编辑部分）位于屏幕左侧，预览位于右侧。
*   垂直布局，源代码位于屏幕底部，预览位于顶部。

可以随时通过按下<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>中的 <span class="tn-icon bx bxs-dock-left"></span> 图标在两种布局之间切换。

## 交互

*   图表的源代码（Mermaid 格式）显示在笔记的左侧或底部（取决于布局）。
    *   更改图表代码将自动刷新图表。
    *   前置元数据（图表开头 `---` 行之间的块，包含其标题和配置）以 YAML 高亮显示，流程图和看板的节点属性（如 `@{ shape: tool }`）也是如此。配置指令（`%%{init: …}%%`）与注释分开高亮显示，无障碍标题和描述（`accTitle:` 和 `accDescr:`）也是如此。
    *   <kbd>Ctrl</kbd>+<kbd>/</kbd>（Mac：<kbd>⌘</kbd>+<kbd>/</kbd>）使用 `%%` 注释当前行或选中行，在前置元数据中使用 `#`。在已注释的行上再次按下可移除注释标记。
*   图表的预览显示在笔记的右侧或顶部（取决于布局）：
    *   预览右下角有专用按钮，用于控制放大、缩小或适应图表。
    *   按住鼠标左键并拖动可以移动预览。
    *   也可以使用滚轮进行缩放。
    *   随着图表变化，预览的缩放和位置将保持固定，以便更轻松地处理大型图表。
    *   双击预览可重置缩放/位置。
    *   也可以通过点击预览使其获得焦点，此时可以使用键盘快捷键：
        *   <kbd>+</kbd> 或 <kbd>E</kbd> 放大，<kbd>-</kbd> 或 <kbd>Q</kbd> 缩小。
        *   <kbd>/</kbd> 重置缩放/位置。
        *   方向键或 <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> 平移。按住 <kbd>Shift</kbd> 平移更快。
*   可以通过将鼠标悬停在源代码/预览窗格之间的边框上并用鼠标拖动来调整其大小。
*   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>中：
    *   源代码/预览可以左右布局（通过 <span class="tn-icon bx bxs-dock-left"></span>）或下上布局（通过 <span class="tn-icon bx bxs-dock-bottom"></span>）。
    *   按下 <span class="tn-icon bx bx-copy"></span>（_复制图片引用到剪贴板_）即可将图表的图片表示插入到文本笔记中。更多信息请参阅<a class="reference-link" href="Text/Images/Image%20references.md">图片引用</a>。
*   要将图表导出为 SVG 或 PNG，请转到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>并选择_导出为图片_：
    *   选择_SVG（矢量）_以下载图表的可缩放/矢量渲染。可用于展示图表，缩放时不会降低质量。
    *   选择_PNG（栅格）_以下载图表的普通图片（1x 比例，栅格）。可用于通过电子邮件等更传统的渠道发送图表。
*   该笔记可以标记为[只读](../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)，此时默认切换到预览（尽管可以使用源代码/预览按钮切换回来），并且源代码不再可编辑。

## 图表中的错误

如果源代码中存在错误，错误将显示在信息窗格中。

在错误状态下，图表将不再渲染，之前正常工作的图表将保留在预览部分。

## 文本笔记中的图表

要在<a class="reference-link" href="Text.md">文本</a>笔记中而不是在其自己的笔记中显示图表，请使用 <span class="tn-icon cke cke-plus"></span> _插入_菜单中的 <span class="tn-icon cke cke-trilium-mermaid-insert"></span> _Mermaid 图表_按钮插入一个。它具有与 Mermaid 笔记相同的视图、缩放和错误显示，其源代码作为代码块保留在文本笔记中。请参阅<a class="reference-link" href="Text/Insert%20buttons.md">插入按钮</a>中的_Mermaid 图表_。