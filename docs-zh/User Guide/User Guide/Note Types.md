# 笔记类型
Trilium 的核心功能之一是它支持多种类型的笔记，具体取决于需求。

## 通过笔记树创建不同类型的新笔记

Trilium 中的默认笔记类型（例如创建新笔记时）是 <a class="reference-link" href="Note%20Types/Text.md">文本</a>，因为它适用于一般用途。

要创建不同类型的新笔记，请前往 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>，右键点击要放置新笔记的现有笔记，然后选择：

*   _在此笔记后插入_，将新笔记放在所选笔记的下方。
*   _插入子笔记_，将笔记作为所选笔记的子笔记插入。

![](Note%20Types_image.png)

## 通过添加链接或新建标签页创建不同类型的新笔记

*   在 <a class="reference-link" href="Note%20Types/Text.md">文本</a> 笔记中添加[链接](Note%20Types/Text/Links.md)时，输入新笔记的所需标题并按 Enter。之后会询问笔记的类型。
*   同样，在创建新标签页时，输入所需的标题并按 Enter。

## 更改笔记的类型

可以通过 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a> 中的 _基本属性_ 标签页在笔记创建后更改其类型。请注意，通常只有在笔记为空时才建议更改笔记类型。也可以用于编辑[笔记的源代码](Advanced%20Usage/Note%20source.md)。

## 支持的笔记类型

Trilium 支持以下笔记类型：

| 笔记类型 | 描述 |
| --- | --- |
| <a class="reference-link" href="Note%20Types/Text.md">文本</a> | 默认笔记类型，支持富文本格式、图片、警示框和从右到左的支持。 |
| <a class="reference-link" href="Note%20Types/Code.md">代码</a> | 使用等宽字体，可用于存储比文本笔记更大的代码块或纯文本，并具有更好的语法高亮。 |
| <a class="reference-link" href="Note%20Types/Saved%20Search.md">保存的搜索</a> | 存储关于搜索的信息（搜索文本、条件等）以供以后使用。例如，可用于快速筛选大量笔记。搜索可以轻松触发。 |
| <a class="reference-link" href="Note%20Types/Relation%20Map.md">关系图</a> | 允许轻松创建笔记及其之间的关系。主要用于关系型数据，如家谱。 |
| <a class="reference-link" href="Note%20Types/Note%20Map.md">笔记图</a> | 显示笔记之间的关系，无论是通过关系还是其层级结构。 |
| <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a> | 用于 <a class="reference-link" href="Scripting.md">脚本</a>，它显示另一个笔记的 HTML 内容。这允许显示任何类型的内容，只要背后有脚本生成它。 |
| <a class="reference-link" href="Collections.md">集合</a> | 以网格、列表或更特殊的情况：日历的形式显示笔记的子笔记。            <br>  <br>通常用于方便阅读短笔记。 |
| <a class="reference-link" href="Note%20Types/Mermaid%20Diagrams.md">Mermaid 图表</a> | 显示条形图、流程图、状态图等图表。需要一些技术知识，因为图表是用专门的格式编写的。 |
| <a class="reference-link" href="Note%20Types/Canvas.md">画布</a> | 允许轻松绘制草图、图表、手写内容。使用与 [excalidraw.com](https://excalidraw.com) 相同的技术。 |
| <a class="reference-link" href="Note%20Types/Web%20View.md">网页视图</a> | 显示外部网页的内容，类似于浏览器。 |
| <a class="reference-link" href="Note%20Types/Mind%20Map.md">思维导图</a> | 通过将想法放置在层级布局中，便于头脑风暴。 |
| <a class="reference-link" href="Collections/Geo%20Map.md">地理地图</a> | 将笔记的子笔记显示为地理地图，一个用例是规划假期。它甚至对轨迹有基本支持。也可以从中创建笔记。 |
| <a class="reference-link" href="Note%20Types/File.md">文件</a> | 表示上传的文件，如 PDF、图片、视频或音频文件。 |