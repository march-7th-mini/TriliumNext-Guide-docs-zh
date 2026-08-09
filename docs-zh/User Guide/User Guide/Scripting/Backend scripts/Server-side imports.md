# 服务端导入

旧版 Trilium Notes 允许在后端脚本中使用 Common.js 模块导入，例如：

```
const isBetween = require('dayjs/plugin/isBetween')
api.dayjs.extend(isBetween)
```

对于较新版本，Node.js 导入**不再被官方支持**，因为我们添加了一个打包器，这使得复用依赖变得更加困难。

理论上，仍然可以通过 `npm` 或 `pnpm` 在服务器目录中手动设置 `node_modules` 来使用导入。