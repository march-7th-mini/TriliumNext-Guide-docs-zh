# 创建图标包
> [!NOTE]
> 本页面逐步说明如何创建自定义图标包。关于如何使用已有图标包的通用说明，请参阅 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md">图标包</a>。

首先阅读快速流程以了解整体步骤。之后有一个具体示例（Phosphor），附带一个可运行以生成清单的小型 Node.js 脚本。

## 快速流程（你需要做什么）

1.  验证图标集是字体（格式之一：.woff2、.woff、.ttf）。
2.  获取将图标名称映射到 Unicode 码点的列表（通常以 JSON 形式提供，如 `selection.json` 或 CSS 文件）。
3.  创建一个清单 JSON，将图标 ID 映射到字形和搜索词。
4.  创建一个类型为代码的 Trilium 笔记，将语言设置为 JSON，将清单粘贴为笔记内容。
5.  将字体文件作为附件上传到同一笔记（MIME 类型必须为 `font/woff2`、`font/woff` 或 `font/ttf`，角色为 `file`）。
6.  为笔记添加标签 `#iconPack=<前缀>`（前缀：仅限字母数字、连字符、下划线）。
7.  刷新客户端并验证图标包是否出现在图标选择器中。

## 验证图标集

第一步是分析要打包的图标集是否可以集成到 Trilium 中。

Trilium 仅支持**基于字体的图标集**，格式如下：

| 扩展名 | MIME 类型 | 描述 |
| --- | --- | --- |
| `.woff2` | `font/woff2` | 推荐使用，压缩率高（体积小）。 |
| `.woff` | `font/woff` | 兼容性更高，但字体文件较大。 |
| `.ttf` | `font/ttf` | 最常见，但字体文件最大。 |

Trilium **不支持**以下格式：

*   基于 SVG 的字体。
*   单独的 SVG 文件。
*   `.eot` 字体（旧式且专有）。
*   双色图标，因为它需要特殊的 CSS 格式，而 Trilium 不支持。
*   任何未在 _支持的格式_ 部分中指定的其他字体格式。

在这种情况下，必须手动将字体转换为支持的格式之一（理想情况下为 `.woff2`）。

## 清单格式

清单是一个 JSON 对象，包含一个 `icons` 映射。每个条目的键是您将使用的 CSS/类 ID（Trilium 在渲染时使用 CSS 类）。值对象：

*   glyph：单个字符（字形）——可以是转义的 Unicode（例如 "\\ue9c2"）或字面字符。
*   terms：搜索别名数组；第一个术语用作选择器中的显示名称。

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
> *   您可以将字形提供为转义的 `\uXXXX` 序列或实际的 UTF-8 字符。
> *   也可以在 JSON 中使用未转义的字形。它看起来会有些奇怪（例如 ），但无论如何都会正确渲染。
> *   清单键（例如 `ph-acorn`）应与字体使用的类名匹配（前缀 + 名称是常见模式）。

## 具体示例：Phosphor 图标

[Phosphor 图标](https://phosphoricons.com/) 提供一个 `selection.json`，其中包含 `properties.code`（码点）和 `properties.name`（图标名称）。目标：将其转换为 Trilium 的清单。

`selection.json` 示例摘录：

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

一个用于生成清单的小型 Node.js 脚本（将 `selection.json` 放在同一目录中，并使用 Node 20+ 运行）：

```javascript
import { join } from "node:path";
import { readFileSync, writeFileSync } from "node:fs";

function processIconPack(packName) {
    const path = join(packName);
    const selectionMeta = JSON.parse(readFileSync(join(path, "selection.json"), "utf-8"));
    const icons = {};

    for (const icon of selectionMeta.icons) {
        let name = icon.properties.name;
        if (name.endsWith(`-${packName}`)) {
            name = name.split("-").slice(0, -1).join("-");
        }

        const id = `ph-${name}`;
        icons[id] = {
            glyph: `${String.fromCharCode(icon.properties.code)}`,
            terms: [ name ]
        };
    }

    writeFileSync("manifest.json", JSON.stringify(icons, null, 2), "utf8");
    console.log("manifest.json created");
}

processIconPack("light");
```

脚本的使用方法：

*   将 `selection.json` 和 `build-manifest.js` 放在一个文件夹中。
*   运行：node build-manifest.js
*   脚本会写入 `manifest.json` — 打开它，验证内容，然后复制到 Trilium 代码笔记中（语言：JSON）。

> [!TIP]
> **处理 CSS 时注意转义格式**
> 
> CSS 中的 Unicode 转义语法（`"\ea3f"`）与 JSON 中的（`"\uea3f"`）不同。注意 JSON 转义是 `\u` 而不是 `\`。
> 
> 作为更紧凑的替代方案，可以直接提供未转义的字符，因为支持 UTF-8。

### 分配前缀

在图标包可以使用之前，需要定义一个前缀。此前缀唯一标识图标包，以便在整个应用程序中使用。

为此，Trilium 使用与内部图标包（Boxicons）相同的格式。例如，当设置了 Boxicons 的图标时，它看起来像这样：`#iconClass="bx bxs-sushi"`。在这种情况下，图标包前缀是 `bx`，图标类名是 `bxs-sushi`。

为了使图标包被识别，必须在前缀中指定 `#iconPack` 标签。

对于我们的 Phosphor 图标示例，我们可以使用 `ph` 前缀，因为它也与原始 CSS 中设置的前缀匹配。所以在这种情况下，它将是 `#iconPack=ph`。

> [!IMPORTANT]
> 前缀必须仅由字母数字字符、连字符和下划线组成。如果前缀不符合这些约束，图标包将被忽略，并且错误将记录在 <a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a> 中。

## 创建 Trilium 图标包笔记

1.  创建一个类型为 _代码_ 的笔记。
2.  将语言设置为 _JSON_。
3.  重命名笔记。笔记的名称也将是图标列表中显示的图标包名称。
4.  将上一步生成的清单复制并粘贴为此笔记的内容。
5.  转到 [笔记附件](../Basic%20Concepts%20and%20Features/Notes/Attachments.md) 并上传字体文件（`.woff2`、`.woff`、`.ttf` 格式）。
    1.  Trilium 通过 MIME 类型从附件中识别要使用的字体，确保上传附件后 MIME 类型正确显示（例如 `font/woff2`）。
    2.  确保 `role` 显示为 `file`，否则字体将无法被识别。
    3.  支持多个附件，但 Trilium 只会按优先级顺序实际使用一种字体：`.woff2`、`.woff`、`.ttf`。因此，每个图标包上传多个字体没有太大意义。
6.  添加标签：`#iconPack=<前缀>`（对于 Phosphor 示例：`#iconPack=ph`）。

### 最终步骤

*   [刷新客户端](../Troubleshooting/Refreshing%20the%20application.md)
    *   更改笔记的图标，并在右上角查找 _筛选器_ 图标。
    *   检查新的图标包是否显示在那里，并点击它以查看完整的图标列表。
    *   浏览大部分项目以查找问题，例如缺少图标、名称错误（某些图标具有可能导致问题的别名/术语）。
*   可选地，为此笔记分配一个来自新图标包的图标。此图标将用于图标包筛选器中，以进行视觉区分。
*   然后可以将图标包 [导出为 ZIP](../Basic%20Concepts%20and%20Features/Import%20%26%20Export.md) 以分发给其他用户。
    *   需要注意的是，图标包默认被视为“不安全”，因此在导入 ZIP 时必须禁用“安全模式”。
    *   考虑将新用户链接到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/Themes/Icon%20Packs.md">图标包</a> 文档，以便他们了解如何导入和使用图标包。

### 故障排除

如果图标包没有显示，请查看 <a class="reference-link" href="../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a> 以获取线索。

*   一个示例是无法检索字体：`ERROR: Icon pack is missing WOFF/WOFF2/TTF attachment: Boxicons v3 400 (dup) (XRzqDQ67fHEK)`。
*   确保前缀是唯一的，并且没有被其他图标包占用。当有两个具有相同前缀的图标包时，只会使用一个。如果出现这种情况，服务器日志会指示。
*   确保前缀仅由字母数字字符、连字符和下划线组成。