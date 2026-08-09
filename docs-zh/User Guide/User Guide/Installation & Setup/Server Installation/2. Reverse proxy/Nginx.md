# Nginx

配置 Nginx 代理和 HTTPS。此处操作系统为 Ubuntu。

## 安装 Nginx

下载 Nginx 并移除 Apache2

```
sudo apt-get install nginx
sudo apt-get remove apache2
```

## 构建配置文件

1.  首先，创建配置文件：
    
    ```
    cd /etc/nginx/conf.d
    vim default.conf
    ```
2.  将下方所示内容填入文件，其中部分设置需要更改。然后你就可以享受强制 HTTPS 和代理带来的网络体验了。
    
    ```
    # 此部分配置你的 Trilium 服务器运行位置
    upstream trilium {
      zone trilium 64k;
      server 127.0.0.1:8080; # 如果使用非默认主机名和端口，请更改
      keepalive 2;
    }
    
    # 此部分用于代理和 HTTPS 配置
    server {
        listen 443 ssl;
        server_name trilium.example.net; #将 trilium.example.net 更改为你的域名（不带 HTTPS 或 HTTP）。
        ssl_certificate /etc/ssl/note/example.crt; #将 /etc/ssl/note/example.crt 更改为你的 crt 文件路径。
        ssl_certificate_key /etc/ssl/note/example.net.key; #将 /etc/ssl/note/example.net.key 更改为你的密钥文件路径。
        ssl_session_cache builtin:1000 shared:SSL:10m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers HIGH:!aNULL:!eNULL:!EXPORT:!CAMELLIA:!DES:!MD5:!PSK:!RC4;
        ssl_prefer_server_ciphers on;
        access_log /var/log/nginx/access.log; #检查 access.log 的路径，如果不适合你的文件，请更改
    
        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass http://trilium;
            proxy_read_timeout 90;
        }
    }
    
    # 此部分用于强制 HTTPS
    server {
        listen 80;
        server_name trilium.example.net; # 更改为你的域名
        return 301 https://$server_name$request_uri;
    }
    ```

## 在不同路径下提供服务

或者，如果你想在不同的路径下提供服务（例如，如果你想同时提供多个实例），请按如下方式更新 location 块：

*   将 location 更新为你想要的路径（如果你的 `proxy_pass` 不以斜杠结尾，请确保不要留下尾随斜杠“/”）
*   添加具有相同路径的 `proxy_cookie_path` 指令：这允许你在多个实例上同时保持登录状态。

```
    location /trilium/instance-one {
        rewrite /trilium/instance-one/(.*) /$1  break;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass http://trilium;
        proxy_cookie_path / /trilium/instance-one
        proxy_read_timeout 90;
    }
```

## 配置受信任的代理

设置反向代理后，请确保配置 <a class="reference-link" href="Trusted%20proxy.md">受信任的代理</a>。