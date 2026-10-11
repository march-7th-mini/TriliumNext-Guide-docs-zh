# 从其他应用程序导入数据
从 v0.104.0 版本开始，Trilium 的导入器扩展到了针对特定应用程序的导入。与标准的 HTML 或 <a class="reference-link" href="Markdown.md">Markdown</a> 导入/导出不同，这些导入器是为支持特定应用程序的功能和笔记结构而量身定制的。

## 支持的应用程序

*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Microsoft%20OneNote.md">Microsoft OneNote</a>，通过使用 Microsoft Graph 连接到你的账户。
*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Notion.md">Notion</a>，通过 ZIP 导出文件。
*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Google%20Keep.md">Google Keep</a>，通过来自 _Google Takeout_ 的 ZIP 导出文件（Keep 没有专门的导出机制）。
*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Evernote.md">Evernote</a>，通过 ENEX 导出文件。
*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Anytype.md">Anytype</a>，通过 JSON 导出文件。
*   <a class="reference-link" href="Importing%20data%20from%20other%20applications/Obsidian.md">Obsidian</a>，通过库的 ZIP 文件。

## 从另一个应用程序导入数据

要从某个应用程序导入，有两种方式可以打开导入对话框：

*   在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中，右键点击一个笔记并选择 _导入到笔记中_。
*   在<a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>中，选择 _导入文件_。

支持的应用程序列表将显示在顶部，每个应用程序都有自己的配置。只需点击其中一个，然后按照屏幕上的说明操作即可。

## 致谢

*   Trilium 的导入器受到了 Obsidian 的 [Importer 插件](https://github.com/obsidianmd/obsidian-importer)（基于 MIT 许可证授权）的启发，例如关于 OneNote 连接过程或 Notion ID 管理方面。