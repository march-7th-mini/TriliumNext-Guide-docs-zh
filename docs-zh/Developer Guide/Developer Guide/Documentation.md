# 文档

Trilium 有多种类型的文档：

*   _用户指南_ 是面向用户的文档。用户可以直接在 Trilium 内按 <kbd>F1</kbd> 浏览此文档。
*   _开发者指南_ 是一组 Markdown 文档，向开发者展示 Trilium 的内部机制。
*   _发布说明_，包含每个已发布或即将发布版本的变更日志。发布说明由 CI 在发布版本时自动使用。
*   _脚本 API_，是自动生成的前端和后端脚本 API 文档。

## 文档的位置

所有文档都存储在 [Trilium](https://github.com/TriliumNext/Trilium) 仓库中：

*   `docs/Developer Guide` 包含 Markdown 文档，可以在外部（使用 Markdown 编辑器）或内部（使用 Trilium）进行修改。
*   `docs/Release Notes` 同样以 Markdown 格式存储，可以自由编辑。
*   部分用户指南页面是从源文件生成的，而非手工编写，其中包括前端和后端 _脚本 API_ 参考；参见下方的[生成的页面](#generated-pages)。
*   `docs/User Guide` 也包含 Markdown 文档，以及一个 `!!!meta.json` 文件，用于描述笔记树（笔记 ID、分享别名、图标、附件）。
    *   由此生成 `apps/server/src/assets/help/help_meta.json`（应用内帮助的笔记树）和 `apps/server/src/assets/help/help_content.json`（每个页面的 HTML）。这些生成的文件绝不能手工编辑。
    *   应用内帮助不存储在数据库中：启动时，Trilium 从这两个文件构建 `_help` 子树作为只读虚拟笔记，这些笔记永远不会被持久化或同步。
    *   Markdown 可以手工编辑，只要之后通过运行 `pnpm edit-docs:sync-docs`（见下文）刷新生成的文件即可。

笔记树与目录之间的映射关系列在仓库根目录的 `edit-docs-config.yaml` 中。

## 编辑文档

有两种方式可以修改文档：

*   使用 Trilium 的特殊模式。
*   手动编辑文件。

### 使用 `edit-docs` 应用

要使用 Trilium 编辑文档，请通过 <a class="reference-link" href="Environment%20Setup.md">环境搭建</a> 设置工作开发环境，并运行以下命令：`pnpm edit-docs:edit-docs`。

工作原理：

*   启动时，`docs/` 中的文档从 Markdown 导入到内存会话中（数据库的初始化已由应用程序处理）。
*   每次修改会在 10 秒后触发从内存中的 Trilium 会话导出回 Markdown，包括元文件，以及应用内帮助所使用的两个文件。

### 手动编辑

小的修改可以直接使用 Markdown 编辑器或 VS Code 等进行。对于用户指南，之后运行 `pnpm edit-docs:sync-docs`：它执行与 `edit-docs` 应用相同的导入和导出，但不打开窗口，因此 Markdown 会以相同方式规范化，应用内帮助也会重新生成。

进行手动修改时，请记住：

*   图片作为 Trilium 附件处理，存储在元文件中，因此不能简单地将图片拖放到目录中。
*   文件或目录结构由元文件描述。未在元文件中描述的文件会导致导入失败，已描述但磁盘上缺失的文件同样如此。
*   `.claude/skills` 中的 `writing-documentation` 技能提供了一个 `docs.mjs` 脚本，用于处理这些情况（创建页面、注册图片、重命名、移动或删除页面），并审计文档中的失效链接、缺失图片和不一致的元数据。

### 审查并提交更改

由于文档使用 Git 进行跟踪，在进行手动或自动修改后（在 `edit-docs` 应用中修改后至少等待 10 秒），更改将反映在 Git 中。

确保分析每个修改的文件并报告可能的问题。

需要考虑的重要方面：

*   Trilium 的导入/导出机制并不完美，因此在下一个导入/导出/导入周期中可能会引入一些空白字符变化。通常可以按原样提交更改。
*   由于我们导入 Markdown、编辑 HTML 然后再将 HTML 导出回 Markdown，可能存在一些格式无法正确保留的边缘情况。尝试识别这些情况并报告，以便修复（这也会惠及用户）。

## 自动化

文档通过 `apps/build-docs` 构建：

1.  清空输出目录。
2.  构建用户指南和开发者指南。
    1.  仓库中的文档被归档并导入到内存实例中。
    2.  使用共享主题导出文档。

`deploy-docs` 工作流触发文档构建并将其上传到 CloudFlare Pages。

## 生成的页面

REST API 参考（ETAPI 和内部 API）、Electron API 参考以及前端和后端脚本 API 参考都是用户指南页面，其 Markdown 从源文件生成，因此它们同时出现在应用内帮助和网站上。`edit-docs-config.yaml` 为每个文档树列出了它们：

*   `openApiPages` 通过 `apps/edit-docs/src/openapi_markdown.ts` 渲染 OpenAPI 文档（`apps/server/src/assets/etapi.openapi.yaml`、`apps/server/internal.openapi.yaml`）。
*   `typeDocPages` 通过 `apps/edit-docs/src/typedoc_markdown.ts` 渲染 TypeDoc 所读取的 TypeScript 模块的导出。Electron API 页面记录 `packages/commons/src/lib/electron_api_interface.ts`，从 `ElectronApi` 开始；其介绍是该模块的 `@packageDocumentation` 注释。前端 API 和后端 API 页面记录 `packages/commons/src/lib/script_api.ts`，即脚本笔记自动补全所使用的精选类型，分别从 `FrontendApi` 和 `BackendApi` 开始。带有 `root` 的页面只显示根可达的内容，因此一个模块可以容纳多个页面的类型。`stripPrefixes` 将命名前缀从页面显示的名称中去掉，因此 `ScriptBNote` 显示为 `BNote`，`ElectronWindowApi` 显示为 `WindowApi`；引用、签名和命名类型的代码片段随之调整，如果两个类型最终得到相同名称，同步将停止。带有 `skillReference` 的页面还会将其显示的内容以紧凑 TypeScript 格式（每个成员一行，位于其描述的第一句话之下，已弃用的成员省略）写入该文件。前端 API 和后端 API 页面将 `frontend_scripting_api.md` 和 `backend_scripting_api.md` 写入 `packages/trilium-core/src/assets/llm/skills/` 下，`load_skill` 会将其追加到手写的脚本速查表中，以便 AI 拥有每个成员的精确签名。当参考列出的成员与 `script_api.ts` 声明的不一致时，`skills.spec.ts` 中的规范测试会失败。

`pnpm edit-docs:sync-docs` 和 `pnpm edit-docs:edit-docs` 都会在导入文档之前重新生成这些页面，因此直接对它们所做的任何编辑都会被覆盖。要更改某个页面，请编辑其源文件（OpenAPI 文档或 TypeScript 模块的注释），然后运行 `pnpm edit-docs:sync-docs`，并将重新生成的页面连同帮助文件一起提交。

## 本地构建

在 Git 根目录中：

*   运行 `pnpm docs:build`。构建的文档将位于 Git 根目录的 `site` 中。
*   如需同时运行 Web 服务器进行测试，请运行 `pnpm docs:preview`（这不会构建文档）并导航到 `localhost:9000`。