# 环境设置
## 设置 `pnpm`

Trilium 使用 `pnpm` 包管理器来更好地管理其 monorepo 结构。与 Node.js 默认自带的 `npm` 不同，`pnpm` 需要手动激活。

在大多数系统上，可以通过 `corepack` 实现：

```
corepack enable
```

之后，在新终端中运行 `pnpm` 以确认其是否正常工作。在 Windows 上，如果你看到：

```
pnpm : 无法将“pnpm”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包含路径，请确保路径正确，然后重试。
```

解决方案是在具有管理员权限的终端中运行 `corepack enable`。

以下是相对于 `npm` 的一些差异的快速提示：

*   通常，我们使用 `pnpm run` 而不是 `npm run`。
*   我们使用 `pnpm exec` 而不是 `npx`。

## 安装依赖

在 `Trilium` 仓库的根目录下运行 `pnpm i` 来安装依赖。

> [!注意]
> 项目会定期更新依赖。通常，在主干分支上每次 `git pull` 之后执行 `pnpm i` 是一个好习惯。

## IDE

我们推荐使用 Visual Studio Code（或者，如果你想要一个完全开源的替代品，可以使用 VSCodium）来开发 Trilium。

默认情况下，我们包含了一些建议的扩展，这些扩展在 VS Code 中打开仓库时应该会显示。大多数扩展用于集成我们正在使用的各种技术，例如用于测试的 Playwright 和 Vitest，或者用于<a class="reference-link" href="Concepts/Internationalisation%20%20Translations.md">国际化 / 翻译</a>。