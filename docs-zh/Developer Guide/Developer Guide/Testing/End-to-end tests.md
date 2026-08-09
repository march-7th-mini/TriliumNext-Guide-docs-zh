# 端到端测试

**服务器端 E2E：**

*   测试整个 ETAPI。
*   测试 WebSocket 功能。

**桌面端 E2E：**

*   使用 Playwright 与 Electron。
*   测试一些基本功能，例如创建新文档。

共享的 E2E 测试位于 `packages/trilium-e2e/`。服务器特定测试位于 `apps/server/e2e/`，桌面端测试位于 `apps/desktop/e2e/`。

通过以下命令运行 E2E 测试：

*   `pnpm --filter server e2e`（服务器）
*   `pnpm --filter standalone e2e`（独立版）
*   `pnpm --filter desktop e2e`（桌面版/Electron）

## 首次运行

在启动 Playwright 之前，需要先在本地安装它：

```
pnpm playwright install
```

## 启动集成测试服务器

只需在某个 e2e 项目中运行 `pnpm e2e` 即可。

集成服务器未启用身份验证，以避免登录问题。

## 启动交互式测试运行器

启动集成测试服务器后，要在终端中运行 Playwright UI，请运行：

```
pnpm playwright test --ui
```

也可以改为运行交互式代码生成器：

```
pnpm playwright codegen
```