# 前端基础

前端脚本是在客户端（浏览器环境）中运行的自定义 JavaScript 笔记。

前端脚本有四种类型：

|  |  |
| --- | --- |
| 常规脚本 | 这些脚本在当前应用和笔记上下文中运行。可以手动运行，也可以在启动时自动运行。 |
| <a class="reference-link" href="Frontend%20Basics/Custom%20Widgets.md">自定义组件</a> | 这些可以在各种位置引入新的 UI 元素，例如在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>附近、内容区域，甚至<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中。 |
| <a class="reference-link" href="Frontend%20Basics/Launch%20Bar%20Widgets.md">启动栏组件</a> | 与<a class="reference-link" href="Frontend%20Basics/Custom%20Widgets.md">自定义组件</a>类似，但专用于<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>。这些可以简单地引入新按钮或图形元素到启动栏中。 |
| <a class="reference-link" href="../Note%20Types/Render%20Note.md">渲染笔记</a> | 这允许使用 HTML 或 Preact JSX 在笔记内渲染自定义内容。 |

对于不需要用户界面的更高级行为（例如批量修改笔记），请参阅<a class="reference-link" href="Backend%20scripts.md">后端脚本</a>。

## 脚本

脚本没有特殊要求。可以使用代码笔记上的 _执行_ 按钮手动运行，也可以自动运行，请参阅<a class="reference-link" href="Frontend%20Basics/Frontend%20Events.md">事件</a>。

## 组件

组件需要特定的格式，Trilium 才能将它们集成到 UI 中。

*   对于旧版组件，脚本笔记必须导出 `BasicWidget` 或其派生类（请参阅<a class="reference-link" href="Frontend%20Basics/Custom%20Widgets/Note%20context%20aware%20widget.md">笔记上下文感知组件</a>或<a class="reference-link" href="Frontend%20Basics/Custom%20Widgets/Right%20pane%20widget.md">右侧面板组件</a>）。
*   对于 Preact 组件，需要使用名为 `defineWidget` 的内置辅助函数。

更多信息，请参阅<a class="reference-link" href="Frontend%20Basics/Custom%20Widgets.md">自定义组件</a>。

## 脚本 API

Trilium 的前端 API 可作为全局变量 `api` 提供给所有在前端上下文中运行的脚本。有关 API 的参考，请参阅<a class="reference-link" href="Script%20API/Frontend%20API">前端 API</a>。

### 教程

有关构建组件的更多信息，请查看 [组件基础](Frontend%20Basics/Custom%20Widgets/Widget%20Basics.md)。