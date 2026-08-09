# 右侧面板小组件
## 关键要点

*   `doRender` 不得被重写，而应重写 `doRenderBody()`。
    *   `doRenderBody` 可以选择性地为 `async`。
*   `parentWidget()` 必须设置为 `"rightPane"`。
*   `widgetTitle()` 获取器可以选择性地被重写，否则小组件将显示为“未命名小组件”。

## 新布局示例

> [!IMPORTANT]
> 本节内容针对为 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>（自 v0.101.0 起可用）量身定制的示例，其中右侧面板小组件/侧边栏不再根据其包含的小组件来显示或隐藏。

### 标题小组件

这是一个上下文感知小组件的示例，用于显示当前笔记的标题：

```
class NoteTitleWidget extends api.RightPanelWidget {
    
    get widgetTitle() { return "Note title"; }
    get parentWidget() { return "right-pane" }

    doRenderBody() {
        this.$body.empty();
        if (this.note) {
            this.$body.append($("<div>").text(this.note.title));
        }
    }   
    
    async refreshWithNote() {
    	this.doRenderBody();
    }
}

module.exports = new NoteTitleWidget();
```

### 时钟

一个显示当前时间的简单小组件，作为如何定期动态更改小组件内容的示例。

### 旧式小组件

```
const template = `<div></div>`;

class ToDoListWidget extends api.RightPanelWidget {
    
    get widgetTitle() { return "Clock"; }        
    get parentWidget() { return "right-pane" }
    
    async doRenderBody() {
        if (!this.timer) {
            this.timer = setInterval(() => {
                this.$body.empty().append(`The time is: <span>${new Date().toLocaleString()}</span>`);                       
            }, 1000);            
        }

        this.$body.empty().append(`The time is: <span>${new Date().toLocaleString()}</span>`);
    }   
}

module.exports = new ToDoListWidget();
```

### Preact 小组件

```
import { defineWidget, RightPanelWidget, useEffect, useState } from "trilium:preact";

export default defineWidget({
    parent: "right-pane",    
    position: 1,
    render() {
        const [ time, setTime ] = useState();
        useEffect(() => {
            const interval = setInterval(() => {
                setTime(new Date().toLocaleString());
            }, 1000);
            return () => clearInterval(interval);
        });        
        return (
            <RightPanelWidget id="clock-jsx" title="Clock (JSX)">
                <p>The time is: {time}</p>
            </RightPanelWidget>
        );
    }
});
```

## 旧布局示例

这是一个显示基本消息（“Hi”）的小组件：

```
const template = `<div>Hi</div>`;

class HelloWorldWidget extends api.RightPanelWidget {
    
    get widgetTitle() {
        return "Title goes here";
    }
        
    get parentWidget() { return "right-pane" }
    
    doRenderBody() {
        this.$body.empty().append($(template));
    }   
    
    async refreshWithNote(note) {
    	// Do something when the note changes.
    }
}

module.exports = new HelloWorldWidget();
```

### 条件性更改可见性

在 `refreshWithNote` 中：

```
const visible = true;	// replace with your own visibility logic
this.toggleInt(visible);
this.triggerCommand("reEvaluateRightPaneVisibility");
```

## 更改侧边栏内的位置

默认情况下，侧边栏项目按照应用程序在搜索 `#widget` 笔记时找到它们的顺序显示。

可以通过调整小组件的 `position` 属性来使其显示在更高或更低的位置：

```
class MyWidget extends api.RightPanelWidget {

+    get position() { return 20 };
        
}
```

通常，默认位置从 10 开始，每个项目（包括默认的目录和亮点列表）依次增加 10。