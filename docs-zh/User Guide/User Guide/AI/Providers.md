# 提供商

提供商在 AI 设置的 _模型提供商_ 部分通过 _添加模型提供商_ 添加。每个提供商都会列出为其选择的模型，这些模型就是对话中提供的模型；未选择任何模型的提供商不会在对话中提供。

## 使用 API 密钥的云提供商

目前支持以下云提供商：

*   <span class="tn-icon tn-brand tn-brand-anthropic"></span> [Anthropic](https://platform.claude.com/settings/workspaces/default/keys)
*   <span class="tn-icon tn-brand tn-brand-openai"></span> OpenAI
*   <span class="tn-icon tn-brand tn-brand-gemini"></span> Gemini
*   <span class="tn-icon tn-brand tn-brand-deepseek"></span> DeepSeek
*   <span class="tn-icon tn-brand tn-brand-openrouter"></span> [OpenRouter](https://openrouter.ai/settings/keys)

对于所有提供商，都需要 API 密钥。请注意，此项费用与您可能已经拥有的订阅（例如 Claude Pro）分开计费。如果这可能是个问题，请考虑使用基于订阅的提供商（见下文）或通过 MCP 在外部使用。

请注意，大多数其他大语言模型提供商（例如 Groq、Mistral、Together）仍然可以通过 OpenAI 兼容的自定义端点（见下文）在 Trilium 中使用。

如果您使用代理或网关，还可以配置基础 URL，否则将使用默认值。

对于 OpenRouter，模型费用从您的 OpenRouter 额度中扣除，其价格、上下文窗口以及它们读取的附件均来自 OpenRouter 自己的模型列表：

*   默认选择可使用工具的 _Latest_ 模型，例如 _Anthropic: Claude Sonnet Latest_。OpenRouter 会将它们各自指向其系列中的最新模型，因此无需编辑提供商即可保持选择为最新。
*   具有推理能力的模型在对话中有一个推理强度下拉菜单（_Low_、_Medium_ 或 _High_）。
*   _Auto Router_（`openrouter/auto`）会为每条消息选择一个模型。在每条回复下方，对话会标明撰写该回复的模型，使用 _Latest_ 模型时也是如此。
*   回复下方显示的费用是 OpenRouter 为其计费的实际金额，而不是根据所列价格估算的金额。
*   图像生成模型和延迟的 _batch_ 变体不会列出。
*   对话标题使用 _Anthropic: Claude Haiku Latest_ 生成。
*   请求会在您的 OpenRouter 活动页面上归属于 Trilium。

对于 Gemini，未指定模型的对话使用 `gemini-3.8-flash`，自动生成的对话标题使用 `gemini-3.5-flash-lite`。您显式选择的模型将按原样使用，不受这些默认值影响。

> [!NOTE]
> 我们不计划支持所有云提供商，即使我们使用的库理论上支持它们。在提交 PR 添加对其他云提供商的支持之前，请务必先在 [GitHub Discussions](https://github.com/orgs/TriliumNext/discussions) 上讨论。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 基于订阅的提供商

Trilium 集成了多个 <a class="reference-link" href="Providers/Subscription-based%20providers.md">基于订阅的提供商</a>：

*   <span class="tn-icon tn-brand tn-brand-claude"></span> Claude Code，通过复用您的 CLI。
*   <span class="tn-icon tn-brand tn-brand-github-copilot"></span> GitHub Copilot，通过复用您 CLI 的 ACP。
*   <span class="tn-icon tn-brand tn-brand-antigravity"></span> Google Antigravity，通过为 Trilium 下载并设置 ACP。
*   <span class="tn-icon tn-brand tn-brand-codex"></span> OpenAI Codex，通过 Trilium 附带的 ACP 适配器复用您的 CLI。

## 本地/自托管提供商

本地或自托管提供商是一种免费的替代方案，尊重您的隐私，但需要特定的硬件。

Trilium 直接支持以下本地提供商：

=== "<span class="tn-icon tn-brand tn-brand-ollama"></span> Ollama"

    通常 Ollama 在后台运行，因此只要下载了模型（例如 `ollama pull llama3.2`），它就应该可以直接在 Trilium 中使用。

=== "<span class="tn-icon tn-brand tn-brand-lmstudio"></span> LM Studio"

    在 LM Studio 安装中，OpenAI 兼容服务器默认是**禁用**的。首先通过图形界面下载您想要的模型，然后转到 _Settings_ → _Developer_ 并切换 _Developer mode_。左侧将出现一个新的 _Developer_ 选项卡，其中有一个用于启动它的开关。

即使对于 Trilium 不直接支持的本地提供商，您仍然可以使用自定义端点（见下文）。

> [!WARNING]
> 在处理自托管的 LLM 模型时，根据训练情况和模型大小，输出质量可能会有所不同。在[报告问题](../Troubleshooting/Reporting%20issues.md)关于输出质量（例如幻觉工具调用）之前，请考虑将响应与云提供商（推荐 Claude Sonnet）进行基准测试。

## 自定义端点

如果您所需的托管（例如 Groq、Mistral、Together）或本地 LLM 提供商未在 Trilium 中列出，您可以使用 _自定义端点_ 部分中专门的 _OpenAI 兼容_ 提供商。

这允许您将基础 URL 设置为 OpenAI 兼容的 API，并在服务需要时提供可选的 API 密钥。

请完全按照服务文档中的说明输入基础 URL，包括其版本路径，例如 `https://api.groq.com/openai/v1` 或 `https://open.bigmodel.cn/api/paas/v4`。只有像 `http://localhost:8080` 这样的裸主机才会补全为 `/v1`。

该端点可以运行在与 Trilium 相同的机器上、本地网络的其他位置，或 Tailscale tailnet 上。Trilium 会拒绝链路本地地址（`169.254.0.0/16`）和云元数据端点，因为这些地址上不提供任何模型服务器。

对于自定义端点，模型的价格未知，因此不会显示对话的费用；这对于托管提供商尤其重要。