# 匿名化数据库

![](Anonymized%20Database_image.png)

在某些情况下，理解数据库的结构对于排查问题至关重要。然而，分享包含个人笔记的实际[数据库](../Advanced%20Usage/Database.md)文件并不可取。为了解决这个问题，Trilium 提供了数据库匿名化功能。您可以通过菜单 -> 选项 -> 高级选项卡访问此功能。

此功能会创建数据库的一个副本，并移除所有敏感数据。具体来说，它会剔除笔记标题、内容、修订版本、历史记录以及部分非系统属性，同时保留整体结构和元数据（如修改日期）。匿名化完成后，数据库会经过[压缩处理](https://sqlite.org/lang_vacuum.html)，以确保文件中不残留任何敏感数据。匿名化后的数据库保存在[数据目录](../Installation%20%26%20Setup/Data%20directory.md)下的 `anonymized` 目录中，可以安全地随错误报告一起分享。

这将创建文档的副本，并移除所有敏感数据（目前包括笔记标题、内容、修订版本、历史记录以及部分选项和非系统属性），同时保留所有结构和元数据（例如最后修改日期）。完成后，数据库会经过[压缩处理](https://sqlite.org/lang_vacuum.html)，以确保文档文件中没有过时的敏感数据。生成的文件存储在 `anonymized` 目录中（位于[数据目录](../Installation%20%26%20Setup/Data%20directory.md)内）。您可以放心地将其附加到错误报告中。

## 命令行匿名化

如果您的[数据库](../Advanced%20Usage/Database.md)损坏到 Trilium 无法启动的程度，仍然可以通过命令行执行匿名化过程：

```
node src/anonymize.js
```

请在包含 Trilium 源文件的目录中运行此命令，对于桌面版，该目录通常位于 `resources/app` 中。