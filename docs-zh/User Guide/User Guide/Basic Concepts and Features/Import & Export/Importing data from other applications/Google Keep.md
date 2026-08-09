# Google Keep

Trilium 可以从 Google Keep 导入笔记，并保留其结构和格式。

## 导入流程

Google Keep 没有原生的导出功能，但 Google Takeout 允许您下载包含所有笔记的 ZIP 文件。

第一步是下载您的 Google Keep 数据：

1.  导航至 [takeout.google.com](https://takeout.google.com/)。
2.  在 _创建新导出_ 部分，点击 _全部取消选择_。
3.  在要导出的数据列表中，勾选 _Keep_。
4.  滚动到底部，选择 _下一步_。
5.  在 _选择文件类型、频率和目的地_ 中，确保设置以下选项：
    1.  _传输到_ 设置为 _通过电子邮件发送下载链接_。
    2.  _频率_ 设置为 _仅导出一次_。
    3.  _文件类型_ 设置为 _.zip_。
    4.  _文件大小_ 可以保持为 _2 GB_。
6.  点击 _创建导出_ 并等待导出完成。

然后在 Trilium Notes 中：

1.  在 <a class="reference-link" href="../../UI%20Elements/Note%20Tree.md">笔记树</a> 中，右键点击并选择 _导入到笔记_。
2.  在 _从导入_ 部分，选择 _Google Keep_。
3.  上传上一步获得的 ZIP 文件。

## 支持的功能

*   基本格式（粗体、斜体、下划线）
*   [笔记颜色](../../Notes/Note%20Icons%20%26%20Colors.md)
*   笔记标题会被保留（如果存在）。
    *   在 Google Keep 中，笔记通常没有标题，这种情况下会使用笔记的日期和时间作为标题。
*   待办事项列表
*   <a class="reference-link" href="../../../Note%20Types/Text/Images.md">图片</a> 和 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
*   创建和修改日期会被保留。

## 限制

目前以下信息不会被导入：

*   标签会被忽略。
*   置顶、已归档或已删除状态不会被保留，所有笔记都同等对待。

## 报告问题

从 Google Keep 导入笔记时，您可能会遇到一些笔记导入方式的问题，或者可能缺少某些信息。在这种情况下，请考虑[报告问题](../../../Troubleshooting/Reporting%20issues.md)。

报告此类问题时，请务必提供以下信息：

*   需要提供笔记样本来更好地了解发生了什么。
    *   由于 Google Keep 没有单笔记导出功能，请解压 Google Takeout ZIP 文件，并复制与问题笔记对应的文件（`.html`、`.json` 以及任何您能识别的附件）。
*   提供导入前原始外观和导入后外观的截图。