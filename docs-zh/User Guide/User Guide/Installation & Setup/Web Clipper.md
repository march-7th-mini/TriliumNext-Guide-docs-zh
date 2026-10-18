# Web Clipper
![](Web%20Clipper_image.png)

Trilium Web Clipper 是一款网页浏览器扩展，允许用户剪藏文本、截图、整个页面和简短笔记，并将它们直接保存到 Trilium Notes 中。

## 支持的浏览器

Trilium Web Clipper 官方支持以下网页浏览器：

*   Mozilla Firefox，使用 Manifest v2。
*   Google Chrome，使用 Manifest v3。理论上该扩展也应能在其他基于 Chromium 的浏览器上运行，但不受官方支持。

## 获取扩展

该扩展可从官方浏览器网上商店获取：

*   **Firefox**：[Firefox Add-ons 上的 Trilium Web Clipper](https://addons.mozilla.org/firefox/addon/trilium-notes-web-clipper/)
*   **Chrome**：[Chrome Web Store 上的 Trilium Web Clipper](https://chromewebstore.google.com/detail/trilium-web-clipper/ofoiklieachadcaeffficgjaajojpkpi)

## 功能

*   选中文本并通过右键上下文菜单剪藏
*   点击图片或链接并通过上下文菜单保存
*   从弹出窗口或上下文菜单保存整个页面
*   将浏览器显示的 PDF 保存为文件笔记
*   从弹出窗口或上下文菜单保存所选区域、页面可见部分或整个页面的截图
*   从弹出窗口创建简短文本笔记

## 弹出窗口

点击浏览器工具栏中的扩展按钮会打开其弹出窗口：

*   弹出窗口显示将从当前页面保存的内容：笔记标题（保存前可编辑）、网站，以及下方的预览，预览以一个用于填写你自己笔记的输入框和页面描述开头。预览上方的开关用于在页面提供的选项中选择要保存的内容：
    
    *   _Selection_（选区），当页面上选中了文本时：_Save selection_ 会将其保存到该页面剪藏笔记中，与上下文菜单的行为相同。
    *   _Page_（页面）：_Save page to Trilium_ 保存页面的文本和图片。预览顶部的一个较小的开关用于选择保留页面的多少内容：_Article_（文章）仅保留页面的正文，不含菜单、侧边栏和页脚；_Whole page_（整个页面）保留页面显示的所有内容。_Whole page_ 适用于非文章的页面（例如图库或卡片页面），此时 _Article_ 可能会遗漏部分内容；预览会显示各自保留的内容。在 Trilium 未找到文章的页面上，_Article_ 不可用。页面所声明的作者显示在描述下方，以 <span class="tn-icon bx bx-user"></span> 图标标记。保存前可编辑或清除，或在页面未声明作者时手动填写，并保存在笔记的 `#pageAuthor` 标签中。当页面声明了发布时间时，该日期显示在作者下方，以 <span class="tn-icon bx bx-calendar"></span> 图标标记，并保存在笔记的 `#publishedDate` 标签中。当页面声明了最后修改时间时，该日期显示在下方，以 <span class="tn-icon bx bx-history"></span> 图标标记，并保存在 `#modifiedDate` 标签中。
    *   _PDF_，当标签页在浏览器查看器中显示 PDF 时：_Save PDF to Trilium_ 会下载该 PDF 并将其保存为文件笔记，Trilium 会在其 <a class="reference-link" href="../Note%20Types/File/PDFs.md">PDF</a> 查看器中打开。由于文件笔记本身没有可供你填写笔记的文本，因此只能编辑标题和描述。页面的地址保存在笔记的 `#pageUrl` 标签中，PDF 的文件名保存在 `#originalFileName` 中。保存 PDF 需要 Trilium v0.107.0 或更高版本。
    *   _Bookmark_（书签），始终可用：没有预览，_Save bookmark_ 会保存一个指向该页面的链接，并以你的笔记作为笔记内容。留空时，标题保持为页面标题。
    
    用于填写笔记的输入框以 <span class="tn-icon bx bx-info-circle"></span> 图标标记，弹出窗口打开时即获得光标，因此可以立即输入笔记（例如说明该页面为何值得保留）。它会随文本增长，并在 _Selection_、_Page_ 和 _Bookmark_ 之间切换时保留内容。针对选区或页面的笔记会保存在剪藏内容上方的一个 _Note_ 警示框中。留空则不添加任何内容。在弹出窗口的任意字段中按 <kbd>Ctrl</kbd>+<kbd>Enter</kbd> 即可保存，无论当前选择的是哪一项。
    
    描述以 <span class="tn-icon bx bx-align-left"></span> 图标标记，来自页面的 `description` meta 标签，或页面提供给社交网站的对应标签。保存前可编辑或清除，或在页面没有描述时手动填写，并保存在笔记的 `#pageDescription` 标签中。通过键盘快捷键或上下文菜单保存的剪藏（包括截图和图片）会获取页面所提供的描述。每次带有描述的剪藏都会更新该标签。点击笔记标题旁的 _Web clip_ 徽章可查看描述、作者和日期（参见 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Note%20badges.md">笔记徽章</a>）。
    
    如果有选区，弹出窗口会打开在 _Selection_ 上，否则打开在 _Page_ 上，显示文章；当页面没有文章时显示整个页面。对于 PDF，会打开在 _PDF_ 上。对于没有可保存内容的页面，会打开在 _Bookmark_ 上并说明原因。键盘快捷键和上下文菜单仍会立即保存，不显示预览：以这种方式保存整个页面时，会保存文章；当页面没有文章时保存整个页面；当标签页显示 PDF 时保存该 PDF。
*   扩展无法访问的页面（浏览器自身的页面、扩展商店，以及安装扩展之前就已打开、尚未重新加载的页面）无法保存或截图，因此弹出窗口会在预览位置说明这一点，且那里仅保留 _All tabs_ 可用。
*   预览下方有一排按钮提供其他操作：_Area_（所选区域的截图）、_Visible_（页面可见部分的截图）、_Full page_（整个页面的截图）和 _All tabs_（将当前窗口中每个标签页的链接保存为 <a class="reference-link" href="../Note%20Types/Text/Link%20Previews.md">链接预览</a> 列表，或在关闭 _Autogenerate link previews_ 时保存为普通链接）。将鼠标悬停在按钮上会显示其完整名称以及键盘快捷键（如果有）。
*   _Full page_ 会滚动浏览页面，对每个部分截图并将它们拼接为一张图片，然后滚动回页面原来的位置。执行期间会隐藏滚动条，因此它们不会出现在图片中。请停留在该标签页直到保存完成：切换到其他标签页会停止截图。固定在窗口顶部的页眉会在图片顶部出现一次，滚动时固定的标题会出现在其在页面中的位置。其他在滚动时保持固定的元素（例如 Cookie 横幅和聊天按钮）会被排除，而填满整个窗口的背景会在每个屏幕上重复出现。在 Firefox 中，页面无需滚动即可截图，速度更快：此时这样的背景只会出现在顶部，而页面仅在滚动进入视图后才加载的图片可能会缺失。长页面会保存为多张图片，在笔记中自上而下排列。超过 100 屏的页面会在该处截断，保存后的消息会说明这一点。截图在 Trilium 中保持完整高度：_Resize image_（位于选项 → 媒体中的 _Automatically compress images_ 下）仅限制其宽度。
*   在 Trilium 保存期间弹出窗口保持打开，对于长页面或大型 PDF 可能需要几秒钟，其他操作会等待其完成。随后弹出窗口顶部的栏会以绿色显示剪藏已保存（替代页面已被剪藏的提示），并提供 _Open note_ 以在 Trilium 中打开它（在 _All tabs_ 之后还有 _Close saved tabs_）；或者以红色显示无法保存的原因。同一剪藏不会因误操作而保存两次：在选择另一种模式之前，保存按钮保持禁用。_Crop_ 是例外：弹出窗口会关闭以便选择页面区域，页面上的通知会报告结果。
*   如果当前页面已被剪藏，顶部的提示会提供在 Trilium 中打开该笔记的选项。
*   如果找不到 Trilium，弹出窗口会解释原因而不显示操作，并提供重新查找 Trilium 和打开选项的按钮。
*   弹出窗口底部以彩色圆点（已连接时为绿色，版本不兼容时为琥珀色，未找到 Trilium 时为红色）加连接描述的形式显示扩展是否已连接到 Trilium，随后是扩展选项和此帮助页面的按钮。将鼠标悬停在该栏上时，旁边会出现一个再次检查连接的按钮，并在无法访问 Trilium 或版本不兼容期间保持可见。

## 剪藏的位置

Trilium 会将这些剪藏保存为“clipper inbox”笔记下的新子笔记。

默认情况下，该笔记是 <a class="reference-link" href="../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>，但你可以在任何其他笔记上设置 [标签](../Advanced%20Usage/Attributes.md) `clipperInbox` 来覆盖此设置。

来自同一页面的同类型后续剪藏会添加到第一次剪藏所创建的笔记中，即使是在之后的某一天，或该笔记已被移出 clipper inbox 之后。该笔记会留在原处，不会被克隆回 inbox。PDF 是例外：每次保存都会创建一个新的文件笔记，因为 PDF 自上次保存以来可能已发生变化。

被剪藏笔记的图标显示所保存的内容：

*   <span class="tn-icon bx bx-paperclip"></span> 来自上下文菜单的选区、截图或链接；
*   <span class="tn-icon bx bx-globe"></span> 页面（_Article_ 或 _Whole page_）；
*   <span class="tn-icon bx bx-bookmark"></span> 书签；
*   <span class="tn-icon bx bx-window-alt"></span> 窗口的标签页。

该图标源自笔记的 `#clipType` 标签，因此在笔记上设置 `#iconClass` 标签会替换它。已保存的 PDF 具有 PDF 文件的图标，与 Trilium 中的任何其他 PDF 相同。

## 嵌入视频

被剪藏页面中嵌入的 YouTube 视频会保存为 <a class="reference-link" href="../Note%20Types/Text/Link%20Previews.md">链接预览</a> 嵌入，包含视频标题和缩略图。与在编辑器中添加的链接预览一样，视频仅在点击时播放。其他嵌入内容（例如来自其他网站的视频）不会被保存。

弹出窗口的预览会将每个此类视频显示为带有 YouTube 图标和视频短链接的标签块，并排除不会被保存的嵌入内容。

## 键盘快捷键

大多数功能都有键盘快捷键：

*   保存选中文本：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存整个页面：<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌥</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存区域截图：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>E</kbd>）
*   保存当前窗口的所有标签页：无默认快捷键，但可按下文所述进行分配。
*   保存整个页面的截图：无默认快捷键，但可按下文所述进行分配。

要设置自定义快捷键，请按照你所使用浏览器的说明操作。

*   **Firefox**：`about:addons` → 齿轮图标 ⚙️ → 管理扩展快捷键
*   **Chrome**：`chrome://extensions/shortcuts`

> [!NOTE]
> 在 Firefox 上，默认快捷键会与某些浏览器功能冲突。因此，这些按键组合不会触发 Web Clipper 操作。要解决此问题，只需将键盘快捷键更改为可用的组合即可。默认值将在未来版本中调整。

## 配置

该扩展需要连接到正在运行的 Trilium 实例。默认情况下，它会查找本地计算机 37840 端口上的桌面应用程序。如果桌面应用程序运行在其他端口（例如因为它使用 `TRILIUM_PORT` 环境变量启动），请在扩展的选项中输入该端口。扩展每分钟会再次检查 Trilium，或在其弹出窗口底部按下刷新按钮时立即检查。

如果你不运行桌面应用程序，或希望在没有桌面应用程序运行的情况下使用，也可以配置[服务器](Server%20Installation.md)地址。

要连接到服务器，请在扩展的选项中输入其地址和你的密码，然后按 _Login to the server instance_。如果服务器使用[多因素身份验证](Server%20Installation/Multi-factor%20authentication%20with%20TOTP.md)，还需在 _Authentication code_ 中填写身份验证器应用中的当前验证码（或你的某个恢复代码）；否则留空。密码和验证码仅使用一次，用于获取扩展的令牌，不会被存储。

### 剪藏失败时

每次通过键盘快捷键或上下文菜单进行剪藏后，页面角落的通知会确认已保存，并附有在 Trilium 中打开新笔记的链接。从弹出窗口进行的剪藏会在弹出窗口中报告，除非弹出窗口在保存前已关闭。如果剪藏无法保存，消息会改为说明原因：

*   未找到 Trilium：启动桌面应用程序，或在扩展的选项中检查服务器地址和令牌。
*   Trilium 与扩展的版本不兼容：更新消息中指明的一方。
*   Trilium 拒绝了请求：消息包含 Trilium 给出的原因。
*   弹出窗口无法连接到扩展的后台脚本，或未收到答复：关闭弹出窗口并重新打开。如果扩展刚刚更新或重新加载，还需重新加载页面。
*   PDF 无法保存：Trilium 版本低于 v0.107.0、网站拒绝再次发送 PDF，或 PDF 大于 100 MB。扩展使用浏览器针对该网站的 Cookie 下载 PDF，因此登录状态下的 PDF 可以在你登录时保存。

扩展会自行下载剪藏中的图片，以便它们与笔记一起存储在 Trilium 中。如果其中一些无法下载（例如因为网站拒绝了请求），剪藏仍会保存，通知会说明缺失了多少张图片。这些图片会保留其在原始网站上的地址：如果在 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _Media_ 中启用了 _Download images automatically_，Trilium 会再次尝试下载它们；否则笔记会从网站显示它们，只要网站仍提供这些图片。

通知显示在页面本身上，因此不会出现在扩展无法运行的页面上（例如浏览器自身的设置页面、扩展商店和 Firefox 的 PDF 查看器）。在此类页面上从弹出窗口保存的剪藏仍会在弹出窗口中报告。

## 测试开发版本

开发版本是预发布版本，通常用于测试目的。这些版本不在 Google 或 Firefox 网上商店中提供，但可以从以下任一来源下载：

*   [GitHub Releases](https://github.com/TriliumNext/Trilium/releases)，查找以 _Web Clipper_ 开头的发布版本。
*   GitHub Actions 中的产物，查找 [_Deploy web clipper extension_ 工作流](https://github.com/TriliumNext/Trilium/actions/workflows/web-clipper.yml)。选择一次工作流运行后，ZIP 文件可在 _Artifacts_ 部分中找到，名称为 `web-clipper-extension`。

=== "<span class="tn-icon bx bxl-chrome"></span> Chrome"

    1.  下载 `trilium-web-clipper-[x.y.z]-chrome.zip`。
    2.  解压该压缩包。
    3.  在 Chrome 中，导航到 `chrome://extensions/`
    4.  打开页面右上角的 _Developer Mode_（开发者模式）。
    5.  点击标题附近的 _Load unpacked_（加载已解压的扩展程序）按钮。
    6.  指向步骤 (2) 中解压出的目录。

=== "<span class="tn-icon bx bxl-firefox"></span> Firefox"

    > [!WARNING]
    > Firefox 的“零售”版本禁止安装未签名的包。要能够从磁盘安装扩展，请考虑使用 _Firefox Developer Edition_ 或非品牌版本的 Firefox（例如 _GNU IceCat_）。
    > 
    > 一次性操作：前往 `about:config` 并将 `xpinstall.signatures.required` 改为 `false`。

    1.  导航到 `about:addons`。
    2.  在左侧导航中选择 _Extensions_（扩展）。
    3.  点击 _Manage Your Extensions_（管理你的扩展）标题右侧的 _Gear_（齿轮）图标。
    4.  选择 _Install Add-on From File…_（从文件安装附加组件…）
    5.  指向 `trilium-web-clipper-[x.y.z]-firefox.zip`。
    6.  点击 _Add_（添加）按钮确认。

## 致谢

部分代码基于 [Joplin Notes 浏览器扩展](https://github.com/laurent22/joplin/tree/master/Clipper)。