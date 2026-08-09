# HTTPS (TLS)

在 Trilium 中，配置 TLS 对于[服务器安装](../Server%20Installation.md)至关重要。本指南详细介绍了在 Trilium 中设置 TLS 的步骤。

> [!TIP]
> 虽然 Trilium 本身支持 HTTPS，但通常建议使用带有 TLS 终止的[反向代理](2.%20Reverse%20proxy.md)。您可以按照[此类指南](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)进行设置。

## 获取 TLS 证书

您有两种获取 TLS 证书的选项：

*   **推荐**：获取由根证书颁发机构签名的 TLS 证书。对于个人使用，[Let's Encrypt](https://letsencrypt.org) 是一个极好的选择。它免费、自动化且简单直接。Certbot 可以简化自动 TLS 设置。
*   生成自签名证书。由于需要将证书导入所有连接到服务器的机器，增加了额外的复杂性，因此不推荐此选项。

## 修改 `config.ini`

获得证书后，修改[数据目录](../Data%20directory.md)中的 `config.ini` 文件，以配置 Trilium 使用该证书：

```
[Network]
port=8080
# 设置为 true 以启用 TLS/SSL/HTTPS（安全），设置为 false 以使用 HTTP（不安全）。
https=true
# 证书路径（运行 "bash bin/generate-cert.sh" 可生成自签名证书）。
# 仅在 https=true 时相关
certPath=/[username]/.acme.sh/[hostname]/fullchain.cer
keyPath=/[username]/.acme.sh/[hostname]/example.com.key
```

您也可以查看[配置](../../Advanced%20Usage/Configuration%20\(config.ini%20or%20environment%20variables\).md)文件，将所有 `config.ini` 值作为环境变量提供。例如，您可以使用环境变量配置 TLS：

```
export TRILIUM_NETWORK_HTTPS=true
export TRILIUM_NETWORK_CERTPATH=/path/to/cert.pem
export TRILIUM_NETWORK_KEYPATH=/path/to/key.pem
```

上面的示例展示了在使用 Let's Encrypt 的 ACME 工具生成证书的环境中如何进行设置。您的路径可能不同。对于 Docker 安装，请确保这些路径位于 Docker 容器可访问的卷或其他目录中，例如 `/home/node/trilium-data/[DIR IN DATA DIRECTORY]`。

配置 `config.ini` 后，重启 Trilium 并使用 "https" 访问主机名。

## 自签名证书

如果您选择为服务器实例使用自签名证书，请注意桌面实例默认不会信任该证书。

要绕过此问题，请通过设置以下环境变量来禁用证书验证（适用于 Linux）：

```
export NODE_TLS_REJECT_UNAUTHORIZED=0
trilium
```

Trilium 提供了以这种模式启动的脚本，例如适用于 Windows 的 `trilium-no-cert-check.bat`。

**警告**：禁用 TLS 证书验证是不安全的。只有在完全理解其影响的情况下才继续操作。