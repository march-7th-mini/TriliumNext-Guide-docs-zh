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

请注意，移动端布局中还有一种“平板模式”。对于这种情况，需要使用媒体查询：

```css
@media (max-width: 991px) {

    #launcher-pane {

        /* 在移动端布局上执行某些操作 */

    }

}



@media (min-width: 992px) {

    #launcher-pane {

        /* 在移动端平板 + 桌面端布局上执行某些操作 */

    }

}
```

## 检测水平与垂直布局

用户可以在垂直布局（经典布局，启动器栏在左侧）和水平布局（启动器栏在顶部且标签页为全宽）之间进行选择。

可以通过在 `body` 级别使用类来应用不同的样式：

```
body.layout-vertical #left-pane {
	/* 执行某些操作 */
}

body.layout-horizontal #center-pane {
	/* 执行其他操作 */	
}
```

这两种不同的布局使用不同的容器（但无论用户如何选择，它们都存在于 DOM 中），例如，可以使用 `#horizontal-main-container` 和 `#vertical-main-container` 来自定义内容区域的背景。

## 检测平台（Windows、macOS）或 Electron

可以通过在 `body` 中使用类来添加仅适用于特定平台的特定样式：

| Windows | macOS |
| --- | --- |
| `<br>body.platform-win32 {<br> background: red;<br>}<br>` | `<br>body.platform-darwin {<br> background: red;<br>}<br>` |

也可以仅在 Electron（桌面应用程序）环境下应用样式：

```
body.electron {
	background: blue;
}
```

### 原生标题栏

可以通过查询 `body` 来检测用户是选择了原生标题栏还是自定义标题栏：

```
body.electron.native-titlebar {
	/* 执行某些操作 */
}

body.electron:not(.native-titlebar) {
	/* 执行其他操作 */
}
```

### 原生窗口按钮

在 Electron 环境下且关闭原生标题栏时，引入了一项功能，可以使用特定于平台的窗口按钮，例如 macOS 上的信号灯按钮。

有关此功能的原始实现（包括截图），请参阅 [由 eliandoran 提交的原生标题栏按钮 · Pull Request #702 · TriliumNext/Notes](https://github.com/TriliumNext/Notes/pull/702)。

#### 在 Windows 上

可以使用 RGB 十六进制颜色调整原生窗口按钮区域的颜色：

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

在 macOS 上，当禁用原生标题栏时，默认启用信号灯窗口按钮。可以使用以下方式调整按钮的偏移量：

```css
body {
    --native-titlebar-darwin-x-offset: 12;
    --native-titlebar-darwin-y-offset: 14 !important;
}
```

### Windows 上的背景/透明效果（Mica）

Windows 11 提供了一种称为 Mica 的特殊背景/透明效果，主题可以通过在 `body` 级别设置 `--background-material` 变量来启用它：

```css
body.electron.platform-win32 {
	--background-material: tabbed; 
}
```

该值可以是 `tabbed`（对水平布局特别有用）或 `mica`（非常适合垂直布局）。

请注意，Mica 效果应用于 `body` 级别，并且主题需要使整个层级结构（半）透明才能使其可见。可以参考 TriliumNext 主题作为灵感。

## 笔记图标、标签页工作区强调色

主题功能是通过 CSS 变量进行的小调整，可以影响应用程序的布局或视觉外观。

在标签栏中，要显示笔记的图标而不是工作区的图标：

```css
:root {
	--tab-note-icons: true;
}
```

当某个标签页提升（hoisted）了一个工作区时，可以获取该工作区的背景颜色，例如，在标签页上应用一个小条而不是整个背景颜色：

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

目前，包含自定义字体的唯一方法是使用[自定义资源提供器](../Advanced%20Usage/Custom%20Resource%20Providers.md)。基本上，将字体导入 Trilium 并为其分配 `#customResourceProvider=fonts/myfont.ttf`，然后通过 `/custom/fonts/myfont.ttf` 在 CSS 中导入字体。如果你的 Trilium 服务器运行在 `/` 以外的路径上，请使用 `../../../custom/fonts/myfont.ttf`。

## 深色和浅色主题

浅色主题需要具有以下 CSS：

```css
:root {
	--theme-style: light;
}
```

如果主题是深色的，则 `--theme-style` 需要为 `dark`。

如果主题是自动的（例如，根据 `prefers-color-scheme` 同时支持浅色或深色），则它还必须声明（除了将 `--theme-style` 设置为 `light` 或 `dark` 之外）：

```css
:root {

    --theme-style-auto: true;

}
```

这将通过将颜色偏好告知操作系统来影响 Electron 应用程序的行为（例如，背景效果在 Windows 上将正确显示）。