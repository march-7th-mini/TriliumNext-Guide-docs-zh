# 日记笔记

笔记记录中一个常见的模式是，许多笔记都会围绕某个特定日期展开——例如，你有一些需要在特定日期完成的任务，有某个日期的会议纪要，有你的想法等等，它们都围绕着发生的那个日期。因此，创建一个特定的"每日工作区"来集中管理某个日期的所有相关笔记是很有意义的。

为此，Trilium 提供了"日记笔记"的概念。Trilium 会为每一天半自动地生成一篇笔记。在这篇笔记下，你可以保存所有相关的笔记。

选择一篇已有的日记笔记，菜单栏中会显示一个日历小组件。选择任意一天即可为该天创建笔记。

![](1_Day%20Notes_image.png)

这种模式之所以好用，还得益于[克隆笔记](../../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)功能——笔记可以出现在笔记树的多个位置，因此除了出现在日记笔记下，它还可以被归类到其他笔记中。

## 演示

![](Day%20Notes_image.png)

你可以看到日记笔记的结构出现在"Journal"笔记下——有一篇涵盖 2025 年全年的笔记，其下有"03 - March"，其中又包含"09 - Monday"。这就是我们的"日记笔记"，它的内容中有一些文本，还有一些子笔记（其中一些来自[任务管理器](Task%20Manager.md)）。

你还可以注意到这篇日记笔记有一个[提升属性](../Attributes/Promoted%20Attributes.md)"weight"，你可以用它来追踪每日体重。这些数据随后会被[体重追踪器](Weight%20Tracker.md)使用。

## 已编辑的笔记

当打开一篇日记笔记时，<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Title.md">标题</a>下方会出现一个可折叠区域，显示当天编辑过的笔记。

## 周笔记和季度笔记

周笔记和季度笔记默认是禁用的，因为对某些人来说可能过于繁杂。要启用它们，你需要在日历根笔记（通过 `#calendarRoot` 标签标识）上设置 `#enableWeekNote` 和 `#enableQuarterNote` 属性。周笔记受"一年的第一周"选项影响。请注意，如果你已经创建了一些周笔记，它不会自动更改现有的周笔记，可能会导致一些重复。

## 模板

Trilium 提供了[模板](../Templates.md)功能，它可以与日记笔记一起使用。

你可以在日记的根笔记（通过 `#calendarRoot` 标签标识）上定义以下关系之一：

*   yearTemplate
*   quarterTemplate（如果设置了 `#enableQuarterNote`）
*   monthTemplate
*   weekTemplate（如果设置了 `#enableWeekNote`）
*   dateTemplate

所有这些都是关系。当 Trilium 为年、月或日期创建新笔记时，它会查看根笔记，并将相应的 `~template` 关系附加到新创建的笔记上。利用这一点，你可以例如创建带有每日例行事项复选框的每日模板等。

### 从旧模板用法迁移

如果你在 v0.93.0 版本之前一直在使用 Journal，之前使用的模板模式很可能是 `~child:template=`。
要迁移到新系统：

1.  在日历根笔记中设置新的模板模式。
2.  使用[批量操作](../Bulk%20Actions.md)从 Journal（日历根笔记）下的所有笔记中移除 `child:template` 和 `child:child:template`。
3.  确保所有旧的模板模式都被完全移除，以防止与新设置产生冲突。

## 命名模式

你可以通过在日历根笔记（通过 `#calendarRoot` 标签标识）上定义 `#datePattern`、`#weekPattern`、`#monthPattern`、`#quarterPattern` 和 `#yearPattern` 属性来自定义生成的日记笔记的标题。命名模式的替换遵循层级兼容规则——每一层级可以使用自身及所有上层级的替换项。例如，`#monthPattern` 可以使用月、季度和年的替换项，而 `#weekPattern` 可以使用周、月、季度和年的替换项。但不能在 `#monthPattern` 中使用周的替换项。

### 日期模式

你可以通过在日历根笔记（通过 `#calendarRoot` 标签标识）上定义 `#datePattern` 属性来自定义生成的日期笔记的标题。以下是可选值：

*   `{isoDate}` 生成 ISO 8061 格式的日期（例如 2025 年 3 月 9 日为 "2025-03-09"）
*   `{dateNumber}` 生成一个数字，例如月份的第 9 天为 `9`，第 11 天为 `11`
*   `{dateNumberPadded}` 生成一个补零的数字，例如月份的第 9 天为 `09`，第 11 天为 `11`
*   `{ordinal}` 替换为序数日期（例如 1st、2nd、3rd）等
*   `{weekDay}` 生成完整的星期名称（例如 `Monday`）
*   `{weekDay3}` 替换为星期的前 3 个字母，例如 Mon、Tue 等
*   `{weekDay2}` 替换为星期的前 2 个字母，例如 Mo、Tu 等

默认值为 `{dateNumberPadded} - {weekDay}`

### 周模式

你也可以通过日历根笔记上的 `#weekPattern` 属性来自定义生成的周笔记的标题。选项包括：

*   `{weekNumber}` 生成一个数字，例如一年中的第 9 周为 `9`，第 11 周为 `11`
*   `{weekNumberPadded}` 生成一个补零的数字，例如一年中的第 9 周为 `09`，第 11 周为 `11`
*   `{shortWeek}` 生成简短的周字符串，例如一年中的第 9 周为 `W9`，第 11 周为 `W11`
*   `{shortWeek3}` 生成简短的周字符串，例如一年中的第 9 周为 `W09`，第 11 周为 `W11`

默认值为 `Week {weekNumber}`

### 月模式

你也可以通过日历根笔记上的 `#monthPattern` 属性来自定义生成的月笔记的标题。选项包括：

*   `{isoMonth}` 生成 ISO 8061 格式的月份（例如 2025 年 3 月为 "2025-03"）
*   `{monthNumber}` 生成一个数字，例如九月为 `9`，十一月为 `11`
*   `{monthNumberPadded}` 生成一个补零的数字，例如九月为 `09`，十一月为 `11`
*   `{month}` 生成完整的月份名称（例如 `September` 或 `October`）
*   `{shortMonth3}` 替换为月份的前 3 个字母，例如 Jan、Feb 等
*   `{shortMonth4}` 替换为月份的前 4 个字母，例如 Sept、Octo 等

默认值为 `{monthNumberPadded} - {month}`

### 季度模式

你也可以通过日历根笔记上的 `#quarterPattern` 属性来自定义生成的季度笔记的标题。选项包括：

*   `{quarterNumber}` 生成一个数字，例如一年中的第 1 季度为 `1`
*   `{shortQuarter}` 生成简短的季度字符串，例如一年中的第 1 季度为 `Q1`

默认值为 `Quarter {quarterNumber}`

### 年模式

你也可以通过日历根笔记上的 `#yearPattern` 属性来自定义生成的年笔记的标题。选项包括：

*   `{year}` 生成完整的年份（例如 `2025`）

默认值为 `{year}`

## 实现

Trilium 通过[后端脚本 API](https://triliumnext.github.io/Notes/backend_api/BackendScriptApi.html) 对日记笔记提供了一些特殊支持——例如参见 getDayNote() 函数。

日（以及年、月）笔记创建时会带有一个标签——例如 `#dateNote="2025-03-09"`，其他脚本可以用它来向日记笔记添加新笔记等。