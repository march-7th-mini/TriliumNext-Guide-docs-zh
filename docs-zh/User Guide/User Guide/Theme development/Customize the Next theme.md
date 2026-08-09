# 自定义 Next 主题
默认情况下，任何自定义主题都基于旧版浅色主题。要改用 TriliumNext 主题，请在现有主题上添加 `#appThemeBase=next` 属性。`appTheme` 属性也必须存在。

![](Customize%20the%20Next%20theme_image.png)

`appThemeBase` 标签可以设置为以下值之一：

*   `next`，用于 TriliumNext（自动浅色或深色模式）。
*   `next-light`，用于 TriliumNext 的始终浅色模式。
*   `next-dark`，用于 TriliumNext 的始终深色模式。
*   任何其他值都将被忽略，并改用旧版白色主题。

## 覆盖项

请注意，TriliumNext 主题比旧版主题有更多的覆盖项。因此，建议在使用 Next 主题时使用 `#trilium-app` 而不是旧版主题的 `:root`。

```css
#trilium-app {
	--launcher-pane-background-color: #0d6efd;
}
```