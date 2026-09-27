# 分享
## 分享主题

分享主题代表了分享笔记功能背后的布局、样式和脚本。当前实现是对 [trilium.rocks](https://trilium.rocks/) 的大量改编，后者是一个第三方分享主题。

*   主题位于 `packages/share-theme`。
*   HTML 定义在 `src/templates` 中，使用 EJS 模板。
*   `src/scripts` 和 `src/styles` 子目录存放主题的其余部分。

## 构建分享主题

*   在 `packages/share-theme` 中，运行 `pnpm build` 触发构建。这将生成 `dist`，随后由服务器使用。
*   或者，使用 `pnpm dev` 监听更改。
*   `pnpm dist` 是相同的构建，但经过压缩。它是应用构建所运行的版本，因此发布版会附带压缩后的资源，而本地开发则保留可读的版本。

这两个脚本都会先清空 `dist`，因为 esbuild 写入其中时不会移除先前构建留下的内容——否则压缩后的发布构建会与 `pnpm install` 生成的非压缩文件一起被复制。`--module=` 构建（`build-scripts`、`build-styles`）只构建一个入口点，并且有意不清空，因此不会影响另一个的输出。

## 代码所在位置

分享子系统位于 `packages/trilium-core/src/share`，以便每个携带核心的运行时都能提供它：

*   `shaca` 是 `_share` 子树的只读缓存，从原始行加载。
*   `content_renderer.ts` 将其中的一个笔记渲染为页面。
*   `handlers.ts` 以传输无关的处理程序形式保存路由：每个处理程序接收一个 `ShareRequest` 并返回一个 `ShareReply`（状态、标头、正文或重定向），不涉及任何 Express 类型。`route_paths.ts` 单独列出 URL 模式，不包含任何导入，因此路由器可以注册它们而无需加载其背后的渲染器。

各平台不同的部分通过 `ShareProvider`（`share_provider.ts`）处理：行来自哪里、EJS 模板来自哪里，以及是否允许笔记提供自己的模板。

|  | 服务器 / 桌面 | 独立版 / 移动版 |
| --- | --- | --- |
| 行 | 第二个只读的 `better-sqlite3` 连接（`apps/server/src/share/sql.ts`） | 唯一的 sqlite-wasm 连接，与其他所有路由共享 |
| 模板 | 从磁盘读取 | 通过 `?raw` 打包进构建中 |
| 笔记自己的 EJS 模板 | 在后端脚本启用时允许 | 从不——此构建没有后端脚本 |

## 与服务器集成以实现分享功能

服务器使用分享主题中的 EJS 模板渲染模板，并托管资源。

*   在开发模式下，模板和资源直接从 `packages/share-theme/dist` 提供。
    *   对资源（脚本或样式）的修改无需重启服务器即可生效。但分享主题需要先构建（见上一节）。
    *   对模板的更改需要重启服务器，因为它们被缓存。只需在 `pnpm server:start` 的控制台中按 Enter 即可快速触发重启。
*   在生产模式下，分享主题由服务器构建脚本自动构建并复制到 `dist/share-theme`。

`apps/server/src/share/routes.ts` 是核心处理程序之上的 Express 适配器，`apps/server/src/share/share_provider.ts` 注册上述提供程序。

## 与独立版（浏览器内）构建集成

`apps/standalone` 从浏览器提供相同的页面。`/share/` 请求由 Service Worker 接管，转发给拥有数据库的标签页，并由 Worker 的 `BrowserRouter`（`apps/standalone/src/lightweight/browser_routes.ts`）应答；其旁边的 `share_provider.ts` 提供行和打包的模板。浏览器之外的任何东西都无法访问这些页面——没有服务器在监听——因此这用于开发分享功能和本地阅读已发布的笔记，而非用于发布。

*   该子系统在首次 `/share/` 请求时通过动态 `import()` 加载，从而将 EJS、分享主题和语法高亮器（合计约 950 KB）排除在 Worker 的启动包之外。这仅在急切图中没有任何内容导入 `share/index.ts` 时成立，这就是它没有从 `@triliumnext/core` 桶文件重新导出的原因。
*   `ejs` 在 `vite.config.mts` 中被别名到其自己的浏览器构建：该包的 ESM 入口导入了 `node:fs` 和 `node:path`，它仅在没有传入 `includer` 时才需要这些，而渲染器总是会传入一个。
*   分享主题的资源被复制到构建中 `content_renderer.ts` 写入页面的路径（`share/assets`、`assets/v<version>/images`），以替代服务器注册的 `express.static` 路由。
*   页面由持有数据库的标签页渲染，因此必须至少打开一个应用标签页，`/share/` URL 才能解析。

## 导出为静态 HTML 文件

静态导出位于 `packages/trilium-core/src/services/export/zip/share_theme.ts`，因此服务器和独立版构建都提供它。它的工作方式与普通分享功能非常相似，但它使用 `BNote` 而不是 `SNote`（其他实体类型也是如此），以便无论笔记是否被分享都能工作。

使用相同的模板，不同之处在于渲染后的页面存储在归档中，而不是提供给 Web 客户端。主题的构建文件和内置图标字体通过 `ShareThemeExportAssets` 到达提供程序，每个平台在其 zip 导出工厂中填充它：

*   服务器从磁盘读取它们（`apps/server/src/services/export/zip/share_theme.ts`）。
*   独立版构建从 `share/assets` 获取它们，它已经在那里为分享页面复制了它们。文件名来自 `virtual:share-theme-assets` 模块，`vite.config.mts` 从 `packages/share-theme/dist` 为页面和 Worker 包生成该模块。