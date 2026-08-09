# 安全

从 v0.104.0 版本开始，Trilium 中的某些功能会被有意禁用，以减少攻击面：

*   <a class="reference-link" href="Backend%20scripts.md">后端脚本</a>，它可以在服务器上运行进程、访问文件系统或绕过安全措施。
*   <a class="reference-link" href="../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a>，它可用于窃取重要数据（如文档密钥）或对数据库造成不可挽回的损害。
*   <a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation/Network%20Access.md">网络访问</a>，适用于<a class="reference-link" href="../Installation%20%26%20Setup/Desktop%20Installation.md">桌面安装</a>。

要激活其中任何一项，有三种方式：

*   对于桌面应用，请前往 <a class="reference-link" href="../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _安全_ 并切换所需选项。
    *   系统会弹出一个对话框确认更改。请注意，脚本也可能调用此确认对话框，请仅在需要启用这些功能时才接受。
    *   设置页面在服务器端也可用，但需要使用此处描述的其他机制手动切换选项。
    *   这是通过在<a class="reference-link" href="../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>中设置单独的配置文件来实现的。
*   在 [config.ini](../Advanced%20Usage/Configuration%20\(config.ini%20or%20environment%20variables\).md) 中，在 `Security` 组下设置相应选项。
*   或者使用环境变量（例如 `TRILIUM_SECURITY_BACKEND_SCRIPTING_ENABLED=true`）。