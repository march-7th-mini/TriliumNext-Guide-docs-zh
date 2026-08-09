# 反链

链接从一个笔记指向另一个笔记；_反链_是从另一端看到的同一连接：指向当前笔记的笔记列表。

反链是自动维护的，并且从这一侧看是只读的。当创建反链的笔记移除该链接时，反链就会消失；它不能从被指向的笔记中删除。

## 什么算作反链

任何指向当前笔记的<a class="reference-link" href="Internal%20(reference)%20links.md">内部（引用）链接</a>，这涵盖两种截然不同的情况：

*   Trilium 代表你维护的关系。
    *   最常见的是 `internalLink`，每当一个笔记通过其文本中的<a class="reference-link" href="Internal%20(reference)%20links.md">内部（引用）链接</a>引用另一个笔记时创建。
    *   嵌入图片（`imageLink`）、关系图连接（`relationMapLink`）和笔记包含（`includeNoteLink`）的工作方式相同。
*   你自己定义的关系。
    *   如果另一个笔记带有指向当前笔记的 `~author` 关系，该笔记也会列在这里。

来自<a class="reference-link" href="../../Saved%20Search.md">已保存搜索</a>的关系被排除在外，因为搜索存储了一个 `ancestor` 关系，否则会将其每个结果都列为反链。

> [!NOTE]
> 只有某些笔记类型会扫描其内容中的链接：<a class="reference-link" href="../../Text.md">文本</a>、<a class="reference-link" href="../../Markdown.md">Markdown</a>、<a class="reference-link" href="../../Relation%20Map.md">关系图</a>和<a class="reference-link" href="../../../AI.md">AI</a>对话。写在<a class="reference-link" href="../../Code.md">代码</a>笔记中的链接不会被注册，也不会作为反链出现在目标笔记上。在代码笔记上手动设置的关系仍然算数。

## 条目如何显示

每个条目都标明引用来源的笔记名称，后跟以下之一：

*   **周围内容的摘录**，链接本身会高亮显示。这适用于<a class="reference-link" href="../../Text.md">文本</a>笔记和<a class="reference-link" href="../../../AI.md">AI</a>对话笔记。链接周围会引用大约 200 个字符的上下文，如果周围文本较长则用省略号截断，图片会被省略。
*   **关系的名称**，适用于所有其他无法引用来源的笔记类型。这适用于<a class="reference-link" href="../../Relation%20Map.md">关系图</a>笔记以及任何带有你自己定义的关系的笔记。

一个笔记每次引用都会列出一次，因此一个三次链接到当前笔记的笔记会占据三行。

值得注意的是：

*   对于 AI 对话笔记，只引用助手自己的文本。纯粹通过工具调用到达该笔记的对话没有可引用的内容，而是按关系名称列出。
*   摘录仅为大约前 50 个来源生成。对于被大量引用的笔记，其余条目会回退到显示关系名称。

## 反链在哪里显示

*   在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Connections%20tab.md">连接选项卡</a>的<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中，作为一个专门的区域。
*   在<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout/Status%20bar.md">状态栏</a>中作为显示反链数量的徽章。该徽章仅在笔记正常读取时（不在修订或附件视图中）且至少有一个反链时出现；按下它会打开上面的区域。
*   入站链接也会绘制在链接图上，参见<a class="reference-link" href="../../../Advanced%20Usage/Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记图（链接图、树图）</a>。
*   在旧布局中，反链显示为<a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域中的一个专用按钮。