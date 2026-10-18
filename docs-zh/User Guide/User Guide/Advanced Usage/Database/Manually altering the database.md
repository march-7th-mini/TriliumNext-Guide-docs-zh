# 手动修改数据库

在某些情况下，可能需要修改 Trilium 所使用的 SQLite 数据库。

如果你正在进行任何高级开发或故障排除并手动修改数据库，可能需要考虑为 `document.db` 文件创建备份。

## 使用 SQL 控制台在内部修改

SQL 控制台是 Trilium 内置的数据库编辑器。

参见 <a class="reference-link" href="Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a>。

## 在外部修改数据库

有时无法使用 SQL 控制台（例如应用程序无法启动时）。

进行外部修改时，请考虑关闭桌面应用程序。如果修改的是服务器数据库，则停止服务或 Docker 容器。

### 使用 DB Browser for SQLite

DB Browser for SQLite 是一个跨平台编辑器，可通过图形用户界面修改数据库。

操作步骤如下：

1.  在主菜单中，选择 File → Open database… 并导航到[数据目录](../../Installation%20%26%20Setup/Data%20directory.md)中的数据库。
2.  选择 _Execute SQL_ 选项卡。
3.  输入所需的 SQL 语句。
4.  按“Execute SQL”选项卡下方工具栏中的“Play”按钮（或 F5 键）。
5.  按主工具栏中的“Write Changes”。
6.  关闭应用程序或关闭数据库。

![](Manually%20altering%20the%20database_image.jpg)

### 使用 SQLite CLI

首先，通过指定数据库路径启动 SQLite 3 CLI：

```
sqlite3 ~/.local/share/trilium-data/document.db
```

*   在提示符中直接输入语句，并确保以 `;` 字符结尾。
*   要退出，只需输入 `.quit` 并回车。