# 列表

文本笔记支持三种类型的列表：

*   <span class="tn-icon cke cke-bulleted-list"></span> 项目符号列表（也称为无序列表）。
*   <span class="tn-icon cke cke-numbered-list"></span> 编号列表（或有序列表）。
*   <span class="tn-icon cke cke-todo-list"></span> 待办列表

对于项目符号列表和编号列表，可以通过按下 <span class="tn-icon cke cke-dropdown-arrow"></span> 图标来配置替代标记，例如方块或罗马数字编号。对于编号列表，还可以指定起始编号或是否按倒序计数。在 <a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动端前端</a> 上，这些选项位于 _列表 ›_ 按钮所在的行中，当光标位于列表中时会显示该按钮；其 _列表类型_ 按钮还可以将列表转换为另一种类型，包括待办列表。

## 键盘交互

*   创建新列表：
    *   项目符号列表：以 `*` 或 `-` 后跟一个空格开始一行；
    *   编号列表：以 `1.` 或 `1)` 后跟一个空格开始一行；
    *   待办列表：以 `- [ ]` 表示未勾选项目，或以 `[x]` 表示已勾选项目开始一行。
*   要在列表中创建新项目，请按 <kbd>Enter</kbd>。
*   要在列表项内创建空行，请按 <kbd>Shift</kbd>+<kbd>Enter</kbd>。
*   要退出列表，请按两次 <kbd>Enter</kbd>。
*   要合并两个列表，只需删除它们之间的间隙。
*   要创建嵌套列表，只需使用 <span class="tn-icon cke cke-indent"></span> 按钮（参见 <a class="reference-link" href="Other%20features.md">其他功能</a> 中的 _缩进_）或 <kbd>Tab</kbd> 键。要减少当前元素的嵌套层级，请按 <kbd>Shift</kbd>+<kbd>Tab</kbd>。

## 列表中的标题、代码块

可以按如下方式在列表中添加内容级块，例如标题、代码块、表格：

<table>
    <tbody>
        <tr>
            <td>1</td>
            <td><img src="2_Lists_image.jpg"></td>
            <td>首先，创建一个列表。</td>
        </tr>
        <tr>
            <td>2</td>
            <td><img src="4_Lists_image.jpg"></td>
            <td>按 Enter 创建新的列表项。</td>
        </tr>
        <tr>
            <td>3</td>
            <td><img src="1_Lists_image.jpg"></td>
            <td>按 Backspace 去除项目符号。注意光标位置。</td>
        </tr>
        <tr>
            <td>4</td>
            <td><img class="image_resized" style="aspect-ratio:676/112;width:98.29%;" src="5_Lists_image.jpg" width="676" height="112"></td>
            <td>此时，插入任何所需的块级项目，例如代码块。</td>
        </tr>
        <tr>
            <td>5</td>
            <td><img class="image_resized" style="aspect-ratio:675/129;width:94.22%;" src="3_Lists_image.jpg" width="675" height="129"></td>
            <td>要继续添加新的项目符号，请按 Enter 直到光标移动到新的空白位置。</td>
        </tr>
        <tr>
            <td>6</td>
            <td><img class="image_resized" style="aspect-ratio:675/129;width:100%;" src="Lists_image.jpg" width="675" height="129"></td>
            <td>再按一次 Enter 创建新的项目符号。</td>
        </tr>
    </tbody>
</table>

同样的原理适用于所有三种列表类型（项目符号、编号和待办）。

## 对齐

列表项可以居中或右对齐，可以通过格式工具栏中的文本对齐按钮，或通过对齐包含该列表的 <a class="reference-link" href="Tables.md">表格</a> 单元格来实现。项目符号、编号或复选框随后会随项目文本一起移动。

## 待办列表

参见 <a class="reference-link" href="To-do%20Lists.md">待办列表</a>。

## 可折叠列表

从 Trilium v0.104.0 开始，可以折叠嵌套的列表项。这适用于项目符号列表、编号列表以及待办列表。

要折叠或展开具有嵌套子项的列表项：

*   使用鼠标，将光标移到列表项上，其左侧会出现一个箭头。点击它将在折叠和展开之间切换。
*   对于项目符号列表和编号列表，也可以直接点击标记（例如项目符号或编号）而不是箭头来折叠或展开它。这不适用于待办列表，因为这样会切换待办状态。
*   按 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Enter</kbd>，将切换光标位置处项目的折叠/展开状态。

注意事项：

*   折叠的项目始终显示箭头以指示其状态。
*   折叠状态保存在笔记级别，并在各实例之间同步，这意味着在刷新或重新打开应用程序后它会恢复。
*   折叠状态也会持久化在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Import%20%26%20Export.md">导入 &amp; 导出</a> 中，但仅限 HTML 格式。Markdown 导出不会保留折叠状态。
*   可折叠项目符号仅存在于可编辑文本笔记的上下文中。只读列表将始终完全展开。
*   列表项在编辑时会自动展开，以避免在隐藏区域中键入。