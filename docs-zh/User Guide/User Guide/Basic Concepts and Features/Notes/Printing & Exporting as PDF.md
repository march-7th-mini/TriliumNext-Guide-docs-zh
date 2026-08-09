# 打印与导出为 PDF

<figure class="image"><img style="aspect-ratio:2023/1488;" src="1_Printing &amp; Exporting as PDF_image.png" width="2023" height="1488"><figcaption>v0.103.0 中引入的打印预览功能截图。</figcaption></figure>

Trilium 允许将笔记打印到真实打印机，或通过<a class="reference-link" href="../../Collections.md">集合</a>为单个笔记或多个笔记生成结构化的 PDF。

请注意，目前并非所有笔记类型都可打印。我们计划在未来增加对更多笔记类型的支持。

打印和导出为 PDF 并非完美无缺。由于技术限制，有时甚至是浏览器或 Electron 的故障，文本在某些情况下可能会出现截断。

## 在桌面上打印笔记或导出为 PDF

> [!NOTE]
> v0.103.0 之前的版本有两个不同的选项，一个用于打印，另一个用于导出为 PDF。随着打印预览的引入，这些功能已统一。

在 Trilium 桌面应用程序中，可以将笔记导出为 PDF。要打印笔记：

*   按下<a class="reference-link" href="../UI%20Elements/Note%20buttons.md">笔记按钮</a>区域中的菜单按钮，然后选择 _打印笔记_。
*   或者，可以通过[键盘快捷键](../Keyboard%20Shortcuts.md)（默认未分配）或通过[命令面板](../Navigation/Jump%20to%20%26%20command%20palette.md)触发打印。

接下来将触发打印预览屏幕。

### 打印预览与打印选项

打印预览对话框允许调整以下打印选项：

*   要使用的打印机
    
    *   _另存为 PDF_ 会生成结构化的 PDF（保留目录，保持文本可选）。优先选择此选项，而不是操作系统自带的虚拟 PDF 打印机。
*   页面方向：_纵向_（默认）或 _横向_。
*   纸张大小
*   将整个内容缩放 10% 到 200%，以更好地适应页面。
*   页边距，可以完全移除或分别调整四个边缘。
*   仅打印部分页面。单个页码用冒号分隔，支持基于连字符的范围（例如 3-5 表示第 3 到 5 页）。

其他交互：

*   _使用系统对话框打印_ 允许设置 Trilium 中不可用的更多选项。

> [!NOTE]
> 此处的大多数选项（打印机和要打印的页面除外）通过<a class="reference-link" href="../../Advanced%20Usage/Attributes.md">属性</a>（例如 `#printLandscape`、`#printPageSize`、`#printScale`、`#printMargins`）在笔记级别进行管理。
> 
> 这意味着打印同一笔记时会恢复打印设置。没有可以为所有笔记配置的默认设置，但可以通过[可继承属性](../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md)实现。

## 在浏览器中打印

此功能允许打印笔记。它既适用于桌面客户端，也适用于 Web 端。

要打印笔记，请选择笔记右侧的 <img src="Printing &amp; Exporting as PDF_image.png" width="29" height="31"> 按钮，然后选择 _打印笔记_。根据笔记的大小和类型，这可能需要几秒钟。之后您将被重定向到系统/浏览器打印对话框。

在服务器或 PWA（移动端）上，由于技术限制，该选项不可用且将被隐藏。

## 报告渲染问题

如果您在生成的 PDF 文件中遇到任何视觉问题（例如表格无法正确适配、文本截断等），请随时[报告问题](../../Troubleshooting/Reporting%20issues.md)。在这种情况下，最好提供一个示例笔记（点击 <img src="Printing &amp; Exporting as PDF_image.png" width="29" height="31"> 按钮，选择导出笔记 → 此笔记及其所有子笔记 → HTML 压缩包）。确保不要意外泄露任何个人信息。

请考虑调整字体大小并使用[分页符](../../Note%20Types/Text/Insert%20buttons.md)来解决布局问题。

> [!TIP]
> 尽管在应用程序的浏览器版本中无法直接导出为 PDF，但仍然可以通过选择 _打印_ 选项并将打印机选择为“另存为 PDF”来生成 PDF（取决于浏览器）。通常，Mozilla Firefox 具有更好的打印功能。

### 自动打开文件

导出 PDF 后，它将自动使用系统默认应用程序打开，以便于预览。

请注意，如果您使用带有 GNOME 桌面环境的 Linux，有时默认应用程序可能看起来不正确（例如在 GIMP 中打开）。这是因为它使用了 GNOME 的“推荐应用程序”列表。

要解决此问题，您可以通过以下命令行更改 PDF 的推荐应用程序。首先，通过 `gio mime application/pdf` 列出可用的应用程序，然后设置所需的应用程序。例如，要使用 GNOME 的 Evince：

```
gio mime application/pdf
```

## 打印多个笔记

自 v0.100.0 起，可以使用<a class="reference-link" href="../../Collections.md">集合</a>一次打印多个笔记：

1.  首先创建一个集合。
2.  将其配置为使用<a class="reference-link" href="../../Collections/List%20View.md">列表视图</a>。
3.  正常打印集合笔记。

生成的集合将包含集合的所有子笔记，同时保持层级结构。

> [!NOTE]
> 并非所有笔记类型在打印或导出为 PDF 时都受支持。遇到不支持的笔记时，将跳过该笔记。最后，如果有任何笔记被跳过，将显示一条消息，并可以查看被跳过笔记的完整列表。与 _约束与限制_ 中描述的相同限制适用。

## 键盘快捷键

可以通过转到<a class="reference-link" href="../UI%20Elements/Options.md">选项</a>中的 _键盘快捷键_ 并为以下操作分配组合键，从键盘触发打印和导出为 PDF：

*   _打印当前笔记_
*   _将当前笔记导出为 PDF_

## 约束与限制

并非所有<a class="reference-link" href="../../Note%20Types.md">笔记类型</a>在打印时都受支持，在这种情况下，_打印_ 和 _导出为 PDF_ 选项将被禁用。

*   对于<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记：
    *   不打印行号。
    *   启用语法高亮，但强制使用默认主题（Visual Studio）。
*   对于<a class="reference-link" href="../../Collections.md">集合</a>，支持以下类型：
    *   <a class="reference-link" href="../../Collections/List%20View.md">列表视图</a>，允许一次打印多个笔记，同时保持层级结构（类似于书籍）。
    *   <a class="reference-link" href="../../Collections/Presentation.md">演示文稿</a>，显示每张幻灯片/子笔记。
        *   支持大多数笔记类型，尤其是具有图像表示的类型，如<a class="reference-link" href="../../Note%20Types/Canvas.md">画布</a>和<a class="reference-link" href="../../Note%20Types/Mind%20Map.md">思维导图</a>。
    *   <a class="reference-link" href="../../Collections/Table.md">表格</a>，以适合打印的方式渲染表格。
        *   过于复杂的表格（尤其是多列表格）可能无法正确适配，但由于分页，支持具有大量行的表格。
        *   请考虑横向打印，或在导出为 PDF 时使用 `#printLandscape`。
    *   其余集合类型不受支持，但我们计划在某个时候添加对所有集合类型的支持。
*   不再支持使用<a class="reference-link" href="../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a>进行打印，而是需要使用自定义的 `printCss` 关系（见下文）。

## 自定义打印 CSS

作为一个高级用例，可以自定义用于打印的 CSS，例如调整字体、大小或页边距。请注意，<a class="reference-link" href="../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a> 不适用于打印。

为此：

*   创建一个 CSS [代码笔记](../../Note%20Types/Code.md)。
*   在要打印的笔记上，应用 `~printCss` 关系指向新创建的 CSS 代码笔记。
*   要将 CSS 应用于多个笔记，请考虑使用[可继承属性](../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md)或<a class="reference-link" href="../../Advanced%20Usage/Templates.md">模板</a>。

例如，将文档的字体从主题或用户定义的字体更改为衬线字体：

```
body {
	--print-font-family: serif;
    --print-font-size: 11pt;
}
```

> [!IMPORTANT]
> 更改 `--print-font-family` 时，请确保更改是在 `body` 级别而不是 `:root` 级别进行的，否则由于特异性规则，更改将不会被应用。

需要说明的是：

*   可以通过使用多个 `~printCss` 关系来添加多个 CSS 笔记。
*   如果指向 `printCss` 的笔记没有正确的笔记类型或 MIME 类型，它将被忽略。
*   如果从使用<a class="reference-link" href="../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a>的先前版本迁移，则无需 `@media print {`，因为样式表仅用于打印。

## 底层机制

打印和导出为 PDF 都使用相同的机制：笔记在单独的网页中单独渲染，然后发送到浏览器或 Electron 应用程序进行打印或导出为 PDF。

渲染单个笔记的网页实际上可以在 Web 浏览器中访问。例如，`http://localhost:8080/#root/WWRGzqHUfRln/RRZsE9Al8AIZ?ntxId=0o4fzk` 变为 `http://localhost:8080/?print#root/WWRGzqHUfRln/RRZsE9Al8AIZ`。

在 Web 浏览器中访问打印笔记可以方便地进行调试，以了解特定笔记为何渲染不佳。渲染机制与<a class="reference-link" href="Note%20List.md">笔记列表</a>中使用的机制类似。

1.  <sup><strong><a href="#fnrefsr779u3zm6">^</a></strong></sup>