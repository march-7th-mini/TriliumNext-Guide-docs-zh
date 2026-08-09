# MCP
[模型上下文协议](https://en.wikipedia.org/wiki/Model_Context_Protocol) 允许诸如 Claude Code 之类的外部聊天应用程序访问 Trilium 数据库。

## 内置 MCP

v0.103.0 附带了一个默认未激活的内置 MCP 服务器。要激活它，请前往 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → AI/大语言模型对话，然后切换 _MCP 服务器_ 选项。

一旦 MCP 激活，只需将 MCP 服务器添加到您的 AI 助手中。要使用的 URL 显示在 MCP 切换开关下方的 _端点_ _URL_ 信息中。

仅支持 HTTP 传输，不支持 `stdio` 方法。如果这成为阻碍，请考虑使用下面列出的第三方替代方案。

暴露给 MCP 的工具与内部对话支持的工具相同（参见 _笔记访问_ 部分）。

### 身份验证

为保护您的笔记免受未经授权的访问，MCP 服务器需要身份验证。通常 MCP 服务器需要支持 OAuth 进行身份验证，但 Trilium 使用一种更简单的基于 Bearer 令牌的机制。

要配置身份验证，首先通过前往 <a class="reference-link" href="../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI（REST API）</a> → _ETAPI_ 创建一个 ETAPI（REST API）令牌。然后按照 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _AI / 大语言模型_ 中的说明操作，查看 MCP 下的 _如何连接助手_ 部分。

## 第三方替代方案

以下是 Trilium 内置 MCP 功能的替代方案。由于 Trilium 的 AI 实现仍处于实验阶段，其工具可能不如外部工具成熟。

*   [perfectra1n/triliumnext-mcp](https://github.com/perfectra1n/triliumnext-mcp)
*   [tan-yong-sheng/triliumnext-mcp](https://github.com/tan-yong-sheng/triliumnext-mcp)
*   [eliassoares/trilium-fastmcp](https://github.com/eliassoares/trilium-fastmcp)

> [!IMPORTANT]
> 这些解决方案是第三方的，因此不受 Trilium Notes 团队的认可或直接支持。请将问题和疑问提交到它们对应的代码仓库。