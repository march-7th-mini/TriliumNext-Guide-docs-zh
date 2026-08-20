# 压缩库

该仓库包含**三个**独立的 ZIP 实现。这看起来是一个明显的整合目标，但实际上并非如此——每个实现都受限于其他实现无法满足的约束。本页面旨在记录此分析，避免重复讨论。

| 库 | 声明位置 | 用途 |
| --- | --- | --- |
| `jszip` | `packages/commons` | XLSX 容器，通过 `exceljs`；也用于 `renderSpreadsheetToCsvZip` |
| `fflate` | `apps/standalone` | 浏览器笔记 `ZipProvider`（`lightweight/zip_provider.ts`） |
| `archiver` + `yauzl` | `apps/server` | 服务器和桌面端使用的 Node `ZipProvider` |

## jszip 无法移除

`exceljs`——commons 的 XLSX 读写引擎，也是真正的运行时依赖——硬依赖 jszip 来处理 XLSX 的 ZIP 容器。`pnpm why jszip` 将其解析为 `jszip → exceljs → @triliumnext/commons`。任何读取或写入电子表格的包都会引入 jszip，无论其他方面如何变更。

`commons/src/lib/spreadsheet/render_to_csv.ts` 也直接使用 jszip。将该调用点切换到 fflate 并**不能**移除 jszip（exceljs 仍会引入它），而且还会适得其反：这会将 fflate 添加到服务器包中，而服务器包中已有 jszip，且该功能已经为 jszip 付出了代价。

## fflate 也不能替代它

fflate 是浏览器端的刻意轻量选择：约 30 KB，而 jszip 约 95 KB，在对此敏感的包中，fflate 为独立笔记 ZipProvider 提供了自定义的 CP437 文件名处理。用 jszip 替换 fflate 会增加独立包的大小，却无法移除一个本来就无法移除的依赖。

## 如果 jszip 被移除的陷阱

`packages/commons` 有意保持**浏览器纯净**——其库 `tsconfig` 不包含 `@types/node`；只有 spec 的 `tsconfig` 包含。jszip 的 `index.d.ts` 带有 `/// <reference types="node" />`，这一直在静默地为 `parse_from_xlsx.ts` 提供 `Buffer` 全局类型。

如果 jszip 离开 commons，`bytesToBase64` 中对 `Buffer` 的引用将会失效。修复方法是通过 `globalThis` 访问它，而不是重新添加 `@types/node`，因为后者会破坏浏览器纯净性的约束。