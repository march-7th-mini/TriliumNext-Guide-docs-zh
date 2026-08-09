# 应用程序中的文档引用
## 硬编码链接

硬编码链接遍布整个应用程序，要么出现在对话框中，要么作为注释出现在源代码中。

您可以通过搜索以下内容来识别这些链接：

```
https://triliumnext.github.io/Docs/Wiki/
```

## 帮助按钮

整个应用程序中有一类“？”按钮模式，它们使用 `data-help-page` 属性。每当按下这些按钮时，用户会通过在 `data-help-page` 属性前加上 wiki 根 URL 而被重定向到相应的 wiki 页面。

### 已弃用的 `help-page` 属性

由于当前 wiki 的结构与原始版本不同，例如要链接到 [https://github.com/TriliumNext/Docs/blob/main/Wiki/tree-concepts.md](https://github.com/TriliumNext/Docs/blob/main/Wiki/tree-concepts.md)，`data-help-page` 属性必须设置为 `tree-concepts.md`。

对于指向标题的链接，只需在 `.md` 后面添加标题：`tree-concepts.md#prefix`

您可以通过查找以下内容来识别这些：

*   `.attr("data-help-page"`
*   `data-help-page="`

### 更新的 `data-in-app-help` 属性

此属性不是在网络浏览器中打开，而是在应用程序中以分屏视图直接打开帮助。这是通过 `data-in-app-help` 属性处理的，其值是帮助页面的笔记 ID，不带 `_help_` 前缀。

### React

使用 `HelpButton` 组件，其用法与 `data-in-app-help` 属性相同。