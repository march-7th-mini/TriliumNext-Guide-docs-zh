# 状态栏

状态栏显示当前笔记的信息，并允许更改与其相关的设置，例如配置语言或属性。

## 布局与交互

在左侧，显示 <a class="reference-link" href="Breadcrumb.md">面包屑导航</a>，它指示当前笔记及其父笔记，并允许在整个层级中快速导航。

在右侧，将根据当前笔记的类型显示特定部分。

1.  对于<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记，会指示笔记的语言模式（例如 JavaScript、纯文本），并允许轻松切换到其他模式。
    1.  在其之前，光标位置以行和列的形式显示，例如 _Ln: 12 Col: 32_。它会随着光标移动而更新。当选中文本时，随后会显示选中的字符数，例如 _Selected: 120_。
2.  对于<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记，会显示内容语言并可以更改，从而配置拼写检查和从右到左支持。
    1.  请注意，这适用于整个笔记而非选区，与某些文本编辑器不同。
    2.  当在选项中开启<a class="reference-link" href="../../Note%20Types/Text/Vim%20mode.md">Vim 模式</a>时，一个 _Vim_ 徽章可为该笔记开启或关闭该模式，其后跟随 Vim 的当前模式。
3.  如果笔记被放置在树中的多个位置（克隆），则会显示笔记路径的数量。
    1.  点击它会打开一个弹出窗口，其中包含笔记路径的完整列表，也可以从中将笔记克隆到新位置。相同的列表可在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中找到。
4.  如果笔记有附件，则会显示其数量。Trilium 为其自身生成的系统附件（参见<a class="reference-link" href="../Notes/Attachments.md">附件</a>）不计入其中。
    1.  点击它将在新选项卡中显示附件列表。
5.  如果笔记被其他文本笔记链接（反链），则会显示反链的数量。
    1.  点击它会打开一个弹出窗口，其中包含链接到此笔记的笔记列表，以及引用该笔记位置的摘录。相同的列表可在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中找到。

无论笔记类型如何，只要存在笔记，以下项目将始终显示：

1.  笔记信息，显示：
    1.  笔记的创建/修改日期。
    2.  笔记的类型和 MIME。
    3.  笔记 ID。
    4.  笔记本身及其子笔记大小的估计值。
    5.  一个按钮，用于在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中显示相似笔记。

> [!NOTE]
> 当按下显示<a class="reference-link" href="Right%20Sidebar.md">右侧边栏</a>的按钮时，如果侧边栏处于隐藏状态，则会有特定行为：侧边栏将被窥视而非停靠。无论如何，侧边栏将切换到相应的选项卡，并且相应的部分将被高亮显示。