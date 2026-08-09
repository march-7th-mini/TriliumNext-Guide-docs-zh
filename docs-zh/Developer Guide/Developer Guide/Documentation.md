# 文档

Trilium 有几种类型的文档：

*   _用户指南_ 代表面向用户的文档。用户可以直接在 Trilium 中按 <kbd>F1</kbd> 键浏览此文档。
*   _开发者指南_ 代表一组 Markdown 文档，为开发者展示 Trilium 的内部机制。
*   _发布说明_，包含每个已发布或即将发布版本的变更日志。CI 在发布版本时会自动使用发布说明。
*   _脚本 API_，这是为脚本自动生成的前端和后端 API 文档。

## 文档的位置

所有文档都存储在 [Trilium](https://github.com/TriliumNext/Trilium) 仓库中：

*   `docs/Developer Guide` 包含 Markdown 格式的文档，可以在外部（使用 Markdown 编辑器）或内部（使用 Trilium）进行修改。
*   `docs/Release Notes` 也以 Markdown 格式存储，可以自由编辑。
*   _脚本 API_ 是自动生成的，**不**提交到仓库。它被构建到 gitignored 的 `site/` 目录中，并发布到 [docs.triliumnotes.org](https://docs.triliumnotes.org/)；请参阅下面的 [更新脚本 API](#updating-the-script-api)。
*   `docs/User Guide` 也包含纯 Markdown 文档，但通常不应在外部编辑。
    *   原因是 `pnpm edit-docs:edit-docs` 功能不仅会导入/导出此文档，还会在 `src/public/app/doc_notes/en/User Guide` 中生成相应的 HTML 文档和元数据结构。
    *   理论上可以在外部编辑 Markdown 文件，然后运行 `docs:edit` 并触发更改以构建文档，但这并不是一个高效的工作流程。

## 编辑文档

有两种修改文档的方法：

*   使用 Trilium 的特殊模式。
*   手动编辑文件。

### 使用 `edit-docs` 应用

要使用 Trilium 编辑文档，请通过 <a class="reference-link" href="Environment%20Setup.md">环境设置</a> 设置一个可用的开发环境，然后运行以下命令：`pnpm edit-docs:edit-docs`。

工作原理：

*   启动时，`docs/` 中的文档会从 Markdown 导入到内存会话中（数据库的初始化已由应用程序处理）。
*   每次修改后 10 秒，将触发从内存中的 Trilium 会话导出回 Markdown，包括元文件。

### 手动编辑

除了用户指南外，通常可以直接使用 Markdown 编辑器或 VS Code 进行小幅修改。

进行手动修改时，请避免：

*   上传图片，因为图片是作为 Trilium 附件处理的，存储在元文件中。
*   以任何方式更改文件或目录结构，因为这也由元文件处理。如果尝试使用 Trilium 编辑文档时缺少文件，几乎肯定会导致启动时崩溃。

### 审查与提交更改

由于文档使用 Git 跟踪，在进行手动或自动修改（修改后至少等待 10 秒）后，更改将反映在 Git 中。

确保分析每个修改过的文件并报告可能的问题。

需要考虑的重要方面：

*   Trilium 的导入/导出机制并不完美，因此如果您使用 `docs:edit` 对文档进行了一些修改，在下一个导入/导出/导入周期中可能会混入一些空白字符。通常可以按原样提交更改。
*   由于我们导入 Markdown，编辑 HTML，然后将 HTML 导出回 Markdown，在某些边缘情况下格式可能无法正确保留。尝试识别此类情况并报告，以便修复它们（这也将使用户受益）。

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

如前所述，脚本 API 不能手动编辑，因为它是使用 TypeDoc 自动生成的。

脚本 API 会作为 `pnpm docs:build` 的一部分自动重新生成——其输出进入 gitignored 的 `site/script-api/{backend,frontend,electron}` 目录，并由 `deploy-docs` 工作流发布，因此无需提交任何内容。要在本地预览更改，请运行 `pnpm docs:build` 并检查 `site/` 下的输出。

请注意，为了模拟脚本可能拥有的环境，一些虚拟源文件（仅用于文档）被用作文档的入口点。请在 `apps/build-docs/src` 中查找 `backend_script_entrypoint` 和 `frontend_script_entrypoint`。

## 本地构建

在 Git 根目录中：

*   运行 `pnpm docs:build`。构建的文档将在 Git 根目录的 `site` 中可用。
*   要同时运行 Web 服务器进行测试，请运行 `pnpm docs:preview`（这不会构建文档）并导航到 `localhost:9000`。