# 使用各种提供商进行设置

> [!NOTE]
> 本页面包含如何使用各种提供商（如 Authelia、GitLab、Google）设置<a class="reference-link" href="../Signing%20in%20with%20OpenID%20Connect.md">使用 OpenID Connect 登录</a>的说明。请注意，虽然配置参考是正确且最新的，但创建 OAuth 应用程序的步骤可能会因提供商更改其界面而略有不同。

## Authelia

1.  生成客户端密钥：
    
    ```
    authelia crypto hash generate pbkdf2 --variant sha512 --random --random.length 72 --random.charset rfc3986
    
    ```
    
    `Random Password` 填入 Trilium，`Digest`（`$pbkdf2-sha512$…` 字符串）填入 Authelia。
2.  在 Authelia 的 `configuration.yml` 中的 `identity_providers.oidc.clients` 下添加客户端，将 `<server>` 替换为您的 Trilium 实例的 URL：
    
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
    
    与 GitLab 不同，`client_id` 是您选择的名称，而不是提供商生成的名称。
3.  重启 Authelia。

调整 `config.ini`，使用步骤 1 中的 `Random Password`：

```
[MultiFactorAuthentication]
oauthBaseUrl=https://<server>
oauthClientId=<ClientId>
oauthClientSecret=<RandomPassword>
oauthIssuerBaseUrl=https://<server>
oauthIssuerName=Authelia
```

> [!IMPORTANT]
> 不要为 Authelia 设置 `oauthClientAuthMethod`。它默认将机密客户端设为 `client_secret_basic`，并拒绝任何其他方法并返回 `invalid_client`，这正是 Trilium 默认使用的方式。这与下面的 GitLab 情况相反。

## GitLab（自托管或云）

1.  前往 [gitlab.com](https://gitlab.com/-/user_settings/applications) 或您自己的自托管实例上的用户设置。
2.  点击 _添加新应用程序_。
3.  为其命名（例如 Trilium）。
4.  将 _重定向 URI_ 设置为 `https://<server>/callback`
5.  确保 _机密_ 已勾选，且 _设备授权授权_ 未勾选。
6.  在范围内，勾选 _openid_、_profile_ 和 _email_（它们应该靠近列表末尾）。
7.  保存应用程序并复制 _应用程序 ID_ 和 _密钥_。

按如下方式调整 `config.ini`，将 `<ApplicationId>` 和 `<Secret>` 替换为最后一步中的值，并将 `<server>` 替换为您的 Trilium 实例的 URL。

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
> 如果您使用的是 GitLab 的自托管实例，请确保同时更新 `oauthIssuerBaseUrl`，并保留上面的 `oauthClientAuthMethod` 行。
> 
> GitLab 的令牌端点不会解码通过 HTTP Basic 发送的凭据，因此如果没有 `oauthClientAuthMethod`，登录将失败并显示 `server responded with a challenge in the WWW-Authenticate HTTP Header` 错误。Trilium 会自动为 `gitlab.com` 应用此设置，但无法检测自托管的签发者 URL。

## Kanidm

1.  创建客户端，添加重定向 URL 并授予范围，将 `<server>` 替换为您的 Trilium 实例的 URL，将 `<group>` 替换为现有 Kanidm 组的名称，该组的成员可以登录：
    
    ```
    kanidm system oauth2 create trilium "Trilium" "https://<server>"
    kanidm system oauth2 add-redirect-url trilium "https://<server>/callback"
    kanidm system oauth2 update-scope-map trilium <group> openid profile email
    ```
    
    `openid` 范围是必需的；没有它，Kanidm 会将客户端视为普通的 OAuth 2.0。
2.  读取客户端密钥：
    
    ```
    kanidm system oauth2 show-basic-secret trilium
    ```

按如下方式调整 `config.ini`，将 `<idm>` 替换为您的 Kanidm 实例的 URL，将 `<BasicSecret>` 替换为步骤 2 中的值：

```
[MultiFactorAuthentication]
oauthBaseUrl=https://<server>
oauthClientId=trilium
oauthClientSecret=<BasicSecret>
oauthIssuerBaseUrl=https://<idm>/oauth2/openid/trilium
oauthIssuerName=Kanidm
```

您在步骤 1 中选择的客户端名称既是客户端 ID，也是签发者 URL 的最后一个路径段，因此两者必须匹配。

> [!IMPORTANT]
> Kanidm 使用 ES256（而非 RS256）对 ID 令牌进行签名。Trilium 在 v0.105.0 及更高版本中会从提供商处检测到此情况，因此无需额外配置。不要运行 `kanidm system oauth2 warning-enable-legacy-crypto`，它会将客户端降级为 RS256 并完全禁用 ES256。在较旧的 Trilium 版本上，登录将失败并显示 `unexpected JWT alg` 错误。

## Pocket ID

> [!IMPORTANT]
> Pocket ID 是无密码的，登录需要通行密钥。在将 Trilium 切换到 OpenID Connect 之前，请先注册一个通行密钥并确认您可以登录 Pocket ID 本身，否则您可能会发现自己无法在任一端进行身份验证。

1.  以管理员身份登录 Pocket ID，然后前往 _OIDC 客户端_ → _添加 OIDC 客户端_。
2.  为其命名（例如 Trilium）。
3.  将 _回调 URL_ 设置为 `https://<server>/callback`，将 `<server>` 替换为您的 Trilium 实例的 URL。
4.  保存，然后复制 _客户端 ID_、_客户端密钥_ 和 _OIDC 发现 URL_。

按如下方式调整 `config.ini`，使用步骤 4 中的值：

```
[MultiFactorAuthentication]
oauthBaseUrl=https://<server>
oauthClientId=<ClientID>
oauthClientSecret=<ClientSecret>
oauthIssuerBaseUrl=<OIDCDiscoveryURL>
oauthIssuerName=Pocket ID
```

> [!NOTE]
> Pocket ID 会为您提供一个以 `/.well-known/openid-configuration` 结尾的 _OIDC 发现 URL_。在 v0.105.0 及更高版本中，您可以直接粘贴。在较早版本中，请删除该后缀，仅使用其前面的部分。

> [!IMPORTANT]
> Pocket ID 在首次启动时生成 RS256 签名密钥，无需进一步配置即可使用。如果您将其轮换为 Ed25519（`pocket-id key-rotate --alg EdDSA --crv Ed25519`），则 ID 令牌将改用 EdDSA 签名。Trilium 在 v0.105.0 及更高版本中会自动检测到此情况；旧版本将失败并显示 `unexpected JWT alg received, expected RS256, got: EdDSA`。

## GitHub

GitHub 不能用作身份提供商，因为它是普通的 OAuth 2.0 而非 OpenID Connect，因此会失败并显示 `OAUTH_RESPONSE_IS_NOT_CONFORM`。

## Google

1.  前往 [Google Cloud 的客户端](https://console.cloud.google.com/auth/clients) 仪表板，然后选择 _创建客户端_。
2.  对于 _应用程序类型_，选择 _Web 应用程序_。
3.  在 _已授权的重定向 URI_ 中，设置 `https://<server>/callback`。
4.  点击 _创建_ 并复制 _客户端 ID_ 和 _客户端密钥_。

按如下方式调整 `config.ini`，将 `<ClientID>` 和 `<ClientSecret>` 替换为最后一步中的值，并将 `<server>` 替换为您的 Trilium 实例的 URL。

```
[MultiFactorAuthentication]
oauthBaseUrl=https://<server>
oauthClientId=<ClientID>
oauthClientSecret=<ClientSecret>
```