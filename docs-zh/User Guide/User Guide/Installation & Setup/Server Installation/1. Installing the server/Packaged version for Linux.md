# Linux 打包版本
这本质上是 Trilium 源代码 + node 模块 + node.js 运行时打包成一个 7z 文件。

## 步骤

*   通过 SSH 连接到你的服务器
*   使用 `wget`（或 `curl`）在服务器上下载最新的 `TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`（从[发布页面](https://github.com/TriliumNext/Trilium/releases)复制链接，注意 `-Server` 后缀）。
*   解压归档文件，例如使用 `tar -xf -d TriliumNotes-Server-[VERSION]-linux-x64.tar.xz`
*   `cd trilium-linux-x64-server`
*   `./trilium.sh`
*   你可以打开浏览器并访问 http://\[your-server-hostname\]:8080，应该能看到 Trilium 初始化页面
*   控制台会列出服务器可访问的地址，你也可以从那里复制一个

上述步骤的问题在于，一旦你关闭 SSH 连接或终端，Trilium 进程就会终止。通常，避免这种情况的最佳方式是配置 systemd 在每次启动时后台运行 Trilium，如下一节所述。它还会在 Trilium 意外停止时重新启动它。

要在没有服务的情况下保持 Trilium 运行，请停止它（使用 <kbd>Ctrl</kbd>+<kbd>C</kbd>）并再次启动它，使其与终端分离：

*   `setsid -f ./trilium.sh > trilium.out 2>&1` 会在新会话中启动 Trilium，因此关闭终端不会影响它。其输出会写入 `trilium.out`。
*   或者，在 Bash 或 Zsh 中，`./trilium.sh > trilium.out 2>&1 & disown` 会在后台启动它并将其从 shell 的作业中移除，因此 shell 在退出时不会停止它。

> [!WARNING]
> `nohup ./trilium.sh &` 无法保持 Trilium 运行。Node.js 在启动时会重置信号处理器，因此它不再忽略 `nohup` 设置的挂起信号（`SIGHUP`），Trilium 会在终端关闭时立即停止。

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

*   现在你可以打开浏览器访问 http://\[your-server-hostname\]:8080，应该能看到 Trilium 初始化页面。

## 服务器的简单自动更新

该脚本可在 <a class="reference-link" href="Packaged%20version%20for%20Linux/Simple%20auto-update%20for%20server.dat">服务器的简单自动更新</a> 中找到。

*   以运行 Trilium 的同一用户运行。
    
    *   如果你以 `root` 运行，请从命令中移除 `sudo`。
*   需要 `jq`：
    
    ```sh
    apt install jq
    ```

它会停止上述服务，覆盖所有内容（预期没有 `config.ini`），并启动服务。它还会在 Trilium 目录中创建一个版本文件，以便仅在版本更新时进行更新。

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