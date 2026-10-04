# Docker
要为 Docker 构建服务器：

*   进入 `apps/server` 并运行：
    *   `pnpm docker-build-debian` 或
    *   `pnpm docker-build-alpine`。
*   如果不仅要构建还要运行 Docker 容器，只需将 `docker-build` 替换为 `docker-start`（例如 `pnpm docker-start-debian`）。
*   要检查镜像是否也能以非 root 用户身份运行（与 CI 一样），请运行 `sh scripts/check-docker-non-root.sh triliumnext-debian`（或 `triliumnext-alpine`）。

请在 Linux 或 WSL 中构建镜像。构建过程只保留宿主机的预构建 `better-sqlite3` 二进制文件，因此在 Windows 上生成的 `dist` 构建出的镜像会在启动时失败，并报错 `Cannot find module …/better_sqlite3.node`。

关于镜像发布到的注册表、旧仓库以及清理旧镜像，请参阅 <a class="reference-link" href="Docker%20Hub%20maintenance.md">Docker Hub 维护</a>。