# 代码片段

代码片段与<a class="reference-link" href="../Templates.md">模板</a>密切相关，但它不是定义整个笔记的内容，而是一段可复用的代码，可以方便地插入到<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记中。

## 创建代码片段

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中：

1. 右键点击你想要放置代码片段的笔记。
2. 选择 _插入子笔记_。
3. 选择 _更多_ → _代码片段_。

然后只需在笔记中输入所需的代码，并设置正确的语言模式。

笔记的标题将成为代码片段的标题。你还可以选择在<a class="reference-link" href="../Attributes/Promoted%20Attributes.md">提升属性</a>部分添加描述。

## 插入代码片段

要插入代码片段，输入 `/snippet` 并从下拉列表中选择其标题。

> [!IMPORTANT]
> 只有语言模式与当前代码笔记匹配的代码片段才会被列出。例如，CSS 代码笔记只显示 CSS 代码片段，而不显示 JavaScript 代码片段。例外情况是设置为“纯文本”的代码片段，它们可以在<a class="reference-link" href="../../Note%20Types/Markdown.md">Markdown</a>笔记以及任何代码笔记中使用，无论其语言模式如何。

## 限制

*   与<a class="reference-link" href="../Templates.md">模板</a>不同，代码片段不能限定于特定的[工作区](../../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md)。