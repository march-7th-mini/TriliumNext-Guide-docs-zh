# 使用 Kubernetes

由于 Trilium 可以在 Docker 中运行，因此也可以部署在 Kubernetes 中。您可以使用我们的 Helm chart、社区 Helm chart，或者自行创建 Kubernetes 部署。

推荐使用 Helm chart。

## 根权限

> [!NOTE]
> 目前 Trilium 容器需要以根权限运行。不过，它会在执行后切换到 UID 和 GID `1000:1000` 来运行 `node` 进程，因此主进程不会以根权限运行。

Trilium docker 容器需要以根权限运行。容器内的 node 进程会在一些初始化逻辑之后以降低的权限（uid:gid 1000:1000）启动。请确保您没有使用会更改用户 ID 的安全上下文（PodSecurityContext）。要为文件存储和应用程序使用不同的 uid:gid，请使用 `USER_UID` 和 `USER_GID` 环境变量。

docker 镜像还会修复 `/home/node` 的权限，因此您不必使用 init 容器。

## Helm Charts

来自 TriliumNext 的[官方 Helm chart](https://github.com/TriliumNext/helm-charts) 由 [ohdearaugustin](https://github.com/ohdearaugustin) 提供的非官方 helm chart：[https://github.com/ohdearaugustin/charts](https://github.com/ohdearaugustin/charts)

## 添加 Helm 仓库

以下是一个示例：

```
helm repo add trilium https://triliumnext.github.io/helm-charts
"trilium" has been added to your repositories
```

## 如何安装 chart

在查看 Helm chart 中的 [`values.yaml`](https://github.com/TriliumNext/helm-charts/blob/main/charts/trilium/values.yaml) 文件，根据需要进行修改并创建您自己的文件之后：

```
helm install --create-namespace --namespace trilium trilium trilium/trilium -f values.yaml
```

有关使用 Helm 的更多信息，请参阅 Helm 文档，或在 TriliumNext GitHub 组织中创建 Discussion。