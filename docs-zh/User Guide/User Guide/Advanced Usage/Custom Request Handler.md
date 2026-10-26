# 自定义请求处理器

Trilium 为[脚本](../Scripting.md)提供了一种打开公共 REST 端点的机制。这为与其他服务的各种集成开辟了途径——一个简单的例子是通过发出斜杠命令（例如 `/trilium buy milk`）从 Slack 创建新笔记。

## 从 Trilium 外部创建笔记

让我们看一个例子。目标是提供一个 REST 端点，我们可以向其发送标题和内容，Trilium 将创建一条笔记。

我们首先创建一个 JavaScript 后端[代码笔记](../Note%20Types/Code.md)，内容包含：

```
const {req, res} = api;
const {secret, title, content} = req.body;

if (req.method == 'POST' && secret === 'secret-password') {
    // notes must be saved somewhere in the tree hierarchy specified by a parent note. 
    // This is defined by a relation from this code note to the "target" parent note
    // alternatively you can just use constant noteId for simplicity (get that from "Note info" dialog of the desired parent note)
    const targetParentNoteId = api.currentNote.getRelationValue('targetNote');
    
    const {note} = api.createTextNote(targetParentNoteId, title, content);
    const notePojo = note.getPojo();

    res.status(201).json(notePojo);
}
else {
    res.send(400);
}
```

此脚本笔记还具有以下两个属性：

*   标签 `#customRequestHandler`，值为 `create-note`
*   关系 `~targetNote` 指向应保存新笔记的笔记

### 说明

让我们通过使用 HTTP 客户端发送请求来测试这一点：

```
POST http://your-trilium-server/custom/create-note
Content-Type: application/json

{
  "secret": "secret-password",
  "title": "hello",
  "content": "world"
}+++++++++++++++++++++++++++++++++++++++++++++++
```

注意请求路径中的 `/custom` 部分——Trilium 将任何带有此前缀的请求视为“自定义”请求，并通过查看所有带有 `customRequestHandler` [标签](Attributes.md)的笔记来尝试找到匹配的处理器。此标签的值包含一个正则表达式，它将匹配请求路径（在我们的例子中是简单的正则表达式 "create-note"）。

然后 Trilium 会找到我们上面创建的代码笔记并执行它。`api.req`、`api.res` 被设置为来自 [request](https://expressjs.com/en/api.html#req) 和 [response](https://expressjs.com/en/api.html#res) 的对象，我们可以从中获取请求的详细信息并进行响应。

在代码笔记中，我们检查请求方法，然后使用简单的身份验证——请记住，这些端点默认是完全未经身份验证的，你需要自行处理这一点。

一旦通过这些检查，我们将使用[脚本 API](../Scripting/Script%20API.md) 创建所需的笔记。

## 自定义资源提供程序

另一个常见用例是你只想公开一个文件笔记——在这种情况下，你创建标签 `customResourceProvider`（值同样是路径正则表达式）。

有关更多信息，请参阅[自定义资源提供程序](Custom%20Resource%20Providers.md)。

## 高级概念

`api.req` 和 `api.res` 是 Express.js 对象——你可以随时查阅其[文档](https://expressjs.com/en/api.html)了解详情。

### 参数

REST 请求路径通常包含 URL 中的参数，例如：

```
http://your-trilium-server/custom/notes/123
```

最后一部分是动态的，因此 URL 的匹配也必须是动态的——为此，匹配是通过正则表达式完成的。以下 `customRequestHandler` 值将匹配它：

```
notes/([0-9]+)
```

此外，这还通过使用括号定义了一个匹配组，从而使提取值更加容易。匹配的组可在 `api.pathParams` 中使用：

```
const noteId = api.pathParams[0];
```

通常你还需要查询参数（例如 `http://your-trilium-server/custom/notes?noteId=123`），你可以使用标准的 express `req.query.noteId` 获取它们。