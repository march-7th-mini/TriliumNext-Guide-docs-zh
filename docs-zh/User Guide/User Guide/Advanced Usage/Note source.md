# 笔记源代码
## 理解不同笔记的源代码

在内部，每种笔记的内容结构根据其<a class="reference-link" href="../Note%20Types.md">笔记类型</a>而有所不同。

例如：

*   <a class="reference-link" href="../Note%20Types/Text.md">文本</a>笔记在内部以 HTML 表示，使用<a class="reference-link" href="Technologies%20used/CKEditor.md">CKEditor</a>的表示形式。请注意，由于自定义插件的原因，某些 HTML 元素是 Trilium 特有的，例如警示框。
*   <a class="reference-link" href="../Note%20Types/Code.md">代码</a>笔记是纯文本，在内部按原样表示。
*   <a class="reference-link" href="../Collections/Geo%20Map.md">地理地图</a>笔记仅包含最少的信息（视口、缩放级别），以 JSON 格式存储。
*   <a class="reference-link" href="../Note%20Types/Canvas.md">画布</a>笔记以 JSON 表示，包含 Trilium 自身的信息以及 [Excalidraw](Technologies%20used.md) 的内部 JSON 表示格式。
*   <a class="reference-link" href="../Note%20Types/Mind%20Map.md">思维导图</a>笔记以 JSON 表示，使用 [MindElixir](Technologies%20used.md) 的内部格式。

请注意，某些信息也存储为<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>。例如，<a class="reference-link" href="../Note%20Types/Canvas.md">画布</a>笔记使用附件功能来存储自定义库，并且与<a class="reference-link" href="../Note%20Types/Mind%20Map.md">思维导图</a>和其他类似笔记类型一起，它会存储内容的 SVG 表示形式，以供其他功能使用，例如包含在其他笔记中、共享笔记等。

以下是此笔记在数据库中存储的 HTML 表示形式的一部分（已美化）。

```
<h2>
	理解不同笔记的源代码
</h2>
<p>
	在内部，每种笔记的内容结构根据&nbsp;
	<a class="reference-link" href="../Note%20Types.md">
		笔记类型
	</a>
	而有所不同。
</p>
```

## 查看源代码

可以通过在<a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20buttons.md">笔记按钮</a>中按下上下文菜单并选择 _笔记源代码_ 来查看笔记的源代码。

![](Note%20source_image.png)

源代码将显示在新的标签页中。

对于某些笔记类型，例如文本笔记和 JSON 笔记，源代码也会进行格式化，以便更易于阅读。

## 修改源代码

可以直接修改笔记的源代码，但不能通过 _笔记源代码_ 功能进行修改。

操作步骤如下：

1.  将笔记类型从实际类型（例如画布、地理类型）更改为代码（纯文本）或相应的格式，如 JSON 或 HTML。
2.  确认关于更改笔记类型的警告。
3.  源代码将显示出来，进行必要的修改。
4.  将笔记类型更改回实际类型。

> [!WARNING]
> 根据所做的更改，笔记可能无法正确渲染。在进行任何重大更改之前，最好先保存一个修订版本。
> 
> 如果笔记无法正确渲染，请再次修改源代码或恢复到之前的修订版本。由于对意外更改的错误处理可能并不总是完美的，可能需要刷新应用程序。