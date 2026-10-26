# 默认笔记标题
创建新笔记时，其名称默认为“new note”。在某些情况下，可能希望使用不同的甚至动态的默认笔记标题。

对于此用例，Trilium（自 v0.52 起）支持 `#titleTemplate` [标签](Attributes.md)。你可以为给定笔记创建此类标签，为其赋值，该值将在创建子笔记时用作默认标题。与其他标签一样，你可以使其可继承以递归应用，甚至可以将其放在根笔记上以全局应用于所有位置。

作为一个示例用例，假设你按如下方式收集某一年读过的书籍：

*   2022 年书籍
    *   尼尔·斯蒂芬森：Anathem，2008
    *   弗朗茨·卡夫卡：变形记，1915

现在，你可以为父笔记“2022 年书籍”分配标签 `#titleTemplate="[Author name]: [Book title], [Publication year]"`。

并且“2022 年书籍”的所有子笔记都将以初始标题“\[Author name\]: \[Book title\], \[Publication year\]”创建。这里没有人工智能，其理念只是提示你自己手动将信息片段填入笔记标题中。

## 由模板设置的标题

模板可以为其创建的笔记命名，无论这些笔记在何处创建。为此，请在模板笔记上添加 `#template:titleTemplate` 标签，例如在 _Meeting_ 模板上添加 `#template:titleTemplate="Meeting ${now.format('YYYY-MM-DD')}"`。

*   无论是显式选择模板，还是模板来自父级的 `~child:template`，它都适用。参见 <a class="reference-link" href="Templates.md">模板</a>。
*   它优先于父级的 `#titleTemplate`。用户手动输入的标题始终优先。
*   它可以从模板在树中的祖先继承（例如，一个包含多个模板的文件夹），在这种情况下，模板自身拥有的标签优先。从模板创建并后来标记为模板的笔记不会保留该模板的标题。
*   其值的计算方式与 `#titleTemplate` 相同，其中 `parentNote` 是新笔记的父级。

## 动态值

`#titleTemplate` 的值在笔记创建时作为 JavaScript 字符串进行求值，这意味着可以借助 JS 字符串插值和动态数据来丰富它。

注入的第二个变量是 `parentNote`，它提供对父级 [`FNote`](../Scripting/Script%20API/Frontend%20API.md) 的访问。

另请参见 <a class="reference-link" href="Templates.md">模板</a>，它提供了类似的功能，包括默认笔记内容。

### 示例

*   假设你收集服务器故障事件并编写一些笔记。它看起来像这样：
    *   事件
        *   2022-05-09：系统崩溃
        *   2022-05-15：备份延迟
    *   你可以通过为父笔记“事件”分配标签 `#titleTemplate="${now.format('YYYY-MM-DD')}: "` 来自动化日期分配。每当创建新的子笔记时，标题模板都会使用注入的 [now](https://day.js.org/docs/en/display/format) 对象进行求值。
*   要在新笔记的标题中使用父级的属性：`#titleTemplate="${parentNote.getLabelValue('authorName')}'s literary works"`
*   要镜像父笔记的标题：`${parentNote.title}`