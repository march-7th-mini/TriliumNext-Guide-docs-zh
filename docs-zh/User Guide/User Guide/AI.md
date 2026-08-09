# AI

Trilium 可以连接到大语言模型，并将其用作直接处理笔记的助手：询问你正在阅读的笔记相关问题，让它起草或重构内容，或者让它为你编写脚本和小组件。

该集成默认关闭，在你启用并配置提供商之前不会执行任何操作；Trilium 本身不附带任何模型。你选择的提供商也决定了你的笔记数据去向：按使用量计费的云 API、你已经付费的订阅，或运行在你自己的硬件上的模型（这种情况下数据不会离开你的机器）。有关每种方案的具体内容，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>，有关具体发送内容的详细信息，请参阅 <a class="reference-link" href="AI/Privacy.md">隐私</a>。

启用后，助手既可作为右侧边栏中的面板使用，也可作为专用的笔记类型使用。它可以通过工具读取和修改笔记，如果你希望它只能看到你输入的内容，可以在每次对话中关闭这些工具。

## 功能亮点

*   基于聊天的界面，支持消息实时流式传输。
*   为 AI 提供当前正在查看的笔记作为上下文。
*   用于修改笔记内容、创建新笔记等的工具。
*   关于上下文窗口使用情况和每条消息定价的统计信息。
*   支持多模态聊天的附件（图像、文本文件、PDF）。
*   可选的 MCP，允许外部聊天工具（例如 Claude Code）操作 Trilium 中的笔记。

## 示例用例

*   创建任何类型的 <a class="reference-link" href="Scripting/Frontend%20Basics/Custom%20Widgets.md">自定义小组件</a>。
*   轻松创建 <a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>，例如 _为我创建一个可以玩井字棋的渲染笔记。确保使用 Preact 而不是旧的 jQuery。_
*   为 <a class="reference-link" href="Collections/Dashboard.md">仪表板</a> 创建小组件，例如计算器、秒表、番茄钟计时器。

> [!NOTE]
> 已知 Claude Sonnet 在很少指导下就能生成非常好的前端或后端脚本，因为 AI 已经接受了如何生成这些脚本的指导。

## 大语言模型提供商

Trilium 支持四种不同类型的提供商：

*   **云提供商**
    按使用量付费，使用 API 密钥，费用与你可能已有的任何订阅分开计费
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
    用于 Trilium 不直接支持的其他提供商，无论是本地的还是托管的（例如 OpenRouter、Groq、Mistral）。

有关每个提供商的更多信息，请参阅 <a class="reference-link" href="AI/Providers.md">提供商</a>。请参阅专门的 <a class="reference-link" href="AI/Privacy.md">隐私</a> 页面，以更好地了解哪些数据会发送给提供商。

## 启用 AI 集成

要启用 AI 集成，只需转到 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_，然后按下对话框右上角的切换开关并配置提供商。

## 创建新对话

有两种不同的对话界面：

*   侧边栏中的一个。
*   专用的笔记类型。

### 侧边栏界面

### 专用笔记类型

专用的对话笔记与侧边栏界面类似，但它使较长的对话更易于阅读。

与侧边栏不同，AI 不会感知到它所在的当前笔记。

### 模板

对话笔记可以设置为 <a class="reference-link" href="Advanced%20Usage/Templates.md">模板</a>，以便轻松复用。整个对话历史都会被保留，允许通过现有的对话充当系统提示词，对 LLM 进行一种基本形式的特化。

### 模型选择

在 <a class="reference-link" href="Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> 中配置提供商后，下一步是选择对话可用的模型。

模型仅在模型选择列表可见时从提供商处动态获取。要更改模型列表，只需按下模型选择框中的“编辑”按钮。

对于已知模型会显示定价信息。定价信息（每百万 token 的价格）内嵌在应用程序中（使用 LiteLLM 数据的子集），并会随着 Trilium 的新版本而更新。本地提供商被视为免费，而自定义端点提供商不提供任何定价信息。

## 功能

### 网络搜索

AI 可以选择性地搜索网络以查找有关特定主题的更多信息。

此功能默认开启，但可以通过点击对话底部的模型选择器并取消选中 _网络搜索_ 来轻松禁用。

> [!NOTE]
> 目前仅支持 LLM 提供商自带的搜索功能。尚不支持 Exa、Tavily 和 SearXNG 等外部搜索提供商。

### 笔记访问（工具）

工具允许智能 AI 直接在你的 Trilium 实例中理解和操作笔记。

此功能默认开启，但可以通过点击对话底部的模型选择器并取消选中 _笔记访问_ 来轻松禁用。

以下是 Trilium 为 LLM 提供的一些工具：

*   笔记级别：
    *   搜索笔记
    *   获取笔记的元数据或内容。
    *   编辑笔记
        *   LLM 有多种编辑笔记的机制：完全重写、查找/替换文本序列或追加。
        *   每当 AI 做出更改时，都会保存一个 [修订](Basic%20Concepts%20and%20Features/Notes/Note%20Revisions.md) 以便能够还原任何不需要的更改。
    *   创建新笔记
    *   重命名或删除笔记。
*   属性级别：
    *   获取完整的属性列表，或特定属性。
    *   设置属性的值。
    *   删除属性。
*   树级别：
    *   获取笔记的直接子笔记。
    *   获取笔记的整个子树。
    *   将笔记移动或克隆到其他位置。
*   对于 <a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a>：
    *   获取附件的元数据。
    *   获取附件的内容。
*   技能（参见专门章节）。

> [!WARNING]
> 目前笔记工具**没有实现权限管理**，这意味着 LLM 可能会删除现有笔记或用笔记塞满整个树。通常大多数操作都很容易逆转（删除笔记、恢复已删除的笔记、还原对笔记的修改），但有些操作较难逆转（例如设置属性，因为没有属性历史记录）。

> [!NOTE]
> Gemini 有一个特殊情况，即 _笔记访问_ 和 _网络搜索_ 不能同时启用。

### 附件

自 Trilium v0.140.0 起，<a class="reference-link" href="Basic%20Concepts%20and%20Features/Notes/Attachments.md">附件</a> 支持多模态对话：

*   光栅图像（作为视觉输入发送，SVG 除外），支持以下格式：PNG、JPEG、GIF、WebP。
*   PDF，以原生格式发送给提供商（受 Anthropic、OpenAI 和 Google 支持）。
*   SVG 图像（作为原始 HTML 发送）。
*   文本文件。

要上传附件：

*   按下文本框下方的专用 _附加_ 按钮（回形针图标）。
*   使用 <kbd>Ctrl</kbd>+<kbd>V</kbd> 直接从剪贴板粘贴图像。

上传一个或多个附件后，它们将出现在文本框正上方：

*   图像有一个小缩略图，便于识别。
*   每个附件都可以通过按下相应的 X 按钮来删除。

当存在附件时，LLM 会被指示优先考虑该附件，即使它可以访问当前笔记。

> [!NOTE]
> 目前 Trilium 在将附件发送给 LLM 提供商之前不会对其进行预处理（例如通过 <a class="reference-link" href="Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取 (OCR)</a>）。

### 提及

提及是一种插入对当前笔记之外的其他笔记的引用的方式，使用与 <a class="reference-link" href="Note%20Types/Text/Links/Internal%20(reference)%20links.md">内部（引用）链接</a> 相同的机制。要引用另一个笔记，只需输入 <kbd>@</kbd> 后跟要引用的笔记名称。

此功能在启用笔记工具时最为有用，否则 LLM 将无法访问给定的笔记。

### 技能

Trilium 中的技能是专门的指令集，通过帮助 AI 理解 Trilium 的工作方式来提高其生产力。

这些技能默认不加载，以避免增加 token 消耗，但如果启用了 _笔记工具_，AI 可以按需加载它们。

内置以下技能：

*   搜索语法：理解 <a class="reference-link" href="Basic%20Concepts%20and%20Features/Navigation/Search.md">搜索</a> 的完整语法。
*   后端脚本：能够编写正确的 <a class="reference-link" href="Scripting/Backend%20scripts.md">后端脚本</a>。
*   前端脚本：能够编写正确的 [前端脚本](Scripting/Frontend%20Basics.md)（基础脚本、小组件、<a class="reference-link" href="Note%20Types/Render%20Note.md">渲染笔记</a>）。

当启用 _笔记工具_ 时，技能将自动提供给 AI，因此无需用户交互。

> [!NOTE]
> 目前不支持自定义技能，但已在计划中。

### MCP

Trilium 附带一个内置的 MCP 服务器，允许你使用外部代理（如 Claude Code）访问你的数据库。有关更多详细信息，请参阅专门的 <a class="reference-link" href="AI/MCP.md">MCP</a> 页面。

## 历史

### 在 v0.102.0 中移除

从 v0.102.0 版本开始，AI/LLM 集成已从 Trilium Notes 核心中移除。

尽管在开发此功能上投入了大量精力，但长期维护和支持它被证明是不可持续的。

升级到 v0.102.0 时，你的对话笔记将被保留，但不再是专用的对话窗口，而是会转换为普通的 <a class="reference-link" href="Note%20Types/Code.md">代码</a> 笔记，显示对话底层的 JSON。

### 在 v0.103.0 中重新引入

鉴于 AI 领域的最新进展，我们决定再次尝试 LLM 集成。v0.103.0 引入了一个全新的对话系统。

导致重新实现的关键变化之一是，现在我们使用一个库（[Vercel AI](https://github.com/vercel/ai)）来管理内部机制以及不同 LLM 提供商之间的差异，而不是自己实现。