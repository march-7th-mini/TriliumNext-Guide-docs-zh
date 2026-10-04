# 后端脚本
与在客户端/浏览器端运行的[前端脚本](Frontend%20Basics.md)不同，后端脚本直接在 Trilium 服务器的 Node.js 环境中运行。

后端脚本既可以在 <a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a> 中使用（此时它将在运行服务器的设备上运行），也可以在 <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 中使用（此时它将在 PC 上运行）。

> [!IMPORTANT]
> 从 v0.104.0 开始，后端脚本默认被禁用，以减少攻击面。更多信息请参见 <a class="reference-link" href="Security.md">安全</a>。

## 后端脚本的优势

后端脚本的优势在于它们可以非常强大，例如可以访问底层系统，比如读取文件或执行进程。

然而，后端脚本的主要优势在于它们更容易访问笔记，因为有关笔记的信息已经加载在内存中。而在客户端，笔记必须首先手动加载。

## 创建后端脚本

创建一个新的 <a class="reference-link" href="../Note%20Types/Code.md">代码</a> 笔记，并选择语言 _JavaScript (Trilium backend)_。

## 运行后端脚本

后端脚本既可以手动运行（通过脚本页面上的执行按钮），也可以在特定事件触发时运行。

当脚本手动运行或从启动器运行时抛出错误，Trilium 会显示一个 _脚本错误_ 通知，其中包含错误消息以及指向失败笔记的链接。如果错误来自脚本所需的子笔记，则链接指向该子笔记。脚本在错误发生之前对笔记所做的更改将被回滚。

此外，脚本还可以在服务器启动时、按固定时间间隔或在特定事件发生时（例如属性被修改）自动运行。更多信息请参见专门的 <a class="reference-link" href="Backend%20scripts/Backend%20Events.md">事件</a> 页面。

## 脚本 API

Trilium 在 `api` 对象下公开了一组可供脚本直接使用的 API。有关此 API 的参考，请参见 <a class="reference-link" href="Script%20API/Backend%20API.dat">后端 API</a>。