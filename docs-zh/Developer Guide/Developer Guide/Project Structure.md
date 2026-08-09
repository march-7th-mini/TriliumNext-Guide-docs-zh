# 项目结构
随着应用程序复杂度的增加，我们决定改用基于 `pnpm` 的 monorepo。我们最初的 monorepo 实现使用了 NX，但我们已经转向纯 `pnpm` workspaces 和我们自己的构建脚本。

## 项目结构

monorepo 主要结构如下：

*   `apps`，代表可运行的入口点，如 `desktop`、`server`，以及额外的工具。
    *   `client`，代表前端，供服务器和桌面应用程序共同使用。
    *   `server`，代表应用程序的 Node.js / 服务器版本。
    *   `desktop`，代表基于 Electron 的桌面应用程序。
    *   `web-clipper`，代表浏览器扩展，用于轻松将网页剪辑到 Trilium，支持 Firefox 和 Chrome（manifest V3）。
*   `packages`，包含一个或多个 `apps` 使用的依赖项。
    *   `commons`，包含所有应用程序共享的代码。

## 使用项目

例如，要运行服务器实例：

```
pnpm server:start
```

## 运行和构建

每个应用程序都有许多任务。以下是开发过程中有用任务的不完整列表。参见 <a class="reference-link" href="Building">构建</a>。

## 管理 monorepo 中的依赖项

我们使用 [pnpm workspaces](https://pnpm.io/workspaces) 来管理项目结构。工作区配置位于项目级别的 `pnpm-workspace.yaml` 中，但通常不应修改。