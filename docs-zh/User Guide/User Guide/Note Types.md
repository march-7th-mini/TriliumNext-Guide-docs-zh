# 笔记类型

Trilium 的核心特性之一是其支持多种类型的笔记，具体取决于需求。

## 通过笔记树创建不同类型的笔记

Trilium 中的默认笔记类型（例如创建新笔记时）是<a class="reference-link" href="Note%20Types/Text.md">文本</a>，因为它适用于一般用途。

要创建其他类型的新笔记，请前往<a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>，右键点击要放置新笔记的现有笔记，然后选择：

*   _在其后插入笔记_，将新笔记放在所选笔记的下方。
*   _插入子笔记_，将新笔记作为所选笔记的子笔记插入。

![](Note%20Types_image.png)

## 通过添加链接或新标签页创建不同类型的笔记

*   在<a class="reference-link" href="Note%20Types/Text.md">文本</a>笔记中添加[链接](Note%20Types/Text/Links.md)时，输入新笔记的所需标题并按回车。之后会询问笔记的类型。
*   类似地，创建新标签页时，输入所需标题并按回车。

## 更改笔记的类型

创建笔记后，可以通过<a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a>中的_基本属性_选项卡更改笔记的类型。请注意，通常只在笔记为空时更改笔记类型才是个好主意。也可以用于编辑[笔记的源代码](Advanced%20Usage/Note%20source.md)。

## 支持的笔记类型

Trilium 支持以下笔记类型：

| 笔记类型 | 描述 |
| --- | --- |
| <a class="reference-link" href="Note%20Types/Text.md">文本</a> | 默认笔记类型，支持富文本格式、图片、警示框以及从右到左显示。 |
| <a class="reference-link" href="Note%20Types/Code.md">代码</a> | 使用等宽字体，可用于存储比文本笔记更大的代码块或纯文本，并且具有更好的语法高亮。 |
| <a class="reference-link" href="Note%20Types/Saved%20Search.md">已保存搜索</a> | 存储搜索信息（搜索文本、条件等）以供以后使用。例如，可用于快速筛选大量笔记。可以轻松触发搜索。 |
| <a class="reference-link" href="Note%20Types/Relation%20Map.md">关系图</a> | 允许轻松创建笔记及其之间的关系。主要用于关系型数据，例如家谱。 |
| <a class="reference-link" href="Note%20Types/Note%20Map.md">笔记地图</a> | 显示笔记之间的关系，无论是通过关系还是它们的层级结构。 |
| <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a> | 用于<a class="reference-link" href="Scripting.md">脚本</a>，显示另一个笔记的 HTML 内容。这允许显示任何类型的内容，前提是有脚本在背后生成它。 |
| <a class="reference-link" href="Collections.md">集合</a> | 将笔记的子笔记显示为网格、列表，或者更专业的场景：日历。          <br>  <br>通常有助于轻松阅读短笔记。 |
| <a class="reference-link" href="Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a> | 显示图表，如条形图、流程图、状态图等。由于图表是用专门格式编写的，因此需要一些技术知识。 |
| <a class="reference-link" href="Note%20Types/Canvas.md">画布</a> | 允许轻松绘制草图、图表、手写内容。使用与 [excalidraw.com](https://excalidraw.com) 相同的技术。 |
| <a class="reference-link" href="Note%20Types/Web%20View.md">网页视图</a> | 显示外部网页的内容，类似于浏览器。 |
| <a class="reference-link" href="Note%20Types/Mind%20Map.md">思维导图</a> | 通过将想法放置在层级布局中，便于头脑风暴。 |
| <a class="reference-link" href="Collections/Geo%20Map.md">地理地图</a> | 将笔记的子笔记显示为地理地图，一个用例是规划假期。它甚至支持基本的轨迹功能。也可以从中创建笔记。 |
| <a class="reference-link" href="Note%20Types/File.md">文件</a> | 表示上传的文件，如 PDF、图片、视频或音频文件。 |