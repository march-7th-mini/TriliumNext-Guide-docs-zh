# 语法高亮

## 定义 MIME 类型

为代码块或代码笔记支持新语言的第一步是定义 MIME 类型。前往 `packages/commons` 中的 `mime_type.ts` 文件，并添加相应的条目：

```
{ title: "ABAP (SAP)", mime: "text/x-abap", mdLanguageCode: "abap" }
```

其中 `mdLanguageCode` 是该语言在 Markdown 中的友好名称。

## Highlight.js 的语法高亮

Trilium 中的 Highlight.js 实例通过 `packages/highlightjs` 中 `syntax_highlighting.ts` 文件里定义的 MIME 类型映射来识别需要高亮的代码。

有三种可能的情况，均涉及修改 `byMimeType` 记录：

### Highlight.js 内置语言：

直接添加相应的条目：

```
"application/dart": () => import("highlight.js/lib/languages/dart"),
```

### 来自 NPM 的外部模块

1.  在 `packages/highlight.js` 中将该模块安装为依赖项
2.  导入：
    
    ```
    "application/x-cypher-query": () => import("highlightjs-cypher")
    ```
3.  如果 npm 模块相对较新且带有 TypeScript 映射，则执行此操作；如果没有，请参见最后一个选项。

### 直接集成到 Trilium 中的模块

*   允许在需要时进行小幅修改（尤其是当模块较旧时）。
*   对于缺少类型定义的模块效果很好，因为类型是直接在代码中添加的。

步骤：

1.  将语法高亮文件（[示例](https://github.com/highlightjs/highlightjs-sap-abap/blob/main/src/abap.js)）复制到 `packages/highlightjs/src/languages/[code].ts`。
2.  在文件顶部的注释中添加指向原始源代码的链接。
3.  将 `module.exports =` 替换为 `export default`。
4.  为该方法添加类型：
    
    ```
    import { HLJSApi, Language } from "highlight.js";
    
    export default function (hljs: HLJSApi): Language {
        // [...]
    }
    ```
5.  移除主高亮函数外部的任何模块加载机制或填充代码（shims）。
6.  修改 `syntax_highlighting.js` 以支持新语言：
    
    ```
    "text/x-abap": () => import("./languages/abap.js"),
    ```

## CodeMirror 的语法高亮

> [!NOTE]
> 较新版本的 Trilium 使用 CodeMirror 6，因此插件必须与此版本兼容。

### 添加 MIME 类型映射

与 Highlight.js 类似，每种 MIME 类型的映射在 `packages/codemirror` 的 `syntax_highlighting.ts` 中通过修改 `byMimeType` 记录来处理。

1.  官方模块：
    
    ```
    async () => (await import('@codemirror/lang-html')).html(),
    ```
2.  旧版模块（从 CodeMirror 5 移植而来）：
    
    ```
    "text/turtle": async () => (await import('@codemirror/legacy-modes/mode/turtle')).turtle, 
    ```
3.  集成到 Trilium 中的模块：
    
    ```
    "application/x-bat": async () => (await import("./languages/batch.js")).batch,
    ```

### 集成现有模块

*   在开头添加注释，指明原始源代码的链接。
*   某些导入可能需要更新：
    *   使用  
        `import { StreamParser, StringStream } from "@codemirror/language";`  
        替代  
        `import { StreamParser, StringStream } from "@codemirror/stream-parser";`。