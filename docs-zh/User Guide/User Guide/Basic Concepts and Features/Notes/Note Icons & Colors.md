# 笔记图标与颜色
## 图标

<figure class="image image-style-align-right image_resized" style="width:48.4%;"><img style="aspect-ratio:1089/995;" src="Note Icons &amp; Colors_image.png" width="1089" height="995"></figure>

图标有助于区分笔记，并显示在笔记标题附近，以及诸如<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>、<a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>或<a class="reference-link" href="../Navigation/Jump%20to%20%26%20command%20palette.md">跳转与命令面板</a>等各个位置。

编辑笔记时，点击标题旁边的图标即可弹出选择图库。

图标可以通过使用<a class="reference-link" href="../../Advanced%20Usage/Templates.md">模板</a>或<a class="reference-link" href="../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>来继承。

> [!NOTE]
> 在技术层面，图标是通过 `iconClass` 属性设置的，该属性会为笔记添加一个 CSS 类。例如，`#iconClass="bx bx-calendar"` 将显示日历图标，而不是默认的页面或文件夹图标。无需查找和记忆 CSS 类名。

## 颜色

笔记还可以带有自定义颜色。与笔记图标类似，该颜色会显示在诸如<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>和<a class="reference-link" href="../../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>等各个位置。

要设置自定义颜色，请在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击笔记，然后从预定义颜色中选择，或使用颜色选择器（最后一个选项）。

另外，也可以通过 `#color` [标签](../../Advanced%20Usage/Attributes/Labels.md)手动设置自定义颜色，其值必须是有效的十六进制颜色代码，并包含前导 `#`（例如，红色为 `#ff0000`）。该颜色可以通过<a class="reference-link" href="../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md">属性继承</a>在多个笔记之间传递。