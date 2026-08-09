# 数据目录

数据目录包含：

*   `document.db` - [数据库](../Advanced%20Usage/Database.md)
*   `config.ini` - 实例级设置，如 Trilium 应用程序运行的端口
*   `backup` - 包含自动[备份](Backup.md)的文档
*   `log` - 包含应用程序日志文件

## 数据目录的位置

查找 Trilium 使用的数据目录的简单方法是查看“关于 Trilium Notes”对话框（从左上角的“菜单”进入）：

![](Data%20directory_image.png)

以下是位置的确定方式：

数据目录通常命名为 `trilium-data`，存储位置如下：

*   Linux 系统：`/home/[user]/.local/share`
*   Windows Vista 及以上系统：`C:\Users\[user]\AppData\Roaming`
*   Mac OS 系统：`/Users/[user]/Library/Application Support`
*   如果上述某些路径不存在，则回退到用户主目录
*   用户主目录也是 \[\[docker|Docker 服务器安装\]\] 的默认设置

如果你想备份 Trilium 数据，只需备份这一个目录即可——它包含了你需要的一切。

### 更改数据目录的位置

如果你希望将数据目录放在其他位置而非默认位置，可以通过 `TRILIUM_DATA_DIR` 环境变量将其更改为其他位置：

### Windows

1.  按下键盘上的 Windows 键。
2.  搜索并选择“编辑系统变量”。
3.  在新打开的屏幕右下角点击“环境变量…”按钮。
4.  在顶部区域（“[用户] 的用户变量”），点击“新建…”按钮。
5.  在_变量名_字段中输入 `TRILIUM_DATA_DIR`。
6.  点击_浏览目录…_按钮并选择存储数据库的新目录。
7.  依次点击每个窗口的_确定_按钮关闭所有窗口。

#### Linux

```
export TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data
```

#### Mac OS X

你需要在 `~/Library/LaunchAgents` 下创建一个 `.plist` 文件，以便每次登录时正确加载。

要手动加载，你需要使用 `launchctl setenv TRILIUM_DATA_DIR <yourpath>`

以下是一个预定义模板，你只需将你的路径添加到其中：

```
        Label
        set.trilium.env
        RunAtLoad
        
        ProgramArguments
        
            launchctl
            setenv
            TRILIUM_DATA_DIR
            /Users/YourUserName/Library/Application Support/trilium-data    
```

### 创建使用特定数据目录运行的脚本

全局设置环境变量的替代方案是仅为此环境变量运行 Trilium Notes。这样可以实现不同的设置方式，例如两个[数据库](../Advanced%20Usage/Database.md)实例或“便携式”安装。

在基于 Unix 的系统上执行此操作，只需像这样运行 `trilium`：

```
TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data trilium
```

然后，你可以将上述命令保存为路径中的 shell 脚本，以方便使用。

## Electron 用户数据目录（仅限桌面版）

运行桌面应用程序时，Electron 会将内部数据（缓存、拼写检查词典、会话存储等）与 Trilium 数据目录分开存储。默认情况下，这些数据存储在系统的应用程序数据文件夹中（例如 Windows 上的 `%APPDATA%`），在具有漫游配置文件的企业环境或便携模式下运行时，这可能不是期望的行为。

要将 Electron 数据保留在系统的漫游配置文件之外，请将 `TRILIUM_ELECTRON_DATA_DIR` 环境变量设置为显式路径。`trilium-portable` 脚本会自动执行此操作，将其指向应用程序旁边的 `trilium-electron-data/`。

## 细粒度的目录/路径位置

除了数据目录之外，其某些子目录也可以通过更改环境变量移动到其他位置：

| 环境变量 | 默认值 | 描述 |
| --- | --- | --- |
| `TRILIUM_DOCUMENT_PATH` | `${TRILIUM_DATA_DIR}/document.db` | <a class="reference-link" href="../Advanced%20Usage/Database.md">数据库</a>（存储所有笔记和元数据）的路径。 |
| `TRILIUM_BACKUP_DIR` | `${TRILIUM_DATA_DIR}/backup` | 存储自动<a class="reference-link" href="Backup.md">备份</a>数据库的目录。 |
| `TRILIUM_LOG_DIR` | `${TRILIUM_DATA_DIR}/log` | 存储每日<a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>的目录。 |
| `TRILIUM_TMP_DIR` | `${TRILIUM_DATA_DIR}/tmp` | 存储临时文件的目录（例如在外部应用程序中打开时）。 |
| `TRILIUM_ANONYMIZED_DB_DIR` | `${TRILIUM_DATA_DIR}/anonymized-db` | 存储<a class="reference-link" href="../Troubleshooting/Anonymized%20Database.md">匿名数据库</a>的目录。 |
| `TRILIUM_CONFIG_INI_PATH` | `${TRILIUM_DATA_DIR}/config.ini` | <a class="reference-link" href="../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>文件的路径。 |
| `TRILIUM_ELECTRON_DATA_DIR` | 系统 appData | Electron 内部数据（缓存、拼写检查词典等）的目录。在便携模式下设置此项以避免写入系统配置文件（仅限桌面版）。 |