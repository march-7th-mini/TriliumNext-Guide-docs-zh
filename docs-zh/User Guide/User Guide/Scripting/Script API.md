# 脚本 API

对于[脚本代码笔记](../Scripting.md)，Trilium 提供了一个 API，使它们能够访问应用程序的各种功能。

有两种 API：

*   一种用于前端脚本：<a class="reference-link" href="Script%20API/Frontend%20API">前端 API</a>
*   一种用于后端脚本：<a class="reference-link" href="Script%20API/Backend%20API.dat">后端 API</a>

在这两种情况下，API 都存在于一个全局变量 `api` 中，可以在脚本中的任何位置使用。

例如，要向用户显示一条消息，可以使用以下前端脚本：

```
api.showMessage("Hello world.");
```

> [!NOTE]
> **注意**  
> 脚本 API 目前处于实验阶段，在未来的更新中可能会发生变化。