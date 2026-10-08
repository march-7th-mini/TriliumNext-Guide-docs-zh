# 参考
## 检测移动端与桌面端

移动端布局与桌面端不同。使用 `body.mobile` 和 `body.desktop` 来区分它们。

```css
body.mobile #root-widget {
	/* Do something on mobile */
}

body.desktop #root-widget {
	/* Do something on desktop */
}
```

请注意，移动端布局中还有一种“平板模式”。对于这种特殊情况，需要使用媒体查询：

```css
@media (max-width: 991px) {

    #launcher-pane {

        /* Do something on mobile layout */

    }

}



@media (min-width: 992px) {

    #launcher-pane {

        /* Do something on mobile tablet + desktop layout */

    }

}
```

## 检测水平与垂直布局

用户可以在垂直布局（经典布局，启动器栏位于左侧）和水平布局（启动器栏位于顶部，标签页为全宽）之间进行选择。

可以通过在 `body` 层级使用类来应用不同的样式：

```
body.layout-vertical #left-pane {
	/* Do something */
}

body.layout-horizontal #center-pane {
	/* Do something else */	
}
```

这两种不同的布局使用不同的容器（但无论用户如何选择，它们都存在于 DOM 中），例如可以使用 `#horizontal-main-container` 和 `#vertical-main-container` 来自定义内容区域的背景。

## 检测平台（Windows、macOS）或 Electron

可以通过使用 `body` 中的类来添加仅适用于特定平台的样式：

| Windows | macOS |
| --- | --- |
| `<br>body.platform-win32 {<br> background: red;<br>}<br>` | `<br>body.platform-darwin {<br> background: red;<br>}<br>` |

也可以仅在 Electron（桌面应用程序）下运行时应用样式：

```
body.electron {
	background: blue;
}
```

### 原生标题栏

可以通过查询 `body` 来检测用户选择的是原生标题栏还是自定义标题栏：

```
body.electron.native-titlebar {
	/* Do something */
}

body.electron:not(.native-titlebar) {
	/* Do something else */
}
```

### 原生窗口按钮

在 Electron 下运行且关闭原生标题栏时，引入了一项功能，可以使用平台特定的窗口按钮，例如 macOS 上的红绿灯按钮。

有关此功能的原始实现（包括截图），请参阅 [Native title bar buttons by eliandoran · Pull Request #702 · TriliumNext/Notes](https://github.com/TriliumNext/Notes/pull/702)。

#### 在 Windows 上

原生窗口按钮区域的颜色可以使用 RGB 十六进制颜色进行调整：

```
body {
	--native-titlebar-foreground: #ffffff;
	--native-titlebar-background: #ff0000;
}
```

也可以使用 RGBA 十六进制颜色来实现透明效果，但代价是悬停颜色会减弱：

```
body {
	--native-titlebar-background: #ff0000aa;
}
```

请注意，该值在窗口初始化时读取，之后仅在用户更改其浅色/深色模式偏好时才会刷新。

#### 在 macOS 上

在 macOS 上，当原生标题栏被禁用时，红绿灯窗口按钮默认启用。按钮的偏移量可以使用以下方式调整：

```css
body {
    --native-titlebar-darwin-x-offset: 12;
    --native-titlebar-darwin-y-offset: 14 !important;
}
```

### Windows 上的背景/透明效果（Mica）

Windows 11 提供了一种名为 Mica 的特殊背景/透明效果，主题可以通过在 `body` 层级设置 `--background-material` 变量来启用它：

```css
body.electron.platform-win32 {
	--background-material: tabbed; 
}
```

该值可以是 `tabbed`（对水平布局特别有用）或 `mica`（非常适合垂直布局）。

请注意，Mica 效果应用于 `body` 层级，主题需要使整个层级结构（半）透明才能使其可见。可以参考 TrilumNext 主题作为灵感。

## 笔记图标、标签页工作区强调色

主题能力是通过 CSS 变量进行的小调整，可以影响应用程序的布局或视觉外观。

在标签栏中，显示笔记的图标而不是工作区的图标：

```css
:root {
	--tab-note-icons: true;
}
```

当某个标签页的工作区被提升时，可以获取该工作区的背景颜色，例如在标签页上应用一个小条而不是整个背景颜色：

```css
.note-tab .note-tab-wrapper {
    --tab-background-color: initial !important;
}

.note-tab .note-tab-wrapper::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background-color: var(--workspace-tab-background-color);
}
```

## 自定义字体

使用自定义字体的推荐方式是直接在 Trilium 中导入字体。有关如何操作的信息，请参阅 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Personalizing%20the%20font.md">个性化字体</a>。

或者，对于提供自己字体的主题，可以使用[自定义资源提供程序](../Advanced%20Usage/Custom%20Resource%20Providers.md)：将字体导入 Trilium 并为其分配 `#customResourceProvider=fonts/myfont.ttf`，然后通过 `/custom/fonts/myfont.ttf` 在 CSS 中导入字体。如果你的 Trilium 服务器运行在 `/` 以外的路径上，请使用 `../../../custom/fonts/myfont.ttf`。

## 深色和浅色主题

浅色主题需要具有以下 CSS：

```css
:root {
	--theme-style: light;
}
```

如果主题是深色的，那么 `--theme-style` 需要为 `dark`。

如果主题是自动的（例如根据 `prefers-color-scheme` 同时支持浅色或深色），则还必须声明（除了将 `--theme-style` 设置为 `light` 或 `dark` 之外）：

```css
:root {

    --theme-style-auto: true;

}
```

这将通过向操作系统告知颜色偏好来影响 Electron 应用程序的行为（例如，背景效果在 Windows 上会正确显示）。

## 自适应文本和表格颜色

在文本笔记中应用的颜色，来自字体颜色和背景颜色按钮（参见 <a class="reference-link" href="../Note%20Types/Text/General%20formatting.md">通用格式</a>）或来自表格和单元格属性（参见 <a class="reference-link" href="../Note%20Types/Text/Tables.md">表格</a>），会以适合主题的色调显示：色相保持不变，而亮度和饱和度则被限制在一定范围内。主题可以更改这些限制，例如，如果其页面背景比内置主题的页面背景暗得多或亮得多：

```css
:root {
    --adaptive-text-light-max-lightness: 35;
    --adaptive-text-dark-min-lightness: 80;
}
```

每个变量的命名格式为 `--adaptive-<role>-<light|dark>-<limit>`：

*   角色为 `text`（字体颜色）、`background`（字体背景颜色）、`table-border` 或 `table-background`（表格和单元格）。
*   `light` 或 `dark` 是该限制所适用的主题类型，由 `--theme-style` 声明。
*   限制为 `min-lightness` 或 `max-lightness`（CIELAB 亮度，从 0 表示黑色到 100 表示白色），或 `max-chroma`（颜色的饱和度上限；`150` 表示实际上没有限制）。每个值必须是纯数字，否则颜色将失去其自适应效果。

默认值如下：

| 角色 | 浅色主题 | 深色主题 |
| --- | --- | --- |
| `text` | `max-lightness: 40`、`max-chroma: 150` | `min-lightness: 75`、`max-chroma: 55` |
| `background` | `min-lightness: 90`、`max-chroma: 20` | `max-lightness: 30`、`max-chroma: 30` |
| `table-border` | `max-lightness: 60`、`max-chroma: 150` | `min-lightness: 47`、`max-chroma: 150` |
| `table-background` | `min-lightness: 90`、`max-chroma: 20` | `max-lightness: 30`、`max-chroma: 30` |

这些限制在笔记显示时生效，因此更改它们会同时影响所有笔记。笔记本身会保留每个颜色被选取时的原样，存储在其 `color`、`background-color` 或 `border-color` 样式中，并再次存储在 `--tn-color`、`--tn-background` 或 `--tn-border-color` 变量中，自适应功能会读取这些变量。