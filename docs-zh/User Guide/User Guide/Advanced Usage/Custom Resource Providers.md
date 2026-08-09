# 自定义资源提供器

自定义资源提供器允许导入到 Trilium 中的任何文件（图片、字体、样式表）通过 URL 公开访问。

一个潜在的使用场景是在主题中嵌入自定义字体。

## 创建自定义资源提供器的步骤

1.  通过拖放将文件（如图片或字体）导入到 Trilium 中。
2.  选择该文件并转到 _自有属性_ 部分。
3.  添加标签 `#customResourceProvider=hello`。
4.  要测试其是否正常工作，请使用浏览器访问 `<协议>://<主机>/custom/hello`（其中 `<协议>` 根据你的设置是 `http` 或 `https`，`<主机>` 是你的 Trilium 服务器实例的主机名或 IP 地址）。如果你在没有服务器的情况下运行 TriliumNext 应用程序，请使用 `http://localhost:37840` 作为基础 URL。
5.  如果一切顺利，在上一步中浏览器应该已经下载了第一步中上传的文件。

除了 `hello`，该名称还可以是：

*   一个路径，例如 `fonts/Roboto.ttf`，可通过 `<主机>/custom/fonts/Roboto.ttf` 访问。
*   作为一个更高级的用例，可以使用正则表达式来匹配多个路由，例如 `hello/.*`，它将可以通过 `/custom/hello/1`、`/custom/hello/2`、`/custom/hello/world` 等路径访问。

## 在主题中使用

例如，如果你有一个自定义字体需要被主题导入，首先将一个字体文件上传到 Trilium，并为其分配 `#customResourceProvider=fonts/myfont.ttf` 属性。

然后修改主题 CSS 以指向：

```css
@font-face {
	font-family: customFont;
	src: url("/custom/fonts/myfont.ttf");
}

div {
	font-family: customFont;
}
```