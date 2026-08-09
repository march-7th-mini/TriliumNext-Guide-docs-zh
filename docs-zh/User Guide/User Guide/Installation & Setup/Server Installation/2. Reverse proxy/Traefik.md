# Traefik

本文的目标是配置 Traefik 代理和 HTTPS。参考 [#7768](https://github.com/TriliumNext/Trilium/issues/7768#issuecomment-3539165814)。

## Traefik 3.6.4 中的重大变更

Traefik 3.6.4 引入了一项关于 URL 中百分号编码字符处理方式的[重大变更](https://doc.traefik.io/traefik/migrate/v3/#encoded-characters-in-request-path)。具体来说，Trilium 使用的某些 URL（例如 `search/%23workspace%20%23!template`）会被 Traefik 自动拒绝，导致 HTTP 400 错误。

为了解决此问题，必须修改 Traefik 的 [**静态**配置](https://doc.traefik.io/traefik/getting-started/configuration-overview/#the-install-configuration)以允许这些字符：

```yaml
entryPoints:
  web:
    http:
      encodedCharacters:
        allowEncodedSlash: true
        allowEncodedHash: true
```

> [!TIP]
> 如果问题仍然存在，根据 Trilium 的使用方式（尤其是搜索功能），您可能需要启用更多编码字符组。有关更多信息，请参阅[相关的 GitHub issue](https://github.com/TriliumNext/Trilium/issues/7968)；欢迎报告您的发现。

### 构建 docker-compose 文件

将 Traefik 设置为反向代理需要设置以下标签：

```yaml
    labels:
      - traefik.enable=true
      - traefik.http.routers.trilium.entrypoints=https
      - traefik.http.routers.trilium.rule=Host(`trilium.mydomain.tld`)
      - traefik.http.routers.trilium.tls=true
      - traefik.http.routers.trilium.service=trilium
      - traefik.http.services.trilium.loadbalancer.server.port=8080
      # scheme 必须是 HTTP 而不是通常的 HTTPS，因为 Trilium 在内部监听 HTTP
      - traefik.http.services.trilium.loadbalancer.server.scheme=http
      - traefik.docker.network=proxy
      # 将 HTTP 转发到 HTTPS
      - traefik.http.routers.trilium.middlewares=trilium-headers@docker
      - traefik.http.middlewares.trilium-headers.headers.customrequestheaders.X-Forwarded-Proto=https
```

### 设置所需的环境变量

设置反向代理后，请确保配置 <a class="reference-link" href="Trusted%20proxy.md">可信代理</a>。

### 示例 `docker-compose.yaml`

```yaml
services:
  trilium:
    image: triliumnext/trilium
    container_name: trilium
    networks:
      - traefik-proxy
    environment:
      - TRILIUM_NETWORK_TRUSTEDREVERSEPROXY=my-traefik-host-ip # 例如，172.18.0.0/16
    volumes:
      - /path/to/data:/home/node/trilium-data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    labels:
      - traefik.enable=true
      - traefik.http.routers.trilium.entrypoints=https
      - traefik.http.routers.trilium.rule=Host(`trilium.mydomain.tld`)
      - traefik.http.routers.trilium.tls=true
      - traefik.http.routers.trilium.service=trilium
      - traefik.http.services.trilium.loadbalancer.server.port=8080
      # scheme 必须是 HTTP 而不是通常的 HTTPS，因为 Trilium 的工作方式
      - traefik.http.services.trilium.loadbalancer.server.scheme=http
      - traefik.docker.network=traefik-proxy
      # 告知 Trilium 原始请求是 HTTPS
      - traefik.http.routers.trilium.middlewares=trilium-headers@docker
      - traefik.http.middlewares.trilium-headers.headers.customrequestheaders.X-Forwarded-Proto=https

networks:
  traefik-proxy:
    external: true
```