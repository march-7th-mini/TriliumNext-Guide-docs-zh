# 提供商
## 使用 API 密钥的云提供商

目前，支持以下云提供商：

*   [Anthropic](https://platform.claude.com/settings/workspaces/default/keys)
*   OpenAI
*   Gemini
*   DeepSeek

对于所有提供商，都需要一个 API 密钥。请注意，这是与您可能已经拥有的订阅（例如 Claude Pro）分开计费的。如果这可能是个问题，请考虑使用订阅制提供商（见下文）或通过 MCP 在外部使用。

请注意，大多数其他大语言模型提供商（例如 OpenRouter、Groq、Mistral）仍然可以通过 OpenAI 兼容的自定义端点（见下文）在 Trilium 中使用。

如果您使用的是代理或网关，您也可以配置基础 URL，否则将使用默认值。

> [!NOTE]
> 我们不打算支持所有云提供商，即使我们使用的库理论上可以支持它们。在提交 PR 添加对其他云提供商的支持之前，请务必先在 [GitHub Discussions](https://github.com/orgs/TriliumNext/discussions) 上讨论。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 基于订阅的提供商

> [!IMPORTANT]
> 基于订阅的提供商仍处于测试阶段。它们可以安全使用（不会使用额外资金，并遵守使用条款），但您可能会遇到一些小问题。请考虑 <a class="reference-link" href="../Troubleshooting/Reporting%20issues.md">报告问题</a>。

一些云提供商提供订阅服务，采用固定的月费而非按使用量付费（与 API 密钥不同）。Trilium v0.104.0 引入了对 Anthropic 的 Claude Pro/Max 订阅的测试版支持。其他基于订阅的提供商（如 ChatGPT）已在路线图中，但尚未实现。

要使用订阅：

1.  首先，需要在运行 Trilium 的机器上安装 Claude Code。因此，对于 <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，Claude 需要安装在本地；对于通过浏览器访问的 <a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，Claude 需要安装在服务器上。
2.  Claude Code 必须已经过身份验证。为此，请在终端中运行一次 `claude`，输入 `/login` 并按照说明操作。
3.  转到 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 Claude Code 提供商。

Trilium 将按以下顺序识别您的 Claude Code 二进制文件：

*   通过查找指向 Claude 二进制文件的 `TRILIUM_CLAUDE_CODE_PATH` 环境变量。这允许在需要时覆盖路径。
*   通过在您的 PATH 中查找 `claude`，通常在大多数情况下都有效。
*   通过向您的登录 shell 询问其 `PATH`，这使桌面安装能够找到通过 `nvm`、`fnm`、`asdf` 或 Homebrew 安装的 CLI，因为通过 GUI 启动的应用不会继承您终端的环境。

设置好提供商后，您将享受到与 API 密钥相同的功能（笔记工具、网络搜索、扩展思考、图像/PDF 附件、流式传输）。

> [!NOTE]
> Trilium 有意使用您的 Claude Code 二进制文件，以避免打包约 250 MB 的客户端，但这也有代价：如果本地安装的版本与 Trilium 期望的版本不匹配，则存在版本不兼容的小风险。通常最好将 Claude Code 和 Trilium 都保持更新到最新版本。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 本地/自托管提供商

本地或自托管提供商是一种免费的替代方案，尊重您的隐私，但需要特定的硬件。

Trilium 直接支持以下本地提供商：

*   Ollama
    *   通常 Ollama 在后台运行，因此只要下载了模型（例如 `ollama pull llama3.2`），它应该可以直接在 Trilium 中使用。
*   LM Studio
    *   在 LM Studio 安装中，OpenAI 兼容服务器默认是**禁用**的。首先通过图形界面下载您想要的模型，然后转到 _Settings_ → _Developer_ 并切换 _Developer mode_。左侧将出现一个新的 _Developer_ 选项卡，其中有一个用于启动它的开关。

即使对于 Trilium 不直接支持的本地提供商，您仍然可以使用自定义端点（见下文）。

> [!WARNING]
> 在处理自托管的大语言模型时，取决于训练和模型的大小，输出质量可能会有所不同。在[报告问题](../Troubleshooting/Reporting%20issues.md)关于输出质量（例如幻觉工具调用）之前，请考虑针对云提供商（推荐 Claude Sonnet）对响应进行基准测试。

## 自定义端点

如果您所需的托管（例如 OpenRouter、Groq、Mistral）或本地大语言模型提供商未在 Trilium 中列出，您可以使用 _Custom endpoint_ 部分中专用的 _OpenAI-compatible_ 提供商。

这允许您将基础 URL 设置为 OpenAI 兼容的 API，并在服务需要时提供可选的 API 密钥。

请严格按照服务文档输入基础 URL，包括其版本路径，例如 `https://api.groq.com/openai/v1` 或 `https://open.bigmodel.cn/api/paas/v4`。只有像 `http://localhost:8080` 这样的裸主机才会补全为 `/v1`。

对于自定义端点，模型的定价未知，因此不会显示对话的费用；这对于托管提供商尤其重要。