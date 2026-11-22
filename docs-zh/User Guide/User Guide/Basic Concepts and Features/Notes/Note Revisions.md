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
*   修订的图标表示该修订的_来源_（例如手动保存的修订显示为 <span class="tn-icon bx bx-save"></span> 图标）。
*   按下对话框右上角的 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 按钮会显示多个选项，包括：
    *   <span class="tn-icon bx bx-save"></span> 立即保存新修订。
    *   检查此笔记的间隔和限制（见下文）。
    *   <span class="tn-icon bx bx-trash"></span> 删除此笔记的所有修订。
*   对于支持的笔记（文本、代码），更改会被高亮显示。此行为可通过对话框顶部的_高亮更改_进行切换。
    *   高亮显示的更改是相对于**笔记的当前状态**，而不是相对于此修订之前的修订。
*   对于任何给定的修订，右上角的按钮允许对其进行操作：
    *   <span class="tn-icon bx bx-trash"></span> 删除该修订。
    *   <span class="tn-icon bx bx-download"></span> 将该修订下载到本地。
    *   <span class="tn-icon bx bx-history"></span> 恢复该修订，这会用修订中的内容替换笔记的当前内容。同时会保存另一个包含笔记当前内容的修订。

## 命名修订

命名修订是 Trilium v0.103.0 的新功能，允许添加关于快照中所含更改的简短描述。

在笔记修订列表中：

*   修订的名称显示在侧边栏中修订时间的下方，同时也完整显示在对话框顶部。
*   点击修订名称附近的 <span class="tn-icon bx bx-edit-alt"></span> 编辑按钮可以更改名称。

要创建命名修订，可以：

*   转到 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a>，选择 _笔记修订…_ → _保存命名修订…_（<span class="tn-icon bx bx-purchase-tag"></span>），输入修订名称并确认。
*   使用相应的[键盘快捷键](../Keyboard%20Shortcuts.md)或同名的 <a class="reference-link" href="../Navigation/Jump%20to%20%26%20command%20palette.md">跳转与命令面板</a> 命令。
*   正常保存修订，然后从笔记修订列表中调整名称。

## 修订的保存时机

修订会在以下情况下保存：

*   按固定间隔自动保存。此行为可以配置（见下文）。
*   手动保存，方式包括：
    *   转到 <a class="reference-link" href="../UI%20Elements/Note%20menu.md">笔记菜单</a> 并选择 _笔记修订…_ → _保存修订_（<span class="tn-icon bx bx-save"></span>）。
    *   使用_强制保存修订_[键盘快捷键](../Keyboard%20Shortcuts.md)。
    *   在_笔记修订_对话框中，按下右上角的 <span class="tn-icon bx bx-dots-horizontal-rounded"></span> 按钮并选择_立即保存修订_。

此外，修订也可能来自其他地方，这通过修订的图标来表示：

*   <span class="tn-icon bx bx-code-alt"></span> 由 <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 在外部生成。
*   <span class="tn-icon bx bx-bot"></span> 由 <a class="reference-link" href="../../AI.md">AI</a> 创建的修改。
*   <span class="tn-icon bx bx-history"></span> 恢复了某个修订，导致现有笔记内容被保存为修订以防止潜在的数据丢失。
*   <span class="tn-icon bx bx-git-compare"></span> 你未保存的更改，因无法保存到笔记中而被保留（见下文_在其他地方所做的更改_）。

#### 快照间隔

拍摄笔记快照的时间间隔可在选项 → 其他对话框中配置。这在更多修订与更多存储数据之间提供了权衡。

要为特定笔记（或子树）关闭笔记版本管理，请向该笔记添加 `disableVersioning` [标签](../../Advanced%20Usage/Attributes.md)。

#### 最大修订数

笔记快照数量的限制可在选项 → 其他对话框中配置。笔记修订快照数量限制指的是每个笔记可保存的最大修订数。其中 -1 表示无限制，0 表示删除所有修订。你可以通过 `versioningLimit=X` 标签为单个笔记设置最大修订数。

笔记限制不会立即生效；它仅在笔记被修改时才会应用。

你可以点击_清除多余的修订快照_下的_立即清除_按钮来立即应用更改。

## 在其他地方所做的更改

如果你在编辑笔记时该笔记在其他地方发生了更改（例如在另一个窗口或另一台设备上），Trilium 会询问要保留哪个版本：

*   _保留此版本_会保存你的更改。另一个版本会作为修订保留。
*   _加载另一个版本_会显示另一个版本。你的更改会作为修订保留。

如果该笔记不保留任何修订，则你未选择的版本将被丢弃。

如果你在编辑笔记时该笔记被转换为另一种类型，或者你编辑的摘录的块在其他地方被更改而无法再单独编辑，你的更改也会作为修订保留。仅包含摘录块的修订无法恢复，但你可以复制它。