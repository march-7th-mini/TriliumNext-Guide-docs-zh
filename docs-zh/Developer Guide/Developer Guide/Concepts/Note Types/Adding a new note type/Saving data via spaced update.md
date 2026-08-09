## 通过间隔更新保存数据

数据持久化通过间隔更新机制实现，该机制已存在，需要集成到新创建的类型组件中。

首先，类必须实现 `getData`，以便从自定义组件中以序列化形式检索数据。以下来自思维导图实现的示例：

```
async getData() {
    const mind = this.mind;
    if (!mind) {
        return;
    }

    return {
        content: mind.getDataString()
    };
}
```

此处 `content` 是包含 JSON 的字符串。也可以在此处提供附件，例如 <a class="reference-link" href="SVG%20rendering.md">SVG 渲染</a> 以提供内容的预览。

然后，要触发更新，请在自定义组件内注册一个监听器来调用间隔更新，例如：

```
mind.bus.addListener("operation", (operation) => {
    this.spacedUpdate.scheduleUpdate();
});
```