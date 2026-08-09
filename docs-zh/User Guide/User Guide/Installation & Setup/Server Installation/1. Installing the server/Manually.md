# 手动安装

> [!警告]
> 此页面描述如何在您的服务器上手动安装 Trilium。**请注意，这不是一种受良好支持的 Trilium 安装方式，可能会出现各种问题，此处提供的信息已相当过时。建议使用** <a class="reference-link" href="Using%20Docker.md">Docker 服务器安装</a> **或** <a class="reference-link" href="Packaged%20version%20for%20Linux.md">Linux 打包版服务器安装</a>**。**

## 要求

Trilium 是一个 node.js 应用程序。受支持（经过测试）的 node.js 版本为最新的 14.X.X 和 16.X.X。Trilium 也可能适用于更早的版本。

您可以通过以下命令检查您的 node 版本（需要先安装 node.js）：

```
node --version
```

如果您的 Linux 发行版只有过时的 node.js 版本，您可以查看 node.js 网站上的安装说明，该说明涵盖了大多数主流发行版。

### 依赖项

需要一些依赖项。您可以在下方看到适用于 Debian 及其衍生版（如 Ubuntu）的命令：

```
sudo apt install libpng16-16 libpng-dev pkg-config autoconf libtool build-essential nasm libx11-dev libxkbfile-dev
```

## 安装

### 下载

您可以从 [https://github.com/TriliumNext/Trilium/releases/latest](https://github.com/TriliumNext/Trilium/releases/latest) 下载源代码的 zip/tar 压缩包。

如需包含测试版的最新版本，请使用以下命令从 `main` 分支克隆 Git 仓库：

```
git clone -b main https://github.com/triliumnext/trilium.git
```

## 安装

```
cd trilium

# 下载所有 node 依赖
npm install

# 确保 better-sqlite3 二进制文件存在
npm rebuild

# 打包并压缩前端 JavaScript
npm run webpack
```

## 运行

```
cd trilium

# 使用 nohup 确保用户注销后 trilium 仍持续运行
nohup TRILIUM_ENV=dev node src/www &
```

默认情况下，应用程序会在 8080 端口启动，因此您可以打开浏览器并访问 [http://localhost:8080](http://localhost:8080) 来使用 Trilium（将 "localhost" 替换为您的服务器主机名）。

## TLS

不要忘记 [配置 TLS](../HTTPS%20(TLS).md)，这是安全使用所必需的！