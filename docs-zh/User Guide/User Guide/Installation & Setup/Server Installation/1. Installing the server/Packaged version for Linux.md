# Linux 打包版本
这本质上是 Trilium 源代码 + node 模块 + node.js 运行时打包成一个 7z 文件。

## 步骤

*   通过 SSH 连接到你的服务器
*   使用 `wget`（或 `curl`）在服务器上下载最新的 `TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`（从[发布页面](https://github.com/TriliumNext/Trilium/releases)复制链接，注意 `-Server` 后缀）。
*   解压归档文件，例如使用 `tar -xf -d TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`
*   `cd trilium-linux-x64-server`
*   `./trilium.sh`
*   你可以打开浏览器并访问 http://\[your-server-hostname\]:8080，你应该能看到 Trilium 初始化页面

上述步骤的问题在于，一旦你关闭 SSH 连接，Trilium 进程就会终止。为避免这种情况，你有两个选择：

*   终止它（例如使用 <kbd>Ctrl</kbd> + <kbd>C</kbd>）并像这样重新运行：`nohup ./trilium.sh &`。（nohup 使进程在后台保持运行，`&` 使其在后台运行）
*   配置 systemd 以在每次启动时自动在后台运行 Trilium

## 配置 Trilium 使用 systemd 开机自启

*   下载后，解压并移动 Trilium：

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
# KillMode=process leads to error, according to https://www.freedesktop.org/software/systemd/man/systemd.kill.html
Restart=always

[Install]
WantedBy=multi-user.target
```

*   保存文件（CTRL-S）并退出（CTRL-X）
*   启用并启动服务：

```
sudo systemctl enable --now -q trilium
```

*   现在你可以打开浏览器访问 http://\[your-server-hostname\]:8080，你应该能看到 Trilium 初始化页面。

## 服务器简易自动更新

该脚本位于 <a class="reference-link" href="Packaged%20version%20for%20Linux/Simple%20auto-update%20for%20server.dat">服务器简易自动更新</a>。

*   以运行 Trilium 的同一用户运行。
    
    *   如果你以 `root` 运行，请从命令中移除 `sudo`。
*   需要 `jq`：
    
    ```sh
    apt install jq
    ```

它将停止上述服务，覆盖所有内容（预期没有 `config.ini`），并启动服务。它还会在 Trilium 目录中创建一个版本文件，以便仅在出现更新版本时才进行更新。

## 常见问题

### glibc 过旧

```
Error: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /var/www/virtual/.../node_modules/@mlink/scrypt/build/Release/scrypt.node)
    at Object.Module._extensions..node (module.js:681:18)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)
```

如果你遇到类似这样的错误，你需要升级 glibc（通常通过升级到最新的发行版版本）或使用其他[服务器安装](../../Server%20Installation.md)方法。

## TLS

不要忘记[配置 TLS](../HTTPS%20\(TLS\).md)，这是安全使用所必需的！