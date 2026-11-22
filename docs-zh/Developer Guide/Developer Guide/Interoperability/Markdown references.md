# Markdown 引用

本页说明 Trilium 在 Markdown 导入和导出时如何存储对标题及其他块的引用。

## 引用锚点

Trilium 将所引用块的 ID 存储在一个空锚点中。

```markdown
## Installation <a data-trilium-block-id="eaJkN47U8kI4"></a>

Download the package for your platform. <a data-trilium-block-id="Hq2LmT0vX9cB"></a>
```

块文本中的锚点标记该块。锚点单独成行时，标记下一个块。锚点后跟一个空行。

```markdown
<a data-trilium-block-id="Zk3PqR8sT1uV"></a>

> A quote, referenced as a whole.
```

Trilium 根据块类型放置锚点。

| 块 | Trilium 存储 ID 的位置 |
| --- | --- |
| 段落、列表项、任务列表项 | 文本末尾的锚点中 |
| 标题 | 文本末尾的锚点中，位于任何结尾 `#` 字符之前 |
| 表格 | 第一个表头单元格末尾的锚点中 |
| 标签页块中的标签页 | 标签页标题末尾的锚点中，位于引号内 |
| 以块公式开头的段落 | 行首的锚点中 |
| 空段落 | `&nbsp;` 之后的锚点中 |
| 代码块、Mermaid 图表、引用、警示框、水平分割线、标签页块 | 块上方单独一行的锚点中 |
| 需要 HTML 的表格，例如没有表头行的表格 | 表格 HTML 包装器上的 `data-trilium-block-id` 属性中，`<figure class="table" data-trilium-block-id="…">` |
| 其他 HTML，例如可折叠块、包含的笔记或摘录、图片、旁注或多栏布局 | 元素本身的 `data-trilium-block-id` 属性中 |

在引用、列表项或标签页内部，单独成行的锚点保留容器的 `>` 前缀或缩进。

Trilium 也接受 `<a data-trilium-block-id="ID" />` 以及没有闭合 `</a>` 的开始标签。ID 可以使用单引号或双引号。保持标签在一行内，并且只包含 `data-trilium-block-id` 属性。

ID 必须至少包含一个字符。冒号保留用于分隔范围的端点。Trilium 生成的 ID 包含 12 个字母和数字。对于其他 ID，Trilium 按原样保留 `A` 到 `Z`、`a` 到 `z`、`0` 到 `9`、`_`、`.` 和 `-`。其他字符编码为数字字符引用，例如空格编码为 `&#32;`。Trilium 在验证之前解码 ID，因此包含 `&#58;` 的 ID 无效。

当 Trilium 渲染 Markdown 笔记时，它将 ID 从锚点移动到块的 HTML 元素上。文本笔记以相同方式存储 ID，因此当你将 Markdown 导入为文本笔记或将 Markdown 笔记转换为文本笔记时，也会发生这种情况。

```html
<h2 data-trilium-block-id="eaJkN47U8kI4">Installation</h2>
<p data-trilium-block-id="Hq2LmT0vX9cB">Download the package for your platform.</p>
```

Markdown 笔记也支持命名锚点，例如 `<a id="setup"></a>`。使用 `?bookmark=setup` 链接到命名锚点。`block` 参数用于块 ID。

## 链接和摘录

要链接到块，请在笔记 ID 之后添加 `block` 参数。对于范围，使用第一个和最后一个块 ID，中间用冒号分隔。

```markdown
[[B9oMG6rFvvfq?block=eaJkN47U8kI4]]
[[B9oMG6rFvvfq?block=eaJkN47U8kI4:Zk3PqR8sT1uV]]
[Installation](#root/B9oMG6rFvvfq?block=eaJkN47U8kI4)
<figure class="include-note" data-note-id="B9oMG6rFvvfq" data-block="eaJkN47U8kI4:Zk3PqR8sT1uV" data-box-size="full"></figure>
```

最后一个示例是摘录。它仅包含笔记中所引用的块。

## 行为

### 标题

*   当你通过 _添加链接_ 对话框或 `@` 列表链接到标题时，如果需要，Trilium 会在标题末尾添加一个锚点。即使笔记是只读的，这也会更新目标笔记。
*   当你重命名标题时，链接会跟随锚点。
*   读取标题文本时忽略锚点。目录和 _添加链接_ 对话框会自动执行此操作。

### 范围

*   单个块需要一个锚点。范围使用两个 ID，写作 `start:end`，并且两端各需要一个锚点。
*   范围包括两个块及其之间的所有内容。Trilium 使用笔记中块的顺序，因此 `end:start` 给出相同的结果。
*   你在两个锚点之间添加的块会成为范围的一部分。
*   Trilium 从渲染后的笔记读取范围。范围覆盖整个块，并保留周围的列表或引用。在 Markdown 源中跨多行换行的段落仍算作一个块。
*   对列表项的引用仅包含该项自身的文本。嵌套项在该引用之外。
*   如果任一锚点缺失，整个引用就会中断。摘录会显示 _引用已损坏_。

### 所有锚点

*   只有块中的第一个锚点有效。
*   两个不同的笔记可以使用相同的 ID。在笔记内，ID 属于第一个使用它的块。当你在同一笔记内复制块时，将其锚点保留在原始块上。
*   在代码块或行内代码中，锚点标记被视为文本。对于 HTML 块，将 ID 放在元素的 `data-trilium-block-id` 属性中。
*   单独成行的锚点标记下一个块。如果你删除该块并保留锚点，它会标记接下来的任意块。
*   其他 Markdown 渲染器会隐藏块内的锚点，并为单独成行的锚点显示一个空段落。转义 HTML 的渲染器会将标签显示为文本。

### 导入和导出

*   当你将文本笔记导出为 Markdown 文件或 ZIP 归档时，Trilium 将其块 ID 写为锚点。_复制为 Markdown_ 和脚本 API 函数 `api.htmlToMarkdown()` 会省略这些锚点。
*   当你将 Markdown 导入为文本笔记时，Trilium 将块 ID 放在 `data-trilium-block-id` 属性中。当你将其导入为 Markdown 笔记时，Trilium 按原样保留源内容。
*   当你在文本笔记和 Markdown 笔记之间转换时，Trilium 会保留块 ID。空代码块和只有一个单元格的表格在 Markdown 中没有地方存储锚点。Trilium 会报告转换期间从这些块中丢失的任何 ID。
*   ZIP 导出会在目标文件名之后保留 `block` 和 `bookmark` 参数。当你导入归档时，Trilium 会将这些参数转移到新的笔记 ID。在 _HTML for web_ 导出格式中，`bookmark` 会变成 `#` 片段。