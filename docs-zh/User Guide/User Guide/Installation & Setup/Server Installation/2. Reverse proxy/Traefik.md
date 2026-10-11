# Traefik
本文的目标是配置 Traefik 代理和 HTTPS。参考 [#7768](https://github.com/TriliumNext/Trilium/issues/7768#issuecomment-3539165814)。

## Traefik 3.6.4 中的破坏性变更

Traefik 3.6.4 引入了一个关于 URL 中百分号编码字符处理方式的[破坏性变更](https://doc.traefik.io/traefik/migrate/v3/#encoded-characters-in-request-path)。Trilium 会将图片或附件的标题放入其 URL 路径中，因此标题包含 `#` 或 `/` 的图片或附件会以类似 `/api/images/…/diagram%231.png` 的路径被请求。Traefik 会以 HTTP 400 拒绝这些路径，导致图片无法加载。搜索不受影响，因为它将文本放在查询参数中发送。

最简单的解决方案是升级到 Traefik 3.6.7 或更高版本，该版本回退了此配置变更。或者，也可以按照下面的章节更改配置。

<details>
    <summary>配置变更</summary>
    <p>要解决此问题，必须修改 Traefik 的<a href="https://doc.traefik.io/traefik/getting-started/configuration-overview/#the-install-configuration"><strong>静态</strong>配置</a>以允许这些字符：</p>
    <pre><code class="language-text-x-yaml">entryPoints:
  web:
    http:
      encodedCharacters:
        allowEncodedSlash: true
        allowEncodedHash: true</code></pre>
    <aside class="admonition tip"><p>如果图片仍然无法加载，你可能需要启用更多的编码字符组。有关更多信息，请参阅<a href="https://github.com/TriliumNext/Trilium/issues/7968">相关的 GitHub issue</a>；欢迎报告你的发现。</p></aside>
</details>

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
      # scheme must be HTTP instead of the usual HTTPS because Trilium listens on HTTP internally
      - traefik.http.services.trilium.loadbalancer.server.scheme=http
      - traefik.docker.network=proxy
      # forward HTTP to HTTPS
      - traefik.http.routers.trilium.middlewares=trilium-headers@docker
      - traefik.http.middlewares.trilium-headers.headers.customrequestheaders.X-Forwarded-Proto=https
```

### 设置所需的环境变量

设置反向代理后，请务必配置<a class="reference-link" href="Trusted%20proxy.md">受信任代理</a>。

### `docker-compose.yaml` 示例

```yaml
services:
  trilium:
    image: triliumnext/trilium
    container_name: trilium
    networks:
      - traefik-proxy
    environment:
      - TRILIUM_NETWORK_TRUSTEDREVERSEPROXY=my-traefik-host-ip # e.g., 172.18.0.0/16
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
      # scheme must be HTTP instead of the usual HTTPS because of how trilium works
      - traefik.http.services.trilium.loadbalancer.server.scheme=http
      - traefik.docker.network=traefik-proxy
      # Tell Trilium the original request was HTTPS
      - traefik.http.routers.trilium.middlewares=trilium-headers@docker
      - traefik.http.middlewares.trilium-headers.headers.customrequestheaders.X-Forwarded-Proto=https

networks:
  traefik-proxy:
    external: true
```