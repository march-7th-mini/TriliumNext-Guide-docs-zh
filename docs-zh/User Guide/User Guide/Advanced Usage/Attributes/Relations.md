# 关系

关系类似于[标签](Labels.md)，但它不是拥有文本值，而是指向另一条笔记。

## 常见用例

*   **个人使用的元数据关系**：例如，将书籍笔记链接到作者笔记。
    这可以与<a class="reference-link" href="Promoted%20Attributes.md">提升属性</a>结合使用，使其显示更加用户友好。
*   **配置**：用于配置某些笔记，例如<a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>，或配置<a class="reference-link" href="../Sharing.md">分享</a>或<a class="reference-link" href="../Templates.md">模板</a>（参见下方列表）。
*   **脚本**：将脚本附加到与笔记相关的事件或条件上。

## 使用可视化编辑器创建关系

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Attributes%20tab.md">属性选项卡</a>。
2.  按下 _自有属性_ 区域右侧的 <span class="tn-icon bx bx-plus"></span> 按钮（_添加新属性_）。
3.  选择 _添加新关系_ 来创建关系。

在可视化编辑器中，设置所需的名称和 _目标笔记_（要指向的笔记）。与标签不同，关系不能没有目标笔记。

子笔记可以继承此关系，点击该关系并勾选 _可继承_。更多信息请参见<a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。

> [!TIP]
> 或者，按下 <kbd>Alt</kbd>+<kbd>L</kbd>，这将在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中打开属性详情（与点击现有属性时的视图相同）。

## 手动创建关系

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中，按下 <span class="tn-icon bx bx-list-check"></span> 按钮以显示属性列表。

*   要创建一个名为 `myRelation` 的关系：
    1.  点击输入框使其获得焦点。
    2.  输入 `~myRelation=@` 。
    3.  之后，应出现一个自动补全框。
    4.  输入要指向的笔记标题，然后按 <kbd>Enter</kbd> 确认（或点击所需的笔记）。
    5.  或者从<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中复制一条笔记，然后粘贴到 `=` 符号之后（在这种情况下不需要 `@` ）。
*   要创建可继承的关系，请按照前面描述的相同步骤操作，但将 `~myRelation` 替换为 `~myRelation(inheritable)`。

## 预定义关系

这些关系由 Trilium 内部支持和使用的。

| 标签 | 描述 |
| --- | --- |
| `runOn*` | 参见<a class="reference-link" href="../../Scripting/Backend%20scripts/Backend%20Events.md">后端事件</a> |
| `template` | 即使没有父子关系，笔记的属性也会被继承；如果实例笔记为空，笔记的内容和子树将被添加到实例笔记中。详情请参见文档。 |
| `template:newNoteDefaultParent` | 在模板笔记上设置，指向当未选择其他位置时，从模板创建的笔记所放置的笔记；当设置多次时，笔记将被克隆到每个目标中。参见<a class="reference-link" href="../Templates.md">模板</a>。 |
| `inherit` | 即使没有父子关系，笔记的属性也会被继承。类似概念请参见<a class="reference-link" href="../Templates.md">模板</a>。文档请参见<a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。 |
| `renderNote` | <a class="reference-link" href="../../Note%20Types/Render%20Note.md">渲染笔记</a>类型的笔记将使用代码笔记（HTML 或脚本）进行渲染，需要使用此关系指向应渲染的笔记 |
| `widget` | 在自定义<a class="reference-link" href="../../Scripting/Frontend%20Basics/Launch%20Bar%20Widgets.md">启动栏小组件</a>的上下文中使用，用于引用将要渲染的小组件。 |
| `shareCss` | 将被注入到分享页面的 CSS 笔记。CSS 笔记也必须位于共享子树中。建议同时使用 `shareHiddenFromTree` 和 `shareOmitDefaultCss`。 |
| `shareJs` | 将被注入到分享页面的 JavaScript 笔记。JS 笔记也必须位于共享子树中。建议使用 `shareHiddenFromTree`。 |
| `shareHtml` | 将被注入到分享页面中由 `shareHtmlLocation` 标签指定位置的 HTML 笔记。HTML 笔记也必须位于共享子树中。建议使用 `shareHiddenFromTree`。 |
| `shareTemplate` | 用作显示共享笔记模板的嵌入式 JavaScript 笔记。回退到默认模板。建议使用 `shareHiddenFromTree`。 |
| `shareFavicon` | 在共享页面中设置的网站图标笔记。通常您希望将其设置到共享根节点并使其可继承。网站图标笔记也必须位于共享子树中。建议使用 `shareHiddenFromTree`。 |