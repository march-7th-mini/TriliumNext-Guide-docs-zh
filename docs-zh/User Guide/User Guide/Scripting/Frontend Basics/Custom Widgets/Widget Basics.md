# 小组件基础
本指南将引导你在 Trilium 中创建一个基础小组件。按照以下步骤操作，你将学会如何构建一个与用户交互的简单 UI 元素。

### 第 1 步：基础小组件结构

首先，我们将创建最基础的小组件。以下是一个简单示例：

```
class MyWidget extends api.BasicWidget {
    get position() { return 1; }
    get parentWidget() { return "left-pane"; }
    
    doRender() {
        this.$widget = $("<div id='my-widget'>");
        return this.$widget;
    }
}

module.exports = new MyWidget();
```

要实现此小组件：

1.  在 Trilium 中创建一个新的 `JS Frontend` 笔记，并粘贴上面的代码。
2.  为[笔记](../../../Basic%20Concepts%20and%20Features/Notes.md)分配 `#widget` [属性](../../../Advanced%20Usage/Attributes.md)。
3.  重启 Trilium 或重新加载窗口。

要验证小组件是否正常工作，请打开开发者工具（<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>）并运行 `document.querySelector("#my-widget")`。如果找到了该元素，则小组件运行正常。如果返回 `undefined`，请仔细检查[笔记](../../../Basic%20Concepts%20and%20Features/Notes.md)是否具有 `#widget` [属性](../../../Advanced%20Usage/Attributes.md)。

### 第 2 步：添加 UI 元素

接下来，我们通过向小组件添加一个按钮来改进它。

```
const template = `<div id="my-widget"><button>Click Me!</button></div>`;

class MyWidget extends api.BasicWidget {
    get position() {return 1;}
    get parentWidget() {return "left-pane"}

    doRender() {
        this.$widget = $(template);
        return this.$widget;
    }
}

module.exports = new MyWidget();
```

做出此更改后，重新加载 Trilium。你现在应该能在左侧窗格的左上角看到一个按钮。

### 第 3 步：为小组件设置样式

为了让按钮在视觉上更具吸引力并正确定位，我们将应用一些自定义样式。Trilium 包含 [Box Icons](https://boxicons.com)，我们将使用它来将按钮文本替换为图标。例如 <span class="tn-icon bx bxs-magic-wand"></span> `bx bxs-magic-wand` 图标。

以下是更新后的模板：

```
const template = `<div id="my-widget"><button class="tree-floating-button bx bxs-magic-wand tree-settings-button"></button></div>`;
```

接下来，我们将使用 CSS 调整按钮的位置：

```
class MyWidget extends api.BasicWidget {
    get position() { return 1; }
    get parentWidget() { return "left-pane"; }
    
    doRender() {
        this.$widget = $(template);
        this.cssBlock(`#my-widget {
            position: absolute;
            bottom: 40px;
            left: 60px;
            z-index: 1;
        }`);
        return this.$widget;
    }
}

module.exports = new MyWidget();
```

重新加载 Trilium 后，按钮现在应出现在左侧窗格的左下角，与其他操作按钮并排。

### 第 4 步：添加用户交互

让我们通过在被点击时显示一条消息来使按钮具有交互性。我们将使用[脚本 API](../../Script%20API.md) 中的 `api.showMessage` 方法。

```
class MyWidget extends api.BasicWidget {
    get position() { return 1; }
    get parentWidget() { return "left-pane"; }
    
    doRender() {
        this.$widget = $(template);
        this.cssBlock(`#my-widget {
            position: absolute;
            bottom: 40px;
            left: 60px;
            z-index: 1;
        }`);
        this.$widget.find("button").on("click", () => api.showMessage("Hello World!"));
        return this.$widget;
    }
}

module.exports = new MyWidget();
```

有关 `parentWidget()` 可能值的列表，请参阅<a class="reference-link" href="../Custom%20Widgets.md">自定义小组件</a>。

最后一次[重新加载](../../../Troubleshooting/Refreshing%20the%20application.md)应用程序。当你点击按钮时，应出现一条“Hello World!”消息，确认你的小组件完全正常工作。