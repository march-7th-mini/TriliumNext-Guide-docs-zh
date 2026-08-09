# 使用 Docker

官方 Docker 镜像已发布在 Docker Hub 上，支持 **AMD64**、**ARMv7** 和 **ARM64/v8** 架构：[https://hub.docker.com/r/triliumnext/trilium/](https://hub.docker.com/r/triliumnext/trilium/)

## 前提条件

确保您的系统上已安装 Docker。

如果您需要有关安装 Docker 的帮助，请参考 [Docker 安装文档](https://docs.docker.com/engine/install/)

**注意：** Trilium 的 Docker 容器需要 root 权限才能正常运行。

> [!WARNING]
> 如果您使用 SMB/CIFS 共享或文件夹作为 Trilium 数据目录，[您需要](https://github.com/TriliumNext/Notes/issues/415#issuecomment-2344824400) 在挂载 SMB 共享时添加 `nobrl` 和 `noperm` 挂载选项。

## 使用 Docker Compose 运行

### 获取最新的 docker-compose.yml：

```
wget https://raw.githubusercontent.com/TriliumNext/Trilium/master/docker-compose.yml
```

（可选）在启动容器之前，编辑 `docker-compose.yml` 文件以配置容器设置。除非另行配置，否则数据目录将为 `~/trilium-data`，容器将在 8080 端口可访问。

### 启动容器：

运行以下命令在后台启动容器：

```
docker compose up -d
```

## 不使用 Docker Compose 运行 / 进一步配置

### 拉取 Docker 镜像

要拉取镜像，请使用以下命令，将 `[VERSION]` 替换为所需的版本或标签，例如 `v0.91.6` 或仅使用 `latest`。（请参阅 [https://hub.docker.com/r/triliumnext/trilium/tags](https://hub.docker.com/r/triliumnext/trilium/tags) 上发布的标签名称。）：

```
docker pull triliumnext/trilium:v0.91.6
```

**警告：** 避免使用 “latest” 标签，因为它可能会自动将您的实例升级到新的次要版本，从而可能中断同步设置或导致其他问题。

### 准备数据目录

Trilium 需要在主机系统上有一个目录来存储其数据。此目录必须挂载到 Docker 容器中并具有写权限。

### 运行 Docker 容器

#### 仅本地访问

运行容器以使其只能从 localhost 访问。此设置适用于测试或使用 Nginx 或 Apache 等代理服务器时。

```
sudo docker run -t -i -p 127.0.0.1:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

1.  使用 `docker ps` 验证容器是否正在运行。
2.  通过 Web 浏览器访问 `127.0.0.1:8080` 上的 Trilium。

#### 本地网络访问

要使容器只能在本地网络上访问，请先创建一个新的 Docker 网络：

```
docker network create -d macvlan -o parent=eth0 --subnet 192.168.2.0/24 --gateway 192.168.2.254 --ip-range 192.168.2.252/27 mynet
```

然后，使用网络设置运行容器：

```
docker run --net=mynet -d -p 127.0.0.1:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:-latest
```

要为保存的数据设置不同的用户 ID (UID) 和组 ID (GID)，请使用 `USER_UID` 和 `USER_GID` 环境变量：

```
docker run --net=mynet -d -p 127.0.0.1:8080:8080 -e "USER_UID=1001" -e "USER_GID=1001" -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:-latest
```

使用 `docker inspect [container_name]` 查找本地 IP 地址，并从本地网络上的设备访问该服务。

```
docker ps
docker inspect [container_name]
```

#### 全局访问

要允许从任何 IP 地址访问，请按如下方式运行容器：

```
docker run -d -p 0.0.0.0:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

使用 `docker stop <CONTAINER ID>` 停止容器，其中容器 ID 从 `docker ps` 获取。

### 自定义数据目录

对于自定义数据目录，请使用：

```
-v ~/YourOwnDirectory:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

如果您想以非默认方式运行实例，请按如下方式使用卷开关：`-v ~/YourOwnDirectory:/home/node/trilium-data triliumnext/trilium:<VERSION>`。了解 Docker 卷的工作原理非常重要，第一个路径是您自己的路径，第二个路径是要虚拟绑定的路径。[https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/) 冒号前的路径是主机目录，冒号后的路径是容器的路径。更多详细信息可以在 [Docker 卷文档](https://docs.docker.com/storage/volumes/) 中找到。

## 反向代理

1.  [Nginx](../2.%20Reverse%20proxy/Nginx.md)
2.  [Apache](../2.%20Reverse%20proxy/Apache%20using%20Docker.md)

### 关于 --user 指令的说明

不支持 `--user` 指令。请改用 `USER_UID` 和 `USER_GID` 环境变量来设置适当的用户和组 ID。

### 关于时区的说明

如果您遇到时区问题并且未使用 docker-compose，则可能需要添加一个 `TZ` 环境变量，其值为您本地时区的 [TZ 标识符](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)。

## 无根 Docker 镜像

> [!NOTE]
> 请记住，数据目录位于 `/home/trilium/trilium-data`，而不是通常的 `/home/node/trilium-data`。这是因为在无根容器中创建了一个新用户来运行 Trilium。

如果您希望在不以 `root` 身份运行 Docker 容器的情况下运行 Trilium，则可以使用带有 `rootless` 标签的 Debian（默认）和 Alpine 镜像中的任意一个。

_**如果您不确定，请坚持使用上面提到的 “rootful” Docker 镜像。**_

以下是一些拉取无根镜像的命令：

```
# 对于基于 Debian 的镜像
docker pull triliumnext/trilium:rootless

# 对于基于 Alpine 的镜像
docker pull triliumnext/trilium:rootless-alpine
```

### 为什么使用无根模式？

以非 root 用户身份运行容器是一种安全最佳实践，可以降低容器逃逸的潜在影响。如果攻击者设法逃逸容器，他们只会拥有非 root 用户的权限，而不是对主机的完全 root 访问权限。

### 工作原理

无根 Trilium 镜像：

1.  在构建时创建一个非 root 用户（`trilium`）
2.  将应用程序配置为以此非 root 用户身份运行
3.  允许通过 Docker 的 `--user` 标志在运行时自定义用户的 UID/GID
4.  不需要单独的 Docker `entrypoint` 脚本

### 使用方法

#### **使用 docker-compose（推荐）**

```
# 使用默认 UID/GID (1000:1000) 运行
docker-compose -f docker-compose.rootless.yml up -d

# 使用自定义 UID/GID 运行（例如，匹配您的主机用户）
TRILIUM_UID=$(id -u) TRILIUM_GID=$(id -g) docker-compose -f docker-compose.rootless.yml up -d

# 指定自定义数据目录
TRILIUM_DATA_DIR=/path/to/your/data TRILIUM_UID=$(id -u) TRILIUM_GID=$(id -g) docker-compose -f docker-compose.rootless.yml up -d

```

#### **使用 Docker CLI**

```
# 构建镜像
docker build -t triliumnext/trilium:rootless -f apps/server/Dockerfile.rootless .

# 使用默认 UID/GID (1000:1000) 运行
docker run -d --name trilium -p 8080:8080 -v ~/trilium-data:/home/trilium/trilium-data triliumnext/trilium:rootless

# 使用自定义 UID/GID 运行
docker run -d --name trilium -p 8080:8080 --user $(id -u):$(id -g) -v ~/trilium-data:/home/trilium/trilium-data triliumnext/trilium:rootless

```

### 环境变量

*   `TRILIUM_UID`：用于容器进程的 UID（传递给 Docker 的 `--user` 标志）
*   `TRILIUM_GID`：用于容器进程的 GID（传递给 Docker 的 `--user` 标志）
*   `TRILIUM_DATA_DIR`：容器内数据目录的路径（默认：`/home/node/trilium-data`）

有关配置环境变量（网络设置、身份验证、同步等）的完整列表，请参阅 <a class="reference-link" href="../../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>。

### 卷权限

如果您遇到数据卷的权限问题，请确保：

1.  主机目录对您使用的 UID/GID 具有适当的权限
2.  您同时设置了 `TRILIUM_UID` 和 `TRILIUM_GID` 以匹配主机目录的所有者

```
# 例如，如果您的数据目录由 UID 1001 和 GID 1001 所有：
TRILIUM_UID=1001 TRILIUM_GID=1001 docker-compose -f docker-compose.rootless.yml up -d

```

### 注意事项

*   容器以特定的 UID/GID 启动，可以在运行时自定义
*   与传统设置不同，此方法不使用带有 `usermod`/`groupmod` 命令的单独 entrypoint 脚本
*   容器无法在运行时修改自身的 UID/GID，这是无根容器的一项安全功能

### 可用的无根镜像

提供了两个无根变体：

1.  **基于 Debian**（默认）：使用 Debian Bullseye Slim 基础镜像
    *   Dockerfile：`apps/server/Dockerfile.rootless`
    *   推荐给大多数用户
2.  **基于 Alpine**：使用 Alpine 基础镜像以获得更小的体积
    *   Dockerfile：`apps/server/Dockerfile.alpine.rootless`
    *   镜像体积更小，但可能与某些系统存在兼容性问题

### 构建自定义无根镜像

如果您愿意，还可以在构建时自定义 UID/GID：

```
# 对于具有自定义 UID/GID 的基于 Debian 的镜像
docker build --build-arg USER=myuser --build-arg UID=1001 --build-arg GID=1001 \
  -t triliumnext/trilium:rootless-custom -f apps/server/Dockerfile.rootless .

# 对于具有自定义 UID/GID 的基于 Alpine 的镜像
docker build --build-arg USER=myuser --build-arg UID=1001 --build-arg GID=1001 \
  -t triliumnext/trilium:alpine-rootless-custom -f apps/server/Dockerfile.alpine.rootless .

```

可用的构建参数：

*   `USER`：非 root 用户的用户名（默认：trilium）
*   `UID`：非 root 用户的用户 ID（默认：1000）
*   `GID`：非 root 用户的组 ID（默认：1000）