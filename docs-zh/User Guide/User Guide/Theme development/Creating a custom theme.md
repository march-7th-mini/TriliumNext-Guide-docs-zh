# 创建自定义主题
## 第一步：找个地方存放主题

组织性是管理知识库的一个重要方面。在开发新主题或导入现有主题时，最好将它们集中放在一个地方。

因此，第一步是创建一个新笔记来汇集所有主题。

![](Creating%20a%20custom%20theme_5_Creating%20a%20custom%20theme_im.png)

## 第二步：创建主题

|  |  |
| --- | --- |
| ![](Creating%20a%20custom%20theme_3_Creating%20a%20custom%20theme_im.png) | 主题是带有特殊属性的代码笔记。首先创建一个新的代码笔记。 |
| ![](Creating%20a%20custom%20theme_1_Creating%20a%20custom%20theme_im.png) | 然后将笔记类型更改为 CSS 代码。 |
| ![](Creating%20a%20custom%20theme_Creating%20a%20custom%20theme_im.png) | 在_拥有的属性_部分中，定义 `#appTheme` 属性并指向任何想要的名称。此名称将显示在设置中的外观部分。 |

## 第三步：定义主题的 CSS

作为一个非常简单的示例，我们将启动器面板的背景颜色更改为蓝色调。

要更改主题的不同变量：

```css
:root {
	--launcher-pane-background-color: #0d6efd;
}
```

## 第四步：激活主题

刷新应用程序（按 Ctrl+Shift+R 是一个好方法）并进入设置。您应该能看到新创建的主题：

![](Creating%20a%20custom%20theme_2_Creating%20a%20custom%20theme_im.png)

之后，应用程序将使用新主题自动刷新：

![](Creating%20a%20custom%20theme_4_Creating%20a%20custom%20theme_im.png)

请注意，该主题将基于旧版主题。要覆盖此设置并将主题基于新的 TriliumNext 主题，请参阅：[主题基础（旧版 vs 新版）](Customize%20the%20Next%20theme.md)

## 第五步：进行修改

只需返回笔记并根据需要进行更改。要将更改应用到当前窗口，请按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> 进行刷新。

建议保持两个窗口，一个用于编辑，另一个用于预览更改。