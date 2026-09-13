# 新布局
_新布局_ 是 v0.101.0 中引入的一系列 UI/UX 变更，这些变更大幅改变了现有的 UI 元素，同时也添加了一些新元素。这个新布局的目标是使应用程序现代化、更加直观，同时减少杂乱。

## 新引入的功能

### 状态栏

在窗口底部有一个新的栏，称为_状态栏_。这个栏包含多个项目，例如面包屑导航以及关于当前笔记的信息和设置，例如[内容语言](../../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md)和<a class="reference-link" href="../../Advanced%20Usage/Attributes.md">属性</a>。

有关更多信息，请参阅[专门页面](New%20Layout/Status%20bar.md)。

<figure class="image"><img style="aspect-ratio:1150/27;" src="5_New Layout_image.png" width="1150" height="27"></figure>

### 内联标题

在之前版本的 Trilium 中，标题栏始终固定。在新布局中，既有固定的标题栏，也有随文本滚动的标题栏。新引入的标题称为_内联标题_，它以更大的字体显示标题，同时还显示创建日期和修改日期等附加信息。

每当标题滚动过去时，将改为显示固定标题。

这仅影响<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记。占据整个屏幕的笔记类型，例如<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>和<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>，将始终只有固定标题栏。

根据笔记类型的不同，内联标题还会提供一些更具交互性的选项，例如能够切换笔记类型（见下文）。

<figure class="image"><img style="aspect-ratio:899/122;" src="New Layout_image.png" width="899" height="122"><figcaption><em>内联标题</em>，显示在笔记顶部，可以滚动过去。</figcaption></figure><figure class="image"><img style="aspect-ratio:910/104;" src="4_New Layout_image.png" width="910" height="104"><figcaption>固定标题栏。只有在滚动过<em>内联标题</em>后才会显示标题。</figcaption></figure>

### 新的笔记类型切换器

当创建新的<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记时，_内联标题_下方会出现一个笔记类型切换器。除了更改笔记类型外，还可以应用[模板](../../Advanced%20Usage/Templates.md)。

一旦输入文本，切换器就会消失。

<img src="6_New Layout_image.png" width="735" height="143">

### 笔记徽章

笔记徽章出现在固定笔记标题附近，指示关于笔记的重要信息，例如它是否为只读。其中一些徽章也是可交互的。

<figure class="image"><img style="aspect-ratio:910/49;" src="3_New Layout_image.png" width="910" height="49"></figure>

以下徽章可用：

*   **只读徽章**，如果笔记由于自动只读或手动只读而不可编辑，则会显示。点击徽章将临时编辑笔记（类似于编辑[浮动按钮](Floating%20buttons.md)）。
*   **共享徽章**，表示当前笔记已共享。该徽章还会指示共享是在本地网络上（对于未设置<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>的桌面应用程序）还是可公开访问（对于服务器）。
*   **网页剪藏徽章**，表示笔记是否使用<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏器</a>剪藏。该徽章充当链接，因此可以点击它导航到页面，或右键单击以获取更多选项。
*   **执行徽章**，用于具有执行按钮或描述的[脚本](../../Scripting.md)或[保存的 SQL 查询](../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md)。

其中一些徽章取代了笔记顶部的专用面板。

### 可折叠区域

<figure class="image"><img style="aspect-ratio:496/265;" src="1_New Layout_image.png" width="496" height="265"></figure>

以下区域已变为可折叠：

*   _提升的属性_
    *   对于全高笔记，例如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>，提升的属性默认折叠以腾出空间。
    *   以前用于触发提升的属性功能区选项卡的键盘快捷键（已不再工作）已被重新用于切换提升的属性。
*   _已编辑的笔记_，出现在<a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>中，现在显示在标题下方。
    *   该区域是否折叠取决于<a class="reference-link" href="Options.md">选项</a> → 外观中的选择。
*   _搜索属性_，出现在完整的<a class="reference-link" href="../Navigation/Search.md">搜索</a>和<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>中。

### 保存状态指示器

<img class="image-style-align-right" src="2_New Layout_image.png" width="168" height="47">在笔记标题右侧，对文档进行更改后会临时出现一个指示器，指示文档是否已保存。

它指示以下状态：

*   _未保存_，如果更改将很快保存。
*   _保存中_，如果更改正在保存。
*   _已保存_，如果所有更改已成功保存到服务器。
*   _错误_，如果更改无法保存，例如由于与服务器通信失败。

在所有更改保存后，指示器将在几秒钟后自动隐藏。

## 更改为现有布局

### 移除功能区

最显著的变化是移除了功能区。功能区中的所有操作和选项已集成到应用程序的其他位置。

以下是曾经属于功能区的所有不同选项卡现在在新布局中的可用方式：

*   “格式工具栏”已重新定位到页面顶部。
    *   现在每个选项卡只有一个格式工具栏，而不是每个分屏一个。这为工具栏项目提供了更多空间。
*   “拥有的属性”和“继承的属性”已合并并移动到状态栏区域（一个显示在另一个上方）。
*   “基本属性”已集成到<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>菜单中。
    *   唯一的例外是语言组合框，现在可以在状态栏中找到（屏幕右上角）。
*   “文件”和“图像”选项卡
    *   按钮已移动到笔记标题右侧，作为<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>中的专用条目。
    *   信息区域已合并到状态栏的_笔记信息_区域中。
*   已编辑的笔记
    *   移动到标题下方，显示在可折叠区域下，笔记以徽章/标签形式表示。
    *   该区域是展开还是折叠取决于选项 → 外观中的“已编辑的笔记功能区选项卡将在日记笔记上自动打开”设置。
*   搜索定义选项卡
    *   移动到标题下方的可折叠区域。
    *   对于新搜索默认展开，对于保存的搜索默认折叠。
*   笔记地图现在可在笔记操作菜单中使用。
    *   笔记地图不再在功能区面板中打开，而是在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中打开，在那里也可以最大化。
*   “笔记信息”选项卡已移动到状态栏中的一个小 (i) 图标。
*   “相似笔记”选项卡
    *   相似笔记不再在功能区面板中打开，而是现在显示在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中。
*   集合属性选项卡已重新定位到笔记标题下方，并分组为：
    *   一个用于快速切换视图的组合框。
    *   子菜单中当前视图的单独设置。
*   一些较小的功能区选项卡已转换为徽章，出现在面包屑区域的笔记标题附近：
    *   剪藏网页的原始 URL 指示器（`#pageUrl`）。
    *   SQL 和脚本执行按钮。

> [!NOTE]
> 功能区键盘快捷键（例如 `toggleRibbonTabClassicEditor`）已被重新用于新布局，它们将切换相应的面板。

### 移除浮动按钮

大多数按钮已重新定位到笔记标题右侧的<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>区域，但以下除外：

*   编辑按钮显示在笔记标题附近，作为徽章。
*   _反链_ 现在显示在侧边栏的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>中。
    *   或者，反链计数显示在状态栏中，点击时侧边栏会在右侧区域打开。
*   关系图缩放按钮现在是关系图本身的一部分。
*   导出图像为 PNG/SVG 现在在笔记操作菜单中的_导出为图像_选项中。

### 侧边栏的变更

侧边栏（也称为右侧面板）也收到了一些重要变更。

最重要的是，v0.105.0 将侧边栏拆分为多个选项卡，并增加了额外功能：

*   <a class="reference-link" href="Right%20Sidebar/Outline%20tab.md">大纲选项卡</a>，汇集了目录和高亮列表。
*   <a class="reference-link" href="Right%20Sidebar/Attributes%20tab.md">属性选项卡</a>，提供了一种图形化方法来编辑标签、关系和（提升的）属性定义。
*   一个专用的<a class="reference-link" href="Right%20Sidebar/AI%20chat%20tab.md">AI 对话选项卡</a>。
*   <a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>，将笔记地图、笔记路径、反链和相似笔记分组在一起。

之前版本的侧边栏会根据是否有任何项目要显示而上下文地出现。这在分屏视图中在两个窗格之间移动时偶尔会导致内容偏移。在新布局中，侧边栏更像<a class="reference-link" href="Note%20Tree.md">笔记树</a>窗格，即使没有任何内容要显示也保持可见。

为了切换侧边栏，屏幕右上角有一个新按钮，靠近窗口按钮（在 Windows 和 Linux 上）。

现在侧边栏的每个区域（例如“目录”、“高亮列表”）都可以单独折叠，并会记住是否已折叠。

一些侧边栏项目还有上下文菜单，由标题上的三个点表示。例如，可以直接从该菜单调整高亮过滤器。

仍然支持自定义小组件。对于自定义脚本，三个点菜单允许快速导航到相应的脚本笔记。

## 如何切换新布局

从 v0.101.0 开始，此新布局默认启用。可以通过转到<a class="reference-link" href="Options.md">选项</a> → 外观并选择_旧布局_来回退到旧布局。

> [!IMPORTANT]
> 由于引入了新布局，它成为标准布局。_旧布局_被视为已弃用，不会获得新功能（例如面包屑），因为我们将重点放在新布局上。在某个时候，旧布局将被完全移除，因为维护两个具有重大差异的布局会造成维护负担。