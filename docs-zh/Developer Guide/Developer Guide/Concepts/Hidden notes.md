# 隐藏笔记
## 禁止添加子笔记

1.  要在服务器级别强制执行，请前往 `services/notes.ts` 并查找 `getAndValidateParent` 方法。找到 `params.ignoreForbiddenParents` 的 if 语句并在其中添加。
2.  要隐藏笔记树中的加号按钮，请在客户端前往 `widgets/note_tree` 并查找 `enhanceTitle`。查找以 `!["search", "launcher"].includes(note.type)` 开头的 if 语句。
3.  要从上下文菜单中禁用它，请前往 `tree_context_menu` 并查找 `getMenuItems` 方法。在其中找到 `insertNoteAfter` 和 `insertChildNote` 操作，并查看它们的 `enabled` 条件。如果要添加带有大量子笔记的大型笔记类型，请参阅选项与帮助的模式（重命名并扩充 `notOptionsOrHelp` 变量）。