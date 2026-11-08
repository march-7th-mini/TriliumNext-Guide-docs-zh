# 链接预览

链接预览可将粘贴的 URL 转换为一个丰富的、能感知元数据的小组件，该组件可以以三种视觉模式显示：

## 链接显示模式

链接预览可以以三种链接显示模式之一显示：

*   **图标和文本** — 显示网站图标和页面标题的链接（与<a class="reference-link" href="Links/Internal%20(reference)%20links.md">内部（引用）链接</a>非常相似）。当你希望链接与周围段落自然衔接时使用此模式。
*   **卡片** — 块级预览，包含缩略图、标题、描述和网站名称。当链接是段落的焦点时使用此模式。
*   **嵌入** — 块级播放器。
    *   支持 YouTube 视频（在 YouTube 播放器中播放），以及网络地址上的音频和视频文件（在 Trilium 的媒体播放器中播放）。
    *   为防止不必要的远程请求，在你点击播放之前不会从网站加载任何内容。在此之前，视频显示其缩略图和播放按钮，音频文件显示其控件。
    *   播放器可以调整大小和对齐（参见下方的_音频和视频_）。

第四种链接显示模式，**文本**，插入一个不带预览的普通链接。

> [!NOTE]
> 自 v0.107.0 起，_显示为_ 和 _显示_ 菜单显示的是 _文本_ 而非 _纯链接_，显示的是 _图标和文本_ 而非 _内联_。

<div class="trilium-multicolumn-layout" data-trilium-column-ratios="1-1-1">
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:251/42;" src="Link Previews_image.png" width="251" height="42"><figcaption><em>图标和文本</em>链接预览</figcaption></figure>

</div>
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:1217/196;" src="2_Link Previews_image.png" width="1217" height="196"><figcaption><em>卡片</em>链接预览</figcaption></figure>

</div>
<div class="trilium-multicolumn-column">

<figure class="image image_resized" style="width:100%;"><img style="aspect-ratio:994/563;" src="1_Link Previews_image.png" width="994" height="563"><figcaption><em>嵌入</em>链接预览</figcaption></figure>

</div>
</div>

## 插入链接预览

有四种方式可以创建链接预览：

### 1\. 通过粘贴 URL

链接预览会自动创建：

*   通过粘贴 URL 并按 <kbd>Space</kbd>。这将创建一个_图标和文本_链接预览。
*   当位于新段落的开头时，按 <kbd>Enter</kbd> 将创建一个_卡片_，或者对于 YouTube 视频或音频/视频文件创建一个_嵌入_。

要撤销自动创建的链接预览，请立即按 <kbd>Ctrl</kbd>+<kbd>Z</kbd>，这样它会保留为文本链接。或者，在创建链接预览后，点击该链接并从链接预览工具栏中选择_文本_，这会创建一个显示为页面标题的链接。

可以通过前往<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ 并在_功能_部分取消勾选_自动生成链接预览_来禁用此自动转换。

如果链接对 Trilium 服务器不可访问（或网络请求因任何其他原因失败），则不会转换为链接预览。文件名以已知扩展名（如 `.mp4`、`.webm`、`.mp3` 或 `.flac`）结尾的音频或视频文件的地址仍然会变为_嵌入_。

> [!NOTE]
> 只有当粘贴的文本_就是_ URL 时才会自动转换。带有显示名称的链接（例如 [Trilium Notes 网站](https://triliumnotes.org)）会保留为文本链接。

### 2\. 从链接对话框

自 v0.107.0 起，链接预览与其他任何链接一样从同一个_添加链接_对话框创建（参见<a class="reference-link" href="Links/External%20links.md">外部链接</a>）：

*   在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中按 <span class="tn-icon cke cke-link"></span>，或按 <kbd>Ctrl</kbd>+<kbd>K</kbd>，在_网页_上打开对话框。
*   输入或粘贴地址，然后在_显示为_中选择预览类型：_图标和文本_、_卡片_，或者对于 YouTube 视频或音频/视频文件的地址，选择_嵌入_。_文本_插入普通链接。当选中了文本时不会显示_显示为_，因为此时链接会保留选中的文本。
*   可选地，输入一个_链接标题_来替代页面自身的标题显示。_卡片_还提供一个_描述_来替代页面自身的描述显示。
*   当你离开地址字段时，或使用 <span class="tn-icon bx bx-paste"></span> _粘贴_按钮粘贴地址时，Trilium 会读取页面并用页面自身的标题填充空的_链接标题_，用页面自身的描述填充卡片为空的_描述_。字段末尾的加载指示器表示其值正在加载；一旦你在字段中输入，你输入的内容会被保留。将_显示为_切换为_卡片_会以相同方式填充_描述_，而无需再次读取页面。
*   按 <kbd>Enter</kbd> 或 _插入链接_ 确认。链接会立即出现，并在 Trilium 读取页面后变为预览。

要阻止对话框读取页面，请前往<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_，在_功能_部分关闭_自动检索文本链接的标题_（针对_文本_）或_自动检索图标和文本链接及卡片的标题和描述_（针对_图标和文本_和_卡片_）。两者默认开启。当它们开启时，Trilium 会在你离开地址字段时立即联系页面，对于文本链接也是如此。插入_图标和文本_链接或_卡片_无论如何都会读取页面，因为预览是基于页面构建的。

或者，使用<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>并选择_链接到网页（带图标）_或_链接到网页（作为卡片）_（两者也可以通过_链接预览_找到）。每个命令都会在_网页_上打开相同的对话框，并已预选_图标和文本_或_卡片_。

要将现有链接转换为预览，请打开其_编辑链接_对话框并更改_显示为_，或在链接工具栏的_显示_菜单中选择一种显示方式。无论哪种方式，文本与地址不同的链接会保留该文本作为预览的标题。

### 3\. 从插入菜单，用于音频和视频

从<a class="reference-link" href="Insert%20buttons.md">插入按钮</a>菜单或<a class="reference-link" href="Slash%20Commands.md">斜杠命令</a>中选择 <span class="tn-icon bx bx-movie-play"></span> _音频/视频嵌入_。粘贴 YouTube 视频或音频/视频文件的地址，然后按_插入媒体_或 <kbd>Enter</kbd> 将其作为_嵌入_插入。字段末尾的 <span class="tn-icon bx bx-paste"></span> _粘贴_按钮会用剪贴板上的文本替换字段中的文本。此按钮仅在 Trilium 可以读取剪贴板的地方显示：在桌面应用中，以及在通过 HTTPS 访问的浏览器中（除非剪贴板访问被阻止）。

媒体会在 Trilium 读取地址后插入，这可能需要几秒钟：读取 YouTube 视频的标题和缩略图，或判断文件是音频还是视频。当地址无法读取，或者是网页地址而非 YouTube 视频或媒体文件地址时，会显示错误且提示框保持打开。在此期间打开另一个笔记会取消插入。

### 4\. 通过从网页剪藏器保存浏览器标签页

当<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏器</a>保存窗口的标签页时，每个标签页会变成一个_图标和文本_链接预览，显示浏览器为其显示的标题和图标。由于此数据来自浏览器，登录后的页面会保留其真实标题，且 Trilium 服务器不会联系已保存的页面。

当_自动生成链接预览_关闭时，标签页会改为保存为文本链接列表。

## 修改现有链接预览

点击已插入的_图标和文本_或_卡片_链接预览以选中它，会出现一个小工具栏，包含以下选项：

*   _打开链接_，在新标签页中打开页面，以及 <span class="tn-icon cke cke-trilium-copy"></span> _复制地址（URL）_。
*   <span class="tn-icon cke cke-pencil"></span> _编辑链接_按钮，会在链接预览上打开_编辑链接_对话框，选中时按 <kbd>Ctrl</kbd>+<kbd>K</kbd> 也是如此。该对话框可更改其地址、其_链接标题_（当标题被登录界面遮挡时特别有用）、卡片的_描述_及其显示方式。新地址会显示新页面的标题和描述，除非你输入自己的内容。
*   _显示_菜单，可将预览转换为显示为其标题的普通链接（_文本_）或切换为另一种显示模式（_图标和文本_、_卡片_或_嵌入_）。
    *   嵌入选项仅对 YouTube 视频或音频/视频文件显示。地址不以已知扩展名（如 `.mp4` 或 `.mp3`）结尾的文件的_卡片_不再提供此选项。
*   <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_菜单，包含 <span class="tn-icon cke cke-web"></span> _打开链接_、<span class="tn-icon cke cke-pencil"></span> _编辑链接_、<span class="tn-icon cke cke-trilium-copy"></span> _复制地址（URL）_、<span class="tn-icon cke cke-trilium-link-preview"></span> _显示为_下的相同显示模式，以及 <span class="tn-icon cke cke-unlink"></span> _取消链接_，它会将预览替换为其地址的纯文本。

右键点击链接预览会选中它并打开其_更多操作_菜单。

### 音频和视频

显示为_嵌入_的 YouTube 视频、视频文件或音频文件具有大小、位置、标题和说明文字，就像<a class="reference-link" href="Include%20Note.md">包含笔记</a>一样。视频保持其形状，因此 YouTube Short 是竖屏的，较旧的视频可能是 4:3。在早期版本中插入的 YouTube 视频在重新插入之前为 16:9。在编辑器中，点击视频既会播放它也会选中它，之后点击播放器也是如此。

视频文件或音频文件在 Trilium 的媒体播放器中播放，即<a class="reference-link" href="../File.md">文件</a>笔记的播放器，带有播放按钮、进度条和音量。视频文件显示插入时截取的某一帧画面（参见下方的_预览数据来自哪里_），没有画面时显示 <span class="tn-icon bx bx-movie"></span> 图标。音频文件显示一行控件。当文件无法播放时，一条消息会以视频的大小替代播放器。其下方是网站返回的错误（如果有），例如文件已不存在时的 _HTTP 404: Not found_。

选中的嵌入的工具栏提供：

*   <span class="tn-icon cke cke-trilium-copy"></span> _复制地址（URL）_。
*   _显示_菜单，可将嵌入转换为带标题的_图标和文本_或_卡片_链接预览，或转换为显示为其标题的_文本_链接。其说明文字的文本会保留，作为其后的一个段落。
*   <span class="tn-icon cke cke-three-vertical-dots"></span> _更多操作_菜单：
    *   <span class="tn-icon bx bx-link-external"></span> _在外部打开_ 在 Trilium 之外打开媒体：在浏览器中，或在处理该链接的应用中，例如 Android 上的 YouTube 应用。
    *   <span class="tn-icon cke cke-pencil"></span> _编辑..._ 打开_编辑链接_对话框，仅包含媒体的_地址（URL）_和_链接标题_，选中嵌入时按 <kbd>Ctrl</kbd>+<kbd>K</kbd> 也是如此。使用另一个地址时，嵌入会播放新媒体并保持其大小、位置、标题和说明文字。它会采用新媒体的缩略图和形状，视频文件会获得其某一帧的画面，如同插入时一样。处于初始大小的视频会采用新视频的初始大小，音频文件替代视频或视频替代音频文件时，会采用新媒体的大小。新地址会显示新媒体的标题，除非你输入自己的内容。当地址不是 YouTube 视频、音频或视频文件的地址时，嵌入保持原样，Trilium 显示错误。
    *   <span class="tn-icon cke cke-trilium-copy"></span> _复制地址（URL）_。
    *   <span class="tn-icon cke cke-trilium-link-preview"></span> _显示为_下的_显示_菜单的显示模式。
    *   _大小_：_中等_视频可以调整大小，_完整_视频占据笔记的宽度，当它会高于窗口的大部分时则更小。新视频为_中等_。在早期版本中插入的 YouTube 视频为_完整_。音频文件只有一种大小，即一行控件，其宽度可以调整，因此没有_大小_菜单。
    *   _位置_：在_文字换行_下，<span class="tn-icon cke cke-object-left"></span> _左对齐_、<span class="tn-icon cke cke-object-center"></span> _居中对齐_ 和 <span class="tn-icon cke cke-object-right"></span> _右对齐_ 将视频放在独立行上，位于笔记的该侧。在_文字环绕_下，<span class="tn-icon cke cke-object-inline-left"></span> _左对齐_ 和 <span class="tn-icon cke cke-object-inline-right"></span> _右对齐_ 将其放在该侧并让文字在其旁边排列。_居中对齐_为默认值。
    *   _显示标题_ 在其上方显示媒体的标题，作为指向媒体的链接。新媒体插入时不带标题。<span class="tn-icon bx bx-dots-vertical-rounded"></span> 标题按钮会打开相同的菜单。
    *   _显示说明文字_ 在视频下方添加居中的说明文字，并将光标置于其中。说明文字是文本笔记的一部分，因此可以像其余文本一样格式化。当光标在说明文字中时，视频保持选中状态并保留其工具栏。再次选择_显示说明文字_会移除说明文字。
    *   <span class="tn-icon bx bx-trash"></span> _删除_ 从笔记中移除视频。

右键点击视频文件或音频文件会打开相同的_更多操作_菜单。右键点击 YouTube 视频也是如此，但仅在它播放之前：此后，右键点击会传递给 YouTube 的播放器，由其显示自己的菜单。

要调整_中等_视频或音频文件的大小，请选中它并拖动其右下角的手柄，对于右对齐的则拖动其左下角的手柄。视频的高度随宽度变化。再次选择_中等_会将视频恢复到其初始大小。

在[共享页面](../../Advanced%20Usage/Sharing.md)上，媒体保持其宽度、位置和说明文字，但不保留其标题。视频或音频文件在访客点击后会在浏览器自带的播放器中播放。在移动端布局中，位置不是_居中对齐_的媒体会占据全宽。

## 预览数据来自哪里

当你插入链接预览时，Trilium 会获取一次元数据并将其与笔记一起存储：

*   **YouTube URL**：标题、频道名称和视频形状通过 YouTube 的公共 oEmbed 端点获取，视频缩略图以最高 1280×720 下载。
*   **音频和视频文件**：Trilium 读取文件的开头部分，足以区分音频和视频，并且对于大多数 MP4 和 WebM 文件，足以判断视频形状。文件的其余部分不会被下载，文件也不会被复制到 Trilium 中。视频文件插入后，编辑器会截取其中几秒处的一帧画面作为其缩略图。该帧通过 Trilium 服务器读取，因此文件所在网站看到的是服务器而非你的浏览器。独立（浏览器）版和移动版没有这样的服务器：它们直接从网站读取该帧，而网站不允许其他网站读取的视频则没有缩略图。
*   **所有其他 URL**：Trilium 获取页面并读取 OpenGraph 标签（`og:title`、`og:description`、`og:image`、`og:site_name`），回退到页面的 `<title>` 和 `<meta name="description">`。网站图标和页面图片也会被下载。

文本保存在笔记的 HTML 中。图片作为笔记的系统<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>保存，列在_由 Trilium 生成_下。

由于数据存储在笔记本身中，链接预览在你重新打开笔记、共享/发布它或导出为 HTML 时都能正确渲染——无需任何进一步的网络请求。

元数据在**插入时**捕获，不会自动刷新。如果链接的页面后来更改了标题或缩略图，你需要重新插入链接以获取新值。要刷新链接，只需重新创建它。

在 v0.107.0 之前插入的 YouTube 嵌入会保留其较小的缩略图（显示为模糊），直到链接被重新插入。

当访问<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>时，数据由服务器而非客户端从远程 URL 获取。

## 已知限制

*   嵌入显示模式支持 YouTube 以及音频和视频文件。其他视频和媒体平台的页面会回退为卡片预览。
*   音频或视频文件从其地址播放：需要该地址可访问，当文件被移动或删除时停止播放。它只能以浏览器或桌面应用支持的格式播放。
*   通过纯 `http://` 提供的文件可能无法在桌面应用中或从通过 `https://` 访问的 Trilium 服务器播放。
*   音频文件不显示可视化效果和波形，这与音频<a class="reference-link" href="../File.md">文件</a>笔记不同，因为文件所在网站通常不允许 Trilium 读取其声音。
*   阻止自动抓取的页面可能产生最小化的预览（仅主机名）。
*   链接预览需要 Trilium 服务器能够访问目标 URL，因此不会为服务器无法访问的网络上的页面生成预览。