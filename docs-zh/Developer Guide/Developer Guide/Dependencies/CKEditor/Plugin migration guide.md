# 插件迁移指南

本指南将引导您完成将 CKEditor 5 插件集成到 Trilium monorepo 中的基本步骤，这样可以：

*   无需维护新仓库即可对实现进行修改。
*   将基于旧版安装方法的旧插件集成，使其与新方法良好兼容。

> [!IMPORTANT]
> 本指南假定 CKEditor 插件是使用 TypeScript 编写的。如果不是，您需要将其移植到 TypeScript 以匹配 monorepo 的其余部分。

## 步骤 1：创建项目骨架

首先，我们将从头开始生成一个项目，以便它采用最新的 CKEditor 插件构建模板，而被集成的插件可能基于旧版方法。

在 `Notes` 仓库之外，我们将使用 CKEditor 生成器为我们生成新的项目结构。我们没有直接在 `Notes` 仓库内进行操作，因为它会使用不同的包管理器（Yarn/NPM 与 `pnpm`），并且它还会创建自己的 Git 仓库。

```
npx ckeditor5-package-generator @triliumnext/ckeditor5-foo --use-npm --lang ts --installation-methods current
```

当然，请将 `foo` 替换为插件的名称。通常最好保留插件的原始名称，可以通过查看文件名的前缀来确定（例如，`mermaidui` 或 `mermaidediting` 中的 `mermaid`）。

## 步骤 2：复制新项目

1.  进入新创建的 `ckeditor5-foo` 目录。
2.  删除 `node_modules`，因为我们将使用 `pnpm` 来管理它。
3.  从中删除 `.git`。
4.  将该文件夹复制到 `Notes` 仓库中，作为 `packages` 的子目录。

## 步骤 3：更新依赖项

在刚复制的包中，进入 `package.json` 并进行编辑：

1.  在 `devDependencies` 中，将 `ckeditor5` 从 `latest` 改为与 `packages/ckeditor5/package.json` 中描述的版本相同的版本（固定版本，例如 `43.2.0`）。
2.  在 `peerDependencies` 中，将 `ckeditor5` 改为与上一步相同的版本。
3.  同样，更新 `vitest` 依赖项以匹配 monorepo 中的版本。
4.  从 `scripts` 部分删除 `prepare` 条目。
5.  将 `build:dist` 改为简单的 `build`。
6.  在 `tsconfig.dist.json` 中，将 `typings/types` 改为 `../typings/types.d.ts` 以兼容最新的 TypeScript 版本。

## 步骤 4：安装缺失的依赖项并解决构建错误

在 `Notes` 根目录运行 `pnpm build-dist`，然后：

1.  如果出现关于 `Invalid module name in augmentation, module '@ckeditor/ckeditor5-core' cannot be found.` 的错误，只需将 `@ckeditor/ckeditor5-core` 替换为 `ckeditor5`。
2.  再次运行构建命令，确保没有构建错误。
3.  提交更改。

## 步骤 5：使用 `git subtree` 拉取原始仓库

我们不是从现有插件复制文件，而是为了可追溯性而继承其历史记录。为此，我们将在仓库内使用一个临时目录：

```
git subtree add --prefix=_regroup/<name> https://[...]/repo.git <main_branch>
```

这将把上游仓库中来自指定分支的所有提交引入，并将它们重写到所需目录下。

## 步骤 6：集成插件

1.  首先复制每个子插件（除了主要的插件，如 `FooEditing` 和 `FooUI`）。
    1.  如果它们是用 JavaScript 编写的，请将它们移植到 TypeScript。
        1.  删除任何非 TypeScript 的类型文档。
    2.  如果它们对 CKEditor 有非标准导入，例如 `'ckeditor5/src/core.js'`，请将它们重写为简单的 `ckeditor`。
2.  安装源代码使用的任何必要依赖项（尝试根据编译错误来判断，而不是简单地从 `package.json` 中复制所有依赖项）。
3.  保留自动生成的现有 TypeScript 文件，并将更改集成到其中。
4.  在插件的 `tsconfig.json` 中，将 `compilerOptions.composite` 设置为 `true`。
5.  在 `packages/ckeditor5/package.json` 中为新插件添加工作区依赖项。
6.  在 `packages/ckeditor5` 中查找 `plugins.ts`，并在 `EXTERNAL_PLUGINS` 中导入顶层插件。

## 处理 CSS

有些插件有自定义 CSS，有些则没有。

1.  在插件的 `index.ts` 中 `import` CSS。
2.  构建插件时，`dist/index.css` 将被更新。
3.  在 `packages/ckeditor5` 的 `plugins.ts` 中，添加对 CSS 的导入。

## 从另一个 monorepo 集成

如果上游插件属于另一个项目的 monorepo（类似于 `trilium-ckeditor5` 曾经的情况），这是一个更复杂的用例。

1.  克隆上游 monorepo 的全新副本以获取插件。
2.  运行 `git filter-repo --path packages/ckeditor5-foo/`（末尾的斜杠非常重要！）。
3.  像前面的步骤一样运行 `git subtree add`，但指向本地 Git 目录（通过在仓库的绝对路径后附加 `/.git`）。
4.  按照正常的集成步骤进行操作。