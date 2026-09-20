# 分享
## 分享主题

分享主题代表了分享笔记功能背后的布局、样式和脚本。当前实现是对 [trilium.rocks](https://trilium.rocks/) 的大量改编，后者是一个第三方分享主题。

*   该主题位于 `packages/share-theme`。
*   HTML 定义在 `src/templates` 中，使用 EJS 模板。
*   `src/scripts` 和 `src/styles` 子目录存放主题的其余部分。

## 构建分享主题

*   在 `packages/share-theme` 中，运行 `pnpm build` 来触发构建。这将生成 `dist`，随后由服务器使用。
*   或者，使用 `pnpm dev` 来监视更改。
*   `pnpm dist` 是相同的构建，但经过压缩。它是应用构建所运行的版本，因此发布版本会附带压缩后的资源，而本地开发则保留可读的版本。

这两个脚本都会先清空 `dist`，因为 esbuild 在写入时不会移除之前构建留下的内容——否则压缩后的发布构建会与 `pnpm install` 生成的未压缩文件一起被复制。`--module=` 构建（`build-scripts`、`build-styles`）只构建一个入口点，并且有意不清空，因此不会影响另一个的输出。

## 与服务器集成以实现分享功能

服务器使用分享主题中的 EJS 模板渲染模板，并托管资源。

*   在开发模式下，模板和资源直接从 `packages/share-theme/dist` 提供。
    *   对资源（脚本或样式）的修改无需重启服务器即可生效。但是分享主题需要先构建（见上一节）。
    *   对模板的更改需要重启服务器，因为它们会被缓存。只需在使用 `pnpm server:start` 的控制台中按 Enter 即可快速触发重启。
*   在生产模式下，分享主题由服务器构建脚本自动构建，并复制到 `dist/share-theme`。

处理此功能的服务器路由位于 `src/share/routes.ts`。

## 导出为静态 HTML 文件

此功能也由服务器处理，但位于 `src/services/export/zip/share_theme` 中。它的工作方式与普通分享功能非常相似，但它使用 `BNote` 而不是 `SNote`（其他实体类型同理），以便无论笔记是否被分享都能正常工作。

服务器使用并渲染相同的模板，只是它们被存储在文件中，而不是提供给 Web 客户端。