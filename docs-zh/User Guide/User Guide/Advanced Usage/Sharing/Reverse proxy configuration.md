# 反向代理配置

可能你只想将 Trilium 的分享功能暴露到互联网，而让应用程序仅在本地网络或通过 VPN 访问。

为此，需要配置反向代理。

## Caddy

```
http://domain.com {
  reverse_proxy /share http://localhost:8080/share
}
```

这适用于分享功能已独立出来的较新版本；对于旧版本，还需要包含 `/assets`。[<sup>[1]</sup>](#fn2b8mg20aol8)

1.  [**<sup>^</sup>**](#fnref2b8mg20aol8)
    
    [https://github.com/orgs/TriliumNext/discussions/7341#discussioncomment-14679897](https://github.com/orgs/TriliumNext/discussions/7341#discussioncomment-14679897)