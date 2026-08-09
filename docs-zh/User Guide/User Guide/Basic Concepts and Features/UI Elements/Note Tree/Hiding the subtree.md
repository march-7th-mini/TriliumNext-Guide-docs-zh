# 隐藏子树
<figure class="image image-style-align-right"><img style="aspect-ratio:328/45;" src="1_Hiding the subtree_image.png" width="328" height="45"><figcaption>一个包含相对大量子笔记的集合示例，这些子笔记在树中被隐藏。</figcaption></figure>

当笔记按层级结构组织，使得条目数量保持较少时，树形结构工作良好。当一个笔记拥有大量子笔记（数量级在数千或数万）时，会出现两个问题：

*   在笔记之间导航变得繁琐，树本身也会被大量笔记弄得杂乱无章。
*   大量的笔记会显著降低应用程序的运行速度。

自 v0.102.0 版本起，Trilium 允许树隐藏特定笔记的子笔记。此功能适用于<a class="reference-link" href="../../../Collections.md">集合</a>和普通笔记。

## 交互

当笔记的子树被隐藏时，会有一些细微的变化：

*   为了指示子树已被隐藏，该笔记将不会显示展开按钮，并会在右侧显示子笔记的数量。
*   无法直接从树中添加新笔记。
    *   对于<a class="reference-link" href="../../../Collections.md">集合</a>，最好使用内置机制来创建笔记（例如，在地图上创建新点，或在表格中添加新行）。
    *   对于普通笔记，仍然可以通过其他方式创建子笔记，例如使用<a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>系统。
*   笔记可以从外部拖入，在这种情况下，它们将被克隆到该笔记中。
    *   不会切换到被复制的子笔记，而是会高亮显示父笔记。
    *   会有通知提示此行为。
*   类似地，剪切/复制然后粘贴到笔记中的功能也将正常工作。

## 聚焦显示

<figure class="image image-style-align-right"><img style="aspect-ratio:322/83;" src="Hiding the subtree_image.png" width="322" height="83"></figure>

即使笔记的子树被隐藏，如果某个子笔记被激活，它仍会以一种称为_聚焦显示_的特殊状态出现在树中。

在此状态下，该笔记保持在其正常的层级位置，以便于确定其位置。此外，这意味着：

*   使用<a class="reference-link" href="../../Navigation/Search.md">搜索</a>时，笔记的位置清晰可见。
*   仍然可以从树中对该笔记进行操作，例如添加<a class="reference-link" href="../../Notes/Cloning%20Notes/Branch%20prefix.md">分支前缀</a>或将其移出集合。

该笔记以斜体显示，表示其为临时显示。当切换到另一个笔记时，聚焦显示的笔记将消失。

> [!NOTE]
> 一次只能高亮显示一个笔记。当处理多个笔记（例如将它们拖入集合）时，不会有笔记被聚焦显示。这是有意为之，以避免显示子树的部分状态。

## 处理集合

对于大型集合，出于性能考虑或整理树的整洁度，隐藏其子笔记可能会有所帮助。

要切换此行为：

*   打开集合，在<a class="reference-link" href="../../../Collections/Collection%20Properties.md">集合属性</a>中，找到_在树中隐藏子笔记_。
*   在<a class="reference-link" href="../Note%20Tree.md">笔记树</a>中右键点击集合笔记，然后选择_高级_ → _显示子树_。

## 处理普通笔记

也可以为普通笔记隐藏子树，而不仅仅是集合。为此，在<a class="reference-link" href="../Note%20Tree.md">笔记树</a>中右键点击笔记，然后选择_高级_ → _隐藏子树_。