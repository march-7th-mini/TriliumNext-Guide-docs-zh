# 网络访问

在 v0.104.0 之前，[桌面应用](../Desktop%20Installation.md)还会打开一个网络端口，以便提供对<a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a>的访问，甚至将其用作 Web 服务器（参见<a class="reference-link" href="Using%20the%20desktop%20application%20as%20a%20server.md">将桌面应用用作服务器</a>）。

为了减少攻击面，Trilium 现在仅对本地设备（例如 `localhost`）启用这些服务，而不再通过局域网提供服务。

为更好地了解受影响的范围，请参阅下表：

| 功能 | 网络访问关闭 | 网络访问开启 |
| --- | --- | --- |
| <a class="reference-link" href="../Web%20Clipper.md">网页剪藏</a> | 🔒️ 仅 `localhost`（同一设备上的浏览器扩展仍可访问） | 🌐 `localhost` + 局域网（需要来自其他设备的身份验证：像[服务器](../Server%20Installation.md)一样从扩展的选项中登录） |
| <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> | 🔒️ 仅 `localhost` | 🌐 `localhost` + 局域网 |
| [LLM MCP](../../AI.md)（仅在设置中启用时） | 🔒️ 仅 `localhost`（需要身份验证） | 🌐 `localhost` + 局域网（需要身份验证） |
| [Web 应用](Using%20the%20desktop%20application%20as%20a%20server.md) | ❌️ 完全禁用（403），仅桌面应用可用。 | 🌐 `localhost` + 局域网 |
| <a class="reference-link" href="../../Advanced%20Usage/Sharing.md">共享</a>笔记 | ❌️ 完全禁用（403），如果您正在使用<a class="reference-link" href="../Synchronization.md">同步</a>，它仍可作为[服务器](../Server%20Installation.md)的一部分正常工作。 | 🌐 `localhost` + 局域网 |