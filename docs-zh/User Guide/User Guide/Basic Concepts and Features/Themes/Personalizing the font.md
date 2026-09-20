# 个性化字体
## 使用不同的字体

Trilium 默认自带自己的字体（_Inter_），但可以在 <a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _外观_ 中，通过勾选 _字体_ 部分下的 _使用不同字体_ 来调整字体。

可以为应用程序的以下区域个性化字体：

*   界面文本，用于大部分 UI（菜单、工具栏、对话框）。
*   <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>。
*   文档文本，用于笔记的实际内容（尤其是 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a> 笔记）。
*   等宽文本，例如用于 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记和 <a class="reference-link" href="../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>。

每个区域也有自己的 _大小_。笔记树和文档大小相对于界面大小，因此更改界面大小会随之改变它们。

字体列表包含以下项目：

*   **通用字体**
    *   _主题定义_，使用当前[主题](../Themes.md)中嵌入的字体。例如在默认的现代主题上，字体是 _Inter_。这不需要安装该字体。
    *   _系统默认_，使用最适合[桌面应用](../../Installation%20%26%20Setup/Desktop%20Installation.md)的字体组合。例如在 Windows 上它会使用 _Segoe UI_。
    *   带衬线（例如类似 _Times New Roman_）、无衬线和等宽的通用字体选择。
*   **Web 字体**，出现在 <a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a> 上，是一个预定义的字体列表，分为无衬线、衬线、等宽和手写。你的系统不支持的字体（即未安装的）不会显示。
*   **系统字体**，出现在 <a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 上。与预定义的服务器字体不同，系统字体是从你的操作系统列出的。
*   **自定义字体**，允许使用任何字体，只要它被导入到 Trilium 中。更多信息请参见下面的部分。

字体更改在重新加载后生效；一旦有更改，该部分会提供一个 _重新加载以应用更改_ 按钮。

## 自定义字体

导入到 Trilium 中的字体文件可以被应用程序本身使用，无需编写任何 CSS。

### 添加字体

1.  导入字体文件，方法是将其拖入 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 或通过 _导入到笔记_。可识别 TrueType（`.ttf`）、OpenType（`.otf`）和 Web 开放字体格式（`.woff`、`.woff2`）文件；笔记会采用字体的名称（不含扩展名），并标记为字体图标（一个“A”图标）。
2.  选择生成的笔记，其中会显示字体预览：一行用于输入你自己文本的示例行、一个用于调整大小的滑块、多种大小的预览，以及拉丁字符集。
3.  打开示例上方的 _在字体选择器中_。
4.  在 <a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _外观_ → _字体_ 中，该字体现在会显示在 _自定义字体_ 下，位于内置字体族之前，并且可以为四个区域中的任意一个设置。

> [!NOTE]
> 嵌入式 OpenType（`.eot`）文件和 TrueType 集合（`.ttc`）无法被浏览器绘制，因此它们会被视为普通文件：没有预览，也不会在选择器中显示条目。

### 自定义字体的行为方式

*   每个条目以其笔记命名，因此重命名笔记会重命名该条目。该设置引用的是笔记本身而不是其名称，并且在重命名后仍然有效。
*   字体文件是普通笔记，因此 <a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a> 会将其带到你的其他设备。字体选择不会同步：外观设置被有意保留为每台设备独立，因此在另一台设备上字体已经存在，只需再次选择即可。
*   保存在[受保护笔记](../Notes/Protected%20Notes.md)中的字体只能在受保护会话打开时预览和使用。

对于主题作者，字体也可以通过 <a class="reference-link" href="../../Advanced%20Usage/Custom%20Resource%20Providers.md">自定义资源提供程序</a> 嵌入到主题的 CSS 中，当字体应随主题一起提供而不是在设置中选择时，这是应采用的方式。

### 从 Google Fonts 下载

可以从 Google Fonts 轻松获取大量字体，方法如下：

1.  前往 [https://fonts.google.com](https://fonts.google.com)。
2.  搜索所需的字体。
3.  点击右上角的 _Get font_。
4.  检查左侧的字体列表是否与你的选择相对应。
5.  点击 _Download all_。
6.  在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中，创建一个用于存储新字体的笔记。
7.  在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中，将 .zip 文件直接拖放到新建的笔记上，然后按照上一部分的步骤操作。

## 编程连字

某些字体支持编程连字，这会在 <a class="reference-link" href="../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a> 和 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记中将诸如 `!=` 之类的字符组合转换为 `≠`，或将 `->` 转换为 `→`。

这些只是显示上的便利，因此复制文本不受影响。无论如何，可以通过在字体设置中取消勾选 _编程连字_ 来在 Trilium 中禁用此功能。