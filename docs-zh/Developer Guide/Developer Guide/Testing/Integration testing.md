## 桌面

### 安装

#### 从 GitHub 发布页面安装

从 [GitHub 发布页面](https://github.com/TriliumNext/Desktop/releases) 下载适用于您平台的最新版本。

#### Windows

下载 Windows 安装程序（`.msi` 文件）并运行它。安装程序会创建桌面快捷方式，并自动在 Windows 启动时启动 Trilium。

#### Linux

下载适用于您发行版的软件包（`.deb`、`.rpm` 或 `.tar.gz`）。

对于 `.tar.gz` 软件包，解压后运行 `trilium` 可执行文件。

#### macOS

下载 `.dmg` 文件，挂载它，然后将 Trilium 拖入您的应用程序文件夹。

### 数据目录

TriliumNext 桌面版将数据存储在用户数据目录中。该目录的位置因操作系统而异：

*   **Windows**：`%APPDATA%\trilium-data`
*   **Linux**：`~/.local/share/trilium-data`
*   **macOS**：`~/Library/Application Support/trilium-data`

您可以通过设置环境变量 `TRILIUM_DATA_DIR` 来覆盖此目录。

### 命令行参数

TriliumNext 桌面版支持以下命令行参数：

*   `--data-dir`：指定数据目录的位置。
*   `--disable-cache`：禁用缓存。
*   `--disable-dev-tools`：禁用开发者工具。
*   `--disable-sandbox`：禁用 Chromium 沙箱。
*   `--hide-main-menu`：隐藏主菜单。
*   `--safe-mode`：以安全模式启动，禁用所有第三方脚本和组件。
*   `--enable-logging`：启用日志记录。

### 故障排除

#### 应用无法启动

如果 TriliumNext 桌面版无法启动，请尝试以下步骤：

1.  检查数据目录是否损坏。您可以尝试将其重命名，然后再次启动应用。
2.  检查日志文件。日志文件位于数据目录中。
3.  尝试以安全模式启动应用：`trilium --safe-mode`。

#### 应用崩溃

如果应用崩溃，请尝试以下步骤：

1.  检查日志文件。
2.  尝试以安全模式启动应用。
3.  尝试清除缓存。

#### 应用运行缓慢

如果应用运行缓慢，请尝试以下步骤：

1.  尝试压缩数据库。
2.  尝试清除缓存。
3.  检查是否有大型笔记或附件。

### 备份

TriliumNext 桌面版会自动创建每日备份。备份存储在数据目录的 `backup` 文件夹中。您也可以手动创建备份，方法是转到“文件”菜单并选择“备份”。

### 更新

TriliumNext 桌面版会自动检查更新。当有新版本可用时，您会收到通知。您也可以转到“帮助”菜单并选择“检查更新”来手动检查更新。

### 卸载

要卸载 TriliumNext 桌面版，请删除数据目录和应用程序文件。