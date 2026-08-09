# Anytype

从 v0.104.0 版本开始，Trilium 能够从 Anytype 的 JSON 导入中导入数据，该导入方式保留了大部分格式和元信息。

## 导入流程

第一步是从 Anytype 导出数据：

*   要导出单个页面：
    *   选择要导出的页面。
    *   点击窗口右上角的 \[…\]，然后选择 _导出_。
    *   确保设置以下选项：
        *   导出格式：Any-Block
        *   文件格式：JSON
        *   Zip 压缩包：开启
        *   包含链接的对象：开启
        *   包含文件：开启
        *   包含已归档对象：开启
*   要导出整个频道：
    *   从左侧栏中选择所需的频道。
    *   在左侧边栏的频道图标下方，点击带有箭头的频道名称，然后选择 _频道设置_。
    *   在左侧边栏中，找到 _集成_ 部分并选择 _导出_。
    *   点击 _Any-Block_。
    *   确保设置以下选项：
        *   文件格式：JSON
        *   Zip 压缩包：开启
        *   包含文件：开启
        *   包含已归档对象：开启

在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键点击并选择 _导入到笔记_。
2.  在 _从导入_ 部分，选择 _Anytype_。
3.  上传 ZIP 文件。

> [!NOTE]
> 单独导出集合有时可能会遗漏信息，而这些信息本可以从整个频道的导出中获取。原因是 Anytype 在导出单个页面/集合时会省略某些信息。

## 支持的功能

Trilium 在导入过程中会保留以下功能：

*   基本格式（粗体、斜体、下划线、删除线、标题、颜色、高亮、行内代码）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Lists.md">列表</a>（有序或无序）
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a>和文件作为<a class="reference-link" href="../../Notes/Attachments.md">附件</a>处理。
*   待办事项列表
*   折叠区块
*   <a class="reference-link" href="../../../Note%20Types/Text/Tables.md">表格</a>
*   行内<a class="reference-link" href="../../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>
*   <a class="reference-link" href="../../../Note%20Types/Text/Math%20Equations.md">数学公式</a>
*   高亮块作为块引用导入。
*   <a class="reference-link" href="../../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>，并尽力恢复其语言。
*   同一导入中其他已导入页面之间的链接会转换为<a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
    *   适用于块链接和行内链接。
*   集合作为 Trilium 原生的<a class="reference-link" href="../../../Collections.md">集合</a>导入（见下文）。
    *   集合内的文件作为<a class="reference-link" href="../../../Note%20Types/File.md">文件</a>笔记导入。
*   分隔线（直线、圆点）作为水平分割线导入。
*   [警示框](../../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md)会被保留，包括其表情符号（作为内容的一部分添加）。
*   页面的创建和修改日期会被保留。

## 集合

在 Anytype 中创建的集合会尽力导入，保留视图模式和页面属性作为<a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>。

支持以下视图模式：

*   列表作为<a class="reference-link" href="../../../Collections/List%20View.md">列表视图</a>
*   画廊作为<a class="reference-link" href="../../../Collections/Grid%20View.md">网格视图</a>
*   <a class="reference-link" href="../../../Collections/Calendar.md">日历</a>，保留标识日期的属性。
*   <a class="reference-link" href="../../../Collections/Kanban%20Board.md">看板</a>，保留看板分组列。
*   <a class="reference-link" href="../../../Collections/Table.md">表格</a>，也用作不支持集合布局的回退方案。

支持以下类型：

<table>
    <thead>
        <tr>
            <th scope="col">Anytype 属性类型</th>
            <th scope="col">Trilium</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>文本 / 单选</td>
            <td>单值 <code spellcheck="false">text</code> 标签</td>
        </tr>
        <tr>
            <td>数字</td>
            <td>单值 <code spellcheck="false">number</code> 标签</td>
        </tr>
        <tr>
            <td>多选</td>
            <td>每个选项一个 <code spellcheck="false">text</code> 标签（多值）</td>
        </tr>
        <tr>
            <td>日期 / 日期时间</td>
            <td><ul><li>如果包含时间，则为 <code spellcheck="false">datetime</code>。</li><li>如果仅日期，则为 <code spellcheck="false">date</code>。</li></ul></td>
        </tr>
        <tr>
            <td>文件</td>
            <td>文件作为附件保留，并在笔记内容前添加指向它们的链接以便查看。</td>
        </tr>
        <tr>
            <td>复选框</td>
            <td><code spellcheck="false">boolean</code> 标签（<code spellcheck="false">true</code>/<code spellcheck="false">false</code>）。</td>
        </tr>
        <tr>
            <td>URL / 电子邮件 / 电话</td>
            <td><code spellcheck="false">url</code> 标签（<code spellcheck="false">mailto:</code>、<code spellcheck="false">tel:</code> 前缀）</td>
        </tr>
    </tbody>
</table>

## 报告问题

在导入 Anytype 笔记时，您可能会发现笔记导入方式存在问题；在这种情况下，请考虑[报告](../../../Troubleshooting/Reporting%20issues.md)问题。

报告此类问题时，请务必提供以下信息：

*   原始笔记（以及适用的子笔记）的 .zip 导出文件。这使我们能够重现问题。
*   导入前原始样子的截图以及导入后的样子。