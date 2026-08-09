# 身份验证
## 禁用身份验证

如果你仅在 `localhost` 上运行 Trilium，或者身份验证由其他组件处理，你可以通过在 `config.ini` 中添加以下内容来禁用 Trilium 的身份验证：

```
[General]
noAuthentication=true
```

自 v0.94.1 起，禁用身份验证将绕过包括 <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">多重身份验证</a> 在内的所有验证。

## 了解会话的工作方式

一旦登录 Trilium，应用程序会将登录信息存储在浏览器中的 cookie 中，同时也会在服务器上存储为会话。

如果勾选了“记住我”，则登录将在 21 天后过期。可以通过修改 `config.ini` 中的 `Session.cookieMaxAge` 值来调整此期限。例如，将会话设置为一天后过期：

```
[Session]
cookieMaxAge=86400
```

当未勾选“记住我”时，行为会有所不同。在客户端/浏览器层面，身份验证没有过期日期，但会在用户关闭浏览器时立即自动清除。然而，服务器也会在与应用程序_最后一次交互_后约 24 小时内解除此身份验证。

## 查看活动会话

登录会话现在与用户数据一起存储在同一个 <a class="reference-link" href="../../Advanced%20Usage/Database.md">数据库</a> 中。要查看哪些会话处于活动状态，请打开 <a class="reference-link" href="../../Advanced%20Usage/Database/Manually%20altering%20the%20database/SQL%20Console.md">SQL 控制台</a> 并运行以下查询：

```
SELECT * FROM sessions
```

过期的会话会由服务器定期清理，通常每小时清理一次。

## 另请参阅

*   <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">多重身份验证</a>