# 使用 Kubernetes
由于 Trilium 可以在 Docker 中运行，它也可以部署在 Kubernetes 中。你可以使用我们的 Helm chart、社区 Helm chart，或者自行构建 Kubernetes 部署。

推荐的方式是使用 Helm chart。

## Root 权限

默认情况下，Trilium 容器以 root 身份启动，将数据目录的所有权赋予 UID 和 GID `1000:1000`，然后以降低后的权限运行 Trilium，因此不需要 init 容器来修复权限。要使用不同的 UID 和 GID，请设置 `USER_UID` 和 `USER_GID` 环境变量。

从 v0.107.0 开始，容器也可以在没有 root 的情况下运行，这是 `restricted` Pod Security Standard 所要求的。在 Pod 的 security context 中设置用户，并设置 `fsGroup`，以便 Kubernetes 将卷分配给该组：

```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
  runAsNonRoot: true
  fsGroup: 1000
```

在该模式下，`USER_UID` 和 `USER_GID` 会被忽略。关于数据目录需要什么，请参阅 <a class="reference-link" href="Using%20Docker.md">使用 Docker</a> 中关于以非 root 用户运行的部分。

## Helm Charts

来自 TriliumNext 的[官方 Helm chart](https://github.com/TriliumNext/helm-charts)，以及由 [ohdearaugustin](https://github.com/ohdearaugustin) 提供的非官方 Helm chart：[https://github.com/ohdearaugustin/charts](https://github.com/ohdearaugustin/charts)

## 添加 Helm 仓库

以下是一个示例

```
helm repo add trilium https://triliumnext.github.io/helm-charts
"trilium" has been added to your repositories
```

## 如何安装 chart

在查看 Helm chart 的 [`values.yaml`](https://github.com/TriliumNext/helm-charts/blob/main/charts/trilium/values.yaml)、按需修改并创建你自己的之后：

```
helm install --create-namespace --namespace trilium trilium trilium/trilium -f values.yaml
```

有关使用 Helm 的更多信息，请参阅 Helm 文档，或在 TriliumNext GitHub Organization 中发起 Discussion。