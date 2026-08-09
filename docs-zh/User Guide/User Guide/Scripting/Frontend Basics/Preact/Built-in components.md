# 内置组件
<figure class="image image_resized" style="width:54.58%;"><img style="aspect-ratio:896/712;" src="Built-in components_image.png" width="896" height="712"><figcaption>来自小组件展示示例的部分截图（见下文）。</figcaption></figure>

Trilium 自带一套 Preact 组件，其中一些也可用于<a class="reference-link" href="../Custom%20Widgets.md">自定义小组件</a>和<a class="reference-link" href="../../../Note%20Types/Render%20Note.md">渲染笔记</a>。

要使用这些组件，只需从 `trilium:preact` 导入它们：

```jsx
import { ActionButton, Button, LinkButton } from "trilium:preact";
```

然后使用它们：

```jsx
export default function MyRenderNote() {
    const onClick = () => showMessage("A button was pressed");
    
    return (
        <>
            <h2>按钮</h2>
            <div style={{ display: "flex", gap: "1em", alignItems: "center" }}>
                <ActionButton icon="bx bx-rocket" text="操作按钮" onClick={onClick} />
                <Button icon="bx bx-rocket" text="简单按钮" onClick={onClick} />
                <LinkButton text="链接按钮" onClick={onClick} />                
            </div>
        </>
    )
}
```

## 小组件展示

> [!TIP]
> 从 v0.101.0 版本开始，小组件展示也可在<a class="reference-link" href="../../../Advanced%20Usage/Database/Demo%20Notes.md">演示笔记</a>中找到。

这是一个带有 JSX 的<a class="reference-link" href="../../../Note%20Types/Render%20Note.md">渲染笔记</a>示例，展示了大多数可供自定义小组件和 JSX 渲染笔记使用的内置组件。

要使用它，只需：

1.  创建一个渲染笔记。
2.  创建一个 JSX 类型的子代码笔记，内容为此文件：<a class="reference-link" href="Built-in%20components/Widget%20showcase.jsx">小组件展示</a>
3.  将父笔记的 `~renderNote` 关系设置为子笔记。
4.  刷新渲染笔记以查看结果。