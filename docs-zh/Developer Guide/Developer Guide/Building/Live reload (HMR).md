# 实时重载（HMR）

Trilium 使用 Vite 的 HMR（热模块重载）机制。

## 服务器实时重载

如果使用 `pnpm server:start` 运行服务器，服务器将监视更改。对于 React 组件，它们将被热重载，无需刷新。对于其他服务，它将重新加载页面。

## 桌面端实时重载

`pnpm desktop:start` 与 `pnpm server:start` 的作用相同，对客户端更改进行热重载。桌面端的更改需要完全重新运行 `pnpm desktop:start` 命令。