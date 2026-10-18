# Google Keep
Trilium 可以从 Google Keep 导入笔记，并保留其结构和格式。

## 导入流程

Google Keep 没有原生的导出流程，但 Google Takeout 允许你下载包含所有笔记的 ZIP 文件。

第一步是下载你的 Google Keep 信息：

1.  访问 [takeout.google.com](https://takeout.google.com/)。
2.  在 _Create a new export_ 部分，点击 _Deselect all._
3.  在要导出的数据列表中，勾选 _Keep_。
4.  滚动到最底部并选择 _Next step_。
5.  在 _Choose file type, frequency & destination_ 中确保设置了以下选项：
    1.  _Transfer to_ 设置为 _Send download link via email_。
    2.  _Frequency_ 设置为 _Export once_。
    3.  _File type_ 设置为 _.zip_。
    4.  _File size_ 可以保持为 _2 GB_。
6.  点击 _Create export_ 并等待导出完成。

然后在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键单击并选择 _Import into note_。
2.  在 _Import from_ 部分，选择 <span class="tn-icon tn-brand tn-brand-google-keep"></span> _Google Keep_。
3.  上传上一步获得的 ZIP 文件。

## 支持的功能

*   基本格式（粗体、斜体、下划线）
*   [笔记颜色](../../Notes/Note%20Icons%20%26%20Colors.md)
*   笔记标题会保留（如果存在）。
    *   在 Google Keep 中，笔记通常没有标题，这种情况下会使用笔记的日期和时间作为标题。
*   待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
*   创建日期和修改日期会保留。

## 限制

目前以下信息不会被导入：

*   标签会被忽略。
*   固定、归档或删除状态不会被保留，所有笔记都按相同方式处理。

## 报告问题

从 Google Keep 导入笔记时，你可能会遇到笔记导入方式方面的一些问题，或者可能缺少某些信息。在这种情况下，请考虑 [报告问题](../../../Troubleshooting/Reporting%20issues.md)。

报告此类问题时，请确保提供以下信息：

*   需要提供笔记样本，以便更好地了解发生了什么。
    *   由于 Google Keep 没有单条笔记导出功能，请解压 Google Takeout ZIP 并复制与问题笔记对应的文件（`.html`、`.json` 以及你能识别的任何附件）。
*   一张截图，包含导入前的原始外观和导入后的外观。