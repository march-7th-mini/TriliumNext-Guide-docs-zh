# 数据库

Trilium 使用 **SQLite**（通过 `better-sqlite3`）作为其嵌入式数据库引擎，提供可靠的、基于文件的存储系统，无需单独的数据库服务器。数据库存储所有笔记、它们之间的关系、元数据和配置。

模式位置：`apps/server/src/assets/db/schema.sql`

### 数据访问模式

**直接 SQL：**

```typescript
// apps/server/src/services/sql.ts
sql.getRows("SELECT * FROM notes WHERE type = ?", ['text'])
sql.execute("UPDATE notes SET title = ? WHERE noteId = ?", [title, noteId])
```

**通过 Becca：**

```typescript
// 推荐方法 - 使用缓存
const note = becca.getNote('noteId')
note.title = 'New Title'
note.save()
```

**通过 Froca（前端）：**

```typescript
// 只读访问
const note = froca.getNote('noteId')
console.log(note.title)
```

### 数据库迁移

*   迁移系统位于 `server/src/migrations/migrations.ts`（实际定义）和 `src/services/migration.ts` 中。
*   同时支持 SQLite 和 TypeScript 迁移。
    *   小型迁移直接包含在 `src/migrations/migrations.ts` 中。
    *   较大的 TypeScript 迁移按顺序编号（例如，`XXXX_migration_name.ts`），并由 `migrations.ts` 动态导入。
*   版本升级时自动执行。
*   模式版本记录在选项表中。