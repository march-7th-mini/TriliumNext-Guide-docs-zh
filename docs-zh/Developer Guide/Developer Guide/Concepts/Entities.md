# 实体

### 实体系统

Trilium 的数据模型基于五个核心实体：

```
graph TD
    Note[Note<br/>BNote]
    Branch[Branch<br/>BBranch]
    Attribute[Attribute<br/>BAttribute]
    Revision[Revision<br/>BRevision]
    Attachment[Attachment<br/>BAttachment]
    
    Note -->|linked by| Branch
    Note -.->|metadata| Attribute
    Branch -->|creates| Revision
    Note -->|has| Attachment
    
    style Note fill:#e1f5ff
    style Branch fill:#fff4e1
    style Attribute fill:#ffe1f5
    style Revision fill:#f5ffe1
    style Attachment fill:#ffe1e1
```

#### 实体定义

**1\. BNote** (`apps/server/src/becca/entities/bnote.ts`)

*   表示带有标题、内容和元数据的笔记
*   类型可以是：文本、代码、文件、图片、画布、Mermaid 图等
*   通过 blob 引用包含内容
*   可以受保护（加密）
*   具有创建和修改时间戳

**2\. BBranch** (`apps/server/src/becca/entities/bbranch.ts`)

*   表示笔记之间的父子关系
*   支持笔记克隆（多个父节点）
*   包含定位信息
*   具有可选的用于自定义的前缀
*   跟踪树中的展开状态

**3\. BAttribute** (`apps/server/src/becca/entities/battribute.ts`)

*   附加到笔记上的键值对元数据
*   两种类型：标签和关系（链接）
*   可以被子笔记继承
*   用于搜索、组织和脚本编写
*   支持提升属性（突出显示）

**4\. BRevision** (`apps/server/src/becca/entities/brevision.ts`)

*   存储笔记内容的历史版本
*   编辑时自动版本化
*   保留标题、类型和内容
*   支持笔记历史的浏览和恢复

**5\. BAttachment** (`apps/server/src/becca/entities/battachment.ts`)

*   链接到笔记的文件附件
*   具有所有者（笔记）、角色和 MIME 类型
*   内容存储在 blob 中
*   可以受保护（加密）

**6\. BBlob** (`apps/server/src/becca/entities/bblob.ts`)

*   二进制大对象存储
*   存储实际的笔记内容和附件
*   被笔记、修订和附件引用
*   支持对受保护内容进行加密

### 基于小组件的 UI

前端使用**小组件系统**来实现模块化、可复用的 UI 组件。

位置：`apps/client/src/widgets/`

```typescript
// 小组件层级
BasicWidget
├── NoteContextAwareWidget（响应笔记变化）
│   ├── RightPanelWidget（显示在右侧边栏）
│   └── 类型特定的小组件
├── 容器小组件（标签页、功能区等）
└── 专用小组件（搜索、日历等）
```

**基类：**

1.  **BasicWidget** (`basic_widget.ts`)
    *   所有 UI 组件的基类
    *   生命周期：构造 → 渲染 → 事件 → 销毁
    *   处理 DOM 操作
    *   事件订阅管理
    *   子组件管理
2.  **NoteContextAwareWidget** (`note_context_aware_widget.ts`)
    *   继承自 BasicWidget
    *   当活动笔记变化时自动更新
    *   访问当前笔记上下文
    *   用于依赖笔记的 UI
3.  **RightPanelWidget**
    *   显示在右侧边栏中的小组件
    *   可折叠区域
    *   上下文相关的工具和信息

**类型特定的小组件：**

每种笔记类型都有专用的小组件，位于 `apps/client/src/widgets/type_widgets`。