# Web Clipper

Web Clipper 位于 monorepo 中的 `apps/web-clipper`。它基于 [WXT](https://wxt.dev/guide/introduction.html)，这是一个用于构建 Web 扩展的框架，可以非常轻松地进行开发和发布。

## Manifest 版本

最初 Web Clipper 仅支持 Manifest v2，这使得该扩展与 Google Chrome 不兼容。[#8494](https://github.com/TriliumNext/Trilium/pull/8494) 为 Google Chrome 引入了 Manifest v3 支持，同时为 Firefox 保留 Manifest v2。

尽管 Firefox 确实支持 Manifest v3，但我们仍然为其使用 Manifest v2，因为 WXT 开发模式在 Firefox / Manifest v3 组合下无法工作，并且有一些关于 Manifest v3 在 Firefox Mobile 上支持不佳的说法（而我们计划支持它）。

## 开发

WXT 允许轻松开发该插件，提供完整的 TypeScript 支持和实时重载。要进入开发模式：

*   运行 `pnpm --filter web-clipper dev` 进入 Chrome 的开发模式（使用 manifest v3）。
*   运行 `pnpm --filter web-clipper dev:firefox` 进入 Firefox 的开发模式（使用 manifest v2）。

这将打开一个单独的浏览器实例，扩展会自动注入其中。其配置文件保存在 `apps/web-clipper/.wxt/chrome-data` 或 `.wxt/firefox-data` 中，因此扩展的设置及其工具栏按钮在多次运行之间会保留；删除该文件夹即可使用全新的配置文件启动。

> [!NOTE]
> 在 NixOS 上，相同的开发命令可以正常工作。只需确保浏览器在系统路径中可用：
> 
> ```sh
> nix-shell -p chromium
> ```

## 默认端口

默认端口为：

*   如果处于开发模式，则为 `37743`，这是 `pnpm desktop:start` 运行桌面应用的端口，因此 Clipper 的开发构建可以找到开发版桌面实例。
*   在生产环境中为 `37840`，即 Trilium 的默认端口。

`pnpm desktop:start-prod` 和 `desktop:start-prod-no-dir` 在 `37841` 上运行桌面应用，因此 Clipper 的生产构建需要在其选项中设置该端口才能找到它们。

## 构建

*   运行 `build`（Chrome）或 `build:firefox` 生成输出文件，输出文件将位于 `.output/[browser]` 中。
*   运行 `zip` 或 `zip:firefox` 生成 ZIP 文件。`zip:firefox` 还会生成源代码 ZIP，Mozilla 的审核人员会基于它构建扩展。

源代码 ZIP 具有 monorepo 的布局：工作区文件和锁文件、`apps/web-clipper`，以及 Clipper 从 `apps/client` 导入的样式表和字体，这些列在 `wxt.config.ts` 的 `zip.includeSources` 中。任何来自 `apps/web-clipper` 之外的新导入都必须添加到该列表中。`apps/web-clipper/README.md`（告诉审核人员如何构建）会被复制到 ZIP 的根目录。

## CI

`.github/workflows/web-clipper.yml` 负责 Web Clipper 的构建。每当 Web Clipper 被修改时，它会生成 ZIP 并将其作为工件上传。它还会从源代码 ZIP 重新构建 Firefox 扩展，如果结果与常规构建不同则失败，这可以捕获 `zip.includeSources` 中缺失的文件。

## 发布

发布通过推送标签来启动。版本号是 `apps/web-clipper/package.json` 中的版本，而不是标签的版本：两个商店都只接受数字和点，并且一个版本只能提交一次。

*   **候选发布版**（`web-clipper-v1.2.0-rc1`，版本号设置为低于最终版本，例如 `1.1.90`）：Firefox 构建在 Mozilla 的非公开渠道上签名，该渠道仅对其进行签名而不列出，并创建一个 GitHub 预发布版，包含 ZIP 和已签名的 `.xpi`，可在任何 Firefox 中安装。
*   **正式发布版**（`web-clipper-v1.2.0`，版本号设置为 `1.2.0`）：创建一个包含 ZIP 的 GitHub 发布版，并将扩展提交到 Chrome Web Store 和 Firefox Add-ons，审核通过后即会发布。每个商店都是独立的任务，因此失败的一个可以重新运行，而无需再次提交到另一个。

手动运行工作流（_Actions_ → _Deploy web clipper extension_ → _Run workflow_）会通过试运行检查商店凭据，而不上传任何内容。

该工作流读取以下仓库密钥：

| 密钥 | 商店 | 值 |
| --- | --- | --- |
| `AMO_JWT_ISSUER`、`AMO_JWT_SECRET` | Firefox Add-ons | 来自开发者中心（_Tools_ → _Manage API Keys_）的 API 凭据，属于开发该附加组件的账户。 |
| `CHROME_PUBLISHER_ID` | Chrome Web Store | Chrome Web Store 开发者仪表板中显示的发布者 ID。 |
| `CHROME_SERVICE_ACCOUNT_CLIENT_EMAIL`、`CHROME_SERVICE_ACCOUNT_PRIVATE_KEY` | Chrome Web Store | 一个启用了 Chrome Web Store API 的 Google Cloud 服务账户，在 Chrome Web Store 开发者仪表板的 _Publisher_ → _Settings_ 下添加。私钥是 PEM 块，带有真实的换行符。 |

发布文本不会自动生成；在工作流创建 GitHub 发布版后，请在其上撰写发布文本。