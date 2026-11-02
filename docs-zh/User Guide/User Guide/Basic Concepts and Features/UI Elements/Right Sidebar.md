# 右侧边栏
<figure class="image"><img style="aspect-ratio:1990/1168;" src="Right Sidebar_image.png" width="1990" height="1168"></figure>

右侧边栏显示当前笔记的特定内容。该边栏分为多个标签页：

*   <a class="reference-link" href="Right%20Sidebar/Outline%20tab.md">大纲标签页</a>，根据笔记类型显示目录、高亮以及其他与导航相关的部分。
*   <a class="reference-link" href="Right%20Sidebar/Attributes%20tab.md">属性标签页</a>，为当前笔记的<a class="reference-link" href="../../Advanced%20Usage/Attributes.md">属性</a>提供可视化编辑器。
*   <a class="reference-link" href="Right%20Sidebar/AI%20chat%20tab.md">AI对话标签页</a>，使用<a class="reference-link" href="../../AI.md">AI</a>集成进行对话，并可选择访问当前笔记。
*   <a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接标签页</a>，将笔记地图、笔记路径、反链和相似笔记分组在一起。

每个窗口保留各自选中的标签页，因此在一个窗口中切换标签页不会影响其他窗口。新打开的窗口会从上次选中的标签页开始。

## 切换右侧边栏

有两种方式可以切换右侧边栏：

*   通过标题栏附近的 <span class="tn-icon bx bx-sidebar bx-flip-horizontal"></span> 图标，用于切换边栏是否停靠。
*   通过 _切换右侧面板_ [键盘快捷键](../Keyboard%20Shortcuts.md)，该快捷键默认未分配。

## 窥视边栏

应用右侧边缘附近有一个小条，显示一个箭头图标。

*   当边栏隐藏时，按下该边缘将_窥视_边栏。
    *   在此模式下，边栏会临时显示在内容上方，而不会移动笔记内容。
    *   在窥视模式下点击边栏外部将直接隐藏边栏。X 按钮和点击右侧边缘也是如此。
    *   按下固定图标将停靠边栏。
*   当边栏已停靠时，按下该边缘将隐藏边栏（类似于顶部的切换图标）。

_窥视右侧面板_ [键盘快捷键](../Keyboard%20Shortcuts.md)，默认为 <kbd>Alt</kbd>+<kbd>]</kbd>，与按下该条的效果相同。

## 移动端支持

在移动端，右侧边栏由笔记面板替代，该面板通过 <a class="reference-link" href="Note%20menu.md">笔记菜单</a> 旁边的 <span class="tn-icon bx bx-dock-bottom"></span> 按钮从屏幕底部以表单形式打开。

*   标签页通过表单底部的栏进行切换。与桌面端一样，对当前笔记没有可显示内容的标签页会被省略，而_小组件_标签页列出脚本的[右侧面板小组件](../../Scripting/Frontend%20Basics/Custom%20Widgets/Right%20pane%20widget.md)。
*   标签页的各个部分以卡片形式依次显示，每张卡片上方有其名称，而不是可折叠的部分。
*   表单的头部显示标签页的名称，但在_属性_和_AI对话_标签页中，头部改为放置它们的按钮（参见<a class="reference-link" href="Right%20Sidebar/Attributes%20tab.md">属性标签页</a>和<a class="reference-link" href="Right%20Sidebar/AI%20chat%20tab.md">AI对话标签页</a>）。
*   点击目录中的标题、PDF 的页面或注释，会关闭面板并将笔记滚动到相应位置。