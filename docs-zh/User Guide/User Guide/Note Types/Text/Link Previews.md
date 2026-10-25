# 链接预览
链接预览可将粘贴的 URL 转换为一个丰富的、可感知元数据的小组件，并支持三种视觉模式显示：

## 显示模式

链接预览可以以下列三种模式之一显示：

*   **内联** — 显示网站图标和页面标题的链接（与<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>非常相似）。当你希望链接与周围段落自然衔接时使用此模式。
*   **卡片** — 块级预览，包含缩略图、标题、描述和站点名称。当链接是段落的焦点时使用此模式。
*   **嵌入** — 块级交互式嵌入。
    *   目前支持 YouTube 视频，可交互式渲染（通过 `iframe`）。
    *   为防止不必要的远程请求，视频仅在首次点击后才会显示。

<div class="trilium-multicolumn-layout" data-trilium-column-ratios="1-1-1">
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:251/42;" src="Link Previews_image.png" width="251" height="42"><figcaption><em>内联</em>链接预览</figcaption></figure>

</div>
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:1217/196;" src="2_Link Previews_image.png" width="1217" height="196"><figcaption><em>卡片</em>链接预览</figcaption></figure>

</div>
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:994/563;" src="1_Link Previews_image.png" width="994" height="563"><figcaption><em>嵌入</em>链接预览</figcaption></figure>

</div>
</div>

## 插入链接预览

有三种创建方式：

### 1\. 通过粘贴 URL

链接预览会自动创建：

*   通过粘贴 URL 并按 <kbd>Space</kbd>。这将创建一个_内联_链接预览。
*   当位于新段落的开头时，按 <kbd>Enter</kbd> 将为 YouTube URL 创建_卡片_或_嵌入_。

要撤销自动创建的链接预览，请立即按 <kbd>Ctrl</kbd>+<kbd>Z</kbd>，这样它就会保持为普通链接。或者，在创建链接预览后，点击该链接并从链接预览工具栏中选择_普通链接_。

可以通过转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_，并在_功能_部分取消勾选_自动生成链接预览_来禁用此自动转换。

如果 Trilium 服务器无法访问该链接（或网络请求因任何其他原因失败），则不会将其转换为链接预览。

> [!NOTE]
> 仅当粘贴的文本_就是_ URL 时才会自动转换。带有显示名称的链接（例如 [Trilium Notes website](https://triliumnotes.org)）会保留为普通链接。

### 2\. 通过使用“链接预览”工具栏按钮或斜杠命令

点击格式工具栏中的_链接预览_（<span class="tn-icon cke cke-trilium-link-preview"></span>）以打开_链接预览_弹出窗口。粘贴 URL 并选择预览类型。

或者，使用<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>并查找_链接预览_（也可以通过_嵌入_、_url_ 或_视频_找到），这将在光标处打开相同的弹出窗口。

### 3\. 通过从网页剪藏器保存浏览器标签页

当<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏器</a>保存窗口的标签页时，每个标签页都会变成一个_内联_链接预览，显示浏览器为其显示的标题和网站图标。由于此数据来自浏览器，登录后的页面会保留其真实标题，并且 Trilium 服务器不会联系已保存的页面。

当_自动生成链接预览_关闭时，标签页将改为保存为普通链接列表。

## 修改现有链接预览

点击已插入的链接预览以选中它，将出现一个小工具栏，包含以下选项：

*   常规链接操作（在新标签页中打开、复制链接、取消链接）。
*   用于编辑链接预览标题的按钮。当标题被登录界面遮挡时，此功能特别有用。
*   在链接预览模式（内联、卡片或嵌入）之间切换，以及将其转换为普通链接的方式。
    *   仅当 URL 指向受支持的服务（目前为 YouTube）时，嵌入选项才会启用。

## 预览数据的来源

当你插入链接预览时，Trilium 会获取一次元数据并将其存储在笔记的 HTML 中：

*   **YouTube URL** — 标题、频道名称和缩略图通过 YouTube 的公共 oEmbed 端点获取。
*   **所有其他 URL** — Trilium 会获取页面并读取 OpenGraph 标签（`og:title`、`og:description`、`og:image`、`og:site_name`），并回退到页面的 `<title>` 和 `<meta name="description">`。网站的图标会被下载并内联。

由于数据存储在笔记本身中，因此当你重新打开笔记、共享/发布它或导出为 HTML 时，链接预览会继续正确渲染——无需任何进一步的网络请求。

元数据是在**插入时**捕获的，不会自动刷新。如果链接的页面之后更改了标题或缩略图，你需要重新插入链接以获取新值。要刷新链接，只需重新创建它即可。

当访问<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>时，数据由服务器而非客户端从远程 URL 获取。

## 已知限制

*   嵌入显示模式目前仅支持 YouTube。其他视频和媒体平台会回退到卡片预览。
*   阻止自动获取的页面可能会产生最小化的预览（仅主机名）。
*   链接预览需要 Trilium 服务器能够访问目标 URL，因此对于服务器无法访问的网络上的页面，它们不会生成预览。