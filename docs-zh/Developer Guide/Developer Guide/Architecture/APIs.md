# API

### 内部 API

**REST 端点** (`/api/*`)

前端用于所有操作：

**笔记操作：**

*   `GET /api/notes/:noteId` - 获取笔记
*   `POST /api/notes/:noteId/content` - 更新内容
*   `PUT /api/notes/:noteId` - 更新元数据
*   `DELETE /api/notes/:noteId` - 删除笔记

**树操作：**

*   `GET /api/tree` - 获取笔记树
*   `POST /api/branches` - 创建分支
*   `PUT /api/branches/:branchId` - 更新分支
*   `DELETE /api/branches/:branchId` - 删除分支

**搜索：**

*   `GET /api/search?query=...` - 搜索笔记
*   `GET /api/search-note/:noteId` - 执行搜索笔记

### ETAPI（外部 API）

位置：`apps/server/src/etapi/`

**用途：** 第三方集成和自动化

**身份验证：** 基于令牌（ETAPI 令牌）

**OpenAPI 规范：** 自动生成

**关键端点：**

*   `/etapi/notes` - 笔记增删改查
*   `/etapi/branches` - 分支管理
*   `/etapi/attributes` - 属性操作
*   `/etapi/attachments` - 附件处理

**示例：**

```
curl -H "Authorization: YOUR_TOKEN" \
  https://trilium.example.com/etapi/notes/noteId
```

### WebSocket API

位置：`apps/server/src/services/ws.ts`

**用途：** 实时更新和同步

**协议：** WebSocket（类似 Socket.IO 的自定义协议）

**消息类型：**

*   `sync` - 同步请求
*   `entity-change` - 实体更新通知
*   `refresh-tree` - 树结构已更改
*   `open-note` - 在界面中打开笔记

**客户端订阅：**

```typescript
ws.subscribe('entity-change', (data) => {
    froca.processEntityChange(data)
})
```