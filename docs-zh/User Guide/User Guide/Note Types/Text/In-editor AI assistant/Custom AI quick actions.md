# 自定义 AI 快捷操作

_快捷操作_ 是<a class="reference-link" href="../In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>针对<a class="reference-link" href="../../Text.md">文本</a>笔记的一项功能，可根据定义的提示词自动触发大语言模型建议。内置快捷操作带有预定义的提示词，但您也可以定义自己的快捷操作。

## 创建自定义快捷操作

在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中：

1.  右键单击要放置文本片段的位置。
2.  选择 _插入子笔记_。
3.  选择 _AI 快捷操作_。

之后，只需在笔记内容中输入所需的提示词即可。文本的格式设置方式与普通文本笔记相同，并将以 Markdown 格式传递给大语言模型。

笔记的标题将成为快捷操作的标题。

请注意：

*   <a class="reference-link" href="../../Code.md">代码</a>笔记同样适用。
*   空笔记将被忽略。
*   <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/Notes/Archived%20Notes.md">已归档笔记</a>也被排除在外。

## 使用快捷操作

定义快捷操作后，该操作将出现在 _快捷操作_ 下拉菜单中名为 _自定义_ 的分组下。