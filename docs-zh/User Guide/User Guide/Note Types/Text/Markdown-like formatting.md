# 类 Markdown 格式
类 Markdown 格式允许通过输入 Markdown 等效语法来插入一些基本格式。请注意，这并不意味着 <a class="reference-link" href="../Text.md">文本</a> 笔记支持 Markdown，这些只是一些便捷的快捷方式。

要将更复杂的格式导入文本笔记，请考虑使用 [_从 Markdown 导入_](Other%20features.md) 功能。如需完整的 Markdown 笔记导入，请考虑使用专门的 [导入](../../Basic%20Concepts%20and%20Features/Import%20%26%20Export/Markdown.md) 功能。

*   对于 [标题：](General%20formatting.md)
    *   `##` 用于二级标题（一级标题保留给笔记标题）。
    *   `###` 用于三级标题
    *   `####` 用于四级标题
    *   `#####` 用于五级标题
    *   `######` 用于六级标题
*   对于 <a class="reference-link" href="General%20formatting.md">常规格式</a>：
    *   **加粗**：输入 `**文本**` 或 `__文本__`
    *   _斜体_：输入 `*文本*` 或 `_文本_`
    *   ~~删除线~~：输入 `~~文本~~`
*   对于 <a class="reference-link" href="Lists.md">列表</a>：
    *   项目符号列表：以 `*` 或 `-` 开头，后跟一个空格；
    *   编号列表：以 `1.` 或 `1)` 开头，后跟一个空格；
    *   待办事项列表：以 `[ ]` 开头表示未选中项，或以 `[x]` 开头表示选中项。
*   对于 [块引用](Block%20quotes%20%26%20admonitions.md)，按 `>`，后跟一个空格。
*   对于 <a class="reference-link" href="Developer-specific%20formatting/Code%20blocks.md">代码块</a>，输入 ` ``` `。
*   对于 [水平线](Other%20features.md)，输入 `---`。
*   对于 [警示框](Block%20quotes%20%26%20admonitions.md)：
    *   `!!! note`
    *   `!!! tip`
    *   `!!! important`
    *   `!!! caution`
    *   `!!! warning`
    *   以 `!!!` 开头输入任何其他文本将插入一个包含该文本的笔记警示框。
*   对于 [表情符号](Insert%20buttons.md)，输入 `:` 后跟表情符号名称以触发自动补全。

如果不希望自动格式化，请按 <kbd>Ctrl</kbd> + <kbd>Z</kbd> 将文本恢复为原始形式。