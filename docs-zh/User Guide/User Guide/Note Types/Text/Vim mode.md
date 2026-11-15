# Vim 模式
> [!TIP]
> 初次接触 Vim？请先阅读<a class="reference-link" href="Vim%20mode/Vim%20beginner%20guide.md">Vim 入门指南</a>，其中解释了各种模式是什么，以及应该先学习哪些按键。

Vim 模式为文本笔记带来了 Vim 风格的模态编辑：在 Trilium 自带的编辑器中，提供 [Vim](https://www.vim.org/) 文本编辑器的移动、操作符和命令。它理解富文本的结构：一个段落、一个标题、一个列表项或一个表格单元格就是一行，图像或包含的笔记也是如此。

最常用的按键见下方的_速查表_，全部按键见<a class="reference-link" href="Vim%20mode/Vim%20full%20reference.md">Vim 完整参考</a>。

## 启用 Vim 模式

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ → _功能_。
2.  开启 _Vim 模式_。

该选项仅适用于当前设备，因此请在每个想要使用 Vim 模式的设备上重复这些步骤。它会立即生效，无需重新加载。代码笔记有单独的选项：<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _代码笔记_ → _编辑器_ → _Vim 键位绑定_。

一旦开启 Vim 模式：

*   新打开的文本笔记以普通模式启动：按 `i` 输入文字，按 <kbd>Esc</kbd> 返回命令模式。
*   在开启 Vim 模式时已经打开的笔记会切换到插入模式，以便你可以继续输入。
*   在插入模式下，常规编辑器仍然可用，包括其格式化、斜杠命令、类 Markdown 格式化和工具栏。少数快捷键在此处也遵循 Vim，参见下方的_编辑器中发生变化的快捷键_。

### Vim 模式的显示位置

Vim 模式使用窗口底部<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>的三个位置：

*   _Vim_ 徽标位于状态栏其他指示器之前，当当前笔记开启 Vim 模式时会高亮显示。点击它可为该笔记关闭或开启 Vim 模式，参见下方的_单个笔记的 Vim 模式_。右键点击它会弹出一个菜单，包含相同的开关、按键提示开关、设置以及本页面。
*   **模式指示器**位于徽标之后，显示当前模式：`NORMAL`、`INSERT`、`VISUAL`、`VISUAL LINE` 或 `REPLACE`。其旁边会显示尚未完成的命令的按键、简短消息以及正在录制的宏。
*   <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Breadcrumb.md">面包屑</a>区域用于两件事：下方描述的按键提示，以及当你按下 `:`、`/` 或 `?` 时在该处打开的命令行。

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Zen%20mode.md">禅模式</a>下，按键提示、_Vim_ 徽标和模式指示器均可见。

## 设置

设置位于<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _文本笔记_ → _功能_。后三项在开启 _Vim 模式_ 后显示在其下方。_Vim 模式_ 本身按设备保存，而其他三项会同步。

| 设置 | 默认值 | 适用于 | 作用 |
| --- | --- | --- | --- |
| _Vim 模式_ | 关闭 | 此设备 | 在文本笔记中开启 Vim 模式。 |
| _按键提示_ | 开启 | 你的所有设备 | 显示当前模式的按键、可跟在命令之后的按键以及命令行的建议。参见下方的_按键提示_。 |
| _插入模式下的 Vim 按键_ | 关闭 | 你的所有设备 | 使 <kbd>Ctrl</kbd>+<kbd>U</kbd>、<kbd>Ctrl</kbd>+<kbd>E</kbd>、<kbd>Ctrl</kbd>+<kbd>Y</kbd>、<kbd>Ctrl</kbd>+<kbd>K</kbd>、<kbd>Ctrl</kbd>+<kbd>V</kbd> 和 <kbd>Ctrl</kbd>+<kbd>A</kbd> 在输入时遵循 Vim。关闭时，它们保持编辑器赋予的含义，例如 <kbd>Ctrl</kbd>+<kbd>U</kbd> 为下划线，<kbd>Ctrl</kbd>+<kbd>V</kbd> 为粘贴。 |
| _启动命令_ | 空 | 你的所有设备 | 在 Vim 模式启动时运行命令，主要用于设置键位映射。 |

### 启动命令

每行写一条命令，就像在 `:` 之后输入的那样。以 `"` 开头的行是注释。

```
" Leave Insert mode by typing jk
imap jk <Esc>
" Make Y yank to the end of the line
nmap Y y$
```

当你编辑列表时，离开该字段后命令会立即重新运行，其映射会替换之前列表的映射。更改其他设置不会再次运行它们。仅能理解 Vim 模式的命令，因此为 Vim 编写的 `.vimrc` 文件无法直接使用。

### 单个笔记的 Vim 模式

要为单个笔记单独决定（无论选项如何设置），请为其添加一个[标签](../../Advanced%20Usage/Attributes/Labels.md)：

*   `#vimMode` 在该笔记中开启 Vim 模式。
*   `#vimMode=false` 使该笔记保持在常规编辑器中。

标签可以被继承，因此一个标签可以覆盖整个子树。设置在笔记本身的标签优先于继承的标签：如果父笔记上有一个可继承的 `#vimMode`，而子笔记有 `#vimMode=false`，则该子笔记保持在常规编辑器中。

当 _Vim 模式_ 选项开启时，状态栏中的 _Vim_ 徽标会为你设置此标签：点击它会为当前笔记设置 `#vimMode=false`，再次点击会移除该标签，或者在笔记将继承 `#vimMode=false` 的情况下设置 `#vimMode=true`。当笔记的标签可继承时，点击也会改变其下笔记的 Vim 模式，其菜单会说明这一点。

## 按键提示

按键提示在学习时很有帮助，熟悉按键后可以关闭。它们显示在状态栏的面包屑区域：

*   在普通模式和可视模式下，该模式最常用的按键会取代面包屑。要在按键和面包屑之间切换，请在普通模式下按 <kbd>Esc</kbd>。这是 <kbd>Esc</kbd> 最后执行的操作：当有其他适用操作时（例如清除搜索高亮），会先执行该操作，需要再按一次。参见下方的_Esc 键_。
*   在命令中间暂停后（例如在 `d` 或 `g` 之后），会显示可以跟随的按键。
*   命令行会建议与输入匹配的命令，<kbd>Tab</kbd> 或方向键可补全它们。搜索提示会说明模式的读取方式。
*   要查看当前模式的所有按键，请点击模式指示器或按 <kbd>Alt</kbd>+<kbd>F1</kbd>。

要关闭提示，请使用 _按键提示_ 设置或输入 `:set nohints`。`:set hints` 会重新开启它们。

## 速查表

以下是使用最多的按键和命令。依次输入的按键写在一起，例如 `dd`。除非另有说明，它们均在普通模式下输入。

<div class="trilium-multicolumn-layout" data-trilium-column-ratios="1-1">
<div class="trilium-multicolumn-column">

### 模式

*   `i` / `a`：在光标前 / 后输入。
*   `I` / `A`：在行首 / 行尾输入。
*   `o` / `O`：在下方 / 上方打开一行并输入。
*   `v` / `V`：选择字符 / 整行。
*   `R`：覆盖现有文本输入。
*   <kbd>Esc</kbd>：返回普通模式。

### 移动

*   `h` `j` `k` `l`：左、下、上、右。
*   `w` / `b` / `e`：下一个词、上一个词、词尾。
*   `0` / `^` / `$`：行首、第一个字符、行尾。
*   `gg` / `G`：笔记的第一行 / 最后一行。`12G` 转到第 12 行。
*   `{` / `}`：上一个 / 下一个块。
*   `f` 加一个字符：跳转到该行中的该字符。`;` 重复跳转。
*   `%`：转到匹配的括号。
*   <kbd>Ctrl</kbd>+<kbd>D</kbd> / <kbd>Ctrl</kbd>+<kbd>U</kbd>：向下 / 向上半页。
*   <kbd>Ctrl</kbd>+<kbd>O</kbd> / <kbd>Ctrl</kbd>+<kbd>I</kbd>：在跳转位置之间后退 / 前进。

### 编辑

*   `x`：删除光标下的字符。
*   `dd` / `dw` / `D`：删除行、词、行剩余部分。
*   `cc` / `cw` / `C`：更改行、词、行剩余部分。
*   `ciw`：更改光标下的词，无论光标位于其中何处。
*   `r` 加一个字符：替换一个字符。
*   `J`：将下一行合并到本行。
*   `>>` / `<<`：增加 / 减少行缩进。
*   `~`：在大写和小写之间切换。
*   `u` / <kbd>Ctrl</kbd>+<kbd>R</kbd>：撤销 / 重做。
*   `.`：重复上一次更改。
*   数字可重复命令：`3dd` 删除三行，`2w` 移动两个词。

</div>
<div class="trilium-multicolumn-column">

### 复制和粘贴

*   `yy` / `yw` / `y$`：复制（yank）行、词、行剩余部分。
*   `p` / `P`：在光标后 / 前放置（粘贴）。
*   `"ayy` / `"ap`：将行复制到寄存器 `a` / 从其中放置。
*   `"+y` / `"+p`：复制到 / 从系统剪贴板粘贴。

复制的文本保留其格式，例如粗体、链接和颜色。

### 选择

*   `v` / `V`：开始选择字符 / 行。任何移动都会扩展选择。
*   `iw`、`ip`、`i"`、`i(`：选择词、块、引号或括号内的文本。用 `a` 代替 `i` 还会包含其周围的内容。
*   `y` / `d` / `c`：复制、删除或更改选择。
*   `>` / `<`：增加 / 减少所选行的缩进。
*   `o`：跳转到选择的另一端。
*   `gv`：重新选择上一次的选择。

### 搜索和替换

*   `/text` / `?text`：向前 / 向后搜索，然后按 <kbd>Enter</kbd>。
*   `n` / `N`：下一个 / 上一个匹配项。
*   `*` / `#`：向前 / 向后搜索光标下的词。
*   `:s/old/new/`：在当前行中替换。
*   `:%s/old/new/g`：在笔记中全局替换。添加 `c` 以确认每个匹配项。
*   `:noh`：清除搜索高亮。

### Trilium 特有功能

*   `:w`：立即保存笔记。Trilium 也会自动保存。
*   `:q` 或 `ZZ`：关闭笔记的标签页或其分屏。
*   `gf`：跟随光标下的链接或链接预览。
*   `]]` / `[[`：转到下一个 / 上一个标题。
*   `za`：折叠或展开光标处的标题、列表项或可折叠块。
*   `:sort`：对选中的段落或列表项，或光标周围的段落或列表项进行排序。
*   `:ck bold`：按名称运行文本编辑器的命令，此处作用于选择。
*   在图像或包含的笔记上按 `i` 或 `a`：编辑其标题或内容。
*   <kbd>Alt</kbd>+<kbd>F1</kbd>：列出当前模式的所有按键。

</div>
</div>

其他按键和命令请参见<a class="reference-link" href="Vim%20mode/Vim%20full%20reference.md">Vim 完整参考</a>。

## Vim 如何读取文本笔记

Vim 以行为单位工作，而文本笔记本身没有行。以下是两者的对应方式：

*   每个段落、标题、列表项的段落、表格单元格的段落以及代码块的行都是一行，无论它在屏幕上占用多少行。这有时被称为_逻辑行_，与_屏幕行_相对。`dd`、`yy`、`j` 和 `k` 作用于逻辑行，而 `gj` 和 `gk` 按屏幕行移动。
*   图像、图表、水平线或包含的笔记也是一行：`j` 和 `k` 会停在其上，`dd` 会删除它。`i` 或 `a` 进入其标题或内容。要离开包含的笔记，请在其普通模式下按 <kbd>Esc</kbd>，在其第一行按 `k`，或在其最后一行按 `j`。
*   `o` 和 `O` 添加 <kbd>Enter</kbd> 在该位置会添加的内容，例如段落、列表项或代码行。`J` 以 <kbd>Backspace</kbd> 的方式合并行。`>>` 和 `<<` 更改列表项的级别或段落的缩进。
*   `{`、`}`、`ip` 和 `ap` 以块而非空行工作：段落、列表项、引用、表格单元格、代码块。在标题上，`ap` 是标题及其所属章节。
*   在表格中，`h` 和 `l` 停留在单元格内，`j` 和 `k` 沿列向下和向上移动。
*   折叠的标题或列表项对 `j` 和 `k` 而言算作一行。搜索也会查看其内部，并展开包含匹配项的那一个。
*   寄存器由所有文本笔记共享，但不与代码笔记共享。要在两者之间传递文本，请使用剪贴板寄存器 `"+`。

## 编辑器中发生变化的快捷键

Vim 使用了 Trilium 的一些 <kbd>Ctrl</kbd> 快捷键。当光标位于文本笔记中时，Vim 的含义优先，正如它在代码笔记中已经做的那样。最后一列显示的是关闭 _插入模式下的 Vim 按键_ 设置（即默认值）时的插入模式：

| 快捷键 | 无 Vim 模式 | 普通和可视模式 | 插入模式 |
| --- | --- | --- | --- |
| <kbd>Ctrl</kbd>+<kbd>R</kbd> | 重新加载应用（<kbd>F5</kbd> 仍可） | 重做 | 插入寄存器内容 |
| <kbd>Ctrl</kbd>+<kbd>O</kbd> | 在当前笔记之后创建笔记 | 返回上一个跳转 | 运行一条普通模式命令 |
| <kbd>Ctrl</kbd>+<kbd>P</kbd> | 创建子笔记 | 向上移动一行，如同 `k` | 无 |
| <kbd>Ctrl</kbd>+<kbd>F</kbd> | 在笔记中搜索（桌面应用） | 向下滚动一页 | 不变 |
| <kbd>Ctrl</kbd>+<kbd>B</kbd>、<kbd>Ctrl</kbd>+<kbd>I</kbd>、<kbd>Ctrl</kbd>+<kbd>U</kbd> | 粗体、斜体、下划线 | 向上滚动一页、前进到下一个跳转、向上滚动半页 | 不变 |
| <kbd>Ctrl</kbd>+<kbd>A</kbd>、<kbd>Ctrl</kbd>+<kbd>X</kbd> | 全选、剪切 | 增加、减少光标处的数字 | 不变 |
| <kbd>Ctrl</kbd>+<kbd>Z</kbd>、<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> | 撤销、重做 | 与 `u` 和 <kbd>Ctrl</kbd>+<kbd>R</kbd> 相同 | 不变 |
| <kbd>Ctrl</kbd>+<kbd>W</kbd> | 关闭标签页 | 无 | 删除光标前的词 |
| <kbd>Ctrl</kbd>+<kbd>T</kbd>、<kbd>Ctrl</kbd>+<kbd>D</kbd> | 打开新标签页、无 | 不变、向下滚动半页 | 增加、减少行缩进 |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | 复制 | 复制选择并离开可视模式。未选择任何内容时，等同于 <kbd>Esc</kbd> | 复制选择。未选择任何内容时，离开插入模式 |
| `/` 和 `:` | 斜杠命令和表情符号补全 | 搜索和命令行 | 不变 |

开启 _插入模式下的 Vim 按键_ 后，还有六个快捷键在输入时遵循 Vim。在普通和可视模式下，该设置不会改变任何内容。

| 快捷键 | 插入模式下，设置关闭 | 插入模式下，设置开启 |
| --- | --- | --- |
| <kbd>Ctrl</kbd>+<kbd>U</kbd> | 下划线 | 从光标删除到行首 |
| <kbd>Ctrl</kbd>+<kbd>E</kbd> | 无 | 插入光标下方的字符 |
| <kbd>Ctrl</kbd>+<kbd>Y</kbd> | 重做 | 插入光标上方的字符 |
| <kbd>Ctrl</kbd>+<kbd>K</kbd> | 创建链接 | 启动二合字母，即用两个按键输入的字符 |
| <kbd>Ctrl</kbd>+<kbd>V</kbd> | 粘贴 | 按原样插入下一个按键 |
| <kbd>Ctrl</kbd>+<kbd>A</kbd> | 全选 | 再次插入最后插入的文本 |

在设置开启时若要粘贴，请先按 <kbd>Esc</kbd>：在普通和可视模式下，<kbd>Ctrl</kbd>+<kbd>V</kbd> 始终执行粘贴。

*   带 <kbd>Alt</kbd>、带 <kbd>Ctrl</kbd>+<kbd>Shift</kbd> 或 <kbd>Ctrl</kbd>+<kbd>Alt</kbd> 的快捷键以及功能键在所有模式下保持其含义，上述 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> 除外。Vim 不使用的快捷键也是如此，例如用于链接到笔记的 <kbd>Ctrl</kbd>+<kbd>L</kbd>。用于链接的 <kbd>Ctrl</kbd>+<kbd>K</kbd> 也是其中之一，但在开启上述设置的插入模式下除外。
*   在 macOS 上，Trilium 的快捷键使用 <kbd>⌘</kbd>，而 Vim 的快捷键使用 <kbd>Ctrl</kbd>，因此不会有任何冲突。<kbd>⌘</kbd>+<kbd>Z</kbd> 和 <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> 执行撤销和重做。
*   在 Windows 和 Linux 上的浏览器中，<kbd>Ctrl</kbd>+<kbd>W</kbd>、<kbd>Ctrl</kbd>+<kbd>T</kbd> 和 <kbd>Ctrl</kbd>+<kbd>N</kbd> 始终属于浏览器。

### Esc 键

<kbd>Esc</kbd> 每次按下只做一件事，即以下第一个适用的事项：

1.  关闭已打开的内容：命令行或搜索提示、弹出窗口（如链接气泡）、补全列表或按键列表。
2.  取消命令中迄今输入的按键。
3.  离开可视或插入模式。
4.  清除搜索高亮。
5.  在包含的笔记中，返回其周围的笔记。
6.  在按键提示开启时，在按键提示和面包屑之间切换。

因此，在插入模式下打开链接气泡时，第一次按下会关闭气泡，第二次按下会离开插入模式。<kbd>Ctrl</kbd>+<kbd>[</kbd> 与 <kbd>Esc</kbd> 作用相同。

## 限制

*   Vim 模式模仿 Vim，并不运行 Vim 本身。为 Vim 制作的插件和脚本不可用，其部分命令也缺失：参见<a class="reference-link" href="Vim%20mode/Vim%20full%20reference.md">Vim 完整参考</a>中的_不支持_。
*   Vim 模式在移动端布局中不可用，只读笔记没有模式。
*   不支持可视块模式。<kbd>Ctrl</kbd>+<kbd>V</kbd> 执行粘贴，但在开启 _插入模式下的 Vim 按键_ 时的插入模式下除外。
*   搜索模式是 JavaScript 正则表达式，而非 Vim 自身的，且匹配不能跨越多行。
*   `:q!` 和 `ZQ` 仅显示一条消息：笔记在输入时即保存，因此没有可丢弃的内容。
*   包含在文本笔记中的代码笔记遵循代码笔记的 _Vim 键位绑定_ 选项。

## 另请参见

*   <a class="reference-link" href="Vim%20mode/Vim%20beginner%20guide.md">Vim 入门指南</a>，了解各种模式以及首先应学习的按键。
*   <a class="reference-link" href="Vim%20mode/Vim%20full%20reference.md">Vim 完整参考</a>，了解所有按键和命令。