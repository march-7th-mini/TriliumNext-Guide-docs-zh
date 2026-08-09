# 后端

### 应用程序入口点

位置：`apps/server/src/main.ts`

**启动顺序：**

1.  加载配置
2.  初始化数据库
3.  运行迁移
4.  加载 Becca 缓存
5.  启动 Express 服务器
6.  初始化 WebSocket
7.  启动定时任务

### 服务层

位于：`apps/server/src/services/`

**核心服务：**

*   **笔记管理**
    *   `notes.ts` - 增删改查操作
    *   `note_contents.ts` - 内容处理
    *   `note_types.ts` - 类型特定逻辑
    *   `cloning.ts` - 笔记克隆/多父级
*   **树操作**
    *   `tree.ts` - 树结构管理
    *   `branches.ts` - 分支操作
    *   `consistency_checks.ts` - 树完整性
*   **搜索**
    *   `search/search.ts` - 主搜索引擎
    *   `search/expressions/` - 搜索表达式解析
    *   `search/services/` - 搜索工具
*   **同步**
    *   `sync.ts` - 同步协议
    *   `sync_update.ts` - 更新处理
    *   `sync_mutex.ts` - 并发控制
*   **脚本**
    *   `backend_script_api.ts` - 后端脚本 API
    *   `script_context.ts` - 脚本执行上下文
*   **导入/导出**
    *   `import/` - 各种导入格式
    *   `export/` - 导出为不同格式
    *   `zip.ts` - 归档处理
*   **安全**
    *   `encryption.ts` - 笔记加密
    *   `protected_session.ts` - 会话管理
    *   `password.ts` - 密码处理

### 路由结构

位于：`apps/server/src/routes/`

```
routes/
├── index.ts              # 路由注册
├── api/                  # REST API 端点
│   ├── notes.ts
│   ├── branches.ts
│   ├── attributes.ts
│   ├── search.ts
│   ├── login.ts
│   └── ...
└── custom/               # 特殊端点
    ├── setup.ts
    ├── share.ts
    └── ...
```

**API 端点模式：**

```typescript
router.get('/api/notes/:noteId', (req, res) => {
    const noteId = req.params.noteId
    const note = becca.getNote(noteId)
    res.json(note.getPojoWithContent())
})
```

### 中间件

关键中间件组件：

*   `auth.ts` - 身份验证
*   `csrf.ts` - CSRF 保护
*   `request_context.ts` - 请求作用域数据
*   `error_handling.ts` - 错误响应