# Preact
自 v0.101.0 版本起，Trilium 集成了 Preact 用于前端脚本编写，并支持 JSX。

Preact 可用于以下场景：

*   <a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>，使用 JSX 代码笔记替代 HTML 笔记。
*   <a class="reference-link" href="Custom%20Widgets.md">自定义组件</a>，使用 JSX 替代旧的基于 jQuery 的机制。

要开始使用，第一步是在代码语言列表中启用 JSX。前往 选项 → 代码笔记 并勾选“JSX”语言。之后，请参阅 <a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a> 或 <a class="reference-link" href="Custom%20Widgets.md">自定义组件</a> 的文档，这两处都将包含如何使用新的 Preact 集成的章节。

> [!IMPORTANT]
> 本文档假设您已具备 React 或 Preact 的相关知识。作为入门，您可以参考 [FreeCodeCamp 前端开发库课程](https://www.freecodecamp.org/learn/front-end-development-libraries-v9/) 或 [Preact 教程](https://preactjs.com/tutorial/)。

## 导入/导出

在将 Preact 与 JSX 结合使用时，有一种特殊的语法可以提供类似 ES 的导入功能。这种 `import` 语法为更直观的编程方式开辟了道路，无需使用全局对象，并为未来可能引入的更好的自动补全支持铺平了道路。

### API 导入

不再使用：

```jsx
api.showMessage("Hello");
```

JSX 版本如下所示：

```jsx
import { showMessage } from "trilium:api";
showMessage("hello");
```

### Preact API 导入（钩子、组件）

有一个新的 <a class="reference-link" href="../Script%20API.md">脚本 API</a> 专门用于 Preact，它提供了 Trilium 内部也使用的共享组件以及钩子等。

```jsx
import { useState } from "trilium:preact";
const [ myState, setMyState ] = useState("Hi");
```

### 导出

JSX 笔记可以导出一个组件，用于 <a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a> 或 <a class="reference-link" href="Preact/Component%20libraries.md">组件库</a>：

```jsx
export default function() {
    return (
        <>
            <p>Hello world.</p>
        </>
    );
}
```

### 导入/导出并非必需

这些导入是语法糖，旨在替代 `api` 全局对象的使用（参见 <a class="reference-link" href="../Script%20API.md">脚本 API</a>）。

> [!NOTE]
> `import` 和 `export` 语法仅适用于 JSX 笔记。标准/jQuery 代码笔记仍需要使用 `api` 全局对象和 `module.exports`。

## 底层原理

与 JavaScript 不同，JSX 需要预处理才能转换为 JavaScript（就像 TypeScript 一样）。为此，Trilium 使用 [Sucrase](https://github.com/alangpierce/sucrase)，这是一个 JavaScript 库，可将 JSX 处理为纯 JavaScript。该处理在每次运行脚本时都会执行（对于小组件，每次程序启动时都会执行）。如果您发现因编译时间过长而导致性能下降，请考虑向我们[报告问题](../../Troubleshooting/Reporting%20issues.md)。