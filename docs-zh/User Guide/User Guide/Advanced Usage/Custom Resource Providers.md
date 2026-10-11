# 自定义资源提供器

自定义资源提供器允许任何导入到 Trilium 中的文件（图片、字体、样式表）通过 URL 公开访问。

一个潜在的使用场景是在主题中嵌入自定义字体。

## 创建自定义资源提供器的步骤

1.  通过拖放将图片或字体等文件导入到 Trilium 中。
2.  将[标签](Attributes/Labels.md) `#customResourceProvider` 设置为 `hello`。
3.  要测试是否正常工作，请使用浏览器导航到 `<protocol>://<host>/custom/hello`（其中 `<protocol>` 根据你的设置是 `http` 或 `https`，`<host>` 是你的 Trilium 服务器实例的主机或 IP）。如果你在没有服务器的情况下运行 TriliumNext 应用程序，请使用 `http://localhost:37840` 作为基础 URL。
4.  如果一切顺利，在上一步中浏览器应该已经下载了第一步中上传的文件。

除了 `hello`，名称还可以是：

*   一个路径，例如 `fonts/Roboto.ttf`，可通过 `<host>/custom/fonts/Roboto.ttf` 访问。
*   作为更高级的用例，可以使用正则表达式来匹配多个路由，例如 `hello/.*`，可通过 `/custom/hello/1`、`/custom/hello/2`、`/custom/hello/world` 等访问。

## 在主题中使用

例如，如果你有一个自定义字体需要由主题导入，首先将字体文件上传到 Trilium 并为其分配 `#customResourceProvider=fonts/myfont.ttf` 属性。

然后修改主题 CSS 指向：

```css
@font-face {
	font-family: customFont;
	src: url("/custom/fonts/myfont.ttf");
}

div {
	font-family: customFont;
}
```