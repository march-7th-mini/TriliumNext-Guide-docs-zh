# 前端事件

前端脚本可以在某些触发条件下自动运行。

为此，请将 `run` [标签](../../Advanced%20Usage/Attributes/Labels.md) 设置为以下任一值：

*   `frontendStartup` - 当 Trilium 前端启动（或刷新）时，但不包括移动端。
*   `mobileStartup` - 当 Trilium 前端启动（或刷新）时，在移动端上。

> [!NOTE]
> 一个脚本可以被多个事件触发，这可以通过添加多个 `run` 标签来实现。**不支持**用逗号分隔多个值。

后端脚本拥有更强大的触发条件，例如它们可以按小时或按天自动运行，也可以在诸如笔记被创建或属性被修改等事件时运行。有关更多信息，请参阅服务器端的 <a class="reference-link" href="../Backend%20scripts/Backend%20Events.md">事件</a>。

## 安全模式

当 [安全模式](../../Advanced%20Usage/Safe%20mode.md) 激活时，带有事件的脚本将不会触发。