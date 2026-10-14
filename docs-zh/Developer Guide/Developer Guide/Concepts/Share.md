# 分享
## 分享主题

分享主题代表了分享笔记功能背后的布局、样式和脚本。当前实现是对 [trilium.rocks](https://trilium.rocks/) 的大量改编，后者是一个第三方分享主题。

*   主题位于 `packages/share-theme`。
*   HTML 定义在 `src/templates` 中，使用 EJS 模板。
*   `src/page` 存放笔记周围的页面部分（布局、页眉、导航树、主题切换、搜索、目录、页脚），`src/content` 存放笔记自身内容的样式和脚本（数学公式、Mermaid、链接嵌入、自适应颜色）。每个脚本导入自己的样式表，样式表与脚本同名并位于其旁边：`toc.ts` 导入 `./toc.css`。
*   `src/index.ts` 是唯一的入口点。它设置每个脚本，并导入没有对应脚本的样式表；其导入顺序就是打包后样式表的顺序。
*   构建输出 `scripts.js`、`tree.js` 和 `scripts.css`，这是分享页面加载的唯一样式表（`#shareOmitDefaultCss` 会将其丢弃）。

## 构建分享主题

分享主题没有自己的构建：客户端的 Vite 构建通过 `apps/client/vite-plugins.mts` 中的 `shareTheme()` 将其打包，独立版的构建也使用它。

*   `scripts.js` 及其分块被写入客户端的 `src/`，与应用的分块放在一起，因此主题和应用共享两者都使用的同一份副本（例如 Mermaid）。主题使用普通的 `import("mermaid")` 导入 Mermaid。
*   `scripts.css` 和 `tree.js` 单独构建，面向比应用更旧的浏览器（`chrome96`）。`scripts.css` 保持 `index.ts` 导入样式表的顺序，而应用的构建会通过将应用共享的样式表移入其分块来改变这一顺序。`tree.js` 构建为单个文件，因为页面的首次绘制需要等待它。
*   `share_theme.json` 列出了页面可以加载的文件，其中仅 Mermaid 加载的文件单独列出，用于静态导出。
*   开发服务器从源码提供 `scripts.js` 和 `tree.js`，并将 `scripts.css` 提供为空，因为 Vite 从模块注入样式。对脚本或样式的更改无需重新构建。

## 代码所在位置

分享子系统位于 `packages/trilium-core/src/share`，以便每个携带核心的运行时都能提供它：

*   `shaca` 是 `_share` 子树的只读缓存，从原始行加载。
*   `content_renderer.ts` 将其中的一个笔记渲染为页面。
*   `handlers.ts` 以传输无关的处理程序形式保存路由：每个处理程序接收一个 `ShareRequest` 并返回一个 `ShareReply`（状态、标头、正文或重定向），不涉及任何 Express 类型。`route_paths.ts` 单独列出 URL 模式，不包含导入，因此路由器可以注册它们而无需加载其背后的渲染器。

各平台不同的部分通过 `ShareProvider`（`share_provider.ts`）处理：行来自哪里、EJS 模板来自哪里，以及是否允许笔记提供自己的模板。

|  | 服务器 / 桌面 | 独立版 / 移动端 |
| --- | --- | --- |
| 行 | 第二个只读的 `better-sqlite3` 连接（`apps/server/src/share/sql.ts`） | 唯一的 sqlite-wasm 连接，与其他所有路由共享 |
| 模板 | 从磁盘读取 | 使用 `?raw` 打包进构建 |
| 笔记自己的 EJS 模板 | 启用后端脚本时允许 | 从不——此构建没有后端脚本 |

## 与服务器集成以实现分享功能

服务器使用分享主题中的 EJS 模板渲染模板，并托管资源。

*   在开发模式下，客户端的 Vite 服务器从源码提供主题的脚本（见上一节），模板从 `packages/share-theme/src/templates` 读取。
    *   对模板的更改需要重启服务器，因为它们被缓存。只需在运行 `pnpm server:start` 的控制台中按 Enter 即可快速触发重启。
*   在生产模式下，`/share/assets/` 从客户端构建的 `src/` 提供，模板被复制到 `dist/share-theme`。

`apps/server/src/share/routes.ts` 是核心处理程序之上的 Express 适配器，`apps/server/src/share/share_provider.ts` 注册上述提供程序。

## 与独立版（浏览器内）构建集成

`apps/standalone` 从浏览器提供相同的页面。`/share/` 请求由 Service Worker 认领，转发到拥有数据库的标签页，并由 Worker 的 `BrowserRouter`（`apps/standalone/src/lightweight/browser_routes.ts`）应答；其旁边的 `share_provider.ts` 提供行和打包的模板。浏览器之外的任何东西都无法访问这些页面——没有服务器在监听——因此这用于开发分享功能和本地阅读已发布的笔记，而非用于发布。

*   该子系统在首次 `/share/` 请求时通过动态 `import()` 加载，这使 EJS、分享主题和语法高亮器（合计约 950 KB）不进入 Worker 的启动包。这仅在急切图中没有任何东西导入 `share/index.ts` 时成立，这就是它没有从 `@triliumnext/core` 桶文件重新导出的原因。
*   `ejs` 在 `vite.config.mts` 中被别名到其自己的浏览器构建：该包的 ESM 入口导入 `node:fs` 和 `node:path`，只有在未传递 `includer` 时才需要它们，而渲染器总是传递一个。
*   分享主题的文件与应用的块一起位于 `src/` 中，静态主机无法从那里提供 `share/assets`，因此构建还将 `scripts.js`、`scripts.css` 和 `tree.js` 写入 `share/assets`，前两者加载 `src/` 中的同名文件。图标字体和图像被复制到 `content_renderer.ts` 写入页面的路径（`share/assets/fonts`、`assets/v<version>/images`），以替代服务器注册的 `express.static` 路由。
*   页面由持有数据库的标签页渲染，因此必须至少打开一个应用标签页，`/share/` URL 才能解析。

## 导出为静态 HTML 文件

静态导出位于 `packages/trilium-core/src/services/export/zip/share_theme.ts`，因此服务器和独立版构建都提供它。它的工作方式与普通分享功能非常相似，但它使用 `BNote` 而不是 `SNote`（其他实体类型同理），以便无论笔记是否被分享都能工作。

使用相同的模板，只是渲染后的页面存储在归档中，而不是提供给 Web 客户端。主题的构建文件和内置图标字体通过 `ShareThemeExportAssets` 到达提供程序，每个平台在其 zip 导出工厂中填充它。两者都将 `share_theme.json` 列出的文件复制到 `assets/`，仅当子树的某个笔记有图表时才复制 Mermaid 的文件（`getShareThemeExportFiles()`）：

*   服务器从客户端构建的 `src/` 读取它们（`apps/server/src/services/export/zip/share_theme.ts`），因此从开发服务器导出需要先运行 `pnpm client:build`。
*   独立版构建从 `/src/` 获取它们。其开发服务器不构建分享主题，因此导出需要生产构建。