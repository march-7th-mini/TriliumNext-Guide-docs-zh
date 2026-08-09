# 将图表导出为 SVG
此机制由 `src/public/app/widgets/floating_buttons/svg_export_button.js` 处理。

## 步骤 1. 启用按钮

修改 `svg_export_button.js` 中的 `isEnabled` 方法，以添加对新笔记类型的支持。

## 步骤 2. 添加对导出图像的支持

SVG 导出需要在笔记类型实现内部进行处理。

首要目标是创建一个方法来处理 <a class="reference-link" href="SVG%20rendering.md">SVG 渲染</a>。如果 SVG 渲染已经处理过，请确保对代码进行去重。

```
async renderSvg() {
    return await this.mind.exportSvg().text();
}
```

然后创建一个事件处理器来管理 SVG 导出：

```
async exportSvgEvent({ntxId}) {
    if (!this.isNoteContext(ntxId) || this.note.type !== "mindMap") {
        return;
    }

    const svg = await this.renderSvg();
    utils.downloadSvg(this.note.title, svg);
}
```

确保修改方法开头的笔记类型断言。这一点非常重要，否则在浏览支持此按钮的多种笔记类型时可能会出现错误。