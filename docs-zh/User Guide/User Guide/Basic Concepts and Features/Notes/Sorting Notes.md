# 笔记排序
## 手动排序

你可以通过在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击父笔记并选择“高级”->“按……排序笔记”来对笔记进行排序。这将对现有笔记进行排序，但不会自动对之后添加到此父笔记的笔记进行排序。

排序对话框允许：

*   按标题、创建日期或修改日期，或按子笔记上某个标签的值进行排序。
*   依次按多个此类条件进行排序，每个条件可升序或降序：下一层级仅在前面的条件判定为相等的笔记之间进行决定。
*   确保文件夹显示在顶部。
*   自然排序，基于特定语言的排序规则。

## 自动/永久排序

可以通过将特定的[标签](../../Advanced%20Usage/Attributes.md)附加到父笔记来对子笔记进行自动排序：

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
            <td><p>保持子笔记按标题字母顺序排序。</p><p>当给定一个值时，将改为按其他条件排序：一个以逗号分隔的层级列表，每个层级是子笔记上以 <code>#</code> 书写的标签，或者是 <code>title</code>、<code>dateCreated</code>、<code>dateModified</code> 和 <code>folders</code> 属性之一，后面可选地跟上 <code>asc</code> 或 <code>desc</code>，如同搜索中的 <code>orderBy</code>。例如 <code>#sorted="#priority desc, #dueDate"</code> 按优先级排序，最高优先，优先级相同的笔记按截止日期排序。缺少某层级标签的子笔记会排在该层级所有具有该标签的子笔记之后，无论该层级的方向如何。当两个笔记都没有该标签时，由下一层级决定。</p><p>标签后跟 <code>first</code> 或 <code>last</code> 则会将具有该标签的子笔记分组到其余笔记之前或之后，无论其值如何。例如 <code>#sorted="#archived last, title"</code> 将<a href="Archived%20Notes.md">已归档笔记</a>保持在其他笔记之下。</p></td>
        </tr>
        <tr>
            <td><code>#sortDirection</code></td>
            <td><p>如果应用了 <code>sorted</code>，则指定排序方向：</p><ul><li><code>ASC</code>，升序（默认）</li><li><code>DESC</code>，降序</li></ul><p><code>sorted</code> 的某个层级后跟其自身的 <code>asc</code> 或 <code>desc</code> 时，无论何种情况都保持该方向，<code>first</code> 或 <code>last</code> 分组也是如此。</p></td>
        </tr>
        <tr>
            <td><code>#sortFoldersFirst</code></td>
            <td>如果应用了 <code>sorted</code>，文件夹（有子笔记的笔记）将作为一组排在顶部（当 <code>#sortDirection</code> 为 <code>desc</code> 时排在底部），其余笔记将被排序。当 <code>sorted</code> 自身放置了 <code>folders</code> 时忽略此项。</td>
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

排序通过比较子笔记的笔记属性或特定标签来完成。共有四个排序层级，第一个具有最高优先级。只有在较高优先级的比较结果为相等时，才会应用较低优先级的层级。

1.  **顶部标签排序**：带有 `#top` 标签的子笔记将出现在文件夹的顶部，除非 `#sorted` 自身放置了 `#top`（见下文）。
2.  **底部标签排序**：（在 Trilium 0.62 中引入）带有 `#bottom` 标签的子笔记将出现在文件夹的底部，除非 `#sorted` 自身放置了 `#bottom`。
3.  **基于属性/标签的排序**：排序基于父笔记的 `#sorted` 标签：
    *   **默认排序**：如果 `#sorted` 没有值，笔记按字母顺序排序。
    *   **属性排序**：如果 `#sorted` 设置为 `title`、`dateModified` 或 `dateCreated`，笔记将基于指定属性排序。`folders` 属性（有子笔记的笔记具有此属性）用于分组，如 `folders first`，单独的 `folders` 层级也会如此，因为没有子笔记的笔记会排在具有子笔记的笔记之后；单独使用时，`#sorted=folders` 仍按 `#folders` 标签排序。
    *   **标签排序**：如果 `#sorted` 设置为子笔记某个标签的名称，则基于该标签的值排序。例如，在父笔记上设置 `#sorted=#myOrder`，并在子笔记上使用 `#myOrder=001`、`#myOrder=002` 等。不带 `#` 且不是上述属性之一的单个名称也会被视为标签，因此 `#sorted=myOrder` 效果相同。
    *   **多层级排序**：上述几种可以组合使用，以逗号分隔；每个层级仅在前面的层级相等时应用。标签以 `#` 书写，属性则不带。每个层级可以在名称后跟一个词来指定自己的方向，`asc` 或 `desc`，否则遵循 `#sortDirection`。例如 `#sorted="#priority desc, #area, dateCreated"` 先按优先级排序（最高优先），再按区域排序，再按创建日期排序。
    *   **分组**：标签或 `folders` 后跟 `first` 或 `last` 会将具有该标签（任意值）的子笔记放在其余笔记之前或之后，不受 `#sortDirection` 影响。后续层级则在每个分组内进行排序。例如 `#sorted="#archived last, #priority desc"`。带有 `#top` 或 `#bottom` 的笔记即使属于某个分组也仍保持在顶部或底部，除非 `#sorted` 也指定了这些标签。
    *   **放置 `#top` 和 `#bottom`**：在 `#sorted` 中指定 `#top` 或 `#bottom` 会将其应用于该位置，而非在每个层级之前。例如 `#sorted="#archived last, #top first, #bottom last, title"` 将已归档笔记保持在所有其他笔记之下（包括带有 `#bottom` 的笔记），而 `#top` 和 `#bottom` 则在两个分组内各自应用。在其后添加 `folders first`，如 `#sorted="#archived last, #top first, #bottom last, folders first, title"`，也会在每个分组内对文件夹进行分组，因此已归档的文件夹会排在其他笔记之下。`#sortFoldersFirst` 以相同方式放置 `folders first`，紧跟在最后一个 `#top` 和 `#bottom` 之后。以 `first` 或 `last` 书写时，标签忽略其值；要按值对多个固定笔记排序，请在其后添加一个层级，如 `#top` 或 `#bottom desc`。
4.  **字母排序**：当其他条件结果为相等时作为最后手段使用。

> [!WARNING]
> 自 v0.107.0 起，多层级 `#sorted` 中的标签必须带 `#` 书写。在 v0.106.0 中，名称是裸写的，如 `#sorted="priority desc, dueDate"`；这样的值现在会将两个名称都读取为不存在的属性，并回退到按标题排序。在每个标签名称前添加 `#` 即可恢复。

所有比较均按字符串进行（例如 "1" \< "2" 或 "2020-10-10" < "2021-01-15"，但 "2" \> "10" 也是如此）。