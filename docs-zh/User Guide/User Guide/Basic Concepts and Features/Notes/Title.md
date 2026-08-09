# 标题

除了内容之外，**标题**是[笔记](../Notes.md)的两个主要属性之一。它是显示在每个笔记顶部可编辑字段中的简短、人类可读的名称，并且它是在整个界面中标识该笔记的方式（在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>、标签页、<a class="reference-link" href="../UI%20Elements/New%20Layout/Breadcrumb.md">面包屑</a>以及<a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>中）。

在内部，笔记通过唯一的<a class="reference-link" href="../../Advanced%20Usage/Note%20ID.md">笔记 ID</a> 而非其标题来标识，因此标题纯粹是为了方便您使用。这带来了一些影响：

*   **标题不必唯一。** 您可以拥有任意数量共享相同标题的笔记，而不会产生冲突。
*   **重命名笔记永远不会破坏指向它的链接。** 笔记之间的链接指向底层笔记，因此更改标题会使现有链接保持完整（它们只会显示新标题）。
*   **标题可以留空。** 没有标题的笔记会显示占位符（_在此输入笔记标题…_），但除此之外是完全有效的。

此外：

*   标题长度没有限制，但在导出时标题可能会被截断。
*   没有禁止使用的符号，导出时不受支持的字符将被截断。
*   导出为 ZIP 文件时，元文件将包含完整标题，Trilium 在再次导入时会识别该标题。

### 编辑标题

要重命名笔记，只需点击标题字段并输入即可。更改会在您输入时自动保存。

您也可以直接从<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>开始编辑标题，方法是选择笔记并按 <kbd>Enter</kbd>（请参阅<a class="reference-link" href="../Keyboard%20Shortcuts.md">键盘快捷键</a>中的 _编辑笔记标题_），这会将焦点聚焦到活动笔记的标题字段上。

> [!NOTE]
> 标题可以包含任何字符，包括 Unicode 和表情符号。出于安全考虑，标题中的任何 HTML 都会被自动剥离，因此标题始终被视为纯文本。

### 在标题和内容之间轻松导航

当光标位于标题字段中时，按 <kbd>Enter</kbd> 会将焦点移动到笔记的内容中。对于<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>笔记，这还会在文档的最顶部插入一个新的空段落，以便您可以立即开始书写——就像其他笔记应用一样。

这使得您可以创建笔记、输入标题、按 <kbd>Enter</kbd>，然后直接继续输入正文，而无需使用鼠标。

### 处理新笔记

当您创建新笔记时，它会获得一个默认标题（_新笔记_），该标题会被预先选中，因此您可以立即输入名称来替换它。新笔记的默认标题可以按分区自定义——请参阅<a class="reference-link" href="../../Advanced%20Usage/Default%20Note%20Title.md">默认笔记标题</a>。

如果您最终决定不想要该笔记，在新建笔记的标题仍处于聚焦状态时按 <kbd>Escape</kbd> 将丢弃它。

### 自动生成的标题

某些笔记的标题是自动分配的，而不是手动输入的：

*   <a class="reference-link" href="../../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记</a>中的**日、周、月和年笔记**根据可配置的日期模式命名。
*   <a class="reference-link" href="../../Note%20Types/Saved%20Search.md">已保存搜索</a>笔记根据其执行的搜索命名。
*   当笔记被复制时，副本的标题会附加一个后缀，以区别于原始笔记。

### 受保护的笔记

对于<a class="reference-link" href="Protected%20Notes.md">受保护的笔记</a>，标题_不_加密——只有内容加密。因此，即使没有活动的受保护会话，标题在树和标签页中仍然可见。但是，在锁定时，标题字段是只读的，在您输入密码之前无法编辑。

## 受保护的笔记

<a class="reference-link" href="Protected%20Notes.md">受保护的笔记</a>的标题与其内容一起加密。在输入密码之前，Trilium 无法解密标题，因此它会显示为 `[protected]`，并且标题无法修改。

一旦您输入密码并且受保护会话处于活动状态，真实标题就会被解密并显示，并且可以再次编辑。