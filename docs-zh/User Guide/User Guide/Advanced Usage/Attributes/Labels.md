# 标签

标签是笔记的一种[属性](../Attributes.md)，它有一个名称，并且可选地有一个值。

## 常见用例

*   **个人使用的元数据**：为分类分配带有可选值的标签，例如 `#year=1999`、`#genre="sci-fi"` 或 `#author="Neal Stephenson"`。这可以与 <a class="reference-link" href="Promoted%20Attributes.md">提升属性</a> 结合使用，使其显示更加用户友好。
*   **配置**：标签可以配置高级功能或设置（参见下面的参考）。
*   **脚本和插件**：用于使用特殊元数据标记笔记，例如 <a class="reference-link" href="../Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a> 中的“weight”属性。

## 使用可视化编辑器创建标签

1.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a> 中的 _拥有的属性_ 部分。
2.  按右侧的 + 按钮（_添加新属性_）。
3.  为关系选择 _添加新标签_。

> [!TIP]
> 如果你更喜欢键盘快捷键，请在笔记或 _拥有的属性_ 部分获得焦点时按 <kbd>Alt</kbd>+<kbd>L</kbd> 以显示可视化编辑器。

在可视化编辑器中：

*   设置所需的名称
*   可选地，设置标签的值。标签可以没有值。
*   如果标签也应被子笔记继承，请勾选 _可继承_。更多信息请参见 <a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。

## 手动创建标签

在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Ribbon.md">功能区</a> 中的 _拥有的属性_ 部分：

*   要创建一个名为 `myLabel` 且没有值的标签，只需输入 `#myLabel`。
*   要创建一个名为 `myLabel` 且值为 `value` 的标签，只需输入 `#myLabel=value`。
*   如果值包含空格，则文本必须用引号括起来：`#myLabel="Hello world"`。
*   如果字符串包含引号（无论是否包含空格），则文本必须改用撇号括起来：`#myLabel='Hello "world"'`。
*   要创建一个名为 `myLabel` 的可继承标签，如果没有值，只需写 `#myLabel(inheritable)`；如果有值，则写 `#myLabel(inheritable)=value`。

## 预定义标签

这是 Trilium 原生支持的标签列表。

> [!TIP]
> 此处列出的一些标签以 `*` 结尾。这意味着存在多个具有相同前缀的标签，请查阅该标签描述中链接的特定页面以获取更多信息。

| 标签 | 描述 |
| --- | --- |
| `disableVersioning` | 为特定笔记禁用 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订</a> 的自动创建。对于例如大型但不重要的笔记（例如用于脚本的大型 JS 库）很有用。 |
| `versioningLimit` | 限制特定笔记的 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订</a> 的最大数量，覆盖全局设置。 |
| `calendarRoot` | 标记应用作 <a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记</a> 根节点的笔记。只应标记一个。 |
| `archived` | 从默认搜索结果和对话框中隐藏笔记。已归档笔记可以选择性地在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中隐藏。 |
| `excludeFromExport` | 导出时排除此笔记及其子笔记。 |
| `run`, `runOnInstance`, `runAtHour` | 参见 <a class="reference-link" href="../../Scripting/Backend%20scripts/Events.md">事件</a>。 |
| `disableInclusion` | 带有此标签的脚本将不会被包含到父脚本的执行中。 |
| `sorted`, `sortDirection`, `sortFoldersFirst`, `sortNatural`, `sortLocale`, `top`, `bottom` | 管理自动/永久排序。参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Sorting%20Notes.md">笔记排序</a>。 |
| `hidePromotedAttributes` | 在此笔记上隐藏 <a class="reference-link" href="Promoted%20Attributes.md">提升属性</a>。在定义继承属性时通常很有用，但父笔记不需要它们。 |
| `readOnly` | 如果笔记类型支持（文本、代码、mermaid），则将此笔记标记为始终[只读](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)。 |
| `autoReadOnlyDisabled` | 为给定笔记禁用自动[只读模式](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)。 |
| `appCss` | 标记加载到 Trilium 应用程序中的 CSS 笔记，因此可用于修改 Trilium 的外观。更多信息请参见 <a class="reference-link" href="../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a>。 |
| `appTheme` | 标记作为完整 Trilium 主题的 CSS 笔记，因此可在 Trilium 选项中使用。更多信息请参见 <a class="reference-link" href="../../Theme%20development">主题开发</a>。 |
| `appThemeBase` | 设置为 `next`、`next-light` 或 `next-dark`，以使用相应的 TriliumNext 主题（自动、浅色或深色）作为自定义主题的基础，而不是旧版主题。更多信息请参见 <a class="reference-link" href="../../Theme%20development/Customize%20the%20Next%20theme.md">自定义 Next 主题</a>。 |
| `cssClass` | 此标签的值将作为 CSS 类添加到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a> 中表示给定笔记的节点上。这对于高级主题设置很有用。可用于模板笔记。 |
| `iconClass` | 此标签的值将作为 CSS 类添加到树上的图标中，这有助于在视觉上区分树中的笔记。示例可能是 bx bx-home - 图标取自 boxicons。可用于模板笔记。 |
| `pageSize` | 指定 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a> 中每页的项目数。 |
| `customRequestHandler` | 参见 <a class="reference-link" href="../Custom%20Request%20Handler.md">自定义请求处理器</a>。 |
| `customResourceProvider` | 参见 <a class="reference-link" href="../Custom%20Resource%20Providers.md">自定义资源提供程序</a>。 |
| `widget` | 将此笔记标记为将添加到 Trilium 组件树中的自定义小组件。更多信息请参见 <a class="reference-link" href="../../Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a>。 |
| `searchHome` | 新的搜索笔记将创建为此笔记的子笔记（参见 <a class="reference-link" href="../../Note%20Types/Saved%20Search.md">已保存的搜索</a>）。 |
| `workspace` 及相关属性 | 参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md">工作区</a>。 |
| `inbox` | 新笔记的默认收件箱位置。更多信息请参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>。 |
| `sqlConsoleHome` | <a class="reference-link" href="../Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a> 已保存查询的默认位置。 |
| `bookmarked` | 表示此笔记是一个[书签](../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md)。 |
| `bookmarkFolder` | 带有此标签的笔记将作为文件夹出现在书签中（允许访问其子笔记）。更多信息请参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md">书签</a>。 |
| `share*` | 参见 <a class="reference-link" href="../Sharing.md">分享</a> 中的属性参考。 |
| `displayRelations`, `hideRelations` | 在 <a class="reference-link" href="../../Note%20Types/Relation%20Map.md">关系图</a>（包括笔记类型和 <a class="reference-link" href="../Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记地图（链接地图、树状地图）</a> 的通用功能）中应显示/隐藏的关系名称，以逗号分隔。 |
| `titleTemplate` | 作为此笔记子笔记创建的新笔记的默认标题。此值作为 JavaScript 字符串求值，因此可以通过注入的 `now` 和 `parentNote` 变量来丰富动态内容。  <br>  <br>更多信息请参见 <a class="reference-link" href="../Default%20Note%20Title.md">默认笔记标题</a>。 |
| `template` | 此笔记将出现在创建新笔记时可用的模板选择中。更多信息请参见 <a class="reference-link" href="../Templates.md">模板</a>。 |
| `toc` | 控制给定笔记的 <a class="reference-link" href="../../Note%20Types/Text/Table%20of%20contents.md">目录</a> 显示。`#toc` 或 `#toc=show` 始终显示目录，`#toc=false` 始终隐藏它。 |
| `color` | 定义笔记在笔记树、链接等中的颜色。使用任何有效的 CSS 颜色值，如 'red' 或 #a13d5f  <br>注意：此颜色在显示时可能会自动调整，以确保与背景有足够的对比度。 |
| `keyboardShortcut` | 定义一个键盘快捷键，将立即跳转到此笔记。示例：'ctrl+alt+e'。需要重新加载前端才能使更改生效。 |
| `keepCurrentHoisting` | 即使笔记在当前提升的子树中不可显示，打开此链接也不会更改提升状态。 |
| `executeButton` | 将执行当前代码笔记的按钮标题。 |
| `executeDescription` | 与执行按钮一起显示的当前代码笔记的较长描述。 |
| `excludeFromNoteMap` | 带有此标签的笔记将从 <a class="reference-link" href="../../Note%20Types/Note%20Map.md">笔记地图</a> 中隐藏。 |
| `newNotesOnTop` | 新笔记将创建在父笔记的顶部，而不是底部。 |
| `hideHighlightWidget` | 隐藏 <a class="reference-link" href="../../Note%20Types/Text/Highlights%20list.md">高亮列表</a> 小组件。 |
| `hideChildrenOverview` | 隐藏该特定笔记的 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>。 |
| `subtreeHidden` | 从树中隐藏此笔记的所有子笔记，显示一个带有隐藏子笔记计数的徽章。子笔记仍然可以通过搜索或直接链接访问。 |
| `printLandscape` | 导出为 PDF 时，将页面方向从纵向更改为横向。 |
| `printPageSize` | 导出为 PDF 时，更改页面大小。支持的值：`A0`、`A1`、`A2`、`A3`、`A4`、`A5`、`A6`、`Legal`、`Letter`、`Tabloid`、`Ledger`。 |
| `printScale`, `printMargins` | 额外的打印选项，通常通过 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印和导出为 PDF</a> 对话框配置。 |
| `geolocation` | 表示笔记的纬度和经度，以便在 <a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a> 中显示。 |
| `map:*` | 为 <a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a> 定义特定选项。 |
| `calendar:*` | 为 <a class="reference-link" href="../../Collections/Calendar.md">日历</a> 定义特定选项。 |
| `viewType` | 设置子笔记的视图（例如网格或列表）。更多信息请参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>。 |
| `webViewSrc` | 定义 <a class="reference-link" href="../../Note%20Types/Web%20View.md">网页视图</a> 的 URL。 |
| `tabWidth`, `indentWithTabs`, `wrapLines` | 每个笔记的代码编辑器设置：缩进宽度、使用制表符还是空格缩进，以及自动换行。参见 <a class="reference-link" href="../../Note%20Types/Code.md">代码</a>。 |
| `datePattern`, `weekPattern`, `monthPattern`, `quarterPattern`, `yearPattern` | 自定义日/周/月/季度/年笔记的标题命名模式。参见 <a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记</a>。 |
| `enableWeekNote`, `enableQuarterNote` | 在日历层级中启用可选的周和季度笔记；在日历根节点上设置。参见 <a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记</a>。 |
| `fullContentWidth` | 将笔记扩展到编辑器的全宽，忽略配置的内容宽度（对于宽表格很有用）。参见 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Content%20width.md">内容宽度</a>。 |
| `iconPack` | 通过其前缀标识自定义图标包。参见 <a class="reference-link" href="../../Theme%20development/Creating%20an%20icon%20pack.md">创建图标包</a>。 |
| `clipperInbox` | 覆盖 Web Clipper 保存剪辑的默认位置（默认为日记）。参见 <a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">Web Clipper</a>。 |
| `similarNotesWidgetDisabled` | 禁用 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Similar%20Notes.md">相似笔记</a> 功能区选项卡（仅限旧布局）。 |
| `docName` , `docUrl` | 用于应用内帮助的内部使用。 |