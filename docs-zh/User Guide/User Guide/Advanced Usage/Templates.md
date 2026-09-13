# 模板
Trilium 中的模板是其他笔记（称为实例笔记）的预定义结构。为笔记分配模板会带来三个主要效果：

1.  **属性继承**：模板笔记中的所有属性都会被实例笔记[继承](Attributes/Attribute%20Inheritance.md)。即使带有 `#isInheritable=false` 的属性也会被实例笔记继承，不过只有可继承的属性才会进一步被实例笔记的子笔记继承。
2.  **内容复制**：模板笔记的内容会被复制到实例笔记，前提是实例笔记在分配模板时为空。
3.  **子笔记复制**：模板的所有子笔记会被深度复制到实例笔记。

## 示例

一个典型的例子是“Book”模板笔记，它可能包含：

*   **提升属性**：例如出版年份、作者等（参见[提升属性](Attributes/Promoted%20Attributes.md)）。
*   **大纲**：书评的大纲，包括主题、结论等部分。
*   **子笔记**：用于摘录、摘要等的附加笔记。

![模板示例](Templates_template.png)

## 实例笔记

实例笔记是与模板笔记相关联的笔记。这种关系意味着实例笔记的内容从模板初始化，并且模板中的所有属性都会被继承。

通过 UI 创建实例笔记：

![显示子笔记模板](Templates_template-create-instance-note.png)

要让模板出现在菜单中，模板笔记必须带有 `#template` 标签。不要将其与 `~template` 关系混淆，后者将实例笔记链接到模板笔记。如果你使用[工作区](../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md)，还可以用 `#workspaceTemplate` 标记模板，使其仅在工作区中显示。

模板也可以在笔记创建后通过创建指向所需模板笔记的 `~template` 关系来添加或更改。

要为子笔记指定模板，可以使用指向相应模板笔记的 `~child:template` 关系。层级深度没有限制——你可以使用 `~child:child:template`、`~child:child:child:template`，依此类推。

> [!IMPORTANT]
> 在父笔记创建后更改模板层级不会追溯应用到新创建的子笔记。  
> 例如，如果你最初使用 `~child:template`，后来改为 `~child:child:template`，它不会自动将新模板应用到孙笔记。只有笔记创建时存在的结构才会被考虑。

## 新笔记的默认父笔记

模板可以将由它创建的笔记集中到一个地方，而不是让它们落在碰巧创建的位置。为此，请在模板笔记上添加一个 `~template:newNoteDefaultParent` 关系，指向应容纳实例的笔记，例如一个 _Person_ 模板指向一个 _People_ 笔记。

多次添加该关系会将新笔记放入每个目标中，如同<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md">克隆笔记</a>。该关系也可以被继承（例如从一个包含多个模板的文件夹继承），在这种情况下，模板自身拥有的关系会替换继承的关系。默认父笔记仅从模板在树中的祖先继承：由另一个模板创建的模板不会采用该模板的默认父笔记。

当通过 _选择笔记类型_ 对话框从模板创建笔记时，会使用默认父笔记：

*   通过 <a class="reference-link" href="../Note%20Types/Text.md">Text</a> 笔记中的 `@` 补全
*   通过笔记搜索的 _创建笔记_ 或 _创建子笔记_ 选项（新标签页或<a class="reference-link" href="../Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>），但仅在设置了默认/空位置时。

从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>上下文菜单（_插入子笔记_、_在之后插入笔记_）创建实例笔记仍会在所选位置创建它。

与<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>不同（后者用于存放快速捕获的笔记直到它们被整理），默认父笔记旨在作为实例的永久位置。

## 关于笔记类型

默认情况下，新创建的笔记是 <a class="reference-link" href="../Note%20Types/Text.md">Text</a> 笔记。如果父笔记定义了指向不同类型模板（例如代码笔记）的 `child:template`，其行为取决于新笔记的创建方式：

*   如果未显式选择笔记类型（例如<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中的 + 按钮），则会应用模板，新笔记采用模板的类型和内容。
*   如果显式选择了笔记类型（例如<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> → _在之后插入笔记_ / _插入子笔记_）：
    *   如果所选类型与模板类型匹配，则应用模板。
    *   如果所选类型不同，则完全忽略模板——新笔记是所选类型的空笔记。

从创建菜单中选择特定模板始终优先于 `child:template`。

## 附加说明

从视觉角度来看，模板可以定义 `#iconClass` 和 `#cssClass` 属性，使所有实例笔记（例如书籍）显示特定的图标和 CSS 样式。

在<a class="reference-link" href="Database/Demo%20Notes.md">演示笔记</a>中进一步探索这一概念，包括<a class="reference-link" href="../Note%20Types/Relation%20Map.md">关系图</a>、<a class="reference-link" href="Advanced%20Showcases/Task%20Manager.md">任务管理器</a>和<a class="reference-link" href="Advanced%20Showcases/Day%20Notes.md">日记笔记</a>等示例。

此外，请参阅<a class="reference-link" href="Default%20Note%20Title.md">默认笔记标题</a>以了解如何创建标题模板。笔记模板和标题模板可以通过为模板笔记创建 `#titleTemplate` 来组合使用。