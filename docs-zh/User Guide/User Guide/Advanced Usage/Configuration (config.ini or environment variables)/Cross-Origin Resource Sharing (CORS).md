# 跨源资源共享（CORS）

默认情况下，Trilium 无法在 Web 浏览器中接受来自除 Trilium 自身以外的其他域名/源（origin）的请求。

不过，自 Trilium v0.93.0 起，可以通过环境变量或 `config.ini` 手动配置[跨源资源共享（CORS）](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)，具体如下：

| CORS 标头 | 对应的环境变量 | `config.ini` 中 `Network` 部分对应的变量选项 |
| --- | --- | --- |
| `Access-Control-Allow-Origin` | `TRILIUM_NETWORK_CORS_ALLOW_ORIGIN` | `corsAllowOrigin` |
| `Access-Control-Allow-Methods` | `TRILIUM_NETWORK_CORS_ALLOW_METHODS` | `corsAllowMethods` |
| `Access-Control-Allow-Headers` | `TRILIUM_NETWORK_CORS_ALLOW_HEADERS` | `corsAllowHeaders` |