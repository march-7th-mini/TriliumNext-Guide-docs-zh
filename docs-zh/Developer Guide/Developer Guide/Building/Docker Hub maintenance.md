# Docker Hub 维护
Trilium 的服务器镜像由 `.github/workflows/main-docker.yml` 构建，并发布到两个注册表：GHCR（`ghcr.io/triliumnext/trilium`）和 Docker Hub（`triliumnext/trilium`）。本页说明哪些标签发布到哪里、旧仓库如何保持更新，以及如何清理一个积累了无人使用镜像的仓库。

## 标签发布到哪里

| 标签 | GHCR | Docker Hub | 创建方式 |
| --- | --- | --- | --- |
| `main` | 是 | 是 | 每次推送到 `main` 且涉及应用变更时 |
| `sha-<commit>` | 是 | **否** | 每次构建 |
| `v<version>` | 是 | 是 | 版本标签 |
| `stable`、`latest` | 是 | 是 | 不带连字符的版本标签（非预发布版） |
| `<branch-name>` | 是 | 是 | 在分支上手动运行工作流 |

`sha-*` 标签只保留在 GHCR 上。在 2026 年 10 月之前，它们也会被复制到 Docker Hub，而那里从没有任何机制删除它们：到 2026 年 10 月，`triliumnext/trilium` 中 1,698 个标签里有 1,672 个是 `sha-*`，仓库报告的存储量为 974 GB。

在分支上手动运行工作流还会发布一个以分支命名的标签，其中 `/` 替换为 `-`（例如 `feature-deployment_fixes`）。分支合并后，请在 Docker Hub 上删除它。

每次推送到 `main` 都会移动 `main` 标签，并在 Docker Hub 上留下上一个没有标签的镜像，每天大约十几个。在 `main` 仅保留在 GHCR 上之前，请按下文所述定期清理它们。

## 旧仓库

两个较旧的 Docker Hub 仓库仍然收到大量来自自动更新安装的拉取：

| 仓库 | 历史 | 每周拉取量（2026 年 9 月） |
| --- | --- | --- |
| `triliumnext/notes` | 重命名前 TriliumNext 的镜像，最后一次自行构建为 v0.95.0 | ~29,600 |
| `zadam/trilium` | 最初的 Trilium 镜像，最后一次自行构建为 0.63.7 | ~24,000 |

`.github/workflows/mirror-legacy-docker.yml` 在每次稳定版发布后将 `ghcr.io/triliumnext/trilium:stable` 复制到 `triliumnext/notes:stable`、`triliumnext/notes:latest` 和 `zadam/trilium:latest`；`main-docker.yml` 从其 `mirror_legacy` 作业中调用它。`zadam/trilium` 上的版本标签和 `0.63-latest` 保持不变，因此固定版本的安装会保留该版本。要手动运行镜像同步，请从 _Actions_ 标签页启动工作流；_tags_ 字段留空会写入每个仓库的发布标签。

每个仓库都有自己的凭据：

*   `triliumnext/notes` 使用 `DOCKERHUB_USERNAME` 和 `DOCKERHUB_TOKEN` 密钥，与主镜像相同。
*   `zadam/trilium` 以 `zadam` 身份登录，使用 `ZADAM_DOCKERHUB_TOKEN` 密钥，即该账户的 Read & Write 访问令牌。个人访问令牌无法限制到单个仓库，因此请为其设置到期日期。

拉取统计信息位于 Docker Hub 上每个仓库的页面；`hub.mjs stats`（见下文）会打印它们，包括 Docker Hub 为组织拥有的仓库发布的每周序列。

## Docker Hub 如何存储镜像

四个事实决定了清理的工作方式：

*   **删除标签不会删除镜像。** 镜像仍留在仓库中，仍可通过摘要拉取，并且仍计入仓库的存储量。只有删除未打标签的镜像才能释放空间。
*   **删除镜像索引也会删除其中的镜像。** 多平台镜像是一个索引，它指向每个平台的一个清单及其证明（Trilium 为八个）。一旦索引被删除，这些清单也会返回 `404`，因此清理只删除索引。
*   **Docker Hub 拒绝删除仍被标签使用的清单。** 对此类摘要执行 `DELETE` 会返回 `403`，因此清理不会破坏保留的标签，即使被删除的镜像与某个发布版共享摘要（发布提交的 `sha-*` 构建与 `v<version>` 是同一个镜像）。
*   **`GET /v2/namespaces/<namespace>/repositories/<name>/manifests` 列出仓库中的每个清单，包括未打标签的。** 它不在 Docker 的公开 API 参考中。它会把已打标签索引的各平台镜像报告为未打标签，因此一个未打标签的单一清单不一定是孤立的。

> [!WARNING]
> 切勿在 Docker Hub 的 _Image Management_ 页面中批量删除未打标签的 _Image_ 条目。每个保留标签的各平台镜像都会在那里显示为未打标签，删除它们会破坏这些标签的 `docker pull`。只删除镜像索引。

## 清理仓库

`.claude/skills` 中的 `maintaining-docker-hub` 技能提供了 `hub.mjs`，它完成整个清理工作。除非传入 `--delete`，否则每个执行删除的命令都是试运行。

```sh
H=.claude/skills/maintaining-docker-hub/hub.mjs
node $H stats triliumnext/trilium                      # pulls, stars, storage, tag count
node $H tags triliumnext/trilium --prefix sha-         # list tags; --delete deletes them
node $H inventory triliumnext/trilium                  # tagged and untagged manifests
node $H purge triliumnext/trilium --older-than 7       # untagged indexes; --delete deletes them
```

它读取 `docker login` 的凭据（或 `DOCKERHUB_USERNAME` 和 `DOCKERHUB_TOKEN`）。删除需要拥有该命名空间的账户。

要清理仓库：

1.  使用 `tags <repo> --prefix <prefix> --delete` 删除不需要的标签。Docker Hub 一次最多列出 1,000 个标签，且其标签计数比删除操作滞后几分钟，因此请反复运行，直到找不到任何标签。
2.  使用 `purge <repo> --delete` 删除未打标签的索引。`purge` 会保留每个剩余标签的索引和各平台镜像，并且在仓库有超过 1,000 个标签时拒绝运行，因为其要保留的标签列表会不完整。
3.  使用 `docker manifest inspect <repo>:<tag>` 检查保留的标签，包括 `latest`、`stable`、`main` 和几个版本，并使用 `stats` 检查存储量。

存储量会在几分钟内更新。2026 年 10 月，这一操作将 `triliumnext/trilium` 从 974 GB 降至 18 GB，将 `triliumnext/notes` 从 658 GB 降至 19 GB，总共约 17,000 个未打标签的索引，删除速度为每分钟 60 到 250 个。

## 另请参阅

*   <a class="reference-link" href="Docker.md">Docker</a>，用于在本地构建镜像。
*   [docker/hub-feedback#2448](https://github.com/docker/hub-feedback/issues/2448)，Docker 在此宣布支持通过注册表 API 删除清单。
*   docs.docker.com 上的 [Registry API reference](https://docs.docker.com/reference/api/registry/latest/)。