# 个性化字体

## 使用不同字体

Trilium 默认自带字体（_Inter_），但可以通过在 <a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _外观_ 中勾选 _字体_ 部分的 _使用不同字体_ 来调整字体。

可以为应用程序的以下区域个性化字体：

*   界面文本，涵盖大部分 UI（菜单、工具栏、对话框）。
*   <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>。
*   文档文本，用于笔记的实际内容（尤其是 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a> 笔记）。
*   等宽文本，例如用于 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记和 <a class="reference-link" href="../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>。

每个区域也有自己的 _大小_。笔记树和文档的大小相对于界面大小，因此更改界面大小会同时调整它们。

字体列表包含以下项目：

*   **通用字体**
    *   _主题定义_，使用当前 [主题](../Themes.md) 内嵌的字体。例如，在默认的现代主题中，字体是 _Inter_。这不需要安装该字体。
    *   _系统默认_，使用最适合 [桌面应用](../../Installation%20%26%20Setup/Desktop%20Installation.md) 的字体组合。例如，在 Windows 上它将使用 _Segoe UI_。
    *   通用字体选择，包括衬线字体（例如类似 _Times New Roman_ 的字体）、无衬线字体和等宽字体。
*   **Web 字体**，出现在 <a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a> 上，这是一个预定义的字体列表，分为无衬线、衬线、等宽和手写体。系统不支持的字体（即未安装的）不会显示。
*   **系统字体**，出现在 <a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 上。与预定义的服务器字体不同，系统字体是从您的操作系统中列出的。
*   **自定义字体**，允许使用任何已导入 Trilium 的字体。更多信息请参见下文。

字体更改在重新加载后生效；一旦有所更改，该部分会提供一个 _重新加载以应用更改_ 按钮。

## 自定义字体

导入 Trilium 的字体文件可以被应用程序本身使用，而无需编写任何 CSS。

### 添加字体

1.  将字体文件拖入 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 或通过 _导入到笔记_ 来导入字体文件。TrueType (`.ttf`)、OpenType (`.otf`) 和 Web Open Font Format (`.woff`、`.woff2`) 文件会被识别；笔记会采用不带扩展名的字体名称，并标记有字体图标（一个“A”图标）。
2.  选择生成的笔记，其中将显示字体预览：一个用于输入您自己文本的样本行、一个大小滑块、多种大小的预览以及拉丁字符集。
3.  在样本上方打开 _在字体选择器中显示_。
4.  在 <a class="reference-link" href="../UI%20Elements/Options.md">选项</a> → _外观_ → _字体_ 中，该字体现在会在 _自定义字体_ 下提供，位于内置字体族之前，并且可以设置为四个区域中的任何一个。

> [!注意]
> 嵌入式 OpenType (`.eot`) 文件和 TrueType 集合 (`.ttc`) 无法由浏览器绘制，因此它们被视为普通文件：没有预览，也没有字体选择器中的条目。

### 自定义字体的行为

*   每个条目以其笔记命名，因此重命名笔记会重命名条目。该设置引用的是笔记本身而不是其名称，并且在重命名后仍然有效。
*   字体文件是一个普通笔记，因此 <a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a> 会将其传送到您的其他设备。字体选择不会同步：外观设置特意按设备保留，因此在另一台设备上字体已经存在，只需再次选择即可。
*   保存在 [受保护笔记](../Notes/Protected%20Notes.md) 中的字体只能在受保护会话打开时进行预览和使用。

对于主题作者，还可以通过 <a class="reference-link" href="../../Advanced%20Usage/Custom%20Resource%20Providers.md">自定义资源提供程序</a> 将字体嵌入主题的 CSS 中。当字体应随主题附带而不是在设置中选择时，应采用此途径。

### 从 Google Fonts 下载

可以轻松地从 Google Fonts 获取大量字体，步骤如下：

1.  前往 [https://fonts.google.com](https://fonts.google.com)。
2.  搜索所需字体。
3.  点击右上角的 _获取字体_。
4.  检查左侧的字体列表是否与您的选择相符。
5.  点击 _全部下载_。
6.  在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中，创建一个笔记来存储新字体。
7.  在 <a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a> 中，将 .zip 文件直接拖放到新创建的笔记上，然后按照上一节的步骤操作。