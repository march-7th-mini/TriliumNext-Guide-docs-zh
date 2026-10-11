# 自定义分享模板
> [!NOTE]
> 创建分享模板这一主题被视为高级内容，需要 JavaScript/EJS 知识。
> 
> 默认分享模板应能覆盖大多数常规用途。

若要完全控制共享页面的 HTML 结构——超出自定义 CSS、JS 或 HTML 片段所能提供的范围——你可以使用 `~shareTemplate` 关系完全替换页面模板。

为此：

1.  创建一个语言为 _Embedded JavaScript_ (EJS) 的 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记。
2.  要让某个共享笔记应用新建的模板，请应用指向步骤 (1) 中所创建笔记的 `~shareTemplate` 关系。利用 <a class="reference-link" href="../Attributes/Attribute%20Inheritance.md">属性继承</a> 将其应用到多个共享笔记。

有两个需要注意的重要限制：

*   由于 EJS 模板会执行任意服务器端 JavaScript，`~shareTemplate` 仅在启用后端脚本时才会生效。如果它被禁用（参见 <a class="reference-link" href="../../Scripting/Security.md">安全</a>），该关系会被忽略，并使用默认模板。出于同样的原因，**只应用来自你信任的笔记的模板**。
*   模板笔记必须是共享子树的一部分（就像 `~shareCss`、`~shareJs` 一样）才能被加载。为防止它显示在导航中，请对其应用 `#shareHiddenFromTree`。

## 分享模板的内容

在创建新的分享模板时，请以[原始模板](https://github.com/TriliumNext/Notes/blob/develop/packages/share-theme/src/templates/page.ejs)作为参考。

## 可用变量

你的模板在渲染时会接收一个上下文对象，其中暴露了笔记及其渲染环境。最有用的值如下：

| 变量 | 描述 |
| --- | --- |
| `note` | 正在渲染的笔记。用它来读取属性（`note.getLabelValue(...)`）、`note.title`、子笔记等。 |
| `content` | 该笔记已渲染好的 HTML 内容，以字符串形式提供。 |
| `header` | 要放入此笔记文档 head 中的额外 HTML（某些笔记类型会使用）。 |
| `isEmpty` | 当笔记自身没有内容时为 `true`。 |
| `head` | 页面 `<head>` 的值：`title`（笔记标题，后跟站点标题）、`description`（`#shareDescription`）、`noIndex`（`#shareDisallowRobotIndexing`），以及包含 `url`、`domain`、`image`、`color` 和 `card` 的 `openGraph`（有图片时为 `summary_large_image`，没有时为 `summary`）。未设置对应标签的值为 `null`。`metaTags` 列出已设置值的 description、OpenGraph 和 Twitter `<meta>` 标签，每个都包含 `attribute`（`name` 或 `property`）、`key` 和 `content`。 |
| `logo` | 导航树上方的站点 logo，在窄屏幕上则位于页眉中：`href`（`#shareRootLink`，否则为站点根页面）、`image`（`~shareLogo` 图片，或 `null`）、`icon`（站点根笔记的图标类，在没有 `image` 时显示），以及图片的 `width` 和 `height`。 |
| `navigation` | 站点的导航树：其可见页面，每个页面包含 `title`、`href`、`isExternal`、`type`、`icon`、`isActive`（当前显示的页面）、`isExpanded`（该页面或其祖先之一）和 `children`。 |
| `contentClasses` | 内容元素的类：`type-<note type>`，文本和 Markdown 笔记为 `ck-content`，占据整页的笔记（如 PDF、网页视图、日历、地理地图或图片）为 `full-height`，当笔记自身没有内容时为 `no-content`。 |
| `childLinks` | 指向笔记可见子项的链接，每个都包含 `title`、`href`、`isExternal`、`type`、`icon`（其图标类）、`excerpt`（其 `#shareDescription` 或其文本开头，段落之间以换行分隔，或 `null`）和 `children`（当它没有摘要时，为其前十个可见子项，每个包含 `title`、`href`、`isExternal` 和 `icon`）。对于不是集合、文本笔记或代码笔记的笔记，对于占据整页的笔记，以及带有 `#hideChildrenOverview` 的笔记，此值为空。 |
| `childLinksLayout` | 默认模板如何布局 `childLinks`：视图类型为列表的集合使用 `list`，否则使用 `grid`。 |
| `prevNext` | 导航树中该笔记之前和之后的页面，分别为 `previous` 和 `next`，每个包含 `title` 和 `href`，或为 `null`。对于占据整页的笔记，两者均为 `null`。 |
| `language` | 页面的语言：`page` 包含应用程序语言的 `lang` 和 `dir`，`content` 包含笔记内容语言对应的值，当二者相同时为 `null`。 |
| `lastUpdated` | 笔记最后更改的时间，`iso` 用于 `<time>` 元素，`text` 使用应用程序语言，或为 `null`；对于占据整页的笔记也为 `null`。 |
| `showTitle` | 默认模板是否在内容上方显示笔记标题。始终为 `true`。 |
| `titleIcon` | 笔记的图标类；对于占据整页的笔记，默认模板会在标题旁单独一行显示它；对于任何其他笔记为 `null`。 |
| `snippets` | 每个位置的 `~shareHtml` 片段的 HTML，例如 `snippets["head:end"]`。每个位置都存在，没有片段放入时为空白。 |
| `subRoot` | 共享子树的根，形式为 `{ note, branch }`——便于设置站点级标题或 logo。 |
| `cssToLoad` / `jsToLoad` | 默认主题会注入的样式表 / 脚本 URL 数组（包括通过 `~shareCss` / `~shareJs` 添加的任何内容）。 |
| `faviconUrl` / `logoUrl` | 解析后的 favicon 和 logo URL。没有 `~shareLogo` 时，`logoUrl` 为 Trilium logo。 |
| `fontPreloads` | 要预加载的图标字体，每个包含 `href` 和 `type`（字体的媒体类型）：Boxicons，以及 logo、导航树或子页面所使用的图标包。默认模板会为每个添加 `<link rel="preload" as="font" crossorigin>`，以便图标不会只在首次绘制后才出现。 |
| `isStatic` | 在静态 HTML 导出期间为 `true`，实时服务器渲染时为 `false`。 |
| `t` | `i18next` 翻译函数。 |
| `utils` | 辅助工具，例如 `slugify()` 和 `stripTags()`。 |

## 错误处理

如果你的模板在渲染时抛出错误，Trilium 会记录该错误并静默回退到默认模板，因此损坏的模板绝不会导致共享页面无法访问。

## 将模板拆分为局部模板

一个模板可以引入其他 EJS 笔记作为局部模板。将它们创建为模板笔记的**子笔记**（每个也都是 `code` / `application/x-ejs` 笔记），并通过标题引用它们：

```
<%- include("header") %>

<main>
    <h1><%= note.title %></h1>
    <%- content %>
</main>

<%- include("footer") %>

```

这里 `header` 和 `footer` 是模板子笔记的标题。只有直接子笔记可以解析，并且它们必须是 EJS 代码笔记。