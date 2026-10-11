# 移动端前端
<figure class="image image-style-align-right image_resized" style="width:33.52%;"><img style="aspect-ratio:1242/2688;" src="Mobile Frontend_IMG_1765.PNG" width="1242" height="2688"></figure>

Trilium 有一个移动端 Web 前端，专为触屏设备（智能手机和平板电脑）进行了优化。它会在登录过程中根据浏览器检测自动激活。

与完整的桌面版相比，移动端前端的功能较为有限。详情请参阅下文。

## 布局基础

与桌面版不同，移动版的 UI 略有不同，旨在更好地适应手机有限的屏幕空间。

以下是桌面版与移动版之间差异的非详尽列表：

*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>以侧边栏形式显示。要显示侧边栏，请按屏幕左上角的按钮。
    *   也可以从屏幕左侧执行滑动手势，但大多数情况下浏览器的导航手势会干扰它（取决于平台）。
    *   长按笔记可显示<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Quick%20search.md">快速搜索</a>栏也显示在笔记树的顶部。
*   完整的<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>功能可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>或<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>（如果已配置）中触发。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>显示在屏幕底部。
    *   启动栏使用的图标配置与桌面版不同。有关如何配置的更多信息，请参阅专门页面。
*   大多数与笔记相关的操作都集中在笔记右上角的水平圆点图标中。
*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Tabs.md">标签页</a>归组在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>中的标签页切换器下，标签页以全屏网格形式显示并带有预览，便于切换，还提供重新打开已关闭标签页等附加选项。
*   自 v0.100.0 起，<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Split%20View.md">分屏视图</a>也可在移动视图中使用，但最多同时显示两个窗格。分屏以垂直方向而非水平方向显示。

## 安装为 PWA

移动视图可以设置为 PWA。虽然这不提供任何离线功能，但它会以全屏方式显示应用程序，并便于通过手机主屏幕访问。

=== "<span class="tn-icon bx bxl-apple"></span> iOS 使用 Safari"

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的 \[…\] 按钮并选择分享。
    4.  向下滚动以显示完整项目列表，然后选择 _添加到主屏幕_。
    5.  按 _添加_，该 Web 应用即可使用。

=== "<span class="tn-icon bx bxl-chrome"></span> Android 使用 Google Chrome"

    > [!IMPORTANT]
    > Google Chrome 要求服务器通过 HTTPS 提供服务才能以全屏显示。如果使用 HTTP，应用将像普通网页一样显示（类似于书签）。

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右上角的三个垂直圆点图标，然后选择 _添加到主屏幕_。
    4.  选择 _安装_ 选项。
    5.  选择一个合适的名称。
    6.  该 Web 应用将作为应用程序出现，而不是在主屏幕上。

=== "Android 使用 Brave"

    > [!IMPORTANT]
    > Brave 要求服务器通过 HTTPS 提供服务才能以全屏显示。如果使用 HTTP，应用将像普通网页一样显示（类似于书签）。

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的三个垂直圆点图标，然后选择 _添加到主屏幕_。
    4.  按 _安装_ 选项。
    5.  该 Web 应用将作为应用程序出现，而不是在主屏幕上。

=== "Samsung Browser"

    1.  打开默认 Web 浏览器并访问你的 Trilium 实例。
    2.  登录。
    3.  按屏幕右下角的汉堡菜单。
    4.  选择 _添加到_，然后选择 _主屏幕_。
    5.  按 _添加_，该 Web 应用将出现在主页上。

## 通过桌面应用程序进行测试

如果你在没有专门的[服务器安装](Server%20Installation.md)的情况下运行 Trilium，你仍然可以使用桌面应用程序测试移动端应用。更多信息请参阅<a class="reference-link" href="Desktop%20Installation/Using%20the%20desktop%20application%20as%20a%20server.md">将桌面应用程序用作服务器</a>。要访问它，请前往 `http://<ip>:37840/login?mobile` 。

## 强制使用移动端/桌面端前端

Trilium 会自动决定使用移动端还是桌面端前端。如果这不合适，你可以在**登录**页面使用 `?mobile` 或 `?desktop` 查询参数（注意：你可能需要先登出）。

或者，只需在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Global%20menu.md">全局菜单</a>中选择 _切换到移动版/桌面版_。

## 脚本

你可以像普通前端一样使用<a class="reference-link" href="../Scripting.md">脚本</a>来改变行为。要使脚本笔记被执行，它们需要标记为 `#run=mobileStartup`。

也支持自定义<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Launch%20Bar.md">启动栏</a>小组件。