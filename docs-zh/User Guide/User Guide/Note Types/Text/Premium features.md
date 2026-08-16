# 高级功能

我们使用的文本编辑器是 <a class="reference-link" href="../../Advanced%20Usage/Technologies%20used/CKEditor.md">CKEditor</a>，它拥有开源核心，但同时也是一个提供[高级功能](https://ckeditor.com/docs/trial/latest/index.html)的商业产品。

在 v0.105.0 版本之前，Trilium 根据 CKEditor 与 Trilium 团队之间的签署协议，使用了以下高级功能：

*   <a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>
*   <a class="reference-link" href="Text%20Snippets.md">文本片段</a>
*   <a class="reference-link" href="Format%20Painter.md">格式刷</a>

从 v0.105.0 版本开始，这些功能已被完全重写为自定义的 CKEditor 插件，并采用 AGPL-3.0 许可证。

## 相似功能

有一些高级 CK 功能看起来像 Trilium 的内置功能，但它们是完全不同的：

*   <a class="reference-link" href="In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>
*   <a class="reference-link" href="Math%20Equations.md">数学公式</a>，它使用了已适配 Trilium 的第三方插件。