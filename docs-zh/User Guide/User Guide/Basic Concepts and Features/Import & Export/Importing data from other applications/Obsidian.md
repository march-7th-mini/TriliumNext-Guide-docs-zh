# Obsidian

虽然 Obsidian 可以通过标准的 <a class="reference-link" href="../Markdown.md">Markdown</a> 导入间接获得支持，但其 vault 结构足够独特，值得拥有专门的导入通道。

## 导入流程

第一步是获取你的 Obsidian vault 的 .zip 压缩包：

1.  首先，确定你的 Obsidian vault 所在位置。最简单的方法是打开 Obsidian，右键点击左侧边栏底部的 vault 名称，然后选择 _在系统资源管理器中显示_。
2.  在系统资源管理器中，右键点击包含你的 Obsidian vault 的目录，并将其压缩为 ZIP 文件（例如，在 Windows 上，选择 _压缩为_ → _ZIP_）。

> [!TIP]
> 压缩时，你可以压缩 vault 的外部文件夹，也可以压缩 vault 的内容，因为 Trilium 会通过 `.obsidian` 目录自动确定 vault 在压缩包中的位置。

然后，在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键点击并选择 _导入到笔记_。
2.  在 _从_ 部分，选择 _Obsidian_。
3.  上传上一步获取的 ZIP 文件。

## 支持的功能

Trilium 在导入过程中会保留以下功能：

*   文件夹层级结构得以保留。
*   基本的 Markdown 格式（粗体、斜体、下划线、删除线、标题）。
*   特定的 Obsidian 格式（高亮）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Lists.md">列表</a>
*   待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>
    *   默认情况下，如果 Vault 中的非 Markdown 文件被至少一个笔记引用，则将其视为附件。
    *   否则，它们将被导入为 <a class="reference-link" href="../../../Note%20Types/File.md">文件</a> 笔记。
*   嵌入（Transclusions）被转换为 <a class="reference-link" href="../../../Note%20Types/Text/Include%20Note.md">包含笔记</a> 或 <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a>（取决于类型）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Math%20Equations.md">数学公式</a>（内联或块级）
*   <a class="reference-link" href="../../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>，并尽力恢复其语言。
*   页面之间的链接被转换为 <a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
*   标注（Callouts）被转换为 Trilium 的 [警示框](../../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md)。
    *   Obsidian 有更多类型的标注（`tldr`、`question`、`attention`），这些都被映射到 Trilium 现有的警示框类型之一（例如，Note、Tip、Important）。
    *   自定义标题会被保留，并显示为警示框顶部的粗体行，因为 Trilium 没有警示框标题的概念。
    *   可折叠的标注在导入时会展开，并且没有折叠标记。
*   由 Obsidian 的 [_Excalidraw_](https://github.com/zsviczian/obsidian-excalidraw-plugin) 社区插件创建的笔记会被转换为 <a class="reference-link" href="../../../Note%20Types/Canvas.md">画布</a>（使用相同的底层技术）。
    *   请注意，该插件引入的自定义功能将不受支持。
*   修改日期通过从 .zip 压缩包获取的信息得以保留，创建日期无法恢复，因此与修改日期保持一致。

## 属性

属性是 Obsidian 中与 <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a> 相对应的概念。两者之间的核心区别之一在于属性信息（即名称和类型）的存储位置：在 Obsidian 中，所有内容都存储在 vault 级别，并在所有笔记之间共享；而在 Trilium 中，每个页面可以有独立的提升属性，通过 <a class="reference-link" href="../../../Advanced%20Usage/Templates.md">模板</a> 或 <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a> 共享。

另一个重要的区别是，Trilium 中的提升属性始终显示，即使为空。在 Obsidian 中，这些属性只是在创建新属性时作为建议出现。

为了调和所有这些差异，属性会在笔记级别转换为 <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>。

支持以下笔记类型：

| Obsidian 类型 | Trilium |
| --- | --- |
| 文本或未定义 | 单值 `text` 标签 |
| 数字 | 单值 `number` 标签 |
| 多文本 | 多值 `text` 标签 |
| 复选框 | `boolean` 标签（`true`/`false`）。 |
| 日期 | `date` |
| 日期和时间 | `datetime` |

### 特殊属性

Obsidian 有一些保留的属性名称，在 Trilium 中也会被区别对待：

*   `tags`，其中每个标签都会变成自己的 [标签](../../../Advanced%20Usage/Attributes/Labels.md)（例如，当 `tags: [ one, two ]` 时，会生成 `#one`、`#two`）。
*   `aliases` 直接映射为单独的 `#alias` 标签。
*   `cssclasses`、`publish`、`permalink` 将被忽略。

## 限制

*   注释（`%%` 语法）会被直接剥离。
*   Obsidian 的 _bases_ 功能不会被保留。
    *   Trilium 中最接近的等价物是 <a class="reference-link" href="../../../Collections.md">集合</a>，但它们的运作方式根本不同，因为 bases 不存储特定笔记，它们更像是一个带有集合视图的 <a class="reference-link" href="../../../Note%20Types/Saved%20Search.md">已保存搜索</a>。
    *   由于 base 查询格式与 Trilium 的 <a class="reference-link" href="../../Navigation/Search.md">搜索</a> 语法差异很大，因此它们不太可能得到支持。
    *   当遇到 base 时，它会在导入时被直接忽略。
*   画布（Canvases）不会被导入。
    *   理论上它们可以映射到 <a class="reference-link" href="../../../Note%20Types/Canvas.md">画布</a> 或 <a class="reference-link" href="../../../Note%20Types/Relation%20Map.md">关系图</a>，但它们差异太大，难以调和。
*   链接
    *   指向另一个笔记中特定标题的链接仍会指向正确的笔记，但标题锚点将被丢弃。
    *   悬空链接（指向不存在的笔记）和歧义链接（在 2 个或更多笔记中具有相同的基础名称）将被转换为纯文本。