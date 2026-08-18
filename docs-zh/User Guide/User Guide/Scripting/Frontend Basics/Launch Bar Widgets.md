# 启动栏小组件

启动栏小组件是<a class="reference-link" href="Custom%20Widgets.md">自定义组件</a>的一个子集，可用于在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中渲染自定义按钮和小组件。

## 为桌面布局创建启动栏小组件

与<a class="reference-link" href="Custom%20Widgets.md">自定义组件</a>不同，设置启动栏小组件的过程略有差异：

1.  创建一个类型为 _JavaScript（前端）_ 或 JSX（用于基于 Preact 的小组件）的代码笔记。
    *   脚本本身使用与<a class="reference-link" href="Custom%20Widgets.md">自定义组件</a>相同的概念，包括使用 `NoteContextAwareWidget` 或 `BasicWidget`（根据需要而定）。
    *   关于旧版和 Preact 格式的示例，请参阅<a class="reference-link" href="Launch%20Bar%20Widgets/Note%20Title%20Widget.md">笔记标题小组件</a>和<a class="reference-link" href="Launch%20Bar%20Widgets/Analog%20Watch.md">模拟手表</a>。
2.  不要设置 `#widget`，因为该属性是为<a class="reference-link" href="Custom%20Widgets.md">自定义组件</a>保留的。
3.  在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中，选择 _配置启动栏_。
4.  在 _可见启动器_ 部分，选择 _添加自定义小组件_。
5.  为新创建的启动器命名（可选）。
6.  在<a class="reference-link" href="../../Advanced%20Usage/Attributes/Promoted%20Attributes.md">提升属性</a>部分，修改 _widget_ 字段以指向新创建的笔记。
7.  [刷新](../../Troubleshooting/Refreshing%20the%20application.md)界面。

## 移动布局

<a class="reference-link" href="../../Installation%20%26%20Setup/Mobile%20Frontend.md">移动前端</a>也支持自定义启动栏小组件。操作步骤如下：

1.  前往<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a> → _高级_ → _显示隐藏子树_。
2.  查找 _移动启动栏_，并按照上一节中的相同创建机制进行操作。