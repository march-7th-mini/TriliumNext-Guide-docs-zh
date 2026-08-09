# 架构

Trilium Notes 是一个基于 TypeScript monorepo 构建的层级化笔记应用。它支持多种部署模式（桌面端、服务器端、移动端 Web），并具备同步、脚本、加密和富文本编辑等高级功能。

### 主要特性

*   **Monorepo 架构**：使用 pnpm workspaces 进行依赖管理
*   **多平台**：桌面端（Electron）、服务器端（Node.js/Express）和移动端 Web
*   **TypeScript 优先**：整个代码库具有强类型
*   **基于插件**：为笔记类型和 UI 组件提供可扩展架构
*   **离线优先**：无网络连接时功能完整可用
*   **支持同步**：内置同步协议，支持多设备使用

### 技术栈

*   **运行时**：Node.js（后端），浏览器/Electron（前端）
*   **语言**：TypeScript，JavaScript
*   **数据库**：SQLite (better-sqlite3)
*   **构建工具**：
    *   客户端：Vite，
    *   服务器端：ESBuild（打包）
    *   包管理器：pnpm
*   **UI 框架**：基于自定义小组件的系统（原生 HTML、CSS 和 JavaScript + jQuery），正在向 React/Preact 转换。
*   **富文本**：CKEditor 5（定制版）
*   **代码编辑**：CodeMirror 6
*   **桌面端**：Electron
*   **服务器端**：Express.js

## 主要架构

Trilium 即使在桌面模式下也遵循**客户端-服务器架构**，其中 Electron 在同一进程中同时运行后端服务器和前端客户端。

```
graph TB
    subgraph Frontend
        Widgets[Widgets<br/>System]
        Froca[Froca<br/>Cache]
        UIServices[UI<br/>Services]
    end
    
    subgraph Backend["Backend Server"]
        Express[Express<br/>Routes]
        Becca[Becca<br/>Cache]
        ScriptEngine[Script<br/>Engine]
        Database[(SQLite<br/>Database)]
    end
    
    Widgets -.-> API[WebSocket & REST API]
    Froca -.-> API
    UIServices -.-> API
    API -.-> Express
    API -.-> Becca
    API -.-> ScriptEngine
    Becca --> Database
    Express --> Database
    ScriptEngine --> Database
```

### 部署模式

1.  **桌面应用**
    *   Electron 封装，同时运行前端和后端
    *   本地 SQLite 数据库
    *   完整的离线功能
    *   跨平台（Windows、macOS、Linux）
2.  **服务器安装**
    *   提供 Web 界面的 Node.js 服务器
    *   支持多用户
    *   可与桌面客户端同步
    *   支持 Docker 部署
3.  **移动端 Web**
    *   优化的响应式界面
    *   通过浏览器访问
    *   需要服务器安装

## Monorepo 结构

Trilium 使用 **pnpm workspaces** 管理其 monorepo 结构，应用和包清晰分离。

```
trilium/
├── apps/                    # 可运行的应用程序
│   ├── client/             # 前端应用（服务器和桌面端共用）
│   ├── server/             # 带 Web 界面的 Node.js 服务器
│   ├── desktop/            # Electron 桌面应用
│   ├── web-clipper/        # 用于捕获网页内容的浏览器扩展
│   ├── db-compare/         # 数据库比较工具
│   ├── dump-db/            # 数据库导出工具
│   ├── edit-docs/          # 文档编辑工具
│   ├── build-docs/         # 文档构建工具
│   └── website/            # 营销网站
│
├── packages/               # 共享库
│   ├── commons/           # 共享接口和工具
│   ├── ckeditor5/         # 自定义富文本编辑器
│   ├── codemirror/        # 代码编辑器定制
│   ├── highlightjs/       # 语法高亮
│   ├── share-theme/              # 共享笔记主题
│   ├── splitjs/                  # 分栏库
│   └── turndown-plugin-gfm/      # Markdown 转换
│
├── docs/                   # 文档
├── scripts/                # 构建和工具脚本
└── patches/                # 包补丁（通过 pnpm）
```

### 包依赖关系

Monorepo 使用 workspace 协议（`workspace:*`）进行内部依赖管理：

```
desktop → client → commons
server  → client → commons
client  → ckeditor5, codemirror, highlightjs
ckeditor5 → its in-tree plugins (src/plugins/)
```

## 安全摘要

### 加密系统

**逐笔记加密：**

*   笔记可以单独保护
*   加密笔记使用 AES-128-CBC 加密。
*   单独的保护会话管理

**保护会话：**

*   对受保护笔记的限时访问
*   自动超时
*   需要重新身份验证
*   前端：`protected_session.ts`
*   后端：`protected_session.ts`

### 身份验证

**密码认证：**

*   PBKDF2 密钥派生
*   每次安装使用独立盐值
*   哈希验证

**OpenID Connect：**

*   支持外部身份提供商
*   OAuth 2.0 流程
*   可配置的提供商

**TOTP（双因素认证）：**

*   基于时间的一次性密码
*   二维码设置
*   备份代码

### 授权

**单用户模型：**

*   桌面端：单用户（所有者）
*   服务器端：每次安装单用户

**分享笔记：**

*   无需身份验证的公共访问
*   独立的 Shaca 缓存
*   只读访问

### CSRF 防护

**CSRF 令牌：**

*   状态变更操作必需
*   令牌位于请求头或 Cookie 中
*   验证中间件

### 输入净化

**XSS 防护：**

*   使用 DOMPurify 进行 HTML 净化
*   CKEditor 内容过滤
*   CSP 请求头

**SQL 注入防护：**

*   仅使用参数化查询
*   Better-sqlite3 预处理语句
*   SQL 中不使用字符串拼接

### 依赖安全

**漏洞扫描：**

*   使用 Renovate bot 进行更新
*   集成 npm audit
*   覆盖有漏洞的子依赖