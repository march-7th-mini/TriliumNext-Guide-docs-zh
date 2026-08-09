# 笔记排序
## 手动排序

您可以通过右键点击<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中的父笔记，然后选择“高级 -> 按...排序笔记”来对笔记进行排序。这将排序现有的笔记，但不会自动排序未来添加到该父笔记下的新笔记。

排序对话框支持：

*   按标题、创建日期或修改日期排序。
*   可以调整排序方向（升序或降序）。
*   确保文件夹显示在顶部。
*   基于特定语言排序规则的自然排序。

## 自动/永久排序

可以通过在父笔记上附加特定的[标签](../../Advanced%20Usage/Attributes.md)来自动排序子笔记：

<table>
    <thead>
        <tr>
            <th>标签</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code spellcheck="false">#sorted</code></td>
            <td><p>保持子笔记按标题字母顺序排序。</p><p>当赋予一个值时，它将改为按另一个标签的值进行排序。如果某个子笔记没有指定的标签，则将使用其标题进行排序。</p></td>
        </tr>
        <tr>
            <td><code spellcheck="false">#sortDirection</code></td>
            <td><p>如果应用了 <code spellcheck="false">sorted</code>，则指定排序方向：</p><ul><li><code spellcheck="false">ASC</code>，升序（默认）</li><li><code spellcheck="false">DESC</code>，降序</li></ul></td>
        </tr>
        <tr>
            <td><code spellcheck="false">#sortFoldersFirst</code></td>
            <td>如果应用了 <code spellcheck="false">sorted</code>，则文件夹（有子笔记的笔记）将作为一组排在顶部，其余笔记再进行排序。</td>
        </tr>
        <tr>
            <td><code spellcheck="false">#sortNatural</code></td>
            <td>按数字自然排序而非字母顺序，因此 2 排在 10 之前。</td>
        </tr>
        <tr>
            <td><code spellcheck="false">#sortLocale</code></td>
            <td>驱动自然排序的语言代码（例如 <code spellcheck="false">zh-CN</code>、<code spellcheck="false">de</code>）。仅与 <code spellcheck="false">#sortNatural</code> 一起使用时才有意义。</td>
        </tr>
        <tr>
            <td><code spellcheck="false">#top</code></td>
            <td>如果父笔记应用了 <code spellcheck="false">sorted</code>，则使指定笔记保持在其父笔记中的顶部。</td>
        </tr>
        <tr>
            <td><code spellcheck="false">#bottom</code></td>
            <td>如果父笔记应用了 <code spellcheck="false">sorted</code>，则使指定笔记保持在其父笔记中的底部。</td>
        </tr>
    </tbody>
</table>

排序是通过比较子笔记的笔记属性或特定标签来完成的。有四个排序级别，第一个级别优先级最高。仅当较高级别的比较结果相等时，才会应用较低优先级的级别。

1.  **顶部标签排序**：带有 `#top` 标签的子笔记将出现在文件夹顶部。
2.  **底部标签排序**：（在 Trilium 0.62 中引入）带有 `#bottom` 标签的子笔记将出现在文件夹底部。
3.  **属性/标签排序**：排序基于父笔记的 `#sorted` 标签：
    *   **默认排序**：如果 `#sorted` 没有值，则笔记按字母顺序排序。
    *   **属性排序**：如果 `#sorted` 设置为 `title`、`dateModified` 或 `dateCreated`，则笔记根据指定的属性进行排序。
    *   **标签排序**：如果 `#sorted` 有任何其他值，则该值被视为子笔记标签的名称，排序基于此标签的值。例如，在父笔记上设置 `#sorted=myOrder`，并在子笔记上使用 `#myOrder=001`、`#myOrder=002` 等。
4.  **字母顺序排序**：当其他条件比较结果相等时，作为最后的手段使用。

所有比较均按字符串方式进行（例如，"1" \< "2" 或 "2020-10-10" < "2021-01-15"，但 "2" \> "10" 也是成立的）。