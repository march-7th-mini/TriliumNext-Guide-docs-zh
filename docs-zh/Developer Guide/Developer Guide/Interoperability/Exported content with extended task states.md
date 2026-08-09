# 带有扩展任务状态的导出内容

如果你是处理从 Trilium 导出的 HTML 或 Markdown 内容的开发者，以下是关于任务状态如何存储的详细信息。

## HTML 笔记

Trilium 将任务状态标识符存储在待办列表 `<li>` 元素的 `data-trilium-task-state` 属性中。同时也会包含任务状态的标题，以提供可读的备用工具提示（即使未渲染自定义复选框时也会显示）。

```html
<ul class="todo-list">

  <li data-trilium-task-state="urgent" title="Urgent priority">
    <label class="todo-list__label">
      <input type="checkbox" disabled="disabled">
      	<span class="todo-list__label__description">
      		Replace the timing belt
      	</span>
    </label>
  </li>
  
</ul>
```

复选框的图形、颜色和其他细节不包含在 HTML 标记中。它们是在渲染时根据 Trilium 隐藏子树中“任务状态”下的任务状态定义来解析的。

默认任务状态使用以下标识符：

| 标题 | 标识符 | 是否计入已完成 |
| --- | --- | --- |
| 无 | none | 否 |
| 进行中 | doing | 否 |
| 已完成 | done | 是 |
| 可能 | maybe | 否 |
| 已取消 | cancelled | 否 |

## Markdown 笔记

导出的 Markdown 笔记只是在复选框主体内携带与任务状态对应的 Markdown 符号，与编辑器中的显示方式一致。

```html
- [ ] 无
- [/] 进行中
- [X] 已完成
- [?] 可能
- [-] 已取消
```