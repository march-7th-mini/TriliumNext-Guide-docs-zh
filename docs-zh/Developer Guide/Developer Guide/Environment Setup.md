# 环境设置
## 设置 `pnpm`

Trilium 使用 `pnpm` 包管理器来更好地管理其 monorepo 结构。与 Node.js 默认自带的 `npm` 不同，`pnpm` 需要手动激活。

在大多数系统上，可以通过 `corepack` 实现：

```
corepack enable
```

之后，在一个新的终端中运行 `pnpm` 以检查其是否正常工作。在 Windows 上，如果你看到：

```
pnpm : 无法将“pnpm”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包含路径，请验证路径是否正确，然后重试。
```

解决方案是在具有管理员权限的终端中运行 `corepack enable`。

以下是相较于 `npm` 的一些差异快速提示：

*   通常我们使用 `pnpm run` 而不是 `npm run`。
*   我们使用 `pnpm exec` 而不是 `npx`。

## 安装依赖

在 `Trilium` 仓库的根目录下运行 `pnpm i` 来安装依赖。

> [!注意]
> 项目会定期更新依赖。通常，在主干分支上每次 `git pull` 之后执行 `pnpm i` 是一个好习惯。

## IDE

我们推荐使用 Visual Studio Code（或者，如果你在寻找完全开源的替代品，可以使用 VSCodium）来开发 Trilium。

默认情况下，我们包含了许多建议的扩展，当你在 VS Code 中打开仓库时，这些扩展应该会显示出来。大多数扩展用于集成我们正在使用的各种技术，例如用于测试的 Playwright 和 Vitest，或者用于<a class="reference-link" href="Concepts/Internationalisation%20%20Translations.md">国际化 / 翻译</a>。

## TypeScript

根目录下的 `package.json` 声明了 **两个** `typescript`（6.x）和 `@typescript/native`（`typescript@7` 的别名）。这是有意为之——不要通过将 `typescript` 升级到 7 来“去重”它们：

*   **`typescript` 6.x 是库。** TypeScript 7 是原生 Go 移植版，其包不再导出 JS 编译器 API（`exports["."]` 只是一个版本存根）。所有执行 `require("typescript")` 的操作都需要 6.x：TypeDoc、typescript-eslint，以及——同样会提供给用户的——`packages/codemirror`，它在浏览器中运行真正的语言服务，为脚本笔记提供智能感知。
*   **`@typescript/native` 是编译器二进制文件**，仅由 `scripts/filter-tsc-output.mts` 在 `pnpm typecheck` 后面使用。它构建整个项目图的速度大约是 6.x 所需时间的七分之一。
*   pnpm 将 `node_modules/.bin/tsc` 提供给别名，因此命令行上的裸 `tsc` 是 **7**，而不是工具加载的 6.x。这也是保持 `.tsbuildinfo` 格式统一的原因——这两个主要版本无法读取彼此的格式，混合使用将导致每次都需要完全重建。

**不要切换到 `@typescript/typescript6`。** 微软记录的并排布局将 `typescript` 别名为该兼容性垫片，以便原生编译器可以拥有 `tsc` bin 名称。这不适用于此处，原因有两个，只有在构建时才会显现：

*   该垫片只包含五个文件，并且 **没有 `lib.*.d.ts`**，因此 `packages/codemirror/src/type_completion/ts_lib_files.ts` 中的 96 个 `typescript/lib/lib.*.d.ts?raw` 导入将无法解析，客户端构建将失败。
*   通过在 `packages/codemirror` 下保留一个真正的 `typescript` 来解决这个问题会分裂解析：`@typescript/vfs` 和 `@valtown/codemirror-ts` 被提升到根目录并跟随垫片，而 codemirror 自身的源码则跟随其嵌套副本。两个物理路径意味着 3.3 MB 的编译器会被 **两次** 打包到懒加载的脚本笔记块中（实测：客户端 `dist` 从 69 M → 72 M）。

官方布局假设 `typescript` 名称的唯一消费者是工具。此仓库还将其打包到浏览器应用程序中，因此必须保留普通包。