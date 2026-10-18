# 批量操作
<figure class="image"><img style="aspect-ratio:1425/644;" src="Bulk Actions_image.png" width="1425" height="644"></figure>

_批量操作_ 对话框可以轻松地同时对多个笔记应用更改，从添加或删除标签等简单操作到执行自定义脚本。

## 交互

*   第一步是在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中选择笔记。可以对以下对象应用批量操作：
    *   单个笔记（可能包括其子笔记），只需单击它（左键单击或右键单击）。
    *   多个笔记。有关如何操作，请参阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>。
*   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键单击，然后选择 _高级_ → _应用批量操作_。
*   对话框顶部的 _选中的笔记_ 部分列出了操作所应用的笔记。当选中许多笔记时，只显示前几个；单击 _+N 更多_ 以显示其余部分。
    *   要在不更改笔记树中选区的情况下排除某个笔记，请按其条目上的 <span class="tn-icon bx bx-x"></span> 按钮。最后一个剩余的笔记无法移除。
*   默认情况下，只有选中的笔记会受到影响。要同时包含笔记的所有后代，请开启 _包含选中笔记的后代_。该选项下方显示的受影响的笔记数量会更新以反映更改。
*   要添加操作，请单击 _已选操作_ 部分底部的 _添加操作_（<span class="tn-icon bx bx-plus"></span>），然后从菜单中选择一个。将鼠标悬停在条目上会显示其功能的简短描述；每个操作的详细描述可在下一节中找到。
    *   每个选中的操作都会作为条目出现在 _已选操作_ 部分中，并带有自己的配置。
    *   要移除操作，只需按其右侧的 <span class="tn-icon bx bx-x"></span> 按钮。
    *   可以应用多个相同类型的操作，例如添加多个类型。
    *   标签或关系名称的字段会在您输入时建议数据库中已使用的名称，并标记 Trilium 本身赋予含义的名称。
    *   _添加标签_ 和 _更新标签值_ 的值字段会建议该名称标签在数据库中已有的值。
*   定义完所有操作后，按 _应用到 N 个笔记_ 按钮以一次性触发所有操作。该按钮会显示将受影响的笔记数量，并且在至少添加一个操作之前保持禁用状态。
    *   如果某个操作缺少所需的字段，例如要重命名的标签名称，对话框不会运行，而是指出空字段。
*   为方便起见，最后一次批量操作配置会被保存以供后续使用，并在再次进入对话框时恢复。

## 操作

### 标签

这些操作作用于笔记的<a class="reference-link" href="Attributes/Labels.md">标签</a>。除 _添加标签_ 外，它们只影响直接设置在笔记上的标签；继承的标签保持不变。

*   **添加标签**
    *   对于每个笔记，它会创建一个具有给定名称的[标签](Attributes/Labels.md)。将 _新值_ 字段留空以创建无值的标签，或填写它以分配值。
    *   即使笔记已经有一个同名标签，该标签也会被添加，因此笔记最终会同时拥有两者。要改为更改现有标签的值，请使用 _更新标签值_。
*   **更新标签值**
    *   对于每个笔记，如果它具有给定名称的[标签](Attributes/Labels.md)，则会将其值更改为指定的值。将 _新值_ 字段留空以创建无值的标签。
    *   没有该标签的笔记不会受到影响。
*   _**重命名标签**_
    *   对于每个笔记，如果它具有给定名称的[标签](Attributes/Labels.md)，则会将其重命名/替换为新名称的标签。标签的值（如果存在）将保持不变。
    *   没有该标签的笔记不会受到影响。
*   **删除标签**
    *   对于每个笔记，如果它具有给定名称的标签，则会被删除（无论它是否有值）。
    *   没有该标签的笔记不会受到影响。

### 关系

这些操作作用于笔记的<a class="reference-link" href="Attributes/Relations.md">关系</a>。除 _添加关系_ 外，它们只影响直接设置在笔记上的关系；继承的关系保持不变。

*   **添加关系**
    *   对于每个笔记，它会创建一个指向给定笔记的关系。
    *   即使笔记已经有一个同名关系，该关系也会被添加。
*   **更新关系目标**
    *   对于每个笔记，它会修改一个关系以指向新给定的笔记。
    *   没有此关系的笔记不会受到影响。
*   **重命名关系**
    *   对于每个笔记，如果它具有给定名称的关系，则会将其重命名/替换为新名称的关系。关系的目标笔记将保持不变。
    *   没有此关系的笔记不会受到影响。
*   **删除关系**
    *   对于每个笔记，如果它具有给定名称的关系，则会被删除。
    *   没有此关系的笔记不会受到影响。

### 笔记

*   **重命名笔记**
    *   对于每个笔记，它会将笔记的标题更改为给定的标题。
    *   标题可以包含 `${` 和 `}` 之间的表达式，这些表达式会为每个笔记填充。它们可以读取笔记的属性，例如 `${note.title}`、`${note.noteId}` 或 `${note.type}`，并调用 `getLabelValue('name')`、`getRelationValue('name')`，或在 `dateCreatedObj` 等日期上调用 `format('…')`。例如：
        *   `NEW: ${note.title}` 将为所有笔记添加 `NEW:` 前缀。
        *   `${note.dateCreatedObj.format('MM-DD:')}: ${note.title}` 将为笔记标题添加每个笔记的创建日期前缀（以月-日格式）。
    *   只允许属性访问和这些方法，不允许任意 JavaScript。在输入时，字段会补全表达式，为不允许的表达式加下划线，并显示第一个选中笔记的结果标题。
*   **移动笔记**
    *   对于每个笔记，它将被移动到指定的父笔记。
    *   具有多个父笔记的笔记会被克隆到新父笔记，因为不清楚应移除其哪个位置。
    *   无法放置在那里的笔记，例如目标笔记的父笔记，将保持原位。
    *   作为较简单情况下的替代方案，可以直接从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中通过剪切 → 粘贴或通过上下文菜单移动笔记。
*   **转换笔记**
    *   这允许将笔记从一种类型转换为另一种类型：
        *   **文本笔记 → Markdown 笔记** — 每个<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记都会转换为<a class="reference-link" href="../Note%20Types/Markdown.md">Markdown</a>笔记。由于 Markdown 不支持文本笔记的所有格式功能，某些格式可能会丢失，某些不支持的元素甚至可能被丢弃。
        *   **Markdown 笔记 → 文本笔记** — 每个<a class="reference-link" href="../Note%20Types/Markdown.md">Markdown</a>笔记都会转换为<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记。
    *   对于每个转换的笔记，会自动保存一个修订版本，允许您恢复原始版本或从中恢复任何丢失的元素。
*   **保存修订版本**
    *   自动为每个笔记创建修订版本。可选地，可以为该修订版本分配一个名称。请参阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订版本</a>。
*   **删除笔记**
    *   对于每个笔记，它将被删除，包括其所有克隆以及未在其他地方克隆的任何子笔记。
    *   已删除的笔记可以从 _最近更改_ 中恢复，直到它们被清除。
    *   作为较简单情况下的替代方案，可以直接从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中通过选中它们并按 <kbd>Delete</kbd> 来移除笔记。
*   **删除笔记修订版本**
    *   这将永久清除笔记的所有<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订版本</a>。与已删除的笔记不同，已清除的修订版本无法恢复。

### 其他

*   **执行脚本**
    *   对于更复杂的场景，可以输入 JavaScript 表达式以应用必要的更改。
    *   脚本在服务器上为每个笔记运行一次，该笔记以 `note` 形式可用，后端脚本 API 以 `api` 形式可用。该字段会在您输入时补全两者并为错误加下划线，就像后端脚本笔记的编辑器一样。
    *   示例：
        *   要为笔记标题应用后缀（此示例中为 `- suffix`）：
            
            ```javascript
            note.title = note.title + " - suffix";
            ```
        *   要根据另一个属性更改笔记的属性，例如将 `#shareAlias` 标签设置为笔记的标题：
            
            ```javascript
            note.setLabel("shareAlias", note.title)
            ```