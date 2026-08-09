# 笔记上下文感知小组件

笔记上下文感知小组件是一种特殊类型的小组件，它会自动响应当前笔记的变化。

重要方面：

*   小组件必须导出一个 `class`，而不是类的实例（例如，不要使用 `new`），因为它需要为每个笔记进行复制，以便拆分功能正常工作。
*   由于导出的是 `class` 而不是实例，`parentWidget` 获取器必须是 `static`，否则该小组件将被忽略。

## 显示当前笔记标题的示例

这是一个笔记上下文感知小组件，它简单地显示当前笔记的名称。

### 经典示例

```
class HelloNoteDetail extends api.NoteContextAwareWidget {

    constructor() {
        super();
        this.contentSized();
    }

    doRender() {
        this.$widget = $("<div>");
    }

    async refreshWithNote(note) {
        this.$widget.text("Current note: " + note.title);
    }
    
    static get parentWidget() { return "note-detail-pane" }    
    get position() { return 10 }
    
}

module.exports = HelloNoteDetail;
```

### Preact（v0.101.0+）

```
import { defineWidget, useNoteContext, useNoteProperty } from "trilium:preact";

export default defineWidget({    
    parent: "note-detail-pane",
    position: 10,
    render: () => {
        const { note } = useNoteContext();
        const title = useNoteProperty(note, "title");
        return <span>Current note JSX: {title}</span>;
    }
});
```