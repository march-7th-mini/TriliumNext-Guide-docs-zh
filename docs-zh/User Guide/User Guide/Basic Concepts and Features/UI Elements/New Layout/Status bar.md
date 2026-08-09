# 状态栏

状态栏显示当前笔记的信息，并允许更改与其相关的设置，例如配置语言或属性。

## 布局与交互

左侧显示<a class="reference-link" href="Breadcrumb.md">面包屑</a>，指示当前笔记及其父笔记，并允许在整个层级结构中快速导航。

右侧会根据当前笔记的类型显示特定部分。

1.  对于<a class="reference-link" href="../../../Note%20Types/Code.md">代码</a>笔记，会显示笔记的语言模式（例如 JavaScript、纯文本），并允许轻松切换到其他模式。
2.  对于<a class="reference-link" href="../../../Note%20Types/Text.md">文本</a>笔记，会显示内容语言且可以更改，从而配置拼写检查和从右到左支持。
    1.  请注意，与某些文本编辑器不同，这适用于整个笔记而非选中部分。
3.  如果笔记在树中被放置在多个位置（已克隆），则会显示笔记路径的数量。
    1.  点击它将在侧边栏的<a class="reference-link" href="../Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中显示笔记路径的完整列表。
4.  如果笔记有附件，则会显示其数量。
    1.  点击它将在新选项卡中显示附件列表。
5.  如果笔记被其他文本笔记链接（反链），则会显示反链的数量。
    1.  点击它将在侧边栏的<a class="reference-link" href="../Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中显示链接到此笔记的笔记列表，以及引用该笔记位置的摘录。

无论笔记类型如何，只要存在笔记，以下项目将始终显示：

1.  笔记信息，显示：
    1.  笔记的创建/修改日期。
    2.  笔记的类型和 MIME。
    3.  笔记 ID。
    4.  笔记本身及其子笔记的大小估算。
    5.  一个按钮，用于在侧边栏的<a class="reference-link" href="../Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中显示相似笔记。

> [!注意]
> 当按下显示<a class="reference-link" href="../Right%20Sidebar.md">右侧边栏</a>的按钮时，如果侧边栏处于隐藏状态，则具有特定行为：侧边栏将临时显示而非停靠。无论哪种情况，侧边栏都将切换到相应的选项卡，并且相应的部分将被高亮显示。