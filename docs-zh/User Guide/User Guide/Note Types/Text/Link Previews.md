# 链接预览

链接预览可将粘贴的 URL 转换为一个丰富的、可感知元数据的小组件，并支持三种视觉模式显示：

## 显示模式

链接预览可通过以下三种模式之一显示：

*   **行内** — 显示网站图标和页面标题的链接（与<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>非常相似）。当你希望链接与周围段落自然衔接时使用此模式。
*   **卡片** — 块级预览，包含缩略图、标题、描述和网站名称。当链接是段落的焦点时使用此模式。
*   **嵌入** — 块级交互式嵌入。
    *   目前支持 YouTube 视频，可交互式渲染（通过 `iframe`）。
    *   为防止不必要的远程请求，视频仅在首次点击后才会显示。在此之前，会显示视频缩略图和播放按钮。

<div class="trilium-multicolumn-layout" data-trilium-column-ratios="1-1-1">
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:251/42;" src="Link Previews_image.png" width="251" height="42"><figcaption><em>行内</em>链接预览</figcaption></figure>

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

*   通过粘贴 URL 并按 <kbd>Space</kbd>。这将创建一个_行内_链接预览。
*   当位于新段落的开头时，按 <kbd>Enter</kbd> 将为 YouTube URL 创建_卡片_或_嵌入_。

要撤销自动创建的链接预览，请立即按 <kbd>Ctrl</kbd>+<kbd>Z</kbd>，将其保留为普通链接。或者，在创建链接预览后，点击该链接并从链接预览工具栏中选择_普通链接_。

可通过前往<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_，并在_功能_部分取消勾选_自动生成链接预览_来禁用此自动转换。

如果 Trilium 服务器无法访问该链接（或网络请求因任何其他原因失败），则不会将其转换为链接预览。

> [!NOTE]
> 仅当粘贴的文本_就是_ URL 时才会自动转换。带有显示名称的链接（例如 [Trilium Notes website](https://triliumnotes.org)）会保留为普通链接。

### 2\. 通过链接对话框

自 v0.107.0 起，链接预览可通过与其他链接相同的_添加链接_对话框创建（参见<a class="reference-link" href="Links/External%20links.md">外部链接</a>）：

*   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中按 <span class="tn-icon cke cke-link"></span>，或按 <kbd>Ctrl</kbd>+<kbd>K</kbd>，在_网页链接_上打开对话框。
*   输入或粘贴地址，然后在_显示为_中选择预览类型：_行内_、_卡片_，或对于 YouTube 视频选择 _YouTube 嵌入_。_普通链接_会插入普通链接。当选中文本时不会显示_显示为_，因为此时链接会保留选中的文本。
*   可选地，输入_链接标题_以替代页面自身的标题显示。_卡片_还提供_描述_选项，以替代页面自身的描述显示。
*   按 <kbd>Enter</kbd> 或 _添加链接_ 确认。链接会立即出现，并在 Trilium 读取页面后转换为预览。

或者，使用<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>并查找_链接预览_（也可通过_嵌入_、_url_ 或 _视频_找到）。它会打开同一个对话框，并已预先选择预览类型：YouTube 视频为 _YouTube 嵌入_，其他页面为_卡片_。

要将现有链接转换为预览，请打开其_编辑链接_对话框并更改_显示为_。如果链接的文本与其地址不同，则该文本会保留为预览的标题。

### 3\. 通过 Web Clipper 保存浏览器标签页

当<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">Web Clipper</a>保存窗口的标签页时，每个标签页都会成为一个_行内_链接预览，显示浏览器为其显示的标题和图标。由于此数据来自浏览器，登录后的页面会保留其真实标题，且 Trilium 服务器不会联系已保存的页面。

当_自动生成链接预览_关闭时，标签页将保存为普通链接列表。

## 修改现有链接预览

点击已插入的链接预览以选中它，会出现一个小工具栏，包含以下选项：

*   常规链接操作（在新标签页中打开、复制链接、取消链接）。
*   <span class="tn-icon cke cke-pencil"></span> _编辑链接_按钮，会在链接预览上打开_编辑链接_对话框，选中时按 <kbd>Ctrl</kbd>+<kbd>K</kbd> 也可实现。该对话框可更改其地址、_链接标题_（当标题被登录界面遮挡时尤其有用）、卡片的_描述_及其显示方式。新地址会显示新页面的标题和描述，除非你自行输入。
*   在链接预览模式（行内、卡片或嵌入）之间切换，以及将其转换为普通链接的方式。
    *   仅当 URL 指向受支持的服务（目前为 YouTube）时，嵌入选项才可用。

## 预览数据的来源

当你插入链接预览时，Trilium 会获取一次元数据并将其与笔记一起存储：

*   **YouTube URL**：标题和频道名称通过 YouTube 的公共 oEmbed 端点获取，视频缩略图以最高 1280×720 下载。
*   **所有其他 URL**：Trilium 会获取页面并读取 OpenGraph 标签（`og:title`、`og:description`、`og:image`、`og:site_name`），回退到页面的 `<title>` 和 `<meta name="description">`。网站图标和页面图片也会一并下载。

文本保存在笔记的 HTML 中。图片作为笔记的系统<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>保存，列在_由 Trilium 生成_下。

由于数据存储在笔记本身中，链接预览在重新打开笔记、共享/发布或导出为 HTML 时仍能正确渲染——无需任何进一步的网络请求。

元数据在**插入时**捕获，不会自动刷新。如果链接页面之后更改了标题或缩略图，你需要重新插入链接以获取新值。要刷新链接，只需重新创建它。

在 v0.107.0 之前插入的 YouTube 嵌入会保留其较小的缩略图（显示为模糊），直到链接被重新插入。

访问<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>时，数据由服务器而非客户端从远程 URL 获取。

## 已知限制

*   嵌入显示模式目前仅支持 YouTube。其他视频和媒体平台会回退为卡片预览。
*   阻止自动抓取的页面可能会生成最小化的预览（仅主机名）。
*   链接预览要求 Trilium 服务器能够访问目标 URL，因此对于服务器无法访问的网络中的页面，不会生成预览。