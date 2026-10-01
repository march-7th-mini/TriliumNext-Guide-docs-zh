# 包含笔记
文本笔记可以将另一条笔记“包含”为只读小组件或交互式小组件，具体取决于笔记的类型。

这对于例如包含动态生成的图表（来自脚本和“渲染 HTML”笔记）或其他更高级的用例非常有用。

## 包含一条笔记

在<a class="reference-link" href="Formatting%20toolbar.md">格式工具栏</a>中，查找 <span class="tn-icon cke cke-trilium-note"></span> 按钮。它也有一个键盘快捷键，但默认未分配。

## 分享功能中的包含笔记

如果一条[分享的笔记](../../Advanced%20Usage/Sharing.md)包含一个或多个被包含的笔记，它们将显示在该笔记的内容中，就像它们是笔记本身的一部分一样。

为此，被包含的笔记也必须被分享，否则它们将不会显示。但是，被包含的笔记仍然可以通过 `#shareHiddenFromTree` 从笔记树中隐藏。

## 交互式笔记

自 v0.104.0 起，被包含的笔记可能会根据其笔记类型变为交互式：

*   <a class="reference-link" href="../../Collections.md">集合</a>（例如<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>）将完全以交互方式渲染，包括创建新笔记。
*   <a class="reference-link" href="../Saved%20Search.md">保存的搜索</a>也会显示结果。
*   <a class="reference-link" href="../Web%20View.md">网页视图</a>提供网站的交互式预览。