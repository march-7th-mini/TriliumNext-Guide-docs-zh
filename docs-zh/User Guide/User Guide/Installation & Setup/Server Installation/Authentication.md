# 身份验证
## 禁用身份验证

如果你仅在 `localhost` 上运行 Trilium，或者身份验证由其他组件处理，你可以通过向 `config.ini` 添加以下内容来禁用 Trilium 的身份验证：

```
[General]
noAuthentication=true
```

自 v0.94.1 起，禁用身份验证甚至会绕过 <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">多因素身份验证</a>。

## 暴力破解防护

Trilium 将每个 IP 地址在 15 分钟内的登录失败尝试限制为 10 次。一旦某个地址达到该限制，Trilium 会拒绝来自该地址的所有后续尝试（包括正确的尝试），直到 15 分钟过去。登录页面随后会显示 _登录尝试次数过多_；其他客户端会收到 HTTP 状态码 429。

该限制适用于所有使用密码登录的方式：

*   登录页面。
*   从桌面或移动应用设置 <a class="reference-link" href="../Synchronization.md">同步</a>。
*   连接 <a class="reference-link" href="../Web%20Clipper.md">网页剪藏器</a> 或 Android 发送器应用。
*   通过 <a class="reference-link" href="../../Advanced%20Usage/ETAPI%20(REST%20API).md">ETAPI (REST API)</a> 请求令牌。

所有这些方式都计入同一限制，错误的密码、错误的一次性密码和错误的恢复代码各计为一次失败尝试。成功的登录不计入。

该限制是按 IP 地址而非按账户计算的，因此攻击者无法通过从自己的地址登录失败来将你锁定在外。计数保存在内存中：重启服务器即可清除。

> [!IMPORTANT]
> 在反向代理后面，除非配置为 <a class="reference-link" href="2.%20Reverse%20proxy/Trusted%20proxy.md">受信任代理</a>，否则 Trilium 会将每个请求都视为来自代理。此时所有客户端共享同一限制，因此任何人几次错误的尝试都会阻止所有人。

### 使用 fail2ban 阻止重复失败

登录页面上的失败尝试会以 HTTP 状态码 401 响应，并在 <a class="reference-link" href="../../Troubleshooting/Error%20logs/Backend%20(server)%20logs.md">后端（服务器）日志</a> 中记录为：

```
WARNING: Wrong password from 203.0.113.7, rejecting.
```

当启用 <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">多因素身份验证</a> 时，错误的一次性密码或恢复代码会记录为 `Wrong totp`。fail2ban 等工具可以匹配该日志行，或匹配反向代理访问日志中对 `POST /login` 的 401 响应，从而将某个地址阻止超过 15 分钟。

## 了解会话的工作方式

登录 Trilium 后，应用程序会将这些登录信息存储在浏览器的 cookie 中，同时也会作为服务器上的一个会话存储。

如果勾选了“记住我”，则登录将在 21 天后过期。可以通过修改 `config.ini` 中的 `Session.cookieMaxAge` 值来调整此期限。例如，要让会话在一天后过期：

```
[Session]
cookieMaxAge=86400
```

当未勾选“记住我”时，行为有所不同。在客户端/浏览器层面，身份验证没有任何过期日期，但用户关闭浏览器后它会被自动清除。不过，服务器也会在_与应用程序的最后一次交互_之后约 24 小时内撤销此身份验证。

更改或重置密码会注销所有会话，包括执行更改的那个会话：打开的标签页会返回登录屏幕，你可以在那里使用新密码重新登录。当密码在另一个实例上更改并通过同步到达服务器时，这也同样适用。如果你怀疑有人获取了你的会话 cookie，更改密码会切断他们的访问。

## 查看活动会话

登录会话现在与用户数据存储在同一个 <a class="reference-link" href="../../Advanced%20Usage/Database.md">数据库</a> 中。要查看哪些会话处于活动状态，请打开 <a class="reference-link" href="../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a> 并运行以下查询：

```
SELECT * FROM sessions
```

过期的会话会由服务器定期清理，通常为每小时一次。

## 另请参阅

*   <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">多因素身份验证</a>
*   <a class="reference-link" href="2.%20Reverse%20proxy/Trusted%20proxy.md">受信任代理</a>