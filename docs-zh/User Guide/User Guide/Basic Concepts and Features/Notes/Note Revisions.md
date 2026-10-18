# 笔记修订

<figure class="image"><img style="aspect-ratio:2089/1515;" src="Note Revisions_image.png" width="2089" height="1515"></figure>

Trilium 通过定期存储笔记的快照（“修订”）来支持笔记的无缝版本管理。

要显示修订，请按 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> 并选择 _笔记修订…_（<span class="tn-icon bx bx-history"></span>）。

## 交互

> [!NOTE]
> 本文档与 v0.103.0 中笔记修订对话框的重新设计相匹配，旧版本的对话框类似但有一些差异。

*   完整的修订列表按时间倒序显示在左侧。
    *   修订按拍摄修订的日期分组。
    *   此列表不包含笔记的_当前状态_，因此可能存在没有保存任何修订/快照的笔记。
*   修订的图标指示该修订的_来源_（例如，手动保存的修订显示 <span class="tn-icon bx bx-save"></span> 图标）。
*   按对话框右上角的 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 按钮会显示多个选项，包括：
    *   <span class="tn-icon bx bx-save"></span> 立即保存新修订。
    *   检查此笔记的间隔和限制（见下文）。
    *   <span class="tn-icon bx bx-trash"></span> 删除此笔记的所有修订。
*   对于支持的笔记（文本、代码），更改会被高亮显示。此行为可通过对话框顶部的_高亮更改_进行切换。
    *   高亮显示的更改是相对于**笔记的当前状态**，而不是相对于此修订之前的修订。
*   对于任何给定的修订，右上角的按钮允许对其进行操作：
    *   <span class="tn-icon bx bx-trash"></span> 删除该修订。
    *   <span class="tn-icon bx bx-download"></span> 将该修订下载到本地。
    *   <span class="tn-icon bx bx-history"></span> 恢复该修订，将笔记的当前内容替换为该修订中的内容。同时会保存另一个包含笔记当前内容的修订。

## 命名修订

命名修订是 Trilium v0.103.0 的新功能，允许添加关于快照中所含更改的简短描述。

在笔记修订列表中：

*   修订的名称显示在侧边栏中修订时间的下方，以及对话框顶部（完整显示）。
*   点击修订名称附近的 <span class="tn-icon bx bx-edit-alt"></span> 编辑按钮可以更改名称。

要创建命名修订，可以：

*   转到 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>，选择_保存命名修订…_（<span class="tn-icon bx bx-purchase-tag"></span>），输入修订名称并确认。
*   使用相应的[键盘快捷键](../Keyboard%20Shortcuts.md)或同名的 <a class="reference-link" href="../Navigation/Jump%20to%20%26%20command%20palette.md">跳转与命令面板</a> 命令。
*   正常保存修订，然后从笔记修订列表中调整名称。

## 修订何时保存

修订会在以下情况下保存：

*   按固定间隔自动保存。此行为可以配置（见下文）。
*   手动保存，方式包括：
    *   转到 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> 并选择_保存修订_（<span class="tn-icon bx bx-save"></span>）。
    *   使用_强制保存修订_[键盘快捷键](../Keyboard%20Shortcuts.md)。
    *   在_笔记修订_对话框中，按右上角的 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 按钮并选择_立即保存修订_。

此外，修订也可能来自其他地方，这通过修订的图标来指示：

*   <span class="tn-icon bx bx-code-alt"></span> 由 <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 在外部生成。
*   <span class="tn-icon bx bx-bot"></span> 由 <a class="reference-link" href="../../AI.md">AI</a> 创建的修改。
*   <span class="tn-icon bx bx-history"></span> 恢复了一个修订，导致现有笔记内容被保存为修订以防止潜在的数据丢失。

#### 快照间隔

拍摄笔记快照的时间间隔可在选项 → 其他对话框中配置。这在更多修订和更多存储数据之间提供了权衡。

要为特定笔记（或子树）关闭笔记版本管理，请向该笔记添加 `disableVersioning` [标签](../../Advanced%20Usage/Attributes.md)。

#### 最大修订数

笔记快照数量的限制可在选项 → 其他对话框中配置。笔记修订快照数量限制指的是每个笔记可以保存的最大修订数。其中 -1 表示无限制，0 表示删除所有修订。你可以通过 `versioningLimit=X` 标签为单个笔记设置最大修订数。

笔记限制不会立即生效；它仅在笔记被修改时才会应用。

你可以点击_清除多余的修订快照_下的_立即清除_按钮来立即应用更改。