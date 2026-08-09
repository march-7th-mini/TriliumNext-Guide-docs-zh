# 多服务器实例

Trilium 不支持多用户。若需让两个或更多人各自拥有自己的笔记集，必须设置多个服务器实例。同时也不支持使用多个[同步](../../Synchronization.md)服务器。

要在单台物理服务器上运行多个服务器实例：

*   对于<a class="reference-link" href="Packaged%20version%20for%20Linux.md">Linux 打包版本</a>或<a class="reference-link" href="Manually.md">手动安装</a>，如果手动启动服务器，只需为每个实例指定不同的端口和数据目录：
    
    ```
    TRILIUM_NETWORK_PORT=8080 TRILIUM_DATA_DIR=/path/to/your/data-dir-A /opt/trilium/trilium.sh
    ```
    
    对于第二个实例：
    
    ```
    TRILIUM_NETWORK_PORT=8081 TRILIUM_DATA_DIR=/path/to/your/data-dir-B /opt/trilium/trilium.sh
    ```
    
    如果使用 `systemd`，请在[服务配置中设置环境变量](https://serverfault.com/questions/413397/how-to-set-environment-variable-in-systemd-service)。
*   对于<a class="reference-link" href="Using%20Docker.md">使用 Docker</a>，只需使用两个不同的容器，每个容器拥有各自的端口绑定和数据目录。
*   对于<a class="reference-link" href="On%20NixOS.md">在 NixOS 上</a>，唯一可行的方法是使用 Docker OCI 容器，或至少使用一个带有自身服务定义的 NixOS 容器。

如需支持或了解更多背景信息，请参阅相关的 [GitHub 讨论](https://github.com/orgs/TriliumNext/discussions/1642#discussioncomment-12768808)。