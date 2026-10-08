# 常见问题
## “Trilium”这个名字的灵感来源

> 给软件命名很难。我刚开始这个项目时住在安大略省，Trillium（延龄草）算是该省的标志性花卉，安大略省的许多机构都以“Trillium \[某某\]”命名。所以我几乎每天都会听到或看到它，我喜欢它的发音和自然意象，就直接沿用了。
> 
> _– Zadam（Trilium 原维护者）_

> [!NOTE]
> 尽管 Trillium 花的名字里有两个“l”，但 Trilium 应用只有一个。

## 如何创建文件夹？

Trilium 没有单独的文件夹类型：任何笔记都可以有子笔记，因此任何笔记都可以充当文件夹。一条笔记可以同时拥有自己的内容和子笔记，这与文件系统将文件和目录分开不同。

要将笔记组织到文件夹中：

1.  创建一条充当文件夹的笔记，例如“Projects”。
2.  在<a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中右键点击它，选择_插入子笔记_，或将鼠标悬停在它上面并按下 <span class="tn-icon bx bx-plus"></span> 按钮。
3.  要将现有笔记移入其中，请在树中将它们拖到它上面。

一条笔记的子笔记列在其内容的末尾（参见<a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>）。

如果你希望笔记看起来像文件夹，没有自己的内容而只显示其子笔记，请将其改为集合：在树中右键点击，选择_集合_，然后选择<a class="reference-link" href="Collections/Grid%20View.md">网格视图</a>或<a class="reference-link" href="Collections/List%20View.md">列表视图</a>。有关其他视图（如表格、看板和日历），请参见<a class="reference-link" href="Collections.md">集合</a>。

## macOS 支持

最初，Trilium Notes 认为 macOS 构建版本不受支持。TriliumNext 致力于让 macOS 上的体验尽可能好。

如果你发现任何平台特定的问题，欢迎[报告它们](Troubleshooting/Reporting%20issues.md)。

## 翻译/本地化支持

最初的 Trilium Notes 应用不支持多语言。由于我们认为国际化是应用的核心部分，我们添加了对它的支持。

欢迎为翻译做出贡献。

## 多用户支持

常见的需求是允许多个用户协作、共享笔记等。到目前为止我一直拒绝这样做，原因如下：

*   这是一个巨大的功能，或者更确切地说是协作功能的潘多拉魔盒，如用户管理、权限、冲突解决、多人实时编辑笔记等。这将是巨大的工作量。Trilium Notes 是一个主要由一个人在空闲时间制作的项目，未来也不太可能改变。
*   鉴于其规模，它可能会将注意力从我的主要关注点（个人笔记）上转移开。
*   只有单个人可以访问应用的假设简化了许多事情，或者直接使它们成为可能。在多用户应用中，我们的[脚本](Scripting.md)支持将是一个 XSS 安全漏洞，而在单用户假设下，它是一个无限可定制的工具。

## 如何在一个 Trilium 实例中打开多个文档

这通常不受支持——一个 Trilium 进程只能打开一个[数据库](Advanced%20Usage/Database.md)实例。但是，你可以运行两个 Trilium 进程（来自一次安装），每个连接到一个单独的文档。要实现这一点，你需要在 `TRILIUM_DATA_DIR` 环境变量中设置[数据目录](Installation%20%26%20Setup/Data%20directory.md)的位置，并在 `TRILIUM_PORT` 环境变量中设置单独的端口。如何做到这一点取决于平台，在基于 Unix 的系统中，你可以通过运行如下命令来实现：

```sh
TRILIUM_DATA_DIR=/home/me/path/to/data/dir TRILIUM_PORT=12345 trilium 
```

你可以将此命令保存到 `.sh` 脚本文件中或创建别名。对具有不同数据目录和端口的第二个实例执行类似操作。

## 我可以使用 Dropbox / Google Drive / OneDrive 在多台计算机之间同步数据吗？

不可以。

这些通用同步应用不适合同步正在被另一个应用打开并处理的数据库文件。结果是它们会损坏数据库文件，导致数据丢失，并在 Trilium 日志中出现以下消息：

```
SqliteError: database disk image is malformed
```

跨网络同步 Trilium 数据的唯一受支持方式是使用[同步/Web 服务器](Installation%20%26%20Setup/Synchronization.md)。

## 为什么使用数据库而不是平面文件？

Trilium 将笔记存储在[数据库](Advanced%20Usage/Database.md)中，这是一个 SQLite 数据库。人们经常问为什么 Trilium 不使用平面文件来存储笔记——这是一个合理的问题，因为平面文件易于互操作，可与 SCM/git 等配合使用。

简短的回答是，文件系统根本不够强大，无法实现我们想要用 Trilium 达成的目标。使用文件系统将意味着功能更少，问题可能更多。

更详细的回答：

*   [克隆](Basic%20Concepts%20and%20Features/Notes/Cloning%20Notes.md)就是你在文件系统术语中可能称之为“硬目录链接”的东西，但这个概念在任何文件系统中都没有实现。
*   文件系统区分目录和文件，而在 Trilium 中有意没有这种区别。
*   文件不按特定顺序存储，用户无法更改这一点。
*   Trilium 允许存储笔记[属性](Advanced%20Usage/Attributes.md)，这些属性可以在扩展用户属性中表示，但它们的支持在不同的文件系统/操作系统之间差异很大。
*   Trilium 在不同笔记之间建立链接/关系，可以快速检索/导航（例如用于[笔记地图](Advanced%20Usage/Note%20Map%20\(Link%20map%2C%20Tree%20map\).md)）。文件系统中没有这样的支持，这意味着这些必须存储在某种附属文件（迷你数据库）中。
*   文件系统通常不是事务性的。虽然这对于笔记应用来说并非完全必需，但拥有事务使得将笔记及其元数据保持在可预测和一致的状态变得容易得多。

## 搜索相关问题

### 为什么搜索有时会找到有拼写错误的结果？

Trilium 使用渐进式搜索策略，当精确匹配返回少于 5 个结果时，会包含模糊匹配。这样即使你的搜索查询中有轻微拼写错误，也能找到笔记。你可以使用模糊搜索运算符（`~=` 用于模糊精确匹配，`~*` 用于模糊包含）。详情请参见<a class="reference-link" href="Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>文档。

### 当我不确定确切拼写时，如何搜索笔记？

使用模糊搜索运算符：

*   `#title ~= "projct"` - 找到标题类似“project”的笔记，尽管有拼写错误
*   `note.content ~* "algoritm"` - 找到包含“algorithm”或类似词的内容

### 为什么有些搜索结果会排在得分更低的结果之前？

Trilium 将精确匹配放在模糊匹配之前。当你搜索“project”时，包含确切“project”的笔记会出现在包含“projects”或“projection”等变体的笔记之前，无论其他评分因素如何。

### 如何让我的搜索更快？

1.  使用“快速搜索”选项，仅搜索标题和属性（不搜索内容）
2.  使用“祖先”字段限制搜索范围
3.  设置结果限制以防止加载过多结果
4.  对于大型数据库，考虑归档旧笔记以缩小搜索范围