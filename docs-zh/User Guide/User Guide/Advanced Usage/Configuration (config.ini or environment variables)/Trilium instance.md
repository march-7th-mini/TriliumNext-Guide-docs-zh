# Trilium 实例

Trilium 实例代表一个服务器。如果已设置<a class="reference-link" href="../../Installation%20%26%20Setup/Synchronization.md">同步</a>，由于涉及多个服务器（桌面客户端的服务器和用于同步的服务器），有时区分您正在运行的实例会很有用。

## 设置实例名称

要为实例设置名称，请修改 `config.ini`：

```
[General]
instanceName=Hello
```

## 在后端区分实例

使用 `api.getInstanceName()` 获取当前服务器的实例名称，该名称在配置文件或环境变量中指定。

## 根据实例限制脚本运行

对于定期运行或由特定事件触发的脚本，可以将其限制在特定实例上运行，而无需修改代码。只需添加 `runOnInstance` 标签，并将值设置为脚本应运行的实例名称。要在多个命名实例上运行，只需多次添加该标签。