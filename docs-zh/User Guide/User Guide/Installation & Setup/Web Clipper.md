# Web Clipper
![](Web%20Clipper_image.png)

Trilium Web Clipper 是一款网页浏览器扩展，允许用户剪藏文本、截图、整个页面和简短笔记，并将它们直接保存到 Trilium Notes 中。

## 支持的浏览器

Trilium Web Clipper 官方支持以下网页浏览器：

*   Mozilla Firefox，使用 Manifest v2。
*   Google Chrome，使用 Manifest v3。理论上该扩展也应能在其他基于 Chromium 的浏览器上运行，但官方并不支持这些浏览器。

## 获取扩展

该扩展可从官方浏览器网上商店获取：

*   **Firefox**：[Firefox 附加组件上的 Trilium Web Clipper](https://addons.mozilla.org/firefox/addon/trilium-notes-web-clipper/)
*   **Chrome**：[Chrome 网上应用店上的 Trilium Web Clipper](https://chromewebstore.google.com/detail/trilium-web-clipper/ofoiklieachadcaeffficgjaajojpkpi)

## 功能

*   选中文本并通过右键上下文菜单剪藏
*   点击图片或链接并通过上下文菜单保存
*   从弹出窗口或上下文菜单保存整个页面
*   从弹出窗口或上下文菜单保存截图（带裁剪工具）
*   从弹出窗口创建简短文本笔记

## 弹出窗口

点击浏览器工具栏中的扩展按钮会打开其弹出窗口：

*   弹出窗口显示将从当前页面保存的内容：笔记标题（保存前可编辑）、网站，以及下方的预览。预览上方有一个开关，用于在页面提供的选项中选择要保存的内容：
    
    *   _选区_，当页面上选中了文本时：_保存选区_ 会将其保存到该页面剪藏笔记中，与上下文菜单的行为相同。
    *   _页面_，当页面包含文章时：_保存页面到 Trilium_ 会保存文章的文本和图片，当页面标注了发布日期时，发布日期会显示在网站旁边。
    *   _书签_，始终可用：一个用于填写页面相关笔记的文本框会取代预览，_保存书签_（或 <kbd>Ctrl</kbd>+<kbd>Enter</kbd>）会保存一个指向该页面的链接及该笔记。若留空，标题将保持为页面标题。
    
    如果有选区，弹出窗口会打开在选区上，否则打开在文章上。对于没有文章（Readability 找不到文章）且没有选区的页面，它会打开在 _书签_ 上，并提示该页面没有文章。键盘快捷键和上下文菜单仍会立即保存，无需预览。
*   扩展无法访问的页面（浏览器自身的页面、扩展商店，以及扩展安装前已打开且尚未重新加载的页面）无法保存或捕获，因此弹出窗口会在预览位置显示相应提示，且那里只有 _标签页_ 可用。
*   预览下方有一排按钮提供其他操作：_裁剪_（对您选定区域截图）、_截图_（对页面可见部分截图）和 _标签页_（将当前窗口中每个标签页的链接保存为列表）。将鼠标悬停在按钮上会显示其完整名称，以及其键盘快捷键（如果有）。
*   如果当前页面已被剪藏，顶部会显示一条通知，提供在 Trilium 中打开该笔记的选项。
*   如果找不到 Trilium，弹出窗口会解释原因而不显示操作，并提供按钮以再次查找 Trilium 和打开选项。
*   弹出窗口底部显示扩展是否已连接到 Trilium，以彩色圆点表示（已连接时为绿色，版本不兼容时为琥珀色，未找到 Trilium 时为红色），旁边是连接状态的描述，随后是扩展选项和此帮助页面的按钮。将鼠标悬停在该栏上时，旁边会出现一个再次检查连接的按钮，且在无法访问 Trilium 或版本不兼容期间会一直可见。

## 剪藏位置

Trilium 会将这些剪藏保存为“剪藏收件箱”笔记下的新子笔记。

默认情况下，该笔记是 <a class="reference-link" href="../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">日记笔记</a>，但您可以通过在任何其他笔记上设置[标签](../Advanced%20Usage/Attributes.md) `clipperInbox` 来覆盖此设置。

来自同一页面的同类型后续剪藏会添加到第一次剪藏所创建的笔记中，即使是在之后的某一天，或该笔记已被移出剪藏收件箱之后。该笔记会留在原处，不会被克隆回收件箱。

## 键盘快捷键

大多数功能都有键盘快捷键：

*   保存选中的文本：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存整个页面：<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌥</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存截图：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>E</kbd>）
*   保存当前窗口的所有标签页：没有默认快捷键，但可以按如下所述分配一个。

要设置自定义快捷键，请按照您所用浏览器的说明操作。

*   **Firefox**：`about:addons` → 齿轮图标 ⚙️ → 管理扩展快捷键
*   **Chrome**：`chrome://extensions/shortcuts`

> [!NOTE]
> 在 Firefox 上，默认快捷键会与某些浏览器功能冲突。因此，这些键盘组合不会触发 Web Clipper 操作。要解决此问题，只需将键盘快捷键更改为可用的组合即可。默认值将在未来版本中调整。

## 配置

该扩展需要连接到正在运行的 Trilium 实例。默认情况下，它会在本地计算机的 37840 端口上查找桌面应用程序。如果桌面应用程序运行在其他端口上（例如因为它使用 `TRILIUM_PORT` 环境变量启动），请在扩展的选项中输入该端口。扩展每分钟会再次检查 Trilium，或在其弹出窗口底部按下刷新按钮时立即检查。

如果您不运行桌面应用程序，或希望它在桌面应用程序未运行时也能工作，也可以配置[服务器](Server%20Installation.md)地址。

要连接到服务器，请在扩展的选项中输入其地址和您的密码，然后按 _登录到服务器实例_。如果服务器使用[多因素身份验证](Server%20Installation/Multi-factor%20authentication%20with%20TOTP.md)，还需在 _身份验证码_ 中填入您身份验证器应用中的当前验证码（或您的某个恢复码）；否则请留空。密码和验证码仅使用一次，用于获取扩展的令牌，不会被存储。

### 当剪藏失败时

每次剪藏后，页面角落会显示一条通知，确认已保存，并附有在 Trilium 中打开新笔记的链接。如果剪藏无法保存，通知会改为说明原因：

*   未找到 Trilium：启动桌面应用程序，或在扩展的选项中检查服务器地址和令牌。
*   Trilium 与扩展的版本不兼容：更新消息中指明的那一个。
*   Trilium 拒绝了请求：消息中包含 Trilium 给出的原因。

扩展会自行下载剪藏中的图片，以便它们与笔记一起存储在 Trilium 中。如果其中一些无法下载（例如因为网站拒绝了请求），剪藏仍会保存，通知会说明有多少张图片缺失。这些图片会保留其在原始网站上的地址：如果在 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _媒体_ 中启用了 _自动下载图片_，Trilium 会再尝试下载一次；否则，只要网站仍提供这些图片，笔记就会从网站显示它们。

通知显示在页面本身上，因此不会出现在扩展无法运行的页面上（例如浏览器自身的设置页面和扩展商店）。

## 测试开发版本

开发版本是预发布版本，通常用于测试目的。这些版本不在 Google 或 Firefox 网上商店中提供，但可以从以下任一来源下载：

*   [GitHub Releases](https://github.com/TriliumNext/Trilium/releases)，查找以 _Web Clipper._ 开头的发布版本。
*   GitHub Actions 中的构件，查找 [_Deploy web clipper extension_ 工作流](https://github.com/TriliumNext/Trilium/actions/workflows/web-clipper.yml)。选中一次工作流运行后，ZIP 文件可在 _Artifacts_ 部分找到，名称为 `web-clipper-extension`。

=== "<span class="tn-icon bx bxl-chrome"></span> Chrome"

    1.  下载 `trilium-web-clipper-[x.y.z]-chrome.zip`。
    2.  解压该归档文件。
    3.  在 Chrome 中，导航到 `chrome://extensions/`
    4.  打开页面右上角的 _开发者模式_。
    5.  按标题附近的 _加载已解压的扩展程序_ 按钮。
    6.  指向步骤 (2) 中解压出的目录。

=== "<span class="tn-icon bx bxl-firefox"></span> Firefox"

    > [!WARNING]
    > Firefox 的“零售”版本会阻止安装未签名的包。为了能够从磁盘安装扩展，请考虑使用 _Firefox Developer Edition_ 或非品牌版本的 Firefox（例如 _GNU IceCat_）。
    > 
    > 一次性操作：转到 `about:config` 并将 `xpinstall.signatures.required` 改为 `false`。

    1.  导航到 `about:addons`。
    2.  在左侧导航中选择 _扩展_。
    3.  按 _管理您的扩展_ 标题右侧的 _齿轮_ 图标。
    4.  选择 _从文件安装附加组件…_
    5.  指向 `trilium-web-clipper-[x.y.z]-firefox.zip`。
    6.  按 _添加_ 按钮以确认。

## 致谢

部分代码基于 [Joplin Notes 浏览器扩展](https://github.com/laurent22/joplin/tree/master/Clipper)。