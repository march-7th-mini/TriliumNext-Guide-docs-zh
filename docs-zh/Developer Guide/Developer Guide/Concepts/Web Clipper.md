# Web Clipper
Web Clipper 位于 monorepo 中的 `apps/web-clipper`。它基于 [WXT](https://wxt.dev/guide/introduction.html)，这是一个用于构建 Web 扩展的框架，可以让开发和发布变得非常容易。

## Manifest 版本

最初，Web Clipper 仅支持 Manifest v2，这使得该扩展与 Google Chrome 不兼容。[#8494](https://github.com/TriliumNext/Trilium/pull/8494) 为 Google Chrome 引入了 Manifest v3 支持，同时为 Firefox 保留了 Manifest v2。

尽管 Firefox 确实支持 Manifest v3，但我们仍然为它使用 Manifest v2，因为 WXT 开发模式在 Firefox / Manifest v3 组合下无法工作，并且有一些提到 Manifest v3 在 Firefox Mobile 上支持不佳的说法（而我们计划支持它）。

## 开发

WXT 让插件的开发变得简单，具有完整的 TypeScript 支持和实时重载。要进入开发模式：

*   运行 `pnpm --filter web-clipper dev` 进入 Chrome 的开发模式（使用 manifest v3）。
*   运行 `pnpm --filter web-clipper dev:firefox` 进入 Firefox 的开发模式（使用 manifest v2）。

这将打开一个单独的浏览器实例，扩展会自动注入其中。

> [!NOTE]
> 在 NixOS 上，相同的开发命令可以正常工作。只需确保浏览器在系统路径中可用：
> 
> ```sh
> nix-shell -p chromium
> ```

## 默认端口

默认端口是：

*   如果处于开发模式，则为 `37743`，这是 `pnpm desktop:start` 运行桌面应用的端口，因此 Clipper 的开发构建可以找到开发版桌面实例。
*   在生产环境中为 `37840`，即 Trilium 的默认端口。

## 构建

*   运行 `build`（Chrome）或 `build:firefox` 生成输出文件，输出文件将位于 `.output/[browser]`。
*   运行 `zip` 或 `zip:firefox` 生成 ZIP 文件。

## CI

`.github/workflows/web-clipper.yml` 负责 Web Clipper 的构建。每当 Web Clipper 被修改时，它都会生成 ZIP 文件并将其作为构件上传。

目前还没有自动发布到应用商店的功能。