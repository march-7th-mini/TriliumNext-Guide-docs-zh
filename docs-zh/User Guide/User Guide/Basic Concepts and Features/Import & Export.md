# 导入与导出

Trilium 原生支持以下格式的导入和导出。

## 支持的格式

*   HTML：
    *   这是 Trilium 使用的主要格式，其中使用标准标签来表示基本格式和布局（例如 `<strong>`、`<table>`、`<pre>`）。
    *   请注意，HTML 不是标准化格式，因此某些更具体的功能，如警示框或 <a class="reference-link" href="../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>，可能不受其他应用程序支持。
    *   笔记也可以导出为[可用于 Web 发布的静态 HTML](../Advanced%20Usage/Sharing/Exporting%20static%20HTML%20for%20web%20publishing.md)。
*   <a class="reference-link" href="Import%20%26%20Export/Markdown.md">Markdown</a>
    *   大部分格式会被保留，请参阅 <a class="reference-link" href="Import%20%26%20Export/Markdown/Supported%20syntax.md">支持的语法</a>。
*   OPML（大纲互换格式）
    *   支持用于纯文本的 OPML v1.0 和支持 HTML 的 v2.0。

要从 OneNote、Notion 等其他应用程序导入，请参阅 <a class="reference-link" href="Import%20%26%20Export/Importing%20data%20from%20other%20applications.md">从其他应用程序导入数据</a>。

## 最大导入大小

v0.104.0 之前的版本有 250 MiB 的上传限制，可以通过 `TRILIUM_NO_UPLOAD_LIMIT` 环境变量绕过；从 v0.104.0 开始，此限制已被移除。

尽管如此，**单个项目**（无论是 <a class="reference-link" href="../Note%20Types/File.md">文件</a>、<a class="reference-link" href="Notes/Attachments.md">附件</a> 还是 <a class="reference-link" href="../Note%20Types/Text.md">文本</a> 笔记）的最大大小仍然有限制。该限制约为 374 MiB，由 <a class="reference-link" href="../Installation%20%26%20Setup/Synchronization.md">同步</a> 协议决定。尝试导入此类大文件将被拒绝。

在大型导入或导出期间，内存消耗可能会激增，但会保持在 2 GB 左右。已使用包含约 21k 条笔记的 2.4 GB 数据库进行测试。

> [!IMPORTANT]
> 对于 <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，有两种不同的导入机制：
> 
> *   从 <a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a> 快速导入。
> *   导入对话框（通过右键单击笔记树中的 _导入到笔记_ 或从 <a class="reference-link" href="UI%20Elements/Note%20buttons.md">笔记按钮</a>）。
> 
> 处理大文件（数 GB）时，建议使用导入对话框，因为它有一种特殊机制，可确保直接从磁盘读取文件，而不是再次上传。

## 导出根笔记

根笔记是最顶层的笔记。导出它的行为与任何其他笔记相同：在 <a class="reference-link" href="UI%20Elements/Note%20Tree.md">笔记树</a> 中右键单击它，然后选择 _导出_。

从 v0.104.0 开始，当导入根笔记时，它将作为现有根笔记的子笔记被导入。此行为确保导入不会更改或覆盖您现有的笔记。

您可以使用树的 <a class="reference-link" href="UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a> 功能轻松地将笔记移动到根笔记下，并删除多余的根笔记。

<table>
    <thead>
        <tr>
            <th scope="col">之前</th>
            <th scope="col">之后</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>根笔记<ul><li>一</li><li>二</li></ul></li></ul></td>
            <td><ul><li>根笔记（现有）<ul><li>根笔记（来自导入）<ul><li>一</li><li>二</li></ul></li></ul></li></ul></td>
        </tr>
    </tbody>
</table>

> [!TIP]
> 与其导出完整的 ZIP 文件（包括根笔记），不如考虑使用[备份](../Installation%20%26%20Setup/Backup.md)。备份始终包含整个结构，以及 ZIP 导出所不具备的附加信息：保留笔记 ID，包含选项/令牌，并能更好地处理 <a class="reference-link" href="Notes/Protected%20Notes.md">受保护的笔记</a>。