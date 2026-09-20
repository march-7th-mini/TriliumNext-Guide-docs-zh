# 环境搭建
## Node.js

使用仓库根目录 `.nvmrc` 中固定的 Node.js 版本。使用 [nvm](https://github.com/nvm-sh/nvm) 时，在仓库内运行 `nvm install` 即可安装并激活该版本。

## 设置 `pnpm`

Trilium 使用 `pnpm` 包管理器，以便更好地管理其 monorepo 结构。与 Node.js 默认自带的 `npm` 不同，`pnpm` 需要单独安装。期望的版本是根 `package.json` 中的 `packageManager` 字段；同一主版本中更新的发行版也可以使用，因为 `pnpm-workspace.yaml` 中的 `pmOnFail: ignore` 会容忍这种差异。

使用 `npm` 安装：

```
npm install -g pnpm
```

pnpm 12 是一个原生可执行文件，其安装脚本会将其链接到位，因此该命令需要允许生命周期脚本（npm 的默认行为）。在 nvm 等版本管理器下，全局包属于某一个 Node.js 版本，因此切换到另一个版本后需要重新运行该命令。[独立安装程序](https://pnpm.io/installation) 是一种不依赖 Node.js 版本的替代方案。

之后，在新终端中运行 `pnpm` 以检查其是否正常工作。

> [!WARNING]
> `corepack enable` 不再是获取 `pnpm` 的推荐方式。只有 Corepack 0.34.5 或更新版本（从 Node.js 24.12 起捆绑）才能启动原生 pnpm 12，而 Node.js 25 已完全不再附带 Corepack。较旧的 Corepack 会失败并报错 `Cannot find module '…/corepack/v1/pnpm/12.x.y/bin/pnpm.cjs'`，并且它写入的 `~/.cache/node/corepack/v1/pnpm/12.x.y` 目录会导致较新的 Corepack 以同样方式失败，因此也要删除该目录。

与 `npm` 相比的一些差异，快速提示如下：

*   通常我们用 `pnpm run` 代替 `npm run`。
*   我们用 `pnpm exec` 代替 `npx`。

## 安装依赖

在 `Trilium` 仓库的顶层运行 `pnpm i` 以安装依赖。

> [!NOTE]
> 项目中的依赖会定期保持更新。通常，在 main 分支上每次 `git pull` 之后执行 `pnpm i` 是一个好习惯。

## IDE

我们推荐用于 Trilium 开发的 IDE 是 Visual Studio Code（如果你在寻找完全开源的替代方案，则是 VSCodium）。

默认情况下，我们包含了一些建议的扩展，在 VS Code 中打开仓库时应该会出现。大多数扩展用于集成我们使用的各种技术，例如用于测试的 Playwright 和 Vitest，或用于 <a class="reference-link" href="Concepts/Internationalisation%20%20Translations.md">国际化 / 翻译</a>。

## TypeScript

根 `package.json` **同时**声明了 `typescript`（6.x）和 `@typescript/native`（`typescript@7` 的别名）。这是有意为之——不要通过将 `typescript` 升级到 7 来“去重”它们：

*   **`typescript` 6.x 是库。** TypeScript 7 是原生 Go 移植版，其包不再导出 JS 编译器 API（`exports["."]` 只是一个版本存根）。所有执行 `require("typescript")` 的地方都需要 6.x：TypeDoc、typescript-eslint，以及——也会随产品发布给用户的——`packages/codemirror`，它在浏览器中运行真正的语言服务，用于脚本笔记的 IntelliSense。
*   **`@typescript/native` 是编译器二进制文件**，仅由 `pnpm typecheck` 背后的 `scripts/filter-tsc-output.mts` 使用。它构建整个项目图的时间大约为 6.x 的七分之一。
*   pnpm 将 `node_modules/.bin/tsc` 提供给该别名，因此命令行中直接使用 `tsc` 得到的是 **7**，而不是工具链加载的 6.x。这也使得 `.tsbuildinfo` 保持单一格式——两个主版本无法读取彼此的格式，混用会导致每次都要完整重建。

**不要切换到 `@typescript/typescript6`。** Microsoft 文档中描述的并排布局将 `typescript` 别名到该兼容垫片，以便原生编译器可以拥有 `tsc` 这个 bin 名称。它在这里并不适用，原因有两个，且只在构建时才会显现：

*   该垫片只附带五个文件，且**没有 `lib.*.d.ts`**，因此 `packages/codemirror/src/type_completion/ts_lib_files.ts` 中的 96 个 `typescript/lib/lib.*.d.ts?raw` 导入无法解析，客户端构建会失败。
*   通过在 `packages/codemirror` 下保留一个真正的 `typescript` 来绕过该问题，会导致解析分裂：`@typescript/vfs` 和 `@valtown/codemirror-ts` 被提升到根目录并遵循垫片，而 codemirror 自身的源码则遵循其嵌套副本。两条物理路径意味着 3.3 MB 的编译器会被**两次**打包进懒加载的脚本笔记 chunk 中（实测：客户端 `dist` 从 69 M 增至 72 M）。

官方布局假定 `typescript` 这个名称的唯一消费者是工具链。而本仓库还会将其打包进浏览器应用，因此普通包必须保留。