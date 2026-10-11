# 保存的搜索
Trilium 允许你将常用搜索保存为笔记树中的笔记。搜索结果将显示在这些“保存的搜索”笔记下作为子笔记。以下是一个示例说明其工作方式：

<figure class="image image-style-align-center image_resized" style="width:50%;"><img style="aspect-ratio:812/585;" src="Saved Search_saved-search.gif" width="812" height="585"></figure>

保存的搜索会在你打开它时运行，也会在笔记树中展开它时运行。位于未显示的标签页中的保存搜索（例如启动时恢复的后台标签页）会在你切换到该标签页时运行。其结果会一直保留，直到你使用搜索参数中的 _搜索_ 按钮再次运行搜索。如果查询有错误，会以通知的形式显示。

在<a class="reference-link" href="../Advanced%20Usage/Safe%20mode.md">安全模式</a>下，以及当请求失败时，搜索不会自行运行。按 _立即搜索_ 来运行它。

一旦搜索被保存，_搜索参数_ 仍然可以在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Title.md">标题</a>下方找到，以便之后能够更改设置，但默认情况下它会以折叠状态显示。

## 位置

默认情况下，保存的搜索存储在日记笔记中。但是，你可以通过使用 `#searchHome` 标签来指定一个不同的笔记来存储保存的搜索。此外，对于[工作区](../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md)，你可以使用 `#workspaceSearchHome` 标签来指定该工作区内保存搜索的存储位置。