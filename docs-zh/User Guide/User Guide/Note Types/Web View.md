# Web 视图
## 配置

Web 视图需要知道要渲染哪个 URL，可以通过设置 `webViewSrc` [属性](../Advanced%20Usage/Attributes.md) 来提供，例如：

```
#webViewSrc="https://www.wikipedia.org"
```

URL 需要包含完整的协议头。

## 服务器端与 Electron 中的 Web 视图对比

当通过浏览器而非桌面应用访问 Trilium 时，Web 视图仍会尝试渲染目标网页的内容。然而，由于它运行在浏览器中，与桌面端相比存在不少限制。

更具体地说，相当多的网站反对被嵌入到另一个网站中（从技术上讲，它们带有非许可性的 `X-Frame-Options` 响应头）。Trilium 无法绕过这一点，因此页面将直接渲染失败。

你可以通过右键点击 Trilium 网页 → 检查（元素）并在“控制台”标签页中查找如下错误来进行诊断：

*   `Refused to display 'https://www.google.com/' in a frame because it set 'X-Frame-Options' to 'sameorigin'.`
*   `Refused to frame 'https://duckduckgo.com/' because an ancestor violates the following Content Security Policy directive: "frame-ancestors 'self' https://html.duckduckgo.com".`

有一些网站确实可以正常渲染，例如 `wikipedia.org`。

请注意，我们也在服务器端应用了一些沙箱限制，因此如果你遇到除上述无法解决的 `X-Frame-Options` 问题之外的其他问题，欢迎报告。

在桌面端，我们使用了不同的技术，可以绕过 `iframe`（`webview`）的限制。

## 嵌入到其他笔记类型中

从 v0.104.0 版本开始，Web 视图可以嵌入到其他笔记类型中：

*   <a class="reference-link" href="../Collections/Dashboard.md">仪表板</a>
*   <a class="reference-link" href="Canvas.md">画布</a>
*   <a class="reference-link" href="Text.md">文本</a> 笔记，通过 <a class="reference-link" href="Text/Include%20Note.md">包含笔记</a> 功能。