# 提升属性
<figure class="image image_resized" style="width:61.4%;"><img style="aspect-ratio:938/368;" src="Promoted Attributes_image.png" width="938" height="368"></figure>

提升属性是[属性](../Attributes.md)，它们在 UI 中显著显示，以便于轻松查看和编辑。

提升属性显示在笔记的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Title.md">标题</a>下方，位于一个可折叠区域中。对于全高度笔记（如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>），提升属性默认折叠以腾出空间。

看待提升属性的一种方式是将其视为一种包含多个字段的表单。每个字段只是普通属性，唯一的区别是它们显示在笔记本身上。

属性非常有用，因为它们允许查询和脚本自动化等，但它们也被不方便地隐藏了。这允许你选择少数重要的属性并将它们推到用户面前。

## 属性定义

<figure class="image image-style-align-right image_resized" style="width:50%;"><img style="aspect-ratio:885/742;" src="2_Promoted Attributes_image.png" width="885" height="742"></figure>

为了拥有提升属性，需要有一种定义它们的方式。

从技术上讲，属性只是名称-值对，其中名称和值都是字符串。

_属性定义_指定了应如何解释此值：

*   它只是字符串，还是日期？
*   我们应该允许多个值还是笔记？
*   我们应该_提升_该属性还是不提升？

## 属性类型

属性定义有一个专用的类型字段，它将改变值在提升属性区域中的编辑方式。

支持以下类型：

*   _文本_，默认选项，允许编辑任何类型的文本，类似于没有关联类型的普通标签。
*   _多行文本_，类似于普通文本字段，但在更大的文本框中呈现，也支持多行书写。
*   _数字_，将显示为带有上下箭头的数字输入字段。
    *   可选的_精度_，设置值步进和显示的小数位数。
*   _复选框_，为真/假值呈现为复选框。在标签定义中，此类型写为 `boolean`。
*   _选择_，在编辑时提供用户定义的选项列表。
    *   列表不是固定的，意味着可以轻松地从提升属性中添加新选项。
    *   重命名选项不会更改现有值，因为值存储为文本。考虑使用[批量重命名](../Bulk%20Actions.md)。
    *   这些项目没有自定义颜色或图标。这是有意为之，因为选择旨在轻量级。对于更可自定义的选项，考虑使用<a class="reference-link" href="Relations.md">关系</a>，它使用笔记作为项目，这些笔记可以着色并带有图标。
*   _日期_，提供日期选择器。
*   _日期和时间_，提供日期和时间选择器。
*   _时间_，提供时间选择器。
*   _URL_，提供一个按钮以在新窗口中打开网址。
*   _电子邮件_，提供一个按钮以使用操作系统的默认应用快速发送电子邮件到该地址。
*   _电话_，提供一个按钮以使用操作系统的默认应用快速拨打该号码。
*   _颜色_，提供颜色选择器和移除值的方式。
*   _关系_，指向另一条笔记，并使用<a class="reference-link" href="Relations.md">关系</a>而不是<a class="reference-link" href="Labels.md">标签</a>。

> [!NOTE]
> 对于基于标签的属性，这些类型不由属性系统强制执行，意味着之后更改类型并不保证其中的值与该类型对应（例如将文本转换为数字）。

## 创建新的提升属性定义

要创建新的提升属性：

1.  转到一条笔记。
2.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Attributes%20tab.md">属性选项卡</a>。
3.  按最顶部区域（_拥有的属性_）的 <span class="tn-icon bx bx-plus"></span> 按钮。
4.  选择_添加新标签定义_或_添加新关系定义_。
5.  选择名称，该名称将是编辑提升属性时创建的标签或关系的名称。
6.  确保勾选_提升_，以便在笔记顶部显示它。
7.  可选地，选择一个_别名_，它将显示在提升属性旁边而不是属性名称。通常最好选择一个“用户友好”的名称，因为它可以包含空格和其他不支持作为属性名称的字符。
8.  勾选_可继承_以将其应用于此笔记及其所有后代。要仅保留在当前笔记，取消勾选。
9.  按_保存并关闭_以应用更改。

或者，可以从<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>创建提升属性，方法是转到 <span class="tn-icon bx bx-list-check"></span>（_属性_），按 <span class="tn-icon bx bx-plus"></span> 按钮并选择_添加新标签定义_。生成的属性也可以复制粘贴或手动编写（尽管不推荐）。

## 属性定义实际如何工作

创建新的提升属性定义时，它会创建一个相应的标签，前缀为 `label` 或 `relation`，取决于定义类型：

```
#label:myColor(inheritable)="promoted,alias=Color,multi,color"
```

属性定义的唯一目的是设置模板。如果属性被标记为提升，那么它也会显示给用户以便于编辑。

<table>
    <tbody>
        <tr>
            <td><figure class="image"><img style="aspect-ratio:495/157;" src="1_Promoted Attributes_image.png" width="495" height="157"></figure></td>
            <td>注意提升属性定义只在文本内容上方创建了一个“截止日期”框。</td>
        </tr>
        <tr>
            <td><figure class="image"><img style="aspect-ratio:663/160;" src="3_Promoted Attributes_image.png" width="663" height="160"></figure></td>
            <td>一旦用户设置了值，就会创建一个新标签（或关系，取决于类型）。属性名称与创建提升属性时设置的名称匹配。</td>
        </tr>
    </tbody>
</table>

所以有一个属性用于值，一个用于定义。但请注意定义属性可以设为[可继承](Attribute%20Inheritance.md)，意味着它也应用于所有后代笔记。在这种情况下，定义用于整个子树，而“值”属性则分别用于每条笔记。

## 使用系统属性

可以从系统属性创建提升属性，以便轻松更改它们。

以下是一些实际示例：

*   <a class="reference-link" href="../../Collections.md">集合</a>已经使用了这种做法，例如：
    *   日历添加“开始日期”、“结束日期”、“开始时间”和“结束时间”作为提升属性。这些映射到系统属性，如 `startDate`，然后由日历视图解释。
    *   <a class="reference-link" href="../../Collections/Presentation.md">演示文稿</a>为每张幻灯片添加“背景”提升属性，以便轻松自定义。
*   Trilium 文档（在 Trilium 中编辑）使用提升属性来轻松编辑 `#shareAlias`（参见<a class="reference-link" href="../Sharing.md">共享</a>）以形成干净的 URL。
*   如果你总是编辑某个特定的系统属性，如 `#color`，只需为它创建一个提升属性以使其更容易。

### 反向关系

有些关系总是成对出现——我最喜欢的例子是家庭。如果你有一条代表丈夫的笔记和一条代表妻子的笔记，那么这两者之间可能存在 `isPartnerOf` 的关系。这是双向关系——意味着如果有一个从丈夫指向妻子的关系，那么应该总是有另一个从妻子指向丈夫的关系。

另一个例子是父子关系。同样这些总是成对出现，但在这种情况下不是完全相同的关系——从父到子的可能称为 `isParentOf`，另一个从子到父的可能称为 `isChildOf`。

关系定义允许你指定这样的“反向关系”——对于你刚刚定义的关系，你指定哪个是反向关系。注意在第二个例子中我们应该有两个关系定义——一个用于 `isParentOf`，它定义 `isChildOf` 作为反向关系，然后第二个关系定义用于 `isChildOf`，它定义 `isParentOf` 作为反向关系。

这在内部的作用是，每当我们保存一个定义了反向关系的关系时，我们检查该反向关系是否存在于关系目标笔记上。类似地，当我们删除关系时，我们也删除目标笔记上的反向关系。

## 另请参阅

*   <a class="reference-link" href="../../Collections/Table.md">表格</a>集合大量使用提升属性来定义表格的列，因为它们已经携带类型信息。当设为可继承时，在打开子笔记时也很容易更改这些字段。