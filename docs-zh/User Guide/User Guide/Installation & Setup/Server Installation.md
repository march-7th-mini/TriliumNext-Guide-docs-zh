# 服务器安装

本指南概述了在您自己的服务器上安装 Trilium 的步骤。如果您想设置[同步](Synchronization.md)或在浏览器中使用 Trilium（可从任何地方访问），您可以考虑此选项。

## 安装选项

有几种方法可以在服务器上安装 Trilium，每种方法都有其自身的优势：

*   **推荐**：[Docker 安装](Server%20Installation/1.%20Installing%20the%20server/Using%20Docker.md) - 适用于 **AMD64** 和 **ARM** 架构。
*   [Linux 打包服务器安装](Server%20Installation/1.%20Installing%20the%20server/Packaged%20version%20for%20Linux.md)
*   [PikaPods 托管服务](https://www.pikapods.com/pods?run=trilium-next)
*   [手动安装](Server%20Installation/1.%20Installing%20the%20server/Manually.md)
*   [Kubernetes](Server%20Installation/1.%20Installing%20the%20server/Using%20Kubernetes.md)
*   [Cloudron](https://www.cloudron.io/store/com.github.trilium.cloudronapp.html)
*   [HomelabOS](https://homelabos.com/docs/software/trilium/)
*   [NixOS 模块](Server%20Installation/1.%20Installing%20the%20server/On%20NixOS.md)

服务器安装包括 Web 和[移动前端](Mobile%20Frontend.md)。

## 配置

设置完服务器安装后，您可能需要配置端口或启用 [TLS](Server%20Installation/HTTPS%20\(TLS\).md) 等设置。配置通过 Trilium `config.ini` 文件进行管理，该文件默认位于[数据目录](Data%20directory.md)中。要开始自定义您的设置，请将提供的包含默认值的 `config-sample.ini` 文件复制为 `config.ini`。

您也可以查看[配置](../Advanced%20Usage/Configuration%20\(config.ini%20or%20environment%20variables\).md)文件，将所有 `config.ini` 值作为环境变量提供。

### 配置位置

默认情况下，`config.ini`、[数据库](../Advanced%20Usage/Database.md)和其他重要的 Trilium 数据文件存储在[数据目录](Data%20directory.md)中。如果您希望使用其他位置，可以通过设置 `TRILIUM_DATA_DIR` 环境变量来更改：

```
export TRILIUM_DATA_DIR=/home/myuser/data/my-trilium-data
```

### 禁用身份验证

参见 <a class="reference-link" href="Server%20Installation/Authentication.md">身份验证</a>。

## 反向代理设置

要为 Trilium 配置反向代理，您可以使用 **nginx** 或 **Apache**。您也可以查看反向代理文件夹中存储的文档。

### nginx

将以下配置添加到您的 `nginx` 设置中，以将请求代理到 Trilium：

```
location /trilium/ {
    proxy_pass http://127.0.0.1:8080/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
}
```

为避免限制负载大小，请在 `server {}` 块中包含以下内容：

```
# 设置为 0 表示无限制。默认值为 1M。
client_max_body_size 0;
```

### Apache

对于 Apache 设置，请参阅 [Apache 代理设置](Server%20Installation/2.%20Reverse%20proxy/Apache%20using%20Docker.md)指南。