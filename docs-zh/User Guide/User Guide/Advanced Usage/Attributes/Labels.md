# 标签

标签是笔记的一种[属性](../Attributes.md)，具有名称和可选的值。

## 常见用例

*   **个人用途的元数据**：为分类分配带可选值的标签，例如 `#year=1999`、`#genre="sci-fi"` 或 `#author="Neal Stephenson"`。这可以与<a class="reference-link" href="Promoted%20Attributes.md">提升属性</a>结合使用，使其显示更加用户友好。
*   **配置**：标签可以配置高级功能或设置（参见下方参考）。
*   **脚本和插件**：用于为笔记标记特殊元数据，例如<a class="reference-link" href="../Advanced%20Showcases/Weight%20Tracker.md">体重追踪器</a>中的 "weight" 属性。

## 使用可视化编辑器创建标签

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar.md">右侧边栏</a>中的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Right%20Sidebar/Attributes%20tab.md">属性选项卡</a>。
2.  按列表末尾的 <span class="tn-icon bx bx-plus"></span>（添加属性）按钮，或通过该区域右上角的 <span class="tn-icon bx bx-plus"></span> 按钮 → _添加新标签_。

在可视化编辑器中：

*   设置所需的名称。
*   可选地，设置标签的值。标签可以没有值。
*   子笔记可以继承此关系，点击该关系并勾选 _可继承_。更多信息请参见<a class="reference-link" href="Attribute%20Inheritance.md">属性继承</a>。

> [!TIP]
> 或者，按 <kbd>Alt</kbd>+<kbd>L</kbd>，这将在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中打开属性详情（与点击现有属性时的视图相同）。

## 手动创建标签

在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Status%20bar.md">状态栏</a>中，按 <span class="tn-icon bx bx-list-check"></span> 按钮以显示属性列表。

*   点击输入框使其获得焦点。
*   要创建一个名为 `myLabel` 且没有值的标签，只需输入 `#myLabel`。
*   要创建一个名为 `myLabel` 且值为 `value` 的标签，只需输入 `#myLabel=value`。
*   如果值包含空格，则文本必须加引号：`#myLabel="Hello world"`。
*   如果字符串包含引号（无论是否包含空格），则文本必须改用单引号括起来：`#myLabel='Hello "world"'`。
*   要创建一个名为 `myLabel` 的可继承标签，只需写 `#myLabel(inheritable)`（无值）或 `#myLabel(inheritable)=value`（有值）。

## 预定义标签

以下是 Trilium 原生支持的标签列表。

> [!TIP]
> 此处列出的一些标签以 `*` 结尾。这意味着存在多个具有相同前缀的标签，请查阅该标签描述中链接的特定页面以获取更多信息。

| 标签 | 描述 |
| --- | --- |
| `disableVersioning` | 禁用特定笔记的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订</a>自动创建。适用于例如大型但不重要的笔记——例如用于脚本的大型 JS 库。 |
| `versioningLimit` | 限制特定笔记的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md">笔记修订</a>最大数量，覆盖全局设置。 |
| `calendarRoot` | 标记应用作<a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记笔记</a>根节点的笔记。只应有一个笔记被如此标记。 |
| `archived` | 从默认搜索结果和对话框中隐藏笔记。已归档的笔记可以选择在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中隐藏。 |
| `excludeFromExport` | 导出时排除此笔记及其子笔记。 |
| `run`、`runOnInstance`、`runAtHour` | 参见<a class="reference-link" href="../../Scripting/Backend%20scripts/Backend%20Events.md">后端事件</a>。 |
| `disableInclusion` | 带有此标签的脚本不会被包含到父脚本执行中。 |
| `sorted`、`sortDirection`、`sortFoldersFirst`、`sortNatural`、`sortLocale`、`top`、`bottom` | 管理自动/永久排序。参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Sorting%20Notes.md">笔记排序</a>。 |
| `hidePromotedAttributes` | 在此笔记上隐藏<a class="reference-link" href="Promoted%20Attributes.md">提升属性</a>。通常在定义继承属性但父笔记不需要它们时有用。 |
| `readOnly` | 将笔记标记为始终[只读](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)，前提是它是受支持的笔记类型（文本、代码、mermaid）。 |
| `autoReadOnlyDisabled` | 为给定笔记禁用自动[只读模式](../../Basic%20Concepts%20and%20Features/Notes/Read-Only%20Notes.md)。 |
| `appCss` | 标记加载到 Trilium 应用程序中的 CSS 笔记，因此可用于修改 Trilium 的外观。更多信息请参见<a class="reference-link" href="../../Theme%20development/Custom%20app-wide%20CSS.md">自定义应用级 CSS</a>。 |
| `appTheme` | 标记完整的 Trilium 主题 CSS 笔记，因此可在 Trilium 选项中选用。更多信息请参见<a class="reference-link" href="../../Theme%20development">主题开发</a>。 |
| `appThemeBase` | 设置为 `next`、`next-light` 或 `next-dark`，以使用相应的 TriliumNext 主题（自动、浅色或深色）作为自定义主题的基础，而非旧版主题。更多信息请参见<a class="reference-link" href="../../Theme%20development/Customize%20the%20Next%20theme.md">自定义 Next 主题</a>。 |
| `customFont` | 将字体标记为可在选项 → 外观字体选择中选择。参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Themes/Personalizing%20the%20font.md">个性化字体</a>。 |
| `cssClass` | 此标签的值将作为 CSS 类添加到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Note%20Tree.md">笔记树</a>中代表给定笔记的节点上。这对于高级主题定制很有用。可用于模板笔记。 |
| `iconClass` | 此标签的值将作为 CSS 类添加到树上的图标，有助于在树中视觉区分笔记。示例可以是 bx bx-home——图标取自 boxicons。可用于模板笔记。 |
| `pageSize` | 指定<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>中每页的项目数。 |
| `customRequestHandler` | 参见<a class="reference-link" href="../Custom%20Request%20Handler.md">自定义请求处理器</a>。 |
| `customResourceProvider` | 参见<a class="reference-link" href="../Custom%20Resource%20Providers.md">自定义资源提供者</a>。 |
| `widget` | 将此笔记标记为自定义小组件，将被添加到 Trilium 组件树中。更多信息请参见<a class="reference-link" href="../../Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义组件</a>。 |
| `searchHome` | 新的搜索笔记将作为此笔记的子笔记创建（参见<a class="reference-link" href="../../Note%20Types/Saved%20Search.md">保存的搜索</a>）。 |
| `workspace` 及相关属性 | 参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Workspaces.md">工作区</a>。 |
| `inbox` | 新笔记的默认收件箱位置。更多信息请参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20Inbox.md">笔记收件箱</a>。 |
| `sqlConsoleHome` | <a class="reference-link" href="../Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a>保存查询的默认位置。 |
| `bookmarked` | 表示此笔记是[书签](../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md)。 |
| `bookmarkFolder` | 带有此标签的笔记将在书签中显示为文件夹（允许访问其子笔记）。更多信息请参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Navigation/Bookmarks.md">书签</a>。 |
| `share*` | 参见<a class="reference-link" href="../Sharing.md">分享</a>中的属性参考。 |
| `displayRelations`、`hideRelations` | 以逗号分隔的关系名称，应在<a class="reference-link" href="../../Note%20Types/Relation%20Map.md">关系图</a>（包括笔记类型和<a class="reference-link" href="../Note%20Map%20(Link%20map%2C%20Tree%20map).md">笔记图（链接图、树图）</a>通用功能）中显示/隐藏。 |
| `titleTemplate` | 作为此笔记子笔记创建的笔记的默认标题。此值作为 JavaScript 字符串求值，因此可以通过注入的 `now` 和 `parentNote` 变量来丰富动态内容。        <br>  <br>更多信息请参见<a class="reference-link" href="../Default%20Note%20Title.md">默认笔记标题</a>。 |
| `template:titleTemplate` | 在模板笔记上设置：从模板创建的笔记的默认标题，优先于父笔记的 `titleTemplate`。求值方式与 `titleTemplate` 相同。参见<a class="reference-link" href="../Default%20Note%20Title.md">默认笔记标题</a>。 |
| `template` | 创建新笔记时，此笔记将出现在可用模板的选择中。更多信息请参见<a class="reference-link" href="../Templates.md">模板</a>。 |
| `color` | 定义笔记在笔记树、链接等中的颜色。使用任何有效的 CSS 颜色值，如 'red' 或 #a13d5f         <br>注意：显示时此颜色可能会自动调整，以确保与背景有足够的对比度。 |
| `keyboardShortcut` | 定义一个键盘快捷键，将立即跳转到此笔记。示例：'ctrl+alt+e'。需要重新加载前端才能使更改生效。 |
| `keepCurrentHoisting` | 打开此链接不会改变提升状态，即使该笔记在当前提升的子树中不可显示。 |
| `executeButton` | 将执行当前代码笔记的按钮的标题 |
| `executeDescription` | 当前代码笔记的较长描述，与执行按钮一起显示 |
| `excludeFromNoteMap` | 带有此标签的笔记将从<a class="reference-link" href="../../Note%20Types/Note%20Map.md">笔记图</a>中隐藏。 |
| `newNotesOnTop` | 新笔记将创建在父笔记的顶部，而不是底部。 |
| `hideChildrenOverview` | 隐藏该特定笔记的<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>。 |
| `subtreeHidden` | 在树中隐藏此笔记的所有子笔记，显示一个带有隐藏子笔记数量的徽章。子笔记仍可通过搜索或直接链接访问。 |
| `printLandscape` | 导出为 PDF 时，将页面方向从纵向改为横向。 |
| `printPageSize` | 导出为 PDF 时，更改页面大小。支持的值：`A0`、`A1`、`A2`、`A3`、`A4`、`A5`、`A6`、`Legal`、`Letter`、`Tabloid`、`Ledger`。 |
| `printScale`、`printMargins` | 额外的打印选项，通常通过<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Printing%20%26%20Exporting%20as%20PDF.md">打印与导出为 PDF</a>对话框进行配置。 |
| `geolocation` | 表示笔记的纬度和经度，将显示在<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>中。 |
| `geoShape` | 表示在<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>上绘制的[形状](../../Collections/Geo%20Map/Drawing%20shapes.md)（例如区域、矩形、圆形）的坐标点。 |
| `map:*` | 为<a class="reference-link" href="../../Collections/Geo%20Map.md">地理地图</a>定义特定选项。 |
| `calendar:*` | 为<a class="reference-link" href="../../Collections/Calendar.md">日历</a>定义特定选项。 |
| `viewType` | 设置子笔记的视图（例如网格或列表）。更多信息请参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/Notes/Note%20List.md">笔记列表</a>。 |
| `webViewSrc` | 定义<a class="reference-link" href="../../Note%20Types/Web%20View.md">网页视图</a>的 URL。 |
| `tabWidth`、`indentWithTabs`、`wrapLines` | 每笔记代码编辑器设置：缩进宽度、使用制表符还是空格缩进，以及自动换行。参见<a class="reference-link" href="../../Note%20Types/Code.md">代码</a>。 |
| `datePattern`、`weekPattern`、`monthPattern`、`quarterPattern`、`yearPattern` | 自定义日/周/月/季度/年笔记的标题命名模式。参见<a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记笔记</a>。 |
| `enableWeekNote`、`enableQuarterNote` | 在日历层级中启用可选的周笔记和季度笔记；在日历根节点上设置。参见<a class="reference-link" href="../Advanced%20Showcases/Day%20Notes.md">日记笔记</a>。 |
| `fullContentWidth` | 将笔记扩展到完整编辑器宽度，忽略配置的内容宽度（适用于宽表格）。参见<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Content%20width.md">内容宽度</a>。 |
| `iconPack` | 通过前缀标识自定义图标包。参见<a class="reference-link" href="../../Theme%20development/Creating%20an%20icon%20pack.md">创建图标包</a>。 |
| `clipperInbox` | 覆盖网页剪藏保存剪藏内容的默认位置（默认为日记笔记）。参见<a class="reference-link" href="../../Installation%20%26%20Setup/Web%20Clipper.md">网页剪藏</a>。 |
| `docName`、`docUrl` | 内部用于应用内帮助。 |
| `aiQuickAction` | 定义用于<a class="reference-link" href="../../Note%20Types/Text/In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>快捷操作的自定义提示词。 |