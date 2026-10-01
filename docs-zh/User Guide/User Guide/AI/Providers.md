# 提供商
## 使用 API 密钥的云提供商

目前，支持以下云提供商：

*   [Anthropic](https://platform.claude.com/settings/workspaces/default/keys)
*   OpenAI
*   Gemini
*   DeepSeek

对于所有提供商，都需要一个 API 密钥。请注意，此项费用与您可能已经拥有的订阅（例如 Claude Pro）是分开计费的。如果这可能是个问题，请考虑使用订阅制提供商（见下文），或者通过 MCP 在外部使用。

请注意，大多数其他 LLM 提供商（例如 OpenRouter、Groq、Mistral）仍然可以通过 OpenAI 兼容的自定义端点（见下文）在 Trilium 中使用。

如果您正在使用代理或网关，您也可以配置基础 URL，否则将使用默认值。

> [!NOTE]
> 我们不打算支持所有云提供商，即使我们使用的库理论上可以支持它们。在提交 PR 添加对其他云提供商的支持之前，请务必先在 [GitHub Discussions](https://github.com/orgs/TriliumNext/discussions) 上讨论。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 订阅制提供商

Trilium 集成了多个 <a class="reference-link" href="Providers/Subscription-based%20providers.md">订阅制提供商</a>：

*   Claude Code，通过复用您的 CLI。
*   GitHub Copilot，通过复用您 CLI 的 ACP。
*   Google Antigravity，通过为 Trilium 下载并设置 ACP。
*   OpenAI Codex，通过 Trilium 附带的 ACP 适配器复用您的 CLI。

## 本地/自托管提供商

本地或自托管提供商是一种免费的替代方案，尊重您的隐私，但需要特定的硬件。

Trilium 直接支持以下本地提供商：

*   Ollama
    *   通常 Ollama 在后台运行，因此只要下载了模型（例如 `ollama pull llama3.2`），它应该可以直接在 Trilium 中使用。
*   LM Studio
    *   在 LM Studio 安装中，OpenAI 兼容服务器默认是**禁用**的。首先通过图形界面下载您想要的模型，然后转到 _设置_ → _开发者_ 并切换 _开发者模式_。左侧将出现一个新的 _开发者_ 标签页，其中有一个用于启动它的开关。

即使对于 Trilium 不直接支持的本地提供商，您仍然可以使用自定义端点（见下文）。

> [!WARNING]
> 在处理自托管 LLM 模型时，根据训练情况和模型大小，输出质量可能会有所不同。在就输出质量（例如幻觉工具调用）[报告问题](../Troubleshooting/Reporting%20issues.md)之前，请考虑针对云提供商（推荐 Claude Sonnet）对响应进行基准测试。

## 自定义端点

如果您想要的托管（例如 OpenRouter、Groq、Mistral）或本地 LLM 提供商未在 Trilium 中列出，您可以使用 _自定义端点_ 部分中专用的 _OpenAI 兼容_ 提供商。

这允许您将基础 URL 设置为 OpenAI 兼容的 API，并在服务需要时提供可选的 API 密钥。

请严格按照服务文档中的说明输入基础 URL，包括其版本路径，例如 `https://api.groq.com/openai/v1` 或 `https://open.bigmodel.cn/api/paas/v4`。只有像 `http://localhost:8080` 这样的裸主机才会被补全为 `/v1`。

对于自定义端点，模型的定价是未知的，因此不会显示对话的成本；这对于托管提供商尤其重要。