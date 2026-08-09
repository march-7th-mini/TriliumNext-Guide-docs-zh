# 错误 [TransformError]：找不到软件包“@esbuild/linux-x64”，而 esbuild 需要它。
完整日志：

```
> trilium@0.91.1-beta start-server
> cross-env TRILIUM_DATA_DIR=./data TRILIUM_ENV=dev TRILIUM_SYNC_SERVER_HOST=http://tsyncserver:4000 nodemon src/main.ts

[nodemon] 3.1.9
[nodemon] 要随时重启，请输入 `rs`
[nodemon] 正在监视路径：src/**/* translations/**/*
[nodemon] 正在监视扩展名：ts,js,json
[nodemon] 正在启动 `tsx src/main.ts`

node:internal/process/promises:391
    triggerUncaughtException(err, true /* fromPromise */);
    ^
Error [TransformError]: The package "@esbuild/linux-x64" could not be found, and is needed by esbuild.

If you are installing esbuild with npm, make sure that you don't specify the
"--no-optional" or "--omit=optional" flags. The "optionalDependencies" feature
of "package.json" is used by esbuild to install the correct binary executable
for your current platform.
    at generateBinPath (/home/elian/Projects/TriliumNext/Notes/node_modules/esbuild/lib/main.js:1752:15)
    at esbuildCommandAndArgs (/home/elian/Projects/TriliumNext/Notes/node_modules/esbuild/lib/main.js:1822:33)
    at ensureServiceIsRunning (/home/elian/Projects/TriliumNext/Notes/node_modules/esbuild/lib/main.js:1979:25)
    at transform (/home/elian/Projects/TriliumNext/Notes/node_modules/esbuild/lib/main.js:1880:37)
    at file:///home/elian/Projects/TriliumNext/Notes/node_modules/tsx/dist/index-DlKgSVBb.mjs:16:2755
    at applyTransformers (file:///home/elian/Projects/TriliumNext/Notes/node_modules/tsx/dist/index-DlKgSVBb.mjs:16:1266)
    at transform (file:///home/elian/Projects/TriliumNext/Notes/node_modules/tsx/dist/index-DlKgSVBb.mjs:16:2702)
    at load (file:///home/elian/Projects/TriliumNext/Notes/node_modules/tsx/dist/esm/index.mjs?1734213798404:2:2245)
    at async nextLoad (node:internal/modules/esm/hooks:868:22)
    at async Hooks.load (node:internal/modules/esm/hooks:451:20)
```

解决方案是删除 `node_modules` 并重新安装所有依赖：

```
rm -r node_modules
pnpm install
```