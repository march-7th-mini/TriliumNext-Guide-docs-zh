# 活动内容
_活动内容_ 是 Trilium 中强大功能的统称，涵盖从自定义 UI 到可修改笔记甚至修改你 PC 的高级脚本。

## 安全导入

活动内容存在安全问题，尤其是当这些活动内容来自第三方时，例如从网站下载后导入到 Trilium 中。

将 .zip 归档文件[导入](Import%20%26%20Export.md)到 Trilium 时，默认启用_安全模式_，它会尝试阻止不受信任的代码执行。例如，[自定义小组件](../Scripting/Frontend%20Basics/Custom%20Widgets.md)需要 `#widget` [标签](../Advanced%20Usage/Attributes/Labels.md)才能正常工作；安全导入会将该标签重命名为 `#disabled:widget`。

## 安全模式

有时活动内容会导致 UI 或服务器出现问题，使其无法正常运行。<a class="reference-link" href="../Advanced%20Usage/Safe%20mode.md">安全模式</a>允许以启动时不加载活动内容的方式启动 Trilium，从而让用户修复有问题的脚本或小组件。

## 活动内容的类型

以下是 Trilium 中活动内容的类型，以及每种类型的不受信任内容可能造成的一些示例：

| 名称 | 在安全[导入](Import%20%26%20Export.md)时禁用 | 描述 | 不受信任代码的潜在风险 |
| --- | --- | --- | --- |
| [前端脚本](../Scripting/Frontend%20Basics.md) | 是 | 允许在 Trilium 的客户端（UI）上运行任意代码，可以更改用户界面。 | 恶意脚本可以执行服务器端代码、访问未加密的笔记或更改其内容。 |
| <a class="reference-link" href="../Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a> | 是 | 可以为 Trilium 添加新的 UI 功能，例如在<a class="reference-link" href="UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中添加新区域。 | UI 可能被篡改以用于提取敏感信息，或者仅仅导致应用程序崩溃。 |
| <a class="reference-link" href="../Scripting/Backend%20scripts.md">后端脚本</a> | 是 | 可以在 Trilium 的服务器（Node.js 环境）上运行自定义代码，拥有对笔记和数据库的完全访问权限。 | 可以访问所有未加密的笔记，并且由于拥有对数据库的完全访问权限，可以彻底破坏数据。它还可以执行其他应用程序或修改服务器上的文件和文件夹。 |
| <a class="reference-link" href="../Note%20Types/Web%20View.md">Web 视图</a> | 是 | 在笔记中显示网站。 | 可以指向钓鱼网站以收集数据（例如在登录页面上）。 |
| <a class="reference-link" href="../Note%20Types/Render%20Note.md">渲染笔记</a> | 是 | 在笔记中渲染自定义内容，例如仪表板或 Trilium 官方不支持的新编辑器。 | 由于脚本并未完全封装，可能会像前端脚本或自定义小组件一样影响 UI，或者可能像 Web 视图一样收集用户输入的数据。 |
| <a class="reference-link" href="../Theme%20development/Custom%20app-wide%20CSS.md">自定义全局 CSS</a> | 否 | 可以使用 CSS 更改 UI 的布局和样式，无论主题如何都会应用。 | 通常比其他活动内容问题更小，但编写不当的 CSS 可能会影响应用程序的布局，需要使用<a class="reference-link" href="../Advanced%20Usage/Safe%20mode.md">安全模式</a>才能使用应用程序。 |
| [自定义主题](../Theme%20development) | 否 | 可以更改整个 UI 的样式。 | 与自定义全局 CSS 类似。 |
| <a class="reference-link" href="Themes/Icon%20Packs.md">图标包</a> | 否 | 引入可用于笔记的新图标。 | 通常更加受控且不易引发问题，但可能导致性能问题（例如图标包中包含数百万个图标）。 |

## 活动内容徽章

如果笔记被认为包含活动内容，会在<a class="reference-link" href="Notes/Note%20badges.md">笔记徽章</a>区域显示一个徽章。点击该徽章会显示一个菜单，其中包含与该内容类型相关的各种选项，例如打开文档或配置脚本的执行。

对于某些活动内容类型，例如带有自定义触发条件的后端脚本，会出现一个切换按钮。这样可以轻松禁用脚本或小组件，也可以在启用安全模式进行导入后重新启用它们。