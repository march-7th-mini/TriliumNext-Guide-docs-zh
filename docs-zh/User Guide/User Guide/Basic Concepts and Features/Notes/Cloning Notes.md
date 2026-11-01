# 克隆笔记
## 动机

Trilium 的核心功能是能够将你的笔记组织成层次化的树状结构。

因此，你预计会拥有一个精细且深入的笔记层次结构——每个子树都代表你知识库中一个更精细、更专业的视图。

这是一种非常强大的方法，但它也隐含了一个假设：每个“子主题”都“归属”于一个父级。我用一个例子来说明——假设我的基本结构是这样的：

*   技术
    *   编程
        *   Kotlin
        *   JavaScript
    *   操作系统
        *   Linux
        *   Windows

现在，我开始学习 [Bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\))，并想创建与此主题相关的笔记。但现在我面临一个问题：该把它归类到哪里。问题在于，Bash 既是一种编程语言，也是一个与 Linux 密切相关的工具（shell）。它似乎同时属于这两者，我无法（也不想）二选一。

## 解决方案

上述问题的解决方案是允许笔记拥有多个父级。

我称之为“克隆”，但这有点误导——并不存在原始笔记和克隆笔记之分——两个父级分类中的笔记是完全相同的。

关于“克隆”的另一个误导之处在于，它暗示已经创建了笔记的副本。这并不完全正确，笔记本身只保留一个原始版本，它只是在树形层次结构中的多个位置被引用。因此，在一个分类中修改它，会同时改变所有其他分类中的它，因为它们都是同一条笔记。

以下是使用克隆后的最终结构：

*   技术
    *   编程
        *   Kotlin
        *   JavaScript
        *   Bash
            *   一些子笔记……
    *   操作系统
        *   Linux
            *   Bash
                *   一些子笔记……
        *   Windows

所以现在“Bash”子树出现在层次结构中的多个位置。两个 Bash 子树是相同的，包含相同的子分类和笔记。

### 演示

![](Cloning%20Notes_create-clone.gif)

在演示中，你可以看到如何使用上下文菜单创建克隆。也可以使用添加链接对话框或 <kbd>Ctrl</kbd>+<kbd>C</kbd> 和 <kbd>Ctrl</kbd>+<kbd>V</kbd> [键盘快捷键](../Keyboard%20Shortcuts.md) 来实现。

你可以查看所有可用克隆的列表：

*   在 <a class="reference-link" href="../UI%20Elements/Status%20bar.md">状态栏</a> 中，查找 <span class="tn-icon bx bx-directions"></span> 图标。
*   在 <a class="reference-link" href="../UI%20Elements/Right%20Sidebar.md">右侧边栏</a> 的 <a class="reference-link" href="../UI%20Elements/Right%20Sidebar/Connections%20tab.md">连接标签页</a> 中，查看 _笔记路径_ 部分。

在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中，无论是在桌面端还是移动端，克隆笔记的标题后面都会跟着一个 <span class="tn-icon bx bxs-directions"></span> 图标，以便轻松看出该笔记也被放置在其他位置。共享笔记同样会跟着一个 <span class="tn-icon bx bx-share-alt"></span> 图标。

## 删除笔记/克隆

对于克隆，删除的工作方式可能不会立即显而易见。

如果你尝试删除一条笔记，其工作方式如下：

1.  如果该笔记有多个克隆，只删除这个克隆，保留实际笔记（及其其他克隆）不变。
2.  如果该笔记没有任何其他克隆，则删除该笔记
    *   对所有笔记的子笔记从第 1 步开始执行整个流程