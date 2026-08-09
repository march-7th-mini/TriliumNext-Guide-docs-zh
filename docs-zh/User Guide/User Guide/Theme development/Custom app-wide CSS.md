# 自定义全局 CSS

可以提供一个 CSS 文件，无论用户设置的主题是什么，都会使用该文件。

|  |  |
| --- | --- |
| ![](Custom%20app-wide%20CSS_image.png) | 首先创建一个新笔记，并将笔记类型更改为 CSS |
| ![](2_Custom%20app-wide%20CSS_image.png) | 在功能区中，按下“自有属性”部分，并输入 `#appCss`。 |
| ![](3_Custom%20app-wide%20CSS_image.png) | 输入所需的 CSS。    <br>  <br>通常，对于正在更改的样式，最好附加 `!important`，以防止其他样式覆盖。 |

## 查看更改

添加新的 _应用 CSS 笔记_ 或修改现有笔记不会立即应用更改。要查看更改，请先按 Ctrl+Shift+R 刷新页面。

## 示例用例

### 自定义打印样式表

> [!TIP]
> 自 v0.99.2 起，不再可能使用 `#appCss` 来自定义打印 CSS，因为打印现在在隔离环境中进行。
> 
> 但是，仍然可以通过 `~printCss` 自定义 CSS；有关更多信息，请参阅 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印和导出为 PDF</a>。

### 按工作区设置样式

使用 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md">工作区</a> 时，在不同工作区的笔记之间创建视觉区分会很有帮助。

为此：

1.  在带有 `#workspace` 的笔记中，添加一个可继承的属性 `#cssClass(inheritable)`，其值能唯一标识该工作区（例如 `my-workspace`）。
2.  在笔记结构中的任意位置，创建一个带有 `#appCss` 的 CSS 笔记。

#### 更改 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中图标的颜色

```
.fancytree-node.my-workspace.fancytree-custom-icon {
    color: #ff0000;
}
```

#### 更改笔记标题和图标的颜色

要更改笔记标题和图标（内容上方）的颜色：

```
.note-split.my-workspace .note-icon-widget button.note-icon,
.note-split.my-workspace .note-title-widget input.note-title {
    color: #ff0000;
}
```

#### 为笔记内容添加水印

<figure class="image image-style-align-right image_resized" style="width:39.97%;"><img style="aspect-ratio:641/630;" src="1_Custom app-wide CSS_image.png" width="641" height="630"></figure>

1.  在任意笔记中插入一张图片，并获取该图片的 URL。
2.  使用以下 CSS，根据需要调整 `background-image`、`width` 和 `height` 的值。

```
.note-split.my-workspace .scrolling-container:after {
    position: fixed;
    content: "";
    background-image: url("/api/attachments/Rvm3zJNITQI1/image/logo.png");
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    width: 237px;
    height: 44px;
    bottom: 1em;
    right: 1em;
    opacity: 0.5;
    z-index: 0;
}
```

## 局限性

应用程序的某些部分无法直接通过自定义 CSS 进行样式设置，因为它们是在隔离模式（shadow DOM）中渲染的，具体包括：

*   <a class="reference-link" href="../Collections/Presentation.md">演示文稿</a> 中的幻灯片。