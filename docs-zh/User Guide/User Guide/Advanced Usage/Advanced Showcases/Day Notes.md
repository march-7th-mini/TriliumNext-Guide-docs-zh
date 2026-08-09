# 日记笔记

笔记记录中一个常见的模式是，大量笔记会围绕某个特定日期展开——例如，你有一些需要在特定日期完成的任务，你有特定日期的会议记录，你有自己的想法等等，所有这些都围绕着它们发生的日期。因此，创建一个“每日工作区”来集中管理特定日期的所有相关笔记是很有意义的。

为此，Trilium 提供了“日记笔记”的概念。Trilium 会半自动地为每一天生成一条笔记。你可以在这条笔记下保存所有相关的笔记。

选中一个已有的日记笔记，菜单栏会显示一个日历小组件。选择任意一天即可为该天创建笔记。

![](1_Day%20Notes_image.png)

这种模式之所以有效，还因为 [克隆笔记](../../Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md) 功能——笔记可以出现在笔记树的多个位置，因此除了出现在日记笔记下，它还可以归类到其他笔记中。

## 演示

![](Day%20Notes_image.png)

你可以看到日记笔记的结构出现在“日志”笔记下——有一个针对整个 2025 年的笔记，在其下方，有“03 - 三月”，其中包含“09 - 星期一”。这就是我们的“日记笔记”，其内容包含一些文本，并且还有一些子笔记（其中一些来自[任务管理器](Task%20Manager.md)）。

你还可以注意到这个日记笔记有[提升属性](../Attributes/Promoted%20Attributes.md) “体重”，你可以在其中跟踪你的每日体重。这些数据随后会用于[体重跟踪器](Weight%20Tracker.md)。

## 周笔记和季度笔记

周笔记和季度笔记默认是禁用的，因为对某些人来说可能太多了。要启用它们，你需要在根日历笔记上设置 `#enableWeekNote` 和 `#enableQuarterNote` 属性，该根日历笔记通过 `#calendarRoot` 标签标识。周笔记受一年中第一周的选项影响。请注意，如果你已经有了一些周笔记，它不会自动更改现有的周笔记，并且可能会导致一些重复。

## 模板

Trilium 提供了[模板](../Templates.md)功能，它可以与日记笔记一起使用。

你可以在日志的根节点（通过 `#calendarRoot` 标签标识）上定义以下关系之一：

*   yearTemplate
*   quarterTemplate (如果设置了 `#enableQuarterNote`)
*   monthTemplate
*   weekTemplate (如果设置了 `#enableWeekNote`)
*   dateTemplate

所有这些都是关系。当 Trilium 为年、月或日期创建新笔记时，它会查看根节点并将相应的 `~template` 关系附加到新创建的角色上。使用此功能，你可以例如创建你的每日模板，其中包含用于每日例程的复选框等。

### 从旧模板用法迁移

如果你在 v0.93.0 版本之前一直在使用日志，之前可能使用的模板模式是 `~child:template=`。
要过渡到新系统：

1.  在日历根笔记中设置新的模板模式。
2.  使用[批量操作](../Bulk%20Actions.md)从日志（日历根节点）下的所有笔记中移除 `child:template` 和 `child:child:template`。
3.  确保所有旧的模板模式都被完全移除，以防止与新设置冲突。

## 命名模式

你可以通过在根日历笔记（通过 `#calendarRoot` 标签标识）上定义 `#datePattern`、`#weekPattern`、`#monthPattern`、`#quarterPattern` 和 `#yearPattern` 属性来自定义生成的日志笔记的标题。命名模式的替换遵循向上兼容性——每个级别可以使用自身及其以上所有级别的替换。例如，`#monthPattern` 可以使用月份、季度和年份的替换，而 `#weekPattern` 可以使用周、月、季度和年份的替换。但不能在 `#monthPattern` 中使用周替换。

### 日期模式

你可以通过在根日历笔记（通过 `#calendarRoot` 标签标识）上定义 `#datePattern` 属性来自定义生成的日期笔记的标题。以下是可能的值：

*   `{isoDate}` 生成 ISO 8061 格式的日期（例如 2025 年 3 月 9 日为 "2025-03-09"）
*   `{dateNumber}` 生成一个数字，例如当月的第 9 天为 `9`，当月的第 11 天为 `11`
*   `{dateNumberPadded}` 生成一个数字，例如当月的第 9 天为 `09`，当月的第 11 天为 `11`
*   `{ordinal}` 被替换为序数日期（例如 1st, 2nd, 3rd）等。
*   `{weekDay}` 生成完整的星期名称（例如 `Monday`）
*   `{weekDay3}` 被替换为星期的前 3 个字母，例如 Mon, Tue 等。
*   `{weekDay2}` 被替换为星期的前 2 个字母，例如 Mo, Tu 等。

默认值是 `{dateNumberPadded} - {weekDay}`

### 周模式

你也可以通过根日历笔记上的 `#weekPattern` 属性来自定义生成的周笔记的标题。选项有：

*   `{weekNumber}` 生成一个数字，例如一年中的第 9 周为 `9`，一年中的第 11 周为 `11`
*   `{weekNumberPadded}` 生成一个数字，例如一年中的第 9 周为 `09`，一年中的第 11 周为 `11`
*   `{shortWeek}` 生成一个短的周字符串，例如一年中的第 9 周为 `W9`，一年中的第 11 周为 `W11`
*   `{shortWeek3}` 生成一个短的周字符串，例如一年中的第 9 周为 `W09`，一年中的第 11 周为 `W11`

默认值是 `Week {weekNumber}`

### 月份模式

你也可以通过根日历笔记上的 `#monthPattern` 属性来自定义生成的月份笔记的标题。选项有：

*   `{isoMonth}` 生成 ISO 8061 格式的月份（例如 2025 年 3 月为 "2025-03"）
*   `{monthNumber}` 生成一个数字，例如九月为 `9`，十一月为 `11`
*   `{monthNumberPadded}` 生成一个数字，例如九月为 `09`，十一月为 `11`
*   `{month}` 生成完整的月份名称（例如 `September` 或 `October`）
*   `{shortMonth3}` 被替换为月份的前 3 个字母，例如 Jan, Feb 等。
*   `{shortMonth4}` 被替换为月份的前 4 个字母，例如 Sept, Octo 等。

默认值是 `{monthNumberPadded} - {month}`

### 季度模式

你也可以通过根日历笔记上的 `#quarterPattern` 属性来自定义生成的季度笔记的标题。选项有：

*   `{quarterNumber}` 生成一个数字，例如一年中的第一季度为 `1`
*   `{shortQuarter}` 生成一个短的季度字符串，例如一年中的第一季度为 `Q1`

默认值是 `Quarter {quarterNumber}`

### 年份模式

你也可以通过根日历笔记上的 `#yearPattern` 属性来自定义生成的年份笔记的标题。选项有：

*   `{year}` 生成完整的年份（例如 `2025`）

默认值是 `{year}`

## 实现

Trilium 以[后端脚本 API](https://triliumnext.github.io/Notes/backend_api/BackendScriptApi.html) 的形式为日记笔记提供了一些特殊支持——例如，参见 getDayNote() 函数。

日（以及年、月）笔记是带有一个标签创建的——例如 `#dateNote="2025-03-09"`，这可以被其他脚本用来向日记笔记添加新笔记等。