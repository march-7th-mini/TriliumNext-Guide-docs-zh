# SQL 控制台
> [!IMPORTANT]
> 从 v0.104.0 开始，后端脚本默认被禁用，以减少攻击面。更多信息请参见 <a class="reference-link" href="../../../Scripting/Security.md">安全</a>。

SQL 控制台是 Trilium 内置的数据库编辑器。

可以通过前往 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> → 高级 → 打开 SQL 控制台来访问它。

![](SQL%20Console_image.png)

### 交互

*   将鼠标悬停在文档顶部列出的某个表上，会显示其列及数据类型。
*   一次只能运行一条 SQL 语句。
*   要运行语句，请按 _执行_ 图标。
*   对于返回结果的查询，数据将显示在表格中。
*   对于语句（例如 `INSERT`、`UPDATE`），会显示受影响的笔记数。

<figure class="image"><img style="aspect-ratio:1124/571;" src="1_SQL Console_image.png" width="1124" height="571"></figure>

### 与表格交互

执行查询后，将显示包含结果的表格：

*   点击某一列可按升序或降序排序。
*   每列下方都有一个输入字段，可按文本进行筛选。
*   按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 将当前单元格复制到剪贴板。
*   可以通过拖动或按住 <kbd>Shift</kbd> + 方向键来选择多个单元格。
*   出于性能原因，结果会分页显示。可以使用表格底部的控件在页面之间导航。

### 已保存的 SQL 控制台

SQL 查询或命令可以保存到专用笔记中。

为此，只需编写查询并按 <span class="tn-icon bx bx-save"></span> 按钮。保存后，该笔记默认会出现在 <a class="reference-link" href="../../Advanced%20Showcases/Day%20Notes.md">日记笔记</a> 中。可以通过分配 `#sqlConsoleHome` [标签](../../Attributes/Labels.md) 来更改已保存查询的默认位置。

可以通过按标题栏附近笔记操作区域中的 _锁定_ 按钮来锁定笔记以禁止编辑（在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a> 中，或者如果使用旧布局，则在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a> 区域中）。当编辑被锁定时，SQL 语句会从视图中隐藏。