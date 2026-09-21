# 导入与导出
要导入笔记：

*   最简单的导入方式是直接将文件或归档文件拖放到<a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a>中。
    *   这会自动检测某些格式，例如 <a class="reference-link" href="Import%20%26%20Export/Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a>。
    *   _安全导入_ 会自动开启，以防止意外运行外部脚本。
*   要配置导入，可以通过<a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a> → _导入到笔记_ 或<a class="reference-link" href="UI%20Elements/Note%20buttons.md">笔记按钮</a> → _导入到笔记_ 访问专用对话框。
    *   此功能允许为其他应用（如 <a class="reference-link" href="Import%20%26%20Export/Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a> 或 <a class="reference-link" href="Import%20%26%20Export/Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>）提供专用导入器。
    *   _安全导入_ 以及其他选项可以在底部折叠的 _选项_ 区域中进行配置。

要导出笔记，请在<a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击该笔记，然后选择 _导出_。同样，在<a class="reference-link" href="UI%20Elements/Note%20buttons.md">笔记按钮</a>中也有 _导出笔记_ 选项。

## 支持的格式

Trilium 原生支持以下格式的导入和导出。

*   HTML：
    *   这是 Trilium 使用的主要格式，其中使用标准标签来表示基本格式和布局（例如 `<strong>`、`<table>`、`<pre>`）。
    *   请注意，HTML 并非标准化格式，因此某些更具体的功能（如警示框或<a class="reference-link" href="../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>）可能不被其他应用程序支持。
    *   笔记也可以导出为[可用于 Web 发布的静态 HTML](../Advanced%20Usage/Sharing/Exporting%20static%20HTML%20for%20web%20publishing.md)。
*   <a class="reference-link" href="Import%20%26%20Export/Markdown.md">Markdown</a>
    *   大部分格式都会保留，请参阅<a class="reference-link" href="Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>。
*   OPML（大纲交换格式）
    *   同时支持用于纯文本的 OPML v1.0 和支持 HTML 的 v2.0。

要从其他应用程序（如 OneNote、Notion 等）导入，请参阅<a class="reference-link" href="Import%20%26%20Export/Importing%20data%20from%20other%20applications.md">从其他应用程序导入数据</a>。

## 最大导入大小

v0.104.0 之前的版本有 250 MiB 的上传限制，可以通过 `TRILIUM_NO_UPLOAD_LIMIT` 环境变量绕过；在 v0.104.0 中此限制已被移除。

尽管如此，**单个项目**（无论是<a class="reference-link" href="../Note%20Types/File.md">文件</a>、<a class="reference-link" href="Notes/Attachments.md">附件</a>还是<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记）的最大大小仍然有限制。该限制约为 374 MiB，由<a class="reference-link" href="../Installation%20%26%20Setup/Synchronization.md">同步</a>协议决定。尝试导入如此大的文件将被拒绝。

在大型导入或导出期间，内存消耗可能会激增，但会保持在 2 GB 左右。已使用约 2.4 GB 数据库（约 21k 条笔记）进行测试。

> [!IMPORTANT]
> 对于<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，有两种不同的导入机制：
> 
> *   快速导入，从<a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a>进行。
> *   导入对话框（通过右键点击笔记树 → _导入到笔记_ 或从<a class="reference-link" href="UI%20Elements/Note%20buttons.md">笔记按钮</a>）。
> 
> 处理大型文件（数 GB）时，建议使用导入对话框，因为它有特殊机制确保文件直接从磁盘读取，而不是再次上传。

## 导出根笔记

根笔记是最顶层的笔记。导出它的行为与其他任何笔记相同：在<a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击它，然后选择 _导出_。

从 v0.104.0 开始，当导入根笔记时，它将作为现有根笔记的子笔记导入。此行为确保导入不会更改或覆盖现有笔记。

你可以使用树的<a class="reference-link" href="UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>功能轻松将笔记移动到根笔记下，并删除多余的根笔记。

<table>
    <thead>
        <tr>
            <th scope="col">之前</th>
            <th scope="col">之后</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>root<ul><li>one</li><li>two</li></ul></li></ul></td>
            <td><ul><li>root（现有）<ul><li>root（来自导入）<ul><li>one</li><li>two</li></ul></li></ul></li></ul></td>
        </tr>
    </tbody>
</table>

> [!TIP]
> 与其导出完整的 ZIP（包括根笔记），不如考虑使用[备份](../Installation%20%26%20Setup/Backup.md)。备份始终包含整个结构，以及 ZIP 导出所没有的额外信息：维护笔记 ID、包含选项/令牌，并更好地处理<a class="reference-link" href="Notes/Protected%20Notes.md">受保护的笔记</a>。