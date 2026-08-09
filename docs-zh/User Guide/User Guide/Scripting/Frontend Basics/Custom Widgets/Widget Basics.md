# 小组件基础

本指南将引导您在 Trilium 中创建一个基本的小组件。通过遵循这些步骤，您将学习如何构建一个与用户交互的简单 UI 元素。

### 第一步：小组件基本结构

首先，我们将创建尽可能基本的小组件。以下是一个简单示例：

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

1.  在 Trilium 中创建一个新的 `JS 前端` 笔记，并粘贴上述代码。
2.  为[笔记](../../../Basic%20Concepts%20and%20Features/Notes.md)分配 `#widget` [属性](../../../Advanced%20Usage/Attributes.md)。
3.  重启 Trilium 或重新加载窗口。

要验证小组件是否正常工作，请打开开发者工具（<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>）并运行 `document.querySelector("#my-widget")`。如果找到了该元素，则小组件运行正常。如果返回 `undefined`，请仔细检查[笔记](../../../Basic%20Concepts%20and%20Features/Notes.md)是否具有 `#widget` [属性](../../../Advanced%20Usage/Attributes.md)。

### 第二步：添加 UI 元素

接下来，我们通过向小组件添加一个按钮来改进它。

```
const template = `<div id="my-widget"><button>点击我！</button></div>`;

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

进行此更改后，重新加载 Trilium。您现在应该会在左侧面板的左上角看到一个按钮。

### 第三步：为小组件设置样式

为了使按钮更具视觉吸引力并正确定位，我们将应用一些自定义样式。Trilium 包含 [Box Icons](https://boxicons.com)，我们将使用它来用图标替换按钮文本。例如 `bx bxs-magic-wand` 图标。

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

重新加载 Trilium 后，按钮现在应出现在左侧面板的左下角，与其他操作按钮一起。

### 第四步：添加用户交互

让我们通过点击按钮时显示一条消息来使其具有交互性。我们将使用 [脚本 API](../../Script%20API.md) 中的 `api.showMessage` 方法。

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
        this.$widget.find("button").on("click", () => api.showMessage("你好，世界！"));
        return this.$widget;
    }
}

module.exports = new MyWidget();
```

有关 `parentWidget()` 的可能值列表，请参阅 <a class="reference-link" href="../Custom%20Widgets.md">自定义小组件</a>。

最后[重新加载](../../../Troubleshooting/Refreshing%20the%20application.md)应用程序。当您点击按钮时，应出现一条“你好，世界！”消息，确认您的小组件完全正常工作。