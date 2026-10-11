# 配置（config.ini 或环境变量）
Trilium 支持通过名为 `config.ini` 的文件和环境变量进行配置。本文档提供了所有配置选项的完整参考。

## 配置文件的位置

配置文件并不位于应用程序所在的目录中。相反，`config.ini` 位于 <a class="reference-link" href="../Installation%20%26%20Setup/Data%20directory.md">数据目录</a> 中。因此，配置文件只有在启动应用程序并创建数据库后才可用。

## 配置优先级

配置值按以下优先级顺序加载（从高到低）：

1.  **环境变量**（首先检查）
2.  **config.ini 文件值**
3.  **默认值**

## 环境变量模式

Trilium 支持多种环境变量模式以提供灵活性。主要模式为：`TRILIUM_[SECTION]_[KEY]`

其中：

*   `SECTION` 是大写的 INI 节名称
*   `KEY` 是转换为大写的 camelCase 配置键（例如，`instanceName` → `INSTANCENAME`）

此外，常见配置还提供了更短的别名（请参阅下方的替代变量部分）。

## 环境变量参考

=== "General"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_GENERAL_INSTANCENAME` | string | "" | 用于 API 识别的实例名称 |
    | `TRILIUM_GENERAL_NOAUTHENTICATION` | boolean | false | 禁用身份验证（仅限服务器） |
    | `TRILIUM_GENERAL_NOBACKUP` | boolean | false | 禁用自动备份 |
    | `TRILIUM_GENERAL_NODESKTOPICON` | boolean | false | 禁用桌面图标创建 |
    | `TRILIUM_GENERAL_READONLY` | boolean | false | 启用只读模式 |

=== "Network"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_NETWORK_HOST` | string | "0.0.0.0" | 服务器主机绑定 |
    | `TRILIUM_NETWORK_PORT` | string | "8080" | 服务器端口 |
    | `TRILIUM_NETWORK_HTTPS` | boolean | false | 启用 HTTPS |
    | `TRILIUM_NETWORK_CERTPATH` | string | "" | SSL 证书路径 |
    | `TRILIUM_NETWORK_KEYPATH` | string | "" | SSL 密钥路径 |
    | `TRILIUM_NETWORK_TRUSTEDREVERSEPROXY` | boolean/string | false | 反向代理信任设置 |
    | `TRILIUM_NETWORK_CORSALLOWORIGIN` | string | "" | CORS 允许的来源 |
    | `TRILIUM_NETWORK_CORSALLOWMETHODS` | string | "" | CORS 允许的方法 |
    | `TRILIUM_NETWORK_CORSALLOWHEADERS` | string | "" | CORS 允许的标头 |
    | `TRILIUM_NETWORK_CORSRESOURCEPOLICY` | string | same-origin | CORS 资源策略允许 same-origin/same-site/cross-origin 作为值，否则将报错 |

=== "Session"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_SESSION_COOKIEMAXAGE` | integer | 1814400 | 会话 cookie 最大有效期（秒）（21 天） |

=== "Sync"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_SYNC_SYNCSERVERHOST` | string | "" | 同步服务器主机 URL |
    | `TRILIUM_SYNC_SYNCSERVERTIMEOUT` | string | "120000" | 同步服务器超时时间（毫秒） |
    | `TRILIUM_SYNC_SYNCPROXY` | string | "" | 同步代理 URL |

=== "MultiFactorAuthentication"

    请参阅 <a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation/Signing%20in%20with%20OpenID%20Connect.md">使用 OpenID Connect 登录</a>。

=== "Logging"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_LOGGING_RETENTIONDAYS` | integer | 90 | 保留日志文件的天数 |

=== "Development"

    | 环境变量 | 类型 | 默认值 | 描述 |
    | --- | --- | --- | --- |
    | `TRILIUM_MANUAL_DB_MIGRATION` | boolean | false | 如果为 `true`，当自动数据库迁移待处理且会修改数据库架构时，应用程序将不会启动。 |

<details>
    <summary>替代环境变量</summary>
    <p>以下替代环境变量名称也受支持，并且与其较长的对应变量作用完全相同。</p>
    <div class="trilium-tabs"><section class="trilium-tab"><p class="trilium-tab-title">Network CORS</p><div class="trilium-tab-panel"><ul><li><code>TRILIUM_NETWORK_CORS_ALLOW_ORIGIN</code>（<code>TRILIUM_NETWORK_CORSALLOWORIGIN</code> 的替代）</li><li><code>TRILIUM_NETWORK_CORS_ALLOW_METHODS</code>（<code>TRILIUM_NETWORK_CORSALLOWMETHODS</code> 的替代）</li><li><code>TRILIUM_NETWORK_CORS_ALLOW_HEADERS</code>（<code>TRILIUM_NETWORK_CORSALLOWHEADERS</code> 的替代）</li><li><code>TRILIUM_NETWORK_CORS_RESOURCE_POLICY</code>（<code>TRILIUM_NETWORK_CORSRESOURCEPOLICY</code> 的替代）</li></ul></div></section><section class="trilium-tab"><p class="trilium-tab-title">Sync</p><div class="trilium-tab-panel"><ul><li><code>TRILIUM_SYNC_SERVER_HOST</code>（<code>TRILIUM_SYNC_SYNCSERVERHOST</code> 的替代）</li><li><code>TRILIUM_SYNC_SERVER_TIMEOUT</code>（<code>TRILIUM_SYNC_SYNCSERVERTIMEOUT</code> 的替代）</li><li><code>TRILIUM_SYNC_SERVER_PROXY</code>（<code>TRILIUM_SYNC_SYNCPROXY</code> 的替代）</li></ul></div></section><section class="trilium-tab"><p class="trilium-tab-title">OAuth/MFA</p><div class="trilium-tab-panel"><ul><li><code>TRILIUM_OAUTH_BASE_URL</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL</code> 的替代）</li><li><code>TRILIUM_OAUTH_CLIENT_ID</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTID</code> 的替代）</li><li><code>TRILIUM_OAUTH_CLIENT_SECRET</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTSECRET</code> 的替代）</li><li><code>TRILIUM_OAUTH_ISSUER_BASE_URL</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERBASEURL</code> 的替代）</li><li><code>TRILIUM_OAUTH_ISSUER_NAME</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERNAME</code> 的替代）</li><li><code>TRILIUM_OAUTH_ISSUER_ICON</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERICON</code> 的替代）</li><li><code>TRILIUM_OAUTH_HTTP_TIMEOUT</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHHTTPTIMEOUT</code> 的替代）</li><li><code>TRILIUM_OAUTH_SCOPE</code>（<code>TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHSCOPE</code> 的替代）</li></ul></div></section><section class="trilium-tab"><p class="trilium-tab-title">Logging</p><div class="trilium-tab-panel"><ul><li><code>TRILIUM_LOGGING_RETENTION_DAYS</code>（<code>TRILIUM_LOGGING_RETENTIONDAYS</code> 的替代）</li></ul></div></section></div>
</details>

## 布尔值

布尔环境变量接受以下值：

*   **True**：`"true"`、`"1"`、`1`
*   **False**：`"false"`、`"0"`、`0`
*   任何其他值默认为 `false`

## 使用环境变量

两种命名模式均完全支持，可以互换使用：

*   较长的格式遵循节/键模式，以与 INI 文件结构保持一致
*   较短的替代格式为常见配置提供了便利
*   您可以使用您偏好的任何格式——两者同样有效

## 示例

=== "<span class="tn-icon bx bxl-docker"></span> Docker Compose"

    ```yaml
    services:
      trilium:
        image: triliumnext/trilium
        environment:
          # Using full format
          TRILIUM_GENERAL_INSTANCENAME: "My Trilium Instance"
          TRILIUM_NETWORK_PORT: "8080"
          TRILIUM_NETWORK_CORSALLOWORIGIN: "https://myapp.com"
          TRILIUM_SYNC_SYNCSERVERHOST: "https://sync.example.com"
          TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL: "https://auth.example.com"
          
          # Or using shorter alternatives (equally valid)
          # TRILIUM_NETWORK_CORS_ALLOW_ORIGIN: "https://myapp.com"
          # TRILIUM_SYNC_SERVER_HOST: "https://sync.example.com"
          # TRILIUM_OAUTH_BASE_URL: "https://auth.example.com"
    ```

=== "<span class="tn-icon bx bxl-tux"></span> Linux Shell"

    ```
    # Using either format
    export TRILIUM_GENERAL_NOAUTHENTICATION=false
    export TRILIUM_NETWORK_HTTPS=true
    export TRILIUM_NETWORK_CERTPATH=/path/to/cert.pem
    export TRILIUM_NETWORK_KEYPATH=/path/to/key.pem
    export TRILIUM_LOGGING_RETENTIONDAYS=30

    # Start Trilium
    npm start
    ```

## config.ini 参考

有关配置选项的完整列表及其 INI 文件格式，请查看 Trilium 仓库中的 [config-sample.ini](https://github.com/TriliumNext/Trilium/blob/main/apps/server/src/assets/config-sample.ini) 文件。