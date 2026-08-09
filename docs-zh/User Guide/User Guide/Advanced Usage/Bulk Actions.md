# 批量操作
<figure class="image"><img style="aspect-ratio:1425/644;" src="Bulk Actions_image.png" width="1425" height="644"></figure>

_批量操作_ 对话框可以轻松地对多个笔记同时应用更改，从添加或删除标签等简单操作到执行自定义脚本等复杂操作。

## 交互方式

*   第一步是在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中选择笔记。可以对以下对象应用批量操作：
    *   单个笔记（以及可能的子笔记），只需单击它（左键单击或右键单击）。
    *   多个笔记。参见<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Multiple%20selection.md">多选</a>了解如何操作。
*   在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键单击，然后选择 _高级_ → _应用批量操作_。
*   默认情况下，只有选中的笔记会受到影响。要同时包含笔记的所有后代，请勾选 _包含所选笔记的后代_。对话框顶部的受影响笔记数量将更新以反映更改。
*   从 _可用操作_ 部分点击要应用的操作。每个操作的详细说明将在下一节中提供。
    *   对于每个选中的操作，_已选操作_ 部分将更新以显示该条目。每个操作都有自己的配置。
    *   要移除某个操作，只需按下其右侧的 X 按钮。
    *   可以应用多个相同类型的操作，例如添加多个类型。
*   当所有操作都定义好后，按下 _执行批量操作_ 即可一次性触发所有操作。
*   为了方便起见，上次的批量操作配置会被保存以供后续使用，并在再次进入对话框时恢复。

## 操作

### 标签

这些操作作用于笔记的<a class="reference-link" href="Attributes/Labels.md">标签</a>：

*   **添加标签**
    *   对于每个笔记，如果它还没有给定名称的[标签](Attributes/Labels.md)，则会创建该标签。将 _新值_ 字段留空以创建无值的标签，或填写它以分配一个值。
    *   如果笔记已有此标签，其值将被更新。
*   **更新标签值**
    *   对于每个笔记，如果它有给定名称的[标签](Attributes/Labels.md)，则会将其值更改为指定值。将 _新值_ 字段留空以创建无值的标签。
    *   没有该标签的笔记将不受影响。
*   _**重命名标签**_
    *   对于每个笔记，如果它有给定名称的[标签](Attributes/Labels.md)，则会将其重命名/替换为新名称的标签。标签的值（如果存在）将保持不变。
    *   没有该标签的笔记将不受影响。
*   **删除标签**
    *   对于每个笔记，如果它有给定名称的标签，则该标签将被删除（无论其是否有值）。
    *   没有该标签的笔记将不受影响。

### 关系

这些操作作用于笔记的<a class="reference-link" href="Attributes/Relations.md">关系</a>：

*   **添加关系**
    *   对于每个笔记，它将创建一个指向给定笔记的关系。
    *   没有此关系的笔记将不受影响。
*   **更新关系目标**
    *   对于每个笔记，它将修改一个关系以指向新给定的笔记。
    *   没有此关系的笔记将不受影响。
*   **重命名关系**
    *   对于每个笔记，如果它有给定名称的关系，则会将其重命名/替换为新名称的关系。关系的目标笔记将保持不变。
    *   没有此关系的笔记将不受影响。
*   **删除关系**
    *   对于每个笔记，如果它有给定名称的关系，则该关系将被删除。
    *   没有此关系的笔记将不受影响。

### 笔记

*   **重命名笔记**
    *   对于每个笔记，它将把笔记的标题更改为给定的标题。
    *   作为更高级的用例，笔记可以是一个“模板字符串”，允许通过<a class="reference-link" href="../Scripting/Script%20API/Frontend%20API/FNote.dat">FNote</a>访问笔记信息来使用动态值，例如：
        *   `NEW: ${note.title}` 将给所有笔记添加 `NEW:` 前缀。
        *   `${note.dateCreatedObj.format('MM-DD:')}: ${note.title}` 将给笔记标题添加每个笔记的创建日期（月-日格式）前缀。
*   **移动笔记**
    *   对于每个笔记，它将被移动到指定的父笔记下。
    *   对于不太复杂的情况，也可以直接在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中通过剪切 → 粘贴或通过上下文菜单来移动笔记。
*   **转换笔记**
    *   这允许将笔记从一种类型转换为另一种类型：
        *   **文本笔记 → Markdown 笔记** — 每个<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记都被转换为<a class="reference-link" href="../Note%20Types/Markdown.md">Markdown</a>笔记。由于 Markdown 不支持文本笔记的所有格式功能，某些格式可能会丢失，某些不支持的元素甚至可能被删除。
        *   **Markdown 笔记 → 文本笔记** — 每个<a class="reference-link" href="../Note%20Types/Markdown.md">Markdown</a>笔记都被转换为<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记。
    *   对于每个转换后的笔记，会自动保存一个修订版，使您可以恢复原始笔记或从中恢复任何缺失的元素。
*   **保存修订版**
    *   自动为每个笔记创建修订版。可选地，可以为该修订版指定一个名称。参见<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订版</a>。
*   **删除笔记**
    *   对于每个笔记，它将被删除。
    *   对于不太复杂的情况，也可以直接在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中选择笔记并按 <kbd>Delete</kbd> 键来删除。
*   **删除笔记修订版**
    *   这将删除笔记的所有<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订版</a>。

### 其他

*   **执行脚本**
    *   对于更复杂的场景，可以输入 JavaScript 表达式以应用必要的更改。
    *   示例：
        *   为笔记标题添加后缀（此示例中为 `- suffix`）：
            
            ```javascript
            note.title = note.title + " - suffix";
            ```
        *   根据另一个属性更改笔记的属性，例如将 `#shareAlias` 标签设置为笔记的标题：
            
            ```javascript
            note.setLabel("shareAlias", note.title)
            ```