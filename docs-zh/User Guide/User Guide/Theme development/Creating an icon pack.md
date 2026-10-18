# 创建图标包
> [!NOTE]
> 本页逐步说明如何创建自定义图标包。关于如何使用已有图标包的通用说明，请参见<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md">图标包</a>。

请先阅读快速流程以了解整体步骤。之后有一个具体示例（Phosphor），附带一个可运行的小型 Node.js 脚本，用于生成清单。

## 快速流程（你需要做的事）

1.  确认图标集是字体文件（.woff2、.woff、.ttf 之一）。
2.  获取一份将图标名称映射到 Unicode 码点的列表（通常以 `selection.json` 或 CSS 文件等形式提供）。
3.  创建一个清单 JSON，将图标 id 映射到字形和搜索词。
4.  创建一个类型为代码的 Trilium 笔记，将语言设为 JSON，把清单粘贴为笔记内容。
5.  将字体文件作为附件上传到同一笔记（MIME 类型必须为 `font/woff2`、`font/woff` 或 `font/ttf`，角色为 `file`）。
6.  为笔记添加标签 `#iconPack=<prefix>`（前缀：仅限字母、数字、连字符、下划线和非 ASCII 字符）。
7.  刷新客户端，确认图标包出现在图标选择器中。

## 验证图标集

第一步是分析待打包的图标集能否集成到 Trilium 中。

Trilium 仅支持**基于字体的图标集**，格式如下：

| 扩展名 | MIME 类型 | 说明 |
| --- | --- | --- |
| `.woff2` | `font/woff2` | 推荐，压缩率高（体积小）。 |
| `.woff` | `font/woff` | 兼容性更高，但字体文件更大。 |
| `.ttf` | `font/ttf` | 最常见，但字体体积最大。 |

Trilium **不支持**以下格式：

*   基于 SVG 的字体。
*   单独的 SVG。
*   `.eot` 字体（遗留且专有）。
*   双色图标，因为它需要 Trilium 不支持的特殊 CSS 格式。
*   _支持的格式_ 一节中未指定的任何其他字体格式。

在这种情况下，必须手动将字体转换为受支持的格式之一（理想情况下为 `.woff2`）。

## 清单格式

清单是一个 JSON 对象，包含一个 `icons` 映射。每个条目的键是你将使用的 CSS/类 id（Trilium 在渲染时使用该 CSS 类）。值对象：

*   glyph：单个字符（字形）——可以是转义的 Unicode（例如 "\\ue9c2"）或字面字符。
*   terms：搜索别名数组；第一个词用作选择器中的显示名称。

最小清单示例：

```
{
  "icons": {
    "ph-acorn": {
      "glyph": "\uea3f",
      "terms": ["acorn", "nut"]
    },
    "ph-book": {
      "glyph": "\uea40",
      "terms": ["book", "read"]
    }
  }
}
```

> [!NOTE]
> *   你可以用转义的 `\uXXXX` 序列或实际的 UTF‑8 字符来提供字形。CSS 形式（`\ea3f`，即样式表中 `content` 的写法）也被接受，因此从字体自带 CSS 中复制出的字形可直接使用。
> *   也可以在 JSON 中使用未转义的字形。它看起来会很奇怪（例如 ），但无论如何都会被正确渲染。
> *   清单的键（例如 `ph-acorn`）应与字体使用的类名匹配（前缀 + 名称是常见模式）。
> *   与前缀一样，清单的键会成为 CSS 类名，因此只能包含字母、数字、连字符、下划线和非 ASCII 字符。标点和空白（例如 `ph.acorn` 或 `ph acorn`）不能用作类名；使用此类键的图标会被跳过，并在<a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>中记录错误，而图标包的其余部分仍会加载。

## 具体示例：Phosphor Icons

[Phosphor Icons](https://phosphoricons.com/) 提供了一个 `selection.json`，其中包含 `properties.code`（码点）和 `properties.name`（图标名称）。目标：将其转换为 Trilium 的清单。

`selection.json` 摘录示例：

```
{
  "icons": [
    {
      "icon": {
        "paths": [ /* [...] */ ],
        "grid": 0,
        "attrs": [{}],
        "isMulticolor": false,
        "isMulticolor2": false,
        "tags": ["acorn"]
      },
      "attrs": [{}],
      "properties": {
        "id": 0,
        "order": 1513,
        "name": "acorn",
        "code": 60314,
        "ligatures": "acorn",
        "prevSize": 16
      },
      "setIdx": 0,
      "setId": 0,
      "iconIdx": 0
    },
    /* [...] */
  ]
}
```

<details open="">
    <summary>一个用于生成清单的小型 Node.js 脚本</summary>
    <p>将 <code>selection.json</code> 放在同一目录下，并使用 Node 20+ 运行）：</p>
    <pre><code class="language-text-javascript">import { join } from "node:path";
import { readFileSync, writeFileSync } from "node:fs";&#10;
function processIconPack(packName) {
    const path = join(packName);
    const selectionMeta = JSON.parse(readFileSync(join(path, "selection.json"), "utf-8"));
    const icons = {};&#10;
    for (const icon of selectionMeta.icons) {
        let name = icon.properties.name;
        if (name.endsWith(`-${packName}`)) {
            name = name.split("-").slice(0, -1).join("-");
        }&#10;
        const id = `ph-${name}`;
        icons[id] = {
            glyph: `${String.fromCharCode(icon.properties.code)}`,
            terms: [ name ]
        };
    }&#10;
    writeFileSync("manifest.json", JSON.stringify(icons, null, 2), "utf8");
    console.log("manifest.json created");
}&#10;
processIconPack("light");</code></pre>
    <p>脚本的使用方法：</p>
    <ul>
        <li>将 <code>selection.json</code> 和 <code>build-manifest.js</code> 放在一个文件夹中。</li>
        <li>运行：node build-manifest.js</li>
        <li>脚本会写出 <code>manifest.json</code>——打开它，验证内容，然后复制到 Trilium 代码笔记中（语言：JSON）。</li>
    </ul>
</details>

> [!TIP]
> **处理 CSS 时注意转义格式**
> 
> CSS 中的 Unicode 转义语法（`"\ea3f"`）与 JSON（`"\uea3f"`）不同。请注意 JSON 转义是 `\u` 而不是 `\`。两种形式都被接受：在 JSON 中将反斜杠本身写作 `"\\ea3f"` 以保留 CSS 转义，或将其转换为 JSON 转义 `"\uea3f"`。
> 
> 作为更紧凑的替代方案，可直接提供未转义的字符，因为支持 UTF-8。

### 分配前缀

图标包在使用前需要定义前缀。该前缀唯一标识图标包，以便在整个应用中使用。

为此，Trilium 采用与内部图标包（Boxicons）相同的格式。例如，当设置一个来自 Boxicons 的图标时，它看起来像这样：`#iconClass="bx bxs-sushi"`。在此例中，图标包前缀是 `bx`，图标类名是 `bxs-sushi`。

为了让图标包被识别，必须在 `#iconPack` 标签中指定前缀。

对于我们的 Phosphor Icons 示例，我们可以使用 `ph` 前缀，因为它也与原始 CSS 中设置的前缀匹配。因此在此例中为 `#iconPack=ph`。

> [!IMPORTANT]
> 前缀只能由字母、数字、连字符、下划线和非 ASCII 字符组成。如果前缀不符合这些约束，图标包将被忽略，并在<a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>中记录错误。

## 创建 Trilium 图标包笔记

1.  创建一个类型为 _代码_ 的笔记。
2.  将语言设为 _JSON_。
3.  重命名笔记。笔记的名称也将是图标包在图标列表中显示的名称。
4.  复制并粘贴上一步生成的清单作为此笔记的内容。
5.  转到[笔记附件](../Basic%20Concepts%20and%20Features/Notes/Attachments.md)并上传字体文件（`.woff2`、`.woff`、`.ttf` 格式）。
    1.  Trilium 通过 MIME 类型从附件中识别要使用的字体，请确保上传附件后 MIME 类型显示正确（例如 `font/woff2`）。
    2.  确保 `role` 显示为 `file`，否则字体将无法被识别。
    3.  支持多个附件，但 Trilium 按以下优先顺序实际只会使用一个字体：`.woff2`、`.woff`、`.ttf`。因此，每个图标包上传多个字体没有太大意义。
6.  添加标签：`#iconPack=<prefix>`（Phosphor 示例：`#iconPack=ph`）。

### 最后步骤

*   [刷新客户端](../Troubleshooting/Refreshing%20the%20application.md)
    *   更改笔记的图标，并在右上角寻找 _筛选_ 图标。
    *   检查新图标包是否显示在那里，点击它以查看完整图标列表。
    *   浏览大部分条目以查找问题，例如缺失图标、名称错误（某些图标有别名/搜索词可能导致问题）。
*   可选地，为此笔记分配一个来自新图标包的图标。该图标将用于图标包筛选器中以作视觉区分。
*   然后可以将图标包[导出为 ZIP](../Basic%20Concepts%20and%20Features/Import%20%26%20Export.md)以便分发给其他用户。
    *   需要注意的是，图标包默认被视为“不安全”，因此导入 ZIP 时必须禁用“安全模式”。
    *   考虑引导新用户查阅<a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md">图标包</a>文档，以了解如何导入和使用图标包。

### 故障排查

如果图标包没有显示，请查看<a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a>寻找线索。

*   一个例子是字体无法获取：`ERROR: Icon pack is missing WOFF/WOFF2/TTF attachment: Boxicons v3 400 (dup) (XRzqDQ67fHEK)`。
*   确保前缀唯一且未被其他图标包占用。当有两个前缀相同的图标包时，只会使用其中一个。服务器日志会指示是否出现这种情况。
*   确保前缀仅由字母、数字、连字符、下划线和非 ASCII 字符组成。
*   如果图标包加载了但个别图标缺失，请在日志中查找 `Skipping icon '<key>' of icon pack`——该键使用了允许集之外的字符，需要在清单中重命名。