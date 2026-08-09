# 自定义分享模板
> [!NOTE]
> 创建分享模板这一主题属于高级内容，需要具备 JavaScript/EJS 知识。
> 
> 默认的分享模板应能满足大多数常规用途。

若要对共享页面的 HTML 结构进行完全控制——超越自定义 CSS、JS 或 HTML 片段所能实现的范围——您可以使用 `~shareTemplate` 关系完全替换页面模板。

操作步骤如下：

1.  创建一个语言为 _嵌入式 JavaScript_ (EJS) 的<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记。
2.  对于要应用新创建模板的共享笔记，请应用指向步骤 (1) 中所创建笔记的 `~shareTemplate` 关系。利用<a class="reference-link" href="../Attributes/Attribute%20Inheritance.md">属性继承</a>可将其应用于多个共享笔记。

需要注意两个重要的限制条件：

*   由于 EJS 模板会执行任意的服务器端 JavaScript，`~shareTemplate` 仅在启用后端脚本时生效。如果后端脚本被禁用（请参阅<a class="reference-link" href="../../Scripting/Security.md">安全</a>），该关系将被忽略，并使用默认模板。出于同样的原因，**请仅应用来自您信任笔记的模板**。
*   模板笔记必须是共享子树的一部分（就像 `~shareCss`、`~shareJs` 一样），以便其能被加载。为防止其显示在导航中，请对其应用 `#shareHiddenFromTree`。

## 分享模板的内容

在创建新的分享模板时，请参考[原始模板](https://github.com/TriliumNext/Notes/blob/develop/packages/share-theme/src/templates/page.ejs)。

## 可用变量

您的模板将使用一个上下文对象进行渲染，该对象公开了笔记及其渲染环境。最有用的值如下：

| 变量 | 描述 |
| --- | --- |
| `note` | 正在渲染的笔记。使用它来读取属性（`note.getLabelValue(...)`）、`note.title`、子笔记等。 |
| `content` | 该笔记已渲染好的 HTML 内容，以字符串形式提供。 |
| `header` | 需要放置在此笔记文档头部的额外 HTML（某些笔记类型会用到）。 |
| `isEmpty` | 当笔记自身没有内容时为 `true`。 |
| `subRoot` | 共享子树的根，形式为 `{ note, branch }` —— 方便用于显示全站标题或徽标。 |
| `cssToLoad` / `jsToLoad` | 默认主题会注入的样式表/脚本 URL 数组（包括通过 `~shareCss` / `~shareJs` 添加的任何内容）。 |
| `faviconUrl` / `logoUrl` | 解析后的网站图标和徽标 URL。 |
| `isStatic` | 在静态 HTML 导出期间为 `true`，在实时服务器渲染时为 `false`。 |
| `t` | `i18next` 翻译函数。 |
| `utils` | 辅助工具，例如 `slugify()` 和 `stripTags()`。 |

## 错误处理

如果您的模板在渲染时抛出错误，Trilium 会记录该错误并静默回退到默认模板，因此损坏的模板绝不会导致共享页面崩溃。

## 将模板拆分为部分模板

模板可以将其他 EJS 笔记作为部分模板引入。将它们创建为模板笔记的**子笔记**（每个子笔记也必须是 `code` / `application/x-ejs` 笔记），并通过标题引用它们：

```
<%- include("header") %>

<main>
    <h1><%= note.title %></h1>
    <%- content %>
</main>

<%- include("footer") %>

```

此处 `header` 和 `footer` 是模板子笔记的标题。只有直接子笔记可以被解析，并且它们必须是 EJS 代码笔记。