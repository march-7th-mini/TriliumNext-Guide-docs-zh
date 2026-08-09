# SQL 控制台

> [!重要]
> 从 v0.104.0 版本开始，后端脚本默认禁用，以减少攻击面。更多信息请参阅 <a class="reference-link" href="../../../Scripting/Security.md">安全</a>。

SQL 控制台是 Trilium 内置的数据库编辑器。

可以通过 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> → 高级 → 打开 SQL 控制台 来访问它。

![](SQL%20Console_image.png)

### 交互

*   将鼠标悬停在文档顶部列出的某个表上，将显示其列及其数据类型。
*   一次只能运行一条 SQL 语句。
*   要运行该语句，请点击 _执行_ 图标。
*   对于返回结果的查询，数据将显示在表格中。
*   对于语句（例如 `INSERT`、`UPDATE`），将显示受影响的行数。

<figure class="image"><img style="aspect-ratio:1124/571;" src="2_SQL Console_image.png" width="1124" height="571"></figure>

### 与表格交互

执行查询后，将显示一个包含结果的表格：

*   点击列标题可以按升序或降序排序。
*   每列下方都有一个输入框，可以按文本进行过滤。
*   按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 将当前单元格复制到剪贴板。
*   可以通过拖动或按住 <kbd>Shift</kbd> + 方向键来选择多个单元格。
*   出于性能原因，结果会分页显示。可以使用表格底部的控件来浏览页面。

### 已保存的 SQL 控制台

SQL 查询或命令可以保存到专用的笔记中。

为此，只需编写查询，然后点击 ![](1_SQL%20Console_image.png) 按钮。保存后，该笔记默认会出现在 <a class="reference-link" href="../../Advanced%20Showcases/Day%20Notes.md">每日笔记</a> 中。可以通过分配 `#sqlConsoleHome` [标签](../../Attributes/Labels.md) 来更改已保存查询的默认位置。

可以通过点击标题栏附近的笔记操作区域中的 _锁定_ 按钮（在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a> 中，或在使用旧布局时的 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a> 区域）来锁定笔记以禁止编辑。当编辑被锁定时，SQL 语句将被隐藏。