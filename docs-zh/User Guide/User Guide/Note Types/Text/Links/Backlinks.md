# 反链
一个链接从一条笔记指向另一条笔记；而_反链_是从另一端看到的同一连接：即引用当前笔记的笔记列表。

反链是自动维护的，并且从这一端看是只读的。当创建反链的笔记移除该链接时，反链就会消失；它无法从被指向的笔记中删除。

## 什么算作反链

任何指向当前笔记的<a class="reference-link" href="Internal%20(reference)%20links.md">内部（引用）链接</a>，这涵盖两种相当不同的情况：

*   Trilium 代你维护的关系。
    *   最常见的是 `internalLink`，当一条笔记通过其文本中的<a class="reference-link" href="Internal%20(reference)%20links.md">内部（引用）链接</a>引用另一条笔记时创建。
    *   嵌入的图片（`imageLink`）、关系图连接（`relationMapLink`）和笔记包含（`includeNoteLink`）的工作方式相同。
*   你自己定义的关系。
    *   如果另一条笔记有指向当前笔记的 `~author`，该笔记也会列在这里。

来自<a class="reference-link" href="../../Saved%20Search.md">保存的搜索</a>的关系会被排除，因为搜索会存储一个 `ancestor` 关系，否则会将其每个结果都列为反链。

> [!NOTE]
> 只有部分笔记类型的内容会被扫描以查找链接：<a class="reference-link" href="../../Text.md">文本</a>、<a class="reference-link" href="../../Markdown.md">Markdown</a>、<a class="reference-link" href="../../Relation%20Map.md">关系图</a>和<a class="reference-link" href="../../../AI.md">AI</a> 对话。写在<a class="reference-link" href="../../Code.md">代码</a>笔记内的链接不会被登记，也不会在目标笔记上显示为反链。在代码笔记上手动设置的关系仍然有效。

## 条目如何显示

每个条目都会指明引用来自哪条笔记，后面跟着以下之一：

*   周围内容的**摘录**，其中链接本身会被高亮显示。这适用于<a class="reference-link" href="../../Text.md">文本</a>笔记和<a class="reference-link" href="../../../AI.md">AI</a> 对话笔记。链接周围大约引用 200 个字符的上下文，当周围文本更长时用省略号截断，图片则被省略。
*   **关系的名称**，适用于所有其他无法引用来源的笔记类型。这适用于<a class="reference-link" href="../../Relation%20Map.md">关系图</a>笔记以及任何带有你自己定义的关系的笔记。

一条笔记每进行一次引用就会被列出一次，因此一条笔记如果三次链接到当前笔记，就会占据三行。

值得注意的是：

*   对于 AI 对话笔记，只引用助手自己的叙述。如果一次对话纯粹通过工具调用到达该笔记，则没有可引用的内容，会改为按关系名称列出。
*   摘录只为大约前 50 个来源生成。在被大量引用的笔记上，其余条目会回退为显示关系名称。

## 反链显示在哪里

*   在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Connections%20tab.md">连接选项卡</a>（位于<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>）中，作为一个专门的区块。
*   作为<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout/Status%20bar.md">状态栏</a>中的一个徽章，显示反链的数量。该徽章仅在笔记被正常阅读时（不在修订或附件视图中）且至少有一条反链时出现；按下它会打开上面的区块。
*   传入链接也会绘制在链接图上，参见<a class="reference-link" href="../../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记图（链接图、树图）</a>。
*   在旧版布局中，反链在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域中显示为一个专门的按钮。