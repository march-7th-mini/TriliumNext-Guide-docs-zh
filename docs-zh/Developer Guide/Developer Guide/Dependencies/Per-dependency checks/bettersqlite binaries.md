# bettersqlite 二进制文件
### 原生 Node 绑定

`better-sqlite3` 具有原生 Node 绑定。随着 `better-sqlite3` 的更新，以及 Electron 和 Node.js 版本的更新，这些绑定也需要更新。

请注意，Electron 和 Node.js 版本需要不同版本的这些绑定，因为 Electron 通常打包了不同版本的 Node.js。

在开发过程中，`pnpm install` 会尝试为当前 Node.js 版本构建或重用预构建的原生模块。这使得 `npm run start-server` 可以直接运行。尝试使用这些版本运行 `npm run start-electron` 通常会导致如下错误：

```
Uncaught Exception:
Error: The module '/Users/elian/Projects/Notes/node_modules/better-sqlite3/build/Release/better_sqlite3.node'
was compiled against a different Node.js version using
NODE_MODULE_VERSION 108. This version of Node.js requires
NODE_MODULE_VERSION 116. Please try re-compiling or re-installing
the module (for instance, using `npm rebuild` or `npm install`).
```

### 原生模块的处理方式

为了避免 `server` 和 `desktop` 之间的问题，`desktop` 构建会在其 `node_module` 中获取自己的 `bettersqlite3` 依赖副本。然后，该副本会自动重新构建以匹配 Electron 版本。

此重新构建过程由 `scripts/electron-rebuild.mts` 处理，该脚本会在 `pnpm install` 之后（通过 `postinstall`）自动运行。

如有需要，可以通过 `pnpm postinstall` 手动再次运行该脚本。