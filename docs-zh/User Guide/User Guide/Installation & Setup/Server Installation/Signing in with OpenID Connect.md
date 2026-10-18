# 使用 OpenID Connect 登录
OpenID 是一种标准化方式，让你可以使用来自其他服务（如 Google 或 Authelia）的账户登录网站，以验证你的身份。

当 OpenID 激活后，Trilium 中基于密码的身份验证将被替换为一个使用你的提供商进行连接的按钮。这意味着<a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">使用 TOTP 的多因素身份验证</a>的配置不再生效，因为你的提供商必须处理任何多因素身份验证。

## 设置

使用 OpenID Connect 设置身份验证是一个两步过程：

1.  首先，必须为 Trilium 服务器配置有关你的身份验证提供商的信息，例如 URL、客户端 ID 和密钥。
2.  其次，用户必须从选项中连接，以在提供商上的账户与 Trilium 拥有的账户之间创建链接。

### 配置身份验证提供商

1.  首先，确保身份验证提供商（例如 Google、Authelia）已正确配置。有关具体示例，请参阅<a class="reference-link" href="Signing%20in%20with%20OpenID%20Connect/Setting%20up%20with%20various%20providers.md">使用各种提供商进行设置</a>。
    
    1.  Trilium 的重定向 URL 为 `https://<your-trilium-domain>/callback`。
    2.  你应该获取基础 URL、客户端 ID 和客户端密钥。
2.  使用<a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a>设置以下信息：
    
    | 配置 | `[MultiFactorAuthentication]` 部分中的 `config.ini` | 环境变量 | 描述 |
    | --- | --- | --- | --- |
    | 基础 URL\* | `oauthBaseUrl` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL` | 你的 Trilium 实例的 URL（例如 `https://example.com`）。 |
    | 客户端 ID\* | `oauthClientId` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTID` | 来自你的提供商配置的客户端 ID。 |
    | 客户端密钥\* | `oauthClientSecret` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTSECRET` | 来自你的提供商配置的客户端密钥。 |
    | 客户端身份验证方法 | `oauthClientAuthMethod` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTAUTHMETHOD` | 令牌端点身份验证方法：`client_secret_basic` 或 `client_secret_post`。留空则自动检测。仅在登录失败并出现 `WWW-Authenticate` 或 `invalid_client` 错误时需要。 |
    | ID 令牌算法 | `oauthIdTokenSigningAlg` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHIDTOKENSIGNINGALG` | <span style="color:rgb(32,32,32);">你的提供商用于签署 ID 令牌的算法，例如</span> `RS256`<span style="color:rgb(32,32,32);">、</span> `EdDSA`<span style="color:rgb(32,32,32);">、</span> `ES256`<span style="color:rgb(32,32,32);">。留空则从提供商自动检测。仅在登录失败并出现</span> `unexpected JWT alg` <span style="color:rgb(32,32,32);">错误时需要。</span> |
    
    星号（\*）标记为必填字段
3.  默认的 OAuth 发行方是 Google。要使用其他服务（如 Authentik 或 Auth0），你可以通过 `config.ini` 文件中的 `oauthIssuerBaseUrl`、`oauthIssuerName` 和 `oauthIssuerIcon` 配置设置。或者，也可以使用环境变量设置这些值：
    
    | 配置 | `[MultiFactorAuthentication]` 部分中的 `config.ini` | 环境变量 | 描述 |
    | --- | --- | --- | --- |
    | 发行方基础 URL | `oauthIssuerBaseUrl` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERBASEURL` | 可以是发行方本身（`https://auth.example.com`），也可以是完整的发现 URL（`https://auth.example.com/.well-known/openid-configuration`）。  <br>  <br>包含 `/.well-known/` 的 URL 将按原样使用<span style="color:rgb(32,32,32);">，当你的提供商提供发现 URL 供你复制时，这很方便。末尾斜杠可以包含也可以省略；Trilium 会匹配提供商所公布的任一写法。</span>  <br>  <br>当你的提供商公布的发行方与其提供发现文档的路径不同时（例如处于“global”发行方模式的 Authentik），请使用完整形式。 |
    | 发行方名称 | `oauthIssuerName` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERNAME` | 你的身份验证提供商的名称，用于在登录屏幕和设置中作为参考。默认为“Google”。 |
    | 发行方图标 | `oauthIssuerIcon` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERICON` | 可选，提供商徽标的 URL。默认情况下会尝试从网站获取 favicon，因此它是可选的。 |
    
    此处的所有字段都是可选的，因为默认的 OAuth 发行方是 Google。
4.  可选地，调整以下高级设置。所有设置都是可选的，并且具有合理的默认值：
    
    | 配置 | `[MultiFactorAuthentication]` 部分中的 `config.ini` | 环境变量 | 描述 |
    | --- | --- | --- | --- |
    | HTTP 超时 | `oauthHttpTimeout` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHHTTPTIMEOUT` | 提供商 HTTP 请求（发现、令牌交换、用户信息）的超时时间（毫秒）。默认为 `30000`（30 秒）。如果你的提供商冷启动较慢并且你偶尔被要求登录两次，请调高此值。可接受的最小值为 `500`。 |
    | 作用域 | `oauthScope` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHSCOPE` | 登录时请求的 OIDC 作用域的空格分隔列表。默认为 `openid profile email`。`openid` 是必需的，如果你省略它，它会自动添加到前面。 |
    
    OIDC 会话生命周期自动绑定到 Trilium 自身的会话 cookie 生命周期（`[Session]` 部分中的 `cookieMaxAge` 设置，默认为 21 天），因此单次登录在 Trilium 会话有效期内保持有效，而不会因 OIDC 库较短的内部默认值而提前过期。
5.  重启服务器以应用更改。

> [!NOTE]
> 也支持旧版环境变量：`TRILIUM_OAUTH_BASE_URL`、`TRILIUM_OAUTH_CLIENT_ID`、`TRILIUM_OAUTH_CLIENT_SECRET`，以及用于自定义提供商的：`TRILIUM_OAUTH_ISSUER_BASE_URL`、`TRILIUM_OAUTH_ISSUER_NAME`、`TRILIUM_OAUTH_ISSUER_ICON`、`TRILIUM_OAUTH_HTTP_TIMEOUT`、`TRILIUM_OAUTH_SCOPE`、`TRILIUM_OAUTH_CLIENT_AUTH_METHOD`、`TRILIUM_OAUTH_ID_TOKEN_SIGNING_ALG`。

## 连接到身份验证提供商

一旦服务器在上一步中配置完成，下一步就是在身份验证提供商上的账户与 Trilium 实例之间创建链接。这确保只有你才能访问 Trilium 实例，而不是任何其他有效账户。

为此：

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _密码与身份验证。_
2.  在 _使用以下方式登录_ 字段中，选择 _OpenID Connect 提供商。_
3.  在 _OpenID Connect_ 部分中，查找 _连接账户_（<span class="tn-icon bx bx-log-in"></span>）按钮。
4.  这会将你重定向到你的身份验证提供商，你可以在那里登录或在需要时确认操作。
5.  一旦你通过身份验证，你将被重定向回 Trilium 应用程序。

## 注销

从 Trilium 注销时，会向身份验证提供商发出请求，以便也从那里注销。此功能取决于身份验证提供商，因此可能不被遵守（Google 和 Authelia 是已知不遵守注销功能的情况）。

## 切换提供商

切换提供商时（例如从 Google 切换到 Authelia），采取以下步骤很重要：

1.  转到<a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _密码与身份验证_。
2.  在 _OpenID Connect_ 部分中，按 _断开连接_（<span class="tn-icon bx bx-trash"></span>）按钮。
3.  等待该部分指示你已断开连接。
4.  更改配置以指向新的提供商。
5.  重启你的服务器。
6.  重复正常步骤以连接到身份验证提供商。

在切换提供商之前未能断开连接可能会暂时将你锁定，因为你将无法登录（凭据不匹配）。如果发生这种情况：

1.  再次将服务器配置修改为你的旧提供商。
2.  重启服务器并按照上述断开连接说明操作。
3.  再次将服务器配置修改为你的新提供商。
4.  再次重启服务器。

## 临时停用 OpenID Connect

要禁用 OpenID Connect 身份验证并暂时依赖本地密码，你必须：

1.  修改 `config.ini` 或环境变量（取决于你如何设置提供商信息），并通过将 `[MultiFactorAuthentication]` 重命名为其他名称（例如 `[MultiFactorAuthentication.bak]`）来临时停用多因素身份验证部分。
2.  重启服务器以使更改生效。

## 故障排除

### 设置失败并出现 `WWW-Authenticate` 或 `invalid_client` 错误

你的提供商与 Trilium 在如何将客户端凭据发送到令牌端点方面存在分歧。将 `oauthClientAuthMethod` 设置为 `client_secret_post`（如果已设置为 post，则设置为 `client_secret_basic`）并重启。提供商各不相同：有些会直接拒绝 `client_secret_post`，因为该方法在客户端注册时是固定的（例如 Authelia），因此如果一个值不起作用，请尝试另一个。

### 设置失败并出现 `invalid user`

如果你在[反向代理](2.%20Reverse%20proxy.md)后面运行，缓冲区溢出也可能导致此问题。以下是针对<a class="reference-link" href="2.%20Reverse%20proxy/Nginx.md">Nginx</a>的示例修复：

```
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;
```

### 设置失败并出现 `unexpected JWT alg` 错误

根据你的版本，消息会显示为 `unexpected JWT "alg" header parameter` 或 `unexpected JWT alg received, expected RS256, got: EdDSA`。两者含义相同：你的提供商使用 RS256 以外的算法签署 ID 令牌。Pocket ID（Ed25519）和 Kanidm（ES256）会这样做。

从 v0.104.2 起，Trilium 会自动从你的提供商检测算法，日志会记录结果（`OAuth: the issuer does not sign ID tokens with RS256; expecting ES256`）。如果检测无法访问提供商，它会回退到 RS256，因此请先检查发行方 URL 是否正确且可访问。如果仍然失败，请将 `oauthIdTokenSigningAlg` 显式设置为你的提供商使用的算法。

### 设置失败并出现 `OAUTH_RESPONSE_IS_NOT_CONFORM`

确保基础 URL 正确，并且身份提供商确实支持 OpenID Connect。某些提供商（如 GitHub）仅提供 OAuth 2.0。