# 工作区

工作区是建立在[笔记提升](Note%20Hoisting.md)之上的概念。它基于这样一种理念：用户有多个不同的兴趣领域。例如“个人”和“工作”，这两个领域相当独立，彼此之间没有交互。当我专注于工作时，我并不关心个人笔记。

到目前为止，工作区包含以下功能：

*   [笔记提升](Note%20Hoisting.md) - 你可以“缩放”到工作区子树中，只关注相关的笔记
*   轻松进入工作区：
    
    ![](1_Workspaces_image.jpg)
*   在标签页中可视化识别工作区：
    ![](Workspaces_image.jpg)

### 配置

| 标签 | 描述 |
| --- | --- |
| `workspace` | 将此笔记标记为工作区，进入工作区的按钮由此控制 |
| `workspaceIconClass` | 定义当提升到此笔记时在标签页中使用的盒子图标 CSS 类 |
| `workspaceTabBackgroundColor` | 当提升到此笔记时在笔记标签页中使用的 CSS 颜色，可使用任何 CSS 颜色格式，例如 "lightblue" 或 "#ddd"。参见 [https://www.w3schools.com/cssref/css\_colors.asp](https://www.w3schools.com/cssref/css_colors.asp)。 |
| `workspaceCalendarRoot` | 使用此标签标记笔记将为<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>定义一个新的按工作区划分的日历。如果没有这样的笔记，将使用全局日历。 |
| `workspaceTemplate` | 此笔记将出现在创建新笔记时可用模板的选择中，但仅在提升到包含此模板的工作区时才会出现 |
| `workspaceSearchHome` | 当提升到此工作区笔记的某个祖先节点时，新的搜索笔记将作为此笔记的子笔记创建 |
| `workspaceInbox` | 当提升到此工作区笔记的某个祖先节点时，新笔记的默认收件箱位置。更多信息请参见<a class="reference-link" href="../Notes/Note%20Inbox.md">笔记收件箱</a>。 |