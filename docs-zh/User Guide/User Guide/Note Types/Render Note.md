# 渲染笔记
<figure class="image"><img style="aspect-ratio:601/216;" src="Render Note_image.png" width="601" height="216"></figure>

渲染笔记是[前端脚本](../Scripting/Frontend%20Basics.md)的一种特殊情形，它允许在笔记内渲染自定义内容。这使得创建自定义仪表板或使用自定义笔记编辑器成为可能。

内容可以是原生 HTML，也可以是 Preact JSX。

## 创建渲染笔记

1.  创建一个<a class="reference-link" href="Code.md">代码</a>笔记，其中：
    1.  对于传统/原生方法，使用 HTML 语言，并包含需要显示的内容（例如 `<p>Hello world.</p>`）。
    2.  对于基于 Preact 的方法，使用 JSX（见下文）。
2.  创建一个<a class="reference-link" href="Render%20Note.md">渲染笔记</a>。
3.  分配 `renderNote` [关系](../Advanced%20Usage/Attributes.md)指向先前创建的代码笔记。

## 使用 jQuery 的传统脚本

对于<a class="reference-link" href="../Scripting.md">脚本</a>而言，静态 HTML 通常是不够的。下一步是使用 JavaScript 自动更改笔记的某些部分。

举一个简单的例子，我们将创建一个渲染笔记，在一个字段中显示当前日期。

为此，首先创建一个包含以下内容的 HTML 代码笔记：

```html
<h1>Current date & time</h1>
The current date & time is <span class="date"></span>
```

现在我们需要添加脚本。再创建一个<a class="reference-link" href="Code.md">代码</a>笔记，但这次使用 JavaScript（前端）语言。确保新创建的笔记是先前创建的 HTML 笔记的直接子笔记；内容如下：

```javascript
const $dateEl = api.$container.find(".date");
$dateEl.text(new Date());
```

现在在任意位置创建一个渲染笔记，并将其 `~renderNote` 关系设置为指向该 HTML 笔记。访问渲染笔记时，它将显示：

> **Current date & time**  
> The current date & time is Sun Apr 06 2025 15:26:29 GMT+0300 (Eastern European Summer Time)

## 使用 Preact 和 JSX 的动态内容

作为 jQuery 的更现代替代方案，可以使用 Preact 和 JSX 来渲染页面。由于 JSX 是 JavaScript 的超集，因此不再需要提供 HTML。

以下是创建简单渲染笔记的步骤：

1.  创建一个类型为<a class="reference-link" href="Render%20Note.md">渲染笔记</a>的笔记。
2.  创建一个子<a class="reference-link" href="Code.md">代码</a>笔记，语言为 JSX。  
    例如，使用以下内容：
    
    ```
    export default function() {
        return (
            <>
                <p>Hello world.</p>
            </>
        );
    }
    ```
3.  在父渲染笔记中，定义一个 `~renderNote` 关系，指向新创建的子笔记。
4.  刷新渲染笔记，它应显示一条“Hello world”消息。

## 刷新笔记

可以通过以下方式刷新笔记：

*   <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>区域中的 <span class="tn-icon bx bx-refresh"></span> 按钮。
*   “渲染活动笔记”[键盘快捷键](../Basic%20Concepts%20and%20Features/Keyboard%20Shortcuts.md)（默认未分配）。

## 打印

一旦设置了 `~renderNote` 关系，就可以从<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20menu.md">笔记菜单</a>打印渲染笔记或将其导出为 PDF（参见<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印与导出为 PDF</a>）。与其他笔记不同，它会完全按照显示的样子打印：脚本不会再次运行，因此笔记中键入、选择或加载的内容都会保留。

*   内容会按页面宽度重新排版，因此脚本为屏幕尺寸设置的元素（如图表）可能无法适应。
*   滚动区域（例如滚动容器中的表格）会按其完整高度打印，不带滚动条。
*   要调整打印布局，请使用 `~printCss` 关系。
*   无论当前主题如何，打印时都使用浅色。

当渲染笔记作为<a class="reference-link" href="../Collections/List%20View.md">列表视图</a>集合的一部分被打印，或从其附件等其他视图打印时，它不在屏幕上，因此其脚本会为打印再次运行。在集合中，输出打印时不带笔记自身的样式。

## 示例

*   <a class="reference-link" href="../Advanced%20Usage/Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a>，它存在于<a class="reference-link" href="../Advanced%20Usage/Database/Demo%20Notes.md">演示笔记</a>中。