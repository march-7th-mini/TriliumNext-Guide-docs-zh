# MCP
[模型上下文协议](https://en.wikipedia.org/wiki/Model_Context_Protocol)允许外部对话应用（如 Claude Code）访问 Trilium 数据库。

## 内置 MCP

v0.103.0 自带一个默认未激活的内置 MCP 服务器。要激活它，请前往 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI/大语言模型，并切换 _MCP 服务器_ 选项。

MCP 激活后，只需将 MCP 服务器添加到你的 AI 助手中即可。要使用的 URL 显示在 MCP 开关下方的 _端点 URL_ 信息中。

仅支持 HTTP 传输，不支持 `stdio` 方式。如果这是一个阻碍，请考虑使用下面列出的第三方替代方案。

暴露给 MCP 的工具与内部对话所支持的工具相同（参见 _笔记访问_ 部分）。带有 `#excludeFromLlm` 标签的笔记对两者都隐藏，参见 <a class="reference-link" href="Privacy.md">隐私</a>。

### 批准工具调用

Trilium 不会请求批准外部助手发起的调用；这留给助手自身的权限设置来决定。为了帮助其做出决定，每个工具都会告知助手它是仅读取你的笔记、仅添加内容（创建笔记、克隆笔记或追加内容），还是可以覆盖或删除某些内容（编辑、重命名、移动或删除）。支持这些提示的助手可以自行执行读取操作，并在更改前询问，就像 Trilium 对话中的 _更改前询问_ 那样。

### 身份验证

为了保护你的笔记免遭未经授权的访问，MCP 服务器需要身份验证。通常 MCP 服务器需要支持 OAuth 进行身份验证，但 Trilium 使用一种更简单的机制，即 Bearer 令牌。

要配置身份验证，首先前往 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _ETAPI_ 创建一个 <a class="reference-link" href="../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 令牌。然后按照 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / LLM_ 中的说明操作，查看 MCP 下的 _如何连接助手_ 部分。

## 第三方替代方案

以下是 Trilium 内置 MCP 功能的替代方案。由于 Trilium 的 AI 实现仍处于实验阶段，其工具可能不如外部工具成熟。

*   [perfectra1n/triliumnext-mcp](https://github.com/perfectra1n/triliumnext-mcp)
*   [tan-yong-sheng/triliumnext-mcp](https://github.com/tan-yong-sheng/triliumnext-mcp)
*   [eliassoares/trilium-fastmcp](https://github.com/eliassoares/trilium-fastmcp)

> [!IMPORTANT]
> 这些解决方案均为第三方提供，因此不受 Trilium Notes 团队的直接认可或支持。请在其对应的代码仓库中提出问题和反馈。