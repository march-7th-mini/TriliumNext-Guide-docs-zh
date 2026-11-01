# 书签

常用的笔记可以添加书签，这样它们就会出现在<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中，方便访问。

## 配置启动栏

如果书签没有出现在启动栏中，那么很可能是书签区域被隐藏了。从<a class="reference-link" href="../UI%20Elements/Global%20menu.md">全局菜单</a>进入<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>配置，确保 _书签_ 位于 _可见启动器_ 区域中。

## 书签文件夹

左侧面板的空间有限，而你可能想为许多项目添加书签。一个可行的解决方案是为文件夹添加书签，这样它就会显示其子项：

为此，先为一个文件夹添加书签，然后在<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中右键单击其按钮并勾选 _显示为文件夹_。此后该按钮会打开一个菜单，而不是直接打开笔记本身：笔记位于顶部，其后是它的子项。取消勾选 _显示为文件夹_ 即可将其恢复为普通书签。

如果某个子项自身还有子项，则会在其行末显示一个箭头。单击箭头可在子菜单中列出其子项，或单击该行的其余部分以打开笔记。子菜单最多可嵌套四层。如果菜单列出的子项超过 15 个，则会在其上方显示一个筛选字段：输入标题的一部分即可只列出匹配的笔记。如果某个笔记的子树被隐藏（参见<a class="reference-link" href="../UI%20Elements/Note%20Tree/Hiding%20the%20subtree.md">隐藏子树</a>），那么它在这里也不会列出其子项。

菜单中的笔记打开方式与链接相同：中键单击或 <kbd>Ctrl</kbd>+单击会在新标签页中打开笔记，<kbd>Shift</kbd>+单击会在新窗口中打开它，而右键单击则会列出其他可以打开它的位置。

_显示为文件夹_ 会为笔记分配 `#bookmarkFolder` 标签，因此手动添加该标签也同样有效。由于该标签属于笔记本身，一个既被添加了书签又被拖放到启动栏上的笔记，会在两个位置都显示其子项。

## 选择书签的打开位置

书签会在当前标签页中打开其笔记。要在其他位置打开，请在<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中右键单击其按钮，然后在 _打开模式_ 下选择一个位置。当前生效的位置会被勾选。

| _打开模式_ | 标签值 | 笔记打开的位置 |
| --- | --- | --- |
| _当前标签页_ | `currentTab` | 在当前标签页中。这是默认值。 |
| _新标签页_ | `newTab` | 在当前标签页之后的新标签页中（参见<a class="reference-link" href="../UI%20Elements/Tabs.md">标签页</a>）。 |
| _新分屏_ | `newSplit` | 在当前笔记旁边的新分屏中（参见<a class="reference-link" href="../UI%20Elements/Split%20View.md">分屏视图</a>）。 |
| _新窗口_ | `newWindow` | 在新窗口中。 |
| _快速编辑_ | `quickEdit` | 在当前笔记上方的弹出窗口中（参见<a class="reference-link" href="Quick%20edit.md">快速编辑</a>）。 |

_打开模式_ 会在笔记上设置 `#bookmarkOpenMode` 标签，因此手动添加该标签也同样有效。该标签对于拖放到启动栏上的笔记以及书签文件夹菜单中的笔记，作用方式相同。对于文件夹，_打开模式_ 会使该标签可继承，因此文件夹菜单及其子菜单中的每个笔记都会遵循它，包括文件夹自身的笔记（参见<a class="reference-link" href="../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>）。文件夹中的笔记仍然可以拥有自己的值，例如手动添加的 `currentTab`。

打开模式仅适用于普通单击。中键单击或 <kbd>Ctrl</kbd>+单击仍会在新标签页中打开笔记，而在文件夹菜单中的笔记上使用 <kbd>Shift</kbd>+单击仍会在新窗口中打开它。

## 移动端

在移动端，书签仅从 v0.102.0 开始显示。由于屏幕尺寸更为受限，书签会分组在一个图标下，而不是作为单独的图标显示。

按下后，会出现一个菜单，列出所有书签。书签文件夹也受支持，并会显示为子菜单。每个子菜单都以其自身的笔记开头，因此带有子项的笔记既可以打开也可以浏览。

在手机上，当<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>显示未提升的标签页根节点时，书签也会列在笔记树的顶部，位于<a class="reference-link" href="Workspaces.md">工作区</a>下方。点击书签即可打开它，或者对于带有子项的书签，则列出其子项，与笔记树中的其他笔记相同。