# SVG 渲染

对于图表及类似的笔记类型，缓存内容的 SVG 渲染是有意义的，这样它可以用于：

*   笔记列表中的内容预览（从父笔记查看笔记列表时）。
*   笔记包含
*   分享

## 步骤 1. 将 SVG 内容保存为附件

第一步是从所使用的自定义组件中获取 SVG。例如，对于 Mind Elixir，有一个 `exportSvg` 方法。

如果返回的值是一个 `Blob`，那么可以通过 `await blob.text()` 获取底层文本。

要将 SVG 作为附件与内容一起保存，只需修改 `getData()`：

```
async getData() {
    const mind = this.mind;
    if (!mind) {
        return;
    }

    const svgContent = await this.mind.exportSvg().text();   
    return {
        content: mind.getDataString(),
        attachments: [
            {
                role: "image",
                title: "mindmap-export.svg",
                mime: "image/svg+xml",
                content: svgContent,
                position: 0
            }
        ]
    };
}
```

您可以通过对笔记进行更改，然后使用笔记菜单中的“笔记附件”选项来测试此步骤。

## 步骤 2. 调整服务器以提供 SVG 附件

`src/routes/api/image.ts` 路由负责提供图片笔记的图像预览，也负责提供自定义笔记类型（如画布）的预览。

按如下方式修改 `returnImageInt` 方法：

1.  将图片类型添加到守护条件中，该条件对不支持的笔记类型返回 400。
2.  添加一个 `if` 语句，使用正确的名称渲染附件：

```
if (image.type === "mindMap") {
	renderSvgAttachment(image, res, 'mindmap-export.svg');
}
```

## 步骤 3. 为笔记预览提供 SVG 附件

客户端也需要调整，以允许其通过调用先前修改的服务器路由来渲染 SVG 附件。

`src/public/app/services/content_renderer.js` 文件负责处理预览。要使用图片路由进行渲染，请修改 `getRenderedContent`，将新的笔记类型添加到调用 `renderImage` 的 `if` 中。

## 步骤 4. 为分享提供 SVG

默认情况下，当尝试通过分享访问给定笔记时，会显示 `无法显示笔记类型`。

要提供 SVG，请打开 `src/share/content_renderer.ts` 并查找 `getContent`。然后，将新的笔记类型添加到包含 `renderImage` 的 `if` 中。

这还不够，因为尝试访问共享笔记会导致图片损坏，并出现 `请求的笔记不是可共享的图片` 错误。要解决此问题，请转到 `src/share/routes.ts`，并在 `router.get('/share/api/images/[...]')` 中添加一个 `renderImageAttachment` 语句。

## 步骤 5. 为修订提供 SVG

在修订列表中，要显示 SVG，请转到 `src/public/app/widgets/dialogs/revisions.js` 并查找 `renderContent` 方法。只需将笔记类型添加到现有的某个 `if` 中，例如用于 `canvas` 和 `mindMap` 或 `mermaid` 的 `if`（如果也应显示图表的文本内容）。