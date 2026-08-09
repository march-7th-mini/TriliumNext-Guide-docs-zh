# 架构决策记录
## 🚀 未来里程碑

*   [移动端](https://github.com/TriliumNext/Trilium/issues/7447)
*   [多用户](https://github.com/TriliumNext/Trilium/issues/4956)

## 2025年8月 - 至今：将客户端移植到 React

- [x] [类型化小组件](https://github.com/TriliumNext/Trilium/pull/7044)
- [x] [集合](https://github.com/TriliumNext/Trilium/pull/6837)
- [x] [各种小组件](https://github.com/TriliumNext/Trilium/pull/6830)
- [x] [浮动按钮](https://github.com/TriliumNext/Trilium/pull/6811)
- [x] [设置](https://github.com/TriliumNext/Trilium/pull/6660)

## 2025年8月 - 弃用 NX

我们决定弃用 NX 单体仓库工具，原因如下：

*   缓存存在各种问题，尤其是在更新 NX 依赖项后，需要定期执行 `nx reset` 才能解决。
*   由于 NX 守护进程（包括关闭 IDE 后它仍在后台运行的问题），导致内存和 CPU 消耗出现各种问题。
*   在 Windows 上，几乎每次构建时都会出现一次卡顿。
*   为了实现我们的需求，需要进行各种 hack（特别是对于构建产物，因为 NX 有时会出于某些任意原因不复制 `.gitignore` 中的资源，需要打补丁，这使得跨更新维护变得困难）。

因此，我们决定切换到……什么都不用。为什么？

*   `pnpm`（我们已经在使用）通过其自身的工作区功能即可满足单体仓库的基本需求。
*   我们的客户端解决方案 Vite 已经支持无需构建产物即可在项目间进行导航。这使得构建过程稍快（尤其是冷启动），但内存消耗会稍高一些。
*   服务端的 ESBuild 似乎也能毫无问题地跨项目工作。

除此之外：

*   在开发模式下，服务器现在直接使用 `tsx` 运行，而不是先构建再运行。这意味着运行速度会快得多。
*   我们回归到一种架构，其中 `server` 和 `desktop` 各自托管自己的 Vite 实例作为中间件。这意味着不再有 `client:dev`，也不需要处理单独的端口。
    *   这使得在开发模式下可以轻松地在移动端进行测试，因为只需访问一个端口。
    *   缺点是 Vite 启动时，初始启动时间会更长。不过，它仍然比过去稍快一些。
*   不再需要复制资源，这也应该能提高性能。
*   不再需要处理 `better-sqlite3` 的原生依赖问题，该问题曾在服务器和桌面端运行时导致令人头疼的版本不匹配。我们（希望）已经找到了一个无需用户干预的永久解决方案。
*   我们制定了一个不错的解决方案，以便在 NixOS 上更轻松地开发桌面应用程序。
*   桌面版也恢复了在发生更改时自动刷新客户端的能力，包括 React 组件的实时更改。

作为开发者的迁移步骤：

1.  在 VS Code 中，卸载 NX Console，除非你计划将其用于其他项目。
2.  删除项目级别的 `.nx` 目录。
3.  理想情况下，清理项目中所有的 `node_modules`（请注意，不仅仅是顶层的，还包括 `apps/client`、`apps/server`、`apps/desktop` 等中的）。
4.  运行 `pnpm i` 来设置新的依赖项并完成安装。
5.  现在，你不再需要运行 `nx run server:serve`，只需在 `apps/server` 目录下运行 `pnpm dev`，或者在根目录下运行 `pnpm server:start` 即可。
6.  首次启动服务器时，由于需要重建依赖项，屏幕上出现内容的时间会比平时稍长。这些依赖项之后会被缓存，因此后续运行会更好。如果最终出现白屏，请多次刷新页面，直到正确显示为止。

## 2025年4月：基于 NX 的单体仓库

*   目标：将应用程序从一种混合结构（客户端是服务器内的一个子文件夹，其他依赖项如 <a class="reference-link" href="../Dependencies/CKEditor.md">CKEditor</a> 分散在各个仓库中）重组为由 NX 驱动的单体仓库。
*   [初步讨论](https://github.com/TriliumNext/Trilium/issues/4941)
*   [相关 PR](https://github.com/TriliumNext/Notes/pull/1773)

## 2024年12月：前端转换为 TypeScript

*   [GitHub 上的相关 PR](https://github.com/TriliumNext/Notes/pulls?q=is%3Apr+is%3Aclosed+%22Port+frontend+to+TypeScript%22)

## 2024年4月：后端转换为 TypeScript

*   [GitHub 上的相关 PR](https://github.com/TriliumNext/Notes/pulls?q=is%3Apr+%22convert+backend+to+typescript%22)