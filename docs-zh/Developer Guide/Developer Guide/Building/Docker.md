# Docker

要构建 Docker 服务器：

*   进入 `apps/server` 并运行：
    *   `pnpm docker-build-debian` 或
    *   `pnpm docker-build-alpine`。
*   同样，要构建无根版本：`pnpm docker-build-rootless-debian` 或 `pnpm docker-build-rootless-alpine`。
*   如果不仅要构建还要运行 Docker 容器，只需将 `docker-build` 替换为 `docker-start`（例如 `pnpm docker-start-debian`）。