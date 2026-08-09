# 笔记树右键菜单
<figure class="image image-style-align-right"><img style="aspect-ratio:269/608;" src="1_Note tree contextual menu_image.png" width="269" height="608"></figure>

_笔记树菜单_ 可以通过在 <a class="reference-link" href="../Note%20Tree.md">笔记树</a> 中右键点击来访问。

## 交互

右键菜单可以操作：

*   单个笔记：在笔记树中右键点击该笔记。
*   多个笔记：先选中它们。关于如何操作，请参阅 <a class="reference-link" href="Multiple%20selection.md">多选</a>。
    *   右键点击时，请注意，无论该笔记是否被选中，通常被右键点击的笔记也会包含在受影响的笔记中。

## 可用选项

> [!NOTE]
> 当选中多个笔记时，只有部分选项会处于激活状态。支持多笔记操作的选项会在下方列表中注明。

*   **在新标签页中打开**
    *   将在新的[标签页](../Tabs.md)中打开单个笔记。
*   **在新分栏中打开**
    *   将在当前标签页内右侧打开一个包含指定笔记的分栏。
*   **提升笔记**
    *   将笔记树聚焦于此笔记。更多信息请参阅 <a class="reference-link" href="../../Navigation/Note%20Hoisting.md">笔记提升</a>。
*   **在其后插入笔记**
    *   允许轻松创建具有指定[笔记类型](../../../Note%20Types.md)的笔记。
    *   <a class="reference-link" href="../../../Advanced%20Usage/Templates.md">模板</a>（如果有）也会出现在列表末尾。
    *   新笔记将添加到与所选笔记相同的层级。
*   **插入子笔记**
    *   与 _在其后插入笔记_ 相同，但新笔记将创建为所选笔记的子笔记。
*   **保护子树**
    *   将此笔记及其所有后代标记为受保护。更多信息请参阅 <a class="reference-link" href="../../Notes/Protected%20Notes.md">受保护的笔记</a>。
*   **取消保护子树**
    *   取消保护此笔记及其所有后代。
*   **剪切**
    *   将指定笔记放入剪贴板。
    *   使用两个粘贴功能之一（或键盘快捷键）将它们移动到所需位置。
*   **复制 / 克隆**
    *   将指定笔记放入剪贴板。
    *   使用两个粘贴功能之一（或键盘快捷键）将它们复制到所需位置。
    *   请注意，此处的复制功能遵循 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a> 的功能（即笔记本身将同时存在于两个位置，在一个位置编辑它会在所有位置生效）。
    *   若要简单地创建一个可以独立修改的重复笔记，请查找 _复制子树_。
*   **粘贴到内部**
    *   如果剪贴板中有任何笔记，它们将作为子笔记粘贴到被右键点击的笔记下。
*   **粘贴到后面**
    *   如果剪贴板中有任何笔记，它们将粘贴到被右键点击的笔记下方。
*   **移动到…**
    *   将显示一个模态框，用于指定将所需笔记移动到的位置。
*   **克隆到…**
    *   将显示一个模态框，用于指定将所需笔记[克隆](../../Notes/Cloning%20Notes.md)到的位置。
*   **复制**
    *   创建笔记及其后代的副本。
    *   此过程不同于 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a>，因为复制的笔记可以独立于原始笔记进行编辑。
    *   如果经常执行此操作，另一种选择是使用 <a class="reference-link" href="../../../Advanced%20Usage/Templates.md">模板</a>。
*   **归档/取消归档**
    *   将笔记标记为[已归档](../../Notes/Archived%20Notes.md)。
    *   如果笔记已归档，则改为取消归档。
    *   也可以选择多个笔记。但是，所有选中的笔记必须处于相同状态（已归档或未归档），否则该选项将被禁用。
*   **删除**
    *   将删除指定笔记，并首先请求确认。
    *   在对话框中，可以配置以下选项：
        *   _同时删除所有克隆_ 以确保如果笔记被放置到多个位置，它将在所有位置被删除（参见 <a class="reference-link" href="../../Notes/Cloning%20Notes.md">克隆笔记</a>）。
        *   _永久删除笔记_ 将确保无法从 <a class="reference-link" href="../Recent%20Changes.md">最近更改</a> 中恢复该笔记。
*   **导入到笔记**
    *   打开[导入](../../Import%20%26%20Export.md)对话框，并将导入的笔记作为所选笔记的子笔记放置。
*   **导出**
    *   为所选笔记打开[导出](../../Import%20%26%20Export.md)对话框。
*   **在子树中搜索**
    *   打开一个完整的 <a class="reference-link" href="../../Navigation/Search.md">搜索</a>，并预先配置为仅搜索此笔记及其后代（_祖先_ 字段）。

## 高级选项

<figure class="image image-style-align-right"><img style="aspect-ratio:231/263;" src="Note tree contextual menu_image.png" width="231" height="263"></figure>

高级选项菜单提供了一些较少使用的笔记操作。

要访问这些选项，请先在右键菜单中找到 _高级_ 选项，以展开一个子菜单，其中包含：

*   **应用批量操作**
    *   打开 <a class="reference-link" href="../../../Advanced%20Usage/Bulk%20Actions.md">批量操作</a> 对话框，以一次性对多个笔记应用诸如添加标签或移动笔记等操作（参见 <a class="reference-link" href="Multiple%20selection.md">多选</a>）。
*   **编辑分支前缀**
    *   打开一个对话框，用于分配名称以区分[克隆](../../Notes/Cloning%20Notes.md)，更多信息请参阅 <a class="reference-link" href="../../Notes/Cloning%20Notes/Branch%20prefix.md">分支前缀</a>。
*   **转换为附件**
    *   将选中的笔记转换为其父笔记的 <a class="reference-link" href="../../Notes/Attachments.md">附件</a>。
    *   此功能在处理从外部来源或旧版 Trilium 导入的图片 <a class="reference-link" href="../../../Note%20Types/File.md">文件</a> 笔记时最为有用。
*   **展开子树**
    *   展开 <a class="reference-link" href="../Note%20Tree.md">笔记树</a> 中的所有子笔记。
*   **折叠子树**
    *   折叠笔记树中的所有子笔记。
*   **排序依据…**
    *   打开一个对话框，用于对所选笔记的所有子笔记进行排序。
    *   排序只执行一次，也有一个自动排序机制，可以使用 <a class="reference-link" href="../../../Advanced%20Usage/Attributes.md">属性</a> 进行设置。
    *   更多信息请参阅 <a class="reference-link" href="../../Notes/Sorting%20Notes.md">笔记排序</a>。
*   **复制笔记路径到剪贴板**
    *   复制一个表示笔记此分支完整路径的 URL 片段，例如 `#root/Hb2E70L7HPuf/4sRFgMZhYFts/2IVuShedRJ3U/LJVMvKXOFv7n`。
    *   该 URL 用于在笔记中手动创建 <a class="reference-link" href="../../../Note%20Types/Text/Links.md">链接</a>，或用于笔记<a class="reference-link" href="../../Navigation">导航</a>。
*   **子树中的最近更改**
    *   这将打开 <a class="reference-link" href="../Recent%20Changes.md">最近更改</a>，但会过滤为仅显示与此笔记或其某个后代相关的更改。