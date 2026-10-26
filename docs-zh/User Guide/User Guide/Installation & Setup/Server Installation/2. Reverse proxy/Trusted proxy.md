# 受信任的代理
如果你在[反向代理](../2.%20Reverse%20proxy.md)下运行 Trilium 服务器，将其配置为受信任的代理非常重要，这样应用程序才能正确识别客户端的真实 IP 地址。Trilium 使用该地址进行[暴力破解防护](../Authentication.md)、记录日志中的登录失败条目，以及检测连接是否通过 HTTPS 建立。

如果没有此设置，每个请求看起来都来自反向代理，因此所有客户端共享同一个登录失败尝试次数限制。

## 配置受信任的代理

要信任反向代理，请修改 <a class="reference-link" href="../../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>，并将 `trustedReverseProxy` 设置为反向代理连接 Trilium 时使用的地址：

```
[Network]
trustedReverseProxy=loopback
```

该值是以逗号分隔的 IP 地址列表、CIDR 表示法的子网，或以下名称之一：

| 名称 | 地址 |
| --- | --- |
| `loopback` | `127.0.0.1/8`、`::1/128` |
| `linklocal` | `169.254.0.0/16`、`fe80::/10` |
| `uniquelocal` | `10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`、`fc00::/7` |

随后 Trilium 会从 `X-Forwarded-For` 头中读取客户端地址，取最右侧不属于受信任地址的条目。客户端添加到该头中的条目位于代理追加的条目左侧，因此会被忽略。

常见配置：

*   **反向代理与 Trilium 运行在同一台机器上**：使用 `loopback`。
*   **Trilium 运行在 Docker 中，反向代理位于宿主机或另一个容器中**：使用 Docker 网络的子网（例如 `172.18.0.0/16`），或使用 `uniquelocal` 覆盖所有 Docker 网络。使用环境变量时：`TRILIUM_NETWORK_TRUSTEDREVERSEPROXY=172.18.0.0/16`。
*   **反向代理运行在另一台机器上**：使用其 IP 地址。

只列出反向代理连接时使用的地址。任何从受信任地址连接的客户端都可以通过 `X-Forwarded-For` 头声称自己是另一个客户端。这对于 `uniquelocal` 等宽泛的值尤为重要：如果你本地网络中的设备也能直接访问 Trilium，请改用代理的确切地址。

> [!WARNING]
> 避免设置 `trustedReverseProxy=true`。这会使 Trilium 使用 `X-Forwarded-For` 最左侧的条目，即客户端发送的值，除非代理丢弃传入的头。代理通常会向其追加内容（例如 Nginx 的 `$proxy_add_x_forwarded_for`），因此客户端可以在每次请求中发送不同的地址，从而绕过登录失败尝试次数限制。

更多信息请参阅 [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html)。