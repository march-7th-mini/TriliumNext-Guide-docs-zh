# 前端

### 应用入口点

**桌面端：** `apps/client/src/desktop.ts` **网页端：** `apps/client/src/index.ts`

### 服务层

位于：`apps/client/src/services/`

关键服务：

*   `froca.ts` - 前端缓存
*   `server.ts` - API 通信
*   `ws.ts` - WebSocket 连接
*   `tree_service.ts` - 笔记树管理
*   `note_context.ts` - 活动笔记追踪
*   `protected_session.ts` - 加密密钥管理
*   `link.ts` - 笔记链接与导航
*   `export.ts` - 笔记导出功能

### UI 组件

**组件位置：**

*   `widgets/containers/` - 布局容器
*   `widgets/buttons/` - 工具栏按钮
*   `widgets/dialogs/` - 模态对话框
*   `widgets/ribbon_widgets/` - 标签页小组件
*   `widgets/type_widgets/` - 笔记类型编辑器

### 事件系统

**应用事件：**

```typescript
// 订阅事件
appContext.addBeforeUnloadListener(() => {
    // 页面卸载前的清理工作
})

// 触发事件
appContext.trigger('noteTreeLoaded')
```

**笔记上下文事件：**

```typescript
// NoteContextAwareWidget 自动接收：
- noteSwitched()
- noteChanged()
- refresh()
```

### 状态管理

Trilium 使用**自定义状态管理**而非 Redux/MobX：

*   `note_context.ts` - 活动笔记及上下文
*   `froca.ts` - 实体缓存
*   组件局部状态
*   用于可共享状态的 URL 参数