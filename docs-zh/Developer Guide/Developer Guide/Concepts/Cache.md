# 缓存
### 三层缓存系统

Trilium 实现了一套精密的**三层缓存系统**，以优化性能并支持离线功能：

#### 1. Becca（后端缓存）

位于：`apps/server/src/becca/`

```typescript
// Becca 将所有实体缓存在内存中
class Becca {
    notes: Record<string, BNote>
    branches: Record<string, BBranch>
    attributes: Record<string, BAttribute>
    attachments: Record<string, BAttachment>
    // ... 其他实体集合
}
```

**职责：**

*   服务端实体缓存
*   在内存中维护完整的笔记树
*   处理实体关系与完整性
*   提供无需数据库查询的快速查找
*   管理实体生命周期（创建、更新、删除）

**关键文件：**

*   `becca.ts` - 主缓存实例
*   `becca_loader.ts` - 从数据库加载实体
*   `becca_service.ts` - 缓存管理操作
*   `entities/` - 实体类（BNote、BBranch 等）

#### 2. Froca（前端缓存）

位于：`apps/client/src/services/froca.ts`

```typescript
// Froca 是后端数据的只读镜像
class Froca {
    notes: Record<string, FNote>
    branches: Record<string, FBranch>
    attributes: Record<string, FAttribute>
    // ... 其他实体集合
}
```

**职责：**

*   前端只读缓存
*   笔记树的懒加载
*   最小化 API 调用
*   支持快速 UI 渲染
*   通过 WebSocket 与后端同步

**加载策略：**

*   初始加载：根笔记及直接子节点
*   懒加载：访问到笔记时才加载
*   笔记加载时，其所有父分支和子分支一并加载
*   已删除的实体通过缺失的分支进行追踪

#### 3. Shaca（分享缓存）

位于：`apps/server/src/share/`

**职责：**

*   针对已分享/已发布笔记的优化缓存
*   处理无需身份验证的公共笔记访问
*   针对高流量场景进行性能优化
*   与主 Becca 分离，以隔离关注点

### 缓存失效

**服务端：**

*   实体保存时自动更新缓存
*   WebSocket 向所有客户端广播变更
*   同步更新触发缓存刷新

**客户端：**

*   WebSocket 监听器更新 Froca
*   通过 `froca.loadSubTree(noteId)` 手动重新加载
*   受保护会话变更时进行完整重新加载

### 缓存一致性

**实体变更追踪：**

```typescript
// 追踪每一次实体修改
entity_changes (
    entityName: 'notes',
    entityId: 'note123',
    hash: 'abc...',
    changeId: 'change456',
    utcDateChanged: '2025-11-02...'
)
```

**同步协议：**

1.  客户端请求自上次同步以来的变更
2.  服务器返回 entity\_changes 记录
3.  客户端将变更应用到 Froca
4.  客户端将本地变更发送至服务器
5.  服务器更新 Becca 和数据库