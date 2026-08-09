# 在 NixOS 上

本页介绍如何配置 NixOS 中自带的 Trilium 模块。

## 环境要求

已安装 [NixOS](https://nixos.org/)。

## 配置

将以下内容添加到你的 `configuration.nix` 中：

```
services.trilium-server.enable = true;

# 默认数据目录：/var/lib/trilium
#services.trilium-server.dataDir = "/var/lib/trilium-sync-server";

# 默认绑定地址：127.0.0.1，端口 8080
#services.trilium-server.host = "0.0.0.0";
#services.trilium-server.port = 12783;
```

如需修改任何选项，请取消对应行的注释。

更多选项（包括 nginx 反向代理配置）请参阅 [NixOS 选项列表](https://search.nixos.org/options?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=trilium-server)。