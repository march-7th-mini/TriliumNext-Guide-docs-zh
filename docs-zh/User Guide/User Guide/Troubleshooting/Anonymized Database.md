# 数据库匿名化
![](Anonymized%20Database_image.jpg)

在某些场景下，了解数据库的结构对于排查问题至关重要。然而，不建议分享包含个人笔记的实际[数据库](../Advanced%20Usage/Database.md)文件。为解决这一问题，Trilium 提供了数据库匿名化功能。该功能可通过菜单 -> 选项 -> 高级选项卡访问。

此功能会创建一份移除了所有敏感数据的数据库副本。具体而言，它会剥离笔记标题、内容、修订、历史记录以及部分非系统属性，同时保留整体结构和元数据（例如修改日期）。匿名化完成后，数据库会经过[清理过程](https://sqlite.org/lang_vacuum.html)，以确保文件中不残留任何敏感数据。匿名化后的数据库保存在[数据目录](../Installation%20%26%20Setup/Data%20directory.md)内的 `anonymized` 目录中，可安全地用于缺陷报告分享。

这将创建一份文档副本并移除所有敏感数据（目前包括笔记标题、内容、修订、历史记录以及部分选项和非系统属性），同时保留所有结构和元数据（例如最后修改日期）。完成此操作后，数据库会经过 [VACUUM](https://sqlite.org/lang_vacuum.html) 处理，以确保文档文件中不存在残留的敏感数据。生成的文件存储在 `anonymized` 目录中（位于[数据目录](../Installation%20%26%20Setup/Data%20directory.md)内）。你可以放心地将其附加到缺陷报告中。

## 命令行匿名化

如果你的[数据库](../Advanced%20Usage/Database.md)已损坏到 Trilium 无法启动的程度，仍可通过命令行执行匿名化过程：

```
node src/anonymize.js
```

请在包含 Trilium 源文件的目录中运行此命令，对于桌面版构建，该目录通常位于 `resources/app` 目录下。