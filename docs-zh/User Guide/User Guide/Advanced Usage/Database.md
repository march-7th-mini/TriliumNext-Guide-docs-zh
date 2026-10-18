# 数据库
你的 Trilium 数据存储在一个 [SQLite](https://www.sqlite.org) 数据库中，其中包含所有笔记、树结构、元数据以及大部分配置。数据库文件名为 `document.db`，存储在应用程序默认的[数据目录](../Installation%20%26%20Setup/Data%20directory.md)中。

## 演示笔记

首次启动 Trilium 时，它会提供一组笔记来展示应用程序的各种功能。

更多信息请参见 <a class="reference-link" href="Database/Demo%20Notes.md">演示笔记</a>。

## 手动修改数据库

Trilium 提供了很大的灵活性，同时也为高级用户提供了调整它的机会。如果你需要直接浏览或修改数据库，可以使用 [SQLite Browser](https://sqlitebrowser.org/) 等工具直接操作数据库文件。

更多信息请参见[手动修改数据库](Database/Manually%20altering%20the%20database.md)。

## 如何重置数据库

如果你想重新开始，并且：

*   创建并切换到一个新的空白知识库
*   使用从服务器或桌面应用程序同步的其他知识库
*   恢复备份

你可以导航到<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _数据库_，然后点击 _重新开始_ 按钮。系统会提示你重启应用程序，并可以选择在继续之前备份当前数据库。

> [!IMPORTANT]
> 对于 Web 客户端，Trilium 无法自动重启。你需要手动重启服务器/容器，然后重新加载 Web 应用程序。

重启后，将出现设置界面。你可以选择备份现有数据库，然后像全新安装一样继续使用设置菜单。只有在选择创建新数据库、与服务器同步或从备份恢复之后，现有数据库才会被覆盖。

### 传统方法

如果你正在试用 Trilium，并希望将其恢复到原始状态，可以通过删除当前数据库来实现。当你重启应用程序时，它会生成一个包含原始演示笔记的新数据库。

要删除数据库，只需前往[数据目录](../Installation%20%26%20Setup/Data%20directory.md)并删除 `document.db` 文件（以及任何以 `document.db` 开头的其他文件）。

如果你不需要保留可能存储在 `config.ini` 文件中的任何配置，你可以直接删除[数据目录](../Installation%20%26%20Setup/Data%20directory.md)的所有内容，以将应用程序完全恢复到原始状态。你也可以查看[配置](Configuration%20\(config.ini%20or%20environment%20variables\).md)文件，改为将所有 `config.ini` 值作为环境变量提供。