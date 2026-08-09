# 使用提升属性配置脚本

提升属性的一个很好的用例是轻松定义脚本可能需要的各种参数，例如处理数据时的输入和输出笔记，或者用于定义脚本行为特定变化的复选框。

![](Using%20promoted%20attributes%20to%20configure%20scripts_image.png)

## 使用复选框切换标志

与其要求用户在脚本中修改布尔值，不如使用复选框作为提升属性，这样更直观。

为此，首先定义提升属性：

```
#label:groupByExtension="promoted,alias=Group by extension,single,boolean"
```

然后使用它：

```javascript
const byExtension = api.currentNote.getLabelValue("groupByExtension") === "true";
if (byExtension) {
	// 执行某些操作。
}
```

这在前端和后端脚本中都能同样良好地工作。

## 使用关系选择笔记

脚本的一个常见用例是从另一个笔记读取数据，并可能将结果输出到另一个笔记中。为此，我们需要定义以下提升属性：

```
#relation:input="promoted,alias=Input,single" #relation:output="promoted,alias=Output,single"
```

一旦我们有了这个，我们可以添加一些基本的错误处理，以确保用户填写了这些字段：

```javascript
const inputNoteId = api.currentNote.getRelationValue("input");
if (!inputNoteId) {
	api.showError("缺少输入。");
    return;
}

const outputNoteId = api.currentNote.getRelationValue("output");
if (!outputNoteId) {
    api.showError("缺少输出。");
    return;
}
```

请注意，这里我们使用了 `api.showError`，它仅适用于前端笔记。如果你正在编写后端笔记，只需移除 `api.showError`，但用户将不会收到关于脚本为何未正确执行的反馈。

之后，我们可以简单地读取笔记并对其进行操作：

```javascript
const note = api.getNote(inputNoteId);
if (!note) {
	return;
}
const content = note.getContent().toString("utf-8");
```