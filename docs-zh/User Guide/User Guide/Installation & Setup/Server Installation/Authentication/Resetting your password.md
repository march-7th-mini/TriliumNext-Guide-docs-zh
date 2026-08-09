# 重置密码
> [!IMPORTANT]
> 如果您忘记了密码：
> 
> *   没有密码，受保护的笔记将无法找回。
> *   未受保护的笔记可以恢复。

有两种方法，都需要访问运行您服务器的设备。

### 通过禁用身份验证

1.  参阅 <a class="reference-link" href="../Authentication.md">身份验证</a> 了解如何禁用身份验证。
2.  重启服务器。
3.  前往 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → 密码 → 重置密码。
4.  按照步骤 (1) 的相反顺序重新启用身份验证。
5.  重启服务器。
6.  使用新密码登录。

### 通过修改数据库

1.  访问[数据目录](../../Data%20directory.md)中的[数据库](../../../Advanced%20Usage/Database.md)文件。使用 SQLite 客户端（例如 [DB Browser](https://sqlitebrowser.org/)）打开 `document.db` 文件。
2.  执行以下查询：
    
    ```
    UPDATE options SET value = '77/twC5O00cuQgNC63VK32qOKKYwj21ev3jZDXoytVU=' WHERE name = 'passwordVerificationSalt';
    UPDATE options SET value = '710BMasZCAgibzIc07X4P9Q4TeBd4ONnqJOho+pWcBM=' WHERE name = 'passwordDerivedKeySalt';
    UPDATE options SET value = 'Eb8af1/T57b89lCRuS97tPEl4CwxsAWAU7YNJ77oY+s=' WHERE name = 'passwordVerificationHash';
    UPDATE options SET value = 'QpC8XoiYYeqHPtHKRtbNxfTHsk+pEBqVBODYp0FkPBa22tlBBKBMigdLu5GNX8Uu' WHERE name = 'encryptedDataKey';
    ```
3.  执行更改后，提交/写入更改。**这会将密码设置为** `**password**`**，允许您重新登录。**
4.  前往 <a class="reference-link" href="../../../Basic%20Concepts%20and%20Features/UI%20Elements/Options.md">选项</a> → _密码_ → _更改密码_ 并替换不安全的密码。

## 处理受保护的笔记

当密码被重置时，受保护的笔记将永久丢失，因为它们使用您的密码进行加密，Trilium 无法恢复它们。

对于之前存在的受保护笔记（现在无法恢复），请考虑删除它们或导出未受保护的笔记。然后，删除 `document.db` 并重新开始。