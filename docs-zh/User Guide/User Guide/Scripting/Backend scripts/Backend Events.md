# 后端事件

[脚本](../../Scripting.md) 笔记可以通过事件触发。请注意，这些是后端事件，因此关系需要指向“JavaScript (Trilium 后端)”代码笔记。

## 全局事件

全局事件通过标签附加到脚本笔记上。只需创建一个带有以下某些值的 `run` 标签，事件发生时脚本笔记就会被执行。

<table>
    <thead>
        <tr>
            <th>标签</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code spellcheck="false">run</code></td>
            <td><p>定义脚本应在哪些事件上运行。可能的值有：</p><ul><li><code spellcheck="false">backendStartup</code> - 当 Trilium 后端启动时</li><li><code spellcheck="false">hourly</code> - 每小时运行一次。你可以使用额外的标签 <code spellcheck="false">runAtHour</code> 来指定在后端运行的整点小时。</li><li><code spellcheck="false">daily</code> - 每天在后端运行一次</li></ul></td>
        </tr>
        <tr>
            <td><code spellcheck="false">runOnInstance</code></td>
            <td>指定脚本应仅在特定的&nbsp;<a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables)/Trilium%20instance.md">Trilium 实例</a>上运行。</td>
        </tr>
        <tr>
            <td><code spellcheck="false">runAtHour</code></td>
            <td>应在哪个小时运行。应与 <code spellcheck="false">#run=hourly</code> 一起使用。可以定义多次以在一天内多次运行。</td>
        </tr>
    </tbody>
</table>

前端脚本也有类似的<a class="reference-link" href="../Frontend%20Basics/Frontend%20Events.md">事件</a>，例如应用程序启动时。

> [!NOTE]
> 一个脚本可以在多个事件上触发，这可以通过添加多个 `run` 标签来实现。用逗号分隔多个值**不**被支持。

## 实体事件

其他事件绑定到某个实体，这些事件被定义为[关系](../../Advanced%20Usage/Attributes.md) - 这意味着只有当笔记通过关系附加了此脚本时，脚本才会被触发（或者它可以继承该脚本）。

| 关系 | 触发条件 | 源实体（见下文） |
| --- | --- | --- |
| `runOnNoteCreation` | 当笔记在后端创建时执行。如果你想为特定子树下创建的所有笔记运行脚本，请使用此关系。在这种情况下，请在子树根笔记上创建它并使其可继承。在子树（任意深度）内创建的新笔记将触发该脚本。 | 被创建的 `BNote`。 |
| `runOnChildNoteCreation` | 当在定义此关系的笔记下创建新笔记时执行 | 被创建的子笔记的 `BNote`。 |
| `runOnNoteTitleChange` | 当笔记标题更改时执行（包括笔记创建） | 标题被更改的笔记的 `BNote`。 |
| `runOnNoteContentChange` | 当笔记内容更改时执行（包括笔记创建）。 | 内容被更改的笔记的 `BNote`。 |
| `runOnNoteChange` | 当笔记更改时执行（包括笔记创建）。不包括内容更改 | 被更改的笔记的 `BNote`。 |
| `runOnNoteDeletion` | 当笔记被删除时执行 | 被（软）删除的笔记的 `BNote`。 |
| `runOnBranchCreation` | 当分支被创建时执行。分支是父笔记和子笔记之间的链接，例如在克隆或移动笔记时创建。 | 被创建的 `BBranch`。 |
| `runOnBranchChange` | 当分支被更新时执行。（自 v0.62 起） | 被更改的 `BBranch`。 |
| `runOnBranchDeletion` | 当分支被删除时执行。分支是父笔记和子笔记之间的链接，例如在移动笔记时被删除（旧分支/链接被删除）。 | 被（软）删除的 `BBranch`。 |
| `runOnAttributeCreation` | 当定义此关系的笔记创建新属性时执行 | 被创建的 `BAttribute`。 |
| `runOnAttributeChange` | 当定义此关系的笔记的属性被更改时执行。属性被删除时也会触发 | 被更改的 `BAttribute`。 |

## 源实体

当脚本由上述事件之一运行时，`api.originEntity` 将被填充为触发更改的笔记、分支或属性。

例如，这是一个带有 `~runOnAttributeChange` 的脚本，它根据 `mycategory` 标签的值自动更改笔记的颜色：

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

当[安全模式](../../Advanced%20Usage/Safe%20mode.md)激活时，带有事件的脚本将不会触发。