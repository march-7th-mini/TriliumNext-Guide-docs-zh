# 升级 TriliumNext
本文档概述了将 Trilium 升级到新发布版本所需的步骤。

## 如何升级

Trilium 不支持内置自动升级；所有更新都必须手动执行。升级过程因安装方法而异：

*   [**Docker 服务器安装**](Server%20Installation/1.%20Installing%20the%20server/Using%20Docker.md)：拉取新镜像并重启容器。
*   **其他安装方式**：从[发布页面](https://github.com/TriliumNext/Trilium/releases/latest)下载最新版本并替换现有的应用程序文件。

## 数据库兼容性与迁移

启动时，Trilium 将自动把[数据库](../Advanced%20Usage/Database.md)迁移到新版本。请注意，迁移后，旧版本的 Trilium 将无法读取该数据库。如果您需要回退到先前版本的 Trilium 及其数据库，可以恢复在迁移前创建的[备份](Backup.md)。

## 同步兼容性

Trilium 使用的[同步](Synchronization.md)协议是版本化的，要求同步集群中的所有成员使用相同的协议版本。因此，升级到新版本时，您可能需要升级同步集群中的所有实例。同步协议版本的变更通常会在发布页面上注明。