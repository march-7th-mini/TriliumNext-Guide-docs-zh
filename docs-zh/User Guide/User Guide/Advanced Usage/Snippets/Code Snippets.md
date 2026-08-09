# 代码片段
代码片段与<a class="reference-link" href="../Templates.md">模板</a>密切相关，但片段并非定义整个笔记的内容，而是一段可复用的代码，可以轻松插入到<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记中。

## 创建代码片段

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中：

1.  右键单击要放置片段的位置的笔记。
2.  选择 **插入子** _笔记_。
3.  选择 _**代码片段**_。

然后只需在笔记中输入所需代码并设置正确的语言模式。

笔记的标题即成为片段的标题。可选地，您可以在<a class="reference-link" href="../Attributes/Promoted%20Attributes.md">提升属性</a>部分添加描述。

## 插入片段

要插入片段，请键入 `/snippet` 并从下拉菜单中选择其标题。

> [!重要]
> 仅列出语言模式与当前代码笔记匹配的代码片段。例如，CSS 代码笔记仅显示 CSS 片段，而不显示 JavaScript 片段。例外情况是设置为“纯文本”的片段，这些片段可在<a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a>笔记以及任何代码笔记中使用，无论其语言模式如何。

## 限制

*   与<a class="reference-link" href="../Templates.md">模板</a>不同，片段不能限制在特定的[工作区](../../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md)中。