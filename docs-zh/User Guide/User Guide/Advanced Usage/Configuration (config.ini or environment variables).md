# 配置（config.ini 或环境变量）

Trilium 支持通过名为 `config.ini` 的文件和环境变量进行配置。本文档提供了所有配置选项的全面参考。

## 配置文件的位置

配置文件与应用不在同一目录中。相反，`config.ini` 位于<a class="reference-link" href="../Installation%20%26%20Setup/Data%20directory.md">数据目录</a>中。因此，配置文件仅在启动应用并创建数据库后才可用。

## 配置优先级

配置值按以下优先级顺序加载（从高到低）：

1.  **环境变量**（首先检查）
2.  **config.ini 文件值**
3.  **默认值**

## 环境变量模式

Trilium 支持多种环境变量模式以提供灵活性。主要模式为：`TRILIUM_[SECTION]_[KEY]`

其中：

*   `SECTION` 是 INI 节名称，使用大写
*   `KEY` 是驼峰式配置键，转换为大写（例如，`instanceName` → `INSTANCENAME`）

此外，常用配置还有更短的别名可用（请参阅下面的备选变量部分）。

## 环境变量参考

### 常规部分

| 环境变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `TRILIUM_GENERAL_INSTANCENAME` | string | "" | 用于 API 标识的实例名称 |
| `TRILIUM_GENERAL_NOAUTHENTICATION` | boolean | false | 禁用身份验证（仅限服务器） |
| `TRILIUM_GENERAL_NOBACKUP` | boolean | false | 禁用自动备份 |
| `TRILIUM_GENERAL_NODESKTOPICON` | boolean | false | 禁用桌面图标创建 |
| `TRILIUM_GENERAL_READONLY` | boolean | false | 启用只读模式 |

### 网络部分

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

### 会话部分

| 环境变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `TRILIUM_SESSION_COOKIEMAXAGE` | integer | 1814400 | 会话 Cookie 最大有效期（秒）（21 天） |

### 同步部分

| 环境变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `TRILIUM_SYNC_SYNCSERVERHOST` | string | "" | 同步服务器主机 URL |
| `TRILIUM_SYNC_SYNCSERVERTIMEOUT` | string | "120000" | 同步服务器超时时间（毫秒） |
| `TRILIUM_SYNC_SYNCPROXY` | string | "" | 同步代理 URL |

### 多因素身份验证部分

请参阅<a class="reference-link" href="../Installation%20%26%20Setup/Server%20Installation/Signing%20in%20with%20OpenID%20Connect.md">使用 OpenID Connect 登录</a>。

### 日志部分

| 环境变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `TRILIUM_LOGGING_RETENTIONDAYS` | integer | 90 | 日志文件保留天数 |

### 开发部分

| 环境变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `TRILIUM_MANUAL_DB_MIGRATION` | boolean | false | 如果为 `true`，当存在待处理的自动数据库迁移且会修改数据库架构时，应用程序将不会启动。 |

## 备选环境变量

以下备选环境变量名称也受支持，并且与其较长的对应项功能相同：

### 网络 CORS 变量

*   `TRILIUM_NETWORK_CORS_ALLOW_ORIGIN`（`TRILIUM_NETWORK_CORSALLOWORIGIN` 的备选）
*   `TRILIUM_NETWORK_CORS_ALLOW_METHODS`（`TRILIUM_NETWORK_CORSALLOWMETHODS` 的备选）
*   `TRILIUM_NETWORK_CORS_ALLOW_HEADERS`（`TRILIUM_NETWORK_CORSALLOWHEADERS` 的备选）
*   `TRILIUM_NETWORK_CORS_RESOURCE_POLICY`（`TRILIUM_NETWORK_CORSRESOURCEPOLICY` 的备选）

### 同步变量

*   `TRILIUM_SYNC_SERVER_HOST`（`TRILIUM_SYNC_SYNCSERVERHOST` 的备选）
*   `TRILIUM_SYNC_SERVER_TIMEOUT`（`TRILIUM_SYNC_SYNCSERVERTIMEOUT` 的备选）
*   `TRILIUM_SYNC_SERVER_PROXY`（`TRILIUM_SYNC_SYNCPROXY` 的备选）

### OAuth/MFA 变量

*   `TRILIUM_OAUTH_BASE_URL`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL` 的备选）
*   `TRILIUM_OAUTH_CLIENT_ID`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTID` 的备选）
*   `TRILIUM_OAUTH_CLIENT_SECRET`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHCLIENTSECRET` 的备选）
*   `TRILIUM_OAUTH_ISSUER_BASE_URL`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERBASEURL` 的备选）
*   `TRILIUM_OAUTH_ISSUER_NAME`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERNAME` 的备选）
*   `TRILIUM_OAUTH_ISSUER_ICON`（`TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHISSUERICON` 的备选）

### 日志变量

*   `TRILIUM_LOGGING_RETENTION_DAYS`（`TRILIUM_LOGGING_RETENTIONDAYS` 的备选）

## 布尔值

布尔环境变量接受以下值：

*   **真**：`"true"`、`"1"`、`1`
*   **假**：`"false"`、`"0"`、`0`
*   任何其他值默认为 `false`

## 使用环境变量

两种命名模式均完全受支持，可以互换使用：

*   较长的格式遵循节/键模式，与 INI 文件结构保持一致
*   较短的备选形式为常见配置提供了便利
*   您可以使用任何一种您喜欢的格式——两者同样有效

## 示例

### Docker Compose 示例

```yaml
services:
  trilium:
    image: triliumnext/trilium
    environment:
      # 使用完整格式
      TRILIUM_GENERAL_INSTANCENAME: "My Trilium Instance"
      TRILIUM_NETWORK_PORT: "8080"
      TRILIUM_NETWORK_CORSALLOWORIGIN: "https://myapp.com"
      TRILIUM_SYNC_SYNCSERVERHOST: "https://sync.example.com"
      TRILIUM_MULTIFACTORAUTHENTICATION_OAUTHBASEURL: "https://auth.example.com"
      
      # 或使用较短的备选形式（同样有效）
      # TRILIUM_NETWORK_CORS_ALLOW_ORIGIN: "https://myapp.com"
      # TRILIUM_SYNC_SERVER_HOST: "https://sync.example.com"
      # TRILIUM_OAUTH_BASE_URL: "https://auth.example.com"
```

### Shell 导出示例

```
# 使用任一格式
export TRILIUM_GENERAL_NOAUTHENTICATION=false
export TRILIUM_NETWORK_HTTPS=true
export TRILIUM_NETWORK_CERTPATH=/path/to/cert.pem
export TRILIUM_NETWORK_KEYPATH=/path/to/key.pem
export TRILIUM_LOGGING_RETENTIONDAYS=30

# 启动 Trilium
npm start
```

## config.ini 参考

有关配置选项及其 INI 文件格式的完整列表，请查看 Trilium 仓库中的 [config-sample.ini](https://github.com/TriliumNext/Trilium/blob/main/apps/server/src/assets/config-sample.ini) 文件。