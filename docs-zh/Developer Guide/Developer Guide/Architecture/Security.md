# 安全

Trilium 实现了**纵深防御安全模型**，为用户数据提供多层保护。安全架构涵盖身份验证、授权、加密、输入净化和安全通信。

## 安全原则

1.  **数据隐私**：用户数据在静态存储和传输过程中均受到保护
2.  **加密**：对敏感内容进行逐笔记加密
3.  **身份验证**：支持多种身份验证方法
4.  **授权**：单用户模型，具有细粒度的受保护会话
5.  **输入验证**：所有用户输入均经过净化处理
6.  **安全默认值**：默认启用安全功能
7.  **透明度**：开源允许进行安全审计

## 威胁模型

### 已考虑的威胁

1.  **未授权访问**
    *   对设备的物理访问
    *   网络窃听
    *   凭证被盗
    *   会话劫持
2.  **数据外泄**
    *   恶意脚本
    *   XSS 攻击
    *   SQL 注入
    *   CSRF 攻击
3.  **数据损坏**
    *   恶意修改
    *   数据库篡改
    *   同步冲突
4.  **隐私泄露**
    *   未加密的备份
    *   搜索索引
    *   临时文件
    *   内存转储

### 不在范围内

*   国家级攻击者
*   依赖项中的零日漏洞
*   硬件漏洞（Spectre、Meltdown）
*   具有无限时间的物理访问
*   量子计算攻击

## 身份验证

### 密码身份验证

**实现位置：** `apps/server/src/services/password.ts`

### TOTP（双因素身份验证）

**实现位置：** `apps/server/src/routes/api/login.ts`

### OpenID Connect

**实现位置：** `apps/server/src/routes/api/login.ts`

**支持的提供商：**

*   任何兼容 OpenID Connect 的提供商
*   Google、GitHub、Auth0 等

**流程：**

```typescript
// 1. 重定向到提供商
GET /api/login/openid

// 2. 提供商携带代码重定向回来
GET /api/login/openid/callback?code=...

// 3. 用代码交换令牌
const tokens = await openidClient.callback(redirectUri, req.query)

// 4. 验证 ID 令牌
const claims = tokens.claims()

// 5. 创建会话
req.session.loggedIn = true
```

### 会话管理

**会话存储：** SQLite 数据库（sessions 表）

**会话配置：**

```typescript
app.use(session({
    secret: sessionSecret,
    resave: false,
    saveUninitialized: false,
    rolling: true,
    cookie: {
        maxAge: 7 * 24 * 60 * 60 * 1000,  // 7 天
        httpOnly: true,
        secure: isHttps,
        sameSite: 'lax'
    },
    store: new SqliteStore({
        db: db,
        table: 'sessions'
    })
}))
```

**会话失效：**

*   不活动后自动超时
*   手动注销清除会话
*   服务器重启使所有会话失效（可选）

## 授权

### 单用户模型

**桌面：**

*   单用户（设备所有者）
*   不支持多用户
*   对所有笔记具有完全访问权限

**服务器：**

*   每次安装单用户
*   所有操作均需身份验证
*   无用户角色或权限

### 受保护会话

**目的：** 临时访问加密（受保护的）笔记

**实现位置：** `apps/server/src/services/protected_session.ts`

**工作流程：**

```typescript
// 1. 用户输入受保护笔记的密码
POST /api/protected-session/enter
Body: { password: "protected-password" }

// 2. 派生加密密钥
const protectedDataKey = deriveKey(password)

// 3. 验证密码（解密已知的加密值）
const decrypted = decrypt(testValue, protectedDataKey)
if (decrypted === expectedValue) {
    // 4. 存储在内存中（不在会话中）
    protectedSessionHolder.setProtectedDataKey(protectedDataKey)
    
    // 5. 设置超时
    setTimeout(() => {
        protectedSessionHolder.clearProtectedDataKey()
    }, timeout)
}
```

**受保护会话超时：**

*   默认：10 分钟（可配置）
*   活动时延长
*   浏览器关闭时清除
*   与主会话分离

### API 授权

**内部 API：**

*   需要经过身份验证的会话
*   CSRF 令牌验证
*   同源策略

**ETAPI（外部 API）：**

*   基于令牌的身份验证
*   无需会话
*   速率限制

## 加密

### 笔记加密

**加密算法：** AES-256-CBC

**密钥层级：**

```
用户密码
    ↓ (scrypt)
数据密钥（用于受保护的笔记）
    ↓ (AES-128)
受保护的笔记内容
```

**受保护笔记的元数据：**

*   内容已加密
*   类型和 MIME 未加密
*   属性未加密

### 数据密钥管理

**密钥轮换：**

*   目前不支持
*   需要重新加密所有受保护的笔记

### 传输加密

**HTTPS：**

*   推荐用于服务器安装
*   仅 TLS 1.2+
*   优先使用强密码套件
*   启用证书验证

**桌面：**

*   本地通信（无网络）
*   无需 HTTPS

### 备份加密

**数据库备份：**

*   受保护的笔记在备份中保持加密状态
*   备份文件应单独保护
*   考虑加密备份存储位置

## 输入净化

### XSS 防护

*   **HTML 净化**
*   **CKEditor 配置：**
    
    ```
    // apps/client/src/widgets/type_widgets/text_type_widget.ts
    ClassicEditor.create(element, {
        // 限制允许的内容
        htmlSupport: {
            allow: [
                { name: /./, attributes: true, classes: true, styles: true }
            ],
            disallow: [
                { name: 'script' },
                { name: 'iframe', attributes: /^(?!src$).*/ }
            ]
        }
    })
    ```
*   内容安全策略

### SQL 注入防护

**参数化查询：**

```typescript
const notes = sql.getRows(
    'SELECT * FROM notes WHERE title = ?',
    [userInput]
)
```

**ORM 使用：**

```typescript
// 基于实体的访问防止 SQL 注入
const note = becca.getNote(noteId)
note.title = userInput  // 由实体净化
note.save()  // 参数化查询
```

### CSRF 防护

**CSRF 令牌验证：**

位置：`apps/server/src/routes/csrf_protection.ts`

使用[双重提交 Cookie 模式](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#double-submit-cookie)通过 [`csrf-csrf`](https://github.com/Psifi-Solutions/csrf-csrf) 实现无状态 CSRF 防护。

### 文件上传验证

**验证：**

```typescript
// 验证文件大小
const maxSize = 100 * 1024 * 1024  // 100 MB
if (file.size > maxSize) {
    throw new Error('文件太大')
}
```

## 网络安全

### HTTPS 配置

**证书验证：**

*   生产环境要求有效证书
*   开发环境允许自签名证书
*   未实现证书固定

### 速率限制

**登录速率限制：**

```typescript
const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 10,  // 10 次失败尝试
    skipSuccessfulRequests: true
})

app.post('/api/login/password', loginLimiter, loginHandler)
```

## 数据安全

### 安全数据删除

**软删除：**

```typescript
// 标记为已删除（先同步）
note.isDeleted = 1
note.deleteId = generateUUID()
note.save()

// 实体变更被跟踪用于同步
addEntityChange('notes', noteId, note)
```

**硬删除（擦除）：**

```typescript
// 同步完成后
sql.execute('DELETE FROM notes WHERE noteId = ?', [noteId])
sql.execute('DELETE FROM branches WHERE noteId = ?', [noteId])
sql.execute('DELETE FROM attributes WHERE noteId = ?', [noteId])

// 将实体变更标记为已擦除
sql.execute('UPDATE entity_changes SET isErased = 1 WHERE entityId = ?', [noteId])
```

**Blob 清理：**

```typescript
// 查找孤立 Blob（未被任何笔记/修订/附件引用）
const orphanedBlobs = sql.getRows(`
    SELECT blobId FROM blobs
    WHERE blobId NOT IN (SELECT blobId FROM notes WHERE blobId IS NOT NULL)
      AND blobId NOT IN (SELECT blobId FROM revisions WHERE blobId IS NOT NULL)
      AND blobId NOT IN (SELECT blobId FROM attachments WHERE blobId IS NOT NULL)
`)

// 删除孤立 Blob
for (const blob of orphanedBlobs) {
    sql.execute('DELETE FROM blobs WHERE blobId = ?', [blob.blobId])
}
```

### 内存安全

**内存中的受保护数据：**

*   受保护的数据密钥仅存储在内存中
*   超时后清除
*   不写入磁盘
*   不存储在会话存储中

## 依赖安全

### 漏洞扫描

**工具：**

*   Renovate bot - 自动依赖更新
*   `pnpm audit` - 检查已知漏洞
*   GitHub Dependabot 警报

**流程：**

```
# 检查漏洞
npm audit

# 自动修复
npm audit fix

# 手动审查破坏性变更
npm audit fix --force
```

### 依赖固定

**package.json：**

```
{
  "dependencies": {
    "express": "4.18.2",  // 精确版本
    "better-sqlite3": "^9.2.2"  // 兼容版本
  }
}
```

**pnpm 覆盖：**

```
{
  "pnpm": {
    "overrides": {
      "lodash@<4.17.21": ">=4.17.21",  // 强制最低版本
      "axios@<0.21.2": ">=0.21.2"
    }
  }
}
```

### 补丁管理

**pnpm 补丁：**

```
# 创建补丁
pnpm patch @ckeditor/ckeditor5

# 在临时目录中编辑文件
# ...

# 生成补丁文件
pnpm patch-commit /tmp/ckeditor5-patch

# 安装时自动应用补丁
```

## 安全审计

### 日志

**记录的安全事件：**

*   登录尝试（成功/失败）
*   受保护会话访问
*   密码更改
*   ETAPI 令牌使用
*   失败的 CSRF 验证

**日志位置：**

*   桌面：控制台输出
*   服务器：日志文件或标准输出

### 监控

**需要监控的指标：**

*   失败的登录尝试
*   API 错误率
*   异常的数据库更改
*   大型导出/导入