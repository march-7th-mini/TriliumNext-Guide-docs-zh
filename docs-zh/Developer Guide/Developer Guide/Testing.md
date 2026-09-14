# 测试
### 测试组织

**并行测试**（可同时运行）：

*   客户端测试
*   包测试
*   E2E 测试（隔离数据库）

**顺序测试**（共享资源）：

*   服务端测试（共享数据库）
*   CKEditor 插件测试

### 测试框架

*   **Vitest** - 单元测试和集成测试
*   **Playwright** - E2E 测试
*   **Happy-DOM** - DOM 测试环境

## 测试位置

```
apps/
├── server/
│   └── src/**/*.spec.ts       # 服务端测试
├── client/
│   └── src/**/*.spec.ts       # 客户端测试
├── server/
│   └── e2e/**/*.spec.ts       # 服务端专用 E2E 测试
└── desktop/
    └── e2e/**/*.spec.ts       # 桌面 E2E 测试
packages/
└── trilium-e2e/
    └── src/**/*.spec.ts       # 共享 E2E 测试
```

## 运行测试

在项目根目录：

```
pnpm test:all          # 所有测试
pnpm test:parallel     # 快速并行测试
pnpm test:sequential   # 仅顺序测试
```

## 单元测试和集成测试

使用 `vitest`，为客户端和服务端都完成了一些单元测试和集成测试。

这些测试可以通过查找与源文件相同目录下的对应 `.spec.ts` 文件来找到。

<table>
    <tbody>
        <tr>
            <td><p>运行服务端测试：</p><pre><code class="language-text-x-trilium-auto">npm run server:test</code></pre><p>查看服务端代码覆盖率：</p><pre><code class="language-text-x-trilium-auto">npm run server:coverage</code></pre><p>之后，可以在 <code>/coverage/index.html</code> 中找到友好的 HTML 报告。</p></td>
            <td><p>运行客户端测试：</p><pre><code class="language-text-x-trilium-auto">npm run client:test</code></pre><p>查看客户端代码覆盖率：</p><pre><code class="language-text-x-trilium-auto">npm run client:coverage</code></pre><p>之后，可以在 <code>/src/public/app/coverage/index.html</code> 中找到友好的 HTML 报告。</p></td>
        </tr>
    </tbody>
</table>

同时运行客户端和服务端测试：

```
npm run test
```

请注意，某些集成测试依赖内存数据库才能运行。

### 文本编辑器的浏览器模式测试

`packages/ckeditor5` 通过 `@vitest/browser-playwright` 在真实的 headless Chromium 中运行其测试，因为编辑器需要真实的 DOM 和真实的选择处理。Playwright 会自行下载浏览器；在仓库根目录使用 `pnpm exec playwright install chromium` 安装一次即可。

当下载的浏览器无法运行时——NixOS 就是一个典型例子，因为它动态链接到没有任何 store 路径提供的库，并因缺少 `libxcb.so.1` 而崩溃——请将测试套件指向系统浏览器：

```
CHROME_BIN=/path/to/chromium pnpm --filter @triliumnext/ckeditor5 test
```

`CHROME_BIN` 由该包的 `vitest.config.ts` 读取，并作为 `launchOptions.executablePath` 传递给 provider，因此 Playwright 会启动该二进制文件而不是其自行下载的版本。无需提供单独的驱动程序——Playwright 直接通过 CDP 与浏览器通信。

Nix 开发 shell（`nix develop`）会从 `pkgs.chromium` 设置它，因此在其中测试可以原样运行。

### 服务端的 REST API 测试

API 测试通过 `vitest` 和 `supertest` 处理，以初始化 Express 服务器并运行断言，而无需向服务器发出实际请求。

一个重要方面是我们能够访问 Express 的 `app`，这允许进行有趣的断言，例如检查服务器状态、注册调试中间件等。

一个例子是 `src/share/routes.spec.ts`，或者 ETAPI 的 `apps/server/spec/etapi`。

这些集成测试与单元测试一起运行。

## 端到端测试

参见 <a class="reference-link" href="Testing/End-to-end%20tests.md">端到端测试</a>。