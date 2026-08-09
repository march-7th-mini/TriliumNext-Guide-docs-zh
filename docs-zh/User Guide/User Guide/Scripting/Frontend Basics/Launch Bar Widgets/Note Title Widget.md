# 笔记标题小组件
<figure class="image"><img style="aspect-ratio:1007/94;" src="Note Title Widget_image.png" width="1007" height="94"></figure>

这是一个笔记上下文感知小组件的示例，它会响应当前打开的笔记，并在用户浏览笔记时自动刷新。

## 旧版小组件

在此示例中，会显示笔记的标题。它最适合在[水平布局](../../../Basic%20Concepts%20and%20Features/UI%20Elements/Vertical%20and%20horizontal%20layout.md)中使用。

```javascript
const TPL = `\
<div style="
    display: flex;
    height: 53px;
    width: fit-content;
    font-size: 0.75em;
    contain: none;
    align-items: center;
    flex-shrink: 0;
    padding: 0 1em;
"></div>`;

class NoteTitleWidget extends api.NoteContextAwareWidget {
    doRender() {
        this.$widget = $(TPL);
    }

    async refreshWithNote(note) {
        this.$widget.text(note.title);
    }
}

module.exports = new NoteTitleWidget();
```

## Preact 小组件（v0.101.0+）

```jsx
import { defineLauncherWidget, useActiveNoteContext } from "trilium:preact";

export default defineLauncherWidget({
    render: () => {
        const { note } = useActiveNoteContext();
        return <div style={{
            display: "flex",
            height: "53px",
            width: "fit-content",
            fontSize: "0.75em",
            alignItems: "center",
            flexShrink: 0            
        }}>{note?.title}</div>;
    }
});
```