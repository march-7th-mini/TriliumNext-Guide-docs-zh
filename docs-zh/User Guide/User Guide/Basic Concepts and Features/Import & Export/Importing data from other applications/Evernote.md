# Evernote

Trilium 可以导入 ENEX 文件，这是 Evernote 用于备份/导出的文件格式。一个 ENEX 文件代表一个笔记本的内容（笔记和资源）。

## 导入流程

第一步是从 Evernote 导出数据：

*   导出单个笔记本：
    *   在左侧边栏中，选择 _笔记本_。
    *   如果有笔记本堆栈，请将其展开。
    *   右键单击一个笔记本，然后选择 _导出笔记本_。
    *   确保设置以下选项：
        *   文件格式设置为 _ENEX 格式_。
        *   勾选 _导出笔记属性_ 中的所有选项。
*   导出一批笔记（最多 100 条）：
    *   在左侧边栏中，选择 _笔记_。
    *   在笔记列表中，按住 <kbd>Ctrl</kbd> 并单击各个笔记以进行选择。或者，单击一个笔记，然后按住 <kbd>Shift</kbd> 并单击更远的笔记以选择两者之间的所有笔记。
    *   底部应有一个浮动工具栏，其中包含一些选项。选择 \[…\] → _导出_。
    *   确保设置以下选项：
        *   文件格式设置为 _ENEX 格式_。
        *   勾选 _导出笔记属性_ 中的所有选项。
*   导出单个笔记：
    *   选择该笔记。
    *   在右上角，按 \[…\] 按钮并选择 _导出_。
    *   确保设置以下选项：
        *   文件格式设置为 _ENEX 格式_。
        *   勾选 _导出笔记属性_ 中的所有选项。

> [!TIP]
> 要批量导出多个笔记本，可以考虑使用名为 [evernote-backup](https://github.com/vzhd1701/evernote-backup) 的第三方命令行工具。

获得 ENEX 文件后，请执行以下操作将其导入 Trilium：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键单击并选择 _导入到笔记_。
2.  在 _从导入_ 部分，选择 _Evernote_。
3.  在导入过程中，您将看到“正在导入”消息。如果导入成功，消息将变为“导入成功完成”，然后消失。
4.  我们建议您检查导入的笔记及其附件，以确认没有丢失任何数据。

## 支持的功能

Trilium 在导入过程中会保留以下功能：

*   基本格式（粗体、斜体、下划线、删除线、颜色、高亮、上标、下标、文本对齐、行内代码）。
*   标题层级（这些标题会调整为从 H2 开始，因为 H1 保留给笔记标题，请参阅 [标题](../../../Note%20Types/Text/General%20formatting.md)）
*   待办事项列表。新任务格式会折叠为标准待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>
*   <a class="reference-link" href="../../../Note%20Types/Text/Lists.md">列表</a>（项目符号或数字）
*   <a class="reference-link" href="../../../Note%20Types/Text/Tables.md">表格</a>
*   块引用
*   [警示框](../../../Note%20Types/Text/Block%20quotes%20%26%20admonitions.md) 会被保留，包括其表情符号（作为内容的一部分添加）。
*   <a class="reference-link" href="../../../Note%20Types/Text/Developer-specific%20formatting/Code%20blocks.md">代码块</a>，并尽力恢复其语言。
*   <a class="reference-link" href="../../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>
*   <a class="reference-link" href="../../../Note%20Types/Text/Math%20Equations.md">数学公式</a>
*   折叠区域
*   外部链接
*   如果目标笔记属于同一次导入，内部链接会被重写为 <a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>。

## 限制

*   单次导入的大小限制为 250Mb。如果文件总大小更大，您可以提高 [上传限制](../../../Installation%20%26%20Setup/Server%20Installation.md)，或者拆分文件，并根据需要多次运行导入。
*   所有资源（图片除外）都会作为笔记的附件创建。
*   如果 ENEX 文件中有 HTML，导入 Trilium 后 HTML 格式可能会损坏或丢失。请参阅 <a class="reference-link" href="../../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

### 指向其他笔记的链接

自 v0.104.0 起，ENEX 导入器会尝试通过将 Evernote 特定的 URL 转换为 Trilium 的 <a class="reference-link" href="../../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a> 来自动重建指向其他笔记的链接。

由于 ENEX 格式不提供笔记的唯一 ID，因此笔记引用是通过其笔记标题来确定的。

限制：

*   只有属于同一次导入的笔记，其链接才会被重写为引用链接，以避免链接到错误的笔记。
*   如果存在两个同名笔记，则不会创建内部链接，以避免指向错误的笔记。
*   无法重写的链接（例如，引用缺失/重复的笔记）将保留其原始的 `evernote://` URL。
*   它不会修复指向锚点的链接，也不会修复指向您在创建链接后在 Evernote 中重命名的笔记的链接。

#### 后处理笔记

> [!TIP]
> 此脚本允许在导入完成后重写链接，并且还应该允许查找两个不同导入之间的链接。

如果您想在导入所有 ENEX 文件后在 Trilium 中恢复内部链接，您可以使用或改编此自定义脚本：<a class="reference-link" href="Evernote/Process%20internal%20links%20by%20title.js">按标题处理内部链接</a>

该脚本执行以下操作：

1.  查找所有 Evernote 内部链接。
2.  对于每个链接，检查其链接文本是否与笔记标题匹配，如果匹配，则将 Evernote 链接替换为 Trilium 内部链接。如果不匹配，则保留 Evernote 链接。
3.  如果找到多个具有匹配标题的笔记，则保留 Evernote 链接。
4.  它将结果输出到日志中，您可以在 Trilium 中相应的代码笔记中查看该日志。

该脚本有以下限制：

*   它不会修复指向锚点的链接，也不会修复指向您在创建链接后在 Evernote 中重命名的笔记的链接。
*   某些笔记标题可能无法被很好地识别，即使它们存在。如果笔记标题包含某些特殊字符，尤其如此。如果这有问题，请考虑 <a class="reference-link" href="../../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

## 报告问题

在导入 Evernote 笔记本时，您可能会发现笔记导入方式存在问题；在这种情况下，请考虑 [报告](../../../Troubleshooting/Reporting%20issues.md) 该问题。

报告此类问题时，请确保提供以下信息：

*   原始笔记的 `.enex` 导出文件。这使我们能够重现该问题。
*   导入前原始外观和导入后外观的截图。