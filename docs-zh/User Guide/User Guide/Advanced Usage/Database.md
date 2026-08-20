# 数据库

您的 Trilium 数据存储在一个 [SQLite](https://www.sqlite.org) 数据库中，其中包含所有笔记、树结构、元数据以及大部分配置。数据库文件名为 `document.db`，存储在应用程序默认的[数据目录](../Installation%20%26%20Setup/Data%20directory.md)中。

## 演示笔记

首次启动 Trilium 时，它会提供一组笔记来展示应用程序的各种功能。

更多信息请参阅 <a class="reference-link" href="Database/Demo%20Notes.md">演示笔记</a>。

## 手动修改数据库

Trilium 提供了很大的灵活性，也为高级用户提供了调整它的机会。如果您需要直接浏览或修改数据库，可以使用 [SQLite Browser](https://sqlitebrowser.org/) 等工具直接操作数据库文件。

更多信息请参阅 [手动修改数据库](Database/Manually%20altering%20the%20database.md)。

## 如何重置数据库

如果您想重新开始，并且：

*   创建并切换到一个新的空白知识库
*   使用从服务器或桌面应用程序同步的其他知识库
*   恢复备份

您可以导航到 **设置 → 数据库**，然后点击 **重新开始** 按钮。系统会提示您重启应用程序，并可以选择在继续之前备份当前数据库。

> [!IMPORTANT]
> 对于 Web 客户端，Trilium 无法自动重启。您需要手动重启服务器/容器，然后重新加载 Web 应用程序。

重启后，将出现设置界面。您可以选择备份现有数据库，然后像新安装一样继续设置菜单。只有在选择创建新数据库、与服务器同步或从备份恢复后，现有数据库才会被覆盖。

### 传统方法

如果您正在试用 Trilium 并希望将其恢复到初始状态，可以通过删除当前数据库来实现。当您重新启动应用程序时，它将生成一个包含原始演示笔记的新数据库。

要删除数据库，只需进入[数据目录](../Installation%20%26%20Setup/Data%20directory.md)并删除 `document.db` 文件（以及任何以 `document.db` 开头的其他文件）。

如果您不需要保留可能存储在 `config.ini` 文件中的任何配置，您可以删除[数据目录](../Installation%20%26%20Setup/Data%20directory.md)中的所有内容，以将应用程序完全恢复到初始状态。您也可以查看[配置](Configuration%20\(config.ini%20or%20environment%20variables\).md)文件，将所有 `config.ini` 值作为环境变量提供。