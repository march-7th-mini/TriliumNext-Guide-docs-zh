# “新建任务”启动器按钮
> [!WARNING]
> 本文档已过时，因为它引用了已弃用的 `addButtonToToolbar` API，该 API 只会为桌面端创建小组件。
> 
> 取而代之，可以使用 <a class="reference-link" href="../Launch%20Bar%20Widgets.md">启动栏小组件</a> 文档来创建自定义启动器小组件。

在本示例中，我们将通过向 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>（![](New%20Task%20launcher%20button_image.png)）添加一个按钮，来扩展 <a class="reference-link" href="../../../Advanced%20Usage/Advanced%20Showcases/Task%20Manager.md">任务管理器</a> 展示（Trilium 默认自带）的功能，从而自动创建新任务并打开它。

## 创建笔记

1.  首先，创建一个新的 <a class="reference-link" href="../../../Note%20Types/Code.md">代码</a> 笔记类型，语言选择 _JavaScript (Trilium frontend)_。
2.  在 <a class="reference-link" href="../../../Advanced%20Usage/Attributes.md">属性</a> 中定义 `#run=frontendStartup` 标签。

## 脚本内容

复制粘贴以下脚本：

```javascript
api.addButtonToToolbar({
	title: "New task",
    icon: "task",
    shortcut: "alt+n",
    action: async () => {
    	const taskNoteId = await api.runOnBackend(() => {
        	const todoRootNote = api.getNoteWithLabel("taskTodoRoot");
            const resp = api.createTextNote(todoRootNote.noteId, "New task", "")           
            return resp.note.noteId;
        });
        
        await api.waitUntilSynced();
        await api.activateNewNote(taskNoteId);
    }
});
```

## 测试功能

由于我们将脚本设置为在启动时运行，我们只需要 [刷新应用程序](../../../Troubleshooting/Refreshing%20the%20application.md)。

## 理解脚本的工作原理

<table class="ck-table-resized">
    <colgroup>
        <col style="width:50%;">
        <col style="width:50%;">
    </colgroup>
    <tbody>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">api.addButtonToToolbar({
	title: "New task",
    icon: "task",
    shortcut: "alt+n",
    action: async () =&gt; {
    	// [...]
    }
});</code></pre></td>
            <td><p>这里使用了 <a href="../../Frontend%20Basics.md">前端 API</a> 在 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a> 中创建一个图标，通过指定：</p><ul><li>标题</li><li>对应的 boxicons 图标（不带 <code>bx-</code> 前缀）。</li><li>可选地，为其分配一个键盘快捷键。</li><li>操作，即按下按钮时将执行的内容。</li></ul></td>
        </tr>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">const taskNoteId = await api.runOnBackend(() =&gt; {
    // Shown below.           
    return resp.note.noteId;
});</code></pre></td>
            <td><ul><li>这部分代码实际上是在服务器（后端）上执行的，而不是在客户端（即浏览器）上。<ul><li>原因是创建笔记是服务器的职责。</li></ul></li><li>这里我们还可以看到，可以从服务器执行中返回结果并在客户端中读取它们（<code>taskNoteId</code>）。</li></ul></td>
        </tr>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">const todoRootNote = api.getNoteWithLabel("taskTodoRoot");</code></pre></td>
            <td><ul><li>这里我们通过 <a href="../../../Advanced%20Usage/Attributes.md">标签</a> <code>#taskTodoRoot</code> 来识别一个笔记。这就是 <a class="reference-link" href="../../../Advanced%20Usage/Advanced%20Showcases/Task%20Manager.md">任务管理器</a> 展示知道在哪里放置各种任务的方式。</li><li>通常，如果无法识别到这样的笔记，这可能会返回 <code>null</code> 值，但错误处理超出了本示例的范围。</li></ul></td>
        </tr>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">const resp = api.createTextNote(todoRootNote.noteId, "New task", "")</code></pre></td>
            <td><ul><li>我们在待办根笔记（第一个参数）中创建一个新的子笔记，标题为“New task”（第二个参数），默认无内容（第三个参数）。</li></ul></td>
        </tr>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">await api.waitUntilSynced();</code></pre></td>
            <td><ul><li>回到客户端，由于我们在服务器上创建了一个新笔记，现在需要等待更改反映到客户端。</li></ul></td>
        </tr>
        <tr>
            <td><pre><code class="language-text-x-trilium-auto">await api.activateNewNote(taskNoteId);</code></pre></td>
            <td><ul><li>由于我们知道新创建笔记的 <a href="../../../Advanced%20Usage/Note%20ID.md">ID</a>，现在只需向用户显示此笔记即可。</li></ul></td>
        </tr>
    </tbody>
</table>