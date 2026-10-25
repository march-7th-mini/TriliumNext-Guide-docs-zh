# 手动安装
> [!WARNING]
> 本页面介绍如何在服务器上手动安装 Trilium。**请注意，这并不是一种受良好支持的 Trilium 安装方式，可能会出现问题，此处列出的信息也相当过时。建议使用** <a class="reference-link" href="Using%20Docker.md">Docker 服务器安装</a> **或** <a class="reference-link" href="Packaged%20version%20for%20Linux.md">Linux 打包版服务器安装</a>**。**

## 环境要求

Trilium 是一个 node.js 应用程序。受支持（已测试）的 node.js 版本为最新的 14.X.X 和 16.X.X。Trilium 也可能在更旧的版本上运行。

你可以使用以下命令检查你的 node 版本（需要先安装 node.js）：

```
node --version
```

如果你的 Linux 发行版只提供过时的 node.js 版本，可以查看 node.js 网站上的安装说明，其中涵盖了大多数主流发行版。

### 依赖项

还需要一些依赖项。下面是 Debian 及其衍生版本（如 Ubuntu）的命令：

```
sudo apt install libpng16-16 libpng-dev pkg-config autoconf libtool build-essential nasm libx11-dev libxkbfile-dev
```

## 安装

### 下载

你可以从 [https://github.com/TriliumNext/Trilium/releases/latest](https://github.com/TriliumNext/Trilium/releases/latest) 下载源代码的 zip/tar 包。

如需获取包含 beta 版的最新版本，请**从** `main` **分支**克隆 Git 仓库：

```
git clone -b main https://github.com/triliumnext/trilium.git
```

## 安装

```
cd trilium

# download all node dependencies
npm install

# make sure the better-sqlite3 binary is there
npm rebuild

# bundles & minifies frontend JavaScript
npm run webpack
```

## 运行

```
cd trilium

# using nohup to make sure trilium keeps running after user logs out
nohup TRILIUM_ENV=dev node src/www &
```

应用程序默认在 8080 端口启动，因此你可以打开浏览器并访问 [http://localhost:8080](http://localhost:8080) 来访问 Trilium（将 "localhost" 替换为你的主机名）。

服务器运行后，控制台会列出可访问的地址，包括网络中的其他设备可以使用的地址。

## TLS

不要忘记[配置 TLS](../HTTPS%20\(TLS\).md)，这是安全使用所必需的！