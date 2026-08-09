# 移动端前端
<figure class="image image_resized image-style-align-right" style="width:33.52%;"><img style="aspect-ratio:1242/2688;" src="Mobile Frontend_IMG_1765.PNG" width="1242" height="2688"></figure>

Trilium 有一个移动端 Web 前端，针对触屏设备（智能手机和平板电脑）进行了优化。在登录过程中，系统会根据浏览器检测自动激活该前端。

与完整的桌面版相比，移动端前端的功能有所限制。更多详情请参见下文。

## 布局基础

与桌面版不同，移动版的用户界面略有差异，旨在更好地适应手机有限的屏幕尺寸。

以下是桌面版与移动版之间的一些主要差异（非详尽列表）：

*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>以侧边栏形式显示。要显示侧边栏，请按屏幕左上角的按钮。
    
    *   也可以从屏幕左侧进行滑动操作，但浏览器的导航手势在大多数情况下会与其冲突（取决于平台）。
    *   长按笔记以显示<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Quick%20search.md">快速搜索</a>栏也显示在笔记树的顶部。
*   完整的<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>功能可以通过<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>或<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>（如果已配置）触发。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>显示在屏幕底部。
    
    *   启动栏的图标配置与桌面版不同。有关如何配置的更多信息，请参阅专门页面。
*   大多数与笔记相关的操作都集中在笔记右上角的水平点状图标中。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Tabs.md">标签页</a>分组在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>的标签切换器中，标签页以全屏网格形式显示并带有预览，便于切换，同时还提供重新打开已关闭标签页等附加选项。
*   自 v0.100.0 起，<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Split%20View.md">分屏视图</a>也可以在移动视图中使用，但最多同时显示两个窗格。分屏为垂直方向而非水平方向。
*   从 v0.102.0 开始，移动端强制使用<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/New%20Layout.md">新布局</a>。这带来了笔记徽章、笔记类型切换器或集合属性等功能，否则这些功能将不可用。

## 安装为 PWA

移动视图可以设置为 PWA。虽然这不提供任何离线功能，但它会以全屏模式显示应用程序，并便于从手机主屏幕访问。

### 在 iOS 上使用 Safari

1.  打开您的默认 Web 浏览器并访问您的 Trilium 实例。
2.  登录。
3.  按屏幕右下角的 \[…\] 按钮，然后选择“共享”。
4.  向下滚动以显示完整项目列表，然后选择“添加到主屏幕”。
5.  按“添加”，Web 应用即可使用。

### 在 Android 上使用 Google Chrome

> [!IMPORTANT]
> Google Chrome 要求服务器通过 HTTPS 提供服务才能全屏显示。如果使用 HTTP，应用程序将像普通网页一样显示（类似于书签）。

1.  打开您的默认 Web 浏览器并访问您的 Trilium 实例。
2.  登录。
3.  按屏幕右上角的三个垂直点图标，然后选择 _添加到主屏幕_。
4.  选择 _安装_ 选项。
5.  选择合适的名称。
6.  Web 应用将作为应用程序显示，而不是在主屏幕上。

### 在 Android 上使用 Brave

> [!IMPORTANT]
> Brave 要求服务器通过 HTTPS 提供服务才能全屏显示。如果使用 HTTP，应用程序将像普通网页一样显示（类似于书签）。

1.  打开您的默认 Web 浏览器并访问您的 Trilium 实例。
2.  登录。
3.  按屏幕右下角的三个垂直点图标，然后选择 _添加到主屏幕_。
4.  按 _安装_ 选项。
5.  Web 应用将作为应用程序显示，而不是在主屏幕上。

### 在三星浏览器上

1.  打开您的默认 Web 浏览器并访问您的 Trilium 实例。
2.  登录。
3.  按屏幕右下角的汉堡菜单。
4.  选择 _添加到_，然后选择 _主屏幕_。
5.  按 _添加_，Web 应用将出现在主屏幕上。

## 通过桌面应用程序进行测试

如果您在没有专用[服务器安装](Server%20Installation.md)的情况下运行 Trilium，您仍然可以使用桌面应用程序测试移动应用程序。有关更多信息，请参阅<a class="reference-link" href="Desktop%20Installation/Using%20the%20desktop%20application%20as%20a%20server.md">将桌面应用程序用作服务器</a>。要访问它，请转到 `http://<ip>:37840/login?mobile`。

## 强制使用移动端/桌面端前端

Trilium 会自动决定使用移动端还是桌面端前端。如果不符合需求，您可以在**登录**页面上使用 `?mobile` 或 `?desktop` 查询参数（注意：您可能需要先注销）。

或者，只需在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中选择 _切换到移动版/桌面版_。

## 脚本

您可以像使用普通前端一样，通过<a class="reference-link" href="../Scripting.md">脚本</a>来更改行为。要执行脚本笔记，它们需要标记为 `#run=mobileStartup`。

也支持自定义<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>小组件。