# 自定义 AI 快速操作
_快速操作_ 是 <a class="reference-link" href="../In-editor%20AI%20assistant.md">编辑器内 AI 助手</a> 的一项功能，适用于 <a class="reference-link" href="../../Text.md">文本</a> 笔记，它会根据定义的提示自动触发大语言模型建议。内置快速操作附带预定义的提示，但也可以定义自己的快速操作。

## 创建自定义快速操作

在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中：

1.  右键单击要放置快速操作的笔记。
2.  选择 _插入子笔记_。
3.  选择 _更多_ → _AI 快速操作_。该条目仅在启用 AI 时出现。

之后，只需在笔记内容中输入所需的提示。文本可以像普通文本笔记一样进行格式化，并会以 Markdown 形式传递给大语言模型。

笔记的标题将成为快速操作的标题。

注意事项：

*   <a class="reference-link" href="../../Code.md">代码</a> 笔记同样适用。
*   空笔记会被忽略。
*   <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Archived%20Notes.md">存档笔记</a> 也会被排除。

## 使用快速操作

定义快速操作后，该操作将出现在 _快速操作_ 下拉菜单下的 _自定义_ 分组中。