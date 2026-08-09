# Notion

Trilium 可以导入从 Notion 导出的 ZIP 文件，同时保留其结构和格式。

## 导入流程

在 Notion 中，有两种导出数据的方式：

*   导出单个页面（以及可选的子页面）：
    *   选择要导出的页面。
    *   点击窗口右上角的 \[…\] 按钮，然后选择 _导出_。
    *   确保设置以下选项：
        *   导出格式：HTML
        *   页面内容：所有内容
        *   包含子页面：开启
        *   为子页面创建文件夹：开启
    *   点击导出按钮。
    *   等待下载完成。
*   要导出整个工作区，请点击左上角的用户名徽章，然后选择 _设置_。
    *   在左侧区域，找到 _工作区_ 类别并选择 _常规_。
    *   在 _常规_ 设置页面中，找到 _导出_ 区域，然后点击与 _工作区内容_ 对应的 _导出_ 按钮。
    *   确保设置以下选项：
        *   导出格式：HTML
        *   页面内容：所有内容
        *   包含子页面：开启
        *   为子页面创建文件夹：开启
    *   点击导出按钮。
    *   等待下载完成。根据工作区的大小，这可能需要一些时间。如果耗时过长，你将通过电子邮件收到可下载的副本。

在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键单击并选择 _导入到笔记_。
2.  在 _从导入_ 部分，选择 _Notion_。
3.  上传上一步获得的 ZIP 文件。

## 支持的功能

Trilium 在导入过程中会保留以下功能：

*   基本格式（粗体、斜体、下划线、删除线、标题、颜色、高亮）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Lists.md">列表</a>
*   待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
*   折叠区块
    *   也支持嵌套的折叠区块。
    *   折叠标题的折叠按钮会被移除，并转换为普通标题。
*   <a class="reference-link" href="../../../Note%20Types/Text/Math%20Equations.md">数学公式</a>（行内或块级）
*   <a class="reference-link" href="../../../Note%20Types/Text/Link%20Previews.md">链接预览</a>
    *   由于导出文件不包含图标和图像，因此需要在线获取这些内容。只有在 <a class="reference-link" href="../../UI%20Elements/Options.md">选项</a> → _媒体_ 中启用了 _自动下载图片_ 时，才会执行此操作。
*   <a class="reference-link" href="../../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>，并会尽力恢复其语言。
*   <a class="reference-link" href="../../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>
*   如果链接指向同一导入中的其他页面，则会转换为 <a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。
*   数据库将作为 <a class="reference-link" href="../../../Collections.md">集合</a> 导入（见下文）。
*   [警示框](../../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md) 会被保留，包括其表情符号（作为内容的一部分添加）。
*   分栏将作为透明的[表格](../../../Note%20Types/Text/Tables.md)导入，并保留分栏定义。
*   目录块会被 _移除_，因为侧边栏（参见 <a class="reference-link" href="../../../Note%20Types/Text/Table%20of%20contents.md">目录</a>）以及共享笔记中已包含目录。

## 数据库

Notion 数据库会导入到 <a class="reference-link" href="../../../Collections.md">集合</a> 中，数据库中的每个条目都会保存为集合中的一个页面。通过使用[继承的](../../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md) <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>，Notion 中的大部分页面属性都能在导入后保留。

生成的集合将是 <a class="reference-link" href="../../../Collections/Table.md">表格</a> 类型，无论数据库导出时的原始视图是什么。这是因为活动视图不会保存在导出文件中，而表格集合是与 Notion 兼容性最好的。

<table>
    <thead>
        <tr>
            <th scope="col">Notion 类型</th>
            <th scope="col">Trilium</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>文本 / 单选 / 状态 / 地点</td>
            <td>单值 <code spellcheck="false">text</code> 标签</td>
        </tr>
        <tr>
            <td>数字</td>
            <td>纯数字使用单值 <code spellcheck="false">number</code> 标签。格式化值（货币、百分比、千位分隔符）会规范化为纯数字，例如 <code spellcheck="false">$1,200.50</code> → <code spellcheck="false">1200.50</code>。</td>
        </tr>
        <tr>
            <td>ID</td>
            <td>单值 <code spellcheck="false">number</code> 或 <code spellcheck="false">text</code> 标签（取决于是否配置了前缀）</td>
        </tr>
        <tr>
            <td>多选</td>
            <td>每个选项一个文本标签（多值）</td>
        </tr>
        <tr>
            <td>URL / 电子邮件 / 电话</td>
            <td><code spellcheck="false">url</code> 标签（带 <code spellcheck="false">mailto:</code>、<code spellcheck="false">tel:</code> 前缀）</td>
        </tr>
        <tr>
            <td>日期</td>
            <td><ul><li>如果至少有一个包含时间，则为 <code spellcheck="false">datetime</code>。</li><li>如果只有日期，则为 <code spellcheck="false">date</code>。</li><li>如果任何日期有结束日期，则为两个属性。</li></ul></td>
        </tr>
        <tr>
            <td>复选框</td>
            <td><code spellcheck="false">boolean</code> 标签（<code spellcheck="false">true</code>/<code spellcheck="false">false</code>）。</td>
        </tr>
        <tr>
            <td>人员</td>
            <td>每个用户一个文本标签（多值）</td>
        </tr>
        <tr>
            <td>创建者 / 编辑者</td>
            <td>单值 <code spellcheck="false">text</code> 标签</td>
        </tr>
        <tr>
            <td>创建时间 / 最后编辑时间</td>
            <td>分配给笔记的创建和修改日期。</td>
        </tr>
        <tr>
            <td>关联</td>
            <td>映射到<a href="../../../Advanced%20Usage/Attributes/Relations.md">关系</a>，每个链接通过现有的跨页面映射解析到其目标笔记；导入范围之外的目标将被丢弃。</td>
        </tr>
        <tr>
            <td>文件与媒体</td>
            <td>文件作为附件保留，并在笔记内容前添加指向它们的链接以便查看。</td>
        </tr>
        <tr>
            <td>公式 / 汇总</td>
            <td><p>根据值类型生成 <code spellcheck="false">text</code>、<code spellcheck="false">number</code> 或 <code spellcheck="false">boolean</code> 标签。日期会渲染为 <code spellcheck="false">text</code>，因为导出文件不提供任何类型信息。</p><p>Notion 导出不保留公式/汇总配置本身，只导出其值。</p></td>
        </tr>
        <tr>
            <td>按钮 / 验证 / 其他任何类型</td>
            <td>不支持，这些属性将从导入中丢弃。</td>
        </tr>
    </tbody>
</table>

> [!NOTE]
> **技术信息**
> 
> 根据上表可以保留的每个页面属性都会保存为对应笔记的标签或关系（创建和修改日期除外，它们保存在笔记级别）。
> 
> 为了保持与 Notion 相似的用户体验，每个属性也会在集合级别转换为 <a class="reference-link" href="../../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>。这也使得这些列在表格集合中可见。提升属性被设置为可继承，以便在子笔记中导航时也能显示。
> 
> 标签的名称有意转换为 `camelCase` 以符合 Trilium 的约定，但列的完整名称会通过提升属性的 _别名_ 机制保留。

## 限制

### 导入时缺失的数据

以下信息无法通过导入保留，因为导出文件中不包含这些信息，因此无法恢复：

*   页面和子页面的顺序。
*   仅当页面包含“创建时间 / 最后编辑时间”属性时（无论是否为集合），才会恢复创建/修改日期；否则将使用导入时间。

### 封面图片和页面图标

页面图标或表情符号不会被保留，创建的笔记将使用默认图标。封面图片完全不会被导入。

## 报告问题

在导入你的 Notion 工作区时，你可能会发现笔记导入方式存在问题；在这种情况下，请考虑[报告](../../../Troubleshooting/Reporting%20issues.md)该问题。

报告此类问题时，请务必提供以下信息：

*   原始 Notion 笔记的 .zip 导出文件（如果适用，包括子笔记）。这使我们能够重现该问题。
*   导入前原始外观和导入后外观的截图。