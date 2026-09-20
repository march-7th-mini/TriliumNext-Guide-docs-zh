# Notion
Trilium 可以导入 Notion 的 ZIP 导出文件，同时保留结构和格式。

## 导入过程

在 Notion 中，有两种导出数据的方式：

*   导出单个页面（以及可选的其子页面）：
    *   选择要导出的页面。
    *   按窗口右上角的 \[…\] 按钮并选择 _Export_。
    *   确保设置了以下选项：
        *   Export format: HTML
        *   Page content: Everything
        *   Include subpages: On
        *   Create folders for subpages: On
    *   按 Export 按钮。
    *   等待下载完成。
*   导出整个工作区，按左上角的用户名徽章并选择 _Settings_。
    *   在左侧区域，找到 _Workspace_ 类别并选择 _General_。
    *   在 _General_ 设置页面中，找到 _Export_ 部分并按对应 _Workspace content_ 的 _Export_ 按钮。
    *   确保设置了以下选项：
        *   Export format: HTML
        *   Page content: Everything
        *   Include subpages: On
        *   Create folders for subpages: On
    *   按 Export 按钮。
    *   等待下载完成。根据工作区的大小，这可能需要一段时间。如果耗时过长，你会通过电子邮件收到可下载的副本。

在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键单击并选择 _Import into note_。
2.  在 _Import from_ 部分，选择 _Notion_。
3.  上传上一步获得的 ZIP 文件。

## 支持的功能

Trilium 在导入过程中会保留以下功能：

*   基本格式（粗体、斜体、下划线、删除线、标题、颜色、高亮）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Lists.md">列表</a>
*   待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
*   折叠区块
    *   也支持嵌套的折叠区块。
    *   折叠标题会去掉其折叠按钮，变为普通标题。
*   <a class="reference-link" href="../../../Note%20Types/Text/Math%20Equations.md">数学公式</a>（行内或块级）
*   <a class="reference-link" href="../../../Note%20Types/Text/Link%20Previews.md">链接预览</a>
    *   链接的图标和图片需要在线获取，因为导出文件不包含图片。仅当在 <a class="reference-link" href="../../UI%20Elements/Options.md">选项</a> → _Media_ 中启用了 _Download images automatically_ 时才会执行此操作。
*   <a class="reference-link" href="../../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>，并尽力恢复语言。
*   <a class="reference-link" href="../../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>
*   其他导入页面之间的链接，如果属于同一次导入，会转换为 <a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
*   数据库会作为 <a class="reference-link" href="../../../Collections.md">集合</a> 导入（见下文）。
*   [警示框](../../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md) 会被保留，包括其 emoji（作为内容的一部分添加）。
*   列会作为透明 [表格](../../../Note%20Types/Text/Tables.md) 导入，保留列定义。
*   目录块会被 _移除_，因为目录已经存在于侧边栏中（见 <a class="reference-link" href="../../../Note%20Types/Text/Table%20of%20contents.md">目录</a>），以及共享笔记中。

## 数据库

Notion 数据库会导入为 <a class="reference-link" href="../../../Collections.md">集合</a>，其中数据库的每个条目都保存为集合中的一个页面。通过使用 [继承](../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md) <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>，Notion 中的大部分页面属性都会被导入保留。

无论数据库导出时的原始视图是什么，生成的集合都会是 <a class="reference-link" href="../../../Collections/Table.md">表格</a>。这是因为活动视图不会保存在导出文件中，而表格集合与 Notion 的兼容性最好。

<table>
    <thead>
        <tr>
            <th scope="col">Notion 类型</th>
            <th scope="col">Trilium</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Text / Select / Status / Place</td>
            <td>单值 <code>text</code> 标签</td>
        </tr>
        <tr>
            <td>Number</td>
            <td>对于纯数字，使用单值 <code>number</code> 标签。格式化值（货币、百分比、千位分隔符）会规范化为纯数字，例如 <code>$1,200.50</code> → <code>1200.50</code>。</td>
        </tr>
        <tr>
            <td>ID</td>
            <td>单值 <code>number</code> 或 <code>text</code> 标签（取决于是否配置了前缀）</td>
        </tr>
        <tr>
            <td>Multi-select</td>
            <td>每个选项一个文本标签（多值）</td>
        </tr>
        <tr>
            <td>URL / Email / Phone</td>
            <td><code>url</code> 标签（<code>mailto:</code>、<code>tel:</code> 前缀）</td>
        </tr>
        <tr>
            <td>Date</td>
            <td><ul><li>如果至少有一个包含时间，则为 <code>datetime</code>。</li><li>如果只有日期，则为 <code>date</code>。</li><li>如果任何日期有结束日期，则为两个属性。</li></ul></td>
        </tr>
        <tr>
            <td>Checkbox</td>
            <td><code>boolean</code> 标签（<code>true</code>/<code>false</code>）。</td>
        </tr>
        <tr>
            <td>Person</td>
            <td>每个用户一个文本标签（多值）</td>
        </tr>
        <tr>
            <td>Created by / Edited by</td>
            <td>单值 <code>text</code> 标签</td>
        </tr>
        <tr>
            <td>Created time / Last edited time</td>
            <td>分配给笔记的创建和修改日期。</td>
        </tr>
        <tr>
            <td>Relation</td>
            <td>映射为 <a href="../../../Advanced%20Usage/Attributes/Relations.md">关系</a>，每个链接通过现有的跨页面映射解析到其目标笔记；导入之外的目标会被丢弃。</td>
        </tr>
        <tr>
            <td>Files &amp; Media</td>
            <td>文件会保留为附件，并且指向它们的链接会前置到笔记内容中以便查看。</td>
        </tr>
        <tr>
            <td>Formulas / Rollup</td>
            <td><p>根据值类型为 <code>text</code>、<code>number</code> 或 <code>boolean</code> 标签。日期会渲染为 <code>text</code>，因为导出文件不提供任何类型信息。</p><p>Notion 导出不会保留公式/汇总配置本身，而只是导出值。</p></td>
        </tr>
        <tr>
            <td>Button / Verification / 任何其他类型</td>
            <td>不支持，它们会从导入中丢弃。</td>
        </tr>
    </tbody>
</table>

> [!NOTE]
> **技术信息**
> 
> 根据上表可以保留的每个页面属性都会保存为对应笔记的标签或关系（创建和修改日期除外，它们保存在笔记级别）。
> 
> 为了保持与 Notion 类似的用户体验，每个属性还会在集合级别转换为 <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>。这也使列在表格集合中可见。提升属性被设为可继承，以便在子笔记中导航时也会出现。
> 
> 标签名称有意转换为 `camelCase` 以匹配 Trilium 的约定，但列的完整名称通过提升属性的 _Alias_ 机制保留。

## 限制

### 导入中缺失的数据

以下信息不会被导入保留，因为它不在导出文件中，因此无法恢复：

*   页面和子页面的顺序。
*   创建/修改日期仅在页面包含 Created time / Last edited time 属性（无论是否为集合）时才会恢复；否则使用导入时间。

### 封面图片和页面图标

页面图标或 emoji 不会被保留，创建的笔记会使用默认图标。封面图片完全不会导入。

## 报告问题

在导入 Notion 工作区时，你可能会发现笔记导入方式的问题；在这种情况下，请考虑 [报告](../../../Troubleshooting/Reporting%20issues.md) 它。

报告此类问题时，请确保提供以下信息：

*   原始 Notion 笔记（以及适用的子笔记）的 .zip 导出文件。这使我们能够重现问题。
*   一张截图，显示导入前的原始外观和导入后的外观。