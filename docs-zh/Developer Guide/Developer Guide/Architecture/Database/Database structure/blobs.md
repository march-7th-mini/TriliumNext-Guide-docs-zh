# blobs

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
            <th><code>blobId</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td><p>blob 的唯一 ID（例如 <code>XXbfAJXqWrYnSXcelLFA</code>）。</p><aside class="admonition important"><p>该 ID 实际上是内容的哈希值，参见 <code>AbstractBeccaEntity#saveBlob</code>！修改现有 blob 属于逻辑错误。</p></aside></td>
        </tr>
        <tr>
            <th><code>content</code></th>
            <td>文本</td>
            <td>可空</td>
            <td><code>null</code></td>
            <td><p>blob 的内容，可以是：</p><ul><li>文本（用于纯文本笔记或 HTML 笔记）。</li><li>二进制（用于图片和其他类型的附件）</li></ul></td>
        </tr>
        <tr>
            <th><code>dateModified</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td>带时区偏移的创建日期（例如 <code>2023-11-08 18:43:44.204+0200</code>）</td>
        </tr>
        <tr>
            <th><code>utcDateModified</code></th>
            <td>文本</td>
            <td>非空</td>
            <td>&nbsp;</td>
            <td><p>UTC 格式的创建日期（例如 <code>2023-11-08 16:43:44.204Z</code>）。</p><p>Blob 不可修改，因此该时间戳表示 blob 的创建时间。</p></td>
        </tr>
    </tbody>
</table>