# 搜索
<figure class="image"><img style="aspect-ratio:987/725;" src="Search_image.png" width="987" height="725"></figure>

笔记搜索使您能够通过搜索笔记标题、内容或[属性](../../Advanced%20Usage/Attributes.md)中的文本来查找笔记。您还可以选择保存搜索，这将创建一个特殊的搜索笔记，该笔记在导航树中可见，并将搜索结果作为子项包含在内。

## 访问搜索

*   从<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中，查找专用的搜索按钮。
*   要将搜索限制在某个笔记及其子笔记范围内，请从<a class="reference-link" href="../UI%20Elements/Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>中选择_从子树搜索_，或按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>。

## 交互

要搜索笔记，请点击工具栏上的放大镜图标或按键盘[快捷键](../Keyboard%20Shortcuts.md)。

1.  在_搜索字符串_字段中设置要搜索的文本。
    1.  除了按字面搜索词语外，还可以搜索笔记的属性或特性。
    2.  更多信息请参阅下面的示例。
2.  要将搜索限制在某个笔记及其子笔记范围内，请在_祖先_中设置一个笔记。
    1.  如果搜索是从[提升笔记](Note%20Hoisting.md)或[工作区](Workspaces.md)触发的，此值也会被预填充。
    2.  要搜索整个数据库，请将该值留空。
3.  要将搜索限制在仅几个层级（例如，在子笔记中查找但不查找子笔记的子笔记），请将_深度_字段设置为提供的值之一。
4.  除此之外，还可以通过_添加搜索选项_按钮配置搜索，如下文所述。
5.  按_搜索_触发搜索。结果显示在搜索配置窗格下方。
6.  _搜索并执行操作_按钮仅在至少添加了一个操作时才有意义（如下文所述）。
7.  _保存到笔记_将创建一个包含搜索配置的新笔记。更多信息请参阅<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>。

## 搜索选项

从添加搜索选项部分点击要应用的搜索选项。

*   对于每个选中的搜索选项，搜索配置将更新以显示该条目。每个搜索选项都有自己的配置。
*   要移除某个搜索选项，只需按右侧的 X 按钮。

可用的选项有：

1.  搜索脚本
    1.  此功能允许编写一个<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记，由其自行处理搜索。
2.  快速搜索
    1.  搜索不会查看笔记的内容，但仍会查看笔记标题和属性、关系（基于搜索查询）。
    2.  对于大型[数据库](../../Advanced%20Usage/Database.md)，此方法可以显著加快搜索速度。
3.  包含已归档
    1.  <a class="reference-link" href="../Notes/Archived%20Notes.md">已归档笔记</a>也将包含在结果中，否则它们将被忽略。
4.  排序方式
    1.  允许更改结果排序的标准，例如按创建日期或字母顺序排序，而不是按相关性（默认）。
    2.  还可以更改结果的顺序（升序或降序）。
5.  限制
    1.  将结果限制在给定的最大数量内。
    2.  当结果数量可能很高时，这很有帮助，代价是无法查看所有结果。
6.  调试
    1.  这将在服务器日志中打印额外信息（请参阅<a class="reference-link" href="../../Troubleshooting/Error%20logs.md">错误日志</a>），关于搜索表达式是如何解析的。
    2.  此功能在详细了解搜索功能后特别有用，可用于确定为什么复杂的搜索查询没有按预期工作。
7.  操作
    1.  除了搜索之外，还可以对搜索匹配到的笔记应用操作，例如添加标签或关系。
    2.  与其他搜索配置不同，这里可以多次应用相同的操作（即能够向笔记应用多个标签）。
    3.  给出的操作与<a class="reference-link" href="../../Advanced%20Usage/Bulk%20Actions.md">批量操作</a>中的操作相同，后者是在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中直接操作笔记的替代方案。
    4.  定义操作后，先按_搜索_检查匹配的笔记，然后按_搜索并执行操作_触发操作。

## 查看搜索结果

结果显示在搜索窗格下方，以**摘要卡片**列表的形式呈现。每张卡片显示笔记标题和匹配文本的简短摘录。

搜索还会高亮显示标题或内容中匹配的词语：

*   实线绿色下划线表示直接匹配；
*   虚线橙色下划线表示部分匹配（由模糊搜索匹配）。

此外：

*   **结果总数**始终显示，因此您可以立即判断查询的范围有多广。
*   **每页大小选择器**让您选择每页显示多少结果。您的选择会被记住并在设备间同步（存储在 `searchResultsPageSize` 选项中），因此您不必在每个设备上重新设置。
*   **点击结果**会打开笔记并直接跳转到第一个匹配项。笔记内查找栏会预先填充您的搜索词，因此您可以使用查找控件逐步浏览其余匹配项。
*   如果匹配项位于**折叠的部分**内（例如折叠的标题），该部分会自动展开，以便匹配项可见。

## 搜索如何匹配您的文本

最常见的困惑来源是 `=` 符号根据其出现位置表示两种_不同_的含义。阅读本节一次，搜索的其余部分就变得可预测了。

有三种匹配模式：

| 模式 | 如何触发 | 匹配内容 | 子字符串？ | 模糊（拼写错误）？ |
| --- | --- | --- | --- | --- |
| **默认** | 输入不带前缀的词语 | 整个词语_和_子字符串，位于标题、内容或属性中的任何位置，按相关性排序 | 是 | 是 |
| **精确全文** | 前导 `=`（例如 `=sync`） | 精确的整个词语或短语，忽略周围的标点符号 | 否 | 否 |
| **属性/特性相等** | 在 `#label=value` 或 `note.property=value` 子句中使用 `=` | _整个_属性或特性值，精确匹配 | 否 | 否 |

下面的每个示例都有 1:1 的自动化测试支持，因此文档不会与引擎产生偏差。

### 默认匹配（无前缀）

**规则：** 输入不带前缀的词语会查找标题、内容或属性中任何位置包含这些词语的笔记，可以是整个词语或子字符串。最接近的匹配排在最前面。

| 查询 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | 是（排名较高） | 包含精确词语 `sync` |
| `sync` | `synchronize the database now` | 是（排名较低） | `sync` 是 `synchronize` 的子字符串 |

### 使用 `=` 前缀的精确匹配

**规则：** 前导 `=` 将全文搜索切换为精确匹配。它仅查找整个词语或短语，忽略周围的标点符号，**没有**子字符串匹配，也**没有**模糊匹配。当普通搜索返回太多近似匹配时使用它。

| 查询 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `=sync` | `see (sync) mode` | 是 | `(sync)` 是完整词语 `sync`；标点符号被忽略 |
| `=sync` | `in sync, then continue` | 是 | `sync,` 是完整词语 `sync` |
| `=sync` | `he said "sync" out loud` | 是 | `"sync"` 是完整词语 `sync` |
| `=sync` | `synchronize the database now` | 否 | `=` 从不匹配子字符串 |
| `=sync` | `please send the file` | 否 | `=` 从不匹配拼写错误/模糊 |

要匹配精确的**短语**，请在 `=` 后加引号（单引号、双引号和反引号都有效）。短语必须作为连续词语出现，但词语之间或周围的标点符号会被忽略：

| 查询 | 示例笔记（标题或内容） | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `="project plan"` | 标题 `Project Plan` | 是 | 标题正是该短语 |
| `="project plan"` | `the (project plan) is ready to share` | 是 | 连续短语出现；标点符号被忽略 |
| `="project plan"` | `the plan for this project is late` | 否 | 词语存在但不连续 |

### 属性和特性相等（`=`、`!=`）

**规则：** 当 `=` 比较属性或特性时，如 `#label=value` 或 `note.title=value`，它是**严格的全值相等**：_整个_值必须等于您输入的内容，忽略大小写和变音符号。这**不是**词语匹配。`!=` 则相反。

下面的示例假设有四个笔记：_Austria_（`#capital=Vienna`）、_Somewhere_（`#capital=Vienna Austria`）、_Czech Republic_（`#capital=Prague`）和 _Switzerland_（`#capital=Zürich`）。

| 查询 | 示例标签值 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `#capital=Vienna` | `Vienna` | 是 | 整个值等于 `Vienna` |
| `#capital=Vienna` | `Vienna Austria` | 否 | 整个值是 `Vienna Austria`，而不是 `Vienna` |
| `#capital="Vienna Austria"` | `Vienna Austria` | 是 | 为多词值加引号以完整匹配 |
| `#capital=Zurich` | `Zürich` | 是 | 相等比较忽略变音符号 |
| `#capital!=Vienna` | `Prague` | 是 | `!=` 匹配所有不等于 `Vienna` 的值 |
| `#capital!=Vienna` | `Vienna` | 否 | `!=` 排除精确值 |

> **快速搜索会放宽此规则。** [快速搜索](Quick%20search.md)栏和自动补全将属性 `=` 视为"包含"，因此在那里输入 `#capital=Vienna` 也会匹配 `Vienna Austria`。此处描述的严格全值相等仅适用于完整搜索。

### 模糊运算符（`~=` 和 `~*`）

**规则：** 模糊运算符容忍拼写错误。`~=`（模糊等于）匹配与您的词接近的整词变体值。`~*`（模糊包含）在您的词作为片段或近似匹配出现在值中任何位置时匹配。两者都适用于笔记特性，如 `note.title` 和 `note.content`，以及标签（`#label`）。模糊运算符接受至少 3 个字符的词，但每个词容忍多少拼写错误取决于其长度——请参阅下面的_模糊容差_。

示例假设有一个标题为 `Books` 的笔记，带有标签 `#author=Tolkien`，以及一个内容为 `learn programming today` 的笔记。

| 查询 | 示例值 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `note.title ~= boks` | 标题 `Books` | 是 | 与 `books` 相差一个编辑 |
| `#author ~= tolkein` | 作者 `Tolkien` | 是 | `tolkein` 是 `tolkien` 的拼写错误 |
| `note.content ~* progr` | `learn programming today` | 是 | `progr` 是 `programming` 的片段 |
| `note.content ~* programing` | `learn programming today` | 是 | `programing` 与 `programming` 相差一个编辑 |

### 模糊容差

**规则：** 容忍多少拼写错误取决于搜索词的**长度**。短词必须精确匹配，因为一个编辑就足以将一个短词变成不相关的词；较长的词容忍更多。

| 词长度 | 允许的编辑数 |
| --- | --- |
| 1–3 个字符 | 0（仅精确） |
| 4–6 个字符 | 1 |
| 7+ 个字符 | 2 |

| 查询 | 词长度 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- | --- |
| `cat` | 3 | `a bright red car` | 否 | 4 个字符以下不允许编辑，因此 `cat` 无法匹配 `car` |
| `carr` | 4 | `a blue debit card` | 是 | 4–6 个字符的词允许 1 个编辑 |
| `ceck` | 4 | `the latest tech trends` | 否 | `ceck`→`tech` 需要 2 个编辑；此长度只允许 1 个 |
| `combinef` | 8 | `the values were combined together` | 是 | `combinef`→`combined` 是 1 个编辑；7+ 个字符允许最多 2 个 |

### 相关性排序

**规则：** 结果按匹配_程度_排序，而不仅仅是否匹配。精确的整词和短语匹配排在子字符串和模糊匹配之前，词语作为连续短语出现的笔记排在词语分散出现的笔记之前。

| 查询 | 排名较高 | 排名较低 | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | `synchronize the database now` | 精确词语优于子字符串 |
| `you and me` | `I like you and me as a phrase` | `the menu is here and you know it` | 连续短语优于分散词语 |

### 可搜索的内容

搜索查看的不仅仅是可见的正文文本。以下所有内容都被索引并可搜索：

*   笔记标题，
*   笔记正文内容，
*   标签和关系（[属性](../../Advanced%20Usage/Attributes.md)），
*   链接 URL 以及链接预览的标题/描述，
*   笔记引用链接指向的笔记的标题。

最后一点最不明显：如果一个笔记的唯一内容是指向另一个笔记的引用链接，搜索那个另一个笔记的**标题**仍然能找到该链接笔记。

| 查询 | 设置 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `special topic` | 一个笔记，其唯一内容是指向标题为 `Special Topic` 的笔记的引用链接 | 是，且被链接的目标排在最前面 | 目标的标题被索引到链接笔记的可搜索文本中 |
| `special` | 同一个笔记（仅是指向 `Special Topic` 的引用链接） | 是，目标标题中的一个词就足够了 | 被索引的标题像正文一样被规范化，因此即使一个小写词也能匹配 |
| `zurich` | 一个笔记，其唯一内容是指向标题为 `Zürich` 的笔记的引用链接 | 是 | 被索引的标题的重音符号被规范化，因此普通形式能匹配带重音的标题 |

### 变音符号

**规则：** 两边的重音符号都被规范化，因此带重音的词语和其普通形式可以相互匹配。

| 查询 | 示例笔记内容 | 匹配？ |
| --- | --- | --- |
| `ktory` | `slovo ktorý znamena nieco` | 是 |
| `ktorý` | `the word ktory appears here` | 是 |

### 正则表达式（`%=`）

**规则：** `%=` 运算符将属性或标签值与正则表达式进行匹配。

| 查询 | 示例笔记内容 | 匹配？ |
| --- | --- | --- |
| `note.content %= 'colou?r'` | `my favorite color of all` | 是 |
| `note.content %= 'colou?r'` | `my favourite colour of all` | 是 |

### 简单笔记搜索示例

*   `rings tolkien`：全文搜索，查找同时包含 "rings" 和 "tolkien" 的笔记。
*   `"The Lord of the Rings" Tolkien`：全文搜索，其中 "The Lord of the Rings" 必须精确匹配。
*   `note.content *=* rings OR note.content *=* tolkien`：查找内容中包含 "rings" 或 "tolkien" 的笔记。
*   `towers #book`：结合全文搜索和属性搜索，查找包含 "towers" 且具有 "book" 标签的笔记。
*   `towers #book or #author`：搜索包含 "towers" 且具有 "book" 或 "author" 标签的笔记。
*   `towers #!book`：搜索包含 "towers" 且不具有 "book" 标签的笔记。
*   `#book #publicationYear = 1954`：查找具有 "book" 标签且 "publicationYear" 设置为 1954 的笔记。
*   `#genre *=* fan`：查找 "genre" 标签包含子字符串 "fan" 的笔记。其他运算符包括 `*=*` 表示"包含"，`=*` 表示"开头是"，`*=` 表示"结尾是"，`!=` 表示"不等于"。
*   `#book #publicationYear >= 1950 #publicationYear < 1960`：使用数值运算符查找所有 1950 年代出版的书籍。
*   `#dateNote >= TODAY-30`：查找 "dateNote" 标签在过去 30 天内的笔记。支持的日期值包括 NOW +- 秒、TODAY +- 天、MONTH +- 月、YEAR +- 年。
*   `~author.title *=* Tolkien`：查找与标题包含 "Tolkien" 的作者相关的笔记。
*   `#publicationYear %= '19[0-9]{2}'`：使用 '%=' 运算符匹配正则表达式（regex）。此功能自 Trilium 0.52 起可用。
*   `note.content %= '\\d{2}:\\d{2} (PM|AM)'`：查找提到时间的笔记。正则表达式中的反斜杠必须转义。

### 高级用例

*   `~author.relations.son.title = 'Christopher Tolkien'`：搜索具有 "author" 关系指向一个具有 "son" 关系指向 "Christopher Tolkien" 的笔记的笔记。这可以用以下笔记结构建模：
    *   Books
        *   Lord of the Rings
            *   标签："book"
            *   关系："author" 指向 "J. R. R. Tolkien" 笔记
    *   People
        *   J. R. R. Tolkien
            *   关系："son" 指向 "Christopher Tolkien" 笔记
            *   Christopher Tolkien
*   `~author.title *= Tolkien OR (#publicationDate >= 1954 AND #publicationDate <= 1960)`：使用布尔表达式和括号对表达式进行分组。请注意，以括号开头的表达式需要前置"表达式分隔符"（# 或 ~）。
*   `note.parents.title = 'Books'`：查找父笔记名为 "Books" 的笔记。
*   `note.parents.parents.title = 'Books'`：查找祖父笔记名为 "Books" 的笔记。
*   `note.ancestors.title = 'Books'`：查找祖先笔记名为 "Books" 的笔记。
*   `note.children.title = 'sub-note'`：查找子笔记名为 "sub-note" 的笔记。

### 使用笔记特性搜索

笔记具有可用于搜索的特性，例如 `noteId`、`dateModified`、`dateCreated`、`isProtected`、`type`、`title`、`text`、`content`、`rawContent`、`ownedLabelCount`、`labelCount`、`ownedRelationCount`、`relationCount`、`ownedRelationCountIncludingLinks`、`relationCountIncludingLinks`、`ownedAttributeCount`、`attributeCount`、`targetRelationCount`、`targetRelationCountIncludingLinks`、`parentCount`、`childrenCount`、`isArchived`、`contentSize`、`noteSize` 和 `revisionCount`。

这些特性可以通过 `note.` 前缀访问，例如 `note.type = code AND note.mime = 'application/json'`。

### 排序和限制

```
#author=Tolkien orderBy #publicationDate desc, note.title limit 10
```

此示例将：

1.  查找作者标签为 "Tolkien" 的笔记。
2.  按 `publicationDate` 降序排列结果。
3.  如果出版日期相同，则使用 `note.title` 作为次要排序。
4.  将结果限制为前 10 个笔记。

### 否定

某些查询只能用否定来表达：

```
#book AND not(note.ancestors.title = 'Tolkien')
```

此查询查找所有不在 "Tolkien" 子树中的书籍笔记。

## 渐进式搜索策略

Trilium 使用渐进式搜索策略，先执行精确匹配，然后在需要时添加模糊匹配。

### 渐进式搜索的工作原理

1.  **阶段 1 - 精确匹配**：当您搜索时，Trilium 首先查找搜索词的精确匹配。这处理了绝大多数搜索（90%+），并几乎即时返回结果。
2.  **阶段 2 - 模糊回退**：如果阶段 1 没有找到足够的高质量结果（少于 5 个具有良好相关性分数的结果），Trilium 会自动添加模糊匹配以查找有拼写错误或拼写变体的结果。
3.  **结果排序**：精确匹配始终出现在模糊匹配之前，无论个别分数如何。这确保当您搜索 "project" 时，包含精确词语 "project" 的笔记会出现在包含类似词语如 "projects" 或 "projection" 的笔记之前。

### 渐进式搜索行为

*   **速度**：大多数搜索仅使用精确匹配完成
*   **排序**：精确匹配出现在模糊匹配之前
*   **回退**：当精确匹配返回少于 5 个结果时激活模糊匹配
*   **标识**：结果会指示它们是精确匹配还是模糊匹配

### 搜索性能

搜索系统规格：

*   内容大小限制：每个笔记 10MB（之前为 50KB）
*   模糊匹配的编辑距离计算
*   快速搜索中的无限滚动

## 底层原理

### 标签和关系快捷方式

按标签搜索的"完整"语法是：

```
note.labels.publicationYear = 1954
```

对于关系：

```
note.relations.author.title *=* Tolkien
```

然而，常见的标签和关系搜索有快捷语法：

```
#publicationYear = 1954
~author.title *=* Tolkien
```

### 分隔全文和属性部分

搜索语法允许将全文搜索与基于属性的搜索结合。例如，`tolkien #book` 包含：

1.  全文标记 - `tolkien`
2.  属性表达式 - `#book`

Trilium 通过查找表示属性和特性的某些特殊字符或词语（例如 #、~、note.）来检测全文搜索与属性/特性搜索之间的分隔。如果您需要在全文搜索中包含这些内容，请用反斜杠转义它们，以便它们作为常规文本处理：

```
"note.txt" 
\#hash 
#myLabel = 'Say "Hello World"'
```

### 转义特殊字符

特殊字符可以用引号括起来或用反斜杠转义，以便在全文搜索中使用：

```
"note.txt"
\#hash
#myLabel = 'Say "Hello World"'
```

支持三种引号：单引号、双引号和反引号。

### 类型强制转换

标签值在技术上是字符串，但可以为数值比较进行强制转换：

```
note.dateCreated =* '2019-05'
```

这会查找 2019 年 5 月创建的笔记。像 `#publicationYear >= 1960` 这样的数值运算符会将字符串值转换为数字进行比较。

## 从 URL 自动触发搜索

您可以通过在 URL 中包含搜索[URL 编码](https://meyerweb.com/eric/tools/dencoder/)字符串来打开 Trilium 并自动触发搜索：

`http://localhost:8080/#?searchString=abc`

## 搜索配置

### 参数

| 参数 | 值 | 描述 |
| --- | --- | --- |
| `MIN_FUZZY_TOKEN_LENGTH` | 3 | `~=` 和 `~*` 运算符接受的最小字符数 |
| `MAX_EDIT_DISTANCE` | 2 | 字符更改的上限，仅 7+ 个字符的词可达到；较短的词允许更少。请参阅上面的_模糊容差_部分 |
| `RESULT_SUFFICIENCY_THRESHOLD` | 5 | 模糊回退前的最小精确结果数 |
| `MAX_CONTENT_SIZE` | 10MB | 搜索处理的笔记内容最大大小 |

### 限制

*   被搜索的笔记内容限制为每个笔记 10MB，以防止性能问题
*   超过此限制的笔记仍会包含在标题和属性搜索中
*   3 个字符或更少的词精确匹配；拼写错误容忍从 4 个字符开始