# 主题
## 默认主题

Trilium 自带几个预装的颜色主题，默认是浅色主题。要切换到深色主题或任何其他可用主题，请导航到选项菜单（可通过左上角的应用图标访问），选择外观选项卡，然后选择您喜欢的主题。

![深色主题](Themes_dark-theme.png)

当深色主题处于活动状态时，Trilium 会请求 Dark Reader 浏览器扩展不要再次将页面变暗。Dark Reader 仍会将浅色主题变暗。从深色主题切换到浅色主题后，请重新加载页面（<kbd>Ctrl</kbd>+<kbd>R</kbd>），以便 Dark Reader 再次生效。

## 创建自定义 CSS 主题

Trilium 支持自定义用户主题，允许您个性化应用程序的外观。要创建自定义主题，请按照以下步骤操作：

1.  **创建 CSS 代码笔记**：首先创建一个类型为 `CSS` 的新[代码笔记](../Note%20Types/Code.md)。
2.  **添加** `#appTheme` **标注**：为您的笔记添加[属性](../Advanced%20Usage/Attributes.md) `#appTheme=my-theme-name`，其中 `my-theme-name` 是您自定义主题的名称。
3.  **定义您的样式**：在笔记中编写您的自定义 CSS。

<details open="">
    <summary>自定义主题示例</summary>
    <pre><code class="language-text-x-trilium-auto">@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  src: url('/custom/fonts/raleway.woff2') format('woff2');
}

:root {
    --main-font-family: 'Raleway' !important;
    --main-font-size: normal;
    --tree-font-family: inherit;
    --tree-font-size: normal;
    --detail-font-family: inherit;
    --detail-font-size: normal;
    --detail-text-font-family: 'Garamond' !important;

    --main-background-color: #404552;
    --main-text-color: #AFB8C6;
    --main-border-color: #AFB8C6;
    --accented-background-color: #383C4A;
    --more-accented-background-color: #2F343F;
    --header-background-color: #383C4A;
    --button-background-color: #2F343F;
    --button-disabled-background-color: #404552;
    --button-border-color: #333;
    --button-text-color: #AFB8C6;
    --button-border-radius: 2px;
    --primary-button-background-color: #6c757d;
    --primary-button-text-color: white;
    --primary-button-border-color: #6c757d;
    --muted-text-color: #86919F;
    --input-text-color: #AFB8C6;
    --input-background-color: #404552;
    --hover-item-text-color: white;
    --hover-item-background-color: #4877B1;
    --active-item-text-color: white;
    --active-item-background-color: #4877B1;
    --menu-text-color: #AFB8C6;
    --menu-background-color: #383C4A;
    --tooltip-background-color: #383C4A;
    --link-color: lightskyblue;
    --modal-background-color: #404552;
    --modal-backdrop-color: black;
    --scrollbar-border-color: rgba(175, 184, 198, 0.5);
}

body .note-detail-text {
    font-size: 120%;
}

body .CodeMirror {
    filter: invert(100%) hue-rotate(180deg);
}</code></pre>
    <p>&nbsp;</p>
</details>

 

### 激活您的自定义主题

创建自定义主题后：

1.  转到“菜单”->“选项”->“外观”。
2.  在主题选择下拉菜单中，您应该会看到您的自定义主题以您通过 `#appTheme` [标签](../Advanced%20Usage/Attributes.md)提供的名称列出。
3.  选择您的自定义主题以激活它。

如果您对主题进行了更改，请按 Ctrl + R 重新加载前端并应用您的更新。

### 共享和导入主题

自定义主题可以导出为 `.tar` 归档文件，可以与其他用户共享。但是，从不受信任的来源导入主题时要小心，因为它们可能包含可执行脚本，可能会带来安全风险。

一个示例用户主题 _Steel Blue_ 可在演示文档中找到。

![Steel Blue 主题](Themes_steel-blue.png)

### 将自定义 CSS 用于特定目的

除了完整的主题外，Trilium 还允许使用不绑定到主题的自定义 CSS。这在脚本编写场景中特别有用，您可能希望修改特定的 UI 元素，例如更改树视图中笔记的颜色。

### 应用自定义 CSS

要使用自定义 CSS：

1.  **创建 CSS 代码笔记**：创建一个类型为 `CSS` 的新 <a class="reference-link" href="../Note%20Types/Code.md">代码</a> 笔记。
2.  **添加** `appCss` **标签**：为笔记添加 `#appCss` [标签](../Advanced%20Usage/Attributes.md)。
3.  **编写您的 CSS**：将您的自定义 CSS 规则添加到笔记中。

例如：

```
/* Custom CSS to style specific elements */
.tree-item {
    color: #ff6347; /* Change tree item color */
}
```

当 Trilium 的前端启动时，所有标记为 `appCss` 的笔记都会自动包含在 HTML 页面的 style 元素中。

进行更改后，按 Ctrl + R 重新加载前端并应用您的新样式。

![](Themes_image.png)

### 为树中的特定笔记设置样式

要为树中的某些笔记应用特定样式：

*   **使用** `cssClass` **属性**：为笔记添加 `cssClass` [属性](../Advanced%20Usage/Attributes.md)，并为其分配一个代表所需 CSS 类的值。
*   **定义** `iconClass`：您还可以使用 `iconClass` 属性为笔记定义自定义图标，可从 [Box Icons](https://boxicons.com) 或您自己的自定义类中选择。

例如，如果您想为特定类型的笔记设置样式，例如包含 PNG 图像的笔记，您可以使用 `type-image mime-image-png` 等类来定位它们。

### 用户提供的主题

有一个用户创建的主题库，展示了 Trilium 社区开发的各种自定义内容。有关更多信息，请查看 <a class="reference-link" href="Themes/Theme%20Gallery.md">主题库</a>。

### 资源路径管理

在自定义主题或 CSS 中引用图像等内置资源时，您可以使用 `vX` 别名来避免硬编码版本号。例如，不要指定 `/assets/v0.57.0-beta/images/icon-grey.png`，您可以使用 `/assets/vX/images/icon-grey.png` 来保持您的主题与 Trilium 的未来版本兼容。