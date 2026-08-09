# 提供商
## 使用 API 密钥的云提供商

目前支持以下云提供商：

*   [Anthropic](https://platform.claude.com/settings/workspaces/default/keys)
*   OpenAI
*   Gemini
*   DeepSeek

所有提供商都需要 API 密钥。请注意，此费用与您可能已有的订阅（例如 Claude Pro）是分开计费的。如果这可能是个问题，请考虑使用订阅提供商（见下文）或通过 MCP 在外部使用。

请注意，大多数其他大语言模型提供商（例如 OpenRouter、Groq、Mistral）仍然可以通过兼容 OpenAI 的自定义端点（见下文）在 Trilium 中使用。

如果您使用代理或网关，您也可以配置基础 URL，否则将使用默认值。

> [!NOTE]
> 我们不打算支持所有云提供商，即使我们使用的库理论上支持它们。在提交添加新云提供商支持的 PR 之前，请务必在 [GitHub Discussions](https://github.com/orgs/TriliumNext/discussions) 上进行讨论。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据被发送到云提供商。

## 基于订阅的提供商

> [!IMPORTANT]
> 基于订阅的提供商仍处于测试阶段。它们可以安全使用（不会产生额外费用，并遵守使用条款），但您可能会遇到一些小问题。请考虑 <a class="reference-link" href="../Troubleshooting/Reporting%20issues.md">报告问题</a>。

一些云提供商提供订阅服务，即固定月费而非按使用量付费（与 API 密钥不同）。Trilium v0.104.0 引入了对 Anthropic 的 Claude Pro/Max 订阅的测试版支持。其他基于订阅的提供商（如 ChatGPT）已在路线图中，但尚未实现。

要使用订阅：

1.  首先，需要在运行 Trilium 的机器上安装 Claude Code。因此，对于 <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，Claude 需要安装在本地；对于通过浏览器访问的 <a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，Claude 需要安装在服务器上。
2.  Claude Code 必须已经完成身份验证。为此，请在终端中运行一次 `claude`，输入 `/login` 并按照说明操作。
3.  前往 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 Claude Code 提供商。

Trilium 将按以下顺序识别您的 Claude Code 二进制文件：

*   查找指向 Claude 二进制文件的 `TRILIUM_CLAUDE_CODE_PATH` 环境变量。这允许在需要时覆盖路径。
*   在 PATH 中查找 `claude`，在大多数情况下通常有效。

提供商设置完成后，您将享有与 API 密钥相同的功能（笔记工具、网络搜索、扩展思考、图像/PDF 附件、流式传输）。

> [!NOTE]
> Trilium 有意使用您的 Claude Code 二进制文件，以避免捆绑约 250 MB 的客户端，但这也有代价：如果本地安装的版本与 Trilium 期望的版本不匹配，则存在版本不兼容的小风险。通常最好将 Claude Code 和 Trilium 都更新到最新版本。

> [!IMPORTANT]
> 另请参阅专门的 <a class="reference-link" href="Privacy.md">隐私</a> 部分，以更好地了解哪些数据被发送到云提供商。

## 本地/自托管提供商

本地或自托管提供商是一种免费的替代方案，它尊重您的隐私，但需要特定的硬件。

Trilium 直接支持以下本地提供商：

*   Ollama
    *   通常 Ollama 在后台运行，因此只要模型已下载（例如 `ollama pull llama3.2`），它就应该可以在 Trilium 中直接使用。
*   LM Studio
    *   兼容 OpenAI 的服务器在 LM Studio 安装中默认**禁用**。首先通过图形界面下载您想要的模型，然后转到 _设置_ → _开发者_ 并切换 _开发者模式_。左侧将出现一个新的 _开发者_ 选项卡，其中有一个启动它的开关。

即使对于 Trilium 不直接支持的本地提供商，您仍然可以使用自定义端点（见下文）。

> [!WARNING]
> 在使用自托管大语言模型时，根据模型的训练和大小，输出质量可能会有所不同。在[报告问题](../Troubleshooting/Reporting%20issues.md)关于输出质量（例如工具调用幻觉）之前，请考虑将响应与云提供商（推荐 Claude Sonnet）进行基准测试。

## 自定义端点

如果您想要使用的托管（例如 OpenRouter、Groq、Mistral）或本地大语言模型提供商未列在 Trilium 中，您可以使用 _自定义端点_ 部分中的专用 _OpenAI 兼容_ 提供商。

这允许您将基础 URL 设置为兼容 OpenAI 的 API，如果服务需要，还可以设置可选的 API 密钥。

对于自定义端点，模型的价格未知，因此不会显示对话成本；这对于托管提供商尤其重要。