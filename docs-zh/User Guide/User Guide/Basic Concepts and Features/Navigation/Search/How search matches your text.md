# 搜索如何匹配你的文本
最常见的困惑来源是：`=` 符号根据出现位置的不同，表示两种_不同_的含义。读完本节，搜索的其余部分就变得可预测了。

共有三种匹配模式：

| 模式 | 如何触发 | 匹配内容 | 是否匹配子串？ | 是否模糊匹配（拼写错误）？ |
| --- | --- | --- | --- | --- |
| **默认** | 输入不带前缀的词 | 标题、内容或属性中任意位置的完整单词_和_子串，按相关度排序 | 是 | 是 |
| **精确全文** | 前导 `=`（例如 `=sync`） | 精确的完整单词或短语，忽略周围的标点符号 | 否 | 否 |
| **属性/特性相等** | 在 `#label=value` 或 `note.property=value` 子句中使用 `=` | _整个_属性或特性值，精确匹配 | 否 | 否 |

### 默认匹配（无前缀）

**规则：** 输入不带前缀的词会找到标题、内容或属性中任意位置包含这些词的笔记，可以是完整单词或子串。最接近的匹配排在最前面。

| 查询 | 示例笔记内容 | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | 是（排名较高） | 包含精确单词 `sync` |
| `sync` | `synchronize the database now` | 是（排名较低） | `sync` 是 `synchronize` 的子串 |

### 使用 `=` 前缀的精确匹配

**规则：** 前导 `=` 将全文搜索切换为精确匹配。它只查找完整单词或短语，忽略周围的标点符号，**不**匹配子串，**不**进行模糊匹配。当普通搜索返回过多近似匹配时使用它。

| 查询 | 示例笔记内容 | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `=sync` | `see (sync) mode` | 是 | `(sync)` 是完整单词 `sync`；标点被忽略 |
| `=sync` | `in sync, then continue` | 是 | `sync,` 是完整单词 `sync` |
| `=sync` | `he said "sync" out loud` | 是 | `"sync"` 是完整单词 `sync` |
| `=sync` | `synchronize the database now` | 否 | `=` 从不匹配子串 |
| `=sync` | `please send the file` | 否 | `=` 从不匹配拼写错误/模糊 |

要匹配精确**短语**，在 `=` 后加引号（单引号、双引号或反引号均可）。短语必须作为连续单词出现，但单词之间或周围的标点符号会被忽略：

| 查询 | 示例笔记（标题或内容） | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `="project plan"` | 标题 `Project Plan` | 是 | 标题正是该短语 |
| `="project plan"` | `the (project plan) is ready to share` | 是 | 连续短语出现；标点被忽略 |
| `="project plan"` | `the plan for this project is late` | 否 | 单词存在但不连续 |

### 属性和特性相等（`=`、`!=`）

**规则：** 当 `=` 比较属性或特性时，如 `#label=value` 或 `note.title=value`，它是**严格的全值相等**：_整个_值必须等于你输入的内容，忽略大小写和变音符号。这**不是**单词匹配。`!=` 则相反。

以下示例假设有四条笔记：_Austria_（`#capital=Vienna`）、_Somewhere_（`#capital=Vienna Austria`）、_Czech Republic_（`#capital=Prague`）和 _Switzerland_（`#capital=Zürich`）。

| 查询 | 示例标签值 | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `#capital=Vienna` | `Vienna` | 是 | 整个值等于 `Vienna` |
| `#capital=Vienna` | `Vienna Austria` | 否 | 整个值是 `Vienna Austria`，不是 `Vienna` |
| `#capital="Vienna Austria"` | `Vienna Austria` | 是 | 用引号括起多词值以完整匹配 |
| `#capital=Zurich` | `Zürich` | 是 | 相等比较忽略变音符号 |
| `#capital!=Vienna` | `Prague` | 是 | `!=` 匹配所有不等于 `Vienna` 的值 |
| `#capital!=Vienna` | `Vienna` | 否 | `!=` 排除精确值 |

> **快速搜索会放宽此规则。** [快速搜索](../Quick%20search.md)栏和自动补全将属性 `=` 视为“包含”，因此在那里输入 `#capital=Vienna` 也会匹配 `Vienna Austria`。此处描述的严格全值相等仅适用于完整搜索。

### 模糊运算符（`~=` 和 `~*`）

**规则：** 模糊运算符容忍拼写错误。`~=`（模糊相等）匹配与你的词接近的完整单词变体。`~*`（模糊包含）在你的词作为片段或近似匹配出现在值中任意位置时匹配。两者都适用于笔记特性如 `note.title` 和 `note.content`，以及标签（`#label`）。模糊运算符接受至少 3 个字符的词，但每个词容忍多少拼写错误取决于其长度——见下方_模糊容忍度_。

示例假设有一条标题为 `Books` 的笔记带有标签 `#author=Tolkien`，以及一条内容为 `learn programming today` 的笔记。

| 查询 | 示例值 | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `note.title ~= boks` | 标题 `Books` | 是 | 与 `books` 相差一个编辑 |
| `#author ~= tolkein` | 作者 `Tolkien` | 是 | `tolkein` 是 `tolkien` 的拼写错误 |
| `note.content ~* progr` | `learn programming today` | 是 | `progr` 是 `programming` 的片段 |
| `note.content ~* programing` | `learn programming today` | 是 | `programing` 与 `programming` 相差一个编辑 |

### 模糊容忍度

**规则：** 容忍多少拼写错误取决于搜索词的**长度**。短词必须精确匹配，因为一个编辑就足以将一个短词变成不相关的词；较长的词有更大的容忍度。

| 词长度 | 允许的编辑数 |
| --- | --- |
| 1–3 个字符 | 0（仅精确） |
| 4–6 个字符 | 1 |
| 7+ 个字符 | 2 |

| 查询 | 词长度 | 示例笔记内容 | 是否匹配？ | 原因 |
| --- | --- | --- | --- | --- |
| `cat` | 3 | `a bright red car` | 否 | 4 个字符以下不允许编辑，因此 `cat` 无法匹配 `car` |
| `carr` | 4 | `a blue debit card` | 是 | 4–6 个字符的词允许 1 个编辑 |
| `ceck` | 4 | `the latest tech trends` | 否 | `ceck`→`tech` 需要 2 个编辑；此长度只允许 1 个 |
| `combinef` | 8 | `the values were combined together` | 是 | `combinef`→`combined` 是 1 个编辑；7+ 个字符允许最多 2 个 |

### 相关度排序

**规则：** 结果按匹配_程度_排序，而不仅仅是否匹配。精确的完整单词和短语匹配排在子串和模糊匹配之上，你的词作为连续短语出现的笔记排在词分散出现的笔记之上。

| 查询 | 排名较高 | 排名较低 | 原因 |
| --- | --- | --- | --- |
| `sync` | `please sync the folders` | `synchronize the database now` | 精确单词胜过子串 |
| `you and me` | `I like you and me as a phrase` | `the menu is here and you know it` | 连续短语胜过分散的词 |

### 可搜索的内容

搜索不仅查看可见的正文文本。以下所有内容都被索引并可搜索：

*   笔记标题，
*   笔记正文内容，
*   标签和关系（[属性](../../../Advanced%20Usage/Attributes.md)），
*   链接 URL 以及链接预览的标题/描述，
*   笔记引用链接所指向的笔记的标题。

最后一点最不明显：如果一条笔记的唯一内容是指向另一条笔记的引用链接，搜索那条笔记的**标题**仍然能找到链接笔记。

| 查询 | 设置 | 是否匹配？ | 原因 |
| --- | --- | --- | --- |
| `special topic` | 一条笔记的唯一内容是指向标题为 `Special Topic` 的笔记的引用链接 | 是，且被链接的目标排在最前 | 目标的标题被索引到链接笔记的可搜索文本中 |
| `special` | 同一条笔记（仅是指向 `Special Topic` 的引用链接） | 是，目标标题中的一个词就足够 | 被索引的标题像正文一样被规范化，因此即使一个小写单词也能匹配 |
| `zurich` | 一条笔记的唯一内容是指向标题为 `Zürich` 的笔记的引用链接 | 是 | 被索引的标题变音符号被规范化，因此普通形式能匹配带变音符号的标题 |

### 变音符号

**规则：** 两侧的变音符号都被规范化，因此带变音符号的词和其普通形式可以互相匹配。

| 查询 | 示例笔记内容 | 是否匹配？ |
| --- | --- | --- |
| `ktory` | `slovo ktorý znamena nieco` | 是 |
| `ktorý` | `the word ktory appears here` | 是 |

### 正则表达式（`%=`）

**规则：** `%=` 运算符将属性或标签值与正则表达式进行匹配。

| 查询 | 示例笔记内容 | 是否匹配？ |
| --- | --- | --- |
| `note.content %= 'colou?r'` | `my favorite color of all` | 是 |
| `note.content %= 'colou?r'` | `my favourite colour of all` | 是 |