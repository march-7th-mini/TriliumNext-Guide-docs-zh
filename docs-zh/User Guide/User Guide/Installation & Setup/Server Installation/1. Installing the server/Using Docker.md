# 使用 Docker
官方 Docker 镜像已发布在 Docker Hub 上，支持 **AMD64**、**ARMv7** 和 **ARM64/v8**：[https://hub.docker.com/r/triliumnext/trilium/](https://hub.docker.com/r/triliumnext/trilium/)

## 前提条件

确保你的系统上已安装 Docker。

如果你需要安装 Docker 的帮助，请参考 [Docker 安装文档](https://docs.docker.com/engine/install/)

默认情况下，容器以 root 身份启动，准备好数据目录，然后以非特权用户身份运行 Trilium。它也可以完全以非 root 身份运行，如下文 _以非 root 用户运行_ 所述。

> [!WARNING]
> 如果你使用 SMB/CIFS 共享或文件夹作为 Trilium 数据目录，[你需要](https://github.com/TriliumNext/Notes/issues/415#issuecomment-2344824400)在挂载 SMB 共享时添加 `nobrl` 和 `noperm` 挂载选项。

## 使用 Docker Compose 运行

### 获取最新的 docker-compose.yml：

```
wget https://raw.githubusercontent.com/TriliumNext/Trilium/master/docker-compose.yml
```

可选地，在启动之前编辑 `docker-compose.yml` 文件以配置容器设置。除非另有配置，数据目录将是 `docker-compose.yml` 旁边的 `trilium-data`，容器将可通过端口 8080 访问。

要将数据保存在其他地方，请编辑 `docker-compose.yml` 中的 `volumes` 条目，并更改冒号前的主机路径（例如 `- /srv/trilium-data:/home/node/trilium-data`）。冒号后的路径保持不变。

### 启动容器：

运行以下命令在后台启动容器：

```
docker compose up -d
```

## 不使用 Docker Compose 运行 / 进一步配置

### 拉取 Docker 镜像

要拉取镜像，请使用以下命令，将 `[VERSION]` 替换为所需的版本或标签，例如 `v0.91.6` 或仅 `latest`。（查看已发布的标签名称：[https://hub.docker.com/r/triliumnext/trilium/tags](https://hub.docker.com/r/triliumnext/trilium/tags)。）：

```
docker pull triliumnext/trilium:v0.91.6
```

**警告：** 避免使用 "latest" 标签，因为它可能会自动将你的实例升级到新的次要版本，可能中断同步设置或导致其他问题。

### 准备数据目录

Trilium 需要在主机系统上有一个目录来存储其数据。此目录必须以写权限挂载到 Docker 容器中。

### 运行 Docker 容器

#### 仅本地访问

运行容器使其仅可从 localhost 访问。此设置适用于测试或使用 Nginx 或 Apache 等代理服务器时。

```
sudo docker run -t -i -p 127.0.0.1:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

1.  使用 `docker ps` 验证容器正在运行。
2.  通过 Web 浏览器在 `127.0.0.1:8080` 访问 Trilium。

#### 本地网络访问

要使容器仅在你的本地网络上可访问，首先创建一个新的 Docker 网络：

```
docker network create -d macvlan -o parent=eth0 --subnet 192.168.2.0/24 --gateway 192.168.2.254 --ip-range 192.168.2.252/27 mynet
```

然后，使用网络设置运行容器：

```
docker run --net=mynet -d -p 127.0.0.1:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:-latest
```

要为保存的数据设置不同的用户 ID（UID）和组 ID（GID），请使用 `USER_UID` 和 `USER_GID` 环境变量：

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

如果你想以非默认方式运行实例，请按如下方式使用卷开关：`-v ~/YourOwnDirectory:/home/node/trilium-data triliumnext/trilium:<VERSION>`。重要的是要了解 Docker 如何处理卷，第一个路径是你自己的路径，第二个是要虚拟绑定的路径。[https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/) 冒号前的路径是主机目录，冒号后的路径是容器的路径。更多详细信息可在 [Docker 卷文档](https://docs.docker.com/storage/volumes/) 中找到。

## 反向代理

1.  [Nginx](../2.%20Reverse%20proxy/Nginx.md)
2.  [Apache](../2.%20Reverse%20proxy/Apache%20using%20Docker.md)

### 关于时区的说明

如果你遇到时区问题且未使用 docker-compose，你可能需要添加一个 `TZ` 环境变量，其值为你本地时区的 [TZ 标识符](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)。

### 其他环境变量

有关 Trilium 读取的完整环境变量列表（网络设置、身份验证、同步等），请参阅 <a class="reference-link" href="../../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>。

## 以非 root 用户运行

默认情况下，容器以 root 身份启动，将数据目录交给 `node` 用户（UID 和 GID 为 `1000`，或 `USER_UID` 和 `USER_GID` 的值），然后以该用户身份运行 Trilium。某些环境根本不允许容器以 root 身份启动，例如无根 Docker 或 Podman，或使用 `runAsNonRoot` 的 Kubernetes。从 v0.107.0 开始，同一镜像可以完全以非 root 用户身份运行。

要以非 root 用户运行 Trilium，请使用 Docker 的 `--user` 标志设置用户：

```sh
docker run -d -p 8080:8080 --user 1000:1000 -v /srv/trilium-data:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

使用 Docker Compose 时，在 `docker-compose.yml` 中为服务添加 `user:`：

```yaml
services:
  trilium:
    user: "1000:1000"
```

该镜像还可以在只读根文件系统且没有任何能力的情况下运行，例如使用 `--read-only --tmpfs /tmp --cap-drop ALL --security-opt no-new-privileges`。

没有 root 权限时，容器无法更改文件的所有权，因此：

*   主机上的数据目录必须在容器启动前存在并属于该用户。如果目录不存在，Docker 会以 root 身份创建它，Trilium 将无法写入。例如：
    
    ```sh
    mkdir -p /srv/trilium-data
    sudo chown 1000:1000 /srv/trilium-data
    ```
*   使用命名卷而非主机目录仅适用于 UID `1000`：Docker 会将新卷的所有者设为镜像数据目录的所有者，即 `node` 用户。
*   `USER_UID` 和 `USER_GID` 会被忽略。用户仅来自 `--user` 或 `user:`。

如果 Trilium 无法使用其数据目录，它会在启动时停止，并打印出它无法使用的目录或文件、其所有者以及修复命令。

> [!NOTE]
> 以 root 身份运行的安装会将其文件保留为 UID `1000` 所有，或者如果设置了 `USER_UID`，则为该值所有。要将其切换为 `--user`，请使用相同的 UID，或先将数据目录交给新用户，例如使用 `sudo chown -R 1001:1001 /srv/trilium-data`。