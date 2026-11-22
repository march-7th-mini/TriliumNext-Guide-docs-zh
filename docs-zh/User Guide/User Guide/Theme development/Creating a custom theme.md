# 创建自定义主题
## 第 1 步：找到一个放置主题的位置

组织是管理知识库的重要方面。在开发新主题或导入现有主题时，将它们集中放在一个地方是个好主意。

因此，第一步是创建一个新笔记来收集所有主题。

## 第 2 步：创建主题

<table>
    <tbody>
        <tr>
            <td><img src="Creating a custom theme_3_Creating a custom theme_im.jpg"></td>
            <td>主题是带有特殊属性的代码笔记。首先创建一个新的代码笔记。</td>
        </tr>
        <tr>
            <td><img src="Creating a custom theme_1_Creating a custom theme_im.jpg"></td>
            <td>然后将笔记类型更改为 CSS 代码。</td>
        </tr>
    </tbody>
</table>

然后，在笔记的<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中（<span class="tn-icon bx bx-list-check"></span> 按钮），将 `#appTheme` 标签设置为任意名称。这就是在设置的外观部分中显示的名称。

## 第 3 步：定义主题的 CSS

作为一个非常简单的示例，我们将把启动器窗格的背景颜色更改为蓝色调。

要更改主题的不同变量：

```css
:root {
	--launcher-pane-background-color: #0d6efd;
}
```

## 第 4 步：激活主题

刷新应用程序（Ctrl+Shift+R 是一个好方法）并转到设置。你应该能看到新创建的主题：

![](Creating%20a%20custom%20theme_2_Creating%20a%20custom%20theme_im.jpg)

之后应用程序将使用新主题刷新自身：

![](Creating%20a%20custom%20theme_4_Creating%20a%20custom%20theme_im.jpg)

请注意，该主题将基于旧版主题。要覆盖该设置并将主题基于 Modern 主题，请参阅<a class="reference-link" href="Customize%20the%20Next%20theme.md">自定义 Next 主题</a>。

## 第 5 步：进行更改

只需回到笔记并根据需要进行更改。要将更改应用到当前窗口，请按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> 刷新。

保持两个窗口是个好主意，一个用于编辑，另一个用于预览更改。