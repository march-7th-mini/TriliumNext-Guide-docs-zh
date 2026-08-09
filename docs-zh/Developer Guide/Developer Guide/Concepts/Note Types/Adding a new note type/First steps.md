# 第一步

> **注意**：在添加或更新步骤标题/顺序时，不要忘记更新 <a class="reference-link" href="Note%20type%20checklist.md">笔记类型清单</a> 中的相应列表。

## 步骤 1. 在服务器中注册笔记类型

前往 `src\services\note_types.ts`，在 `noteTypes` 中添加一个新条目，包含类型 ID 和默认 MIME 类型。

## 步骤 2. 在客户端上下文菜单中注册笔记类型

客户端在 `src\public\app\services\note_types.ts` 中列出可用的笔记类型。

## 步骤 3. 创建类型小组件

前往 `src\public\app\widgets\type_widgets` 目录，创建一个与新笔记类型对应的新文件。

一个空白的实现大致如下：

## 步骤 4. 注册类型小组件

类型小组件需要放入 `src\public\app\widgets\note_detail.ts`，其中有一个 `typeWidgetClasses` 映射，将类型 ID 与上一步创建的类型小组件对应起来。

## 步骤 5. 添加默认图标映射

要为该笔记类型设置默认图标，请前往 `src\public\app\entities\fnote.ts` 并将其添加到 `NOTE_TYPE_ICONS` 中。

## 步骤 6. 添加到笔记类型选择器

前往 `src/public/app/widgets/note_type.ts`，在 `NOTE_TYPES` 中注册新的笔记类型。

## 步骤 7. 将笔记添加到服务器允许的笔记类型中

这是实现导入所必需的，否则它们将被作为纯文本导入。

前往 `src/becca/entities/rows.ts`，将新的笔记类型添加到 `ALLOWED_NOTE_TYPES` 中。

## 其他更改

*   如果小组件需要全高度，则必须在 `src\public\app\widgets\note_detail.ts` 中配置（查找 `checkFullHeight`），然后可以对容器应用 `height: 100%` 样式以使其适配。
*   要使笔记始终全宽（忽略用户的内容宽度），请前往 `note_wrapper` 并查找 `refresh` 方法。其中有一个基于笔记类型的 `full-content-width` 的 `toggleClass`。
*   要允许查看笔记源，请前往 `src/public/app/widgets/buttons/note_actions.ts`，在 `refreshVisibility` 中查找 `this.toggleDisabled(this.$showSourceButton`。

## 最后步骤

*   更新 <a class="reference-link" href="../../Demo%20document.md">演示文档</a> 以展示新的笔记类型。

## 故障排除

### 内容不显示，但在 DOM 中显示为隐藏

类型小组件会在每次选择笔记时进行检查，以确定是否需要根据笔记类型显示该小组件。确保新添加的类型小组件中正确实现了 `getType()`（特别注意返回值，并确保笔记类型 ID 与前面步骤中注册的 ID 匹配）：

```
static getType() { return "foo"; }
```