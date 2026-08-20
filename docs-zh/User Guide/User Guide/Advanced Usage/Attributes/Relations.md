# 关系

关系与[标签](Labels.md)类似，但它的值不是文本，而是指向另一条笔记。

## 常见用例

*   **个人使用的元数据关系**：例如，将书籍笔记链接到作者笔记。  
    这可以与<a class="reference-link" href="Promoted%20Attributes.md">提升的属性</a>结合使用，使其显示更加用户友好。
*   **配置**：用于配置某些笔记，如<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>，或配置<a class="reference-link" href="../Sharing.md">分享</a>或<a class="reference-link" href="../Templates.md">模板</a>（参见下方列表）。
*   **脚本编写**：将脚本附加到与笔记相关的事件或条件上。

## 使用可视化编辑器创建关系

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>中的_自有属性_部分。
2.  点击右侧的 + 按钮（_添加新属性_）。
3.  选择_添加新关系_以创建关系。

> [!TIP]
> 如果您更喜欢键盘快捷键，请在聚焦于笔记或_自有属性_部分时按 <kbd>Alt</kbd>+<kbd>L</kbd> 以显示可视化编辑器。

在可视化编辑器中：

*   设置所需的名称
*   设置目标笔记（要指向的笔记）。与标签不同，关系不能没有目标笔记。
*   如果标签也应被子笔记继承，请勾选_可继承_。更多信息请参阅<a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。

## 手动创建关系

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>的_自有属性_部分中：

*   要创建名为 `myRelation` 的关系：
    *   首先输入 `~myRelation=@` 。
    *   之后，应出现一个自动补全框。
    *   输入要指向的笔记的标题，然后按 <kbd>Enter</kbd> 确认（或点击所需的笔记）。
    *   或者，从<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中复制一条笔记，然后粘贴到 `=` 符号后面（在这种情况下，不要输入 `@` ）。
*   要创建可继承的关系，请按照上述相同步骤操作，但将 `~myRelation` 写为 `~myRelation(inheritable)`。

## 预定义关系

这些关系受 Trilium 支持并在内部使用。

| 标签 | 描述 |
| --- | --- |
| `runOn*` | 参见<a class="reference-link" href="../../Scripting/Backend%20scripts/Backend%20Events.md">事件</a> |
| `template` | 笔记的属性将被继承，即使没有父子关系；如果实例笔记为空，笔记的内容和子树将被添加到实例笔记中。详见文档。 |
| `template:newNoteDefaultParent` | 设置在模板笔记上，指向当未选择其他位置时，从模板创建的笔记所放置的笔记；如果设置多次，则笔记会被克隆到每个目标中。参见<a class="reference-link" href="../Templates.md">模板</a>。 |
| `inherit` | 笔记的属性将被继承，即使没有父子关系。参见<a class="reference-link" href="../Templates.md">模板</a>了解类似概念。参见文档中的<a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。 |
| `renderNote` | <a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>类型的笔记将使用代码笔记（HTML 或脚本）进行渲染，并且必须使用此关系指向应渲染哪个笔记。 |
| `widget` | 用于自定义<a class="reference-link" href="../../Scripting/Frontend%20Basics/Launch%20Bar%20Widgets.md">启动栏小组件</a>的上下文中，以引用将要渲染的小组件。 |
| `shareCss` | 将被注入到分享页面中的 CSS 笔记。CSS 笔记也必须位于共享子树中。也可以考虑使用 `shareHiddenFromTree` 和 `shareOmitDefaultCss`。 |
| `shareJs` | 将被注入到分享页面中的 JavaScript 笔记。JS 笔记也必须位于共享子树中。也可以考虑使用 `shareHiddenFromTree`。 |
| `shareHtml` | 将被注入到分享页面中由 `shareHtmlLocation` 标签指定位置的 HTML 笔记。HTML 笔记也必须位于共享子树中。也可以考虑使用 `shareHiddenFromTree`。 |
| `shareTemplate` | 用作显示共享笔记模板的内嵌 JavaScript 笔记。如果未设置，则回退到默认模板。也可以考虑使用 `shareHiddenFromTree`。 |
| `shareFavicon` | 在共享页面中设置的网站图标笔记。通常您希望将其设置为共享根笔记并使其可继承。网站图标笔记也必须位于共享子树中。也可以考虑使用 `shareHiddenFromTree`。 |