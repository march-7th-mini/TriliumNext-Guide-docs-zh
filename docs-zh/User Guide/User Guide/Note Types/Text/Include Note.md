# 包含笔记

文本笔记可以“包含”另一个笔记，具体取决于笔记的类型，可以将其作为只读小组件或交互式小组件。

这对于例如包含动态生成的图表（来自脚本和“渲染 HTML”笔记）或其他更高级的用例非常有用。

## 包含一个笔记

在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中，查找![](Include%20Note_image.png)按钮。该功能也有对应的键盘快捷键，但默认情况下未分配。

## 分享功能中包含的笔记

如果[共享笔记](../../Advanced%20Usage/Sharing.md)包含一个或多个被包含的笔记，它们将显示在笔记内容中，就像它们是笔记本身的一部分一样。

为此，被包含的笔记也必须被共享，否则它们将不会显示。但是，被包含的笔记仍然可以通过`#shareHiddenFromTree`在笔记树中隐藏。

## 交互式笔记

自 v0.104.0 版本起，被包含的笔记可能会根据其笔记类型变为交互式：

*   <a class="reference-link" href="../../Collections.md">集合</a>（例如<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>）将完全交互式渲染，包括创建新笔记。
*   <a class="reference-link" href="../Saved%20Search.md">已保存的搜索</a>也将显示结果。
*   <a class="reference-link" href="../Web%20View.md">网页视图</a>提供网站的交互式预览。