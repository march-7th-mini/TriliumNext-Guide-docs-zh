# AI
Trilium 可以连接到大语言模型，并将其用作直接在你的笔记上工作的助手：针对你正在阅读的笔记提问，让它起草或重构内容，或者让它为你编写脚本和小组件。

该集成默认关闭，在你启用并配置提供商之前不会执行任何操作；Trilium 本身不附带任何模型。你选择的提供商决定了你的笔记如何传输：按使用量计费的云 API、你已付费的订阅，或在你自己的硬件上运行的模型（在这种情况下任何内容都不会离开本机）。有关每种方式涉及的内容，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>；有关具体发送了哪些内容，请参阅 <a class="reference-link" href="AI/Privacy.md">隐私</a>。

启用后，助手可通过以下形式使用：

*   作为一种专用笔记类型，它可以通过工具读取和修改笔记；如果你希望它只看到你输入的内容，可以在每次对话中关闭此功能。
*   右侧边栏中的一个面板，其行为与专用笔记类型类似，但它还可以选择性地访问当前笔记。
*   一个 <a class="reference-link" href="Note%20Types/Text/In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>，它带有对选中文本进行操作的内置操作（如校对、总结），以及 <a class="reference-link" href="Note%20Types/Text/In-editor%20AI%20assistant/Custom%20AI%20quick%20actions.md">自定义 AI 快捷操作</a>。

## 功能亮点

*   基于聊天的界面，消息实时流式显示。
*   为 AI 提供当前正在查看的笔记作为上下文。
*   用于修改笔记内容、创建新笔记等的工具。
*   关于上下文窗口使用情况和每条消息定价的统计信息。
*   用于多模态聊天的附件（图像、文本文件、PDF）。
*   可选的 MCP，允许外部聊天工具（例如 Claude Code）对 Trilium 中的笔记进行操作。

## 示例用例

*   创建任意类型的 <a class="reference-link" href="Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a>。
*   轻松创建 <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>，例如 _为我创建一个渲染笔记，让我可以玩井字棋。确保使用 Preact 而不是旧版的 jQuery。_
*   为 <a class="reference-link" href="Collections/Dashboard.md">仪表板</a> 创建小组件，例如计算器、秒表、番茄钟。

> [!NOTE]
> 众所周知，Claude Sonnet 在几乎没有指导的情况下也能生成非常好的前端或后端脚本，因为该 AI 已被教导如何生成它们。

## 大语言模型提供商

Trilium 支持四种不同类型的提供商：

*   **云提供商**  
    使用 API 密钥按使用量付费，与你可能已有的任何订阅分开计费
    *   Anthropic (Claude)
    *   OpenAI (GPT)
    *   Google (Gemini)
    *   DeepSeek
*   **基于订阅**  
    复用现有订阅，而不是按使用量付费。
    *   目前仅支持 Claude Code。
*   **本地或自托管的大语言模型解决方案**
    *   Ollama
    *   LM Studio。
*   **自定义 OpenAI 兼容端点**  
    用于 Trilium 不直接支持的其他提供商，无论是本地还是托管的（例如 OpenRouter、Groq、Mistral）。

有关每个提供商的更多信息，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>。请参阅专门的 <a class="reference-link" href="AI/Privacy.md">隐私</a> 页面，以更好地了解发送给提供商的数据。

## 启用 AI 集成

要启用 AI 集成，只需转到 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_，然后按下对话框右上角的开关并配置一个提供商。

## 创建新对话

有两种不同的聊天界面：

*   侧边栏中的一个。
*   一种专用笔记类型。

### 侧边栏界面

### 专用笔记类型

专用对话笔记与侧边栏界面类似，但它使较长的对话更易于阅读。

与侧边栏不同，AI 不会感知到它所在的当前笔记。

### 模板

对话笔记可以设置为 <a class="reference-link" href="Advanced%20Usage/Templates.md">模板</a>，以便轻松复用。整个对话历史都会被保留，从而允许对 LLM 进行一种基本形式的专门化，现有对话就像系统提示一样起作用。

### 模型选择

在 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> 中配置提供商后，下一步是选择可用于聊天的模型。

模型仅在模型选择列表可见时从提供商动态获取。要更改模型列表，只需按下模型选择框中的编辑按钮。

已知模型会显示定价信息。定价信息（每百万 token 的价格）内嵌在应用程序中（使用 LiteLLM 数据的子集），并随 Trilium 的新版本更新。本地提供商被视为免费，而自定义端点提供商不提供任何定价信息。

## 功能

### 网络搜索

AI 可以选择性地搜索网络，以查找有关特定主题的更多信息。

搜索来源在聊天底部模型选择器旁边的 <span class="tn-icon bx bx-shield-quarter"></span> _工具_ 菜单中的 _网络搜索_ 下选择：

*   _禁用_ 会为此对话关闭网络搜索。
*   _使用模型的内置搜索_（默认值）让模型使用其提供商自有的搜索进行搜索。Anthropic、OpenAI 和 Google Gemini 模型都有内置搜索，Claude Code、Google Antigravity 和 OpenAI Codex 也有。DeepSeek、Ollama、LM Studio 和自定义端点没有，因此对于它们的模型此选项会被禁用。
*   搜索提供商（Brave Search、Tavily、Exa、Serper、Perplexity 或 SearXNG）则通过该服务进行搜索，无论哪个模型在回答。搜索提供商在 AI 设置的 _搜索提供商_ 部分添加，该部分可通过菜单中 _网络搜索_ 标题旁的 <span class="tn-icon bx bx-cog"></span> 按钮打开。浏览器版本无法使用 Brave Search、Exa 或 Perplexity，因为它们的服务拒绝来自网页的请求，所以它们在那里显示为禁用状态。

要使用 SearXNG，请通过在该实例的 `settings.yml` 中向搜索格式添加 `json` 来启用其 JSON 输出。SearXNG 默认关闭 JSON，没有它每次搜索都会失败。

```yaml
search:
  formats:
    - html
    - json
```

SearXNG 不使用 API 密钥，因此请将 API 密钥留空。仅当你的实例位于需要令牌的代理后面时才填写它；Trilium 会将其作为 bearer token 在 `Authorization` 头中发送。

网络搜索是否开启按对话保留；搜索来源由所有对话共享。当前模型无法使用的选择会保留在菜单中，但处于禁用状态；将鼠标悬停在其旁边的 <span class="tn-icon bx bx-info-circle"></span> 图标上即可查看原因。Claude Code、GitHub Copilot、Google Antigravity 和 OpenAI Codex 运行它们自己的工具，因此它们无法使用搜索提供商。

在聊天中，通过搜索提供商进行的搜索会在其行首显示该提供商的徽标，而不是 <span class="tn-icon bx bx-search"></span> 放大镜；将鼠标悬停在徽标上即可查看提供商名称。

使用搜索提供商时，模型还可以将其找到的页面，或你提供给它的链接，作为文本读取：Trilium 会自行获取该页面，并将最多前 20,000 个字符交给模型。你自己机器或网络上的地址会被拒绝。在浏览器版本中，大多数网站不允许以这种方式被读取，因此在那里读取页面通常会失败。

### 思考

某些模型在回答之前会进行推理。当模型正在思考时，其推理过程会在一个加载指示器下完整显示；完成后，它会折叠为回复上方一行可折叠的 _思考过程_。

模型思考的程度按对话设置，具体方式取决于模型，有以下两种之一：

*   大多数模型有一个 <span class="tn-icon bx bx-brain"></span> _扩展思考_ 按钮，位于 <span class="tn-icon bx bx-shield-quarter"></span> _工具_ 按钮旁边。
*   提供多个推理级别的模型（DeepSeek V4、OpenAI Codex、Antigravity）则在模型选择器旁边有一个 <span class="tn-icon bx bx-brain"></span> 推理强度下拉菜单。在提供的情况下，_无_ 会关闭思考；更高的级别对困难问题给出更好的答案，但耗时更长、成本更高。

> [!NOTE]
> 只有在 Trilium 知道模型的级别后，强度下拉菜单才会出现。对于使用较早版本 Trilium 设置的 DeepSeek 提供商，请在模型选择框中编辑该提供商并按下 _保存_ 一次。

### 笔记访问（工具）

工具允许智能体式 AI 直接在你的 Trilium 实例中理解并操作笔记。

此功能默认开启。要关闭它，请按下聊天底部模型选择器旁边的 <span class="tn-icon bx bx-shield-quarter"></span> _工具_ 按钮，然后关闭 _笔记访问_。当笔记访问或网络搜索开启时，_工具_ 按钮会高亮显示。

以下是 Trilium 为 LLM 提供的一些工具：

*   在笔记级别：
    *   搜索笔记
    *   获取笔记的元数据或内容。
    *   编辑笔记
        *   LLM 有多种编辑笔记的机制：完全重写、查找/替换文本序列或追加。
        *   在重写笔记时，LLM 还可以更改其类型（例如从文本笔记更改为代码笔记）或代码笔记的语言，并重写内容以匹配。
        *   每当 AI 进行更改时，都会保存一个[修订版本](Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md)，以便能够还原任何不需要的更改。
    *   创建新笔记
        *   当被要求绘制图形时，LLM 可以创建 SVG 图像笔记，或将现有笔记转换为 SVG 图像笔记。它只能编写 SVG 图像，不能编写 PNG 等其他格式。
    *   重命名或删除笔记。
*   在属性级别：
    *   获取属性的完整列表，或某个特定属性。
    *   设置属性的值。
        *   运行代码的属性，例如 `#run`、`#widget` 或 `~renderNote`，会以 `disabled:` 前缀保存（例如 `#disabled:widget`），与安全导入禁用它的方式相同（请参阅 <a class="reference-link" href="Basic%20Concepts%20and%20Features/Active%20content.md">活动内容</a>）。如果该笔记已经启用了该属性，AI 会将其移除，因此在启用新值之前它们都不会运行。AI 会告诉你它在哪个笔记上；检查代码，然后使用笔记标题旁活动内容徽章旁边的开关启用它，或者对于 <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>，使用笔记中的 _启用渲染笔记_ 按钮。
    *   删除属性。
*   在树级别：
    *   获取笔记的直接子节点。
    *   获取笔记的整个子树。
    *   将笔记移动或克隆到其他地方。
*   对于 <a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>：
    *   获取附件的元数据。
    *   获取附件的内容。
*   技能（请参阅专门章节）。

AI 使用的每个工具都会在聊天中显示为一行，标明该工具以及它所操作的笔记或查询；重命名的笔记会显示其先前的标题并加删除线，删除的笔记其标题加删除线，移动的笔记显示它从哪里移动到哪里，AI 读取、设置或删除的属性显示为一个胶囊（删除后加删除线），附件显示其标题、笔记和大小，AI 读取的网页显示为链接。只有当有内容可内联阅读时，该行才会展开：搜索找到的笔记、网络搜索找到的页面、图标搜索找到的图标、AI 读取的笔记的类型、属性或内容开头、笔记的所有属性、附件或网页的文本、AI 查阅的用户指南页面或其目录（两者都在帮助面板中打开）、笔记的子节点或整个子树、AI 写入它所创建、重写或添加到的笔记的内容、编辑的更改，或工具失败的原因。搜索还会显示它找到了多少笔记、它所限制的树的部分（如果有），以及 AI 请求的匹配数量；它列出的每个笔记点击即可打开。要确切查看 AI 发送给工具的内容以及它返回的内容，请将鼠标悬停在该行上，然后按下其旁边的 <span class="tn-icon bx bx-code-alt"></span> 按钮；在触摸屏上该按钮始终显示。

当 AI 仍在工作时回复停止移动几秒钟时，例如当它读取工具返回的内容时，其下方会出现一行 _仍在工作…_，直到回复的下一部分到达。

> [!WARNING]
> 目前笔记工具**没有实现权限管理**，这意味着 LLM 可能会删除现有笔记或用笔记弄乱树。通常大多数操作都很容易撤销（删除笔记、恢复已删除的笔记、还原对笔记的修改），但有些操作更难还原（例如设置属性，因为没有属性历史记录）。

> [!NOTE]
> Gemini 在笔记访问开启时无法使用其内置搜索。在开启时，_工具_ 菜单中的内置搜索选项会被禁用并说明原因；搜索提供商在笔记访问开启时可以正常工作。

### 附件

自 Trilium v0.140.0 起，<a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a> 支持多模态聊天：

*   光栅图像（作为视觉输入发送，SVG 除外），支持以下格式：PNG、JPEG、GIF、WebP。
*   PDF，原生发送给提供商（Anthropic、OpenAI 和 Google 支持）。
*   SVG 图像（作为原始 HTML 发送）。
*   文本文件。

并非每个模型都能读取每种附件：DeepSeek 不读取 PDF，且仅在其视觉模型中读取图像；OpenAI Codex、GitHub Copilot 和 Google Antigravity 读取图像但不读取 PDF。对于此类模型：

*   附加按钮只提供该模型可读取的类型，粘贴或拖放的它无法读取的文件不会被附加。
*   切换到此类模型后，它无法读取的附件会标记一个 <span class="tn-icon bx bx-error"></span> 警告，并且在移除该附件或选择另一个模型之前无法发送消息。
*   在较早消息中发送的附件到达模型时仅为其名称，例如 `[attached file: report.pdf]`，因此它可以告诉你它看不到内容。

要上传附件：

*   按下文本框下方的专用 _附加_ 按钮（回形针图标）。
*   使用 Ctrl+V 直接从剪贴板粘贴图像。

上传一个或多个附件后，它们会直接显示在文本框上方：

*   图像有一个小缩略图，便于识别。
*   每个附件都可以通过按下其对应的 X 按钮来删除。

点击图像或 PDF，无论是文本框上方的其标签，还是它在已发送消息中出现的位置，都会在查看器中打开它：图像可以在那里缩放和平移，PDF 可以逐页阅读。查看器关闭按钮旁边的按钮会在新的浏览器标签页中打开原始文件。<kbd>Ctrl</kbd>\+ 点击则会在新的浏览器标签页中打开图像，并在新的 Trilium 标签页中作为附件打开 PDF。

当存在附件时，LLM 会被指示优先考虑该附件，即使它可以访问当前笔记。

> [!NOTE]
> 目前 Trilium 在将附件发送给 LLM 提供商之前不会对其进行预处理（例如通过 <a class="reference-link" href="Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取 (OCR)</a>）。

### 提及

提及是一种插入对当前笔记以外笔记的引用的方式，使用与 <a class="reference-link" href="Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a> 相同的机制。要引用另一个笔记，只需输入 @ 后跟要引用的笔记名称。

此功能在笔记工具启用时最有用，否则 LLM 将无法访问给定的笔记。

### 技能

Trilium 中的技能是专门的指令集，通过理解 Trilium 来帮助 AI 更高效地工作。

这些技能默认不加载，以避免增加 token 消耗，但如果启用了 _笔记工具_，AI 可以按需加载它们。

以下技能是内置的：

*   搜索语法：理解 <a class="reference-link" href="Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a> 的完整语法。
*   后端脚本：能够编写正确的 <a class="reference-link" href="Scripting/Backend%20scripts.md">后端脚本</a>。
*   前端脚本：能够编写正确的[前端脚本](Scripting/Frontend%20Basics.md)（基本脚本、小组件、<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>）。
*   仪表板：构建 <a class="reference-link" href="Collections/Dashboard.md">仪表板</a> 及其小组件，包括使用 <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a> 制作的交互式小组件。

当 _笔记工具_ 启用时，这些技能会自动提供给 AI，因此无需用户交互。

> [!NOTE]
> 目前不支持自定义技能，但已计划支持。

### MCP

Trilium 附带一个内置的 MCP 服务器，允许你使用外部智能体（如 Claude Code）访问你的数据库。有关更多详细信息，请参阅专门的 <a class="reference-link" href="AI/MCP.md">MCP</a> 页面。

## 历史

### 在 v0.102.0 中移除

从 v0.102.0 版本开始，AI/LLM 集成已从 Trilium Notes 核心中移除。

尽管在开发此功能上投入了大量精力，但长期维护和支持它被证明是不可持续的。

升级到 v0.102.0 时，你的对话笔记将被保留，但它们将不再是专用对话窗口，而是变为普通的 <a class="reference-link" href="Note%20Types/Code.md">代码</a> 笔记，显示对话的底层 JSON。

### 在 v0.103.0 中重新引入

鉴于 AI 领域最近的进展，我们决定再给 LLM 集成一次机会。v0.103.0 引入了一个全新的聊天系统。

导致重新实现的关键变化之一是，我们现在使用一个库（[Vercel AI](https://github.com/vercel/ai)）来管理内部机制以及 LLM 提供商之间的差异，而不是必须自己实现它。