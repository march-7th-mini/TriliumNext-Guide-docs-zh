好的，这是您要求的 Markdown 文档的简体中文翻译：

---

# 在 Trilium 中创建自定义小组件

Trilium 提供了一种创建自定义小组件的机制，这些小组件可以显示在应用程序的不同区域，例如侧边栏或属性面板中。

## 创建自定义小组件

自定义小组件是通过创建类型为 `自定义小组件` 的笔记来定义的。此笔记的内容必须是 JavaScript 代码，并且必须导出一个返回 HTML 字符串（或 HTML 元素）的函数。

```javascript
class MyWidget extends api.NoteAwareScript {
    getWidget() { return { render: () => this.render() }; }

    render() {
        return `<div>Hello, world!</div>`;
    }
}

module.exports = MyWidget;
```

## 小组件类型

有几种类型的小组件：

*   **`widget`** - 在应用程序的各个区域中渲染。
*   **`dock`** - 渲染为可停靠的面板。

## 小组件位置

小组件的位置由 `widget` 属性决定。可能的值有：

*   `sidebar` - 在左侧边栏中渲染。
*   `properties` - 在属性面板中渲染。
*   `editor` - 在编辑器顶部渲染。
*   `context-menu` - 在上下文菜单中渲染。

## 小组件 API

自定义小组件可以使用 `api` 对象，该对象提供了与 Trilium 交互的方法。例如，`api.NoteAwareScript` 类提供了对当前笔记的访问。

## 示例

### 显示当前笔记标题的小组件

```javascript
class MyWidget extends api.NoteAwareScript {
    getWidget() { return { render: () => this.render() }; }

    render() {
        return `<div>当前笔记：${this.note.title}</div>`;
    }
}

module.exports = MyWidget;
```

### 显示当前笔记属性的小组件

```javascript
class MyWidget extends api.NoteAwareScript {
    getWidget() { return { render: () => this.render() }; }

    render() {
        const attributes = this.note.getAttributes();
        let html = '<ul>';
        for (const attr of attributes) {
            html += `<li>${attr.name}: ${attr.value}</li>`;
        }
        html += '</ul>';
        return html;
    }
}

module.exports = MyWidget;
```

## 刷新小组件

当笔记发生变化时，小组件会自动刷新。您也可以使用 `api.refreshWidgets()` 方法手动刷新所有小组件。

## 故障排除

*   确保您的 JavaScript 代码没有错误。
*   确保您导出了正确的类。
*   确保 `widget` 属性设置正确。
*   检查后端日志中是否有错误。

## 高级主题

*   [自定义小组件 API](custom-widget-api.md)
*   [小组件样式](widget-styling.md)

---

**注意：** 这是一个高级功能，需要对 JavaScript 和 Trilium 的 API 有很好的理解。