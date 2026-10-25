# 内容语言与从右到左支持
![](Content%20language%20&%20Right-to-left%20support_image.jpg)

内容语言决定以下事项：

*   在浏览器中时，笔记的拼写检查。桌面安装版有专门的拼写检查部分。
*   对于阿拉伯语、希伯来语等语言，文本是否从右到左显示。
*   输入的引号如何被[自动替换](Automatic%20replacements.md)（例如英语使用 `“text”`，而某些语言使用 `«text»`）。这仅在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本_ → _单/双引号_ 设置为 _基于笔记的内容语言_ 时适用。
*   <a class="reference-link" href="In-editor%20AI%20assistant.md">编辑器内 AI 助手</a> 提供哪些语言用于翻译。
*   在[共享页面](../../Advanced%20Usage/Sharing.md)上，内容所标记的语言和文本方向，屏幕阅读器和浏览器会遵循这些设置。

## 设置单个笔记的语言

要设置 <a class="reference-link" href="../Text.md">文本</a> 笔记内容的语言，<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a> 中有一个由 <span class="tn-icon bx bx-globe"></span> 图标指示的语言选择器。

## 调整语言列表

默认情况下，未配置任何语言。要配置它们，请转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _语言与地区_ → _内容语言_，或在设置语言时选择 _配置语言..._ 项。已启用的语言按其本地名称列出，按字母顺序排序，这也是语言选择器显示它们的顺序。在此你可以：

*   通过按下 <span class="tn-icon bx bx-plus"></span> _添加语言_ 按钮（启用一个语言后变为 _添加另一种语言_）来添加语言，该按钮还会显示剩余多少种语言，然后选择它。
*   按下语言旁边的 <span class="tn-icon bx bx-x"></span> 按钮将其从列表中移除。

## 默认内容语言

没有自己语言的笔记遵循 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _语言与地区_ → _默认内容语言_。它最初设置为英语，可以设置为任何内容语言，或设置为 _基于应用程序的语言_。

如果笔记设置了语言，它始终优先于默认值。