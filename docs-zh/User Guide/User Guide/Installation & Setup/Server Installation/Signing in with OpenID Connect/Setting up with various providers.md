# 使用各种提供商进行设置
本页面包含如何通过多种提供商（如 Authelia、GitLab、Google）设置 <a class="reference-link" href="../Signing%20in%20with%20OpenID%20Connect.md">使用 OpenID Connect 登录</a> 的说明。

> [!NOTE]
> 虽然配置参考是正确且最新的，但创建 OAuth 应用程序的步骤可能会因提供商更改其 UI 而略有不同。

=== "Authelia"

    1.  生成客户端密钥：
        
        ```
        authelia crypto hash generate pbkdf2 --variant sha512 --random --random.length 72 --random.charset rfc3986
        
        ```
        
        `Random Password` 用于 Trilium，`Digest`（即 `$pbkdf2-sha512$…` 字符串）用于 Authelia。
    2.  在 Authelia 的 `configuration.yml` 中，在 `identity_providers.oidc.clients` 下添加一个客户端，将 `<server>` 替换为你的 Trilium 实例的 URL：
        
        ```yaml
        identity_providers:
          oidc:
            clients:
              - client_id: 'trilium'
                client_name: 'Trilium'
                client_secret: '<Digest>'
                public: false
                authorization_policy: 'two_factor'
                redirect_uris:
                  - 'https://<server>/callback'
                scopes:
                  - 'openid'
                  - 'profile'
                  - 'email'
        ```
        
        与 GitLab 不同，`client_id` 是你自己选择的名称，而不是提供商生成的。
    3.  重启 Authelia。

    使用第 1 步中的 `Random Password` 调整 `config.ini`：

    ```
    [MultiFactorAuthentication]
    oauthBaseUrl=https://<server>
    oauthClientId=<ClientId>
    oauthClientSecret=<RandomPassword>
    oauthIssuerBaseUrl=https://<server>
    oauthIssuerName=Authelia
    ```

    > [!IMPORTANT]
    > **不要**为 Authelia 设置 `oauthClientAuthMethod`。它会将机密客户端默认为 `client_secret_basic`，并以 `invalid_client` 拒绝任何其他方法，而这正是 Trilium 已经使用的默认值。这与下面的 GitLab 情况相反。

=== "<span class="tn-icon bx bxl-gitlab"></span> GitLab"

    1.  前往 [gitlab.com](https://gitlab.com/-/user_settings/applications) 或你自己的自托管实例上的用户设置。
    2.  点击 _Add new application_。
    3.  为其命名（例如 Trilium）。
    4.  将 _Redirect URI_ 设置为 `https://<server>/callback`
    5.  确保勾选 _Confidential_ 并取消勾选 _Device authorization grant_。
    6.  在 scopes 下，勾选 _openid_、_profile_ 和 _email_（它们应该靠近末尾）。
    7.  保存应用程序并复制 _Application ID_ 和 _Secret_。

    按如下方式调整 `config.ini`，将 `<ApplicationId>` 和 `<Secret>` 替换为最后一步中的值，并将 `<server>` 替换为你的 Trilium 实例的 URL。

    ```
    [MultiFactorAuthentication]
    oauthBaseUrl=https://<server>
    oauthClientId=<ApplicationId>
    oauthClientSecret=<Secret>
    oauthIssuerBaseUrl=https://gitlab.com
    oauthIssuerName=GitLab
    oauthClientAuthMethod=client_secret_post

    ```

    > [!IMPORTANT]
    > 如果你使用的是自托管的 GitLab 实例，请确保同时更新 `oauthIssuerBaseUrl`，并保留上面的 `oauthClientAuthMethod` 行。
    > 
    > GitLab 的令牌端点不会解码通过 HTTP Basic 发送的凭据，因此如果没有 `oauthClientAuthMethod`，登录会失败并报错 `server responded with a challenge in the WWW-Authenticate HTTP Header`。Trilium 会为 `gitlab.com` 自动应用此项，但无法检测自托管的 issuer URL。

=== "Kanidm"

    1.  创建客户端，添加重定向 URL 并授予 scopes，将 `<server>` 替换为你的 Trilium 实例的 URL，将 `<group>` 替换为成员可以登录的现有 Kanidm 组：
        
        ```
        kanidm system oauth2 create trilium "Trilium" "https://<server>"
        kanidm system oauth2 add-redirect-url trilium "https://<server>/callback"
        kanidm system oauth2 update-scope-map trilium <group> openid profile email
        ```
        
        `openid` scope 是必需的；没有它，Kanidm 会将客户端视为普通的 OAuth 2.0。
    2.  读取客户端密钥：
        
        ```
        kanidm system oauth2 show-basic-secret trilium
        ```

    按如下方式调整 `config.ini`，将 `<idm>` 替换为你的 Kanidm 实例的 URL，将 `<BasicSecret>` 替换为第 2 步中的值：

    ```
    [MultiFactorAuthentication]
    oauthBaseUrl=https://<server>
    oauthClientId=trilium
    oauthClientSecret=<BasicSecret>
    oauthIssuerBaseUrl=https://<idm>/oauth2/openid/trilium
    oauthIssuerName=Kanidm
    ```

    你在第 1 步中选择的客户端名称既是客户端 ID，也是 issuer URL 的最后一段路径，因此两者必须匹配。

    > [!IMPORTANT]
    > Kanidm 使用 ES256 而非 RS256 对 ID 令牌进行签名。Trilium 在 v0.105.0 及更高版本中会从提供商处检测到这一点，因此无需额外配置。**不要**运行 `kanidm system oauth2 warning-enable-legacy-crypto`，它会把客户端降级为 RS256 并完全禁用 ES256。在较旧的 Trilium 版本上，登录会失败并报错 `unexpected JWT alg`。

=== "Pocket ID"

    > [!IMPORTANT]
    > Pocket ID 是无密码的，登录需要 passkey。请先注册一个并确认你可以登录 Pocket ID 本身，_然后_再将 Trilium 切换到 OpenID Connect，否则你可能会发现自己无法在两端进行身份验证。

    1.  以管理员身份登录 Pocket ID，然后前往 _OIDC Clients_ → _Add OIDC Client_。
    2.  为其命名（例如 Trilium）。
    3.  将 _Callback URLs_ 设置为 `https://<server>/callback`，将 `<server>` 替换为你的 Trilium 实例的 URL。
    4.  保存，然后复制 _Client ID_、_Client Secret_ 和 _OIDC Discovery URL_。

    使用第 4 步中的值按如下方式调整 `config.ini`：

    ```
    [MultiFactorAuthentication]
    oauthBaseUrl=https://<server>
    oauthClientId=<ClientID>
    oauthClientSecret=<ClientSecret>
    oauthIssuerBaseUrl=<OIDCDiscoveryURL>
    oauthIssuerName=Pocket ID
    ```

    > [!NOTE]
    > Pocket ID 会给你一个以 `/.well-known/openid-configuration` 结尾的 _OIDC Discovery URL_。在 v0.105.0 及更高版本上，你可以原样粘贴它。在更早的版本上，请移除该后缀，只使用它之前的部分。

    > [!IMPORTANT]
    > Pocket ID 在首次启动时会生成一个 RS256 签名密钥，无需进一步配置即可使用。如果你将其轮换为 Ed25519（`pocket-id key-rotate --alg EdDSA --crv Ed25519`），ID 令牌将改用 EdDSA 签名。Trilium 在 v0.105.0 及更高版本中会自动检测到这一点；较旧的版本会失败并报错 `unexpected JWT alg received, expected RS256, got: EdDSA`。

=== "<span style="--tn-color:#e64d4d;color:#e64d4d;"><span class="tn-icon bx bx-x"></span> GitHub</span>"

    GitHub 不能用作身份提供商，因为它是普通的 OAuth 2.0 而非 OpenID Connect，因此会失败并报错 `OAUTH_RESPONSE_IS_NOT_CONFORM`。

=== "<span class="tn-icon bx bxl-google"></span> Google"

    1.  前往 [Google Cloud's Clients](https://console.cloud.google.com/auth/clients) 仪表板并选择 _Create client_。
    2.  对于 _Application type_，选择 _Web application_。
    3.  在 _Authorized redirect URIs_ 中，设置 `https://<server>/callback`。
    4.  点击 _Create_ 并复制 _Client ID_ 和 _Client secret_。

    按如下方式调整 `config.ini`，将 `<ClientID>` 和 `<ClientSecret>` 替换为最后一步中的值，并将 `<server>` 替换为你的 Trilium 实例的 URL。

    ```
    [MultiFactorAuthentication]
    oauthBaseUrl=https://<server>
    oauthClientId=<ClientID>
    oauthClientSecret=<ClientSecret>
    ```