# 代码片段
代码片段与<a class="reference-link" href="../Templates.md">模板</a>密切相关，但代码片段并非定义整个笔记的内容，而是一段可复用的代码，可以轻松插入到<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记中。

## 创建代码片段

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中：

1.  右键单击要放置代码片段的笔记。
2.  选择 _插入子笔记_。
3.  选择 _更多_ → _代码片段_。

然后只需在笔记中输入所需的代码并设置正确的语言模式。

笔记的标题将成为代码片段的标题。可选地，你可以在<a class="reference-link" href="../Attributes/Promoted%20Attributes.md">提升属性</a>部分添加描述。

## 插入代码片段

要插入代码片段，输入 <kbd>/</kbd> 后跟其标题的首字母，然后从列表中选择它。输入 `/snippet` 会列出笔记中所有可用的代码片段。这同样适用于就地编辑的内嵌代码笔记或 Markdown 笔记，参见<a class="reference-link" href="../../Note%20Types/Text/Include%20Note.md">包含笔记</a>。

> [!IMPORTANT]
> 仅列出语言模式与当前代码笔记匹配的代码片段。例如，CSS 代码笔记只显示 CSS 代码片段，而不显示 JavaScript 代码片段。例外情况是设置为“纯文本”的代码片段，它们在<a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a>笔记以及任何代码笔记中均可用，无论其语言模式如何。

## 限制

*   与<a class="reference-link" href="../Templates.md">模板</a>不同，代码片段不能限定于特定的[工作区](../../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md)。