# 基于订阅的提供商

一些云提供商提供订阅服务，采用固定的月费而非按使用量付费（与 API 密钥不同）。

简而言之，基于订阅的提供商通过复用你现有的 CLI 工具（例如通过 ACP 使用 Claude Code、GitHub Copilot 和 OpenAI Codex）来工作，而有些则需要手动安装 ACP 服务器（例如 Google Antigravity）。由于它们需要在你的设备上安装某些东西，这些提供商在移动端（Android 或 iOS）或独立模式下不可用。

另请参阅专门的 <a class="reference-link" href="../Privacy.md">隐私</a> 部分，以更好地了解哪些数据会被发送到云提供商。

## 使用 Flatpak

Trilium 的 Flatpak 版本（参见 [从 Flathub 安装](../../Installation%20%26%20Setup/Desktop%20Installation.md)）运行在一个沙箱中，该沙箱隐藏了你计算机上安装的程序，因此它自身无法找到 Claude Code、GitHub Copilot CLI、Codex CLI 或 Google 的 Antigravity ACP 服务器。一旦你允许，Trilium 就可以在沙箱外启动它们：

1.  在你的计算机上安装 CLI 并登录，如下文针对每个提供商所述。
2.  通过在终端中运行以下命令，允许 Trilium 在其沙箱外启动程序：
    
    ```sh
    flatpak override --user --talk-name=org.freedesktop.Flatpak org.triliumnotes.Trilium
    ```
3.  重启 Trilium，然后转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加该提供商。

随后 Trilium 会在你计算机的 `PATH` 以及你登录 shell 的 `PATH` 中查找该 CLI，并通过 `flatpak-spawn --host` 在那里启动它。在授予权限之前，添加这些提供商中的任何一个都会失败，并显示一条重复这些步骤的消息。

> [!WARNING]
> 此权限允许 Trilium 在你的计算机上于沙箱外运行任何程序，这与 Flatpak 之外的安装所具有的访问权限相同。要收回该权限，请运行 `flatpak override --user --no-talk-name=org.freedesktop.Flatpak org.triliumnotes.Trilium` 并重启 Trilium。

用于将 Trilium 指向某个 CLI 的环境变量（例如 `TRILIUM_CLAUDE_CODE_PATH`）命名的是沙箱内的文件，因此在使用 Flatpak 时，请保持它们未设置，让 Trilium 在你的计算机上查找该 CLI。

## <span class="tn-icon tn-brand tn-brand-claude"></span> Claude Code

要使用订阅：

1.  首先，Claude Code 需要安装在运行 Trilium 的机器上。因此，对于<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>，Claude 需要安装在本地；对于通过浏览器访问的<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，Claude 需要安装在服务器上。
2.  Claude Code 必须已经过身份验证。为此，请在终端中运行一次 `claude`，输入 `/login` 并按照说明操作。
3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 Claude Code 提供商。

<details>
    <summary>Trilium 如何识别你的 Claude Code 二进制文件</summary>
    <p>按以下顺序：</p>
    <ul>
        <li>查找指向 Claude 二进制文件的 <code>TRILIUM_CLAUDE_CODE_PATH</code> 环境变量。这允许在需要时覆盖路径。</li>
        <li>在你的 PATH 中查找 <code>claude</code>，在大多数情况下通常有效。</li>
        <li>向你的登录 shell 询问其 <code>PATH</code>，这使桌面安装能够找到通过 <code>nvm</code>、<code>fnm</code>、<code>asdf</code> 或 Homebrew 安装的 CLI，因为通过 GUI 启动的应用不会继承你终端的环境。</li>
    </ul>
</details>

设置好提供商后，你将受益于与 API 密钥相同的功能（笔记工具、网络搜索、扩展思考、图像/PDF 附件、流式传输）。

> [!NOTE]
> Trilium 有意使用你的 Claude Code 二进制文件，以避免随附打包一个约 250 MB 的客户端，但这也有代价：如果本地安装的版本与 Trilium 期望的版本不匹配，则存在版本不兼容的小风险。通常最好将 Claude Code 和 Trilium 都保持更新到最新版本。

## <span class="tn-icon tn-brand tn-brand-github-copilot"></span> GitHub Copilot

> [!NOTE]
> 此基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金并遵守使用条款），但你可能会遇到一些小问题。请考虑<a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

GitHub Copilot 无需 API 密钥即可访问你的 GitHub Copilot 订阅（Pro、Pro+、Business 或 Enterprise）的模型。使用量会计入你的 Copilot 计划。

1.  在运行 Trilium 的机器上安装 GitHub Copilot CLI，例如使用 `npm install -g @github/copilot`。与 Claude Code 一样，对于<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，它需要安装在服务器上。
2.  在终端中运行一次 `copilot login` 以登录。如果你已在该机器的另一个编辑器中使用 GitHub Copilot，则会复用该登录。
3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 GitHub Copilot 提供商。

<details>
    <summary>Trilium 如何识别你的 Copilot CLI 二进制文件</summary>
    <p>按以下顺序：</p>
    <ul>
        <li>查找指向 Copilot 二进制文件的 <code>TRILIUM_COPILOT_PATH</code> 环境变量。</li>
        <li>在你的 PATH 中查找 <code>copilot</code>。</li>
        <li>向你的登录 shell 询问其 <code>PATH</code>，与 Claude Code 相同。</li>
    </ul>
</details>

### 已知限制

*   该代理只能通过 Trilium 的笔记工具处理你的笔记；出于安全原因，它自己的文件、shell 和网络工具被阻止。
*   图像可以附加到对话中，PDF 则不能。当启用笔记工具时，大语言模型仍应能够通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>读取 PDF 笔记和附件。

## <span class="tn-icon tn-brand tn-brand-antigravity"></span> Google Antigravity

> [!NOTE]
> 此基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金并遵守使用条款），但你可能会遇到一些小问题。请考虑<a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

Google Antigravity 无需 API 密钥即可使用 Google 账户（免费、Google AI Pro 或 Google AI Ultra）访问 Gemini 模型。在撰写本文时，免费的 Google 账户就足以使用它。

与 Claude Code 或 GitHub Copilot 不同，Google 的 Antigravity ACP 服务器不是 CLI 的一部分，因此需要专门为 Trilium 手动安装。下载的压缩包约为 112-334 MB，解压后的大小根据平台约为 230 MB-2 GB。

=== "<span class="tn-icon bx bxl-windows"></span> Windows"

    1.  下载适用于你平台的 Google Antigravity ACP 服务器。在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 中添加提供商时会显示该链接。在运行 Trilium 的设备上解压它。
    2.  使其可被 Trilium 找到，可以：
        1.  将解压后的文件夹添加到你的 PATH，或
        2.  设置一个指向 `agy_acp_server.exe` 的 `TRILIUM_ANTIGRAVITY_ACP_PATH` 环境变量。
    3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI / LLM 并添加 <span class="tn-icon tn-brand tn-brand-antigravity"></span> _Google Antigravity_ 提供商。首次加载模型列表时，Google 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

=== "<span class="tn-icon bx bxl-tux"></span> Linux 与 <span class="tn-icon bx bxl-apple"></span> macOS"

    1.  下载适用于你平台的 Google Antigravity ACP 服务器。在<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 中添加提供商时会显示该链接。在运行 Trilium 的设备上解压它。
    2.  使其可被 Trilium 找到，可以：
        1.  将解压后的文件夹添加到你的 PATH，或
        2.  设置一个指向 `agy_acp_server.par` 的 `TRILIUM_ANTIGRAVITY_ACP_PATH` 环境变量。
    3.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI / LLM 并添加 <span class="tn-icon tn-brand tn-brand-antigravity"></span> _Google Antigravity_ 提供商。首次加载模型列表时，Google 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

=== "NixOS"

    1.  在 NixOS 上，`antigravity-acp` 包已经可用，但在撰写本文时仅在 `nixos-unstable` 中。测试它的最简单方法是使用带 flakes 的 `nix shell`：
        
        ```
        NIXPKGS_ALLOW_UNFREE=1 nix shell --impure github:nixos/nixpkgs/nixos-unstable#antigravity-acp
        trilium
        ```
    2.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI / LLM 并添加 <span class="tn-icon tn-brand tn-brand-antigravity"></span> _Google Antigravity_ 提供商。首次加载模型列表时，Google 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

> [!NOTE]
> Trilium 需要 `curl` 才能使用 Google Antigravity。它随 Windows 10 及更高版本、macOS 和大多数 Linux 发行版一起提供。

### 已知限制

*   该代理只能通过 Trilium 的笔记工具处理你的笔记；出于安全原因，它自己的文件和 shell 工具被阻止。
*   Antigravity ACP 服务器需要通过登录链接进行身份验证。登录链接需要在同一设备上运行，因此在使用 Docker 安装的 Web 版本时可能无法设置该提供商。<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>应该可以正常工作。
*   图像可以附加到对话中，PDF 则不能。当启用笔记工具时，大语言模型仍应能够通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>读取 PDF 笔记和附件。
*   工具调用的结果（例如读取笔记、写入属性）无法正确显示，因为 ACP 服务器未公开它们。

## <span class="tn-icon tn-brand tn-brand-codex"></span> OpenAI Codex

> [!NOTE]
> 此基于订阅的提供商仍处于测试阶段。使用是安全的（不会使用额外资金并遵守使用条款），但你可能会遇到一些小问题。请考虑<a class="reference-link" href="../../Troubleshooting/Reporting%20issues.md">报告问题</a>。

OpenAI Codex 无需 API 密钥即可访问你的 ChatGPT 计划（Free、Go、Plus、Pro 或 Business）的 Codex 模型。在撰写本文时，免费的 ChatGPT 账户就足以使用它。使用量会计入你计划的 Codex 限制，Free 计划上的限制很小。

=== "<span class="tn-icon bx bxl-windows"></span><span class="tn-icon bx bxl-tux"></span><span class="tn-icon bx bxl-apple"></span> 大多数平台"

    1.  在运行 Trilium 的机器上安装 Codex CLI，例如使用 `npm install -g @openai/codex`。与 Claude Code 一样，对于<a class="reference-link" href="../../Installation%20%26%20Setup/Server%20Installation.md">服务器安装</a>，它需要安装在服务器上。Trilium 随附了连接到它的 ACP 适配器，因此无需其他操作。
    2.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 <span class="tn-icon tn-brand tn-brand-codex"></span> _OpenAI Codex_ 提供商。首次加载模型列表时，ChatGPT 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

=== "NixOS"

    1.  在 NixOS 上，Codex 在 nixpkgs 中作为 `codex` 包提供。稳定通道可能落后于 Codex 的发布版本，因此可以从 `nixos-unstable` 获取较新的版本：
        
        ```sh
        nix shell github:nixos/nixpkgs/nixos-unstable#codex
        trilium
        ```
    2.  转到 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 并添加 <span class="tn-icon tn-brand tn-brand-codex"></span> _OpenAI Codex_ 提供商。首次加载模型列表时，ChatGPT 登录页面会在运行 Trilium 的机器上的浏览器中打开；在那里完成登录。

Trilium 保留自己的 Codex 登录和设置，与你在终端中使用的任何 Codex CLI 分开，因此不会复用现有的 `codex login`。

<details>
    <summary>Trilium 如何识别你的 Codex CLI 二进制文件</summary>
    <p>按以下顺序：</p>
    <ul>
        <li>查找指向 Codex 二进制文件的 <code>TRILIUM_CODEX_PATH</code> 环境变量。</li>
        <li>在你的 PATH 中查找 <code>codex</code>。</li>
        <li>向你的登录 shell 询问其 <code>PATH</code>，与 Claude Code 相同。</li>
    </ul>
</details>

> [!NOTE]
> Trilium 需要 `curl` 才能使用 OpenAI Codex，与 Google Antigravity 相同：Trilium 通过它检查 Codex 进行的每次工具调用。它随 Windows 10 及更高版本、macOS 和大多数 Linux 发行版一起提供。

### 已知限制

*   该代理只能通过 Trilium 的笔记工具处理你的笔记，并在对话允许时搜索网络；出于安全原因，它自己的文件、shell 和其他工具被阻止。
*   ChatGPT 登录会在运行 Trilium 的设备上的浏览器中打开，因此在使用 Docker 安装的 Web 版本时可能无法设置该提供商。<a class="reference-link" href="../../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>应该可以正常工作。
*   图像和 SVG 可以附加到对话中，PDF 则不能。当启用笔记工具时，大语言模型仍应能够通过<a class="reference-link" href="../../Advanced%20Usage/Text%20Extraction%20(OCR).md">文本提取（OCR）</a>读取 PDF 笔记和附件。