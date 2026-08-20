# 新布局
_新布局_ 是在 v0.101.0 中引入的一系列 UI/UX 更改，它极大地改变了现有的 UI 元素，并添加了一些新元素。此新布局的目标是使应用程序现代化、更直观，同时减少杂乱。

## 新引入的功能

### 状态栏

窗口底部有一个名为 _状态栏_ 的新栏。此栏包含多个项目，例如面包屑导航以及当前笔记的信息和设置，例如[内容语言](../../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md)和<a class="reference-link" href="../../Advanced%20Usage/Attributes.md">属性</a>。

更多信息，请查阅[专门页面](New%20Layout/Status%20bar.md)。

<figure class="image"><img style="aspect-ratio:1150/27;" src="5_New Layout_image.png" width="1150" height="27"></figure>

### 内联标题

在以前的 Trilium 版本中，标题栏始终固定。在新布局中，既有固定的标题栏，也有随文本滚动的标题栏。新引入的标题称为 _内联标题_，它以更大的字体显示标题，同时还显示创建和修改日期等附加信息。

当标题滚动过去后，将显示固定标题。

这仅影响<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>和<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记。占据整个屏幕的笔记类型，如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>，将始终只有固定的标题栏。

根据笔记类型的不同，内联标题还会提供一些更交互式的选项，例如能够切换笔记类型（见下文）。

<figure class="image"><img style="aspect-ratio:899/122;" src="New Layout_image.png" width="899" height="122"><figcaption>_内联标题_，显示在笔记顶部，可以滚动过去。</figcaption></figure><figure class="image"><img style="aspect-ratio:910/104;" src="4_New Layout_image.png" width="910" height="104"><figcaption>固定标题栏。只有在滚动过 _内联标题_ 后才会出现。</figcaption></figure>

### 新的笔记类型切换器

当创建新的<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>或<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记时，_内联标题_ 下方会出现一个笔记类型切换器。除了更改笔记类型，还可以应用[模板](../../Advanced%20Usage/Templates.md)。

一旦输入文本，切换器将消失。

<img src="6_New Layout_image.png" width="735" height="143">

### 笔记徽章

笔记徽章出现在固定笔记标题附近，指示有关笔记的重要信息，例如它是否为只读。某些徽章也是可交互的。

<figure class="image"><img style="aspect-ratio:910/49;" src="3_New Layout_image.png" width="910" height="49"></figure>

可用的徽章如下：

*   **只读徽章**，如果笔记由于自动只读或手动只读而无法编辑，则会显示。点击徽章将临时编辑笔记（类似于编辑[浮动按钮](Floating%20buttons.md)）。
*   **分享徽章**，指示当前笔记已共享。该徽章还会指示共享是在本地网络上（对于未设置<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>的桌面应用程序）还是可公开访问（对于服务器）。
*   **网页剪藏徽章**，指示笔记是否使用<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏器</a>剪藏。该徽章充当链接，因此可以点击导航到页面或右键单击以获取更多选项。
*   **执行徽章**，用于具有执行按钮或描述的[脚本](../../Scripting.md)或[已保存的 SQL 查询](../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md)。

其中一些徽章取代了笔记顶部的专用面板。

### 可折叠部分

<figure class="image"><img style="aspect-ratio:496/265;" src="1_New Layout_image.png" width="496" height="265"></figure>

以下部分已变为可折叠：

*   _提升属性_
    *   对于全高笔记（如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>），提升属性默认折叠以腾出空间。
    *   以前用于触发提升属性功能区选项卡（已不再起作用）的键盘快捷键已被重新用于切换提升属性。
*   _已编辑笔记_，出现在<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记</a>中，现在显示在标题下方。
    *   该部分是否折叠取决于<a class="reference-link" href="Options.md">选项</a> → 外观中的选择。
*   _搜索属性_，出现在完整的<a class="reference-link" href="../Navigation/Search.md">搜索</a>和<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">已保存搜索</a>中。

### 保存状态指示器

<img class="image-style-align-right" src="2_New Layout_image.png" width="168" height="47">在笔记标题的右侧，对文档进行更改后会出现一个临时指示器，指示文档是否已保存。

它指示以下状态：

*   _未保存_，如果更改即将保存。
*   _正在保存_，如果更改正在保存中。
*   _已保存_，如果所有更改都已成功保存到服务器。
*   _错误_，如果更改无法保存，例如由于与服务器的通信问题。

在所有更改都保存后，指示器会在几秒钟后自动隐藏。

## 对现有布局的更改

### 移除功能区

最显著的变化是移除了功能区。功能区中的所有操作和选项都已集成到应用程序的其他位置。

以下是曾经属于功能区的不同选项卡现在在新布局中的可用方式：

*   “格式工具栏”已移至页面顶部。
    *   现在每个标签页只有一个格式工具栏，而不是每个分栏一个。这为工具栏项目提供了更多空间。
*   “自有属性”和“继承属性”已合并并移至状态栏区域（上下显示）。
*   “基本属性”已集成到<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>菜单中。
    *   唯一的例外是语言组合框，现在可以在状态栏（屏幕右上角）中找到它。
*   “文件”和“图片”选项卡
    *   按钮已移至笔记标题右侧，作为<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>中的专用条目。
    *   信息部分已合并到状态栏的 _笔记信息_ 部分。
*   已编辑笔记
    *   移至标题下方，显示在可折叠区域下，笔记以徽章/标签形式呈现。
    *   该部分是展开还是折叠取决于选项 → 外观中的“已编辑笔记功能区选项卡将在日记中自动打开”设置。
*   搜索定义选项卡
    *   移至标题下方的可折叠区域。
    *   对于新搜索默认展开，对于已保存搜索默认折叠。
*   笔记地图现在可以在笔记操作菜单中找到。
    *   笔记地图不再是打开到功能区中的面板，而是在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中打开，并且可以最大化。
*   “笔记信息”选项卡已移至状态栏中的一个小 (i) 图标。
*   “相似笔记”选项卡
    *   相似笔记不再是打开到功能区中的面板，而是在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中显示。
*   集合属性选项卡已移至笔记标题下方，并分组为：
    *   一个用于快速切换视图的组合框。
    *   子菜单中当前视图的单独设置。
*   一些较小的功能区选项卡已转换为出现在面包屑区域中笔记标题附近的徽章：
    *   剪藏网页的原始 URL 指示器（`#pageUrl`）。
    *   SQL 和脚本执行按钮。

> [!注意]
> 功能区键盘快捷键（例如 `toggleRibbonTabClassicEditor`）已被重新用于新布局，它们将切换相应的面板。

### 移除浮动按钮

大多数按钮已移至笔记标题右侧的<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>区域，但以下情况除外：

*   编辑按钮作为徽章显示在笔记标题附近。
*   _反链_ 现在显示在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中。
    *   或者，反链计数显示在状态栏中，点击时侧边栏会在相应部分打开。
*   关系图缩放按钮现在是关系图本身的一部分。
*   导出图像为 PNG/SVG 现在位于笔记操作菜单中的 _导出为图像_ 选项下。

### 侧边栏的更改

侧边栏（也称为右侧面板）也进行了一些重要的更改。

最重要的是，v0.105.0 将侧边栏拆分为多个具有附加功能的选项卡：

*   <a class="reference-link" href="Right%20Sidebar/Outline%20tab.md">大纲选项卡</a>，汇集了目录和高亮列表。
*   <a class="reference-link" href="Right%20Sidebar/Attributes%20tab.md">属性选项卡</a>，提供了一种编辑标签、关系和（提升的）属性定义的图形化方法。
*   一个专用的<a class="reference-link" href="Right%20Sidebar/AI%20chat%20tab.md">AI对话选项卡</a>。
*   <a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>，将笔记地图、笔记路径、反链和相似笔记组合在一起。

以前版本的侧边栏会根据是否有要显示的项目而按上下文显示。这导致在分屏视图中的两个窗格之间移动时偶尔会发生内容偏移。在新布局中，侧边栏更像<a class="reference-link" href="Note%20Tree.md">笔记树</a>窗格，即使没有要显示的内容也保持可见。

为了切换侧边栏，屏幕右上角靠近窗口按钮（在 Windows 和 Linux 上）有一个新按钮。

现在侧边栏的每个部分（例如“目录”、“高亮列表”）都可以单独折叠，并会记住其折叠状态。

一些侧边栏项目也有上下文菜单，由标题上的三个点表示。例如，可以直接从该菜单调整高亮过滤器。

自定义组件仍然受支持。对于自定义脚本，三点菜单允许快速导航到相应的脚本笔记。

## 如何切换新布局

从 v0.101.0 开始，此新布局默认启用。可以通过转到<a class="reference-link" href="Options.md">选项</a> → 外观并选择 _旧布局_ 来回退到旧布局。

> [!重要]
> 由于引入了新布局，这已成为标准布局。_旧布局_ 被视为已弃用，并且不会获得新功能（例如面包屑），因为我们专注于新布局。在某个时候，旧布局将被完全移除，因为维护两个差异巨大的布局会造成维护负担。