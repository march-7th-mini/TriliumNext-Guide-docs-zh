# 钩子
## 标准 Preact 钩子

所有标准的 Preact 钩子都可以通过 `trilium:api` 导入使用。

例如：

```jsx
import { useState } from "trilium:preact";
const [ myState, setMyState ] = useState("Hi");
```

## 自定义钩子

Trilium 附带了一大套用于 Preact 的自定义钩子，所有这些钩子也可用于自定义小组件和 <a class="reference-link" href="../../../Note%20Types/Render%20Note.md">渲染笔记</a>。

### `useNoteContext`

作为 <a class="reference-link" href="../Custom%20Widgets/Note%20context%20aware%20widget.md">笔记上下文感知小组件</a>的替代方案，Preact 在 `useNoteContext` 钩子中暴露了当前的笔记上下文：

```jsx
import { defineWidget, useNoteContext, useNoteProperty } from "trilium:preact";

export default defineWidget({    
    parent: "note-detail-pane",
    position: 10,
    render: () => {
        const { note } = useNoteContext();
        const title = useNoteProperty(note, "title");
        return <span>当前笔记 JSX：{title}</span>;
    }
});
```

请注意，自定义小组件必须位于内容区域内（即笔记详情小组件），这样才能正常工作，尤其是在处理分屏时。

### `useActiveNoteContext`

`useActiveNoteContext` 是 `useNoteContext` 的替代方案，即使小组件不在笔记详情部分内也能正常工作，并且当用户在标签页和分屏之间导航时，它会自动切换笔记上下文。

### `useNoteProperty`

此钩子允许“监听” `FNote` 特定属性的变化，例如笔记的 `title` 或 `type`。使用此钩子的好处是它能够实际响应变化，例如当笔记标题或类型被更改时。