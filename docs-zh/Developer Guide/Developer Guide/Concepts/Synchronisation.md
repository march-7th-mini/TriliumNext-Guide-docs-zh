# 同步

Trilium 实现了一个**双向同步系统**，允许用户在多台设备（桌面客户端和服务器实例）之间同步其笔记数据库。同步协议旨在处理：

*   跨设备的并发修改
*   简单的冲突解决（无需“合并冲突”提示）。
*   部分同步（仅同步更改的实体）
*   受保护笔记的同步
*   高效的带宽使用

## 同步架构

```
graph TB
    Desktop1[桌面 1<br/>客户端]
    Desktop2[桌面 2<br/>客户端]
    
    subgraph SyncServer["同步服务器"]
        SyncService[同步服务<br/>- 实体变更管理<br/>- 冲突解决<br/>- 版本跟踪]
        SyncDB[(数据库<br/>entity_changes)]
    end
    
    Desktop1 <-->|WebSocket/HTTP| SyncService
    Desktop2 <-->|WebSocket/HTTP| SyncService
    SyncService --> SyncDB
```

## 核心概念

### 实体变更

对任何实体（笔记、分支、属性等）的每次修改都会创建一个**实体变更**记录：

```
entity_changes (
    id,                    -- 自增 ID
    entityName,            -- 'notes', 'branches', 'attributes' 等
    entityId,              -- 变更实体的 ID
    hash,                  -- 用于完整性校验的内容哈希
    isErased,              -- 实体是否已被擦除（永久删除）
    changeId,              -- 唯一变更标识符
    componentId,           -- 唯一组件/小组件标识符
    instanceId,            -- 进程实例标识符
    isSynced,              -- 是否已同步到服务器
    utcDateChanged         -- 变更发生时间
)
```

**关键属性：**

*   **changeId**：变更的全局唯一标识符 (UUID)
*   **componentId**：生成变更的组件/小组件的唯一标识符（可用于避免刷新正在编辑的小组件）。
*   **instanceId**：每个进程唯一（重启时更改）
*   **hash**：用于完整性验证的实体数据 SHA-256 哈希

### 同步版本

每个 Trilium 安装都会跟踪：

*   **本地同步版本**：本地看到的最新变更 ID
*   **服务器同步版本**：服务器上的最新变更 ID
*   **实体版本**：每种实体类型的最后同步版本

### 变更跟踪

**当实体被修改时：**

```typescript
// apps/server/src/services/entity_changes.ts
function addEntityChange(entityName, entityId, entity) {
    const hash = calculateHash(entity)
    const changeId = generateUUID()
    
    sql.insert('entity_changes', {
        entityName,
        entityId,
        hash,
        changeId,
        componentId: config.componentId,
        instanceId: config.instanceId,
        isSynced: 0,
        utcDateChanged: now()
    })
}
```

**实体修改触发条件：**

*   笔记内容更新
*   笔记元数据变更
*   分支创建/删除/重新排序
*   属性添加/移除
*   选项修改

## 同步协议

### 同步握手

**步骤 1：客户端发起同步**

```typescript
// 客户端发送当前同步版本
POST /api/sync/check
{
    "sourceId": "client-component-id",
    "maxChangeId": 12345
}
```

**步骤 2：服务器响应状态**

```typescript
// 服务器检查变更
响应:
{
    "entityChanges": 567,        // 服务器上的变更
    "maxChangeId": 12890,        // 服务器的最大变更 ID
    "outstandingPushCount": 23   // 尚未同步的客户端变更
}
```

**步骤 3：决策**

*   如果 `entityChanges > 0`：从服务器拉取变更
*   如果 `outstandingPushCount > 0`：向服务器推送变更
*   两者可以按顺序进行

### 拉取同步（服务器 → 客户端）

**客户端请求变更：**

```typescript
POST /api/sync/pull
{
    "sourceId": "client-component-id",
    "lastSyncedChangeId": 12345
}
```

**服务器响应：**

```typescript
响应:
{
    "notes": [
        { noteId: "abc", title: "新笔记", ... }
    ],
    "branches": [...],
    "attributes": [...],
    "revisions": [...],
    "attachments": [...],
    "entityChanges": [
        { entityName: "notes", entityId: "abc", changeId: "...", ... }
    ],
    "maxChangeId": 12890
}
```

**客户端处理：**

1.  将实体变更应用到本地数据库
2.  更新 Froca 缓存
3.  更新本地同步版本
4.  触发 UI 刷新

### 推送同步（客户端 → 服务器）

**客户端发送变更：**

```typescript
POST /api/sync/push
{
    "sourceId": "client-component-id",
    "entities": [
        {
            "entity": {
                "noteId": "xyz",
                "title": "已修改的笔记",
                ...
            },
            "entityChange": {
                "changeId": "change-uuid",
                "entityName": "notes",
                ...
            }
        }
    ]
}
```

**服务器处理：**

1.  验证变更
2.  检查冲突
3.  将变更应用到数据库
4.  更新 Becca 缓存
5.  标记为已同步
6.  通过 WebSocket 广播给其他已连接的客户端

**冲突检测：**

```typescript
// 检查自客户端上次同步以来实体是否在服务器上被修改
const serverEntity = becca.getNote(noteId)
const serverLastModified = serverEntity.utcDateModified

if (serverLastModified > clientSyncVersion) {
    // 冲突！
    resolveConflict(serverEntity, clientEntity)
}
```

## 冲突解决

### 冲突类型

**1\. 内容冲突**

*   客户端和服务器都修改了同一笔记内容
*   **解决方式**：基于 `utcDateModified` 的最后写入者胜出

**2\. 结构冲突**

*   分支在一侧被移动/删除，在另一侧被修改
*   **解决方式**：墓碑记录，对账

**3\. 属性冲突**

*   同一属性被不同地修改
*   **解决方式**：最后写入者胜出

### 冲突解决策略

**最后写入者胜出：**

```typescript
if (clientEntity.utcDateModified > serverEntity.utcDateModified) {
    // 客户端胜出，应用客户端更改
    applyClientChange(clientEntity)
} else {
    // 服务器胜出，拒绝客户端更改
    // 客户端将在下次同步时拉取服务器版本
}
```

**墓碑记录：**

*   已删除的实体在 `entity_changes` 中留下墓碑
*   防止已删除项目被重新同步
*   永久删除时 `isErased = 1`

### 受保护笔记同步

**挑战：** 加密内容在没有密码的情况下无法同步

**解决方案：**

1.  **加密同步**：内容以加密形式同步
2.  **哈希验证**：无需解密即可检查完整性
3.  **延迟解密**：仅在访问时解密

## 同步状态

### 连接状态

*   **已连接**：WebSocket 连接处于活动状态
*   **已断开**：未连接到同步服务器
*   **同步中**：正在积极传输数据
*   **冲突**：因冲突而暂停同步

### 实体同步状态

每个实体可以处于以下状态：

*   **已同步**：与服务器同步
*   **待处理**：本地更改尚未推送
*   **冲突**：检测到冲突的更改

### UI 指示器

```typescript
// apps/client/src/widgets/sync_status.ts
class SyncStatusWidget {
    showSyncStatus() {
        if (isConnected && allSynced) {
            showIcon('synced')
        } else if (isSyncing) {
            showIcon('syncing-spinner')
        } else {
            showIcon('not-synced')
        }
    }
}
```

## 性能优化

### 增量同步

仅传输自上次同步以来更改的实体：

```
SELECT * FROM entity_changes 
WHERE id > :lastSyncedChangeId 
ORDER BY id ASC
LIMIT 1000
```

### 批量处理

更改分批发送以减少往返次数：

```typescript
const BATCH_SIZE = 1000
const changes = getUnsyncedChanges(BATCH_SIZE)
await syncBatch(changes)
```

### 基于哈希的变更检测

```typescript
// 仅在哈希不同时同步
const localHash = calculateHash(localEntity)
const serverHash = getServerHash(entityId)

if (localHash !== serverHash) {
    syncEntity(localEntity)
}
```

### 压缩

大型负载在传输前进行压缩：

```typescript
// 服务器发送压缩响应
res.setHeader('Content-Encoding', 'gzip')
res.send(gzip(syncData))
```

## 错误处理

### 网络错误

报告给用户，同步将在间隔时间过后重试。

### 同步完整性检查

**哈希验证：**

```typescript
// 验证实体哈希是否匹配
const calculatedHash = calculateHash(entity)
const receivedHash = entityChange.hash

if (calculatedHash !== receivedHash) {
    throw new Error('哈希不匹配 - 检测到数据损坏')
}
```

**一致性检查：**

*   孤立分支检测
*   缺失父笔记
*   无效实体引用
*   循环依赖

## 同步服务器配置

### 服务器设置

**必需选项：**

```javascript
{
    "syncServerHost": "https://sync.example.com",
    "syncServerTimeout": 60000,
    "syncProxy": ""  // 可选 HTTP 代理
}
```

**身份验证：**

*   用户名/密码 或
*   同步令牌（在服务器上生成）

## 同步 API 端点

位于：`apps/server/src/routes/api/sync.ts`

## WebSocket 同步更新

通过 WebSocket 进行实时同步：

```typescript
// 服务器向所有已连接的客户端广播更改
ws.broadcast('frontend-update', {
    lastSyncedPush,
    entityChanges
})

// 客户端接收并处理信息。
```

## 同步调度

### 自动同步

**桌面：**

*   启动时同步
*   定期同步（可配置间隔，默认：60 秒）

**服务器：**

*   实体修改时同步
*   通过 WebSocket 推送给已连接的客户端

### 手动同步

用户可以触发：

*   完全同步
*   立即同步
*   同步特定子树

## 故障排除

### 常见问题

**同步卡住：**

```
-- 重置同步状态
UPDATE entity_changes SET isSynced = 0;
DELETE FROM options WHERE name LIKE 'sync%';
```

**哈希不匹配：**

*   检测到数据损坏
*   从备份重新同步
*   检查数据库完整性

**冲突循环：**

*   需要手动干预
*   导出冲突笔记
*   选择胜出版本
*   重新同步

## 安全考虑

### 加密同步

*   受保护笔记以加密形式同步
*   网络上无明文传输
*   服务器无法读取受保护内容

### 身份验证

*   用户名/密码仅通过 HTTPS
*   用于基于令牌认证的同步令牌
*   带有 CSRF 保护的会话 Cookie

### 授权

*   用户只能同步自己的数据
*   不支持跨用户同步
*   同步服务器验证所有权

## 性能指标

**典型同步性能：**

*   1000 个更改：约 2-5 秒
*   10000 个更改：约 20-50 秒
*   初始完全同步（10 万条笔记）：约 5-10 分钟

**影响因素：**

*   网络延迟
*   数据库大小
*   受保护笔记数量
*   附件大小