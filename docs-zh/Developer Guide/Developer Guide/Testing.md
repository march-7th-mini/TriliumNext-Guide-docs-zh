# 测试
### 测试组织

**并行测试**（可同时运行）：

*   客户端测试
*   包测试
*   E2E 测试（隔离数据库）

**顺序测试**（共享资源）：

*   服务器测试（共享数据库）
*   CKEditor 插件测试

### 测试框架

*   **Vitest** - 单元测试和集成测试
*   **Playwright** - E2E 测试
*   **Happy-DOM** - DOM 测试环境

## 测试位置

```
apps/
├── server/
│   └── src/**/*.spec.ts       # 服务器测试
├── client/
│   └── src/**/*.spec.ts       # 客户端测试
├── server/
│   └── e2e/**/*.spec.ts       # 服务器特定的 E2E 测试
└── desktop/
    └── e2e/**/*.spec.ts       # 桌面端 E2E 测试
packages/
└── trilium-e2e/
    └── src/**/*.spec.ts       # 共享的 E2E 测试
```

## 运行测试

在项目根目录：

```
pnpm test:all          # 所有测试
pnpm test:parallel     # 快速的并行测试
pnpm test:sequential   # 仅顺序测试
```

## 单元测试和集成测试

使用 `vitest`，对客户端和服务器都进行了一些单元测试和集成测试。

这些测试可以通过在源文件所在目录中查找相应的 `.spec.ts` 文件来找到。

<table>
    <tbody>
        <tr>
            <td><p>要运行服务器端测试：</p><pre><code class="language-text-x-trilium-auto">npm run server:test</code></pre><p>要查看服务器的代码覆盖率：</p><pre><code class="language-text-x-trilium-auto">npm run server:coverage</code></pre><p>之后，可以在 <code>/coverage/index.html</code> 中找到一份友好的 HTML 报告。</p></td>
            <td><p>要运行客户端测试：</p><pre><code class="language-text-x-trilium-auto">npm run client:test</code></pre><p>要查看客户端的代码覆盖率：</p><pre><code class="language-text-x-trilium-auto">npm run client:coverage</code></pre><p>之后，可以在 <code>/src/public/app/coverage/index.html</code> 中找到一份友好的 HTML 报告。</p></td>
        </tr>
    </tbody>
</table>

要同时运行客户端和服务器端测试：

```
npm run test
```

请注意，某些集成测试依赖于内存数据库才能正常运行。

### 文本编辑器的浏览器模式测试

`packages/ckeditor5` 通过 `@vitest/browser-webdriverio` 在真实的无头 Chrome 中运行其测试，因为编辑器需要真实的 DOM 和真实的选区处理。默认情况下，webdriverio 会下载 Chrome for Testing 构建版本和匹配的 chromedriver，这在普通机器上会自动进行，无需额外设置。

在那些下载的二进制文件无法运行的地方——NixOS 就是一个典型例子，因为它们动态链接了存储路径中不提供的库，并且会因缺少 `libxcb.so.1` 而崩溃——可以将测试套件指向系统浏览器和驱动程序：

```
CHROME_BIN=/path/to/chromium CHROMEDRIVER_PATH=/path/to/chromedriver pnpm --filter @triliumnext/ckeditor5 test
```

`CHROMEDRIVER_PATH` 是 webdriverio 自己的变量；`CHROME_BIN` 由包的 `vitest.config.ts` 读取并作为 capability 传递，这也会阻止 webdriverio 下载浏览器。这两个版本必须匹配，至少在主要版本号上要一致。

Nix 开发环境（`nix develop`）会从 `pkgs.chromium` 和 `pkgs.chromedriver` 设置这两个变量，因此在其中测试可以原样运行。

### 服务器的 REST API 测试

API 测试通过 `vitest` 和 `supertest` 处理，以初始化 Express 服务器并运行断言，而无需向服务器发出实际请求。

一个重要方面是我们可以访问 Express `app`，这允许进行有趣的断言，例如检查服务器状态、注册调试中间件等。

一个例子是 `src/share/routes.spec.ts`，或者 `apps/server/spec/etapi` 中的 ETAPI 测试。

这些集成测试与单元测试一起运行。

## 端到端测试

参见 <a class="reference-link" href="Testing/End-to-end%20tests.md">端到端测试</a>。