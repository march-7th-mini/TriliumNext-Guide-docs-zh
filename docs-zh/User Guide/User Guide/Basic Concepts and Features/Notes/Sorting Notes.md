# 笔记排序
## 手动排序

你可以通过在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击父笔记，然后选择“高级”->“按...排序笔记”来对笔记进行排序。这将排序现有的笔记，但不会自动排序将来添加到此父笔记下的笔记。

排序对话框允许：

*   按标题、创建日期或修改日期，或按子笔记上某个标签的值进行排序。
*   依次按多个此类条件排序，每个条件可升序或降序：下一级仅在前面几级判定为相等的笔记之间进行区分。
*   确保文件夹显示在顶部。
*   基于特定语言的排序规则进行自然排序。

## 自动/永久排序

通过将特定的[标签](../../Advanced%20Usage/Attributes.md)附加到父笔记上，可以自动对子笔记进行排序：

<table>
    <thead>
        <tr>
            <th>标签</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>#sorted</code></td>
            <td><p>保持子笔记按标题字母顺序排序。</p><p>当给定一个值时，它将改为按其他条件排序：一个以逗号分隔的层级列表，每个层级为 <code>title</code>、<code>dateCreated</code>、<code>dateModified</code> 或子笔记上某个标签的名称，后面可选跟 <code>asc</code> 或 <code>desc</code>，如同搜索的 <code>orderBy</code> 一样。例如 <code>#sorted="priority desc, dueDate"</code> 按优先级排序，最高优先，优先级相同的笔记按截止日期排序。没有某个层级标签的子笔记会排在该层级所有拥有该标签的子笔记之后，无论该层级的方向如何。当两个笔记都没有该标签时，由下一层级决定。</p></td>
        </tr>
        <tr>
            <td><code>#sortDirection</code></td>
            <td><p>如果应用了 <code>sorted</code>，则指定排序方向：</p><ul><li><code>ASC</code>，升序（默认）</li><li><code>DESC</code>，降序</li></ul><p>某个 <code>sorted</code> 层级后面若跟有自己的 <code>asc</code> 或 <code>desc</code>，则无论何种情况都保持该方向。</p></td>
        </tr>
        <tr>
            <td><code>#sortFoldersFirst</code></td>
            <td>如果应用了 <code>sorted</code>，文件夹（有子笔记的笔记）将作为一个组排在顶部（当 <code>#sortDirection</code> 为 <code>desc</code> 时排在底部），其余笔记则进行排序。</td>
        </tr>
        <tr>
            <td><code>#sortNatural</code></td>
            <td>按数字自然排序而非字母顺序，因此 2 排在 10 之前。</td>
        </tr>
        <tr>
            <td><code>#sortLocale</code></td>
            <td>驱动自然排序的语言代码（例如 <code>zh-CN</code>、<code>de</code>）。仅在配合 <code>#sortNatural</code> 时才有意义。</td>
        </tr>
        <tr>
            <td><code>#top</code></td>
            <td>如果父笔记应用了 <code>sorted</code>，则保持给定笔记在其父笔记中位于顶部。</td>
        </tr>
        <tr>
            <td><code>#bottom</code></td>
            <td>如果父笔记应用了 <code>sorted</code>，则保持给定笔记在其父笔记中位于底部。</td>
        </tr>
    </tbody>
</table>

排序是通过比较笔记属性或子笔记上的特定标签来完成的。共有四个排序层级，第一个优先级最高。只有在较高优先级的比较结果相等时，才会应用较低优先级的层级。

1.  **顶部标签排序**：带有 `#top` 标签的子笔记将出现在文件夹的顶部。
2.  **底部标签排序**：（在 Trilium 0.62 中引入）带有 `#bottom` 标签的子笔记将出现在文件夹的底部。
3.  **基于属性/标签的排序**：排序基于父笔记的 `#sorted` 标签：
    *   **默认排序**：如果 `#sorted` 没有值，笔记按字母顺序排序。
    *   **属性排序**：如果 `#sorted` 设置为 `title`、`dateModified` 或 `dateCreated`，笔记将基于指定的属性排序。
    *   **标签排序**：如果 `#sorted` 有任何其他值，该值将被视为子笔记某个标签的名称，排序基于该标签的值。例如，在父笔记上设置 `#sorted=myOrder`，并在子笔记上使用 `#myOrder=001`、`#myOrder=002` 等。
    *   **多层级排序**：上述几种可以组合使用，以逗号分隔；每个层级仅在前面的层级相等时才应用。每个层级可以在名称后跟一个词来携带自己的方向，`asc` 或 `desc`，否则遵循 `#sortDirection`。例如 `#sorted="priority desc, area, dateCreated"` 按优先级排序，最高优先，然后按区域，然后按创建日期。
4.  **字母顺序排序**：当其他条件结果相等时，作为最后的手段使用。

所有比较均按字符串进行（例如，"1" \< "2" 或 "2020-10-10" < "2021-01-15"，但 "2" \> "10" 也是如此）。