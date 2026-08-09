# 可信代理

如果你在[反向代理](../2.%20Reverse%20proxy.md)下运行 Trilium 服务器，将其配置为可信代理非常重要，这样应用程序才能正确识别客户端的真实 IP 地址（用于身份验证和速率限制）。

为此，只需修改<a class="reference-link" href="../../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>并设置：

```
[Network]
trustedReverseProxy=true
```

这将使用 `X-Forwarded-For` 头中最左侧的 IP。或者，也可以使用反向代理的 IP 地址或 Express.js 的快捷方式（如 `true`）：

```
loopback(127.0.0.1/8, ::1/128), linklocal(169.254.0.0/16, fe80::/10), uniquelocal(10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, fc00::/7)
```

更多信息，请参阅 [Express 代理设置](https://expressjs.com/en/guide/behind-proxies.html)。