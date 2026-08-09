# Web Clipper

Web Clipper 位于 monorepo 的 `apps/web-clipper` 目录中。它基于 [WXT](https://wxt.dev/guide/introduction.html)，这是一个用于构建浏览器扩展的框架，可以非常轻松地进行开发和发布。

## Manifest 版本

最初 Web Clipper 仅支持 Manifest v2，这使得该扩展与 Google Chrome 不兼容。[#8494](https://github.com/TriliumNext/Trilium/pull/8494) 为 Google Chrome 引入了 Manifest v3 支持，同时为 Firefox 保留了 Manifest v2。

尽管 Firefox 支持 Manifest v3，我们仍然为其使用 Manifest v2，因为 WXT 开发模式不适用于 Firefox / Manifest v3 的组合，并且有一些关于 Manifest v3 在 Firefox Mobile 上支持不佳的提及（我们计划支持该平台）。

## 开发

WXT 允许轻松开发插件，支持完整的 TypeScript 和实时重载。要进入开发模式：

*   运行 `pnpm --filter web-clipper dev` 进入 Chrome 的开发模式（使用 manifest v3）。
*   运行 `pnpm --filter web-clipper dev:firefox` 进入 Firefox 的开发模式（使用 manifest v2）。

这将打开一个单独的浏览器实例，扩展会自动注入其中。

> [!NOTE]
> 在 NixOS 上，相同的开发命令也可以正常工作。只需确保浏览器在系统路径中可用：
> 
> ```sh
> nix-shell -p chromium
> ```

## 默认端口

默认端口为：

*   开发模式下为 `37742`。这使得可以使用 `pnpm desktop:start` 启动一个桌面实例来配合 Clipper 使用。
*   生产环境下为 `37840`，即 Trilium 的默认端口。

## 构建

*   运行 `build`（Chrome）或 `build:firefox` 来生成输出文件，这些文件将位于 `.output/[browser]` 目录中。
*   运行 `zip` 或 `zip:firefox` 来生成 ZIP 文件。

## CI

`.github/workflows/web-clipper.yml` 负责处理 web clipper 的构建。每当 web clipper 被修改时，它都会生成 ZIP 文件并将其作为工件上传。

目前还没有自动发布到应用商店的功能。