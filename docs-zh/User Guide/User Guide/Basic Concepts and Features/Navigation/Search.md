# 搜索
<figure class="image"><img style="aspect-ratio:987/725;" src="Search_image.png" width="987" height="725"></figure>

笔记搜索使您能够通过在笔记的标题、内容或[属性](../../Advanced%20Usage/Attributes.md)中搜索文本来查找笔记。您还可以选择保存搜索，这将创建一个特殊的搜索笔记，该笔记在导航树中可见，并将搜索结果作为子项包含在内。

## 访问搜索

*   在<a class="reference-link" href="../UI%20Elements/Launch%20Bar.md">启动栏</a>中，查找专用的搜索按钮。
*   要将搜索限制在某条笔记及其子笔记中，请从<a class="reference-link" href="../UI%20Elements/Note%20Tree/Note%20tree%20contextual%20menu.md">笔记树上下文菜单</a>中选择 _从子树中搜索_，或按 <kbd spellcheck="false">Ctrl</kbd>+<kbd spellcheck="false">Shift</kbd>+<kbd spellcheck="false">S</kbd>。

## 交互

要搜索笔记，请点击工具栏上的放大镜图标或按下键盘[快捷键](../Keyboard%20Shortcuts.md)。

1.  在 _搜索字符串_ 字段中设置要搜索的文本。
    1.  除了按字面意思搜索单词外，还可以搜索笔记的属性或特性。
    2.  有关更多信息，请参见下面的示例。
2.  要将搜索限制在某条笔记及其子笔记中，请在 _祖先_ 中设置一条笔记。
    1.  如果从[提升笔记](Note%20Hoisting.md)或[工作区](Workspaces.md)触发搜索，此值也会被预填。
    2.  要搜索整个数据库，请将该值留空。
3.  要将搜索限制在几个层级内（例如，查找子笔记但不查找子-子笔记），请将 _深度_ 字段设置为提供的值之一。
4.  此外，可以通过 _添加搜索选项_ 按钮配置搜索，如下一节所述。
5.  按 _搜索_ 触发搜索。结果显示在搜索配置面板下方。
6.  _搜索并执行操作_ 按钮仅在至少添加了一个操作时相关（如下一节所述）。
7.  _保存到笔记_ 将使用搜索配置创建一条新笔记。有关更多信息，请参见<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">已保存的搜索</a>。

## 搜索选项

从“添加搜索选项”部分点击要应用的搜索选项。

*   对于每个选中的搜索选项，搜索配置将更新以显示输入项。每个搜索选项都有自己的配置。
*   要移除某个搜索选项，只需按一下其右侧的 X 按钮。

可用的选项有：

1.  搜索脚本
    1.  此功能允许编写一个<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>笔记来自行处理搜索。
2.  快速搜索
    1.  搜索不会查看笔记的内容，但仍会查看笔记标题、属性和关系（基于搜索查询）。
    2.  对于大型[数据库](../../Advanced%20Usage/Database.md)，此方法可以大大加快搜索速度。
3.  包含已归档
    1.  <a class="reference-link" href="../Notes/Archived%20Notes.md">已归档笔记</a>也会包含在结果中，否则它们将被忽略。
4.  排序方式
    1.  允许更改结果排序的标准，例如按创建日期或字母顺序排序，而不是按相关性（默认）排序。
    2.  也可以更改结果的顺序（升序或降序）。
5.  限制
    1.  将结果限制在给定的最大值内。
    2.  如果结果数量可能很大，这会有帮助，但代价是无法查看所有结果。
6.  调试
    1.  这将在服务器日志中打印关于搜索表达式如何被解析的附加信息（参见<a class="reference-link" href="../../Troubleshooting/Error%20logs.md">错误日志</a>）。
    2.  在详细了解搜索功能后，此功能对于确定复杂搜索查询为何未按预期工作尤其有用。
7.  操作
    1.  除了仅搜索之外，还可以应用操作，例如向搜索匹配到的笔记添加标签或关系。
    2.  与其他搜索配置不同，这里可以多次应用相同的操作（即能够向笔记应用多个标签）。
    3.  给定的操作与<a class="reference-link" href="../../Advanced%20Usage/Bulk%20Actions.md">批量操作</a>中的操作相同，这是在<a class="reference-link" href="../UI%20Elements/Note%20Tree.md">笔记树</a>中直接操作笔记的替代方法。
    4.  定义操作后，首先按 _搜索_ 检查匹配的笔记，然后按 _搜索并执行操作_ 触发操作。

## 查看搜索结果

结果作为**片段卡片**列表显示在搜索面板下方。每张卡片显示笔记标题和匹配文本的简短摘录。

搜索还会突出显示标题或内容中匹配的单词：

*   使用实心下划线绿色表示直接匹配；
*   使用虚线下划线橙色表示部分匹配（由模糊搜索匹配）。

此外：

*   始终显示**结果总数**，以便您立即判断查询的范围。
*   通过**每页大小选择器**，您可以选择每页显示多少结果。您的选择会被记住并在您的设备间同步（存储在 `searchResultsPageSize` 选项中），因此您无需在每台设备上重置它。
*   **点击结果**会打开笔记并直接跳转到第一个匹配项。笔记内查找栏会打开并预填您的搜索词，以便您可以使用查找控件浏览其余匹配项。
*   如果匹配项位于**折叠的部分**（例如折叠的标题）内，则该部分会自动展开以便匹配项可见。

## 搜索如何匹配您的文本

最常见的困惑来源是 `=` 符号根据其出现位置意味着两种_不同_的事物。请阅读本节一次，其余的搜索行为将变得可预测。

有三种匹配模式：

| 模式 | 触发方式 | 匹配内容 | 子串？ | 模糊（拼写错误）？ |
| --- | --- | --- | --- | --- |
| **默认** | 输入无前缀的单词 | 标题、内容或属性中任意位置的完整单词_和_子串，按相关性排序 | 是 | 是 |
| **精确全文** | 前导 `=`（例如 `=sync`） | 精确的完整单词或短语，忽略周围标点 | 否 | 否 |
| **属性/特性相等** | `#label=value` 或 `note.property=value` 子句中的 `=` | _整个_属性或特性值，精确匹配 | 否 | 否 |

下面的每个示例都由自动化测试 1:1 支持，因此文档不会与搜索引擎脱节。

### 默认匹配（无前缀）

**规则：** 输入无前缀的单词会查找在标题、内容或属性中任意位置包含这些单词（作为完整单词或子串）的笔记。最接近的匹配项排在前面。

| 查询 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | 是（排名更高） | 包含精确单词 `sync` |
| `sync` | `synchronize the database now` | 是（排名较低） | `sync` 是 `synchronize` 的子串 |

### 使用 `=` 前缀进行精确匹配

**规则：** 前导 `=` 将全文搜索切换为精确匹配。它仅查找完整的单词或短语，忽略周围标点，**没有**子串和**没有**模糊匹配。当普通搜索返回过多近似匹配时使用它。

| 查询 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `=sync` | `see (sync) mode` | 是 | `(sync)` 是完整单词 `sync`；标点被忽略 |
| `=sync` | `in sync, then continue` | 是 | `sync,` 是完整单词 `sync` |
| `=sync` | `he said "sync" out loud` | 是 | `"sync"` 是完整单词 `sync` |
| `=sync` | `synchronize the database now` | 否 | `=` 从不匹配子串 |
| `=sync` | `please send the file` | 否 | `=` 从不匹配拼写错误/模糊 |

要匹配精确的**短语**，请在 `=` 后加上引号（单引号、双引号或反引号均可）。该短语必须作为连续的单词出现，但它们之间或周围的标点将被忽略：

| 查询 | 示例笔记（标题或内容） | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `="project plan"` | 标题 `Project Plan` | 是 | 标题正是该短语 |
| `="project plan"` | `the (project plan) is ready to share` | 是 | 连续短语出现；标点被忽略 |
| `="project plan"` | `the plan for this project is late` | 否 | 单词存在但不连续 |

### 属性和特性相等（`=`， `!=`）

**规则：** 当 `=` 比较属性或特性时，如 `#label=value` 或 `note.title=value`，它是**严格的全值相等**：_整个_值必须等于您输入的内容，忽略大小写和变音符号。这**不是**单词匹配。`!=` 是其否定形式。

以下示例假设有四条笔记：_Austria_ (`#capital=Vienna`)， _Somewhere_ (`#capital=Vienna Austria`)， _Czech Republic_ (`#capital=Prague`) 和 _Switzerland_ (`#capital=Zürich`)。

| 查询 | 示例标签值 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `#capital=Vienna` | `Vienna` | 是 | 整个值等于 `Vienna` |
| `#capital=Vienna` | `Vienna Austria` | 否 | 整个值是 `Vienna Austria`， 不是 `Vienna` |
| `#capital="Vienna Austria"` | `Vienna Austria` | 是 | 引用多词值以进行完整匹配 |
| `#capital=Zurich` | `Zürich` | 是 | 相等性忽略变音符号 |
| `#capital!=Vienna` | `Prague` | 是 | `!=` 匹配所有不等于 `Vienna` 的值 |
| `#capital!=Vienna` | `Vienna` | 否 | `!=` 排除精确值 |

> **快速搜索放宽了此规则。** [快速搜索](Quick%20search.md)栏和自动完成将属性 `=` 视为“包含”，因此在那里输入的 `#capital=Vienna` 也会匹配 `Vienna Austria`。此处描述的严格全值相等仅适用于完整搜索。

### 模糊运算符（`~=` 和 `~*`）

**规则：** 模糊运算符容忍拼写错误。`~=`（模糊等于）匹配与您的词条接近的完整单词变体的值。`~*`（模糊包含）在您的词条出现在值内的任何位置时匹配，无论是作为片段还是近似匹配。两者都适用于笔记属性，如 `note.title` 和 `note.content`，以及标签（`#label`）。模糊运算符需要至少 3 个字符。

以下示例假设有一条标题为 `Books` 的笔记，带有标签 `#author=Tolkien`，以及一条内容为 `learn programming today` 的笔记。

| 查询 | 示例值 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `note.title ~= boks` | 标题 `Books` | 是 | 与 `books` 相差一次编辑 |
| `#author ~= tolkein` | 作者 `Tolkien` | 是 | `tolkein` 是 `tolkien` 的拼写错误 |
| `note.content ~* progr` | `learn programming today` | 是 | `progr` 是 `programming` 的片段 |
| `note.content ~* programing` | `learn programming today` | 是 | `programing` 与 `programming` 相差一次编辑 |

### 模糊容忍度（AUTO）

**规则：** 容忍多少拼写错误取决于您搜索词条的**长度**（由 Elasticsearch 推广的“AUTO”方案）。短词条必须几乎完全匹配以避免噪音；较长的词条容忍更多的错误。

| 词条长度 | 允许的编辑次数 |
| --- | --- |
| 1–2 个字符 | 0（仅精确） |
| 3–5 个字符 | 1 |
| 6+ 个字符 | 2 |

| 查询 | 词条长度 | 示例笔记内容 | 匹配？ | 原因 |
| --- | --- | --- | --- | --- |
| `cat` | 3 | `a bright red car` | 是 | 对于 3–5 个字符的词条，1 次编辑在预算内 |
| `ceck` | 4 | `the latest tech trends` | 否 | `ceck`→`tech` 需要 2 次编辑；此长度只允许 1 次 |
| `combinef` | 8 | `the values were combined together` | 是 | `combinef`→`combined` 是 1 次编辑；6+ 字符最多允许 2 次 |

### 相关性排序

**规则：** 结果按匹配的_程度_排序，而不仅仅取决于是否匹配。精确的完整单词和短语匹配排在子串和模糊匹配之前，并且您的单词作为连续短语出现的笔记排在分散出现的笔记之前。

| 查询 | 排名更高 | 排名较低 | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | `synchronize the database now` | 精确单词优于子串 |
| `you and me` | `I like you and me as a phrase` | `the menu is here and you know it` | 连续短语优于分散单词 |

### 可搜索内容

搜索查看的不只是可见的正文文本。以下所有内容都会被索引和搜索：

*   笔记标题，
*   笔记正文内容，
*   标签和关系（[属性](../../Advanced%20Usage/Attributes.md)），
*   链接 URL 和链接预览的标题/描述，
*   笔记引用链接到的笔记的标题。

最后一点最不明显：如果一条笔记的唯一内容是引用链接到另一条笔记，搜索该另一条笔记的**标题**仍然会找到该链接笔记。

| 查询 | 设置 | 匹配？ | 原因 |
| --- | --- | --- | --- |
| `special topic` | 一条笔记，其唯一内容是引用链接到标题为 `Special Topic` 的笔记 | 是，并且链接目标排在首位 | 目标的标题被索引到链接笔记的可搜索文本中 |
| `special` | 同一条笔记（仅引用链接到 `Special Topic`） | 是，目标标题中的一个词就足够了 | 索引的标题像正文文本一样被规范化，因此即使是一个小写单词也能匹配 |
| `zurich` | 一条笔记，其唯一内容是引用链接到标题为 `Zürich` 的笔记 | 是 | 索引的标题已规范化其重音符号，因此普通形式可以匹配带重音的标题 |

### 变音符号

**规则：** 重音符号在两侧都被规范化，因此带重音的单词与其普通形式可以相互匹配。

| 查询 | 示例笔记内容 | 匹配？ |
| --- | --- | --- |
| `ktory` | `slovo ktorý znamena nieco` | 是 |
| `ktorý` | `the word ktory appears here` | 是 |

### 正则表达式（`%=`）

**规则：** `%=` 运算符根据正则表达式匹配属性或标签值。

| 查询 | 示例笔记内容 | 匹配？ |
| --- | --- | --- |
| `note.content %= 'colou?r'` | `my favorite color of all` | 是 |
| `note.content %= 'colou?r'` | `my favourite colour of all` | 是 |

### 简单笔记搜索示例

*   `rings tolkien`：全文搜索以查找同时包含“rings”和“tolkien”的笔记。
*   `"The Lord of the Rings" Tolkien`：全文搜索，其中“The Lord of the Rings”必须精确匹配。
*   `note.content *=* rings OR note.content *=* tolkien`：查找内容中包含“rings”或“tolkien”的笔记。
*   `towers #book`：结合全文和属性搜索，查找包含“towers”且具有“book”标签的笔记。
*   `towers #book or #author`：搜索包含“towers”且具有“book”或“author”标签的笔记。
*   `towers #!book`：搜索包含“towers”但不具有“book”标签的笔记。
*   `#book #publicationYear = 1954`：查找具有“book”标签且“publicationYear”设置为 1954 的笔记。
*   `#genre *=* fan`：查找“genre”标签包含子串“fan”的笔记。其他运算符包括用于“包含”的 `*+*`， 用于“开始于”的 `=*`， 用于“结束于”的 `*=`， 以及用于“不等于”的 `!=`。
*   `#book #publicationYear >= 1950 #publicationYear < 1960`：使用数字运算符查找所有在 20 世纪 50 年代出版的书籍。
*   `#dateNote >= TODAY-30`：查找“dateNote”标签在过去 30 天内的笔记。支持的日期值包括 NOW +- 秒， TODAY +- 天， MONTH +- 月， YEAR +- 年。
*   `~author.title *=* Tolkien`：查找与标题包含“Tolkien”的作者相关的笔记。
*   `#publicationYear %= '19[0-9]{2}'`：使用 `%=` 运算符匹配正则表达式。此功能自 Trilium 0.52 起可用。
*   `note.content %= '\\d{2}:\\d{2} (PM|AM)'`：查找提及时间的笔记。正则表达式中的反斜杠必须转义。

### 高级用例

*   `~author.relations.son.title = 'Christopher Tolkien'`：搜索具有“author”关系指向某条笔记，而该笔记又具有指向“Christopher Tolkien”的“son”关系的笔记。这可以通过以下笔记结构建模：
    *   书籍
        *   指环王
            *   标签：“book”
            *   关系：“author”指向“J. R. R. Tolkien”笔记
    *   人物
        *   J. R. R. Tolkien
            *   关系：“son”指向“Christopher Tolkien”笔记
            *   Christopher Tolkien
*   `~author.title *= Tolkien OR (#publicationDate >= 1954 AND #publicationDate <= 1960)`：使用布尔表达式和括号对表达式进行分组。请注意，以括号开头的表达式需要前置“表达式分隔符”（# 或 ~）。
*   `note.parents.title = 'Books'`：查找父笔记名为“Books”的笔记。
*   `note.parents.parents.title = 'Books'`：查找祖父笔记名为“Books”的笔记。
*   `note.ancestors.title = 'Books'`：查找祖先笔记名为“Books”的笔记。
*   `note.children.title = 'sub-note'`：查找子笔记名为“sub-note”的笔记。

### 使用笔记属性搜索

笔记具有可用于搜索的属性，例如 `noteId`、`dateModified`、`dateCreated`、`isProtected`、`type`、`title`、`text`、`content`、`rawContent`、`ownedLabelCount`、`labelCount`、`ownedRelationCount`、`relationCount`、`ownedRelationCountIncludingLinks`、`relationCountIncludingLinks`、`ownedAttributeCount`、`attributeCount`、`targetRelationCount`、`targetRelationCountIncludingLinks`、`parentCount`、`childrenCount`、`isArchived`、`contentSize`、`noteSize` 和 `revisionCount`。

这些属性可以通过 `note.` 前缀访问，例如，`note.type = code AND note.mime = 'application/json'`。

### 排序和限制

```
#author=Tolkien orderBy #publicationDate desc, note.title limit 10
```

此示例将：

1.  查找具有作者标签“Tolkien”的笔记。
2.  按 `publicationDate` 降序对结果排序。
3.  如果出版日期相同，则使用 `note.title` 作为次级排序。
4.  将结果限制为前 10 条笔记。

### 否定

某些查询只能通过否定来表达：

```
#book AND not(note.ancestors.title = 'Tolkien')
```

此查询查找所有不在“Tolkien”子树中的书籍笔记。

## 渐进式搜索策略

Trilium 使用渐进式搜索策略，首先执行精确匹配，然后在需要时添加模糊匹配。

### 渐进式搜索如何工作

1.  **阶段 1 - 精确匹配**：当您搜索时，Trilium 首先查找您搜索词条的精确匹配。这处理了绝大多数搜索（90%+）并几乎立即返回结果。
2.  **阶段 2 - 模糊回退**：如果阶段 1 未找到足够多的高质量结果（少于 5 个具有良好相关性得分的结果），Trilium 会自动添加模糊匹配以查找包含拼写错误或拼写变体的结果。
3.  **结果排序**：无论个别得分如何，精确匹配总是出现在模糊匹配之前。这确保了当您搜索“project”时，包含精确单词“project”的笔记会出现在包含类似单词（如“projects”或“projection”）的笔记之前。

### 渐进式搜索行为

*   **速度**：大多数搜索仅使用精确匹配即可完成
*   **排序**：精确匹配出现在模糊匹配之前
*   **回退**：当精确匹配返回少于 5 个结果时，模糊匹配被激活
*   **识别**：结果会指示它们是精确匹配还是模糊匹配

### 搜索性能

搜索系统规格：

*   内容大小限制：每条笔记 10MB（之前为 50KB）
*   用于模糊匹配的编辑距离计算
*   快速搜索中的无限滚动

## 底层原理

### 标签和关系快捷方式

按标签搜索的“完整”语法是：

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

搜索语法允许结合全文搜索和基于属性的搜索。例如，`tolkien #book` 包含：

1.  全文词元 - `tolkien`
2.  属性表达式 - `#book`

Trilium 通过查找表示属性和特性的某些特殊字符或单词（例如 #， ~， note.）来检测全文搜索和属性/特性搜索之间的分隔。如果您需要在全文搜索中包含这些字符，请使用反斜杠对其进行转义，以便将它们作为常规文本处理：

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

支持三种类型的引号：单引号、双引号和反引号。

### 类型强制

标签值在技术上是字符串，但可以被强制转换以进行数字比较：

```
note.dateCreated =* '2019-05'
```

这将查找创建于 2019 年 5 月的笔记。像 `#publicationYear >= 1960` 这样的数字运算符会将字符串值转换为数字进行比较。

## 从 URL 自动触发搜索

您可以通过在 URL 中包含搜索[url 编码](https://meyerweb.com/eric/tools/dencoder/)字符串来打开 Trilium 并自动触发搜索：

`http://localhost:8080/#?searchString=abc`

## 搜索配置

### 参数

| 参数 | 值 | 描述 |
| --- | --- | --- |
| `MIN_FUZZY_TOKEN_LENGTH` | 3 | 模糊匹配的最小字符数 |
| `MAX_EDIT_DISTANCE` | 2 | 字符更改的上限，仅由 6+ 个字符的词条达到；较短的词条允许更少的更改。请参阅上面的_模糊容忍度（AUTO）_部分 |
| `RESULT_SUFFICIENCY_THRESHOLD` | 5 | 触发模糊回退前所需的最小精确结果数 |
| `MAX_CONTENT_SIZE` | 10MB | 用于搜索处理的笔记内容最大大小 |

### 限制

*   被搜索的笔记内容限制为每条笔记 10MB，以防止性能问题
*   超过此限制的笔记仍将包含在标题和属性搜索中
*   模糊匹配要求词元至少为 3 个字符