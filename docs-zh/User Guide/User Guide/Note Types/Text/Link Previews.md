# 链接预览

链接预览可将粘贴的 URL 转换为一个富元数据小组件，并支持三种显示模式：

## 显示模式

链接预览可选用以下三种模式之一进行显示：

*   **行内** — 显示网站图标和页面标题的链接（与<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>非常相似）。当您希望链接与周围段落文字融合时，请使用此模式。
*   **卡片** — 包含缩略图、标题、描述和网站名称的块级预览。当链接是段落焦点时，请使用此模式。
*   **嵌入** — 块级交互式嵌入。
    *   目前支持 YouTube 视频，可进行交互式渲染（通过 `iframe`）。
    *   为防止不必要的远程请求，视频仅在首次点击后才会显示。

<table class="ck-table-resized">
    <colgroup>
        <col style="width:21.85%;">
        <col style="width:38.84%;">
        <col style="width:39.31%;">
    </colgroup>
    <tbody>
        <tr>
            <td><figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:251/42;" src="Link Previews_image.png" width="251" height="42"><figcaption><em>行内</em>链接预览</figcaption></figure></td>
            <td><figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:1217/196;" src="2_Link Previews_image.png" width="1217" height="196"><figcaption><em>卡片</em>链接预览</figcaption></figure></td>
            <td><figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:994/563;" src="1_Link Previews_image.png" width="994" height="563"><figcaption><em>嵌入</em>链接预览</figcaption></figure></td>
        </tr>
    </tbody>
</table>

## 插入链接预览

有两种创建方式：

### 1\. 通过粘贴 URL

以下操作会自动创建链接预览：

*   粘贴 URL 后按 <kbd>空格</kbd> 键。这将创建一个_行内_链接预览。
*   在新段落开头按 <kbd>Enter</kbd> 键，对于 YouTube URL 将创建_卡片_或_嵌入_预览。

若要撤销自动创建的链接预览，请立即按 <kbd>Ctrl</kbd>+<kbd>Z</kbd>，这将使其保留为纯链接。或者，在创建链接预览后，点击该链接并从链接预览工具栏中选择_纯链接_。

可以通过进入<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_，然后在_功能_部分取消勾选_自动生成链接预览_来禁用此自动转换功能。

如果 Trilium 服务器无法访问该链接（或网络请求因任何其他原因失败），则不会将其转换为链接预览。

> [!NOTE]
> 仅当粘贴的文本_本身是_ URL 时，才会自动转换。带有显示名称的链接（例如 [Trilium Notes website](https://triliumnotes.org)）将保留为纯链接。

### 2\. 通过使用“链接预览”工具栏按钮

点击格式工具栏中的 **链接预览** 以打开_链接预览_弹窗。粘贴 URL 并选择预览类型。

## 修改现有链接预览

点击已插入的链接预览以将其选中，此时会出现一个小工具栏，其中包含以下选项：

*   常规链接操作（在新标签页中打开、复制链接、取消链接）。
*   一个用于编辑链接预览标题的按钮。当标题隐藏在登录屏幕后面时，此功能尤其有用。
*   在链接预览模式（行内、卡片或嵌入）之间切换的方法，以及将其转换为普通链接的方法。
    *   仅当 URL 指向受支持的服务（目前为 YouTube）时，嵌入选项才可用。

## 预览数据的来源

当您插入链接预览时，Trilium 会获取一次元数据并将其存储在笔记的 HTML 中：

*   **YouTube URL** — 通过 YouTube 的公共 oEmbed 端点获取标题、频道名称和缩略图。
*   **所有其他 URL** — Trilium 会获取页面并读取 OpenGraph 标签（`og:title`、`og:description`、`og:image`、`og:site_name`），如果不存在则回退到页面的 `<title>` 和 `<meta name="description">`。网站图标会被下载并内联。

由于数据存储在笔记本身中，因此当您重新打开笔记、分享/发布笔记或导出为 HTML 时，链接预览无需任何进一步的网络请求即可继续正确渲染。

元数据在**插入时**捕获，不会自动刷新。如果链接页面之后更改了其标题或缩略图，您需要重新插入链接以获取新值。要刷新链接，只需重新创建它即可。

当访问<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>时，数据由服务器（而非客户端）从远程 URL 获取。

## 已知限制

*   嵌入显示模式目前仅支持 YouTube。其他视频和媒体平台将回退为卡片预览。
*   阻止自动抓取的页面可能只会生成极简预览（仅主机名）。
*   链接预览要求 Trilium 服务器能够访问目标 URL，因此对于服务器无法访问的网络上的页面，将无法生成预览。