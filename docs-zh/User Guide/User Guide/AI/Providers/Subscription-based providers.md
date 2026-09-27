# 基于订阅的提供商

一些云提供商提供订阅服务，采用固定的月费而非按使用量付费（与 API 密钥不同）。

简而言之，基于订阅的提供商通过复用你现有的 CLI 工具（例如通过 ACP 使用 Claude Code、GitHub Copilot 和 OpenAI Codex）来工作，而有些则需要手动安装 ACP 服务器（例如 Google Antigravity）。由于它们需要在你的设备上安装某些东西，这些提供商在移动端（Android 或 iOS）或独立模式下不可用。

另请参阅专门的 <a class="reference-link" href="../Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## Claude Code

要使用订阅：

1.  首先，Claude Code 需要安装在运行 Trilium 的机器上。因此对于 <a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，Claude 需要安装在本地；对于通过浏览器访问的 <a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，Claude 需要安装在服务器上。
2.  Claude Code 必须已经通过身份验证。为此，在终端中运行一次 `claude`，输入 `/login` 并按照说明操作。
3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 Claude Code 提供商。

Trilium 将按以下顺序识别你的 Claude Code 二进制文件：

*   通过查找指向 Claude 二进制文件的 `TRILIUM_CLAUDE_CODE_PATH` 环境变量。这允许在需要时覆盖路径。
*   通过在 PATH 中查找 `claude`，通常在大多数情况下都能正常工作。
*   通过向你的登录 shell 询问其 `PATH`，这使桌面安装能够找到通过 `nvm`、`fnm`、`asdf` 或 Homebrew 安装的 CLI，因为通过 GUI 启动的应用不会继承你终端的环境。

设置好提供商后，你将受益于与 API 密钥相同的功能（笔记工具、网络搜索、扩展思考、图像/PDF 附件、流式传输）。

> [!NOTE]
> Trilium 有意使用你的 Claude Code 二进制文件，以避免随附打包约 250 MB 的客户端，但这也有代价：如果本地安装的版本与 Trilium 期望的版本不匹配，存在版本不兼容的小风险。通常最好将 Claude Code 和 Trilium 都保持更新到最新版本。

## GitHub Copilot

> [!NOTE]
> 这个基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金且遵守使用条款），但你可能会遇到一些小问题。请考虑 <a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

GitHub Copilot 让你无需 API 密钥即可访问你的 GitHub Copilot 订阅（Pro、Pro+、Business 或 Enterprise）中的模型。使用量会计入你的 Copilot 计划。

1.  在运行 Trilium 的机器上安装 GitHub Copilot CLI，例如使用 `npm install -g @github/copilot`。与 Claude Code 一样，对于 <a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，它需要安装在服务器上。
2.  在终端中运行一次 `copilot login` 来登录。如果你已在同一台机器的其他编辑器中使用 GitHub Copilot，则会复用该登录。
3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 GitHub Copilot 提供商。

Trilium 将按以下顺序识别你的 Copilot CLI：

*   通过查找指向 Copilot 二进制文件的 `TRILIUM_COPILOT_PATH` 环境变量。
*   通过在 PATH 中查找 `copilot`。
*   通过向你的登录 shell 询问其 `PATH`，与 Claude Code 相同。

### 已知限制

*   代理只能通过 Trilium 的笔记工具处理你的笔记；出于安全原因，其自身的文件、shell 和网络工具被阻止。
*   图像可以附加到对话中，PDF 则不能。当笔记工具启用时，大语言模型仍应能够通过 <a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a> 读取 PDF 笔记和附件。

## Google Antigravity

> [!NOTE]
> 这个基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金且遵守使用条款），但你可能会遇到一些小问题。请考虑 <a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

Google Antigravity 让你无需 API 密钥即可使用 Google 账户（免费、Google AI Pro 或 Google AI Ultra）访问 Gemini 模型。在撰写本文时，免费的 Google 账户就足以使用它。

与 Claude Code 或 GitHub Copilot 不同，Google 的 Antigravity ACP 服务器不是 CLI 的一部分，因此需要专门为 Trilium 手动安装。下载的压缩包大约为 112-334 MB，解压后的大小根据平台约为 230 MB-2 GB。

在 Windows、macOS 和 Linux（不包括 NixOS）上：

1.  下载适用于你平台的 Google Antigravity ACP 服务器。在 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 中添加提供商时会显示该链接。在运行 Trilium 的设备上解压它。
2.  让 Trilium 能够找到它，可以：
    1.  将解压后的文件夹添加到你的 PATH，或
    2.  设置一个 `TRILIUM_ANTIGRAVITY_ACP_PATH` 环境变量，指向 `agy_acp_server.exe`（Windows）或 `agy_acp_server.par`（Linux 和 macOS）。
3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI / LLM 并添加 Google Antigravity 提供商。首次加载模型列表时，Google 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

> [!NOTE]
> Trilium 需要 `curl` 才能使用 Google Antigravity。它随 Windows 10 及更高版本、macOS 和大多数 Linux 发行版一起提供。

在 NixOS 上，`antigravity-acp` 包已经可用，但在撰写本文时仅在 `nixos-unstable` 中。测试它的最简单方法是使用带 flakes 的 `nix shell`：

```sh
NIXPKGS_ALLOW_UNFREE=1 nix shell --impure github:nixos/nixpkgs/nixos-unstable#antigravity-acp
trilium
```

### 已知限制

*   代理只能通过 Trilium 的笔记工具处理你的笔记；出于安全原因，其自身的文件和 shell 工具被阻止。
*   Antigravity ACP 服务器需要通过登录链接进行身份验证。登录链接需要在同一设备上运行，因此在使用 Docker 安装的 Web 版本时可能无法设置该提供商。<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 应该可以正常工作。
*   图像可以附加到对话中，PDF 则不能。当笔记工具启用时，大语言模型仍应能够通过 <a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a> 读取 PDF 笔记和附件。
*   工具调用的结果（例如读取笔记、写入属性）无法正确显示，因为 ACP 服务器未公开它们。

## OpenAI Codex

> [!NOTE]
> 这个基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金且遵守使用条款），但你可能会遇到一些小问题。请考虑 <a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

OpenAI Codex 让你无需 API 密钥即可访问你的 ChatGPT 计划（Free、Go、Plus、Pro 或 Business）中的 Codex 模型。在撰写本文时，免费的 ChatGPT 账户就足以使用它。使用量会计入你计划的 Codex 限制，Free 计划中的限制很小。

1.  在运行 Trilium 的机器上安装 Codex CLI，例如使用 `npm install -g @openai/codex`。与 Claude Code 一样，对于 <a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，它需要安装在服务器上。Trilium 随附了连接到它的 ACP 适配器，因此不需要其他东西。
2.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 OpenAI Codex 提供商。首次加载模型列表时，ChatGPT 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

Trilium 保留自己的 Codex 登录和设置，与你终端中使用的任何 Codex CLI 分开，因此不会复用现有的 `codex login`。

Trilium 将按以下顺序识别你的 Codex CLI：

*   通过查找指向 Codex 二进制文件的 `TRILIUM_CODEX_PATH` 环境变量。
*   通过在 PATH 中查找 `codex`。
*   通过向你的登录 shell 询问其 `PATH`，与 Claude Code 相同。

在 NixOS 上，Codex 作为 nixpkgs 中的 `codex` 包提供。稳定频道可能落后于 Codex 的发布，因此可以从 `nixos-unstable` 获取更新的版本：

```sh
nix shell github:nixos/nixpkgs/nixos-unstable#codex
trilium
```

> [!NOTE]
> Trilium 需要 `curl` 才能使用 OpenAI Codex，与 Google Antigravity 相同：Trilium 通过它检查 Codex 进行的每次工具调用。它随 Windows 10 及更高版本、macOS 和大多数 Linux 发行版一起提供。

### 已知限制

*   代理只能通过 Trilium 的笔记工具处理你的笔记，并在聊天允许时搜索网络；出于安全原因，其自身的文件、shell 和其他工具被阻止。
*   ChatGPT 登录会在运行 Trilium 的设备上的浏览器中打开，因此在使用 Docker 安装的 Web 版本时可能无法设置该提供商。<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a> 应该可以正常工作。
*   图像和 SVG 可以附加到对话中，PDF 则不能。当笔记工具启用时，大语言模型仍应能够通过 <a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a> 读取 PDF 笔记和附件。