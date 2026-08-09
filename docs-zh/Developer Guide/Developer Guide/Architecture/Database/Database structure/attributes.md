# 属性

<table>
    <thead>
        <tr>
            <th>列名</th>
            <th>数据类型</th>
            <th>可空性</th>
            <th>默认值</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th><code>attributeId</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>属性的唯一 ID（例如 <code>qhC1vzU4nwSE</code>），也可以是<a class="reference-link" href="#root/r11Bh3uxFGRj">特殊笔记</a>的专用唯一 ID（例如 <code>_lbToday_liconClass</code>）。</td>
        </tr>
        <tr>
            <th><code>noteId</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>该属性所属<a href="notes.md">笔记</a>的 ID。</td>
        </tr>
        <tr>
            <th><code>type</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>属性的类型（<code>label</code> 或 <code>relation</code>）。</td>
        </tr>
        <tr>
            <th><code>name</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>属性的名称/键。</td>
        </tr>
        <tr>
            <th><code>value</code></th>
            <td>文本</td>
            <td>非空</td>
            <td><code>""</code></td>
            <td><ul><li>对于 <code>label</code> 属性，为属性的自由格式值。</li><li>对于 <code>relation</code> 属性，为关系所指向的<a href="notes.md">笔记</a>的 ID。</li></ul></td>
        </tr>
        <tr>
            <th><code>position</code></th>
            <td>整数</td>
            <td>非空</td>
            <td>0</td>
            <td>属性相对于其他属性的位置。某些预定义属性（如 <code>originalFileName</code>）的值为 1000。</td>
        </tr>
        <tr>
            <th><code>utcDateModified</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>UTC 格式的修改日期（例如 <code>2023-11-08 16:43:44.204Z</code>）</td>
        </tr>
        <tr>
            <th><code>isDeleted</code></th>
            <td>整数</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>如果实体已被<a href="../../../Concepts/Deleted%20notes.md">删除</a>则为 <code>1</code>，否则为 <code>0</code>。</td>
        </tr>
        <tr>
            <th><code>deleteId</code></th>
            <td>文本</td>
            <td>可空</td>
            <td><code>null</code></td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <th><code>isInheritable</code></th>
            <td>整数</td>
            <td>可空</td>
            <td>0</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>