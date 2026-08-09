# 运行开发构建

首先，请遵循<a class="reference-link" href="../Environment%20Setup.md">环境设置</a>。

## 客户端

尽管客户端被描述为一个应用，但它并不打算单独运行。请参阅有关服务器的文档。

## 服务器

*   要以开发模式运行服务器，请运行 `server:start`。开发端口为 `8080`。
*   要以生产模式运行服务器（使用其自身的资源副本），请运行 `server:start-prod`。
*   要为 Docker 构建，请参阅<a class="reference-link" href="Docker.md">Docker</a>。

要使用自定义端口运行，请更改 `package.json` 中的 `TRILIUM_PORT` 环境变量。

## 桌面

*   要以开发模式运行，请使用 `pnpm desktop:start`。
*   要以生产模式运行，请使用 `pnpm desktop:start-prod`。

## 安全模式

安全模式默认关闭，要在 Unix shell 上临时启用它，请在环境变量设置前加上前缀：

```
pnpm cross-env TRILIUM_SAFE_MODE=1 pnpm server:start
```

## 在 NixOS 上运行

在进行开发时，从 NPM 获取的 Electron 二进制文件将与 NixOS 不兼容，导致尝试运行它时出错。但是，Trilium 在运行 `pnpm desktop:start` 时会自动处理此问题。

如果系统路径中没有 `electron`，它将尝试使用 `nix-shell` 来获取它。