# 脚本

Trilium 支持创建<a class="reference-link" href="Note%20Types/Code.md">代码</a>笔记，即允许你存储一些编程代码并对其进行高亮的笔记。特殊情况是 JavaScript 代码笔记，它可以在 Trilium 内部执行，结合<a class="reference-link" href="Scripting/Script%20API.md">脚本 API</a> 可以提供额外的功能。

## 架构概述

为了进一步说明，我必须解释 Trilium 的基本架构——本质上它是一个经典的 Web 应用程序——它有以下两个主要组件：

*   **前端**在浏览器中运行（使用 HTML、CSS、JavaScript）——主要用于与用户交互、显示笔记等。
*   **后端**在 node.js 运行时中运行 JavaScript 代码——负责例如存储笔记、加密笔记等。

因此我们有前端和后端，各自承担不同的职责，但它们的共同特点是都运行 JavaScript 代码。再加上我们能够创建 JavaScript <a class="reference-link" href="Note%20Types/Code.md">代码</a> 笔记这一事实，我们就有了用武之地。

## 使用案例

*   <a class="reference-link" href="Scripting/Frontend%20Basics/Examples/New%20Task%20launcher%20button.md">“新建任务”启动器按钮</a>

## 操作处理器

将笔记保存到数据库是后端的职责，因此我们立即将控制权传递给后端，并请求它创建一个笔记。完成后，我们显示新创建的笔记，以便用户设置任务标题，也许还可以设置一些属性。

## 脚本执行

所以我们有一个脚本，它会将按钮添加到工具栏。但是我们如何执行它呢？一种可能性是点击“播放”图标（用红色圆圈标出）。这样做的问题是，这种 UI 更改受 Trilium 运行时的限制，因此当我们重启 Trilium 时，按钮将不复存在。

我们需要在每次 Trilium 启动时都执行它，但我们可能不想在每次启动时都手动点击播放按钮。

解决方案在底部用红色圆圈标出——这个笔记有一个 [标签](Advanced%20Usage/Attributes.md) `#run=frontendStartup`——这是 Trilium 能够理解的“系统”标签之一。正如你可能猜到的，这将导致所有此类带标签的脚本笔记在 Trilium 前端启动时执行一次。

（`#run=frontendStartup` 不适用于 [移动前端](Installation%20%26%20Setup/Mobile%20Frontend.md) —— 如果你想在那里运行脚本，请给脚本添加 `#run=mobileStartup` 标签）。

### 执行按钮

可运行的代码笔记（前端或后端）和已保存的 SQL 控制台可以选择性地在描述旁边拥有一个专用的执行按钮。

为此，请应用以下 [标签](Advanced%20Usage/Attributes/Labels.md)：

*   一个 `#executeButton`，其标签值将显示为按钮的文本。
*   一个可选的 `#executeDescription`，用于在其旁边添加解释性文本。

## 自动补全与代码检查

从 Trilium v0.104.0 开始，前端脚本、后端脚本和渲染笔记受益于自动补全系统。

自动补全会在输入 <kbd>.</kbd> 时自动触发，或通过按 <kbd>Ctrl</kbd>+<kbd>Space</kbd> 手动触发。

除此之外，编辑器还会显示语法错误和警告，例如不可达代码。

> [!注意]
> 如果你发现报告的错误/警告存在误报，或者 API 不正确或缺失，欢迎[提交一个问题](Troubleshooting/Reporting%20issues.md)并附上代码示例。

## 更多示例

你可以在 <a class="reference-link" href="Advanced%20Usage/Advanced%20Showcases.md">高级示例</a> 中查看更多带有解释的脚本用法。

## 事件

参见 <a class="reference-link" href="Scripting/Backend%20scripts/Backend%20Events.md">事件</a>。

## 脚本 API

参见 <a class="reference-link" href="Scripting/Script%20API.md">脚本 API</a>。