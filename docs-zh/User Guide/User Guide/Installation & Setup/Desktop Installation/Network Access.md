# 网络访问

在 v0.104.0 版本之前，[桌面应用程序](../Desktop%20Installation.md) 也会开放一个网络端口，以便提供对 <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 的访问，甚至可以用作 Web 服务器（参见 <a class="reference-link" href="Using%20the%20desktop%20application%20as%20a%20server.md">将桌面应用程序用作服务器</a>）。

为了减少攻击面，Trilium 现在仅为本机设备（例如 `localhost`）启用这些服务，而不再通过局域网提供访问。

为了更好地理解受影响的功能，请参考下表：

| 功能 | 网络访问关闭 | 网络访问开启 |
| --- | --- | --- |
| <a class="reference-link" href="../Web%20Clipper.md">Web Clipper</a> | 🔒️ 仅 `localhost`（同一设备上的浏览器扩展仍可访问） | 🌐 `localhost` + 局域网 |
| <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> | 🔒️ 仅 `localhost` | 🌐 `localhost` + 局域网 |
| [LLM MCP](../../AI.md)（仅在设置中启用时） | 🔒️ 仅 `localhost`（需要身份验证） | 🌐 `localhost` + 局域网（需要身份验证） |
| [Web 应用](Using%20the%20desktop%20application%20as%20a%20server.md) | ❌️ 完全禁用（403），仅可使用桌面应用程序。 | 🌐 `localhost` + 局域网 |
| <a class="reference-link" href="../../Advanced%20Usage/Sharing.md">分享</a> 笔记 | ❌️ 完全禁用（403），如果您使用 <a class="reference-link" href="../Synchronization.md">同步</a>，此功能仍可作为[服务器](../Server%20Installation.md)的一部分正常工作。 | 🌐 `localhost` + 局域网 |