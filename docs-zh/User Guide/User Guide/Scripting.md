# 脚本

Trilium 支持创建 <a class="reference-link" href="Note%20Types/Code.md">代码</a> 笔记，即允许你存储一些编程代码并对其进行高亮显示的笔记。特殊情况是 JavaScript 代码笔记，它们还可以在 Trilium 内部执行，结合 <a class="reference-link" href="Scripting/Script%20API.md">脚本 API</a> 可以提供额外的功能。

## 架构概览

为了进一步说明，我必须解释 Trilium 的基本架构——本质上它是一个经典的 Web 应用程序——它有两个主要组件：

*   运行在浏览器中的前端（使用 HTML、CSS、JavaScript）——主要用于与用户交互、显示笔记等。
*   运行在 node.js 运行时中的后端 JavaScript 代码——负责例如存储笔记、加密笔记等。

所以我们有前端和后端，各自有各自的职责，但它们的共同特征是都运行 JavaScript 代码。再加上我们能够创建 JavaScript <a class="reference-link" href="Note%20Types/Code.md">代码</a> 笔记，这就很有意思了。

## 使用场景

*   <a class="reference-link" href="Scripting/Frontend%20Basics/Examples/New%20Task%20launcher%20button.md">"新建任务"启动器按钮</a>

## 操作处理器

将笔记保存到数据库是后端的职责，因此我们立即将控制权交给后端，请求它创建一条笔记。完成后，我们显示新创建的笔记，以便用户可以设置任务标题以及一些属性。

## 脚本执行

现在我们有了一个将按钮添加到工具栏的脚本。但如何执行它呢？一种可能是点击 <span class="tn-icon bx bx-play"></span> _执行脚本_ 按钮。这样做的问题在于，这个 UI 变更受 Trilium 运行时的时间限制，所以当我们重启 Trilium 时，按钮就不在了。

我们需要在每次 Trilium 启动时执行它，但可能不想在每次启动时都手动点击播放按钮。

解决方案是给笔记添加 [标签](Advanced%20Usage/Attributes.md) `#run=frontendStartup`——这是 Trilium 理解的"系统"标签之一。如你所料，这会导致所有带有此标签的脚本笔记在 Trilium 前端启动时被执行一次。

（`#run=frontendStartup` 对 [移动端前端](Installation%20%26%20Setup/Mobile%20Frontend.md) 不起作用——如果你希望脚本在那里运行，请给脚本添加 `#run=mobileStartup` 标签）。

### 执行按钮

可运行的代码笔记（前端或后端）以及已保存的 SQL 控制台可以选择在描述旁边拥有一个专用的 <span class="tn-icon bx bx-play"></span> 执行按钮。

为此，请应用以下 [标签](Advanced%20Usage/Attributes/Labels.md)：

*   一个 `#executeButton`，其标签值将作为按钮的标签显示。
*   一个可选的 `#executeDescription`，用于在其旁边添加说明性文本。

## 自动补全与代码检查

从 Trilium v0.104.0 开始，前端脚本、后端脚本和渲染笔记受益于自动补全系统。

自动补全在输入名称时或输入 <kbd>.</kbd> 后自动打开，也可以通过按 <kbd>Ctrl</kbd>+<kbd>Space</kbd> 手动打开。其列表的外观和工作方式类似于文本笔记的 <kbd>/</kbd> 列表：每个条目都有表示其类型的图标（函数、属性、类……），按 <kbd>Enter</kbd> 或 <kbd>Tab</kbd> 插入高亮项，按 <kbd>Esc</kbd> 关闭。

除此之外，编辑器还会显示语法错误和警告，例如不可达代码。

> [!NOTE]
> 如果你发现报告的错误/警告存在误报，或者 API 不正确或缺失，欢迎附上代码示例 [提交 issue](Troubleshooting/Reporting%20issues.md)。

## 更多展示

你可以在 <a class="reference-link" href="Advanced%20Usage/Advanced%20Showcases.md">高级展示</a> 中看到更多带解释的脚本示例。

## 事件

参见 <a class="reference-link" href="Scripting/Backend%20scripts/Backend%20Events.md">事件</a>。

## 脚本 API

参见 <a class="reference-link" href="Scripting/Script%20API.md">脚本 API</a>。