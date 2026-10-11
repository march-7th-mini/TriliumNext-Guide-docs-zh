# 只读笔记
某些笔记类型，例如 <a class="reference-link" href="../../Note%20Types/Text.md">文本</a>、<a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记，甚至某些 <a class="reference-link" href="../../Collections.md">集合</a> 都可以设置为只读。当笔记处于只读模式时，会以不可编辑的视图呈现给用户，如有需要，可以选择切换到编辑模式。

## 自动只读模式

出于优化目的，Trilium 会自动将非常大的笔记设置为只读。在编辑模式下显示如此冗长的笔记可能会降低性能，尤其是在不需要编辑的情况下。

可以按照下一节的说明，针对单个笔记禁用此行为。

此外，可以在 <a class="reference-link" href="../UI%20Elements/Options.md">选项</a> 中更改触发自动只读模式的字符数，方法是进入 <a class="reference-link" href="#root/_hidden/_options/_optionsTextNotes">文本笔记</a> 和 <a class="reference-link" href="#root/_hidden/_options/_optionsCodeNotes">代码笔记</a> 的选项。

## 更改笔记的只读行为

可以通过 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> → _可编辑_ 来更改笔记的只读行为。可以使用以下选项：

*   **自动**  
    这是默认行为，笔记默认情况下可编辑，除非它变得足够大以触发只读模式。
*   **只读**  
    无论笔记大小如何，都将始终标记为只读。尽管如此，如有需要，仍然可以临时编辑该笔记。这通常适用于不易更改的笔记。
*   **始终可编辑**  
    此选项将针对此特定笔记绕过自动只读激活。它适用于经常编辑的大型笔记。

如果 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> 中缺少 _可编辑_ 部分，则该笔记类型不支持只读模式。

### 手动设置选项

除了如前所述使用 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> 之外，还可以使用[标签](../../Advanced%20Usage/Attributes.md)来更改行为：

*   要设置为只读，请将 `readOnly` 标签应用到笔记。
*   要禁用自动只读（始终可编辑），请应用 `autoReadOnlyDisabled` 标签。

## 临时编辑只读笔记

访问只读笔记时，可以通过按下 _只读_ 徽章来临时编辑它。

按下后，笔记将变为可编辑，但在导航到其他笔记后将再次变为只读。