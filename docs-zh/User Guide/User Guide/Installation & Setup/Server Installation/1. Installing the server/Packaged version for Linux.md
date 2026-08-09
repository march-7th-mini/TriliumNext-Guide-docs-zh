# Linux 打包版本
这本质上是 Trilium 源码 + node 模块 + node.js 运行时打包成一个 7z 文件。

## 步骤

*   SSH 登录到你的服务器
*   使用 `wget`（或 `curl`）在服务器上下载最新的 `TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`（从[发布页面](https://github.com/TriliumNext/Trilium/releases)复制链接，注意 `-Server` 后缀）。
*   解压归档文件，例如使用 `tar -xf -d TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`
*   `cd trilium-linux-x64-server`
*   `./trilium.sh`
*   你可以打开浏览器并访问 http://\[你的服务器主机名\]:8080，你应该会看到 Trilium 初始化页面

上述步骤的问题在于，一旦你关闭 SSH 连接，Trilium 进程就会被终止。为了避免这种情况，你有两个选择：

*   终止它（例如使用 <kbd>Ctrl</kbd> + <kbd>C</kbd>）然后像这样重新运行：`nohup ./trilium.sh &`。（nohup 保持进程在后台运行，`&` 使其在后台运行）
*   配置 systemd，让 Trilium 在每次启动时自动在后台运行

## 使用 systemd 配置 Trilium 开机自启

*   下载、解压并移动 Trilium：

```
tar -xvf TriliumNotes-Server-[VERSION]-linux-x64.tar.xz
sudo mv trilium-linux-x64-server /opt/trilium
```

*   创建服务：

```
sudo nano /etc/systemd/system/trilium.service
```

*   将以下内容粘贴到文件中（根据需要替换用户和组）：

```
[Unit]
Description=Trilium Daemon
After=syslog.target network.target

[Service]
User=xxx
Group=xxx
Type=simple
ExecStart=/opt/trilium/trilium.sh
WorkingDirectory=/opt/trilium/

TimeoutStopSec=20
# KillMode=process 会导致错误，根据 https://www.freedesktop.org/software/systemd/man/systemd.kill.html
Restart=always

[Install]
WantedBy=multi-user.target
```

*   保存文件（CTRL-S）并退出（CTRL-X）
*   启用并启动服务：

```
sudo systemctl enable --now -q trilium
```

*   现在你可以打开浏览器访问 http://\[你的服务器主机名\]:8080，你应该会看到 Trilium 初始化页面。

## 服务器的简单自动更新

以运行 Trilium 的同一用户身份运行

如果你以 root 身份运行，请从命令中移除 'sudo'

需要 "jq" `apt install jq`

它会停止上述服务，覆盖所有内容（我假设没有 config.ini），然后启动服务。它还会在 Trilium 目录中创建一个版本文件，以便仅在存在更新版本时才进行更新。

```
#!/bin/bash

# 配置
REPO="TriliumNext/Trilium"
PATTERN="TriliumNotes-Server-.*-linux-x64.tar.xz"
DOWNLOAD_DIR="/var/tmp/trilium_download"
OUTPUT_DIR="/opt/trilium"
SERVICE_NAME="trilium"
VERSION_FILE="$OUTPUT_DIR/version.txt"

# 确保依赖项已安装
command -v curl >/dev/null 2>&1 || { echo "错误：需要 curl"; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "错误：需要 jq"; exit 1; }
command -v tar >/dev/null 2>&1 || { echo "错误：需要 tar"; exit 1; }

# 创建下载目录
mkdir -p "$DOWNLOAD_DIR" || { echo "错误：无法创建 $DOWNLOAD_DIR"; exit 1; }

# 获取最新发布版本
LATEST_VERSION=$(curl -sL https://api.github.com/repos/$REPO/releases/latest | jq -r '.tag_name')
if [ -z "$LATEST_VERSION" ]; then
  echo "错误：无法获取最新发布版本"
  exit 1
fi

# 检查当前安装的版本（来自 version.txt 或现有的 tarball）
CURRENT_VERSION=""
if [ -f "$VERSION_FILE" ]; then
  CURRENT_VERSION=$(cat "$VERSION_FILE")
elif [ -f "$DOWNLOAD_DIR/TriliumNotes-Server-$LATEST_VERSION-linux-x64.tar.xz" ]; then
  CURRENT_VERSION="$LATEST_VERSION"
fi

# 比较版本
if [ "$CURRENT_VERSION" = "$LATEST_VERSION" ]; then
  echo "已安装最新版本（$LATEST_VERSION）"
  exit 0
fi

# 下载最新发布版本
LATEST_URL=$(curl -sL https://api.github.com/repos/$REPO/releases/latest | jq -r ".assets[] | select(.name | test(\"$PATTERN\")) | .browser_download_url")
if [ -z "$LATEST_URL" ]; then
  echo "错误：未找到匹配模式 '$PATTERN' 的资源"
  exit 1
fi

FILE_NAME=$(basename "$LATEST_URL")
FILE_PATH="$DOWNLOAD_DIR/$FILE_NAME"

# 如果尚未下载则进行下载
if [ -f "$FILE_PATH" ]; then
  echo "最新版本 $FILE_NAME 已下载"
else
  curl -LO --output-dir "$DOWNLOAD_DIR" "$LATEST_URL" || { echo "错误：下载失败"; exit 1; }
  echo "已将 $FILE_NAME 下载到 $DOWNLOAD_DIR"
fi

# 解压 tarball
EXTRACT_DIR="$DOWNLOAD_DIR/extracted"
mkdir -p "$EXTRACT_DIR"
tar -xJf "$FILE_PATH" -C "$EXTRACT_DIR" || { echo "错误：解压失败"; exit 1; }

# 查找解压后的目录（例如，TriliumNotes-Server-0.97.2-linux-x64）
INNER_DIR=$(find "$EXTRACT_DIR" -maxdepth 1 -type d -name "TriliumNotes-Server-*-linux-x64" | head -n 1)
if [ -z "$INNER_DIR" ]; then
  echo "错误：找不到匹配 TriliumNotes-Server-*-linux-x64 的解压目录"
  exit 1
fi

# 停止 trilium-server 服务
if systemctl is-active --quiet "$SERVICE_NAME"; then
  echo "正在停止 $SERVICE_NAME 服务..."
  sudo systemctl stop "$SERVICE_NAME" || { echo "错误：无法停止 $SERVICE_NAME"; exit 1; }
fi

# 将内容复制到 /opt/trilium，覆盖现有文件
echo "正在将内容从 $INNER_DIR 复制到 $OUTPUT_DIR..."
sudo mkdir -p "$OUTPUT_DIR"
sudo cp -r "$INNER_DIR"/* "$OUTPUT_DIR"/ || { echo "错误：复制失败"; exit 1; }
echo "$LATEST_VERSION" | sudo tee "$VERSION_FILE" >/dev/null
echo "文件已复制到 $OUTPUT_DIR"

# 启动 trilium-server 服务
echo "正在启动 $SERVICE_NAME 服务..."
sudo systemctl start "$SERVICE_NAME" || { echo "错误：无法启动 $SERVICE_NAME"; exit 1; }

# 清理
rm -rf "$EXTRACT_DIR"
echo "清理完成。Trilium 已更新到 $LATEST_VERSION。"
```

## 常见问题

### glibc 过旧

```
Error: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /var/www/virtual/.../node_modules/@mlink/scrypt/build/Release/scrypt.node)
    at Object.Module._extensions..node (module.js:681:18)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)
```

如果你遇到这样的错误，你需要升级你的 glibc（通常通过升级到最新的发行版版本）或者使用其他[服务器安装](../../Server%20Installation.md)方法。

## TLS

不要忘记[配置 TLS](../HTTPS%20\(TLS\).md)，这是安全使用所必需的！