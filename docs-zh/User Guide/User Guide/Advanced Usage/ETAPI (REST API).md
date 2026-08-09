# ETAPI（REST API）
> [!提示]
> 如需快速入门，请参阅 <a class="reference-link" href="ETAPI%20(REST%20API)/API%20Reference.dat">API 参考</a>。

ETAPI 是 Trilium 的公共/外部 REST API。自 Trilium v0.50 起可用。

## API 客户端

除了直接调用 API 之外，还可以使用客户端库来简化此过程

*   [trilium-py](https://github.com/Nriver/trilium-py)，您可以使用 Python 与 Trilium 进行通信。

## 获取令牌

所有与 REST API 相关的操作都必须使用令牌进行身份验证。您可以通过“选项”->“ETAPI”获取此令牌，或者使用 `/auth/login` REST 调用以编程方式获取（请参阅[规范](https://github.com/TriliumNext/Trilium/blob/master/src/etapi/etapi.openapi.yaml)）。

## 身份验证

### 通过 `Authorization` 请求头

```
GET https://myserver.com/etapi/app-info
Authorization: ETAPITOKEN
```

其中 `ETAPITOKEN` 是上一步中获取的令牌。

为了与各种工具兼容，也可以使用 `Bearer ETAPITOKEN` 格式指定 `Authorization` 请求头的值（自 0.93.0 起）。

### 基本身份验证

自 v0.56 起，您还可以使用基本身份验证格式：

```
GET https://myserver.com/etapi/app-info
Authorization: Basic BATOKEN
```

*   其中 `BATOKEN = BASE64(username + ':' + password)` - 这是标准的 Basic Auth 序列化格式
*   其中 `username` 为 "etapi"
*   而 `password` 是上述生成的 ETAPI 令牌。

基本身份验证旨在用于仅支持基本身份验证的工具。

## 使用 Bash 脚本进行交互

可以编写简单的 Bash 脚本来与 Trilium 进行交互。例如，以下是如何获取笔记的 HTML 内容：

```
#!/usr/bin/env bash

# 配置
TOKEN=z1vA4fkGxjOR_ZXLrZeqHEFOv65yV3882iFCRtNIK9k9iWrHliITNSLQ=
SERVER=http://localhost:8080

# 按 ID 下载笔记
NOTE_ID="i6ra4ZshJhgN"
curl "$SERVER/etapi/notes/$NOTE_ID/content" -H "Authorization: $TOKEN" 
```

请确保替换以下值：

*   将 `TOKEN` 替换为您的 ETAPI 令牌。
*   将 `SERVER` 替换为您的 Trilium 实例的正确协议、主机名和端口。
*   将 `NOTE_ID` 替换为要下载的现有笔记 ID。

再举一个例子，要获取笔记的 .zip 导出文件并将其放入名为 `out` 的目录中，只需将脚本中的最后一条语句替换为：

```
curl -H "Authorization: $TOKEN" \
	-X GET "$SERVER/etapi/notes/$NOTE_ID/export" \
    --output "out/$NOTE_ID.zip"
```