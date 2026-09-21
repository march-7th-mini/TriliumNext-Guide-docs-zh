# 自定义小组件

自定义小组件是脚本的一个特殊子集，用于在应用程序的特定部分渲染图形元素。它们可用于为 Trilium 应用程序添加新功能。

## 使用 JSX 的 Preact 与原生 jQuery 对比

在旧版本的 Trilium 中，自定义小组件完全使用 jQuery 结合 Trilium 的内部小组件架构（例如 `BasicWidget`、`NoteContextAwareWidget`）编写。

从 v0.101.0 开始，自定义小组件也可以使用 <a class="reference-link" href="Preact.md">Preact</a> 框架以 JSX 编写。旧版小组件和 Preact 小组件具有相同的功能，只有一个区别：

*   Preact 小组件默认按内容调整大小，而旧版小组件需要在构造函数中调用 `this.contentSized()`。更多信息请参阅 <a class="reference-link" href="Custom%20Widgets/Troubleshooting.md">故障排除</a> 中的相应章节。

在可能的情况下，小组件示例将同时提供旧版和 Preact 格式。

## 创建自定义小组件

1.  创建一个 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记。
2.  将语言设置为：
    1.  JavaScript (frontend)，用于使用 jQuery 的旧版小组件。
    2.  JSX，用于 Preact 小组件。你可能需要先前往 选项 → 代码 启用该语言。
3.  应用 `#widget` [标签](../../Advanced%20Usage/Attributes/Labels.md)。

## 从简单示例开始

让我们从创建一个在内容区域附近显示消息的小组件开始。按照上一节创建代码笔记，并使用以下内容。

### 旧版（jQuery）

```
class HelloCenterPane extends api.BasicWidget {

    constructor() {
        super();
        this.contentSized();
    }

    get parentWidget() { return "center-pane" }

    doRender() {
        this.$widget = $("<span>Center pane</span>");
    }
    
}

module.exports = new HelloCenterPane();
```

[刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)，该小组件应出现在内容区域下方。

### Preact 版本

```
import { defineWidget } from "trilium:preact";

export default defineWidget({
    parent: "center-pane",
    render: () => <span>Center pane from Preact.</span>
});
```

[刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)，该小组件应出现在内容区域下方。

## 小组件位置（父小组件）

小组件可以放置在应用程序的以下区域之一：

<table class="ck-table-resized">
    <colgroup>
        <col style="width:15.59%;">
        <col style="width:30.42%;">
        <col style="width:16.68%;">
        <col style="width:37.31%;">
    </colgroup>
    <thead>
        <tr>
            <th><code>parentWidget</code> 的值</th>
            <th>描述</th>
            <th>示例小组件</th>
            <th>特殊要求</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th><code>left-pane</code></th>
            <td>出现在包含 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 的同一窗格中。</td>
            <td>与上述相同，仅 <code>parentWidget</code> 不同。</td>
            <td>无。</td>
        </tr>
        <tr>
            <th><code>center-pane</code></th>
            <td>在内容区域中。如果打开了分屏，小组件将横跨所有分屏。</td>
            <td>参见上面的示例。</td>
            <td>无。</td>
        </tr>
        <tr>
            <th><code>note-detail-pane</code></th>
            <td><p>在内容区域中，位于笔记详情区域内。如果打开了分屏，小组件将包含在分屏内。</p><p>如果小组件是特定于笔记的，这是理想选择。</p></td>
            <td><a class="reference-link" href="Custom%20Widgets/Note%20context%20aware%20widget.md">笔记上下文感知小组件</a></td>
            <td><ul><li>小组件必须导出一个 <code>class</code> 而不是类的实例（例如 <code>no new</code>），因为它需要为每个笔记进行多份实例化，以便分屏正常工作。</li><li>由于导出的是 <code>class</code> 而不是实例，<code>parentWidget</code> getter 必须是 <code>static</code>，否则小组件将被忽略。</li></ul></td>
        </tr>
        <tr>
            <th><code>right-pane</code></th>
            <td>在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a> 中，作为一个专用区域。</td>
            <td><a class="reference-link" href="Custom%20Widgets/Right%20pane%20widget.md">右侧窗格小组件</a></td>
            <td><ul><li>虽然不是强制要求，但最好使用 <code>RightPanelWidget</code> 而不是 <code>BasicWidget</code> 或 <code>NoteContextAwareWidget</code>。</li></ul></td>
        </tr>
    </tbody>
</table>

要将小组件放置在其他位置，只需更改旧版小组件中传递给 `get parentWidget()` 的值，或 Preact 中的 `parent` 字段。请注意，某些位置（如 `note-detail-pane` 和 `right-pane`）有需要考虑的特殊要求（见上表）。

## 单个笔记中的多个小组件

一个小组件笔记通常返回一个小组件，但也可以返回一个小组件数组。当多个小组件共享代码或状态时，这很有用，因为它们可以全部放在同一个笔记中，而不必分散在需要共享模块的多个笔记中。

数组中的每个小组件都会单独注册，因此它们可以有不同的父级和位置。缺少 `parentWidget`（或 Preact 中的 `parent`）的小组件会被报告为错误，但不会影响该笔记中的其他小组件。

### 旧版（jQuery）

```
class TreeWidget extends api.BasicWidget {
    get parentWidget() { return "left-pane"; }
    doRender() { this.$widget = $("<span>Left pane</span>"); }
}

class SidebarWidget extends api.BasicWidget {
    get parentWidget() { return "right-pane"; }
    doRender() { this.$widget = $("<span>Right pane</span>"); }
}

module.exports = [ new TreeWidget(), new SidebarWidget() ];
```

### Preact 版本

```
import { defineWidget } from "trilium:preact";

export default [
    defineWidget({
        parent: "left-pane",
        render: () => <span>Left pane from Preact.</span>
    }),
    defineWidget({
        parent: "right-pane",
        render: () => <span>Right pane from Preact.</span>
    })
];
```

## 启动栏小组件

启动栏小组件类似于 _自定义小组件_，但专门用于 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>。更多信息请参阅 <a class="reference-link" href="Launch%20Bar%20Widgets.md">启动栏小组件</a>。

## 自定义位置

自定义小组件的位置通过 `position` 整数定义。

在旧版小组件中：

```
class MyWidget extends api.BasicWidget {
	// [..
	get position() { return 10; }
}
```

在 Preact 小组件中：

```
export default defineWidget({
    // [...]
    position: 10
});
```