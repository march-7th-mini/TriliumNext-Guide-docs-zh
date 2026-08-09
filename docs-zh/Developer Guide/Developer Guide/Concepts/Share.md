# 分享
## 分享主题

分享主题代表了分享笔记功能背后的布局、样式和脚本。当前实现是对 [trilium.rocks](https://trilium.rocks/)（一个第三方分享主题）的重度改编。

*   该主题位于 `packages/share-theme`。
*   HTML 在 `src/templates` 中使用 EJS 模板定义。
*   `src/scripts` 和 `src/styles` 子目录包含主题的其余部分。

## 构建分享主题

*   在 `packages/share-theme` 中，运行 `pnpm build` 以触发构建。这将生成 `dist`，随后供服务器使用。
*   或者，使用 `pnpm dev` 来监听更改。

## 与服务器集成以实现分享功能

服务器使用分享主题中的 EJS 模板渲染模板，并托管资源。

*   在开发模式下，模板和资源直接从 `packages/share-theme/dist` 提供。
    *   对资源（脚本或样式）的修改将无需重启服务器即可生效。但是，分享主题需要先构建（参见上一节）。
    *   对模板的更改需要重启服务器，因为它们会被缓存。只需在控制台中使用 `pnpm server:start` 按回车键即可快速触发重启。
*   在生产模式下，分享主题由服务器构建脚本自动构建并复制到 `dist/share-theme`。

处理此功能的服务端路由位于 `src/share/routes.ts`。

## 导出为静态 HTML 文件

此功能也由服务器处理，但在 `src/services/export/zip/share_theme` 中。它的工作方式与正常的分享功能非常相似，但它使用 `BNote` 而不是 `SNote`（其他实体类型也是如此），以便无论笔记是否被分享都能工作。

服务器使用并渲染相同的模板，只是它们被存储在文件中而不是提供给 Web 客户端。