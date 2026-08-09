# 自定义组件

自定义组件是脚本的一个特殊子集，用于在应用程序的特定区域渲染图形元素。这些组件可用于为 Trilium 应用程序添加新功能。

## 使用 JSX 的 Preact 与原生 jQuery 对比

在 Trilium 的旧版本中，自定义组件完全使用 jQuery 结合 Trilium 的内部组件架构（例如 `BasicWidget`、`NoteContextAwareWidget`）编写。

从 v0.101.0 版本开始，自定义组件也可以使用 <a class="reference-link" href="Preact.md">Preact</a> 框架以 JSX 编写。传统组件和 Preact 组件具有相同的功能，只有一个区别：

*   Preact 组件默认按内容大小调整，而传统组件需要在构造函数中应用 `this.contentSized()`。更多信息请参阅 <a class="reference-link" href="Custom%20Widgets/Troubleshooting.md">Troubleshooting</a> 中的相应章节。

在可能的情况下，组件示例将同时提供传统格式和 Preact 格式。

## 创建自定义组件

1.  创建一个 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a> 笔记。
2.  将语言设置为：
    1.  对于使用 jQuery 的传统组件，选择 JavaScript（前端）。
    2.  对于 Preact 组件，选择 JSX。您可能需要前往 选项 → 代码 先启用该语言。
3.  应用 `#widget` [标签](../../Advanced%20Usage/Attributes/Labels.md)。

## 从一个简单的示例开始

让我们先创建一个在内容区域附近显示消息的组件。按照上一节创建一个代码笔记，并使用以下内容。

### 传统版本（jQuery）

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

[刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)，组件应出现在内容区域下方。

### Preact 版本

```
import { defineWidget } from "trilium:preact";

export default defineWidget({
    parent: "center-pane",
    render: () => <span>Center pane from Preact.</span>
});
```

[刷新应用程序](../../Troubleshooting/Refreshing%20the%20application.md)，组件应出现在内容区域下方。

## 组件位置（父组件）

组件可以放置在应用程序的以下区域之一：

<table class="ck-table-resized">
    <colgroup>
        <col style="width:15.59%;">
        <col style="width:30.42%;">
        <col style="width:16.68%;">
        <col style="width:37.31%;">
    </colgroup>
    <thead>
        <tr>
            <th><code spellcheck="false">parentWidget</code> 的值</th>
            <th>描述</th>
            <th>示例组件</th>
            <th>特殊要求</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th><code spellcheck="false">left-pane</code></th>
            <td>出现在包含 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 的同一窗格中。</td>
            <td>与上述相同，仅 <code spellcheck="false">parentWidget</code> 不同。</td>
            <td>无。</td>
        </tr>
        <tr>
            <th><code spellcheck="false">center-pane</code></th>
            <td>在内容区域中。如果打开了分屏，组件将横跨所有分屏。</td>
            <td>参见上面的示例。</td>
            <td>无。</td>
        </tr>
        <tr>
            <th><code spellcheck="false">note-detail-pane</code></th>
            <td><p>在内容区域的笔记详情区域内。如果打开了分屏，组件将包含在分屏内部。</p><p>如果组件是特定于笔记的，则此位置是理想选择。</p></td>
            <td><a class="reference-link" href="Custom%20Widgets/Note%20context%20aware%20widget.md">笔记上下文感知组件</a></td>
            <td><ul><li>组件必须导出一个 <code spellcheck="false">class</code> 而不是类的实例（例如 <code spellcheck="false">no new</code>），因为它需要为每个笔记进行复制，以便分屏正常工作。</li><li>由于导出的是 <code spellcheck="false">class</code> 而不是实例，因此 <code spellcheck="false">parentWidget</code> 获取器必须是 <code spellcheck="false">static</code>，否则组件将被忽略。</li></ul></td>
        </tr>
        <tr>
            <th><code spellcheck="false">right-pane</code></th>
            <td>在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a> 中，作为一个专用区域。</td>
            <td><a class="reference-link" href="Custom%20Widgets/Right%20pane%20widget.md">右侧窗格组件</a></td>
            <td><ul><li>虽然不是强制性的，但最好使用 <code spellcheck="false">RightPanelWidget</code> 而不是 <code spellcheck="false">BasicWidget</code> 或 <code spellcheck="false">NoteContextAwareWidget</code>。</li></ul></td>
        </tr>
    </tbody>
</table>

要将组件放置在其他位置，只需更改传递给传统组件的 `get parentWidget()` 或 Preact 组件的 `parent` 字段的值。请注意，某些位置（如 `note-detail-pane` 和 `right-pane`）有需要满足的特殊要求（参见上表）。

## 启动栏组件

启动栏组件与 _自定义组件_ 类似，但特定于 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>。更多信息请参阅 <a class="reference-link" href="Launch%20Bar%20Widgets.md">启动栏组件</a>。

## 自定义位置

自定义组件的位置通过 `position` 整数定义。

在传统组件中：

```
class MyWidget extends api.BasicWidget {
	// [..
	get position() { return 10; }
}
```

在 Preact 组件中：

```
export default defineWidget({
    // [...]
    position: 10
});
```