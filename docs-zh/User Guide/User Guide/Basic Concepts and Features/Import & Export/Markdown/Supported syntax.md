# 支持的语法
[GitHub 风格的 Markdown](https://github.github.com/gfm/) 是 Trilium 遵循的主要语法。

## 图片

导出时，图片通常保留在基本的 Markdown 语法中，但如果图片具有自定义宽度，则会使用 HTML 语法。图形始终以 HTML 形式嵌入。

## 表格

支持使用 Markdown 语法的简单表格。如果表格过于复杂或包含会渲染为 HTML 的元素，则表格也会以 HTML 形式渲染。

## 链接

支持标准 Markdown 链接。

Trilium 内部链接（镜像笔记标题并显示其图标）以 HTML 形式嵌入，以便在导入时保留信息。

<a class="reference-link" href="../../../Note%20Types/Text/Anchors.md">锚点</a> 也保留为 HTML，因此指向锚点的链接在笔记再次导入后仍能指向它。

## 数学公式

支持行内公式和独立公式，使用 `$` 和 `$$` 语法。

## 警示框

Trilium 支持的警示框 Markdown 语法是 GitHub 所使用的语法，如下所示：

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

目前没有支持替代警示框语法（如 `!!! note`）的计划。

## 标签页

标签页使用 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/) 的语法：每个标签页以 `=== "Title"` 行开始，其后是缩进四个空格的内容。连续的标签页构成一个标签页块，而 `===!` 会在另一个标签页块之后立即开始一个新块：

```
=== "Windows"

    Run the **installer**.

=== "Linux"

    Use the package.

===! "Another block"

    This tab starts a separate tabs block.
```

标签页可以通过在标签页内容中缩进内部标签页来嵌套。标签页标题是纯文本，因此其格式在导出时不会保留。有关标签页块在文本笔记中的工作方式，请参阅 <a class="reference-link" href="../../../Note%20Types/Text/Content%20tabs.md">内容标签页</a>。

## Wiki 链接

v0.96.0 中已添加对 Wiki 链接的基本支持：

*   `[[foo/bar]]` 将在 `foo` 目录中查找 `bar.md` 文件，并将其转换为内部链接。
*   `![[foo/baz.png]]` 将在 `foo` 目录中查找 `baz.png` 文件，并将其转换为图片。

此功能仅用于导入，这意味着它会将 Wiki 链接转换为 Trilium 兼容的语法，但不会将 Trilium 笔记导出为使用此语法的 Markdown 文件。

> [!IMPORTANT]
> Wiki 链接中的页面路径是相对于 _导入根目录_ 解析的，而不是相对于笔记的当前目录。这是为了与使用 Wiki 链接的其他平台（如 SilverBullet）保持一致。
> 
> 导入的根路径确定如下：
> 
> *   如果归档中根级别只有一个目录，则该目录被视为根目录。
> *   如果根级别有多个文件和目录，则归档根目录（包含所有这些项目）被视为根目录。

## 高亮

背景高亮以两种方式支持：

*   Markdown `==` 扩展，其他基于 Markdown 的应用程序（如 Obsidian）也支持：
    
    ```
    ==highlighted==
    ```
*   Trilium 支持的高亮规范 HTML 表示形式：
    
    ```html
    <span style="background-color:hsl(0,0%,100%);">Highlighted</span>
    ```

当使用黄色高亮时，导入/导出优先使用 `==` 语法，否则使用规范 HTML 表示形式。