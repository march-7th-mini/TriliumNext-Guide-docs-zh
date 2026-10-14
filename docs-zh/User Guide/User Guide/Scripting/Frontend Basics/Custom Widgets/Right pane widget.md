# 右侧面板小组件
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

一个简单的小组件，用于显示当前时间，作为如何定期动态更改小组件内容的示例。

=== "<span class="tn-icon bx bxl-react"></span> Preact"

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

=== "<span class="tn-icon bx bxl-javascript"></span> Legacy"

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

## 调整侧边栏中的位置

默认情况下，侧边栏项目按照应用程序搜索 `#widget` 笔记时找到的顺序显示。

可以通过调整小组件的 `position` 属性，使其显示在更高或更低的位置：

=== "<span class="tn-icon bx bxl-react"></span> Preact"

    ```javascript
    import { defineWidget, RightPanelWidget, useEffect, useState } from "trilium:preact";

    export default defineWidget({
    	/* [...] */
        position: 20,
        render() {
    		/* [...] */
        }
    });
    ```

=== "<span class="tn-icon bx bxl-javascript"></span> Legacy"

    ```javascript
    class MyWidget extends api.RightPanelWidget {

        get position() { return 20 };
            
    }
    ```

通常默认位置从 10 开始，每个项目递增 10，包括默认的目录和高亮列表。

## 旧版小组件的关键要点

*   不能覆盖 `doRender`，而必须覆盖 `doRenderBody()`。
    *   `doRenderBody` 可以选择性地设为 `async`。
*   `parentWidget()` 必须设置为 `“rightPane”`。
*   `widgetTitle()` getter 可以选择性地覆盖，否则小组件将显示为“Untitled widget”。