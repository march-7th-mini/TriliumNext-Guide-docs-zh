# 使用 Docker 的 Apache

本教程假设您已经为 `trilium.yourdomain.com` 创建了 DNS A 记录，并希望将其用于您的 Trilium 服务器。

## Docker 设置

下载 Docker 镜像并创建容器

```
 docker pull triliumnext/trilium:[VERSION]
 docker create --name trilium -t -p 127.0.0.1:8080:8080 -v ~/trilium-data:/home/node/trilium-data triliumnext/trilium:[VERSION]
```

## 配置 Apache 代理

1.  启用 Apache 代理模块
    
    ```
     a2enmod ssl
     a2enmod proxy
     a2enmod proxy_http
     a2enmod proxy_wstunnel
    ```
2.  创建新的 Let's Encrypt 证书
    
    ```
     sudo certbot certonly -d trilium.mydomain.com
    ```
    
    选择 standalone (2) 并记下所创建证书的位置（通常为 /etc/letsencrypt/live/...）
3.  为 Apache 创建新的虚拟主机文件（您可能希望使用 `apachectl -S` 来确定服务器根目录的位置，我的是 /etc/apache2）
    
    ```
     sudo nano /etc/apache2/sites-available/trilium.yourdomain.com.conf
    ```
    
    将以下文本粘贴（并自定义）到配置文件中
    
    ```
     
         ServerName http://trilium.yourdomain.com
         RewriteEngine on
             RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,QSA,R=permanent]
     
     
         ServerName https://trilium.yourdomain.com
         RewriteEngine On
         RewriteCond %{HTTP:Connection} Upgrade [NC]
         RewriteCond %{HTTP:Upgrade} websocket [NC]
         RewriteRule /(.*) ws://localhost:8080/$1 [P,L]
         AllowEncodedSlashes NoDecode
         ProxyPass / http://localhost:8080/ nocanon
         ProxyPassReverse / http://localhost:8080/
         SSLCertificateFile /etc/letsencrypt/live/trilium.yourdomain.com/fullchain.pem
         SSLCertificateKeyFile /etc/letsencrypt/live/trilium.yourdomain.com/privkey.pem
         Include /etc/letsencrypt/options-ssl-apache.conf
     
    ```
4.  使用 `sudo a2ensite trilium.yourdomain.com.conf` 启用虚拟主机
5.  使用 `sudo systemctl reload apache2` 重新加载 Apache2

## 配置受信任的代理

设置反向代理后，请确保配置 <a class="reference-link" href="Trusted%20proxy.md">受信任的代理</a>。

## 设置 systemd 服务以启动服务器

创建并启用一个 systemd 服务，以便在启动时启动 Docker 容器

1.  创建一个名为 `/lib/systemd/system/trilium.service` 的新空文件，内容如下
    
    ```
     [Unit]
     Description=Trilium Server
     Requires=docker.service
     After=docker.service
    
     [Service]
     Restart=always
     ExecStart=/usr/bin/docker start -a trilium
     ExecStop=/usr/bin/docker stop -t 2 trilium
    
     [Install]
     WantedBy=local.target
    ```
2.  安装、启用并启动服务
    
    ```
     sudo systemctl daemon-reload
     sudo systemctl enable trilium.service
     sudo systemctl start trilium.service
    ```