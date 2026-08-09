# 使用 OpenID Connect 登录

OpenID 是一种标准化方式，允许您使用其他服务（如 Google 或 Authelia）的账户登录网站，以验证您的身份。

当 OpenID 被激活时，Trilium 中基于密码的身份验证将被一个使用您的提供商进行连接的按钮所取代。这意味着 <a class="reference-link" href="Multi-factor%20authentication%20with%20TOTP.md">使用 TOTP 的多因素身份验证</a> 的配置将不再生效，因为任何多因素身份验证都必须由您的提供商来处理。

## 设置

使用 OpenID Connect 设置身份验证是一个两步过程：

1.  首先，必须使用您的身份验证提供商的相关信息（如 URL、客户端 ID 和密钥）来配置 Trilium 服务器。
2.  其次，用户必须从选项中进行连接，以在提供商的账户和 Trilium 的账户之间建立链接。

### 配置身份验证提供商

1.  首先，确保身份验证提供商（例如 Google、Authelia）已正确配置。具体示例请参阅 <a class="reference-link" href="Signing%20in%20with%20OpenID%20Connect/Setting%20up%20with%20various%20providers.md">使用各种提供商进行设置</a>。
    
    1.  Trilium 的重定向 URL 是 `https://<your-trilium-domain>/callback`。
    2.  您应该获取基础 URL、客户端 ID 和客户端密钥。
2.  使用 <a class="reference-link" href="../../Advanced%20Usage/Configuration%20(config.ini%20or%20environment%20variables).md">配置（config.ini 或环境变量）</a> 设置以下信息：
    
    | 配置 | `config.ini` 中的 `[MultiFactorAuthentication]` 部分 | 环境变量 | 描述 |
    | --- | --- | --- | --- |
    | 基础 URL\* | `oauthBaseUrl` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL` | 您的 Trilium 实例的 URL（例如 `https://example.com`）。 |
    | 客户端 ID\* | `oauthClientId` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTID` | 来自您的提供商配置的客户端 ID。 |
    | 客户端密钥\* | `oauthClientSecret` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTSECRET` | 来自您的提供商配置的客户端密钥。 |
    | 客户端认证方法 | `oauthClientAuthMethod` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTAUTHMETHOD` | 令牌端点认证方法：`client_secret_basic` 或 `client_secret_post`。留空则自动检测。仅在登录失败并出现 `WWW-Authenticate` 或 `invalid_client` 错误时需要。 |
    | ID 令牌算法 | `oauthIdTokenSigningAlg` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHIDTOKENSIGNINGALG` | <span style="color:rgb(32,32,32)">您的提供商用于签署 ID 令牌的算法，例如</span> `RS256`<span style="color:rgb(32,32,32)">、</span> `EdDSA`<span style="color:rgb(32,32,32)">、</span> `ES256`<span style="color:rgb(32,32,32)">。留空则从提供商自动检测。仅在登录失败并出现</span> `unexpected JWT alg` <span style="color:rgb(32,32,32)">错误时需要。</span> |
    
    星号（\*）表示必填字段
3.  默认的 OAuth 颁发者是 Google。要使用其他服务（如 Authentik 或 Auth0），您可以通过 `config.ini` 文件中的 `oauthIssuerBaseUrl`、`oauthIssuerName` 和 `oauthIssuerIcon` 配置设置。或者，这些值也可以使用环境变量设置：
    
    | 配置 | `config.ini` 中的 `[MultiFactorAuthentication]` 部分 | 环境变量 | 描述 |
    | --- | --- | --- | --- |
    | 颁发者基础 URL | `oauthIssuerBaseUrl` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERBASEURL` | 可以是颁发者本身（`https://auth.example.com`）或完整的发现 URL（`https://auth.example.com/.well-known/openid-configuration`）。<br>  <br>包含 `/.well-known/` 的 URL 将按原样使用<span style="color:rgb(32,32,32)">，当您的提供商给您一个发现 URL 以便复制时，这很方便。尾部斜杠可以包含也可以省略；Trilium 会匹配提供商通告的任意拼写。</span>  <br>  <br>当您的提供商通告的颁发者与其提供发现文档的路径不同时（例如 Authentik 的“全局”颁发者模式），请使用完整形式。 |
    | 颁发者名称 | `oauthIssuerName` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERNAME` | 您的身份验证提供商的名称，用于登录屏幕和设置中的参考。默认为“Google”。 |
    | 颁发者图标 | `oauthIssuerIcon` | `TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERICON` | 可选，提供商标志的 URL。默认情况下，它会尝试从网站获取 favicon，因此这是可选的。 |
    
    这里的所有字段都是可选的，因为默认的 OAuth 颁发者是 Google。
4.  重启服务器以使更改生效。

> [!NOTE]
> 也支持旧版环境变量：`TRILIUM_OAUTH_BASE_URL`、`TRILIUM_OAUTH_CLIENT_ID`、`TRILIUM_OAUTH_CLIENT_SECRET`，以及用于自定义提供商的：`TRILIUM_OAUTH_ISSUER_BASE_URL`、`TRILIUM_OAUTH_ISSUER_NAME`、`TRILIUM_OAUTH_ISSUER_ICON`、`TRILIUM_OAUTH_CLIENT_AUTH_METHOD`、`TRILIUM_OAUTH_ID_TOKEN_SIGNING_ALG`。

## 连接到身份验证提供商

在上一步骤中服务器配置完成后，下一步是在您的身份验证提供商账户和 Trilium 实例之间建立链接。这可以确保只有您能访问 Trilium 实例，而不是任何其他有效账户。

操作步骤如下：

1.  前往 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _密码与认证。_
2.  在 _使用以下方式登录_ 字段中，选择 _OpenID Connect 提供商。_
3.  在 _OpenID Connect_ 部分，查找 _连接账户_ 按钮。
4.  这将重定向到您的身份验证提供商，您可以在那里登录或在需要时确认操作。
5.  一旦您通过身份验证，您将被重定向回 Trilium 应用程序。

## 登出

当登出 Trilium 时，也会向身份验证提供商发出请求，要求其同时登出。此功能取决于身份验证提供商，因此可能不被支持（已知 Google 和 Authelia 不遵守登出功能）。

## 切换提供商

在切换提供商时（例如从 Google 切换到 Authelia），务必遵循以下步骤：

1.  前往 <a class="reference-link" href="../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _密码与认证_。
2.  在 _OpenID Connect_ 部分，按下 _断开连接_ 按钮。
3.  等待该部分指示您已断开连接。
4.  更改指向新提供商的配置。
5.  重启您的服务器。
6.  重复连接到身份验证提供商的常规步骤。

在切换提供商之前未能断开连接可能会暂时将您锁定，因为您将无法登录（凭据不匹配）。如果发生这种情况：

1.  再次将服务器配置修改回您的旧提供商。
2.  重启服务器并按照上述断开连接说明操作。
3.  再次将服务器配置修改为您的新提供商。
4.  再次重启服务器。

## 临时停用 OpenID Connect

要禁用 OpenID Connect 身份验证并临时依赖本地密码，您必须：

1.  修改 `config.ini` 或环境变量（取决于您如何设置提供商信息），并通过将 `[MultiFactorAuthentication]` 重命名为其他名称（例如 `[MultiFactorAuthentication.bak]`）来临时停用多因素身份验证部分。
2.  重启服务器以使更改生效。

## 故障排除

### 设置失败并出现 `WWW-Authenticate` 或 `invalid_client` 错误

您的提供商与 Trilium 在客户端凭据应如何发送到令牌端点的问题上存在分歧。将 `oauthClientAuthMethod` 设置为 `client_secret_post`（如果已设置为 post，则设置为 `client_secret_basic`）并重启。提供商各不相同：有些提供商（例如 Authelia）会直接拒绝 `client_secret_post`，因为客户端注册时该方法是固定的，所以如果一个值不起作用，请尝试另一个。

### 设置失败并出现 `invalid user` 错误

如果您在 [反向代理](2.%20Reverse%20proxy.md) 后面运行，缓冲区溢出也可能导致此问题。以下是针对 <a class="reference-link" href="2.%20Reverse%20proxy/Nginx.md">Nginx</a> 的示例修复方法：

```
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;
```

### 设置失败并出现 `unexpected JWT alg` 错误

根据您的版本，消息可能显示为 `unexpected JWT "alg" header parameter` 或 `unexpected JWT alg received, expected RS256, got: EdDSA`。两者含义相同：您的提供商使用 RS256 以外的算法签署 ID 令牌。Pocket ID (Ed25519) 和 Kanidm (ES256) 就是这样做的。

从 v0.104.2 开始，Trilium 会自动从您的提供商检测算法，并且日志会记录结果（`OAuth: the issuer does not sign ID tokens with RS256; expecting ES256`）。如果检测无法到达提供商，它将回退到 RS256，因此请首先检查颁发者 URL 是否正确且可访问。如果仍然失败，请将 `oauthIdTokenSigningAlg` 显式设置为您的提供商使用的算法。

### 设置失败并出现 `OAUTH_RESPONSE_IS_NOT_CONFORM` 错误

确保基础 URL 正确，并且身份提供商确实支持 OpenID Connect。某些提供商（如 GitHub）仅提供 OAuth 2.0。