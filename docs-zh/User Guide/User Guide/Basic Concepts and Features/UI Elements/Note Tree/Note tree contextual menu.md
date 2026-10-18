# 笔记树上下文菜单
<figure class="image image-style-align-right"><img style="aspect-ratio:269/608;" src="1_Note tree contextual menu_image.png" width="269" height="608"></figure>

_笔记树菜单_ 可通过在 <a class="reference-link" href="../Note%20Tree.md">笔记树</a> 中右键单击来访问。

## 交互

上下文菜单可作用于：

*   单个笔记，通过在笔记树中右键单击该笔记。
*   多个笔记，通过先选中它们。有关操作方法，请参阅 <a class="reference-link" href="Multiple%20selection.md">多选</a>。
    *   右键单击时请注意，通常被右键单击的笔记也会包含在受影响的笔记中，无论它是否已被选中。

## 可用选项

> [!NOTE]
> 当选中多个笔记时，只有部分选项会处于可用状态。支持多笔记的选项将在下方列表中注明。

最常用的操作并排显示在菜单顶部，每个操作以图标加名称的形式呈现。使用 <kbd>←</kbd> 和 <kbd>→</kbd>，或 <kbd>↑</kbd> 和 <kbd>↓</kbd> 在它们之间移动。

*   **剪切**
    *   将给定的笔记放入剪贴板。
    *   使用两个粘贴功能之一（或键盘快捷键）将它们移动到所需位置。
*   **克隆**
    *   将给定的笔记放入剪贴板。
    *   使用两个粘贴功能之一（或键盘快捷键）将它们复制到所需位置。
    *   请注意，此处的复制功能按照 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a> 功能工作（即笔记本身会同时存在于两个位置，在一处编辑它会在所有位置生效）。
    *   若要简单地创建一个可独立修改的重复笔记，请查找 _创建副本_。
*   **粘贴到内部**
    *   将剪贴板中的笔记作为右键单击笔记的子笔记粘贴。
    *   仅在笔记已被剪切或克隆后显示。
*   **粘贴到之后**
    *   将剪贴板中的笔记粘贴到右键单击笔记的下方。
    *   仅在笔记已被剪切或克隆后显示。
*   **删除…**
    *   将删除给定的笔记，并先请求确认。
    *   在对话框中，可以配置以下选项：
        *   _同时删除所有克隆_ 以确保如果笔记被放置在多个位置，它将在所有位置被删除（请参阅 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a>）。
        *   _永久擦除笔记_ 将确保笔记无法从 <a class="reference-link" href="../Recent%20Changes.md">最近更改</a> 中恢复。

菜单的其余部分每行列出一个选项：

*   **打开笔记**
    *   单击它会在新的[标签页](../Tabs.md)中打开笔记。
    *   悬停它或单击其箭头会打开一个子菜单，其中包含可打开笔记的位置：_在新标签页中打开_、_在新分屏中打开_（在当前标签页内笔记的右侧）以及 _在新窗口中打开_。
*   **快速编辑**
    *   在当前笔记之上以 <a class="reference-link" href="../../Navigation/Quick%20edit.md">快速编辑</a> 方式打开笔记。
*   **提升笔记**
    *   将笔记树聚焦于此笔记。有关更多信息，请参阅 <a class="reference-link" href="../../Navigation/Note%20Hoisting.md">笔记提升</a>。
*   **在之后插入笔记**
    *   允许便捷地创建具有指定[笔记类型](../../../Note%20Types.md)的笔记。
    *   _代码_ 子菜单以脚本类笔记开头，每个都是为其角色配置好的代码笔记：_自定义 CSS_（带有 `#appCss`）、_小组件_（带有 `#widget` 和起始骨架）以及 _后端脚本_。随后是已启用的代码语言。
    *   <a class="reference-link" href="../../../Collections.md">集合</a> 归入 _集合_ 子菜单。创建频率较低的笔记类型、<a class="reference-link" href="../../../Advanced%20Usage/Snippets.md">代码片段</a> 以及 AI 快速操作位于 _更多_ 子菜单中。
    *   <a class="reference-link" href="../../../Advanced%20Usage/Templates.md">模板</a>（如果有）也会出现在列表末尾。
    *   若要快速查找条目，请在子菜单顶部的搜索框中输入，或在子菜单打开时直接开始输入。子菜单随后会列出所有匹配的条目，包括其自身子菜单内的条目（例如代码语言或集合），每个条目都会标明其来源子菜单。使用 <kbd>↑</kbd> 和 <kbd>↓</kbd> 选择匹配项，<kbd>Enter</kbd> 创建它，<kbd>Esc</kbd> 清除搜索。
    *   笔记将添加到与所选笔记相同的层级。
*   **插入子笔记**
    *   与 _在之后插入笔记_ 相同，但笔记将创建为所选笔记的子笔记。
*   **移动到…**
    *   将显示一个模态框，用于指定将所需笔记移动到的位置。
*   **克隆到…**
    *   将显示一个模态框，用于指定将所需笔记[克隆](../../Notes/Cloning%20Notes.md)到的位置。
*   **创建副本**
    *   创建笔记及其后代的副本，放置在原始笔记之后。
    *   当笔记有子笔记时，该条目还会有一个箭头，由分隔线隔开。悬停该条目或单击箭头会打开一个子菜单：
        *   _笔记及其子笔记_ 与单击 _创建副本_ 相同。
        *   _仅此笔记_ 复制笔记及其内容和属性，但不包含任何子笔记。指向原始子笔记的链接和关系仍指向它们。
    *   此过程与 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a> 不同，因为创建的副本可以独立于原始笔记进行编辑。
    *   如果经常这样做，另一种替代方法是使用 <a class="reference-link" href="../../../Advanced%20Usage/Templates.md">模板</a>。
*   **归档/取消归档**
    *   将笔记标记为[已归档](../../Notes/Archived%20Notes.md)。
    *   如果笔记已归档，则会改为取消归档。
    *   也可以选择多个笔记。但是，所有选中的笔记必须处于相同状态（已归档或未归档），否则该选项将被禁用。
*   **保护子树/取消保护子树**
    *   对于未受保护的笔记，_保护子树_ 会将此笔记及其所有后代标记为受保护。对于受保护的笔记，该条目显示为 _取消保护子树_，并改为取消保护它们。有关更多信息，请参阅 <a class="reference-link" href="../../Notes/Protected%20Notes.md">受保护的笔记</a>。
    *   悬停该条目或单击其箭头会打开一个包含两个操作的子菜单，例如用于取消保护本身未受保护的笔记下方的受保护笔记。
*   **导入到笔记…**
    *   打开[导入](../../Import%20%26%20Export.md)对话框，并将导入的笔记作为所选笔记的子笔记放置。
*   **导出…**
    *   为所选笔记打开[导出](../../Import%20%26%20Export.md)对话框。
*   **在子树中搜索**
    *   打开一个完整的 <a class="reference-link" href="../../Navigation/Search.md">搜索</a>，并预先配置为仅查找此笔记及其后代（_祖先_ 字段）。

## 高级选项

<figure class="image image-style-align-right"><img style="aspect-ratio:231/263;" src="Note tree contextual menu_image.png" width="231" height="263"></figure>

高级选项菜单提供了一些较少使用的笔记操作。

要访问这些选项，请先查找上下文菜单底部的 _高级_ 选项，以展开一个子菜单，其中包含：

*   **应用批量操作…**
    *   打开 <a class="reference-link" href="../../../Advanced%20Usage/Bulk%20Actions.md">批量操作</a> 对话框，以对多个笔记一次性应用添加标签或移动笔记等操作（请参阅 <a class="reference-link" href="Multiple%20selection.md">多选</a>）。
*   **编辑分支前缀…**
    *   打开一个对话框，用于分配名称以便区分[克隆](../../Notes/Cloning%20Notes.md)，有关更多信息，请参阅 <a class="reference-link" href="../../Notes/Cloning%20Notes/Branch%20prefix.md">分支前缀</a>。
*   **转换为附件…**
    *   将所选笔记转换为其父笔记的 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
    *   此功能在处理从外部来源或旧版 Trilium 导入的图像 <a class="reference-link" href="../../../Note%20Types/File.md">文件</a> 笔记时最为有用。
*   **展开子树**
    *   展开 <a class="reference-link" href="../Note%20Tree.md">笔记树</a> 中的所有子笔记。
*   **折叠子树**
    *   折叠笔记树中的所有子笔记。
*   **排序方式…**
    *   打开一个对话框，对所选笔记的所有子笔记进行排序。
    *   排序仅执行一次，也有自动排序机制可通过 <a class="reference-link" href="../../../Advanced%20Usage/Attributes.md">属性</a> 设置。
    *   有关更多信息，请参阅 <a class="reference-link" href="../../Notes/Sorting%20Notes.md">笔记排序</a>。
*   **复制笔记路径到剪贴板**
    *   复制表示笔记此分支完整路径的 URL 片段，例如 `#root/Hb2E70L7HPuf/4sRFgMZhYFts/2IVuShedRJ3U/LJVMvKXOFv7n`。
    *   该 URL 用于在笔记中手动创建 <a class="reference-link" href="../../../Note%20Types/Text/Links.md">链接</a>，或用于笔记 <a class="reference-link" href="../../Navigation">导航</a>。
*   **子树中的最近更改**
    *   这将打开 <a class="reference-link" href="../Recent%20Changes.md">最近更改</a>，但仅筛选出与此笔记或其某个后代相关的更改。