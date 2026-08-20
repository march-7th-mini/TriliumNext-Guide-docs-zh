# 只读笔记

Trilium 中的某些笔记类型，例如<a class="reference-link" href="../../Note%20Types/Text.md">文本</a>和<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记，可以设置为只读。当笔记处于只读模式时，它会以不可编辑的视图呈现给用户，并在需要时提供切换到编辑模式的选项。

## 自动只读模式

出于优化目的，Trilium 会自动将非常大的笔记设置为只读。在编辑模式下显示此类冗长笔记可能会降低性能，尤其是在不需要编辑的情况下。

可以按照下一节的说明，针对单个笔记禁用此行为。

此外，可以通过进入<a class="reference-link" href="../UI%20Elements/Options.md">选项</a>中的<a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a>和<a class="reference-link" href="#root/_hidden/_options/_optionsCodeNotes">代码笔记</a>选项，来更改触发自动只读模式的字符数。

## 更改笔记的只读行为

可以通过以下方式更改笔记的只读行为：

*   在新布局中，通过<a class="reference-link" href="../UI%20Elements/Note%20buttons.md">笔记按钮</a> → 新布局上的 _可编辑_
*   对于旧布局，通过<a class="reference-link" href="../UI%20Elements/Ribbon.md">功能区</a>，转到 _基本属性_ 选项卡并查找 _可编辑_ 选项。

可能的选项如下：

*   **自动**  
    这是默认行为，笔记默认可编辑，除非它变得足够大以触发只读模式。
*   **只读**  
    无论笔记大小如何，该笔记都将始终标记为只读。尽管如此，如果需要，仍然可以临时编辑该笔记。这对于不经常更改的笔记通常很有用。
*   **始终可编辑**  
    此选项将针对此特定笔记绕过自动只读激活。这对于经常编辑的大笔记很有用。

如果功能区中缺少 _可编辑_ 部分，则说明该笔记类型不支持只读模式。

### 手动设置选项

除了前面提到的使用功能区之外，还可以使用[标签](../../Advanced%20Usage/Attributes.md)来更改行为：

*   要设置为只读，请将 `readOnly` 标签应用于该笔记。
*   要禁用自动只读（始终可编辑），请应用 `autoReadOnlyDisabled` 标签。

## 临时编辑只读笔记

访问只读笔记时，可以通过以下方式临时编辑它：

*   在<a class="reference-link" href="../UI%20Elements/New%20Layout.md">新布局</a>上按下 _只读_ 徽章。
*   或者在<a class="reference-link" href="../UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域按下 ![](Read-Only%20Notes_image.png) 按钮。

按下后，笔记将变为可编辑，但在导航到其他笔记后将再次变为只读。

## 特殊只读行为

某些笔记类型根据是否启用只读模式而具有特殊行为：

*   <a class="reference-link" href="../../Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a>将隐藏 Mermaid 源代码，并全尺寸显示图表预览。在这种情况下，可以通过<a class="reference-link" href="../UI%20Elements/Floating%20buttons.md">浮动按钮</a>区域中的专用按钮轻松切换只读模式。
*   <a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>将禁止所有可能更改地图的交互（拖动笔记、添加新项目）。