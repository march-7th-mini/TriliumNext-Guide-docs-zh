# 移动端前端
<figure class="image image-style-align-right image_resized" style="width:33.52%;"><img style="aspect-ratio:1242/2688;" src="Mobile Frontend_IMG_1765.PNG" width="1242" height="2688"></figure>

Trilium 拥有一个针对触屏设备（智能手机和平板电脑）优化的移动端 Web 前端。它会在登录过程中根据浏览器检测自动激活。

与完整的桌面版相比，移动端前端的功能较为有限。详情请见下文。

## 布局基础

与桌面版不同，移动版的 UI 略有差异，旨在更好地适配手机有限的屏幕空间。

以下是桌面版与移动版之间差异的非详尽列表：

*   在手机上，<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>位于笔记下方。屏幕左上角的 <span class="tn-icon bx bx-chevron-left"></span> 按钮会将笔记滑开以显示树，而从树中打开笔记则会将其滑回。
    *   从屏幕左边缘滑动也会显示树，但根据平台不同，系统或浏览器的返回手势可能会将其接管。
    *   每个标签页都会记住它之前显示的是树还是笔记，切换标签页时会恢复该状态。
    *   在 Android 应用中，系统返回手势或按钮会先关闭顶部的菜单或对话框，然后关闭 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> 中的设置页面，接着将笔记滑开以显示树，最后在树中向上返回一级。在树的顶层，它会把应用切换到后台。
    *   在更宽的屏幕上（例如横屏的平板电脑），笔记树会作为侧边栏显示在笔记旁边。此时，<span class="tn-icon bx bx-sidebar"></span> 按钮用于隐藏和显示它，该选择会与桌面版的左侧面板一起被记住。
    *   有子笔记的笔记会显示子笔记数量和一个 <span class="tn-icon bx bx-chevron-right"></span>：点击它会列出其子笔记，点击任何其他笔记则会打开该笔记。
    *   长按笔记可显示 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Quick%20search.md">快速搜索</a> 栏也显示在笔记树的顶部。
*   完整的 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a> 功能可以从 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> 或（如果已配置）<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a> 中触发。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> 更简短：省略了 _新建窗口_ 和 _键盘快捷键_，而 _切换到桌面版_ 位于 _高级_ 下。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a> 显示在屏幕底部。
    *   启动栏的图标配置与桌面版不同。有关如何配置的更多信息，请参阅专门页面。
*   大多数与笔记相关的操作都集中在笔记右上角的水平三点图标中。
*   在文本笔记中，格式工具栏位于屏幕底部。请参阅下方的 _编辑文本笔记_。
*   在 iOS 上，标题行、启动栏、格式工具栏、从屏幕底部打开的菜单以及短对话框的按钮都是半透明的面板，悬浮在屏幕边缘之外，笔记会在标题行和启动栏下方滚动。高度超过屏幕一半的对话框则是不透明的，并附着在屏幕底部。要使面板变为不透明，请转到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _外观_ → _性能_，然后关闭 _菜单、弹出窗口和面板的背景效果_。在 Android 上，该选项不显示，它们始终是不透明的。
*   当屏幕键盘打开时，键盘正上方右下角的 <span class="tn-icon bx bxs-keyboard"></span> 按钮会将其隐藏。在文本笔记中，该按钮位于格式工具栏的右端。当格式工具栏的菜单代替键盘就地打开时，该按钮会变为 <span class="tn-icon bx bx-x"></span>，用于关闭菜单并恢复键盘。这在所有笔记类型和所有文本字段中都有效，并且是在 iOS 应用中隐藏键盘的唯一方式，因为该平台的键盘没有 _完成_ 按钮。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Tabs.md">标签页</a> 集中在 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a> 中的标签页切换器下，标签页以全屏网格形式显示并带有预览以便于切换，此外还有重新打开已关闭标签页等附加选项。
*   自 v0.100.0 起，<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Split%20View.md">分屏视图</a> 也可在移动视图中使用，但最多同时显示两个窗格。分屏以垂直而非水平方式显示。

## 编辑文本笔记

### 格式工具栏

在文本笔记中，格式工具栏位于屏幕底部，为单行并可横向滚动。它仅在你编辑文本时显示，当你隐藏键盘或移动到其他字段（如笔记标题）时会隐藏。从左到右，它包含：

*   _撤销_ 和 _重做_，因为屏幕键盘没有对应的按键。
*   一个高亮按钮，显示光标所在的元素名称，例如 _表格 ›_ 或 _列表 ›_（当光标位于其中时）。请参阅下方的 _表格、图片和其他元素_ 以及 _列表_。
*   <span class="tn-icon cke cke-trilium-block-type"></span> 块类型按钮、<span class="tn-icon cke cke-plus"></span> 用于插入内容，以及 <span class="tn-icon cke cke-text"></span> 用于应用于文本的格式。
*   <span class="tn-icon cke cke-link"></span> 用于添加链接，<span class="tn-icon cke cke-paper-clip"></span> 用于附加文件。
*   缩进按钮，然后是 <span class="tn-icon cke cke-arrow-up"></span> 和 <span class="tn-icon cke cke-arrow-down"></span>，用于将当前块或选中的块向上或向下移动，效果如同键盘上的 <kbd>Alt</kbd>+<kbd>↑</kbd> 和 <kbd>Alt</kbd>+<kbd>↓</kbd>。在表格内，它们移动的是行。
*   <span class="tn-icon cke cke-trilium-ai"></span> AI 助手按钮，在配置了提供商后显示，它会在屏幕底部以菜单形式打开其快捷操作，顶部为 _询问 AI…_。

当键盘打开时，工具栏右端的 <span class="tn-icon bx bxs-keyboard"></span> 按钮会将其隐藏。

编辑器角落中解释光标下元素的提示（例如待办事项的状态及其快捷键）不会显示，无论 _选项_ → _文本笔记_ → _功能_ 下的 _内容提示_ 设置如何。

### 插入内容

<span class="tn-icon cke cke-plus"></span> 按钮会在屏幕底部以磁贴形式打开插入项：

*   图片、表格和待办列表。
*   代码块、块引用和警示框。
*   较少使用的折叠块、标签页、分栏、水平线、分页符、脚注、数学公式、绘图画布、Mermaid 图表、书签、链接和内容嵌入、特殊字符、表情符号、图标、日期/时间、模板和 Markdown 导入。

图片也位于回形针下，待办列表、代码块、块引用和警示框也位于块类型按钮中。

带有 <span class="tn-icon bx bx-chevron-right"></span> 标记的磁贴会打开一个选项列表：

*   _代码块_：语言。
*   _警示框_：其类型。
*   _插入表格_：表格的大小。
*   _分栏_：列数。
*   _脚注_：新建脚注或引用现有脚注。
*   _日期/时间_：日期和时间的格式。
*   _插入文本片段_：要插入的模板。当没有模板时，该项为灰色。

### 块类型

<span class="tn-icon cke cke-trilium-block-type"></span> 块类型按钮会在屏幕底部以磁贴形式打开块类型，当前类型会高亮显示：

*   段落和标题 2 至 6。
*   项目符号列表、编号列表和待办列表。
*   代码块、块引用和警示框。

在列表中选择段落或标题会将该项恢复为纯文本，代码块同理。块引用和警示框会包裹当前块而非替换它，因此它们会与当前块一起高亮显示；再次选择即可移除。

在行首输入 `-`、`1.` 或 `[ ]` 也会开始一个列表。

### 列表

当光标位于列表中时，_列表 ›_ 按钮会跟在 _撤销_ 和 _重做_ 之后。其所在行包含：

*   缩进按钮以及将项向上或向下移动的按钮，与主行相同。
*   _列表类型_，它会以磁贴形式打开待办列表以及项目符号列表和编号列表的标记（例如方块或罗马数字），标记按类别分组，当前标记会高亮显示。选择其他类别的磁贴也会将列表转换为该类别，例如将项目符号列表转换为编号列表，或将待办列表转换回项目符号列表。
*   在编号列表中，_起始于_ 用于询问列表的起始编号，以及 <span class="tn-icon bx bx-sort-down"></span> _逆序_，当列表倒序计数时会高亮显示。
*   在待办列表中，每个任务状态对应一个按钮，其后是 <span class="tn-icon bx bx-pencil"></span> 用于编辑状态。

从块类型按钮、插入菜单或通过输入 `-`、`1.` 或 `[ ]` 开始列表时，会立即显示此行。一旦你点击返回按钮，它就会保持关闭，直到你开始另一个列表。

### 表格、图片和其他元素

当光标位于表格、图片、代码块、链接或桌面版中拥有自己工具栏的其他元素中时，一个高亮按钮（显示该元素名称，例如 _表格 ›_）会跟在 _撤销_ 和 _重做_ 之后。它会用该元素的工具栏替换格式工具栏，该工具栏以一个返回按钮开头（用于再次关闭它），随后是元素名称及其工具。当光标离开该元素时，该按钮会消失。

整体选中某个元素（例如图片）或点击链接会立即显示其工具栏；点击返回按钮可返回格式工具栏。

元素工具栏中带有选项列表的按钮（例如表格的列和行操作）会在屏幕底部以菜单形式打开该列表，其中处于开启或关闭状态的选项（例如表格的表头行）以开关形式呈现。

### 格式化文本

应用于文本的格式（粗体、斜体、下划线、删除线、行内代码、上标和下标、键盘快捷键、字体大小和颜色，以及移除格式）位于单独一行，其后是当前块的左对齐、居中、右对齐和两端对齐，当前对齐方式会高亮显示。该行以 <span class="tn-icon cke cke-trilium-scissors"></span> 结尾，用于将选区剪切为子笔记。

*   点击 <span class="tn-icon cke cke-plus"></span> 按钮之后的 <span class="tn-icon cke cke-text"></span> 可显示它，点击其开头的 <span class="tn-icon cke cke-previous-arrow"></span> 可返回主行。
*   选中文本会单独显示此行，一旦选区消失（例如当你开始输入时），它就会返回主行，除非你在此期间自行打开或关闭了该行。

字体大小按钮会在屏幕底部以菜单形式打开大小列表，每个选项以其对应大小绘制，当前选项会被勾选。

单个颜色按钮取代了单独的文本颜色和背景颜色按钮。它会打开一个菜单，其中一行用于文本颜色，一行用于背景颜色，每行都有一个移除颜色的单元格和一个打开设备取色器的单元格。

### 链接和附件

<span class="tn-icon cke cke-link"></span> 链接按钮取代了单独的链接和内部链接按钮。它会打开 _添加链接_ 对话框，可链接到笔记或网址；当光标位于链接内时，则打开 _编辑链接_。该对话框不会自动打开键盘；点击笔记或地址字段即可输入。同一按钮也位于文本格式行中（在内联样式之后），用于将选中的文本转换为链接。

<span class="tn-icon cke cke-paper-clip"></span> 按钮以列表形式打开 _图片_、_相机_、_附加并嵌入文件_ 和 _将文件作为链接附加_：即桌面工具栏的菜单，并添加了 _相机_。_相机_ 会打开设备相机并插入拍摄的照片；其他选项则打开设备的文件选择器。

## 安装为 PWA

移动视图可以设置为 PWA。虽然这不提供任何离线功能，但它会以全屏方式显示应用，并便于通过手机主屏幕访问。

=== "<span class="tn-icon bx bxl-apple"></span> iOS 使用 Safari"

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的 \[…\] 按钮并选择共享。
    4.  向下滚动以显示完整项目列表，然后选择 _添加到主屏幕_。
    5.  按 _添加_，该 Web 应用即可使用。

=== "<span class="tn-icon bx bxl-chrome"></span> Android 使用 Google Chrome"

    > [!IMPORTANT]
    > Google Chrome 要求服务器通过 HTTPS 提供服务才能以全屏显示。如果使用 HTTP，应用将显示为普通网页（类似于书签）。

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右上角的三个垂直点图标并选择 _添加到主屏幕。_
    4.  选择 _安装_ 选项。
    5.  选择一个合适的名称。
    6.  该 Web 应用将作为应用出现，而非在主屏幕上。

=== "Android 使用 Brave"

    > [!IMPORTANT]
    > Brave 要求服务器通过 HTTPS 提供服务才能以全屏显示。如果使用 HTTP，应用将显示为普通网页（类似于书签）。

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的三个垂直点图标并选择 _添加到主屏幕_。
    4.  按 _安装_ 选项。
    5.  该 Web 应用将作为应用出现，而非在主屏幕上。

=== "Samsung Browser"

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的汉堡菜单。
    4.  选择 _添加到_，然后选择 _主屏幕_。
    5.  按 _添加_，该 Web 应用将出现在主页上。

## 分享到 Trilium

在 Android 上安装为 PWA 后，Trilium 会出现在系统的分享菜单中，因此可以从其他应用将链接、文本、图片和其他文件发送到它。分享的内容会保存到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>，Trilium 会打开它创建的笔记：

*   文本或链接会变为文本笔记。分享的链接还会存储在 `#pageUrl` 标签中。
*   单个文件会变为图片笔记或文件笔记，直接放置在收件箱中。
*   多个文件，或与文本一起分享的文件，会放置在一个包含该文本的新文本笔记下。

以这种方式创建的每个笔记都带有 `#clipType=share` 标签，这会给分享的文本笔记加上 <span class="tn-icon bx bx-share"></span> 图标，除非该笔记有自己的 `#iconClass`。单次分享最多可携带 20 个文件。

> [!NOTE]
> 分享需要处于登录状态。如果会话已过期，请重新登录并再次分享。

## 通过桌面应用进行测试

如果你在没有专用[服务器安装](Server%20Installation.md)的情况下运行 Trilium，你仍然可以使用桌面应用测试移动应用。更多信息请参阅 <a class="reference-link" href="Desktop%20Installation/Using%20the%20desktop%20application%20as%20a%20server.md">将桌面应用用作服务器</a>。要访问它，请转到 `http://<ip>:37840/login?mobile`。

## 强制使用移动/桌面前端

Trilium 会自动决定使用移动端还是桌面端前端。如果这不合适，你可以在**登录**页面使用 `?mobile` 或 `?desktop` 查询参数（注意：你可能需要先登出）。

或者，只需在 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> 中选择 _切换到移动版_。在移动版中，则在那里选择 _高级_ → _切换到桌面版_。

## 脚本

你可以像普通前端一样，通过 <a class="reference-link" href="../Scripting.md">脚本</a> 更改行为。要使脚本笔记被执行，它们需要带有 `#run=mobileStartup` 标签。

也支持自定义 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a> 小组件。