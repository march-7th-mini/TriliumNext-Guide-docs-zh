# Web Clipper

![](Web%20Clipper_image.png)

Trilium Web Clipper 是一款浏览器扩展，允许用户将文本、截图、整个页面和简短笔记剪藏并直接保存到 Trilium Notes 中。

## 支持的浏览器

Trilium Web Clipper 官方支持以下浏览器：

*   Mozilla Firefox，使用 Manifest v2。
*   Google Chrome，使用 Manifest v3。理论上，该扩展也应适用于其他基于 Chromium 的浏览器，但官方不支持这些浏览器。

## 获取扩展

该扩展可从官方浏览器应用商店获取：

*   **Firefox**：[Firefox Add-ons 上的 Trilium Web Clipper](https://addons.mozilla.org/firefox/addon/trilium-notes-web-clipper/)
*   **Chrome**：[Chrome 网上应用店上的 Trilium Web Clipper](https://chromewebstore.google.com/detail/trilium-web-clipper/ofoiklieachadcaeffficgjaajojpkpi)

## 功能

*   选择文本并通过右键上下文菜单进行剪藏
*   点击图片或链接并通过上下文菜单保存
*   从弹出窗口或上下文菜单保存整个页面
*   从弹出窗口或上下文菜单保存截图（带裁剪工具）
*   从弹出窗口创建简短文本笔记

## 剪藏内容的位置

Trilium 会将这些剪藏内容作为新子笔记保存在“clipper inbox”笔记下。

默认情况下，该笔记是 <a class="reference-link" href="../Advanced%20Usage/Advanced%20Showcases/Day%20Notes.md">Day Notes</a>，但您可以通过在任何其他笔记上设置 [label](../Advanced%20Usage/Attributes.md) `clipperInbox` 来覆盖此设置。

如果同一页面（且在同一天）有多个剪藏内容，它们将被添加到同一笔记中。

## 键盘快捷键

大多数功能都有可用的键盘快捷键：

*   保存选中文本：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存整个页面：<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>（Mac：<kbd>⌥</kbd>+<kbd>⇧</kbd>+<kbd>S</kbd>）
*   保存截图：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>（Mac：<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>E</kbd>）

要设置自定义快捷键，请按照您所用浏览器的说明进行操作。

*   **Firefox**：`about:addons` → 齿轮图标 ⚙️ → 管理扩展快捷键
*   **Chrome**：`chrome://extensions/shortcuts`

> [!NOTE]
> 在 Firefox 上，默认快捷键会干扰某些浏览器功能。因此，这些键盘组合不会触发 Web Clipper 操作。要解决此问题，只需将键盘快捷键更改为其他可用的组合即可。默认设置将在未来版本中调整。

## 配置

该扩展需要连接到正在运行的 Trilium 实例。默认情况下，它会扫描本地计算机上的端口范围以查找桌面版 Trilium 实例。

如果您不运行桌面应用程序，或者希望在没有桌面应用程序运行的情况下工作，也可以配置 [server](Server%20Installation.md) 地址。

## 测试开发版本

开发版本是预发布版本，通常用于测试目的。这些版本不在 Google 或 Firefox 应用商店中提供，但可以从以下任一位置下载：

*   [GitHub Releases](https://github.com/TriliumNext/Trilium/releases)，查找以 _Web Clipper._ 开头的版本。
*   GitHub Actions 中的构建产物，查找 [_Deploy web clipper extension_ workflow](https://github.com/TriliumNext/Trilium/actions/workflows/web-clipper.yml)。选择一次工作流运行后，ZIP 文件可在 _Artifacts_ 部分中找到，名称为 `web-clipper-extension`。

### 对于 Chrome

1.  下载 `trilium-web-clipper-[x.y.z]-chrome.zip`。
2.  解压压缩包。
3.  在 Chrome 中，导航到 `chrome://extensions/`
4.  在页面右上角切换 _开发者模式_。
5.  点击标题附近的 _加载已解压的扩展程序_ 按钮。
6.  指向步骤 (2) 中解压的目录。

### 对于 Firefox

> [!WARNING]
> Firefox 阻止在“零售”版本中安装未签名的软件包。要能够从磁盘安装扩展，请考虑使用 _Firefox Developer Edition_ 或非品牌版本的 Firefox（例如 _GNU IceCat_）。
> 
> 一次性操作，请转到 `about:config` 并将 `xpinstall.signatures.required` 更改为 `false`。

1.  导航到 `about:addons`。
2.  在左侧导航中选择 _扩展_。
3.  点击 _管理您的扩展_ 标题右侧的 _齿轮_ 图标。
4.  选择 _从文件安装附加组件…_
5.  指向 `trilium-web-clipper-[x.y.z]-firefox.zip`。
6.  点击 _添加_ 按钮进行确认。

## 致谢

部分代码基于 [Joplin Notes 浏览器扩展](https://github.com/laurent22/joplin/tree/master/Clipper)。