# 笔记菜单
<figure class="image image-style-align-right image_resized" style="width:25.95%;"><img style="aspect-ratio:402/988;" src="Note menu_image.png" width="402" height="988"></figure>

笔记菜单包含针对当前笔记的各种操作和配置。它位于<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>区域（<a class="reference-link" href="../Notes/Title.md">标题</a>的右侧）。

每个分屏都有各自的笔记菜单，作用于该分屏中显示的笔记。不适用于当前笔记的条目仍会列出，但会显示为灰色；而仅存在于某些笔记上的条目（在_笔记特定条目_中描述）只会在这些笔记上出现。

## 导航笔记

这些条目是菜单顶部的一行图标，每个图标都有一个简短的标题。将鼠标悬停在某个图标上会显示其完整名称和键盘快捷键。在手机上的快速编辑中，由于只剩下_查找_，它会作为普通条目列出。

*   <span class="tn-icon bx bx-file-find"></span> _查找_会打开<a class="reference-link" href="../Navigation/Search%20in%20note.md">在笔记中搜索</a>栏，用于在当前笔记中查找和替换文本。在桌面应用程序中，同一栏可通过 <kbd>Ctrl</kbd>+<kbd>F</kbd> 打开。
    *   它适用于<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>、<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>、<a class="reference-link" href="../../Note%20Types/Mind%20Map.md">思维导图</a>和<a class="reference-link" href="../../Note%20Types/Spreadsheets.md">电子表格</a>笔记、<a class="reference-link" href="../../Collections.md">集合</a>、PDF 文件，以及任何以<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>形式显示的笔记。
*   <span class="tn-icon bx bx-paperclip"></span> _附件_会将笔记切换到其<a class="reference-link" href="../Notes/Attachments.md">附件</a>列表，在那里可以上传、打开、下载、重命名或删除附件。
*   <span class="tn-icon bx bxs-network-chart"></span> _笔记地图_会打开<a class="reference-link" href="Right%20Sidebar.md">右侧边栏</a>的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>，其中显示以当前笔记为中心的<a class="reference-link" href="../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记地图（链接地图、树状地图）</a>。

## 笔记属性

此部分中的开关会立即生效：

*   <span class="tn-icon bx bx-share-alt"></span> _共享_会通过<a class="reference-link" href="../../Advanced%20Usage/Sharing.md">共享</a>功能发布笔记，将其克隆到_共享笔记_树中。
    *   关闭它会从该树中移除克隆。如果笔记仅作为共享笔记存在，Trilium 会要求确认，因为取消共享会删除它。
    *   该开关在根笔记、_共享笔记_笔记本身以及系统笔记上不可用。
*   <span class="tn-icon bx bx-lock-alt"></span> _保护笔记_会加密笔记，将其变为<a class="reference-link" href="../Notes/Protected%20Notes.md">受保护的笔记</a>之一。如果没有活动的受保护会话，Trilium 会先要求输入密码。只有当前笔记受影响，其子笔记不受影响。
*   <span class="tn-icon bx bx-bookmark"></span> _书签_会将笔记添加到<a class="reference-link" href="Launch%20Bar.md">启动栏</a>中显示的<a class="reference-link" href="../Navigation/Bookmarks.md">书签</a>中，或从中移除。
*   <span class="tn-icon bx bx-copy-alt"></span> _模板_会将笔记标记为<a class="reference-link" href="../../Advanced%20Usage/Templates.md">模板</a>之一（通过添加 `#template` 标签），使其在创建新笔记时可用。
*   <span class="tn-icon bx bx-expand-horizontal"></span> _全宽_通过添加 `#fullContentWidth` 标签，让笔记使用窗口的整个宽度，而不是<a class="reference-link" href="Content%20width.md">内容宽度</a>中设置的限制。对于始终以全宽显示的笔记类型，不会列出此项。

此部分中的两个子菜单：

*   <span class="tn-icon bx bx-file"></span> _笔记类型_会将笔记的类型更改为任何<a class="reference-link" href="../../Note%20Types.md">笔记类型</a>；当前类型会被勾选。如果笔记已有内容，Trilium 会先要求确认，因为内容通常不会保留。<a class="reference-link" href="../../Note%20Types/Converting%20between%20note%20types.md">在笔记类型之间转换</a>。
    *   对于<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记，语言是在<a class="reference-link" href="Status%20bar.md">状态栏</a>中选择的。
*   <span class="tn-icon bx bx-edit-alt"></span> _可编辑_控制笔记何时以只读方式打开（参见<a class="reference-link" href="../Notes/Read-Only%20Notes.md">只读笔记</a>）：
    *   _自动_（默认）：笔记可编辑，除非它足够长以至于自动以只读方式打开。
    *   _只读_：笔记始终以只读方式打开，但在按下_编辑笔记_后仍可编辑。
    *   _始终可编辑_：无论长度如何，笔记始终可编辑。

## 导入、导出和打印

*   <span class="tn-icon bx bx-import"></span> _导入文件_会打开导入对话框，将文件作为当前笔记的子笔记导入。参见<a class="reference-link" href="../Import%20%26%20Export.md">导入与导出</a>。它在<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>笔记上不可用。
*   <span class="tn-icon bx bx-export"></span> _导出笔记_会打开导出对话框，并选中_仅此笔记_；在那里选择_此笔记及所有后代_以导出整个子树。
*   <span class="tn-icon bx bx-printer"></span>_打印/导出为 PDF…_会打印笔记或将其保存为 PDF 文件。参见<a class="reference-link" href="../Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印与导出为 PDF</a>，包括哪些笔记类型和集合可以打印。

某些笔记类型会在_导出笔记_正下方添加自己的导出格式：

*   <span class="tn-icon bx bxs-file-image"></span>_导出为图片_，在<a class="reference-link" href="../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>和<a class="reference-link" href="../../Note%20Types/Mind%20Map.md">思维导图</a>笔记上，将图表下载为 _PNG（栅格）_ 或 _SVG（矢量）_。
*   <span class="tn-icon bx bxs-spreadsheet"></span>_导出为 Excel (.xlsx)_ 和 _导出为 CSV (.csv)_，在<a class="reference-link" href="../../Note%20Types/Spreadsheets.md">电子表格</a>上，以这些格式下载电子表格。

## 修订

这些条目管理笔记的<a class="reference-link" href="../Notes/Note%20Revisions.md">笔记修订</a>：

*   <span class="tn-icon bx bx-history"></span>_笔记修订…_会打开修订对话框，在那里可以预览、与当前版本比较、下载或恢复以前的版本。其旁边的箭头会打开立即保存修订的条目。在移动端，点击它会打开这些条目，其中_笔记修订…_排在第一位。
    *   <span class="tn-icon bx bx-save"></span>_保存修订_会立即保存笔记的修订，而不是等待下一次自动快照。
    *   <span class="tn-icon bx bx-purchase-tag"></span>_保存命名修订…_也会立即保存修订，但会先要求输入更改的简短描述，该描述会显示在修订对话框中。

## 笔记特定条目

以下条目仅出现在某些笔记上：

*   <span class="tn-icon bx bx-pencil"></span>_编辑笔记_在笔记当前为只读时出现在菜单顶部。它会启用编辑，直到笔记关闭。
*   <span class="tn-icon bx bx-align-justify"></span>_自动换行_出现在<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记的菜单顶部，设置此笔记中的长行是否换行：
    *   _自动_（默认）遵循<a class="reference-link" href="Options.md">选项</a> → _代码笔记_ → _在代码笔记中换行_。
    *   _开_和_关_通过设置 `#wrapLines` 标签仅为此笔记覆盖该设置。
*   <span class="tn-icon bx bx-paperclip"></span>_转换为附件_出现在没有子笔记且只有一个父笔记（为<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记）的图片笔记上。确认后，它会将图片变为其父笔记的附件并在那里打开。参见<a class="reference-link" href="../Notes/Attachments.md">附件</a>。
*   <span class="tn-icon bx bx-extension"></span>_重新渲染笔记_出现在<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>上，会再次运行其脚本以刷新输出。
*   <span class="tn-icon bx bx-cog"></span>_看板属性_出现在<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>上，配置其列、卡片属性和卡片模板。
*   <span class="tn-icon bx bx-cog"></span>_日历属性_出现在创建事件的<a class="reference-link" href="../../Collections/Calendar.md">日历</a>上，配置其事件模板。
*   <span class="tn-icon bx bx-cog"></span>_地理地图属性_出现在<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>上，配置其地图设置以及[图片地图](../../Collections/Geo%20Map/Image%20maps.md)的图片。
*   <span class="tn-icon bx bx-cog"></span>_表格属性_出现在<a class="reference-link" href="../../Collections/Table.md">表格</a>上，配置它显示哪些笔记。

## 高级

<span class="tn-icon bx bx-wrench"></span>_高级_子菜单将较少使用的操作分组：

*   <span class="tn-icon bx bx-file-find"></span>_在外部打开笔记_（仅桌面应用程序）会将笔记保存到临时文件，并在操作系统关联的应用程序中打开它。Trilium 会监视该文件，并提供将修改后的版本上传回笔记。它在<a class="reference-link" href="../../Collections.md">集合</a>和<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>笔记上不可用。
*   <span class="tn-icon bx bx-customize"></span>_使用自定义程序打开笔记_（仅桌面应用程序，Windows 和 Linux）的工作方式类似于_在外部打开笔记_，但允许你选择用于打开文件的应用程序。
*   <span class="tn-icon bx bx-code"></span>_笔记源代码_显示<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>，即笔记存储时的确切内容。
*   <span class="tn-icon bx bxl-markdown"></span>_转换为 Markdown 笔记_（在文本笔记上）和_转换为文本笔记_（在 Markdown 笔记上）会在富文本和 Markdown 之间切换笔记。确认后，Trilium 会保存一个修订并转换内容；该修订允许在某些格式丢失时回退。参见<a class="reference-link" href="../../Note%20Types/Converting%20between%20note%20types.md">在笔记类型之间转换</a>。
*   <span class="tn-icon bx bx-collapse-alt"></span>_压缩图片_会打开一个对话框，减小笔记中图片的大小。它会列出找到的图片及其占用的空间，并提供以下选项：
    
    *   调整大于所选尺寸的图片的大小。
    *   保留或压缩 JPEG 图片。
    *   保留、优化或将 PNG 图片转换为 JPEG。
    *   _同时处理子笔记_，以包含此笔记下方笔记的图片。
    
    压缩无法撤销。图片也可以在上传时自动压缩，参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>。
*   <span class="tn-icon bx bx-text"></span>_查看 OCR 文本_（在图片和文件笔记上）显示通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取 (OCR)</a>从笔记中提取的文本。如果笔记尚未处理，对话框会提供_处理 OCR_。
*   <span class="tn-icon bx bx-world"></span>_在服务器上打开笔记_（仅桌面应用程序，在配置了<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>时列出）会在 Web 浏览器中于同步服务器上打开同一笔记。

## 删除笔记

<span class="tn-icon bx bx-trash"></span>_删除笔记_会打开当前笔记及其子树的删除对话框。对话框会列出将被删除的笔记以及将被断开的关系，并提供以下选项：

*   如果笔记在其他地方被克隆，也删除该笔记的其他克隆。否则，仅移除当前位置，笔记保留在其他位置。参见<a class="reference-link" href="../Notes/Cloning%20Notes.md">克隆笔记</a>。
*   _永久擦除_，而不是通常的软删除。此操作无法撤销。

未擦除而删除的笔记可以恢复，参见<a class="reference-link" href="../Notes/Restoring%20Deleted%20Notes.md">恢复已删除的笔记</a>。

## 限制

*   笔记菜单在启动器上不可用。
*   在<a class="reference-link" href="Options.md">选项</a>和应用内帮助的笔记上，大多数条目显示为灰色，因为这些笔记无法导入、删除或拥有修订。两者中，只有应用内帮助可以导出，参见<a class="reference-link" href="../Import%20%26%20Export.md">导入与导出</a>。
*   [笔记属性](#note-properties)部分仅在显示笔记本身时列出，而不是其<a class="reference-link" href="../Notes/Attachments.md">附件</a>或<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>。
*   在<a class="reference-link" href="../Navigation/Quick%20edit.md">快速编辑</a>中，不会列出_笔记地图_、_全宽_和_转换为附件_。

## 移动端支持

在<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a>上，笔记菜单从屏幕底部以表单形式打开。除了上述条目外，它还包含桌面布局放置在其他位置的项：

*   表单最顶部图标行中的另外两个图标，从左到右依次为 <span class="tn-icon bx bx-dock-right"></span> _新建分屏_、_笔记地图_、_查找_ 和 <span class="tn-icon bx bx-plus"></span> _子笔记_：当选项卡中没有分屏时，_新建分屏_会打开一个<a class="reference-link" href="Split%20View.md">分屏视图</a>，而_子笔记_会在当前笔记下创建笔记。
*   图标行下方的_反链_和_笔记路径_，它们会打开<a class="reference-link" href="../../Note%20Types/Text/Links/Backlinks.md">反链</a>和笔记的其他位置。
*   它们下方的 <span class="tn-icon bx bx-paperclip"></span> _附件_和 <span class="tn-icon bx bx-list-check"></span> _属性_，分别打开笔记的附件和属性，各自带有笔记拥有的数量。由笔记内容建立的链接不计为属性。_属性_在笔记无法编辑的地方不可用。在移动端，_附件_列在此处而不是图标行中。
*   笔记类型的自定义按钮（例如<a class="reference-link" href="../../Note%20Types/File.md">文件</a>上的 <span class="tn-icon bx bx-download"></span>_下载_）。
*   _关闭此窗格_，位于<a class="reference-link" href="Split%20View.md">分屏视图</a>的第二个笔记上。
*   <span class="tn-icon bx bx-slider-alt"></span> _笔记设置_，位于_保护笔记_下方，会在其自己的页面上打开_共享_和_书签_，然后是_笔记类型_、_模板_和_全宽_，以及笔记的语言：<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记上的内容语言（参见<a class="reference-link" href="../../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md">内容语言与从右到左支持</a>），以及<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记上的代码语言。_可编辑_的选项列在该页面末尾，位于各自的标题下，而不是在进一步的子菜单中。
*   <span class="tn-icon bx bx-info-circle"></span> _笔记信息_，位于_笔记设置_下方，会在其自己的页面上打开笔记的日期、类型、ID 和大小，最后是_显示相似笔记_（参见<a class="reference-link" href="../Navigation/Similar%20Notes.md">相似笔记</a>）。
*   _笔记地图_会在弹出窗口中打开地图，而不是在右侧边栏中。