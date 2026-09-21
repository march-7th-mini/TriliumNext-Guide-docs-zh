# 后端事件
[脚本](../../Scripting.md)笔记可以由事件触发。请注意，这些是后端事件，因此关系需要指向“JavaScript (Trilium 后端)”代码笔记。

## 全局事件

全局事件通过标签附加到脚本笔记上。只需创建一个带有以下某些值的 `run` 标签，脚本笔记就会在事件发生时执行。

<table>
    <thead>
        <tr>
            <th>标签</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>run</code></td>
            <td><p>定义脚本应在哪些事件上运行。可能的值有：</p><ul><li><code>backendStartup</code> - 当 Trilium 后端启动时</li><li><code>hourly</code> - 每小时运行一次。你可以使用额外的标签 <code>runAtHour</code> 在后端指定在哪个小时运行。</li><li><code>daily</code> - 每天在后端运行一次</li></ul></td>
        </tr>
        <tr>
            <td><code>runOnInstance</code></td>
            <td>指定脚本应仅在特定的&nbsp;<a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables)/Trilium%20instance.md">Trilium 实例</a>上运行。</td>
        </tr>
        <tr>
            <td><code>runAtHour</code></td>
            <td>应在哪个小时运行。应与 <code>#run=hourly</code> 一起使用。可以定义多次，以便在一天中运行更多次。</td>
        </tr>
    </tbody>
</table>

前端脚本也有类似的 <a class="reference-link" href="../Frontend%20Basics/Frontend%20Events.md">事件</a>，例如应用程序启动时。

> [!NOTE]
> 一个脚本可以在多个事件上触发，这可以通过添加多个 `run` 标签来实现。**不支持**用逗号分隔多个值。

## 实体事件

其他事件绑定到某个实体，这些事件定义为[关系](../../Advanced%20Usage/Attributes.md) —— 这意味着只有当笔记通过关系附加了此脚本（或者它可以继承它）时，脚本才会被触发。

| 关系 | 触发条件 | 来源实体（见下文） |
| --- | --- | --- |
| `runOnNoteCreation` | 在后端创建笔记时执行。如果你想为特定子树下创建的所有笔记运行脚本，请使用此关系。在这种情况下，请在子树根笔记上创建它并使其可继承。在子树内（任意深度）创建的新笔记将触发脚本。 | 被创建的 `BNote`。 |
| `runOnChildNoteCreation` | 在定义了此关系的笔记下创建新笔记时执行 | 被创建的子笔记的 `BNote`。 |
| `runOnNoteTitleChange` | 笔记标题更改时执行（也包括笔记创建） | 标题被更改的笔记的 `BNote`。 |
| `runOnNoteContentChange` | 笔记内容更改时执行（也包括笔记创建）。 | 内容被更改的笔记的 `BNote`。 |
| `runOnNoteChange` | 笔记更改时执行（也包括笔记创建）。不包括内容更改 | 被更改的笔记的 `BNote`。 |
| `runOnNoteDeletion` | 笔记被删除时执行 | 被（软）删除的笔记的 `BNote`。 |
| `runOnBranchCreation` | 分支创建时执行。分支是父笔记和子笔记之间的链接，例如在克隆或移动笔记时创建。 | 被创建的 `BBranch`。 |
| `runOnBranchChange` | 分支更新时执行。（自 v0.62 起） | 被更改的 `BBranch`。 |
| `runOnBranchDeletion` | 分支删除时执行。分支是父笔记和子笔记之间的链接，例如在移动笔记时删除（旧分支/链接被删除）。 | 被（软）删除的 `BBranch`。 |
| `runOnAttributeCreation` | 为定义此关系的笔记创建新属性时执行 | 被创建的 `BAttribute`。 |
| `runOnAttributeChange` | 定义此关系的笔记的属性更改时执行。属性被删除时也会触发 | 被更改的 `BAttribute`。 |

## 来源实体

当脚本由上述事件之一运行时，`api.originEntity` 将被填充为触发更改的笔记、分支或属性。

例如，下面是一个带有 `~runOnAttributeChange` 的脚本，它根据 `mycategory` 标签的值自动更改笔记的颜色：

```javascript
const attr = api.originEntity;
if (attr.name !== "mycategory") return;
const note = api.getNote(attr.noteId);
if (attr.value === "Health") {
    note.setLabel("color", "green");
} else {
    note.removeLabel("color");
}
```

## 安全模式

当[安全模式](../../Advanced%20Usage/Safe%20mode.md)处于活动状态时，带有事件的脚本将不会触发。