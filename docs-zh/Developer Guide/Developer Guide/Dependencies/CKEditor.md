# CKEditor
*   我们已从使用 Webpack 的旧版 CKEditor 构建迁移，转而使用预编译的 npm 二进制文件。
*   `packages/ckeditor5` 的作用是收集供客户端使用的 CKEditor，其中包含插件定义。
*   Trilium 内部插件（例如“剪切到笔记”、“包含笔记”）位于 `packages/ckeditor5/src/plugins` 中。
*   需要调整的外部 CKEditor 插件位于 `packages/ckeditor5-*` 中。
    *   要集成新插件，请参阅 <a class="reference-link" href="CKEditor/Plugin%20migration%20guide.md">插件迁移指南</a>。