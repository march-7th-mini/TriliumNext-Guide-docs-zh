# 笔记排序

Trilium 可以通过 _按…排序_ 对话框对笔记的子笔记进行一次排序，也可以使用 `#sorted` 标签让它们保持永久排序。两者使用相同的排序条件：标题、创建或修改日期，或子笔记上某个标签的值，并且两者都可以将其中几项组合成排序层级。

## 使用对话框进行一次排序

要对某个笔记的子笔记进行一次排序，请在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中右键单击它并选择 _按…排序_，或选中它并按 <kbd>Alt</kbd>+<kbd>S</kbd>。该顺序仅应用于现有的子笔记；之后添加的笔记会放置在它们被创建的位置。

该对话框由以下部分组成：

*   _排序条件_，一个层级列表。每个层级按 _标题_、_创建日期_、_修改日期_ 或 _标签_（后跟标签名称）、_升序_ 或 _降序_ 排序。
    *   要按多个条件排序，请选择 _添加层级_。第一个层级决定顺序；下一个层级只在前面的层级判定相等的笔记之间做决定（见下文 _排序层级_）。
    *   要更改层级的顺序，请使用 <span class="tn-icon bx bx-up-arrow-alt"></span> 和 <span class="tn-icon bx bx-down-arrow-alt"></span> 按钮。要移除某个层级，请使用 <span class="tn-icon bx bx-x"></span> 按钮。
*   _文件夹排在顶部_，将自身拥有子笔记的笔记排在其他笔记之前。当第一个层级为降序时，它们会被放置在底部。
*   _自然排序_，按语言规则比较数字和字符（见下文 _值如何比较_）。_自然排序语言_ 设置语言代码，例如中文使用 `zh-CN`。

带有 `#top` 或 `#bottom` 的笔记会保持在顶部或底部，与自动排序相同（见下文 _将笔记固定到顶部或底部_）。

## 保持子笔记有序

要保持某个笔记的子笔记有序，请为其添加 `#sorted` [标签](../../Advanced%20Usage/Attributes/Labels.md)。每当添加子笔记或子笔记发生变化，以及排序标签发生变化时，Trilium 都会重新对其子笔记进行排序。

| 标签 | 描述 |
| --- | --- |
| `#sorted` | 保持子笔记有序。没有值时，按标题排序；有值时，按其列出的层级排序（见下文 _排序层级_）。`#sorted=off` 关闭排序。 |
| `#sortDirection` | `asc`（默认）或 `desc`。每个未指定自身方向的层级的方向。 |
| `#sortFoldersFirst` | 将自身拥有子笔记的笔记排在其他笔记之前，当 `#sortDirection` 为 `desc` 时则排在其后。 |
| `#sortNatural` | 按数值而非逐字符比较数字，因此 2 排在 10 之前。 |
| `#sortLocale` | `#sortNatural` 的语言代码，例如 `zh-CN` 或 `de`。 |
| `#top` | 在子笔记上：使其保持在已排序父笔记的顶部。 |
| `#bottom` | 在子笔记上：使其保持在已排序父笔记的底部。 |

这些标签应用于携带它们的笔记，并且当设为[可继承](../../Advanced%20Usage/Attributes/Attribute%20Inheritance.md)时，也应用于其下的每个笔记，因此单个 `#sorted(inheritable)` 即可对整个子树排序。从带有 `#sorted` 的[模板](../../Advanced%20Usage/Templates.md)创建的笔记也会保持其子笔记有序。要排除此类子树的一部分，请为必须保持手动顺序的子笔记添加 `#sorted=off`；要同时排除其下的所有内容，请将该标签也设为可继承。

## 排序层级

`#sorted` 的值是一个以逗号分隔的层级列表，写法类似于[搜索](../Navigation/Search.md)的 `orderBy`。每个层级是以下之一：

*   子笔记上的标签，以 `#` 书写，例如 `#priority`。
*   `title`、`dateCreated` 和 `dateModified` 属性之一，不带 `#` 书写。
*   `folders`，只有自身拥有子笔记的笔记才具有（见下文 _分组_）。

层级后面可以跟 `asc` 或 `desc` 来设置其方向；否则它遵循 `#sortDirection`。

子笔记按第一个层级排序。在该层级上相等的笔记按第二个层级排序，依此类推。在每个层级上都相等的笔记按标题排序，方向遵循 `#sortDirection`。

不具有某层级标签的子笔记会被放置在所有具有该标签的子笔记之后，无论该层级的方向如何。在两个都不具有该标签的笔记之间，由下一个层级决定。

例如，在具有以下子笔记的父笔记上设置 `#sorted="#priority desc, #dueDate"`：

| 子笔记 | 标签 |
| --- | --- |
| Book report | `#priority=2` `#dueDate=2026-11-01` |
| Groceries | `#priority=1` |
| Taxes | `#priority=2` `#dueDate=2026-10-25` |
| Ideas | 无 |

将它们排序为 _Taxes_、_Book report_、_Groceries_、_Ideas_。最高优先级排在最前；_Taxes_ 和 _Book report_ 共享该优先级，因此由较早的截止日期在它们之间做决定。_Ideas_ 没有优先级，排在最后。

不带 `#` 的单个名称值按旧版本的方式读取：`title`、`dateCreated` 或 `dateModified` 是属性，任何其他名称是标签，因此 `#sorted=myOrder` 按子笔记的 `#myOrder` 标签排序。

> [!WARNING]
> 自 v0.107.0 起，`#sorted` 值中具有多个层级或带有方向的标签必须用 `#` 书写。在 v0.106.0 中，名称是裸写的，如 `#sorted="priority desc, dueDate"`；这样的值现在会将两个名称都读取为不存在的属性，笔记会回退到按标题排序。在每个标签名称前添加 `#` 即可恢复。

## 使用 `first` 和 `last` 进行分组

标签后跟 `first` 或 `last` 时不按标签的值排序：它将具有该标签（任意值）的子笔记放置在其他笔记之前或之后。随后的层级则在每个组内排序。分组会忽略 `#sortDirection`。

例如，在具有以下子笔记的父笔记上设置 `#sorted="#archived last, #priority desc"`：

| 子笔记 | 标签 |
| --- | --- |
| Old project | `#archived` `#priority=3` |
| Draft | `#priority=1` |
| Launch | `#priority=3` |
| Meeting notes | 无 |

将它们排序为 _Launch_、_Draft_、_Meeting notes_、_Old project_。[已归档笔记](Archived%20Notes.md)尽管优先级很高，仍排在其他所有笔记之下，其余笔记按优先级排序。

`folders first` 和 `folders last` 对自身拥有子笔记的笔记进行分组。不带 `first` 或 `last` 的 `folders` 层级也会将它们排在最前，无论方向如何。`#sortFoldersFirst` 是 `folders first` 层级的快捷方式；当 `#sorted` 已包含 `folders` 时它不起作用。

## 将笔记固定到顶部或底部

带有 `#top` 的子笔记保持在已排序父笔记的顶部，带有 `#bottom` 的子笔记保持在底部，无论 `#sorted` 的层级如何规定。当多个笔记带有 `#top` 时，它们按标签的值排序，因此 `#top=1` 排在 `#top=2` 之前，不带值的 `#top` 排在最前。`#bottom` 则相反：最后的笔记是 `#bottom=2`，然后是 `#bottom=1`，最后是不带值的 `#bottom`。

`#sortFoldersFirst` 将文件夹紧接在 `#top` 笔记之后放置。

要在组内而非整个列表中固定笔记，请在 `#sorted` 中于其适用位置命名 `#top` 和 `#bottom`。例如：

*   `#sorted="#archived last, #top first, #bottom last, title"` 将已归档笔记保持在所有其他笔记之下，包括带有 `#bottom` 的笔记。`#top` 和 `#bottom` 随后分别在已归档组和非已归档组内应用。
*   `#sorted="#archived last, #top first, #bottom last, folders first, title"` 还会在每个组内将文件夹排在最前。`#sortFoldersFirst` 也是如此：其 `folders first` 层级紧接在 `#top` 和 `#bottom` 的最后一个之后。
*   以 `first` 或 `last` 书写时，`#top` 和 `#bottom` 会忽略其值。要按值对多个固定笔记排序，请在其后添加一个层级，例如 `#top first, #top, #bottom last, #bottom desc`。

## 值如何比较

*   值按文本逐字符比较，不区分字母大小写。`YYYY-MM-DD` 形式的日期能正确排序，但数字不能：`"10"` 排在 `"2"` 之前。要么用零填充数字（`02`、`10`），要么启用 `#sortNatural`。
*   使用 `#sortNatural` 时，数字按其值比较，比较遵循由 `#sortLocale`（或默认语言）设置的语言规则，该规则也会忽略重音符号。
*   笔记的标题包含其<a class="reference-link" href="Cloning%20Notes/Branch%20prefix.md">分支前缀</a>（如果它在此父笔记中具有该前缀），形式为 `prefix - title`。
*   不带值的标签仍视为存在：它排在不存在该标签的笔记之前，并且在具有该标签的笔记中，作为最小值。