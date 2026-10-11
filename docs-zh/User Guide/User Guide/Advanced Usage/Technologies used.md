# 使用的技术

Trilium 能够支持多种[笔记类型](../Note%20Types.md)的一个核心方面在于，它利用了各种现成的或可复用的库。

本页面展示了一些所使用的技术，以便更好地理解 Trilium 的工作原理，同时也向这些特定技术的开发者致谢。

## CKEditor

CKEditor 是<a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记背后的编辑器，同时也集成在应用程序的各个方面，例如<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中的属性编辑器，或<a class="reference-link" href="../AI.md">AI</a>侧边栏或笔记中的聊天框。

更多信息请参见<a class="reference-link" href="Technologies%20used/CKEditor.md">CKEditor</a>。

## Excalidraw

[Excalidraw](https://excalidraw.com/) 是<a class="reference-link" href="../Note%20Types/Canvas.md">画布</a>笔记背后的技术。该库的源代码可在 [GitHub](https://github.com/excalidraw/excalidraw) 上获取。

我们使用的是未经修改的版本，因此它与原版存在相同的 [issues](https://github.com/excalidraw/excalidraw/issues)。

## MapLibre GL JS

Trilium v0.105.0 为<a class="reference-link" href="../Collections/Geo%20Map.md">地理地图</a>集合引入了 [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js)，通过使用图形加速（WebGL）带来了性能提升。Trilium 自带自己的轨迹解析逻辑以及大部分 UI，例如右侧面板。

## MindElixir

MindElixir 是我们用于<a class="reference-link" href="../Note%20Types/Mind%20Map.md">思维导图</a>笔记类型的库。主库可在 [GitHub 上以 mind-elixir-core 获取](https://github.com/SSShooter/mind-elixir-core/issues)。

Trilium 自带自己的 UI，涵盖工具栏、上下文菜单、缩放按钮以及点击节点时显示的右侧面板。

## FullCalendar

[FullCalendar](https://fullcalendar.io/) 是<a class="reference-link" href="../Collections/Calendar.md">日历</a>集合背后的技术，提供各种视图（日、周、月、年）和事件管理。Trilium 还自带自己的 UI，形式为编辑时出现的弹出窗口，以及出现在<a class="reference-link" href="../Collections/Collection%20Properties.md">集合属性</a>中的标题栏。

基于 MIT 许可证授权。