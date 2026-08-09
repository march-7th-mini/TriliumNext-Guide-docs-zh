# 同步失败并返回 504 网关超时

同步有时可能需要很长时间来计算需要更新的项目。当在反向代理后面运行时，请求可能会超时。

解决方案是在代理级别增加超时时间。

## Nginx

将以下内容添加到配置文件中：

```nginx
proxy_connect_timeout 300;
proxy_send_timeout 300;
proxy_read_timeout 300;
send_timeout 300;
```

然后重启服务器。

有关 Nginx 设置的更多信息，请参阅 [Nginx 代理设置](../Installation%20%26%20Setup/Server%20Installation/2.%20Reverse%20proxy/Nginx.md)。

如果仍然不起作用，请尝试增加超时时间。