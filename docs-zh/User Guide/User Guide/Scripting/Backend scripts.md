# 后端脚本

与在客户端/浏览器端运行的[前端脚本](Frontend%20Basics.md)不同，后端脚本直接运行在 Trilium 服务器的 Node.js 环境中。

后端脚本既可用于<a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>（脚本将在运行服务器的设备上执行），也可用于<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>（脚本将在个人电脑上执行）。

> [!IMPORTANT]
> 从 v0.104.0 版本开始，后端脚本默认禁用，以减少攻击面。更多信息请参阅<a class="reference-link" href="Security.md">安全</a>。

## 后端脚本的优势

后端脚本的优势在于其功能相当强大，例如可以访问底层系统，比如读取文件或执行进程。

然而，后端脚本的主要优势在于它们更容易访问笔记，因为笔记的相关信息已经加载到内存中。而在客户端，笔记需要首先手动加载。

## 创建后端脚本

创建一个新的<a class="reference-link" href="../Note%20Types/Code.md">代码</a>笔记，并选择语言 _JavaScript (Trilium backend)_。

## 运行后端脚本

后端脚本可以手动运行（通过脚本页面上的“执行”按钮），也可以在特定事件发生时触发运行。

此外，脚本还可以在服务器启动时、按固定时间间隔或当特定事件发生（如属性被修改）时自动运行。更多信息，请参阅专门的<a class="reference-link" href="Backend%20scripts/Backend%20Events.md">事件</a>页面。

## 脚本 API

Trilium 提供了一组 API，脚本可以通过 `api` 对象直接调用。有关此 API 的参考，请参阅<a class="reference-link" href="Script%20API/Backend%20API.dat">后端 API</a>。