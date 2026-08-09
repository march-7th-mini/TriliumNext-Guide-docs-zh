# 自定义请求处理器

Trilium 提供了一种机制，允许[脚本](../Scripting.md)开放一个公共 REST 端点。这为与其他服务的各种集成开辟了道路——一个简单的例子是通过 Slack 发出斜杠命令（例如 `/trilium buy milk`）来创建新笔记。

## 从 Trilium 外部创建笔记

让我们看一个例子。目标是提供一个 REST 端点，我们可以向其发送标题和内容，然后 Trilium 将创建一个笔记。

我们将从创建一个包含以下内容的 JavaScript 后端[代码笔记](../Note%20Types/Code.md)开始：

```
const {req, res} = api;
const {secret, title, content} = req.body;

if (req.method == 'POST' && secret === 'secret-password') {
    // 笔记必须保存在由父笔记指定的树层次结构中的某个位置。
    // 这是通过从此代码笔记到“目标”父笔记的关系来定义的。
    // 或者，为简单起见，您可以直接使用常量 noteId（从所需父笔记的“笔记信息”对话框中获取）
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
*   关系 `~targetNote`，指向新笔记应保存到的笔记

### 解释

让我们使用 HTTP 客户端发送请求来测试一下：

```
POST http://your-trilium-server/custom/create-note
Content-Type: application/json

{
  "secret": "secret-password",
  "title": "hello",
  "content": "world"
}+++++++++++++++++++++++++++++++++++++++++++++++
```

注意请求路径中的 `/custom` 部分——Trilium 将任何带有此前缀的请求视为“自定义”请求，并通过查找所有具有 `customRequestHandler` [标签](Attributes.md) 的笔记来尝试找到匹配的处理器。然后，此标签的值包含一个正则表达式，该表达式将匹配请求路径（在我们的例子中，是简单的正则表达式 "create-note"）。

然后，Trilium 将找到我们上面创建的代码笔记并执行它。`api.req` 和 `api.res` 被设置为 [请求](https://expressjs.com/en/api.html#req) 和 [响应](https://expressjs.com/en/api.html#res) 对象，我们可以从中获取请求的详细信息并做出响应。

在代码笔记中，我们检查请求方法，然后使用简单的身份验证——请记住，这些端点默认是完全未认证的，您需要自己处理这个问题。

一旦我们通过这些检查，我们将使用 [脚本 API](../Scripting/Script%20API.md) 创建所需的笔记。

## 自定义资源提供器

另一个常见的用例是您只想公开一个文件笔记——在这种情况下，您创建标签 `customResourceProvider`（值同样是路径正则表达式）。

有关更多信息，请参阅 [自定义资源提供器](Custom%20Resource%20Providers.md)。

## 高级概念

`api.req` 和 `api.res` 是 Express.js 对象——您可以随时查看其 [文档](https://expressjs.com/en/api.html) 以了解详细信息。

### 参数

REST 请求路径通常在 URL 中包含参数，例如：

```
http://your-trilium-server/custom/notes/123
```

最后一部分是动态的，因此 URL 的匹配也必须是动态的——因此，匹配使用正则表达式完成。以下 `customRequestHandler` 值将匹配它：

```
notes/([0-9]+)
```

此外，这也通过使用括号定义了一个匹配组，这使得提取值更加容易。匹配的组可在 `api.pathParams` 中获得：

```
const noteId = api.pathParams[0];
```

通常您还需要查询参数（例如 `http://your-trilium-server/custom/notes?noteId=123`），您可以使用标准的 express `req.query.noteId` 来获取这些参数。