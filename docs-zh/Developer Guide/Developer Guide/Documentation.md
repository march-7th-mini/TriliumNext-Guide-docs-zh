# 文档
Trilium 有多种类型的文档：

*   _用户指南_ 是面向用户的文档。用户可以直接在 Trilium 中按 <kbd>F1</kbd> 浏览此文档。
*   _开发者指南_ 是一组 Markdown 文档，向开发者展示 Trilium 的内部机制。
*   _发行说明_ 包含每个已发布或即将发布版本的变更日志。CI 在发布版本时会自动使用发行说明。
*   _脚本 API_ 是自动生成的前端和后端脚本 API 文档。

## 文档的位置

所有文档都存储在 [Trilium](https://github.com/TriliumNext/Trilium) 仓库中：

*   `docs/Developer Guide` 包含 Markdown 文档，可以在外部（使用 Markdown 编辑器）或内部（使用 Trilium）进行修改。
*   `docs/Release Notes` 同样以 Markdown 格式存储，可以自由编辑。
*   _脚本 API_ 是自动生成的，**不会**提交到仓库中。它构建到被 gitignore 忽略的 `site/` 目录中，并发布到 [docs.triliumnotes.org](https://docs.triliumnotes.org/)；请参阅下方的[更新脚本 API](#updating-the-script-api)。
*   `docs/User Guide` 同样包含 Markdown 文档，以及一个描述笔记树的 `!!!meta.json` 文件（笔记 ID、分享别名、图标、附件）。
    *   由此生成 `apps/server/src/assets/doc_notes/en/User Guide`（应用内帮助渲染的 HTML）和 `apps/standalone/src/assets/help_meta.json`。这些生成的文件绝不能手动编辑。
    *   Markdown 可以手动编辑，只要之后通过运行 `pnpm edit-docs:sync-docs`（见下文）刷新生成的文件即可。

笔记树与目录之间的映射关系列在仓库根目录的 `edit-docs-config.yaml` 中。

## 编辑文档

有两种修改文档的方式：

*   使用 Trilium 的特殊模式。
*   手动编辑文件。

### 使用 `edit-docs` 应用

要使用 Trilium 编辑文档，请通过<a class="reference-link" href="Environment%20Setup.md">环境搭建</a>设置一个可用的开发环境，然后运行以下命令：`pnpm edit-docs:edit-docs`。

工作原理：

*   启动时，`docs/` 中的文档会从 Markdown 导入到内存会话中（数据库的初始化已由应用程序处理）。
*   每次修改后会在 10 秒后触发从内存中的 Trilium 会话导出回 Markdown，包括元文件，以及应用内帮助使用的 HTML 和元文件。

### 手动编辑

小型修改可以直接使用 Markdown 编辑器或 VS Code 等进行。对于用户指南，之后运行 `pnpm edit-docs:sync-docs`：它会执行与 `edit-docs` 应用相同的导入和导出，但不打开窗口，因此 Markdown 会以相同方式规范化，应用内帮助也会重新生成。

进行手动修改时，请记住：

*   图片作为 Trilium 附件处理，存储在元文件中，因此不能简单地将图片放入目录中。
*   文件或目录结构由元文件描述。元文件中未描述的文件会导致导入失败，元文件中描述但磁盘上缺失的文件也会导致导入失败。
*   `.claude/skills` 中的 `writing-documentation` 技能提供了一个 `docs.mjs` 脚本，用于处理这些情况（创建页面、注册图片、重命名、移动或删除页面），并审计文档中的损坏链接、缺失图片和不一致的元数据。

### 审查并提交更改

由于文档使用 Git 进行跟踪，在进行手动或自动修改后（在 `edit-docs` 应用中进行修改后至少等待 10 秒），更改会反映在 Git 中。

请务必分析每个修改过的文件并报告可能的问题。

需要考虑的重要方面：

*   Trilium 的导入/导出机制并不完美，因此在下一个导入/导出/导入周期中可能会引入一些空白字符。通常按原样提交更改是安全的。
*   由于我们导入 Markdown、编辑 HTML 然后再将 HTML 导出回 Markdown，可能会出现一些格式无法正确保留的边缘情况。请尝试识别此类情况并报告，以便修复（这也会让用户受益）。

## 自动化

文档通过 `apps/build-docs` 构建：

1.  清空输出目录。
2.  构建用户指南和开发者指南。
    1.  仓库中的文档被归档并导入到内存实例中。
    2.  使用共享主题导出文档。
3.  API 文档（内部和 ETAPI）通过 Redocly 静态渲染。
4.  脚本 API 通过 `typedoc` 生成。

`deploy-docs` 工作流触发文档构建并将其上传到 CloudFlare Pages。

## 更新脚本 API

如前所述，脚本 API 无法手动编辑，因为它是使用 TypeDoc 自动生成的。

脚本 API 作为 `pnpm docs:build` 的一部分自动重新生成——其输出进入被 gitignore 忽略的 `site/script-api/{backend,frontend,electron}` 目录，并由 `deploy-docs` 工作流发布，因此无需提交任何内容。要在本地预览更改，请运行 `pnpm docs:build` 并检查 `site/` 下的输出。

请注意，为了模拟脚本所处的环境，一些虚假的源文件（即仅用于文档目的）被用作文档的入口点。请在 `apps/build-docs/src` 中查找 `backend_script_entrypoint` 和 `frontend_script_entrypoint`。

## 本地构建

在 Git 根目录中：

*   运行 `pnpm docs:build`。构建好的文档将位于 Git 根目录的 `site` 中。
*   如需同时运行 Web 服务器进行测试，请运行 `pnpm docs:preview`（这不会构建文档），然后导航到 `localhost:9000`。