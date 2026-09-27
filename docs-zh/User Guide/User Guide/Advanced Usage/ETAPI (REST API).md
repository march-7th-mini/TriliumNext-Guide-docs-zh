# ETAPI (REST API)
> [!TIP]
> 如需快速上手，请参阅 <a class="reference-link" href="ETAPI%20(REST%20API)/API%20Reference.dat">API 参考</a>。

ETAPI 是 Trilium 的公共/外部 REST API。自 Trilium v0.50 起可用。

## API 客户端

除了直接调用 API 之外，还有一些客户端库可以简化这一过程

*   [trilium-py](https://github.com/Nriver/trilium-py)，你可以使用 Python 与 Trilium 通信。

## 获取令牌

所有 REST API 操作都必须使用令牌进行身份验证。你可以从 选项 -> ETAPI 获取此令牌，也可以通过 `/auth/login` REST 调用以编程方式获取（参见[规范](https://github.com/TriliumNext/Trilium/blob/master/src/etapi/etapi.openapi.yaml)）。

## 身份验证

### 通过 `Authorization` 请求头

```
GET https://myserver.com/etapi/app-info
Authorization: ETAPITOKEN
```

其中 `ETAPITOKEN` 是上一步中获取的令牌。

为了与各种工具兼容，也可以使用 `Bearer ETAPITOKEN` 格式指定 `Authorization` 请求头的值（自 0.93.0 起）。

### 基本身份验证

自 v0.56 起，你也可以使用基本身份验证格式：

```
GET https://myserver.com/etapi/app-info
Authorization: Basic BATOKEN
```

*   其中 `BATOKEN = BASE64(username + ':' + password)` —— 这是标准的 Basic Auth 序列化格式
*   其中 `username` 为 "etapi"
*   而 `password` 为上述生成的 ETAPI 令牌。

基本身份验证适用于仅支持 basic auth 的工具。

## 使用 Bash 脚本进行交互

可以编写简单的 Bash 脚本来与 Trilium 交互。例如，以下是如何获取笔记的 HTML 内容：

```
#!/usr/bin/env bash

# Configuration
TOKEN=z1vA4fkGxjOR_ZXLrZeqHEFOv65yV3882iFCRtNIK9k9iWrHliITNSLQ=
SERVER=http://localhost:8080

# Download a note by ID
NOTE_ID="i6ra4ZshJhgN"
curl "$SERVER/etapi/notes/$NOTE_ID/content" -H "Authorization: $TOKEN" 
```

请确保替换以下各项的值：

*   `TOKEN` 替换为你的 ETAPI 令牌。
*   `SERVER` 替换为你的 Trilium 实例的正确协议、主机名和端口。
*   `NOTE_ID` 替换为要下载的现有笔记 ID。

再举一个例子，要获取笔记的 .zip 导出文件并将其放入名为 `out` 的目录中，只需将脚本中的最后一条语句替换为：

```
curl -H "Authorization: $TOKEN" \
	-X GET "$SERVER/etapi/notes/$NOTE_ID/export" \
    --output "out/$NOTE_ID.zip"
```

## 上传二进制内容

JSON 请求体只能携带文本，因此 `POST /etapi/attachments` 的 `content` 字段存储的正是它接收到的字符串。要上传图片、PDF 或任何其他二进制文件，请将原始字节以 `application/octet-stream` 内容类型发送到内容端点。笔记的内容（`PUT /etapi/notes/{noteId}/content`）也是如此。

要将文件附加到笔记，请先创建不带内容的附件，然后将文件上传到该附件：

```
ATTACHMENT_ID=$(curl -s -X POST "$SERVER/etapi/attachments" \
    -H "Authorization: $TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"ownerId\": \"$NOTE_ID\", \"role\": \"file\", \"mime\": \"application/pdf\", \"title\": \"report.pdf\", \"position\": 10}" \
    | jq -r .attachmentId)

curl -X PUT "$SERVER/etapi/attachments/$ATTACHMENT_ID/content" \
    -H "Authorization: $TOKEN" \
    -H "Content-Type: application/octet-stream" \
    --data-binary @report.pdf
```

请使用 `--data-binary` 而不是 `-d`，因为后者会去除文件中的换行符。对于图片，请将 `role` 设置为 `image`，并将 `mime` 设置为图片的类型，例如 `image/png`。