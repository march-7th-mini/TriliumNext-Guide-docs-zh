# 打印与导出为 PDF

笔记打印由 `note_detail.js` 中的 `printActiveNoteEvent` 方法处理。导出为 PDF 的方式与之类似。

## 工作原理

打印和导出为 PDF 都使用相同的机制：笔记会在一个单独的网页中单独渲染，然后发送到浏览器或 Electron 应用进行打印或导出为 PDF。

渲染单个笔记的网页实际上可以在网络浏览器中访问。例如，`http://localhost:8080/#root/WWRGzqHUfRln/RRZsE9Al8AIZ?ntxId=0o4fzk` 变为 `http://localhost:8080/?print#root/WWRGzqHUfRln/RRZsE9Al8AIZ`。

在网络浏览器中访问打印笔记可以方便地进行调试，以了解为什么某个特定笔记渲染效果不佳。渲染机制与 <a class="reference-link" href="#root/0ESUbbAxVnoK">笔记列表</a> 中使用的机制类似。

## 语法高亮

代码块的语法高亮同样受支持：

*   它通过向打印内容中注入 Highlight.js 样式表来实现。
*   所使用的主题是硬编码的（在撰写本文时为 _Visual Studio Light 主题_），以避免打印时出现深色背景。
*   <a class="reference-link" href="Syntax%20highlighting.md">语法高亮</a> 由内容渲染器处理。