# 任务管理器

任务管理器是一个[提升属性](../Attributes/Promoted%20Attributes.md)和[脚本](../../Scripting.md)的展示示例，存在于[演示笔记](../Database.md)中。

## 演示

![](Task%20Manager_task-manager.png)

任务管理器管理未完成（TODO）的任务和已完成的任务（非空的 doneDate 属性）。未完成的任务进一步按位置和任意标签进行分类——每当你在任务笔记中更改标签属性时，该任务会自动移动到相应的位置。

任务管理器还与[日记笔记](Day%20Notes.md)集成——笔记会被[克隆](../../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)到日记笔记中，同时进入 todoDate 笔记和 doneDate 笔记（带有"TODO"或"DONE"的[前缀](../../Basic%20Concepts%20and%20Features/Navigation/Tree%20Concepts.md)）。

## 实现方式

新任务在 TODO 笔记中创建，该笔记具有指向任务模板的 `~child:template` [关系](../Attributes.md)（参见[属性继承](../Attributes/Attribute%20Inheritance.md)）。

### 属性

任务模板定义了多个[提升属性](../Attributes/Promoted%20Attributes.md)——todoDate、doneDate、tags、location。重要的是，它还定义了 `~runOnAttributeChange` 关系——在属性变更时运行的[事件](../../Scripting/Backend%20scripts/Backend%20Events.md)处理器。该[脚本](../../Scripting.md)处理例如当我们填写 doneDate 属性时的情况——这意味着任务已完成，应移动到"已完成"笔记，并从 TODO、位置和标签中移除。

### 新建任务按钮

还有一个"按钮"笔记，其中包含一个简单的脚本，用于在 TODO 笔记中添加一个创建新笔记（任务）的按钮。

```
api.addButtonToToolbar({
    title: 'New task',
    icon: 'check',
    shortcut: 'alt+n',
    action: async () => {
        // creating notes is backend (server) responsibility so we need to pass
        // the control there
        const taskNoteId = await api.runOnBackend(async () => {
            const todoRootNote = await api.getNoteWithLabel('taskTodoRoot');
            const {note} = await api.createNote(todoRootNote.noteId, 'new task', '');

            return note.noteId;
        });

        // we got an ID of newly created note and we want to immediatelly display it
        await api.activateNewNote(taskNoteId);
    }
});
```

### CSS

在上面的演示截图中，你可能会注意到 TODO 任务为红色，DONE 任务为绿色。

这是通过以下 CSS [代码笔记](../../Note%20Types/Code.md)实现的，它定义了额外的 CSS 类：

```
span.fancytree-node.todo .fancytree-title {
    color: red !important;
}

span.fancytree-node.done .fancytree-title {
    color: green !important;
}
```

这个[代码笔记](../../Note%20Types/Code.md)具有 `#appCss` [标签](../Attributes.md)，Trilium 在启动时会识别该标签并将其作为 CSS 加载到应用程序中。

该功能的第二部分基于上述事件处理器，它根据任务状态将 `#cssClass` 标签分配给任务，值为"done"或"todo"。