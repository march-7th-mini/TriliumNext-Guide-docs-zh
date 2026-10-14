# 参考
## 检测移动端与桌面端

移动端布局与桌面端不同。使用 `body.mobile` 和 `body.desktop` 来区分它们。

```css
body.mobile #root-widget {
	/* 在移动端执行某些操作 */
}

body.desktop #root-widget {
	/* 在桌面端执行某些操作 */
}
```

请注意，移动端布局中还存在“平板模式”。对于这种特殊情况，需要使用媒体查询：

```css
@media (max-width: 991px) {
    #launcher-pane {
        /* 在移动端布局中执行某些操作 */
    }
}



@media (min-width: 992px) {
    #launcher-pane {
        /* 在移动端平板 + 桌面端布局中执行某些操作 */
    }
}
```

## 检测水平与垂直布局

用户可以在垂直布局（经典布局，启动器栏位于左侧）和水平布局（启动器栏位于顶部，标签页为全宽）之间进行选择。

可以通过在 `body` 层级使用类来应用不同的样式：

```css
body.layout-vertical #left-pane {
	/* 执行某些操作 */
}

body.layout-horizontal #center-pane {
	/* 执行其他操作 */	
}
```

这两种不同的布局使用不同的容器（但无论用户如何选择，它们都存在于 DOM 中），例如 `#horizontal-main-container` 和 `#vertical-main-container` 可用于自定义内容区域的背景。

## 检测平台（Windows、macOS）或 Electron

=== "<span class="tn-icon bx bxl-windows"></span> Windows"

    ```css
    body.platform-win32 {
    	background: red;
    }
    ```

=== "<span class="tn-icon bx bxl-apple"></span> macOS"

    ```css
    body.platform-darwin {
    	background: red;
    }
    ```

=== "<span class="tn-icon bx bx-windows"></span> Electron（桌面应用）"

    要区分<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>和<a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>：

    ```
    body.electron {
    	background: blue;
    }
    ```

    可以与 Windows/macOS 检测链式组合（例如 `body.electron.platform-win32`）。

### 原生标题栏

可以通过查询 `body` 来检测用户是否选择了原生标题栏或自定义标题栏：

```
body.electron.native-titlebar {
	/* 执行某些操作 */
}

body.electron:not(.native-titlebar) {
	/* 执行其他操作 */
}
```

### 原生窗口按钮

在 Electron 下运行时，如果关闭了原生标题栏，则引入了一项功能，使用平台特定的窗口按钮，例如 macOS 上的信号灯按钮。

有关此功能的原始实现（包括截图），请参阅 [Native title bar buttons by eliandoran · Pull Request #702 · TriliumNext/Notes](https://github.com/TriliumNext/Notes/pull/702)。

=== "<span class="tn-icon bx bxl-windows"></span> Windows"

    原生窗口按钮区域的颜色可以使用 RGB 十六进制颜色进行调整：

    ```
    body {
    	--native-titlebar-foreground: #ffffff;
    	--native-titlebar-background: #ff0000;
    }
    ```

    也可以使用 RGBA 十六进制颜色来实现透明效果，但代价是悬停颜色会减少：

    ```
    body {
    	--native-titlebar-background: #ff0000aa;
    }
    ```

    请注意，该值在窗口初始化时读取，之后仅在用户更改其浅色/深色模式偏好时才会刷新。

=== "<span class="tn-icon bx bxl-apple"></span> macOS"

    在 macOS 上，当禁用原生标题栏时，信号灯窗口按钮默认启用。按钮的偏移量可以使用以下方式调整：

    ```css
    body {
        --native-titlebar-darwin-x-offset: 12;
        --native-titlebar-darwin-y-offset: 14 !important;
    }
    ```

### Windows 上的背景/透明效果（Mica）

Windows 11 提供了一种特殊的背景/透明效果，称为 Mica，主题可以通过在 `body` 层级设置 `--background-material` 变量来启用：

```css
body.electron.platform-win32 {
	--background-material: tabbed; 
}
```

该值可以是 `tabbed`（对水平布局特别有用）或 `mica`（非常适合垂直布局）。

请注意，Mica 效果应用于 `body` 层级，主题需要使整个层级结构（半）透明才能使其可见。可以参考 TrilumNext 主题作为灵感。

## 笔记图标、标签页工作区强调色

主题功能是通过 CSS 变量进行的小调整，可以影响应用程序的布局或视觉外观。

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

使用自定义字体的推荐方式是直接在 Trilium 中导入字体。有关如何操作的信息，请参阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Personalizing%20the%20font.md">个性化字体</a>。

或者，对于提供自己字体的主题，可以使用[自定义资源提供程序](../Advanced%20Usage/Custom%20Resource%20Providers.md)：将字体导入 Trilium 并为其分配 `#customResourceProvider=fonts/myfont.ttf`，然后通过 `/custom/fonts/myfont.ttf` 在 CSS 中导入字体。如果您的 Trilium 服务器运行在 `/` 以外的路径上，请使用 `../../../custom/fonts/myfont.ttf`。

## 深色和浅色主题

浅色主题需要具有以下 CSS：

```css
:root {
	--theme-style: light;
}
```

如果主题是深色的，则 `--theme-style` 需要为 `dark`。深色的 `--theme-style` 还会告诉 Dark Reader 浏览器扩展不要修改页面。

如果主题是自动的（例如基于 `prefers-color-scheme` 同时支持浅色或深色），则还必须声明（除了将 `--theme-style` 设置为 `light` 或 `dark` 之外）：

```css
:root {

    --theme-style-auto: true;

}
```

这将通过向操作系统告知颜色偏好来影响 Electron 应用程序的行为（例如，背景效果在 Windows 上将正确显示）。

## 自适应文本和表格颜色

在文本笔记中应用的颜色，来自字体颜色和背景颜色按钮（请参阅<a class="reference-link" href="../Note%20Types/Text/General%20formatting.md">通用格式</a>）或来自表格和单元格属性（请参阅<a class="reference-link" href="../Note%20Types/Text/Tables.md">表格</a>），会以适合主题的色调显示：色相保持不变，而亮度和饱和度则保持在限制范围内。主题可以更改这些限制，例如，如果其页面背景比内置主题的页面背景暗得多或亮得多：

```css
:root {
    --adaptive-text-light-max-lightness: 35;
    --adaptive-text-dark-min-lightness: 80;
}
```

每个变量的命名为 `--adaptive-<role>-<light|dark>-<limit>`：

*   角色为 `text`（字体颜色）、`background`（字体背景颜色）、`table-border` 或 `table-background`（表格和单元格）。
*   `light` 或 `dark` 是该限制所适用的主题类型，由 `--theme-style` 声明。
*   限制为 `min-lightness` 或 `max-lightness`（CIELAB 亮度，从黑色的 0 到白色的 100），或 `max-chroma`（颜色的最大饱和度；`150` 表示没有实际限制）。每个值必须是纯数字，否则颜色将失去其自适应能力。

默认值为：

| 角色 | 浅色主题 | 深色主题 |
| --- | --- | --- |
| `text` | `max-lightness: 40`、`max-chroma: 150` | `min-lightness: 75`、`max-chroma: 55` |
| `background` | `min-lightness: 90`、`max-chroma: 20` | `max-lightness: 30`、`max-chroma: 30` |
| `table-border` | `max-lightness: 60`、`max-chroma: 150` | `min-lightness: 47`、`max-chroma: 150` |
| `table-background` | `min-lightness: 90`、`max-chroma: 20` | `max-lightness: 30`、`max-chroma: 30` |

这些限制在笔记显示时生效，因此对它们的更改会同时影响每个笔记。笔记本身会保留每个颜色在被选取时的状态，存储在其 `color`、`background-color` 或 `border-color` 样式中，并再次存储在 `--tn-color`、`--tn-background` 或 `--tn-border-color` 变量中，自适应功能会读取这些变量。