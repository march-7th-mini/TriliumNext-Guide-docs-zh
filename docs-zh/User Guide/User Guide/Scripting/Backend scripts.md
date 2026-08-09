# 后端脚本

与在客户端/浏览器端运行的[前端脚本](Frontend%20Basics.md)不同，后端脚本直接在 Trilium 服务器的 Node.js 环境中运行。

后端脚本既可用于<a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>（在运行服务器的设备上运行），也可用于<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>（在 PC 上运行）。

> [!IMPORTANT]
> 从 v0.104.0 版本开始，后端脚本默认禁用，以减少攻击面。更多信息请参阅<a class="reference-link" href="Security.md">安全</a>。

## 后端脚本的优势

后端脚本的优势在于它们功能强大，例如可以访问底层系统，比如读取文件或执行进程。

然而，后端脚本的主要优势在于它们可以更轻松地访问笔记，因为相关信息已经加载到内存中。而在客户端，笔记必须先手动加载。

## 创建后端脚本

创建一个新的<a class="reference-link" href="../Note%20Types/Code.md">代码</a>笔记，并选择语言 _JavaScript (Trilium backend)_。

## 运行后端脚本

后端脚本可以手动运行（通过脚本页面上的“执行”按钮），也可以在特定事件触发时运行。

此外，脚本可以在服务器启动时自动运行，也可以按固定时间间隔运行，或在特定事件（如属性被修改）发生时运行。更多信息，请参阅专门的<a class="reference-link" href="Backend%20scripts/Events.md">事件</a>页面。

## 脚本 API

Trilium 提供了一组 API，脚本可以通过 `api` 对象直接调用。有关此 API 的参考，请参阅<a class="reference-link" href="Script%20API/Backend%20API.dat">后端 API</a>。