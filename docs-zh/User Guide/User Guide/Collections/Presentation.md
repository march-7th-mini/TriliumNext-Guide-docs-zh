# 演示

<figure class="image"><img style="aspect-ratio:1120/763;" src="Presentation_image.png" width="1120" height="763"></figure>

演示视图允许直接在 Trilium 中创建幻灯片。

### 创建新演示

在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击现有笔记，选择*插入子笔记*，然后查找*演示*。

## 工作原理

*   每张幻灯片是集合的子笔记。
*   子笔记的顺序决定幻灯片的顺序。
*   与传统演示软件不同，幻灯片可以水平或垂直排列（详见下文）。
*   直接子笔记将水平排列，而这些子笔记的子笔记将垂直排列。超过两层嵌套的子笔记将被忽略。

## 交互与导航

在浮动按钮区域（右上角）：

*   编辑按钮可跳转到当前幻灯片对应的笔记。
*   按概览按钮（或 <kbd>O</kbd> 键）可显示幻灯片的鸟瞰视图。再次按下该按钮可关闭。
*   按“开始演示”按钮可以全屏显示演示。

支持以下键盘快捷键：

*   按 <kbd>←</kbd> 和 <kbd>→</kbd>（或 <kbd>H</kbd> 和 <kbd>L</kbd>）可跳转到左侧或右侧的幻灯片（水平方向）。
*   按 <kbd>↑</kbd> 和 <kbd>↓</kbd>（或 <kbd>K</kbd> 和 <kbd>J</kbd>）可跳转到上方或下方的幻灯片（垂直方向）。
*   按 <kbd>Space</kbd> 和 <kbd>Shift</kbd> + <kbd>Space</kbd> 可按顺序跳转到下一张/上一张幻灯片。
*   还有更多快捷键，按 <kbd>?</kbd> 可显示包含所有支持的键盘组合的弹窗。

## 垂直幻灯片与嵌套

与 Microsoft PowerPoint 等传统演示软件不同，Trilium 中的幻灯片可以水平或垂直排列，以创建层次感或更好地按主题组织幻灯片。

这种水平/垂直组织方式会影响过渡效果（尤其是“滑动”过渡），但在导航中最为明显。

*   按 <kbd>←</kbd> 和 <kbd>→</kbd> 将水平导航幻灯片，从而跳过当前幻灯片下的垂直笔记。这对于跳过整个章节/相关幻灯片非常有用。
*   按 <kbd>↑</kbd> 和 <kbd>↓</kbd> 将在当前层级中垂直导航幻灯片。
*   按 <kbd>Space</kbd> 和 <kbd>Shift</kbd> + <kbd>Space</kbd> 将按顺序跳转到下一张/上一张幻灯片，无论方向如何。这通常是演示时使用的按键组合。
*   幻灯片右下角的箭头也会反映此导航方案。

<figure class="image image-style-align-right image_resized" style="width:55.57%;"><img style="aspect-ratio:890/569;" src="1_Presentation_image.png" width="890" height="569"></figure>

集合的所有直接子笔记将水平排列。如果直接子笔记也有子笔记，这些子笔记将作为垂直幻灯片放置。

在以下示例中，笔记结构如下：

*   演示集合
    *   Trilium Notes（演示页面）
    *   “介绍”幻灯片
        *   “个人知识管理的挑战”
        *   “笔记结构”
    *   “演示与功能亮点”幻灯片
        *   “极快的安装过程”
        *   视频幻灯片

## 自定义

在集合级别，可以调整：

*   通过前往<a class="reference-link" href="Collection%20Properties.md">集合属性</a>并查找*主题*选项，将整个演示的主题调整为预定义主题之一。
*   目前无法创建自定义主题，但已在计划中。
*   请注意，无法通过<a class="reference-link" href="../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a> 修改 CSS，因为幻灯片是隔离渲染的（在 shadow DOM 中）。

在幻灯片级别：

*   可以通过使用[预定义提升属性](../Advanced%20Usage/Attributes/Promoted%20Attributes.md)来调整幻灯片的背景颜色，或手动将 `#slide:background` 设置为十六进制颜色。
*   更复杂的背景可以通过渐变实现。没有对应的 UI；必须通过 `#slide:background` 设置为 CSS 渐变定义，例如：`linear-gradient(to bottom, #283b95, #17b2c3)`。

## 提示与技巧

*   文本笔记通常遵循格式（粗体、斜体、前景色和背景色）和字体大小。代码块和表格也可以使用。
*   尝试使用不仅仅是文本笔记，演示使用与[共享笔记](../Advanced%20Usage/Sharing.md)和<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>相同的机制，因此它应该能够全屏显示<a class="reference-link" href="../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>、<a class="reference-link" href="../Note%20Types/Canvas.md">Canvas</a> 和<a class="reference-link" href="../Note%20Types/Mind%20Map.md">思维导图</a>（不含交互功能）。
    *   如果幻灯片有自定义背景，考虑为 <a class="reference-link" href="../Note%20Types/Canvas.md">Canvas</a> 使用透明背景（前往 Canvas 中的汉堡菜单，按下按钮选择自定义颜色并输入 `transparent`）。
    *   对于 <a class="reference-link" href="../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>，其中一些有预定义的背景，可以通过 frontmatter 更改。例如，对于 XY 图表：
        
        ```
        ---
        config:
            themeVariables:
                xyChart:
                    backgroundColor: transparent
        ---
        ```

## 底层实现

演示视图使用 [Reveal.js](https://revealjs.com/) 来处理幻灯片的导航和布局。