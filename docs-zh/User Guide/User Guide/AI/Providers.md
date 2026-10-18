# 提供商

提供商在 AI 设置的*模型提供商*部分通过*添加模型提供商*来添加。每个提供商都会列出为其选择的模型，这些模型就是对话中提供的模型；未选择任何模型的提供商不会在对话中提供。

## 使用 API 密钥的云提供商

目前支持以下云提供商：

*   <span class="tn-icon tn-brand tn-brand-anthropic"></span> [Anthropic](https://platform.claude.com/settings/workspaces/default/keys)
*   <span class="tn-icon tn-brand tn-brand-openai"></span> OpenAI
*   <span class="tn-icon tn-brand tn-brand-gemini"></span> Gemini
*   <span class="tn-icon tn-brand tn-brand-deepseek"></span> DeepSeek

对于所有提供商，都需要一个 API 密钥。请注意，此项费用与您可能已经拥有的订阅（例如 Claude Pro）是分开计费的。如果这可能是个问题，请考虑使用订阅制提供商（见下文）或通过 MCP 在外部使用。

请注意，大多数其他大语言模型提供商（例如 OpenRouter、Groq、Mistral）仍然可以通过 OpenAI 兼容的自定义端点（见下文）在 Trilium 中使用。

如果您使用的是代理或网关，您也可以配置基础 URL，否则将使用默认值。

> [!NOTE]
> 我们不计划支持所有云提供商，即使我们使用的库理论上支持它们。在提交 PR 添加对其他云提供商的支持之前，请务必先在 [GitHub Discussions](https://github.com/orgs/TriliumNext/discussions) 上讨论。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 订阅制提供商

Trilium 集成了多个 <a class="reference-link" href="Providers/Subscription-based%20providers.md">订阅制提供商</a>：

*   <span class="tn-icon tn-brand tn-brand-claude"></span> Claude Code，通过复用您的 CLI。
*   <span class="tn-icon tn-brand tn-brand-github-copilot"></span> GitHub Copilot，通过复用您 CLI 的 ACP。
*   <span class="tn-icon tn-brand tn-brand-antigravity"></span> Google Antigravity，通过为 Trilium 下载并设置 ACP。
*   <span class="tn-icon tn-brand tn-brand-codex"></span> OpenAI Codex，通过 Trilium 附带的 ACP 适配器复用您的 CLI。

## 本地/自托管提供商

本地或自托管提供商是一种免费的替代方案，尊重您的隐私，但需要特定的硬件。

Trilium 直接支持以下本地提供商：

=== "<span class="tn-icon tn-brand tn-brand-ollama"></span> Ollama"

    通常 Ollama 在后台运行，因此只要模型已下载（例如 `ollama pull llama3.2`），它应该可以直接在 Trilium 中使用。

=== "<span class="tn-icon tn-brand tn-brand-lmstudio"></span> LM Studio"

    在 LM Studio 安装中，OpenAI 兼容服务器默认是**禁用**的。首先通过图形界面下载您想要的模型，然后转到*设置* → *开发者* 并切换*开发者模式*。左侧将出现一个新的*开发者*选项卡，其中有一个用于启动它的开关。

即使对于 Trilium 不直接支持的本地提供商，您仍然可以使用自定义端点（见下文）。

> [!WARNING]
> 在处理自托管的大语言模型时，根据训练情况和模型大小，输出质量可能会有所不同。在[报告问题](../Troubleshooting/Reporting%20issues.md)（例如幻觉工具调用）之前，请考虑将响应与云提供商（推荐 Claude Sonnet）进行基准比较。

## 自定义端点

如果您想要的托管（例如 OpenRouter、Groq、Mistral）或本地大语言模型提供商未在 Trilium 中列出，您可以使用*自定义端点*部分中专门的*OpenAI 兼容*提供商。

这允许您将基础 URL 设置为 OpenAI 兼容的 API，如果服务需要，还可以选择提供 API 密钥。

请完全按照服务文档中的说明输入基础 URL，包括其版本路径，例如 `https://api.groq.com/openai/v1` 或 `https://open.bigmodel.cn/api/paas/v4`。仅输入裸主机（例如 `http://localhost:8080`）时会自动补全为 `/v1`。

对于自定义端点，模型的定价未知，因此不会显示对话的费用；这对于托管提供商尤其相关。