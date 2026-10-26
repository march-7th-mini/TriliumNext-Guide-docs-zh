# AI

Trilium 可以连接到大语言模型，并将其作为助手直接在笔记上工作：针对你正在阅读的笔记提问，让它起草或重构内容，或者让它为你编写脚本和小组件。

该集成默认关闭，在你启用并配置提供商之前不会执行任何操作；Trilium 本身不附带任何模型。你选择的提供商决定了你的笔记如何传输：按使用量计费的云 API、你已付费的订阅，或运行在你自己硬件上的模型（在这种情况下，任何数据都不会离开本机）。关于每种方式的具体内容，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>；关于具体会发送哪些数据，请参阅 <a class="reference-link" href="AI/Privacy.md">隐私</a>。

启用后，助手可通过以下方式使用：

*   作为一种专用笔记类型，它可以通过工具读取和修改笔记；如果你希望它只看到你输入的内容，可以按对话关闭这些工具。
*   右侧边栏中的一个面板，其行为与专用笔记类型类似，但它还可以选择性地访问当前笔记。
*   一个<a class="reference-link" href="Note%20Types/Text/In-editor%20AI%20assistant.md">编辑器内 AI 助手</a>，它内置了针对选中文本执行的操作（如校对、摘要），以及<a class="reference-link" href="Note%20Types/Text/In-editor%20AI%20assistant/Custom%20AI%20quick%20actions.md">自定义 AI 快捷操作</a>。

## 功能亮点

*   基于聊天的界面，消息实时流式显示。
*   为 AI 提供当前正在查看的笔记作为上下文。
*   用于修改笔记内容、创建新笔记等的工具。
*   关于上下文窗口使用情况和每条消息定价的统计信息。
*   用于多模态对话的附件（图片、文本文件、PDF）。
*   可选的 MCP，允许外部聊天工具（例如 Claude Code）操作 Trilium 中的笔记。

## 示例用例

*   创建任意类型的<a class="reference-link" href="Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a>。
*   轻松创建一个<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>，例如 _为我创建一个渲染笔记，让我可以玩井字棋。确保使用 Preact 而不是旧版 jQuery。_
*   为<a class="reference-link" href="Collections/Dashboard.md">仪表板</a>创建小组件，例如计算器、秒表、番茄钟。

> [!NOTE]
> 众所周知，Claude Sonnet 在几乎没有指导的情况下就能生成非常出色的前端或后端脚本，因为该 AI 已被指示如何生成它们。

## 大语言模型提供商

Trilium 支持四种不同类型的提供商：

=== "<span class="tn-icon bx bx-cloud"></span> 云端"

    使用 API 密钥按使用量付费，费用与你可能已有的任何订阅分开计费。

    *   <span class="tn-icon tn-brand tn-brand-anthropic"></span> Anthropic Claude
    *   <span class="tn-icon tn-brand tn-brand-openai"></span> OpenAI GPT
    *   <span class="tn-icon tn-brand tn-brand-gemini"></span> Google Gemini
    *   <span class="tn-icon tn-brand tn-brand-deepseek"></span> DeepSeek
    *   <span class="tn-icon tn-brand tn-brand-openrouter"></span> OpenRouter，用一个密钥即可访问大多数实验室的模型

=== "<span class="tn-icon bx bx-coin"></span> 基于订阅"

    复用现有订阅，而不是按使用量付费。

    *   <span class="tn-icon tn-brand tn-brand-claude"></span> [Claude Code](AI/Providers/Subscription-based%20providers.md)
    *   <span class="tn-icon tn-brand tn-brand-github-copilot"></span> [GitHub Copilot](AI/Providers/Subscription-based%20providers.md)
    *   <span class="tn-icon tn-brand tn-brand-antigravity"></span> [Google Antigravity](AI/Providers/Subscription-based%20providers.md)
    *   <span class="tn-icon tn-brand tn-brand-codex"></span> [OpenAI Codex](AI/Providers/Subscription-based%20providers.md)

=== "<span class="tn-icon bx bx-network-chart"></span> 本地/自托管"

    *   <span class="tn-icon tn-brand tn-brand-ollama"></span> Ollama
    *   <span class="tn-icon tn-brand tn-brand-lmstudio"></span> LM Studio

=== "<span class="tn-icon bx bx-code-curly"></span> 自定义端点"

    用于 Trilium 未直接支持的其他提供商，无论是本地还是托管（例如 Groq、Mistral、Together）。

> [!TIP]
> 关于每个提供商的更多信息，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>。请参阅专门的<a class="reference-link" href="AI/Privacy.md">隐私</a>页面，以更好地了解哪些数据会发送给提供商。

## 启用 AI 集成

要启用 AI 集成，只需转到<a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_，然后按下对话框右上角的开关并配置提供商。

## 创建新对话

有两种不同的聊天界面：

*   侧边栏中的一个。
*   一种专用笔记类型。

### 侧边栏界面

### 专用笔记类型

专用对话笔记与侧边栏界面类似，但它使较长的对话更易于阅读。

与侧边栏不同，AI 不会感知到它所在的当前笔记。

### 模板

对话笔记可以设置为<a class="reference-link" href="Advanced%20Usage/Templates.md">模板</a>，以便轻松复用。整个对话历史都会被保留，从而允许对 LLM 进行一种基本形式的专门化，现有对话就像系统提示一样起作用。

### 模型选择

在<a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a>中配置提供商后，下一步是选择可用于对话的模型。

模型仅在模型选择列表可见时从提供商动态获取。要更改模型列表，只需按模型选择框中的编辑按钮。

已知模型会显示定价信息。定价信息（每百万 token 的价格）内嵌在应用程序中（使用 LiteLLM 数据的子集），并随 Trilium 的新版本更新。本地提供商被视为免费，而自定义端点提供商不提供任何定价信息。

## 功能

### 网络搜索

AI 可以选择性地搜索网络，以查找有关特定主题的更多信息。

搜索来源在聊天底部模型选择器旁边的 <span class="tn-icon bx bx-shield-quarter"></span>_工具_ 菜单的 _网络搜索_ 子菜单中选择，其所在行会显示正在使用的来源：

*   _禁用_ 会为此对话关闭网络搜索。
*   _使用模型的内置搜索_（默认）让模型使用其提供商自有的搜索进行搜索。Anthropic、OpenAI、Google Gemini 和 DeepSeek 的模型都有内置搜索，Claude Code、Google Antigravity 和 OpenAI Codex 也是如此。OpenRouter、Ollama、LM Studio 和自定义端点没有，因此对于它们的模型此选项被禁用。DeepSeek 的搜索按搜索次数在你的 DeepSeek 账户上计费，并且仅适用于 DeepSeek 自己的端点，不适用于自定义基础 URL。
*   搜索提供商（Brave Search、Tavily、Exa、Serper、Perplexity 或 SearXNG）则通过该服务进行搜索，无论哪个模型在回答。搜索提供商在 AI 设置的 _搜索提供商_ 部分添加，可通过子菜单底部的 _管理搜索提供商_ 打开。浏览器版本无法使用 Brave Search、Exa 或 Perplexity，因为它们的服务拒绝来自网页的请求，因此在那里显示为禁用。

要使用 SearXNG，请通过将 `json` 添加到实例 `settings.yml` 中的搜索格式来启用其 JSON 输出。SearXNG 默认关闭 JSON，没有它每次搜索都会失败。

```yaml
search:
  formats:
    - html
    - json
```

SearXNG 不使用 API 密钥，因此请将 API 密钥留空。仅当你的实例位于需要令牌的代理后面时才填写；Trilium 会将其作为 bearer token 在 `Authorization` 头中发送。

网络搜索是否开启按对话保存；搜索来源由所有对话共享。当前模型无法使用的选择会保留在菜单中，但处于禁用状态；将鼠标悬停在其旁边的 <span class="tn-icon bx bx-info-circle"></span>图标上可查看原因。Claude Code、GitHub Copilot、Google Antigravity 和 OpenAI Codex 运行自己的工具，因此它们无法使用搜索提供商。

在对话中，通过搜索提供商进行的搜索会在其行首显示该提供商的徽标，而不是 <span class="tn-icon bx bx-search"></span>放大镜；将鼠标悬停在徽标上可查看提供商名称。

使用搜索提供商时，模型还可以将其找到的页面或你给它的链接作为文本读取：Trilium 自行获取页面，并将最多前 20,000 个字符交给模型。你自己机器或网络上的地址会被拒绝。在浏览器版本中，大多数网站不允许以这种方式被读取，因此在那里读取页面通常会失败。

### 思考

某些模型在回答之前会进行推理。当模型思考时，其推理过程会在加载指示器下完整显示；完成后，它会折叠成回复上方一行可折叠的 _思考过程_。

模型的思考量按对话设置，根据模型不同有两种方式：

*   大多数模型有一个 <span class="tn-icon bx bx-brain"></span>_扩展思考_ 按钮，位于 <span class="tn-icon bx bx-shield-quarter"></span>_工具_ 按钮旁边。
*   提供多个推理级别的模型（DeepSeek V4、会推理的 OpenRouter 模型、OpenAI Codex、Antigravity）则在模型选择器旁边有一个 <span class="tn-icon bx bx-brain"></span>推理强度下拉菜单。_无_（在提供的情况下）会关闭思考；更高的级别对难题给出更好的答案，但耗时更长、成本更高。

> [!NOTE]
> 只有在 Trilium 知道模型的级别后，强度下拉菜单才会出现。对于使用早期版本 Trilium 设置的 DeepSeek 提供商，请在模型选择框中编辑该提供商并按一次 _保存_。

### 笔记访问（工具）

工具允许智能体 AI 直接在你的 Trilium 实例中理解和操作笔记。

此功能默认开启。要关闭它，请按聊天底部模型选择器旁边的 <span class="tn-icon bx bx-shield-quarter"></span>_工具_ 按钮，并关闭 _笔记访问_。当笔记访问或网络搜索开启时，_工具_ 按钮会高亮显示。

以下是 Trilium 为 LLM 提供的一些工具：

*   在笔记级别：
    *   搜索笔记
    *   获取笔记的元数据或内容。
    *   编辑笔记
        *   LLM 有多种编辑笔记的机制：完全重写、查找/替换文本序列或追加。
        *   重写笔记时，LLM 还可以更改其类型（例如从文本笔记更改为代码笔记）或代码笔记的语言，并重写内容以匹配。
        *   每当 AI 进行更改时，都会保存一个[修订](Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md)，以便能够还原任何不需要的更改。
    *   创建新笔记
        *   当被要求绘图时，LLM 可以创建 SVG 图像笔记，或将现有笔记转换为 SVG 图像笔记。它只能编写 SVG 图像，不能编写 PNG 等其他格式。
    *   重命名或删除笔记。
*   在属性级别：
    *   获取完整的属性列表，或特定属性。
    *   设置属性的值，或在现有值旁边添加另一个值（例如第二个 `#tag`）。当设置值替换现有值时，AI 会被告知它替换了哪个值。
        *   运行代码的属性（如 `#run`、`#widget` 或 `~renderNote`）会以 `disabled:` 前缀保存（例如 `#disabled:widget`），与安全导入禁用它时的方式相同（请参阅<a class="reference-link" href="Basic%20Concepts%20and%20Features/Active%20content.md">活动内容</a>）。如果笔记已经启用了该属性，而 AI 是设置而不是添加值，则 AI 会移除已启用的那个，因此在启用新值之前不会运行任何内容。AI 会告诉你它在哪个笔记上；审查代码，然后使用笔记标题旁活动内容徽标旁边的开关启用它，或者对于<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>，使用笔记中的 _启用渲染笔记_ 按钮。
    *   删除属性。
*   在树级别：
    *   获取笔记的直接子项。
    *   获取笔记的整个子树。
    *   将笔记移动或克隆到其他地方。
*   对于<a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>：
    *   获取附件的元数据。
    *   获取附件的内容。
*   技能（请参阅专门章节）。

AI 使用的每个工具都会在对话中显示为一行，标明工具名称及其操作的笔记或查询；重命名的笔记会显示其之前的标题并带删除线，删除的笔记其标题带删除线，移动的笔记显示从哪里移动到哪里，AI 读取、设置、添加或删除的属性显示为胶囊（删除后带删除线），附件显示其标题、笔记和大小，AI 读取的网页显示为链接。只有当有内容可内联阅读时，该行才会展开：搜索找到的笔记、网络搜索找到的页面、图标搜索找到的图标、AI 读取的笔记的类型、属性或内容开头、笔记的所有属性、附件或网页的文本、AI 查阅的用户指南页面或其目录（两者都在帮助面板中打开）、笔记的子项或整个子树、AI 写入其创建、重写或添加的笔记的内容、编辑的更改，或工具失败的原因。搜索会在其行上标明它所限定的树的部分（如果有），还会显示它找到了多少笔记以及 AI 请求的匹配项中有多少；它列出的每个笔记点击即可打开。要确切查看 AI 发送给工具的内容以及它收到的返回内容，请将鼠标悬停在该行上并按旁边的 <span class="tn-icon bx bx-code-alt"></span>按钮；在触摸屏上该按钮始终显示。

当 AI 仍在工作时回复停止移动几秒钟（例如在它读取工具返回的内容时），其下方会出现一行 _仍在工作…_，直到回复的下一部分到达。

#### 批准工具调用

在 AI 运行工具之前，对话会询问是否允许。该工具的行会标记一个 <span class="tn-icon bx bxs-hand"></span>图标，其下方有 _允许_ 和 _拒绝_ 按钮。当调用会写入笔记时，该行会展开显示它将写入的文本或编辑的更改。回复会等待你的回答。

*   要让调用运行，请按 _允许_。
*   要在本次对话的剩余时间内不再询问某个工具，请打开 _允许_ 旁边的菜单，选择为此对话始终允许该工具。该调用会运行，该工具仍在等待的其他调用以及此对话中之后的每个调用也会运行。其他工具会继续询问，新对话会再次询问。
*   要拒绝它，请按 _拒绝_。AI 会被告知你拒绝了，其回复会在没有该调用的情况下继续，该调用标记为 _已拒绝_。
*   停止回复会拒绝所有仍在等待的调用。

要让对话再次询问某个工具，请打开聊天底部的 <span class="tn-icon bx bx-shield-quarter"></span>_工具_ 菜单，并在 _此对话中已允许_ 下按该工具。一旦对话允许了某个工具，该子菜单就会显示。

哪些调用会询问取决于对话的权限模式，在 <span class="tn-icon bx bx-shield-quarter"></span>_工具_ 菜单的 _权限_ 下选择：

*   _始终询问_：每个调用都会询问，包括只读的调用（搜索笔记，或读取笔记或附件）。
*   _更改前询问_：只读的调用自行运行，而更改你笔记的调用（创建、编辑、重命名、移动或删除笔记，以及设置、添加或删除属性）会询问。
*   _不询问_：每个调用都无需询问即可运行，包括更改。

新对话会以你上次在任何对话中选择的模式开始，或者在你选择之前以 _更改前询问_ 开始。因此，选择 _不询问_ 也会延续到下一个对话。

为此对话允许的工具在任何模式下都无需询问即可运行。在 Trilium 自带的内容（其用户指南、教 AI Trilium 搜索语法和笔记类型的技能表，以及图标）中查找内容也是如此，因为它不读取你的任何笔记。搜索网络和读取网页也从不询问：在 _工具_ 菜单中开启网络搜索就是允许它们的方式，无论模型是自己搜索还是通过搜索提供商搜索。

> [!NOTE]
> <a class="reference-link" href="AI/Providers/Subscription-based%20providers.md">基于订阅的提供商</a>（Claude Code、GitHub Copilot、Google Antigravity 和 OpenAI Codex）会像其他任何提供商一样询问。

> [!NOTE]
> 你允许的大多数更改都可以撤销：删除的笔记可以恢复，编辑可以从其修订还原。设置属性更难撤销，因为属性没有历史记录。

> [!NOTE]
> 在笔记访问开启时，Gemini 无法使用其内置搜索。在开启期间，_工具_ 菜单中的内置搜索选项被禁用并说明原因；搜索提供商在笔记访问开启时可以工作。

### 附件

自 Trilium v0.140.0 起，<a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>支持多模态对话：

*   光栅图像（作为视觉输入发送，SVG 除外），支持以下格式：PNG、JPEG、GIF、WebP。
*   PDF，原生发送给提供商（Anthropic、OpenAI 和 Google 支持）。
*   SVG 图像（作为原始 HTML 发送）。
*   文本文件。

并非每个模型都能读取每种附件：DeepSeek 不读取 PDF，且仅在其视觉模型中读取图像；OpenAI Codex、GitHub Copilot 和 Google Antigravity 读取图像但不读取 PDF。对于此类模型：

*   附加按钮只提供该模型可读取的类型，粘贴或拖放的它无法读取的文件不会被附加。
*   切换到此类模型后，它无法读取的附件会标记一个 <span class="tn-icon bx bx-error"></span>警告，在移除附件或选择其他模型之前无法发送消息。
*   在较早消息中发送的附件会仅以其名称到达模型，例如 `[attached file: report.pdf]`，因此它可以告诉你它看不到内容。

要上传附件：

*   按文本框下方的专用 _附加_ 按钮（回形针图标）。
*   使用 Ctrl+V 直接从剪贴板粘贴图像。

上传一个或多个附件后，它们会直接显示在文本框上方：

*   图像有一个小缩略图，便于识别。
*   每个附件都可以通过按相应的 X 按钮删除。

点击图像或 PDF（无论是文本框上方的标签，还是已发送消息中出现的位置），都会在查看器中打开它：图像可以在其中缩放和平移，PDF 可以逐页阅读。查看器关闭按钮旁边的按钮会在新的浏览器标签页中打开原始文件。<kbd>Ctrl</kbd> 加点击则会在新的浏览器标签页中打开图像，并将 PDF 作为附件在新的 Trilium 标签页中打开。

当存在附件时，LLM 会被指示优先考虑附件，即使它可以访问当前笔记。

> [!NOTE]
> 目前 Trilium 在将附件发送给 LLM 提供商之前不会对其进行预处理（例如通过<a class="reference-link" href="Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>）。

### 提及

提及是一种插入对当前笔记以外笔记的引用的方式，使用与<a class="reference-link" href="Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a>相同的机制。要引用另一个笔记，只需输入 @ 后跟要引用的笔记名称。

此功能在启用笔记工具时最有帮助，否则 LLM 将无法访问给定的笔记。

### 技能

Trilium 中的技能是专门的指令集，通过理解 Trilium 来帮助 AI 更高效地工作。

这些技能默认不加载，以避免增加 token 消耗，但如果启用了 _笔记工具_，AI 可以按需加载它们。

以下技能是内置的：

*   搜索语法：理解<a class="reference-link" href="Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a>的完整语法。
*   后端脚本：能够编写正确的<a class="reference-link" href="Scripting/Backend%20scripts.md">后端脚本</a>。
*   前端脚本：能够编写正确的[前端脚本](Scripting/Frontend%20Basics.md)（基本脚本、小组件、<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>）。
*   仪表板：构建<a class="reference-link" href="Collections/Dashboard.md">仪表板</a>及其小组件，包括使用<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>制作的交互式小组件。

当启用 _笔记工具_ 时，技能会自动提供给 AI，因此无需用户交互。

> [!NOTE]
> 目前不支持自定义技能，但已计划支持。

### MCP

Trilium 附带一个内置的 MCP 服务器，允许你使用外部代理（如 Claude Code）访问你的数据库。更多详情请参阅专门的 <a class="reference-link" href="AI/MCP.md">MCP</a> 页面。

## 历史

### 在 v0.102.0 中移除

从 v0.102.0 版本开始，AI/LLM 集成已从 Trilium Notes 核心中移除。

虽然开发此功能投入了大量精力，但长期维护和支持它被证明是不可持续的。

升级到 v0.102.0 时，你的对话笔记会被保留，但它们不会显示专用的对话窗口，而是会变成普通的<a class="reference-link" href="Note%20Types/Code.md">代码</a>笔记，显示对话底层的 JSON。

### 在 v0.103.0 中重新引入

鉴于 AI 领域的最新进展，我们决定再次尝试 LLM 集成。v0.103.0 引入了全新的对话系统。

导致重新实现的关键变化之一是，现在我们使用一个库（[Vercel AI](https://github.com/vercel/ai)）来管理内部机制和 LLM 提供商之间的差异，而不是必须自己实现。