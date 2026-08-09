# user_data

包含用于双因素身份验证的用户信息。此表**不**用于多用户。

相关文件：

*   `apps/server/src/services/encryption/open_id_encryption.ts`

| 列名 | 数据类型 | 可空性 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `tmpID` | 整数 |  |  | 用户的顺序 ID。由于 Trilium 仅支持单用户，此值始终为零。 |
| `username` | 文本 |  |  | 从 OAuth 操作返回的用户名。 |
| `email` | 文本 |  |  | 从 OAuth 操作返回的电子邮件地址。 |
| `userIDEncryptedDataKey` | 文本 |  |  | 来自 OAuth 操作的用户主体标识符的加密哈希。 |
| `userIDVerificationHash` | 文本 |  |  | 来自 OAuth 操作的主体标识符的加盐哈希。 |
| `salt` | 文本 |  |  | 验证盐值。 |
| `derivedKey` | 文本 |  |  | 随机安全令牌。 |
| `isSetup` | 文本 |  | `"false"` | 指示用户是否已保存（`"true"`）。 |