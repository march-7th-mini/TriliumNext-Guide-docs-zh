# 支持的语法
[GitHub 风格的 Markdown](https://github.github.com/gfm/) 是 Trilium 遵循的主要语法。

## 图片

导出时，图片通常保留为基本的 Markdown 语法，但如果图片具有自定义宽度，则会使用 HTML 语法。图表始终以 HTML 形式嵌入。

## 表格

简单表格支持 Markdown 语法。如果表格过于复杂或包含会渲染为 HTML 的元素，则表格也会以 HTML 形式渲染。

## 链接

支持标准 Markdown 链接。

Trilium 内部链接（镜像笔记标题并显示其图标）以 HTML 形式嵌入，以便在导入时保留信息。

<a class="reference-link" href="../../../Note%20Types/Text/Anchors.md">锚点</a> 同样以 HTML 形式保留，因此指向锚点的链接在笔记再次导入后仍能指向该锚点。

## 数学公式

支持行内公式和块级公式，使用 `$` 和 `$$` 语法。

## 警示框

Trilium 支持的警示框 Markdown 语法与 GitHub 使用的语法相同，如下所示：

```
> [!NOTE]
> This is a note.

> [!TIP]
> This is a tip.

> [!IMPORTANT]
> This is a very important information.

> [!CAUTION]
> This is a caution.
```

目前没有计划支持其他警示框语法，例如 `!!! note`。

## 标签页

标签页使用 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/) 的语法：每个标签页以 `=== "Title"` 行开始，其后是缩进四个空格的内容。连续的标签页构成一个标签页块，而 `===!` 会在另一个标签页块之后紧接着开始一个新的块：

```
=== "Windows"

    Run the **installer**.

=== "Linux"

    Use the package.

===! "Another block"

    This tab starts a separate tabs block.
```

标签页可以通过在标签页内容中缩进内部标签页来实现嵌套。标签页标题是纯文本，因此其格式在导出时不会保留。关于标签页块在文本笔记中的工作方式，请参阅 <a class="reference-link" href="../../../Note%20Types/Text/Content%20tabs.md">内容标签页</a>。

## 旁注块

<a class="reference-link" href="../../../Note%20Types/Text/Aside%20blocks.md">旁注块</a> 以单独成行的 `<aside>` 标签书写，标签之间的内容使用 Markdown：

```
<aside>

A **side note** at the right of the text.

</aside>
```

不带属性的 `<aside>` 标签的放置位置和颜色与新插入的旁注块相同：位于右侧，文字环绕其周围，灰色背景。带属性的标签仅采用属性所设置的内容。如需其他位置，请添加 `data-position` 属性，其值为以下之一：

| 值 | 位置 |
| --- | --- |
| `wrap-left` | _环绕文字_ → _左对齐_ |
| `wrap-right` | _环绕文字_ → _右对齐_，默认值 |
| `left` | _分隔文字_ → _左对齐_ |
| `center` | _分隔文字_ → _居中对齐_ |
| `right` | _分隔文字_ → _右对齐_ |

如需背景颜色，请添加 `style` 属性，例如 `style="background-color:#4d99e6"`。如果没有该属性，带属性的标签会生成透明的旁注块。

导出遵循相同的规则，并且还会保留调整大小后的旁注块的宽度。

开始标签后的空行是必需的。如果没有空行，内容将被读取为纯文本而非 Markdown，并且旁注块会占据笔记的整个宽度。

## Wiki 链接

v0.96.0 中增加了对 Wiki 链接的基本支持：

*   `[[foo/bar]]` 将在 `foo` 目录中查找 `bar.md` 文件，并将其转换为内部链接。
*   `![[foo/baz.png]]` 将在 `foo` 目录中查找 `baz.png` 文件，并将其转换为图片。

此功能仅支持导入，这意味着它会将 Wiki 链接转换为 Trilium 兼容的语法，但不会将 Trilium Notes 导出为使用此语法的 Markdown 文件。

> [!IMPORTANT]
> Wiki 链接中的页面路径是相对于 _导入根目录_ 解析的，而不是相对于笔记的当前目录。这是为了与使用 Wiki 链接的其他平台（如 SilverBullet）保持一致。
> 
> 导入的根路径按如下方式确定：
> 
> *   如果归档根级别只有一个目录，则该目录被视为根目录。
> *   如果根级别有多个文件和目录，则归档根目录（包含所有这些项目）被视为根目录。

## 高亮

背景高亮支持两种方式：

*   Markdown `==` 扩展，其他基于 Markdown 的应用程序（如 Obsidian）也支持该扩展：
    
    ```
    ==highlighted==
    ```
*   Trilium 支持的高亮规范 HTML 表示形式：
    
    ```html
    <span style="background-color:hsl(0,0%,100%);">Highlighted</span>
    ```

当使用黄色高亮时，导入/导出优先使用 `==` 语法，否则使用规范的 HTML 表示形式。