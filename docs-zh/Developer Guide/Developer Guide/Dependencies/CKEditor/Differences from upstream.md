# 与上游版本的差异
*   内嵌了 [`~~isaul32/ckeditor5-math~~`](https://github.com/isaul32/ckeditor5-math) <a class="reference-link" href="ckeditor5-math.md">ckeditor5-math</a>，这是一个用于添加数学支持的第三方插件。CKEditor 本身也有一个带有 MathType 和 ChemType 的[数学插件](https://ckeditor.com/docs/ckeditor5/latest/features/math-equations.html)，但该插件仅限高级版使用。
*   Zadam 在 `findandreplaceUI` 中留下了一个待办事项：`// FIXME: keyboard shortcut doesn't work:` [`https://github.com/ckeditor/ckeditor5/issues/10645`](https://github.com/ckeditor/ckeditor5/issues/10645)
*   `packages\ckeditor5-build-balloon-block\src\mention_customization.js` 引入了通过 `@` 字符插入笔记的功能。

| 受影响的文件 | 受影响的方法 | 变更提交 | 变更原因 |
| --- | --- | --- | --- |
| `packages/ckeditor5-mention/src/mentionui.ts` | `createRegExp()` | `6db05043be24bacf9bd51ea46408232b01a1b232`（已重新添加） | 允许在属性编辑器中触发标签和属性的自动补全。 |
| `init()` | `55a63a1934efb9a520fcc2d69f3ce55ac22aca39` | 允许在按下 ESC 后永久关闭 @-提及功能，否则一旦输入空格，它会自动弹出。 |

## 检查旧仓库

使用以下命令来识别 Zadam 的提交：

```
git log --oneline --author="adam" --all
```

最好在 zadam 的 `trilium-ckeditor5` 分支副本中运行此命令，而不是在 TriliumNext 的副本中运行，因为后者可能不包含所有未合并的分支。

要显示某个提交的过滤后差异：

```
git show d42e772783 -- ':!*yarn.lock' ':!*packages/ckeditor5-build-balloon-block/build/*' ':!*package.json'
```