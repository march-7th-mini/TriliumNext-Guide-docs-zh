# 数据目录

数据目录包含：

*   `document.db` - [数据库](../Advanced%20Usage/Database.md)
*   `config.ini` - 实例级设置，例如 Trilium 应用程序运行的端口
*   `backup` - 包含文档的自动[备份](Backup.md)
*   `log` - 包含应用程序日志文件

## 数据目录的位置

找出 Trilium 使用哪个数据目录的简单方法是查看“关于 Trilium Notes”对话框（位于左上角的“菜单”中）：

![](Data%20directory_image.jpg)

位置的决定方式如下：

数据目录通常命名为 `trilium-data`，存储在：

*   Linux 下为 `/home/[user]/.local/share`
*   Linux 上 Flathub 版本为 `/home/[user]/.var/app/org.triliumnotes.Trilium/data`
*   Windows Vista 及更高版本为 `C:\Users\[user]\AppData\Roaming`
*   Mac OS 下为 `/Users/[user]/Library/Application Support`
*   如果上述某些路径不存在，则回退到用户主目录
*   用户主目录也是 \[\[docker|Docker 服务器安装\]\] 的默认设置

如果你想备份 Trilium 数据，只需备份这一个目录即可——它包含了你需要的一切。

### 更改数据目录的位置

如果你想为数据目录使用默认位置以外的其他位置，可以通过 `TRILIUM_DATA_DIR` 环境变量将其更改为其他位置：

=== "<span class="tn-icon bx bxl-windows"></span> Windows"

    1.  按下键盘上的 <span class="tn-icon bx bxl-windows"></span> 键。
    2.  搜索并选择 _编辑系统变量_。
    3.  在新打开的屏幕右下角按下 _环境变量…_ 按钮。
    4.  在顶部区域（_\[user\] 的用户变量_）中，按下 _新建…_ 按钮。
    5.  在 _变量名_ 字段中输入 `TRILIUM_DATA_DIR`。
    6.  按下 _浏览目录…_ 按钮，选择用于存储数据库的新目录。
    7.  对每个窗口按下 _确定_ 按钮以关闭所有窗口。

=== "<span class="tn-icon bx bxl-tux"></span> Linux"

    Trilium 在启动时读取 `TRILIUM_DATA_DIR`，因此必须在启动它的环境中设置该变量。

    > [!NOTE]
    > 设置该变量不会移动现有笔记。要保留它们，请先关闭 Trilium，并将旧数据目录复制到新位置。如果路径的最后一级文件夹不存在，Trilium 会创建它，但不会创建其父文件夹。

    **桌面应用程序（.deb、.rpm、AppImage 或 .zip）**

    无论 Trilium 以何种方式启动（从应用程序菜单、桌面快捷方式、登录时或从终端），要使用新位置，请为整个会话设置该变量：

    1.  创建文件 `~/.config/environment.d/trilium.conf`，内容如下，使用完整路径（此文件中不会展开 `~`）：
        
        ```
        TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data
        ```
    2.  注销并重新登录。

    这适用于由 `systemd` 启动的桌面环境，涵盖了大多数运行 GNOME 或 KDE Plasma 的发行版。在其他系统上，请改为将以下行添加到 `~/.profile`，然后注销并重新登录：

    ```sh
    export TRILIUM_DATA_DIR="$HOME/data/my-trilium-data"
    ```

    在 `~/.bashrc`（或你的 shell 的等效文件）中添加同一行仅在从终端启动 Trilium 时生效，从应用程序菜单启动时不生效。

    **Flatpak（Flathub）**

    Flathub 版本运行在无法看到文件系统其余部分的沙箱中，因此它既需要访问该文件夹，也需要该变量：

    ```sh
    flatpak override --user \
        --env=TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data \
        --filesystem=/home/myuser/data/my-trilium-data:create \
        org.triliumnotes.Trilium
    ```

    要恢复默认位置，请运行 `flatpak override --user --reset org.triliumnotes.Trilium`。这也会移除为 Trilium 设置的其他所有覆盖项。

    **作为 systemd 服务运行的服务器**

    在 <a class="reference-link" href="Server%20Installation/1.%20Installing%20the%20server/Packaged%20version%20for%20Linux.md">Linux 打包版本</a> 中描述的单元文件的 `[Service]` 部分添加一行 `Environment=`：

    ```
    [Service]
    Environment=TRILIUM_DATA_DIR=/var/lib/trilium-data
    ```

    然后重新加载并重启服务：

    ```sh
    sudo systemctl daemon-reload
    sudo systemctl restart trilium
    ```

    在 `User=` 中设置的用户必须能够写入该文件夹。对于 Docker，请参阅 <a class="reference-link" href="Server%20Installation/1.%20Installing%20the%20server/Using%20Docker.md">使用 Docker</a>。

=== "<span class="tn-icon bx bxl-apple"></span> macOS"

    你需要在 `~/Library/LaunchAgents` 下创建一个 `.plist` 文件，以便每次登录时正确加载它。

    要手动加载它，你需要使用 `launchctl setenv TRILIUM_DATA_DIR <yourpath>`

    以下是一个预定义模板，你只需在其中添加你的路径：

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>set.trilium.env</string>
        <key>RunAtLoad</key>
        <true/>
        <key>ProgramArguments</key>
        <array>
            <string>/bin/launchctl</string>
            <string>setenv</string>
            <string>TRILIUM_DATA_DIR</string>
            <string>/Users/YourUserName/Library/Application Support/trilium-data</string>
        </array>
    </dict>
    </plist>

    ```

### 创建使用特定数据目录运行的脚本

全局设置环境变量的替代方法是仅使用此环境变量运行 Trilium Notes。这样就可以实现不同的设置方式，例如两个[数据库](../Advanced%20Usage/Database.md)实例或“便携式”安装。

在基于 Unix 的系统中，只需像这样运行 `trilium`：

```
TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data trilium
```

为了方便，你可以将上述命令保存为路径中的 shell 脚本。

## Electron 用户数据目录（仅桌面端）

运行桌面应用程序时，Electron 会将内部数据（缓存、拼写检查词典、会话存储等）与 Trilium 数据目录分开存储。默认情况下，这些数据会进入系统的应用程序数据文件夹（例如 Windows 上的 `%APPDATA%`），在具有漫游配置文件的企业环境中或以便携模式运行时，这可能并不理想。

要将 Electron 数据排除在系统的漫游配置文件之外，请将 `TRILIUM_ELECTRON_DATA_DIR` 环境变量设置为一个明确的路径。`trilium-portable` 脚本会自动执行此操作，将其指向应用程序旁边的 `trilium-electron-data/`。

## 细粒度的目录/路径位置

除了数据目录之外，还可以通过更改环境变量将其中的某些子目录移动到其他位置：

| 环境变量 | 默认值 | 描述 |
| --- | --- | --- |
| `TRILIUM_DOCUMENT_PATH` | `${TRILIUM_DATA_DIR}/document.db` | <a class="reference-link" href="../Advanced%20Usage/Database.md">数据库</a>（存储所有笔记和元数据）的路径。 |
| `TRILIUM_BACKUP_DIR` | `${TRILIUM_DATA_DIR}/backup` | 存储自动<a class="reference-link" href="Backup.md">备份</a>数据库的目录。 |
| `TRILIUM_LOG_DIR` | `${TRILIUM_DATA_DIR}/log` | 存储每日<a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>的目录。 |
| `TRILIUM_TMP_DIR` | `${TRILIUM_DATA_DIR}/tmp` | 存储临时文件的目录（例如在外部应用中打开时）。 |
| `TRILIUM_ANONYMIZED_DB_DIR` | `${TRILIUM_DATA_DIR}/anonymized-db` | 存储<a class="reference-link" href="../Troubleshooting/Anonymized%20Database.md">匿名化数据库</a>的目录。 |
| `TRILIUM_RESOURCES_DIR` | `${TRILIUM_DATA_DIR}/resources` | 存储<a class="reference-link" href="Downloaded%20resources.md">已下载资源</a>（例如语音识别模型）的目录。 |
| `TRILIUM_CONFIG_INI_PATH` | `${TRILIUM_DATA_DIR}/config.ini` | <a class="reference-link" href="../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>文件的路径。 |
| `TRILIUM_ELECTRON_DATA_DIR` | 系统 appData | Electron 内部数据（缓存、拼写检查词典等）的目录。在便携模式下设置此项以避免写入系统配置文件（仅桌面端）。 |