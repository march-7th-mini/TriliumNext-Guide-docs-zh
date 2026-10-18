# 笔记菜单
<figure class="image image-style-align-right image_resized" style="width:25.95%;"><img style="aspect-ratio:402/988;" src="Note menu_image.png" width="402" height="988"></figure>

笔记菜单包含针对当前笔记的各种操作和配置。它位于<a class="reference-link" href="Note%20buttons.md">笔记按钮</a>区域（<a class="reference-link" href="../Notes/Title.md">标题</a>的右侧）。

每个分屏都有各自的笔记菜单，作用于该分屏中显示的笔记。不适用于当前笔记的条目仍会列出，但会显示为灰色；而仅存在于某些笔记的条目（在_笔记专属条目_中描述）只会在这些笔记上出现。

## 在笔记中导航

*   <span class="tn-icon bx bx-search"></span> _在笔记中搜索_ 会打开<a class="reference-link" href="../Navigation/Search%20in%20note.md">在笔记中搜索</a>栏，用于在当前笔记中查找和替换文本。在桌面应用中，同一栏可通过 <kbd>Ctrl</kbd>+<kbd>F</kbd> 打开。
    *   它适用于<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>、<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>、<a class="reference-link" href="../../Note%20Types/Mind%20Map.md">思维导图</a>和<a class="reference-link" href="../../Note%20Types/Spreadsheets.md">电子表格</a>笔记、<a class="reference-link" href="../../Collections.md">集合</a>、PDF 文件，以及任何以<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>形式显示的笔记。
*   <span class="tn-icon bx bx-paperclip"></span> _笔记附件_ 会将笔记切换到其<a class="reference-link" href="../Notes/Attachments.md">附件</a>列表，可在其中上传、打开、下载、重命名或删除附件。
*   <span class="tn-icon bx bxs-network-chart"></span> _笔记地图_ 会打开<a class="reference-link" href="Right%20Sidebar.md">右侧边栏</a>的<a class="reference-link" href="Right%20Sidebar/Connections%20tab.md">连接选项卡</a>，其中显示以当前笔记为中心的<a class="reference-link" href="../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记地图（链接图、树图）</a>。

## 笔记属性

本节中的开关会立即生效：

*   <span class="tn-icon bx bx-share-alt"></span> _共享_ 通过<a class="reference-link" href="../../Advanced%20Usage/Sharing.md">共享</a>功能发布笔记，将其克隆到_共享笔记_树中。
    *   关闭它会从该树中移除克隆。如果该笔记仅作为共享笔记存在，Trilium 会请求确认，因为取消共享会删除它。
    *   该开关在根笔记、_共享笔记_笔记本身以及系统笔记上不可用。
*   <span class="tn-icon bx bx-lock-alt"></span> _保护笔记_ 会加密笔记，将其变为<a class="reference-link" href="../Notes/Protected%20Notes.md">受保护的笔记</a>之一。如果没有活动的受保护会话，Trilium 会先请求密码。仅影响当前笔记，不影响其子笔记。
*   <span class="tn-icon bx bx-bookmark"></span> _书签_ 会将笔记添加到<a class="reference-link" href="Launch%20Bar.md">启动栏</a>中显示的<a class="reference-link" href="../Navigation/Bookmarks.md">书签</a>，或从中移除。
*   <span class="tn-icon bx bx-copy-alt"></span> _模板_ 会将笔记标记为<a class="reference-link" href="../../Advanced%20Usage/Templates.md">模板</a>之一（通过添加 `#template` 标签），使其在创建新笔记时可用。
*   <span class="tn-icon bx bx-expand-horizontal"></span> _全宽_ 通过添加 `#fullContentWidth` 标签，让笔记使用窗口的整个宽度，而不是<a class="reference-link" href="Content%20width.md">内容宽度</a>中设置的限制。对于始终以全宽显示的笔记类型，不会列出此项。

本节中的两个子菜单：

*   <span class="tn-icon bx bx-file"></span> _笔记类型_ 会将笔记的类型更改为任何<a class="reference-link" href="../../Note%20Types.md">笔记类型</a>；当前类型会被勾选。如果笔记已有内容，Trilium 会先请求确认，因为内容通常不会保留。<a class="reference-link" href="../../Note%20Types/Converting%20between%20note%20types.md">在笔记类型之间转换</a>。
    *   对于<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记，语言改为在<a class="reference-link" href="Status%20bar.md">状态栏</a>中选择。
*   <span class="tn-icon bx bx-edit-alt"></span> _可编辑_ 控制笔记何时以只读方式打开（参见<a class="reference-link" href="../Notes/Read-Only%20Notes.md">只读笔记</a>）：
    *   _自动_（默认）：笔记可编辑，除非它足够长而自动以只读方式打开。
    *   _只读_：笔记始终以只读方式打开，但在按下_编辑笔记_后仍可编辑。
    *   _始终可编辑_：无论长度如何，笔记始终可编辑。

## 导入、导出和打印

*   <span class="tn-icon bx bx-import"></span> _导入文件_ 会打开导入对话框，将文件作为当前笔记的子笔记导入。参见<a class="reference-link" href="../Import%20%26%20Export.md">导入与导出</a>。它在<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>笔记上不可用。
*   <span class="tn-icon bx bx-export"></span> _导出笔记_ 会打开导出对话框，并选中_仅此笔记_；在那里选择_此笔记及所有后代_可导出整个子树。
*   <span class="tn-icon bx bx-printer"></span>_打印笔记…_ 会打印笔记。在桌面应用中，此条目显示为_打印/导出为 PDF…_，也可将笔记保存为 PDF 文件。参见<a class="reference-link" href="../Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印与导出为 PDF</a>，包括哪些笔记类型和集合可以打印。

某些笔记类型会在_导出笔记_正下方添加自己的导出格式：

*   <span class="tn-icon bx bxs-file-image"></span>_导出为图片_，在<a class="reference-link" href="../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>和<a class="reference-link" href="../../Note%20Types/Mind%20Map.md">思维导图</a>笔记上，将图表下载为 _PNG（栅格）_ 或 _SVG（矢量）_。
*   <span class="tn-icon bx bxs-spreadsheet"></span>_导出为 Excel (.xlsx)_ 和 _导出为 CSV (.csv)_，在<a class="reference-link" href="../../Note%20Types/Spreadsheets.md">电子表格</a>上，以这些格式下载电子表格。

## 修订

这些条目管理笔记的<a class="reference-link" href="../Notes/Note%20Revisions.md">笔记修订</a>：

*   <span class="tn-icon bx bx-history"></span>_笔记修订…_ 会打开修订对话框，可在其中预览、与当前版本比较、下载或恢复以前的版本。
*   <span class="tn-icon bx bx-save"></span>_保存修订_ 会立即保存笔记的修订，而不是等待下一次自动快照。
*   <span class="tn-icon bx bx-purchase-tag"></span>_保存命名修订…_ 也会立即保存修订，但会先请求对更改的简短描述，该描述会显示在修订对话框中。

## 笔记专属条目

以下条目仅在某些笔记上出现：

*   <span class="tn-icon bx bx-pencil"></span>_编辑笔记_ 在笔记当前为只读时出现在菜单顶部。它会启用编辑，直到笔记关闭。
*   <span class="tn-icon bx bx-align-justify"></span>_自动换行_ 在<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记上出现在菜单顶部，设置此笔记中的长行是否换行：
    *   _自动_（默认）遵循<a class="reference-link" href="Options.md">选项</a> → _代码笔记_ → _在代码笔记中换行_。
    *   _开_ 和 _关_ 通过设置 `#wrapLines` 标签仅为此笔记覆盖该设置。
*   <span class="tn-icon bx bx-paperclip"></span>_转换为附件_ 出现在没有子笔记且只有一个父笔记（为<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记）的图片笔记上。确认后，它会将图片变为其父笔记的附件并在那里打开。参见<a class="reference-link" href="../Notes/Attachments.md">附件</a>。
*   <span class="tn-icon bx bx-extension"></span>_重新渲染笔记_ 出现在<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>上，会再次运行其脚本以刷新输出。
*   <span class="tn-icon bx bx-cog"></span>_看板属性_ 出现在<a class="reference-link" href="../../Collections/Kanban%20Board.md">看板</a>上，配置其列、卡片属性和卡片模板。
*   <span class="tn-icon bx bx-cog"></span>_日历属性_ 出现在创建事件的<a class="reference-link" href="../../Collections/Calendar.md">日历</a>上，配置其事件模板。
*   <span class="tn-icon bx bx-cog"></span>_地理地图属性_ 出现在<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>上，配置其地图设置以及[图片地图](../../Collections/Geo%20Map/Image%20maps.md)的图片。
*   <span class="tn-icon bx bx-cog"></span>_表格属性_ 出现在<a class="reference-link" href="../../Collections/Table.md">表格</a>上，配置其显示哪些笔记。

## 高级

<span class="tn-icon bx bx-wrench"></span>_高级_ 子菜单将较少使用的操作分组：

*   <span class="tn-icon bx bx-file-find"></span>_在外部打开笔记_（仅桌面应用）会将笔记保存到临时文件，并在操作系统关联的应用程序中打开它。Trilium 会监视该文件，并提供将修改后的版本上传回笔记的选项。它在<a class="reference-link" href="../../Collections.md">集合</a>和<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>笔记上不可用。
*   <span class="tn-icon bx bx-customize"></span>_使用自定义程序打开笔记_（仅桌面应用，Windows 和 Linux）的工作方式类似于_在外部打开笔记_，但允许你选择用于打开文件的应用程序。
*   <span class="tn-icon bx bx-code"></span>_笔记源代码_ 显示<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>，即笔记存储时的确切内容。
*   <span class="tn-icon bx bxl-markdown"></span>_转换为 Markdown 笔记_（在文本笔记上）和 _转换为文本笔记_（在 Markdown 笔记上）会在富文本和 Markdown 之间切换笔记。确认后，Trilium 会保存一个修订并转换内容；该修订允许在某些格式丢失时回退。参见<a class="reference-link" href="../../Note%20Types/Converting%20between%20note%20types.md">在笔记类型之间转换</a>。
*   <span class="tn-icon bx bx-collapse-alt"></span>_压缩图片_ 会打开一个对话框，减小笔记中图片的大小。它会列出找到的图片及其占用的空间，并提供以下选项：
    
    *   将大于所选尺寸的图片调整大小。
    *   保留或压缩 JPEG 图片。
    *   保留、优化或将 PNG 图片转换为 JPEG。
    *   _同时处理子笔记_，以包含此笔记下方笔记的图片。
    
    压缩无法撤销。图片也可以在上传时自动压缩，参见<a class="reference-link" href="../../Note%20Types/Text/Images.md">图片</a>。
*   <span class="tn-icon bx bx-text"></span>_查看 OCR 文本_（在图片和文件笔记上）显示通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>从笔记中提取的文本。如果笔记尚未处理，对话框会提供_处理 OCR_选项。
*   <span class="tn-icon bx bx-world"></span>_在服务器上打开笔记_（仅桌面应用，在配置了<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>时列出）会在 Web 浏览器中于同步服务器上打开同一笔记。

## 删除笔记

<span class="tn-icon bx bx-trash"></span>_删除笔记_ 会为当前笔记及其子树打开删除对话框。对话框会列出将被删除的笔记以及将被断开的关系，并提供以下选项：

*   如果笔记在其他位置被克隆，也删除该笔记的其他克隆。否则，仅移除当前位置，笔记保留在其他位置。参见<a class="reference-link" href="../Notes/Cloning%20Notes.md">克隆笔记</a>。
*   _永久擦除_，而不是通常的软删除。此操作无法撤销。

未擦除而删除的笔记可以恢复，参见<a class="reference-link" href="../Notes/Restoring%20Deleted%20Notes.md">恢复已删除的笔记</a>。

## 限制

*   笔记菜单在启动器上不可用。
*   在<a class="reference-link" href="Options.md">选项</a>和应用内帮助的笔记上，大多数条目显示为灰色，因为这些笔记无法导入、删除或拥有修订。两者中，只有应用内帮助可以导出，参见<a class="reference-link" href="../Import%20%26%20Export.md">导入与导出</a>。
*   [笔记属性](#note-properties)部分仅在显示笔记本身时列出，而不是其<a class="reference-link" href="../Notes/Attachments.md">附件</a>或<a class="reference-link" href="../../Advanced%20Usage/Note%20source.md">笔记源代码</a>。
*   在<a class="reference-link" href="../Navigation/Quick%20edit.md">快速编辑</a>中，不会列出_在笔记中搜索_、_笔记地图_、_全宽_和_转换为附件_。

## 移动端支持

在<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a>上，笔记菜单从屏幕底部以工作表形式打开。除了上述条目外，它还包含桌面布局放置在其他位置的项：

*   _反链_ 和 _笔记路径_，位于顶部，分别打开<a class="reference-link" href="../../Note%20Types/Text/Links/Backlinks.md">反链</a>和笔记的其他位置。
*   笔记类型的自定义按钮（例如<a class="reference-link" href="../../Note%20Types/File.md">文件</a>上的 <span class="tn-icon bx bx-download"></span>_下载_）。
*   _插入子笔记_，在当前笔记下创建笔记。
*   _创建新分屏_ 和 _关闭此窗格_，用于管理<a class="reference-link" href="Split%20View.md">分屏视图</a>。
*   _笔记属性_，打开笔记的属性。
*   在<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记上，为内容语言（参见<a class="reference-link" href="../../Note%20Types/Text/Content%20language%20%26%20Right-to-left%20support.md">内容语言与从右到左支持</a>）；在<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记上，为代码语言。
*   _笔记信息_ 和<a class="reference-link" href="../Navigation/Similar%20Notes.md">相似笔记</a>。
*   _笔记地图_ 在弹出窗口中打开地图，而不是在右侧边栏中。